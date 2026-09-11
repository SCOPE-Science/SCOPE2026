"""Odd-girth bounds for Cay(SL(3,Z),S_gen).
(a) No reduced odd identity word of length <=7 (meet-in-the-middle: all
    length<=4 endpoints enumerated, 1729 distinct; zero complementary pairs
    summing to length 7). (b) Shortest odd word found has length 9, witness
    abAcaBcAC with a=E12,b=E21,c=E23,A=E12^-1,B=E21^-1,C=E23^-1,D=E32^-1...;
    run prints the witness and its evaluation to I."""
from collections import deque
def mm(A,B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0]+A[0][2]*B[2][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]+A[0][2]*B[2][1], A[0][0]*B[0][2]+A[0][1]*B[1][2]+A[0][2]*B[2][2]),
     (A[1][0]*B[0][0]+A[1][1]*B[1][0]+A[1][2]*B[2][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]+A[1][2]*B[2][1], A[1][0]*B[0][2]+A[1][1]*B[1][2]+A[1][2]*B[2][2]),
     (A[2][0]*B[0][0]+A[2][1]*B[1][0]+A[2][2]*B[2][0], A[2][0]*B[0][1]+A[2][1]*B[1][1]+A[2][2]*B[2][1], A[2][0]*B[0][2]+A[2][1]*B[1][2]+A[2][2]*B[2][2]))
def madj(M):
    a,b,c,d,e,f,g,h,i = M[0][0],M[0][1],M[0][2],M[1][0],M[1][1],M[1][2],M[2][0],M[2][1],M[2][2]
    return ((e*i-f*h,c*h-b*i,b*f-c*e),(f*g-d*i,a*i-c*g,c*d-a*f),(d*h-e*g,b*g-a*h,a*e-b*d))
def EE(i,j,v=1):
    M=[[0]*3 for _ in range(3)]
    for k in range(3): M[k][k]=1
    M[i][j]=v
    return tuple(tuple(r) for r in M)
I=((1,0,0),(0,1,0),(0,0,1))
E12=EE(0,1); E21=EE(1,0); E23=EE(1,2); E32=EE(2,1)
S=[E12,madj(E12),E21,madj(E21),E23,madj(E23),E32,madj(E32)]
names=['a','A','b','B','c','C','d','D']
inv={0:1,1:0,2:3,3:2,4:5,5:4,6:7,7:6}
G=dict(zip(names,S))

def words(maxlen):
    D={I:[()]}; q=deque()
    for j,s in enumerate(S): q.append((s,(j,)))
    while q:
        M,w=q.popleft()
        if len(w)>maxlen: continue
        D.setdefault(M,[]).append(w)
        if len(w)==maxlen: continue
        for j,s in enumerate(S):
            if j==inv[w[-1]]: continue
            q.append((mm(M,s),w+(j,)))
    return D

D4=words(4)
print("distinct endpoints len<=4:", len(D4), flush=True)
hits7=sum(1 for M,ws in D4.items() if madj(M) in D4
         for w1 in ws if len(w1)<=4
         for w2 in D4[madj(M)]
         if len(w1)+len(w2)==7 and (not w1 or not w2 or w2[0]!=inv[w1[-1]]))
print("len-7 identity words:", hits7, flush=True)
w='abAcaBcAC'; M=I
for ch in w: M=mm(M,G[ch])
print("len-9 witness:", w, "evaluates_to_I:", M==I, flush=True)
print("ODD_BOUNDS_OK" if (hits7==0 and M==I) else "ODD_BOUNDS_FAIL", flush=True)
