# Independent mathematical audit

## correctness

PASS

Using exactly the published nonzero real-ray illumination and finite Borel mass normalization, construct ν_B=2σ_1+2σ_2 (mass 4) on unit phase circles for the complex l1 two-block; each nonzero boundary coordinate contributes mass 1 from inward half-phases, while zero coordinates do not contribute, so every block boundary point has cover >=1. Every additional disk has ν_j=2σ_j (mass 2) with boundary inward weight 1. Product/pushforward of these factor measures, normalized onto Euclidean unit directions (which preserves illumination and has no zero-vector mass), has mass 4*2^(n-2)=2^n and illuminates every product point. For a dual hard-boundary distribution choose J uniformly in {1,2}, one active phase at J and all remaining disk boundary phases independently Haar. A fixed v has first-block right derivative Re(e^-iθ v_J)+|v_{3-J}|; it can be strictly negative only for at most one of the two choices J and then on at most half the phase circle, yielding probability <=1/4. Other active disks each have conditional illumination probability at most 1/2, so P(v illuminates X)<=2^-n; Tonelli forces any fractional illuminating μ to have mass >=2^n. Equalities include n=2, empty product. Finally, a complex-linear polydisc representation would express |z1|+|z2| as max of finitely many |a_k z1+b_k z2|, but at (1,e^{iθ}) each fixed k saturates 2 for at most one θ and cannot cover the continuum. Every step is analytic and separately covers nonsmooth zero-coordinate corners; no sampling needed.

## originality

PASS

Rotem–Schejter–Slomka Conjecture 1.2 (2024 arXiv preprint and 2026 open published version) explicitly proposes ill*(K)<=2^n with equality only for complex-linear polydiscs; their Theorem 1.3 computes polydisc ill*, and Theorems 1.9–1.10 give strict non-polydisc bounds only inside the complex zonotope/zonoid subclasses. The inspected sections do not imply the nonzonotope l1-block equality case. Targeted published-result queries returned this claim as a self-index hit, but no independently prior l1-block product equality example. Residual unindexed counterexamples are possible.

## value

PASS

An exact natural complex l1^2–polydisc product supplies matching explicit covering and dual probability witnesses and changes the equality-case landscape of an explicit open conjecture in every complex dimension. It does not claim to resolve the conjectured universal upper bound and its failure is not based on mere finite numerical illustration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
