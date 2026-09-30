# Independent Audit — 2026/09/11/040

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `429ac1909ba8d861d6ddc1c1ec96f6e75eb8118c`  
**Audited current source tree:** `429ac1909ba8d861d6ddc1c1ec96f6e75eb8118c`  
**Audited main commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

## Correctness

PASS. The integral-point proof is correct. I independently expanded f=(x-1)g, recomputed disc(f)=1957, verified all three sandwich identities, and brute-checked integer x from -1000 through 1000. The only nonnegative-square values occur at x=1 and x=2, giving (1,0) and (2,±3). The proof covers all integers: x<=-3 gives f<0 by the derivative-sign argument, {-2,-1,0,1} are explicit, x=3,4,5 and x>6 are excluded by strict consecutive-square sandwiches for g together with gcd(x-1,g)=1, and x=6 is excluded directly. The record correctly limits itself to affine integral points and makes no rational-point closure claim.

## Originality

SUPPORTED, NARROW. The cited Chabauty/Mordell-Weil-sieve literature is methodological and does not state this exact integral census, and targeted searches for the exact quintic did not locate a covering earlier result. Search absence is not treated as proof of novelty. The defensible originality is the explicit elementary complete integral-point determination for this named genus-2 model, not a new general method.

## Scientific value

MEANINGFUL BUT NARROW. A complete, elementary, reproducible integral-point census for a concrete genus-2 curve has genuine arithmetic value and cleanly closes the integral slice of the broader rational-point target. Its scope is modest and the record states that limitation accurately.

## Independent checks

- symbolic factorization, discriminant and sandwich identities independently recomputed
- integer brute check for -1000<=x<=1000 as a consistency check in addition to the all-x proof
- current main record tree SHA equals the assigned source-tree SHA

## Sources consulted

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/040
- https://mathe2.uni-bayreuth.de/stoll/papers/MWsieve.pdf
- https://www.lmfdb.org/Genus2Curve/Q/

## Limitations

- The audit establishes only the affine integral locus; non-integral rational points remain open as the record says.
- No exhaustive bibliographic database can prove novelty; the originality finding is deliberately limited to absence of a located covering statement plus the curve-specific construction.
