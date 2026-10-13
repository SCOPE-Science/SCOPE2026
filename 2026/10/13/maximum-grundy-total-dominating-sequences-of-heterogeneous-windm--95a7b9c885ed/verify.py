from itertools import product, combinations
from math import comb, factorial


def graph(profile):
    blades=[]
    idx=1
    for m in profile:
        B=list(range(idx,idx+m)); idx+=m; blades.append(B)
    N=idx
    neigh=[0]*N
    for B in blades:
        for v in B:
            neigh[0] |= 1<<v
            neigh[v] |= 1<<0
        for a,b in combinations(B,2):
            neigh[a] |= 1<<b
            neigh[b] |= 1<<a
    return neigh,blades


def predicted_set(mask, blades):
    center=bool(mask&1)
    counts=[sum((mask>>v)&1 for v in B) for B in blades]
    if not center:
        return all(c==2 for c in counts)
    return counts.count(1)==1 and all(c in (1,2) for c in counts) and counts.count(2)==len(blades)-1


def verify_profile(profile):
    neigh,blades=graph(profile)
    N=len(neigh); ALL=(1<<N)-1
    dom=[0]*(1<<N)
    legal_orders=[0]*(1<<N)
    legal_orders[0]=1
    for mask in range(1,1<<N):
        lsb=mask & -mask
        v=lsb.bit_length()-1
        dom[mask]=dom[mask^lsb] | neigh[v]
    append_checks=0
    for mask in range(1,1<<N):
        total=0
        x=mask
        while x:
            bit=x & -x; x-=bit
            v=bit.bit_length()-1
            prev=mask^bit
            append_checks += 1
            if legal_orders[prev] and (neigh[v] & ~dom[prev]):
                total += legal_orders[prev]
        legal_orders[mask]=total
    td_masks=[m for m in range(1,1<<N) if dom[m]==ALL and legal_orders[m]]
    maxlen=max(m.bit_count() for m in td_masks)
    max_masks=[m for m in td_masks if m.bit_count()==maxlen]
    r=len(profile)
    assert maxlen==2*r, (profile,maxlen)
    classification_checks=0
    for mask in range(1,1<<N):
        if mask.bit_count()==2*r:
            actual=(dom[mask]==ALL and legal_orders[mask]>0)
            pred=predicted_set(mask,blades)
            classification_checks+=1
            assert actual==pred,(profile,mask,actual,pred,legal_orders[mask])
    prod_pairs=1
    for m in profile: prod_pairs*=comb(m,2)
    sum_center=0
    for j,m in enumerate(profile):
        q=m
        for i,mi in enumerate(profile):
            if i!=j: q*=comb(mi,2)
        sum_center += q
    pred_sets=prod_pairs+sum_center
    pred_sequences=factorial(2*r)*prod_pairs + factorial(2*r-1)*sum_center
    actual_sequences=sum(legal_orders[m] for m in max_masks)
    assert len(max_masks)==pred_sets,(profile,len(max_masks),pred_sets)
    assert actual_sequences==pred_sequences,(profile,actual_sequences,pred_sequences)
    # each no-center maximum set has (2r)! orderings; each center maximum set has (2r-1)!.
    for m in max_masks:
        want=factorial(2*r-1) if (m&1) else factorial(2*r)
        assert legal_orders[m]==want,(profile,m,legal_orders[m],want)
    return N,(1<<N)-1,append_checks,classification_checks,len(max_masks),actual_sequences

profiles=[]
for r in (2,3,4):
    profiles.extend(product((2,3), repeat=r))
profiles += [(2,4),(3,4),(2,2,4),(2,3,4),(2,2,2,4)]
seen=[]
for p in profiles:
    p=tuple(p)
    if p not in seen: seen.append(p)
profiles=seen

tot_masks=tot_app=tot_class=tot_maxsets=0
max_order=0
sequence_checksum=0
for p in profiles:
    N,masks,app,cl,ms,seq=verify_profile(p)
    max_order=max(max_order,N)
    tot_masks+=masks;tot_app+=app;tot_class+=cl;tot_maxsets+=ms;sequence_checksum+=seq
print(f"VERIFY_OK profiles={len(profiles)} subset_masks={tot_masks} append_checks={tot_app} classification_checks={tot_class} maximum_set_checks={tot_maxsets} sequence_checksum={sequence_checksum} max_order={max_order}")
