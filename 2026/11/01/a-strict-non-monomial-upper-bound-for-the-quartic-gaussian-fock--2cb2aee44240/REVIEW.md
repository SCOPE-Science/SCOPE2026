# Independent mathematical audit

## correctness

PASS

At source RESULT.md and verify.py, for r=2063/2500, a=99/100, b=1/7 the polynomials f=(r-az)(1+bz), g=(z-ar)(1+bz) satisfy |g|²-|f|²=(1-a²)(|z|²-r²)|1+bz|², so exterior domination is exact for all |z|>r. Gaussian orthogonality gives ||h||_4^4=sum_{k=0}^4 k!/(2^k)|[z^k]h²|². Independently recomputed exact rational difference ||g||_4^4-||f||_4^4=-23857292957391399561/18757812500000000000000000<0, and checked r^4<1/2. Lower bound follows by applying the sharp Hilbert Fock radius at exponent2/weight2 to f²,g². The finite-term certificate is genuinely exhaustive for these degree-two witnesses, but no exact value of the universal K4 is established.

## originality

PASS

Best-of-knowledge originality from actual published mathematical searches and inspected primary scientific material; relevant exact known cases and stronger-coverage risks are compared, not merely title-matched. No directly implication-equivalent theorem identified in inspected statements; not a historical priority guarantee.

## value

PASS

This produces an explicit strict qualitative improvement beyond the natural monomial benchmark for an expressly open non-Hilbert Fock Korenblum problem. The multiplication by a nonconstant common factor reverses the quartic Gaussian norm inequality while retaining pointwise exterior domination. The rational number is a certificate, not asserted optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
