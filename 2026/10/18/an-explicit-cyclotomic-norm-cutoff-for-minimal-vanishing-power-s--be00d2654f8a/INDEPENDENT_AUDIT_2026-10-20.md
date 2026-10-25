# Independent mathematical audit

## correctness

PASS

Order n modulo p^k stays order n modulo p because its p-power kernel cannot remove factors of n|(p−1). Thus q^n−1=product_{h|n}Phi_h(q) and proper factors are units modulo p^k, so Phi_n(q)=0(mod p^k). If a sum of s<r powers vanishes modulo p^k, reduce exponents mod n and form integer polynomial f. Lam–Leung weight theorem makes f(zeta_n) nonzero; each of d Galois conjugates has modulus<=s, so its integral resultant R=Res(Phi_n,f) is nonzero and |R|<=s^d<=(r−1)^d. The Sylvester integer Bezout identity evaluated at q gives p^k|R, impossible above bound. Conversely v=q^{n/r} has exact order r with v−1 invertible mod p^k, so 1+v+...+v^{r−1}=0, proving m=r. Since p>=n+1>r−1 the depth bound <=phi(n). Independent bounded brute search of short sums reproduced m values (n,p,k)=(5,11,1):3,(5,11,2):5,(5,11,3):5,(7,29,1):4,(7,29,2):7. The all-n statement rests on the resultant argument, not enumerated cases.

## originality

PASS

Jacob–Külshammer Prop10 proves eventual stabilization at least prime factor and expressly asks for an effective depth upper bound. Lam–Leung gives the complex roots-of-unity weight obstruction, and Breuer et al give qualitative resultant finiteness; both are credited. The explicit universal (r−1)^phi(n) integer norm cutoff is an extra quantified estimate; sharper fixed n=5,7 cases are prior, not reclaimed.

## value

PASS

The proposed invariant is the stabilization depth of modular vanishing power sums in a natural finite cyclic subgroup, and the published foundational work explicitly asks for an upper bound. An elementary uniform effective norm bound simultaneously for every n|(p−1), even if far from optimal, is directly useful to bound needed modulus depth and makes qualitative finiteness effective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
