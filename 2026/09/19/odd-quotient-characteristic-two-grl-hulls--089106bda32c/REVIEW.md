# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**Verdict: PASS.**

The proof reduces the construction to two facts. First, for q=2^e with e/gcd(e,ell) odd, gcd(2^ell+1,2^e-1)=1, so every nonzero field element has a unique (2^ell+1)-st root. Second, Proposition II.8 of Wu--Liu--Chen--Zhou characterizes membership in the ell-Galois dual of a GRL code by a polynomial g and one extension-coordinate equation.

After choosing multipliers with v_i^(2^ell+1)=u_i and scaling exactly z=k-s-h of them, the unscaled evaluation coordinates force g=f^(2^ell): there are n-z=n-k+s+h roots, while the relevant degree is at most n-k+s-1. The bound on k is exactly what gives deg(f^(2^ell))<=n-k-1. The extension equation then forces the top s coefficients of f to vanish because A_s^(2^ell) is nonsingular. The scaled coordinates force z specified roots of f. This leaves precisely h free coefficients. The converse substitutes these polynomials back into the same equations.

Boundary cases h=0 and h=k-s were checked explicitly in the argument: for h=0 only the zero polynomial survives; for h=k-s no multiplier is scaled and all polynomials of degree at most k-s-1 belong to the hull.

The distance-neutral corollary is independent of the hull proof: changing the nonzero multipliers is diagonal coordinate scaling on the first n positions, hence a Hamming monomial equivalence preserving the complete weight distribution and dual distance.

The supplied finite-field verifier directly computes hull dimensions from generator matrices in representative fields and includes an ell not dividing e case. Its output agrees with the theorem.

## Originality

**Verdict: PASS, to the best of our knowledge.**

The primary source arXiv:2609.20453 was inspected at its standing field hypothesis, GRL dual characterization (Proposition II.8), characteristic-two root lemma (Lemma II.9), and common construction (Propositions III.1--III.2). The paper assumes 2ell|e throughout its constructions, even after observing a characteristic-two root phenomenon, and its common arbitrary-hull construction requires a subfield condition on normalized Lagrange coefficients.

Important prior art exists in the GRS setting. Wan--Zhu, arXiv:2412.05011, explicitly classify the characteristic-two case in which the extension degree divided by the relevant gcd is odd, construct Galois self-orthogonal GRS/EGRS MDS codes, and obtain arbitrary Galois hull dimensions by propagation. Accordingly, neither the odd-quotient finite-field regime nor the power-map observation is claimed as new here.

Targeted searches using generalized Roth--Lempel/GRL together with Galois hull, characteristic two, odd quotient, gcd conditions, arbitrary evaluation sets, and prescribed/arbitrary hull dimensions found the new Wu--Liu--Chen--Zhou preprint and Hermitian GRL work, but no earlier statement of the arbitrary-evaluation, arbitrary-extension-matrix GRL theorem proved here. The April 2026 GRL self-orthogonality paper is Hermitian-specific; Hermitian duality corresponds to an even quotient and does not cover this regime.

The originality claim is narrowly limited to transferring the odd-quotient characteristic-two mechanism through the GRL dual equations to obtain hull universality for every fixed GRL skeleton in the stated low-degree range, together with the distance-neutral tuning corollary. The motivating preprint is extremely recent, so a near-simultaneous observation or a later revision is a substantial priority risk.

No inaccessible source is currently identified as concrete evidence of prior coverage. The closest older source, Wan--Zhu, was accessible at least through its abstract and stated classification; its GRS scope is explicitly accounted for above. The literature search cannot establish absolute novelty.

## Value

**Verdict: PASS.**

Within the stated characteristic-two regime, the result removes the source construction's evaluation-set engineering entirely: arbitrary distinct evaluation points and an arbitrary nonsingular extension matrix work. It also includes infinitely many Galois exponents excluded by 2ell|e, including cases ell does not divide e. Because multiplier changes are Hamming isometries, any independently established MDS/AMDS/NMDS GRL skeleton in the dimension range immediately acquires all hull dimensions without sacrificing its classical distance profile. This separates the classical distance design problem from hull tuning in this regime.

## Limitations

The dimension range remains k<=floor((n+2^ell-1)/(2^ell+1)); no claim is made for larger k. The result does not classify MDS/AMDS/NMDS skeletons, does not improve known large-dimension GRS self-orthogonality results, and does not cover odd characteristic. The power-map lemma is standard finite-field arithmetic and is not claimed as a contribution. Independent audit and independent validation have not been performed.
