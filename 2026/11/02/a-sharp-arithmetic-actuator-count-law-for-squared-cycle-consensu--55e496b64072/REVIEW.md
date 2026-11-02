# Mathematical review

## Correctness — PASS

The finite-n graph is specified by an integer circulant matrix, and the Fourier symbol is derived explicitly. The factorization of equal eigenvalues reduces the nontrivial cases to a cosine-sum equation; Galois averaging via the Ramanujan sum gives the restrictive Möbius/totient equation. The only candidates are orders two/six, three/four, and distinct order-five cosine values. Counting indices yields maximal eigenspace dimension exactly two, three, or four. The PBH lower bound and full-rank Vandermonde restrictions at consecutive input sites establish the exact global minimum; all quantifiers \(n\ge5\) are covered. An independent finite modular-rank and trigonometric diagnostic script passed 816 checks. No finite experiment is presented as an infinite proof.

## Originality — PASS (residual historical risk)

Parlangeli–Notarstefano (2011) concerns the ordinary cycle; Yuan et al. (2013) and Nabi-Abdolyousefi–Mesbahi (2013) supply general maximum-eigenspace multiplicity principles for graph/circulant controllability. Those principles alone do not give the arithmetic \(5,6,12\) classification of the squared cycle. Monshizadeh–Zhang–Camlibel (2014) addresses zero forcing over a matrix class. Saha–Das (2025) writes down the Fourier eigenvalues but its claimed pairing-based multiplicity representation does not account for the extra cyclotomic collisions. The new claim is the complete all-dimension multiplicity arithmetic and resulting exact minimum leader count, not a new general PBH theorem. The 2013 circulant paper and a 2014 related expanded chapter remain possible sources of overlap because their complete texts were not available for direct inspection.

## Mathematical value — PASS

The squared cycle is a standard four-regular distributed-control topology. The number of actuators is a natural discrete invariant: the sharp two-versus-three-versus-four classification is neither evident from degree nor monotone in network size, and the explicit consecutive construction makes it operational. The cyclotomic-order obstruction and exact dimension boundaries are structural, rather than a reparameterized generic inequality or a list of tested numerical instances.

## Scope and open risks

The theorem applies to fixed unit-weight Laplacian consensus dynamics and independent, localized inputs, not arbitrary circulant weights or structural controllability. Its closeness to the existing general circulant control literature is acknowledged, and historical special-case coverage cannot be excluded without all relevant full texts. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
