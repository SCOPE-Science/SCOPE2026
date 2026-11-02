# Independent mathematical audit

## correctness

PASS

PASS: Exact Fourier eigenvalues 1, B=(1−2p)^h, λ^h, conjugate; Fourier inversion gives deviations (B+2Reλ^h, −B+2Imλ^h, B−2Reλ^h,−B−2Imλ^h)/4 and TV d=[max(|B|,2|Reλ^h|)+max(|B|,2|Imλ^h|)]/4. Hence d>=|λ|^h/2>=2^{-h/2-1}, strict for p !=1/2. For even h the center reaches equality, proving unique minimum. For odd h the center has |cos|+|sin|=sqrt2 and expansion d(p)/d(1/2)=1−2h(h−1)(p−1/2)^2+O_h((p−1/2)^4), strict local maximum. Endpoint d=3/4 excludes endpoints, symmetry gives reflected off-center minima. Phase aligned p=(1+tan(pi/(4h)))/2 yields upper 2^{-h/2-1}sec^h(pi/(4h))+(1/4)tan^h(pi/(4h)); lower bound yields ratio 1/sqrt2+O(1/h). Independently checked 20 horizons with exact rational binomial modulo 4 convolution, sample grid; no assertion of unique odd minimizer.

## originality

PASS

PASS with residual priority risk: General hypercube and fastest-mixing works concern distinct chain families and optimization objectives; a published four-state cyclic ℓ4-contraction result concerns a norm other than finite-time TV from a point mass. No equivalent binomial-mod-four optimization theorem was located in searches. The new precise parity law is distinct from standard Fourier diagonalization.

## value

PASS

PASS: A smallest nontrivial nonreversible cyclic chain exhibits a genuine parity reversal between spectral-rate optimization and finite-horizon total-variation optimization. Uniform exact even-h minima, strict odd-h central maxima and sharp ~29.3% asymptotic improvement provide a useful counterexample/boundary, not a rote numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
