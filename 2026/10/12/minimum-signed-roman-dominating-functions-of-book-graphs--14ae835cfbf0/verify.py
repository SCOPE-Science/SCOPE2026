from itertools import product
from math import comb

VALS=(-1,1,2)

def is_srdf_book(labels,n):
    u,v=labels[0],labels[1]
    pages=[(labels[2+2*i],labels[3+2*i]) for i in range(n)]
    # closed-neighborhood inequalities
    if u+v+sum(a for a,b in pages) < 1: return False
    if u+v+sum(b for a,b in pages) < 1: return False
    for a,b in pages:
        if u+a+b < 1: return False
        if v+a+b < 1: return False
    # every -1 has a 2-neighbor
    if u==-1 and not (v==2 or any(a==2 for a,b in pages)): return False
    if v==-1 and not (u==2 or any(b==2 for a,b in pages)): return False
    for a,b in pages:
        if a==-1 and not (u==2 or b==2): return False
        if b==-1 and not (v==2 or a==2): return False
    return True

def predicted_count(n):
    t=sum(comb(n,k) for k in range(n+1) if abs(n-2*k)<=3)
    if 3 <= n <= 5:
        t += 2*n
    return t

def classified(labels,n):
    u,v=labels[0],labels[1]
    pages=[(labels[2+2*i],labels[3+2*i]) for i in range(n)]
    if u==2 and v==2:
        if all(p in {(-1,1),(1,-1)} for p in pages):
            k=sum(p==(-1,1) for p in pages)
            return abs(n-2*k)<=3
        return False
    if 3 <= n <=5 and u==1 and v==2:
        return pages.count((-1,2))==1 and pages.count((1,-1))==n-1
    if 3 <= n <=5 and u==2 and v==1:
        return pages.count((2,-1))==1 and pages.count((-1,1))==n-1
    return False

def brute(n):
    best=10**9; count=0; class_count=0; checked=0
    for lab in product(VALS, repeat=2*n+2):
        checked += 1
        if not is_srdf_book(lab,n): continue
        w=sum(lab)
        if w<best:
            best=w; count=1; class_count=int(classified(lab,n))
        elif w==best:
            count+=1; class_count+=int(classified(lab,n))
    return best,count,class_count,checked

def dp_min_count(n):
    # Independent state enumeration derived directly from the SRDF conditions,
    # without using the theorem's classification.
    best=10**9; total_count=0
    for u,v in product(VALS, repeat=2):
        states=[]
        for a,b in product(VALS, repeat=2):
            if u+a+b<1 or v+a+b<1: continue
            if a==-1 and not (u==2 or b==2): continue
            if b==-1 and not (v==2 or a==2): continue
            states.append((a,b))
        # map (A,B,has_a2,has_b2,total_page_weight)-> count
        dp={(0,0,False,False,0):1}
        for _ in range(n):
            nd={}
            for (A,B,ha,hb,w),c in dp.items():
                for a,b in states:
                    key=(A+a,B+b,ha or a==2,hb or b==2,w+a+b)
                    nd[key]=nd.get(key,0)+c
            dp=nd
        for (A,B,ha,hb,pw),c in dp.items():
            if u+v+A<1 or u+v+B<1: continue
            if u==-1 and not(v==2 or ha): continue
            if v==-1 and not(u==2 or hb): continue
            w=u+v+pw
            if w<best:
                best=w; total_count=c
            elif w==best:
                total_count+=c
    return best,total_count

def main():
    brute_checks=0
    for n in range(3,6):
        best,count,class_count,checked=brute(n)
        brute_checks += checked
        assert best==4, (n,best)
        assert count==predicted_count(n), (n,count,predicted_count(n))
        assert class_count==count, (n,class_count,count)
    dp_states=0
    for n in range(3,13):
        best,count=dp_min_count(n)
        assert best==4, (n,best)
        assert count==predicted_count(n), (n,count,predicted_count(n))
        dp_states += count
    print(f"VERIFY_OK brute_n=3..5 labelings={brute_checks} dp_n=3..12 minimum_functions_summed={dp_states}")

if __name__=='__main__':
    main()
