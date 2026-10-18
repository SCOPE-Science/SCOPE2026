"""Exact ambiguity-zero and operator-rank checks for quartic-graph Gabor windows.
Run with Python standard library: python verify_quartic_tomography.py.
The zero test uses the minimal polynomial 1+...+T^(p-1) for primitive pth roots.
"""
import json

def chi_minus_three(p):
    return 1 if pow((-3)%p,(p-1)//2,p)==1 else -1

def inspect_prime(p):
    q=p
    f4=[pow(t,4,p) for t in range(p)]
    roots={(a,b):[] for a in range(p) for b in range(p)}
    for a in range(p):
        for t in range(p):
            b=(f4[(t+a)%p]-f4[t])%p
            roots[a,b].append(t)
    support_cubic=len({(w**3+w)%p for w in range(p)})
    chi=chi_minus_three(p)
    predicted_support=(2*p+chi)//3
    assert support_cubic==predicted_support
    cperm=[c for c in range(p) if len({(w**4+c*w)%p for w in range(p)})==p]
    assert cperm==([3,4] if p==7 else [])
    zeros=0
    split={'empty_intersection':0,'origin_permutation':0}
    for (a,b),ts in roots.items():
        if (a,b)!=(0,0):
            assert len(ts)<=3
        for m in range(p):
            for n in range(p):
                exps={(m*t+n*f4[t])%p for t in ts}
                # If sum of fewer than p p-th roots vanishes, impossible;
                # for exactly p terms, vanishing iff all exponents occur once.
                is_zero = len(ts)==0 or (len(ts)==p and len(exps)==p)
                if is_zero:
                    zeros+=1
                    if not ts:split['empty_intersection']+=1
                    else:split['origin_permutation']+=1
                expected = ((a==0 and b!=0) or
                            (a!=0 and (2*b*pow(a,-4,p))%p not in
                                 {(w**3+w)%p for w in range(p)}) or
                            (a==b==0 and
                             ((n==0 and m!=0) or
                              (p==7 and n!=0 and (m*pow(n,-1,p))%p in (3,4)))))
                assert is_zero==expected,(p,a,b,m,n,is_zero,expected)
    total=p**4
    predicted=p*p*(1+(p-1)*predicted_support)-(p-1)*(3 if p==7 else 1)
    rank=total-zeros
    assert rank==predicted,(p,rank,predicted)
    return {'prime':p,'chi_minus_3':chi,'cubic_image_size':support_cubic,
            'quartic_linear_permutation_coefficients':cperm,
            'operator_rank':rank,'kernel_dimension':zeros,
            'zero_counts':split,'matrix_dimension':p*p}

def main():
    output=[inspect_prime(p) for p in [5,7,11,13,17,19,23,29,31]]
    print(json.dumps({'status':'all exact direct ambiguity checks passed',
                      'checked_primes':len(output),'results':output},sort_keys=True,indent=2))
if __name__=='__main__':main()
