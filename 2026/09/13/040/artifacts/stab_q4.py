import itertools
import numpy as np
from collections import defaultdict
from math import factorial

# Sum-zero model V_k: basis u_i = e_i - e_{k-1}, i=0..k-2
# S_k action: sigma as tuple perm of 0..k-1 (image of indices: sigma acts on positions? We act on vectors by permuting coords: (sigma.x)_a = x_{sigma^{-1}(a)}? Or x -> permute basis e_i -> e_{sigma(i)}.
# Use e_i -> e_{sigma(i)} (left action). Then sigma.u_i = e_{sigma(i)} - e_{sigma(k-1)}.

def V_action_matrix(k, sigma):
    # sigma: tuple/list with sigma[i] = image of i
    d=k-1
    import numpy as np
    M=np.zeros((d,d),dtype=int)
    s_k_1 = sigma[k-1]
    # w_a = e_a - e_{k-1} = u_a if a<k-1 else 0
    # sigma.u_i = w_{sigma(i)} - w_{sigma(k-1)}
    # w_a = u_a if a<d else 0
    for i in range(d):
        si=sigma[i]
        # w_{si}
        col=np.zeros(d,dtype=int)
        if si<d:
            col[si]+=1
        # else 0
        # minus w_{s_{k-1}}
        if s_k_1<d:
            col[s_k_1]-=1
        # else minus 0
        M[:,i]=col
    return M

def wedge2(M):
    d=M.shape[0]
    pairs=[(i,j) for i in range(d) for j in range(i+1,d)]
    m=len(pairs)
    idx={p:i for i,p in enumerate(pairs)}
    W=np.zeros((m,m),dtype=int)
    for cj,(a,b) in enumerate(pairs):
        ca=M[:,a]; cb=M[:,b]
        for c in range(d):
            for dd in range(c+1,d):
                coeff=int(ca[c]*cb[dd]-ca[dd]*cb[c])
                if coeff:
                    W[idx[(c,dd)],cj]+=coeff
    return W,pairs

def Phi_V_matrix(k):
    # V_k (dim k-1) -> V_{k+1} (dim k): Phi(u_i)=u_i' - u_{k-1}' where u_j' = e_j - e_k
    d=k-1; dp=k
    P=np.zeros((dp,d),dtype=int)
    for i in range(d):
        # u_i' coefficient 1 at i, -1 at k-1
        P[i,i]+=1
        P[k-1,i]-=1
    return P

def Phi_W_matrix(k):
    P=Phi_V_matrix(k)
    dp,d=P.shape
    pairs_src=[(i,j) for i in range(d) for j in range(i+1,d)]
    pairs_tgt=[(i,j) for i in range(dp) for j in range(dp) if i<j]
    idx={p:i for i,p in enumerate(pairs_tgt)}
    m_src=len(pairs_src); m_tgt=len(pairs_tgt)
    PW=np.zeros((m_tgt,m_src),dtype=int)
    for cj,(a,b) in enumerate(pairs_src):
        ca=P[:,a]; cb=P[:,b]
        for c in range(dp):
            for dd in range(c+1,dp):
                coeff=int(ca[c]*cb[dd]-ca[dd]*cb[c])
                if coeff:
                    PW[idx[(c,dd)],cj]+=coeff
    return PW

# Test S action valid: check transposition order 2, etc.
for k in [3,4,5]:
    # gens
    import random
    # check homomorphism on two perms
    def compose(s,t): # apply t then s? e_i -> e_t(i) -> e_s(t(i))
        return tuple(s[t[i]] for i in range(k))
    for _ in range(20):
        a=list(range(k)); b=list(range(k))
        np.random.shuffle(a); np.random.shuffle(b)
        A=V_action_matrix(k,tuple(a)); B=V_action_matrix(k,tuple(b))
        C=V_action_matrix(k,compose(a,b))
        assert np.array_equal(A@B,C), f"fail k={k}"
print("V action homomorphism ok")
# Check wedge dims and coinvariant dims with new model
import sympy as sp
def coinv_dim(k):
    d=k-1; m=d*(d-1)//2
    if m==0: return 0
    # gens of S_k: adjacent transpositions
    gens=[]
    for i in range(k-1):
        p=list(range(k)); p[i],p[i+1]=p[i+1],p[i]; gens.append(tuple(p))
    rows=[]
    for g in gens:
        M=V_action_matrix(k,g)
        W,_=wedge2(M)
        G=sp.Matrix(W.tolist())-sp.eye(m)
        for r in range(m):
            rows.append(list(G[r,:]))
    A=sp.Matrix(rows)
    return m-A.rank()
for k in [3,4,5,6]:
    print(k, coinv_dim(k))

# Build A4 bases and S actions for G part
def build_A4(k):
    # basis: pt_i (k), A_ij/B_ij? Use types: 'P',i ; ('A',i,j) i<j ; ('B',i,j); ('C',i,j) ordered? Wait A4: pt_i, a_ia_j? Actually need:
    # - pt_i
    # - a_i a_j (i<j), b_i b_j, a_i b_j (i!=j? ordered? a_i b_j for i!=j includes both orders? For i<j, a_i b_j and a_j b_i distinct? plus a_i b_i? a_i b_i with same index: a*b=0 in same factor, so zero! So only i!=j, and ordered pairs? Since a_i b_j with i!=j: ordered (i,j), i!=j. Number k(k-1).
    # Similarly a_i a_j (i<j), b_i b_j.
    idx={}; lst=[]
    for i in range(k):
        idx[('P',i)]=len(lst); lst.append(('P',i))
    for i in range(k):
        for j in range(i+1,k):
            idx[('A',i,j)]=len(lst); lst.append(('A',i,j))
    for i in range(k):
        for j in range(i+1,k):
            idx[('B',i,j)]=len(lst); lst.append(('B',i,j))
    for i in range(k):
        for j in range(k):
            if i==j: continue
            idx[('C',i,j)]=len(lst); lst.append(('C',i,j))
    return idx,lst

def permute_A4(k, sigma, idx, lst):
    # sigma acts on positions: pt_i -> pt_{sigma(i)}, a_i a_j -> a_{s(i)}a_{s(j)} (symmetric, order), etc.
    n=len(lst)
    # return permutation matrix as dict perm: new_index of each old? Build matrix P where (P v)[new]=v[old]? For action on vectors: (sigma.v)_{basis element with labels} = v_{sigma^{-1} labels}? If we use e_i -> e_{sigma(i)}, then basis element labelled by positions S maps to labels sigma(S). So matrix with rows new, cols old: P[sigma(b), b]=1.
    perm=[None]*n
    for old,key in enumerate(lst):
        if key[0]=='P':
            new=idx[('P',sigma[key[1]])]
        elif key[0] in ('A','B'):
            a,b=key[1],key[2]
            sa,sb=sigma[a],sigma[b]
            if sa>sb: sa,sb=sb,sa
            new=idx[(key[0],sa,sb)]
        elif key[0]=='C':
            new=idx[('C',sigma[key[1]],sigma[key[2]])]
        perm[old]=new
    return perm

def apply_perm_to_tensor_A4W(k, sigma, vec, Aidx, Alst, wpairs, widx):
    # vec flat: [a*nW + w]
    nA=len(Alst); nW=len(wpairs)
    M=V_action_matrix(k,sigma)
    W,_=wedge2(M)
    perm=permute_A4(k,sigma,Aidx,Alst)
    out=np.zeros_like(vec)
    # out[new_a, new_w] = sum_{old} ... Actually action: (sigma.(a tensor w)) = sigma(a) tensor sigma(w)
    # vec indexed (a,w). out[perm[a], W w] = vec[a,w]
    # So out = (P_A \otimes W) vec
    # Compute via loops
    # Reshape
    V=vec.reshape(nA,nW)
    # First apply W on rows? out1[a, :] = V[a,:] @ W.T? Since new_w = sum_old W[new,old] V[a,old]
    T=V@np.array(W).T  # nA x nW (int)
    out2=np.zeros_like(V)
    for a in range(nA):
        out2[perm[a],:]+=T[a,:]
    return out2.reshape(-1)

def orbit_sum(k, rep_a_key, rep_w_pair):
    Aidx,Alst=build_A4(k)
    # sum-zero W basis pairs
    d=k-1
    wpairs=[(i,j) for i in range(d) for j in range(i+1,d)]
    widx={p:i for i,p in enumerate(wpairs)}
    nA=len(Alst); nW=len(wpairs)
    N=nA*nW
    # start vector e_{rep} then average over group? For invariant projection we can orbit-sum over all perms? |S_k| huge. Instead use random/stabilizer orbit enumeration via support? Use support-based enumeration as before but with new models.
    # General orbit sum: sum over cosets of stabilizer? Equivalent to sum over distinct images under S_k: sum over injective maps of support as before.
    # Determine support labels: rep uses abstract labels; we need to map abstract support set to 0..k-1 injectively and compute image term (G-part image + W-part image with V action of partial injection?).
    # W-part: rep_w_pair = (p,q) abstract V indices? Abstract V indices are differences e_x - e_{r}? Hmm abstract labels for W in sum-zero model are more subtle: basis u depends on distinguished last index (k-1). Abstract rep should be expressed in terms of e-differences, which are canonical (e_x - e_y), independent of basis choice.
    # Better: represent W basis elements as e_x ^ e_y? Alternative canonical model: V_k = {sum zero} subset Q^k, W = Lambda^2 V. But Lambda^2 V can be identified with ...? Basis elements (e_a - e_b)^(e_c - e_d)? Might be messy.
    # Alternative: use symmetric description: V = span{e_i - e_0}? Hmm.
    # Simpler: compute invariants via Reynolds over full group using random averaging + rank? For k<=7, |S_k|=5040 manageable to sum over all perms explicitly with sparse vectors? N~ (nA~? for k=6: nA=6+15+15+30=66, nW=10, N=660). Summing over 720 perms with matrix apply O(N) each => 720*660 ~ 475k ops per orbit sum, fine. For k=7: 5040*1365 ~ 6.8M, ok. For k=8: 40320*2520 ~ 100M, heavy but maybe ok for few reps in python? Might be slow.
    # Use full-group averaging for k<=7.
    pass
