# Mathematical review: A Gaussian interface-merger law for projective Fock concentration bands

## Correctness — PASS

The exact spectral domain and Gaussian normalization are fixed in RESULT.md. Angular orthogonality, two independent gamma variables and their beta ratio give the eigenvalues; the integer shape sum is \(n+2\), hence the binomial coupling has \(n+1\) trials. The identity \(V_n=\tfrac12\mathbb E|I_1\triangle I_2|\) follows by exact indicator variance. For finite critical width, the binomial CLT and vanishing rescaled increment variance reduce the continuum defect to the symmetric difference of equal-length normal-shifted intervals; the endpoint difference \(L^2\) bound supplies uniform integrability. The diverging-width case requires and uses a separate overlap-probability argument. The folded-normal integral yields the asserted coefficient and derivatives. The code checks exact finite identities and numerical approach but no numerical test substitutes for this proof.

## Originality — PASS, subject to historical-priority risk

The source projective Toeplitz decomposition (González-Flores et al., November 2023) gives the setting but not a band-merger law. The strongest inspected radial counting works (Charlier, 2021, and Akemann–Byun–Ebke, 2022) concern fixed-separated jumps or single-disk counting, so the sharp \(O(n^{-1/2})\) two-interface covariance is not implied. An exact coupled-binomial interval formula and the full \(0\le c\le\infty\) crossover were not located in relevant accessible primary texts, matching published-finding corpus queries, or other previously documented mathematical claims. The DPP annulus reformulation is recognized explicitly: historical equivalence elsewhere is a residual risk, and failed searches are not proof of novelty.

## Mathematical value — PASS

Projective latitude-band concentration is a canonical two-interface spectral localization problem under the established projective decomposition of Gaussian Fock space. Two asymptotically independent boundary contributions cease to be additive precisely when their separation is comparable to the quantum interface width. The explicit strictly concave response \(H_t(c)\) quantitatively resolves that transition, and the exact finite coupled-interval identity supplies a usable formula beyond the limiting case. This is not a gratuitous parameter substitution or a fixed-width asymptotic restatement.

## Limitations and closest prior work

The proof treats interior projective latitudes only; projective poles and nonradial domains remain open. Fixed separated radial jump asymptotics from arXiv:2109.03660 and single-disk variance universality from arXiv:2206.08815 do not cover merging interfaces, but broad random-normal-matrix covariance results beyond those inspected could. The source at DOI 10.3390/axioms12121080 supplies decomposition, not the variance law. Independent expert audit and historical-priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
