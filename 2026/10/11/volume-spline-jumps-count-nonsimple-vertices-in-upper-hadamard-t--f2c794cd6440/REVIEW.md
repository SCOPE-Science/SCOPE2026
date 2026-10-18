# Independent mathematical audit

## correctness

PASS

In Lebedev’s actual upper affine chart, (d+1) Hamming-separated cube corners have disjoint cut caps with threshold t=(dn−m)/2. Cube cap volume is 1/d! Σ(−1)^k binom(d,k)(t−kn)_+^d, so chart Jacobian 2^d directly gives the displayed exact full volume spline. At m_j=(d−2j)n only k=j branch changes; d-th right-minus-left derivative is (d+1)(−1)^{j+d}binom(d,j). For noninteger τ=(dn−m)/(2n), delete Hamming layers ≤r and replace each exposed r→r+1 cube edge with a simple cut vertex, yielding f0 formula (6). At integer τ=j the disjoint layer-j vertices number (d+1)binom(d,j); local tangent cone has d+1 facets and rays e_a (a in N), e_a+e_b (a in N,b in P), hence degree (j+1)(d−j). Every other vertex is simple; equality of jump magnitude and K_j follows. Independently checked exact d=7,11,15 resonances and sign/degree; no finite check substituted for universal disjointness proof.

## originality

PASS

Lebedev’s 2026 primary paper supplies the disjoint-corner upper chart, smoothness resonances and tangent-cone description, but the inspected original treatment does not give the exact assembled volume spline, phase-by-phase vertex count, derivative-jump constant or its equality with the nonsimple vertex count. The prior geometric cut representation plus elementary inclusion–exclusion and combinatorial Hamming counting is substantive synthesis: a general elementary cube-cap formula is known, but the exact analytic/combinatorial identification across all Hadamard dimensions is not located as an existing theorem. Best-of-knowledge PASS; possible broad polytope-spline coverage explicitly remains.

## value

PASS

The separated upper Hadamard truncation family already has a meaningful published smoothness-resonance problem. A complete volume spline and vertex-count profile, and the exact equality |jump of d-th volume derivative|=number of nonsimple vertices with degrees, are natural and structurally connected invariants for the entire Hadamard-order family. Value does not rest on the already known single-cap inclusion-exclusion formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
