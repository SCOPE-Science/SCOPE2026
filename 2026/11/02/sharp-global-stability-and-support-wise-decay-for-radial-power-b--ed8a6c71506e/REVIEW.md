# Independent mathematical audit

## correctness

PASS

With q=p−2 and H(r)=1+r^q, the radial dual map has strictly increasing modulus rH(r) onto [0,∞). The next dual coordinate is [H(r)−ηa_i|x_i|^q]x_i; for each nonzero coordinate and η≤2/a_max the subtracted term is positive and at most 2r^q<2H(r). The norm strictly contracts after radial inversion, including at η=2/a_max. A positive limiting radius would, by compactness, give a nonzero limit point whose next radius contradicts continuity and strict contraction. On axis i, modulus comparison to t+t|t|^q reduces exactly to (ηa_i−2)|t|^q<2. At equality the un-inverted dual update is the negative of the current dual vector, hence a flip; outside it magnitudes strictly increase, reverse sign on every step, and no finite limiting magnitude above the flip radius can satisfy the continuous iteration. A maximum-weight axis supplies divergence for every larger η. Zeros are absorbing. On a surviving coordinate, z_k=|y_i^k| eventually obeys z_{k+1}=z_k(1−c_k z_k^q) with c_k=ηa_i/H(r_k)^(q+1)→ηa_i, and the multiplier is eventually in (0,1). Taylor expansion gives z_{k+1}^{−q}−z_k^{−q}→qηa_i; averaging and H→1 prove the coordinate limit. Raising the coordinate asymptotic to p/q and multiplying by a_i/p yields the exponent −2/q on a_i in the objective constant. Finite extinction and noninteger p>2 are covered by the analytic argument, not the floating-point tests.

## originality

PASS

The mirror update, radial kernel and even the exact scalar quartic special case as a toy model were known. The available comparisons do not give the exact all-start weighted-power frontier with the endpoint included, the unstable axial classification, or surviving-coordinate constants. The novelty assessment is limited to this phase portrait, not the algorithm or kernel.

## value

PASS

For an existing kernel family, the exact all-start boundary distinguishes sufficient safe steps from a sharp guarantee and includes the critical endpoint. The axial two-cycle and escape above it give constructive obstructions, not merely a lost descent estimate. The leading constants on the surviving support explain why initializations that extinguish coordinates need not have the same objective asymptotic. This is a useful deterministic control case rather than a generic performance claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
