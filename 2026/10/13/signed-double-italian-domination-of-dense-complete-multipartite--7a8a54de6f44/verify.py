from itertools import product

VALUES=(-1,1,2,3)

def parts_of_n(n, lo=2):
    # unordered integer partitions with all parts >=2 and at least three parts
    def rec(rem, last):
        if rem==0:
            yield ()
            return
        for x in range(last, rem+1):
            if x < 2: continue
            for rest in rec(rem-x, x):
                yield (x,)+rest
    for p in rec(n,lo):
        if len(p)>=3:
            yield p

def labels_to_parts(parts):
    owner=[]
    for i,n in enumerate(parts):
        owner += [i]*n
    return owner

def is_sdidf(parts, f):
    owner=labels_to_parts(parts)
    r=len(parts)
    s=[0]*r
    pos=[0]*r
    for v,x in enumerate(f):
        i=owner[v]
        s[i]+=x
        if x>0:
            pos[i]+=x
    W=sum(f)
    P=sum(x for x in f if x>0)
    for v,x in enumerate(f):
        i=owner[v]
        outside_sum=W-s[i]
        if x+outside_sum < 1:
            return False
        outside_pos=P-pos[i]
        if x==-1 and outside_pos<3:
            return False
        if x==1 and outside_pos<2:
            return False
    return True

def predicted(parts):
    return 2 if min(parts)==2 else 3

def construction(parts):
    # theorem's explicit construction
    r=len(parts)
    lab=[]
    if min(parts)==2:
        j=parts.index(2)
        blocks=[]
        for i,n in enumerate(parts):
            if i==j:
                blocks.append([1,1])
            elif n%2==0:
                blocks.append([1]*(n//2)+[-1]*(n//2))
            else:
                blocks.append([2]+[1]*((n-3)//2)+[-1]*((n+1)//2))
        return tuple(x for b in blocks for x in b)
    else:
        blocks=[]
        for i,n in enumerate(parts):
            if i<3: # sum one
                if n%2:
                    blocks.append([1]*((n+1)//2)+[-1]*((n-1)//2))
                else:
                    blocks.append([2]+[1]*((n-2)//2)+[-1]*(n//2))
            else: # sum zero
                if n%2==0:
                    blocks.append([1]*(n//2)+[-1]*(n//2))
                else:
                    blocks.append([2]+[1]*((n-3)//2)+[-1]*((n+1)//2))
        return tuple(x for b in blocks for x in b)

types=0
labelings=0
witnesses=0
mins={}
for N in range(6,10):
    for parts in parts_of_n(N):
        types += 1
        target=predicted(parts)
        best=None
        for f in product(VALUES, repeat=N):
            labelings += 1
            # safe pruning: only test weights <= target to verify no smaller and existence;
            # construction separately verifies existence.
            w=sum(f)
            if w>target:
                continue
            if is_sdidf(parts,f):
                if best is None or w<best:
                    best=w
        c=construction(parts)
        assert sum(c)==target,(parts,sum(c),target,c)
        assert is_sdidf(parts,c),(parts,c)
        witnesses += 1
        if best is None:
            best=target
        assert best==target,(parts,best,target)
        mins[parts]=best

print("VERIFY_OK")
print("complete_multipartite_types_checked =",types)
print("orders_checked = 6..9")
print("labelings_scanned =",labelings)
print("explicit_constructions_checked =",witnesses)
print("all parts >=2 and at least three parts")
print("every minimum matched 2 iff a part has size 2, else 3")
