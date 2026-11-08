#!/usr/bin/env python3
"""Independent rank test for the finite-field reversible wave on cones of Boolean cubes."""
def rank(rows, width):
    a=list(rows)
    r=0
    for col in range(width):
        pivot=next((j for j in range(r,len(a)) if a[j]>>col&1),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        for j in range(len(a)):
            if j!=r and a[j]>>col&1:
                a[j]^=a[r]
        r+=1
    return r

def mmul(a,b):
    out=[]
    for row in a:
        z=0
        while row:
            bit=row&-row
            z^=b[bit.bit_length()-1]
            row^=bit
        out.append(z)
    return out

def main():
    total=0
    for d in range(2,7):
        n=1<<d
        s=n+1
        adj=[sum(1<<(v^(1<<j)) for j in range(d)) | (1<<n)
             for v in range(n)] + [(1<<n)-1]
        wave=[adj[i] | (1<<(s+i)) for i in range(s)] \
             + [1<<i for i in range(s)]
        identity=[1<<i for i in range(2*s)]
        power=identity[:]
        exps=[]
        for t in range(1,25):
            power=mmul(power,wave)
            dim=2*s-rank([power[i]^identity[i] for i in range(2*s)],2*s)
            if d%2==0:
                want=(2*s if t%8==0 else 2*n if t%4==0
                      else n+2 if t%2==0 else n//2+1)
            else:
                want=(2*s if t%6==0 else n+1 if t%3==0
                      else 2 if t%2==0 else 1)
            assert dim==want,(d,t,dim,want)
            exps.append(dim)
            total+=1
        print("d=%d vertices=%d fixed_dims(t=1,2,3,4,6,8)=%s order=%d" %
              (d,s,[exps[i-1] for i in (1,2,3,4,6,8)],
               6 if d%2 else 8))
    print("PASS: %d full-rank iterate comparisons over F2; same dimensions over every F_(2^f)"%total)

if __name__=="__main__":
    main()
