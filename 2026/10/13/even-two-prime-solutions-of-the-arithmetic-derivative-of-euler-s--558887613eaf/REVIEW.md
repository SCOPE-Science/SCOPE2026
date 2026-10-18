# Independent mathematical audit

## correctness

PASS

For n=2^a p^b with p odd prime, a,b>=1, p−1=2^t u (u odd), D(m)/m=sum_{ell|m} e_ell/ell yields exactly a+t−1+2(b−1)/p+2sum_{q|u} e_q/q=4+4/(2^t u). Coprimality forces p|(b−1), so b=1+kp. Comparing powers of 2 in the denominators rules out t>=3; comparing q-adic valuations rules out repeated q factors in u. Thus u squarefree and t∈{1,2}; the equations become a=4−2k−2(S(u)−1/u) for t=1 and a=3−2k−(2S(u)−1/u) for t=2. When omega(u)<=2, the only integral positive possibilities are u=1,t=1 (p=3, three pairs), u=1,t=2 (p=5, two pairs), u=q prime,t=1 (safe-prime p=2q+1, two pairs), and u=3·5,t=2 (p=61,a=2,b=1). For u=qr,t=1, 0<(q+r−1)/(qr)<1 forbids integer a; for t=2 only q=3,r=5 makes (2q+2r−1)/(qr) integral. Direct reverse substitution proves sufficiency. Independently factored and evaluated 3960 exact positive-integer cases for primes p<201, permitted omega(u), 1<=a<=8, b=1..10 and b=p+1, including exceptional (p,a,b)=(61,2,1). The infinite classification follows from the valuation proof, not finite factoring.

## originality

PASS

OEIS A248815 lists specific solutions of the exact equation n=D(phi(n)) and code searching a finite range but states no complete two-prime-support classification or the p−1 odd-support restriction; it lists 244 and many samples consistent with the theorem. OEIS A217715 concerns the reversed composition n=phi(D(n)), logically a different equation even where its small witnesses overlap. Grau–Oller-Marcén, Giuga Numbers and the Arithmetic Derivative, derives properties of D and a Giuga-number equation n′=an+1, not D(phi(n))=n. Resultary ranked work on the cototient gap D(n)-(n−phi(n)), iterated D and unrelated totient fibers; these do not imply the present case analysis. No stronger covered classification was identified, retaining risk of unindexed literature.

## value

PASS

An exact classification of an established OEIS composition equation on the natural even-two-prime family, with a motivated bound omega(odd(p−1))<=2, yields two genuinely infinite parameterized patterns and a rigid exceptional p=61 case. The special large exponent b=p+1 is not evident from finite OEIS search ranges. The support cutoff defines a natural tractable arithmetic slice, rather than arbitrary numerical truncation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
