# Independent mathematical audit

## correctness

PASS

For S(n)=prod(j!,1<=j<=n), Legendre excludes precisely odd valuation with odd-unit 7 modulo 8 when the 2-adic valuation is even. Pairing binary digit sums shows that odd n are excluded exactly when n=5 mod 8; for n=2m, the obstruction is even s_2(m) and f(m)=7 mod 8. The factorial odd-unit recurrences f(2t)=f(t)O(t), f(2t+1)=f(t)O(t)(2t+1) derive the local binary parities A(m),B(m). The explicit 32-state deterministic bit automaton carries (m mod4,s_2(m) mod2,f(m) mod8), has constant row/column sum 2, a primitive Perron 2 eigenvalue and verified annihilating polynomial with remaining nonzero roots on |z|=sqrt(2); the dyadic-cylinder decomposition gives E(X)=3X/16+O(sqrt X). Cayley-Hamilton applied to diag(M^8,256,16) proves E(2^(8j+5))=3*2^(8j+1)+2^(4j) for every j >=0 from 34 exact initial equalities, not from extrapolation. Independently recomputed the odd-unit/valuation test for n=0..599 (first obstructions 5,10,13,20,21,24,29,37,45,48,53,61), the annihilator and small cylinder counts. These are corroborations of the unrestricted symbolic proof.

## originality

PASS

Burns 2021 and 2022 prove three-square properties of ordinary factorials and a 1/8-density/sqrt-error law. The submitted superfactorial criterion follows a different cumulative factorial product, and its exact all-j dyadic fluctuation is not supplied by the inspected theorems. The source acknowledges that Burns covers the broad density/error mechanism, so novelty is specifically the superfactorial obstruction and sharp exact dyadic identity.

## value

PASS

Three-square representability of superfactorials is a natural intersection of 2-adic arithmetic and automatic counting. The explicit forbidden-index predicate and sharp all-j dyadic fluctuation distinguish a meaningful new exact invariant rather than re-proving an ordinary factorial density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
