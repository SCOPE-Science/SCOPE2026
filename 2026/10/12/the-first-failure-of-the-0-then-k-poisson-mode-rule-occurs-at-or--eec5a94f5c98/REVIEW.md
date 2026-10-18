# Independent mathematical audit

## correctness

PASS

Normalized probability coefficients a_{k,n}=[z^n] exp(lambda sum_{j=1}^k z^j) obey n a_{k,n}=lambda sum_{j<=min(k,n)} j a_{k,n-j}, and are strictly increasing for n>0. Independently executed exact Fraction recurrence at B=q/10^6 and L=B-10^-6 for all 14 k values, n<=40k; every target crosses one and all alternate coefficients are strictly below one at B, kB<4. For n>40k every summand needs >=41 jumps, giving a_n(B)<=sum_{m>=41}(kB)^m/m!<2*4^41/41!<1. Thus all infinitely many indices and all real lambda before first crossing are controlled, with no possible third tie. The smallest alternate gap at k=15 is at n=26, about 0.000528; no significance is attributed to decimals as proofs.

## originality

PASS

Crucial close prior art: S. R. Mane arXiv:2309.05190 §4, Fig. 2 explicitly numerically observed first k15 switch 0-to-25 around lambda 0.25023 and k<=14 switch 0-to-k; arXiv:2309.09278 repeats the same numerical result. Hence the numerical discovery and index are NOT new. Both works state numerical findings/partly conjectural classifications, defer proof, and leave triple modes uninvestigated. The narrower original advance is a new exact rational finite-prefix certificate PLUS rigorous all-index tail bound proving first-transition uniqueness and excluding triple ties across k=2..15. Existing low-order theorems do not imply that fully rigorous certified conclusion.

## value

PASS

An exact global proof of a previously reported but numerically unsupported first exception is a motivated open certification problem for a natural probability-law modal transition. It settles the order-15 first transition, its precise unique equality case and true infinite-support cutoff, without pretending that previously published numerical values were newly discovered. Meaningful finite-order result; not a mere table recomputation because rigorous exclusion of every index and tie is missing from the strongest prior numerical studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
