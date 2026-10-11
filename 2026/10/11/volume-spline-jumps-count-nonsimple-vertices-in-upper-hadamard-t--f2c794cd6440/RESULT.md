# Volume-spline jumps count nonsimple vertices in upper Hadamard truncations
## Finding
Let \(H\) be a real Hadamard matrix of order \(d+1>2\). Normalize one column to all \(+1\), delete it, and write the remaining rows as \(v_0,\ldots,v_d\in\{\pm1\}^d\). Put
\[
\Delta=\operatorname{conv}\{v_0,\ldots,v_d\},\qquad
P_{m,n}=m\Delta\cap[-n,n]^d,
\]
with \(n>0\) and
\[
\frac{d-1}{2}n<m<dn.
\]
Define \(a_+=\max\{a,0\}\). Then
\[
\operatorname{vol}_d(P_{m,n})
=(2n)^d-\frac{d+1}{d!}\sum_{k=0}^d(-1)^k\binom{d}{k}
\bigl((d-2k)n-m\bigr)_+^d. \tag{1}
\]
For every integer \(j\) satisfying
\[
1\le j<\frac{d+1}{4},
\]
set \(m_j=(d-2j)n\). The volume profile in \(m\) is \(C^{d-1}\) but not \(C^d\) at \(m_j\), with right-minus-left jump
\[
[V^{(d)}]_{m_j}=(d+1)(-1)^{j+d}\binom{d}{j}. \tag{2}
\]
At exactly the same parameter, \(P_{m_j,n}\) has
\[
K_j=(d+1)\binom{d}{j} \tag{3}
\]
nonsimple vertices, and every other vertex is simple. Each nonsimple vertex has graph degree
\[
(j+1)(d-j). \tag{4}
\]
Consequently,
\[
\left|[V^{(d)}]_{m_j}\right|
=\#\{\text{nonsimple vertices of }P_{m_j,n}\}. \tag{5}
\]
Thus the analytic singularity of the volume spline counts the combinatorial singularities at every upper-regime smoothness resonance.

There is also a complete vertex-count profile. Write
\[
\tau=\frac{dn-m}{2n}.
\]
If \(\tau\notin\mathbb Z\) and \(r=\lfloor\tau\rfloor\), then all vertices are simple and
\[
f_0(P_{m,n})
=2^d-(d+1)\sum_{h=0}^{r}\binom{d}{h}
 +(d+1)(d-r)\binom{d}{r}. \tag{6}
\]
If \(\tau=j\in\mathbb Z\) is an internal resonance, then
\[
f_0(P_{m_j,n})
=2^d-(d+1)\sum_{h=0}^{j-1}\binom{d}{h}, \tag{7}
\]
and exactly the \(K_j\) boundary-layer vertices in (3) are nonsimple.

## Assumptions and scope
The Hadamard order is \(d+1>2\); hence the standard divisibility condition gives \(d\equiv3\pmod4\). The formulas (1), (6), and (7) are geometric and hold for real \(n>0\) and real \(m\) in the strict upper regime. To identify the resonances with the lattice smoothness criterion in Lebedev's setting, take the positive odd integer parameters used there. No assertion is made about the lower regime \(m\le(d-1)n/2\), where the corner cuts need not be disjoint.

## Proof
Lebedev's affine chart
\[
y=\frac{x+n\mathbf1}{2}
\]
sends \(P_{m,n}\) into the cube \([0,n]^d\). For each Hadamard row there is a cube corner \(c\in\{0,n\}^d\), and the corresponding simplex inequality deletes the cap
\[
L_c(y)<t,\qquad t=\frac{dn-m}{2},
\]
where \(L_c\) is the \(\ell_1\)-distance from \(c\). Distinct Hadamard corners have Hamming distance \((d+1)/2\), hence \(\ell_1\)-distance \((d+1)n/2\). Since \(m>(d-1)n/2\),
\[
2t<\frac{d+1}{2}n,
\]
so the \(d+1\) deleted caps are pairwise disjoint.

Reflecting coordinates about the sides of the cube sends every cap to
\[
C_t=\left\{z\in[0,n]^d:\sum_{i=1}^d z_i<t\right\}.
\]
Inclusion-exclusion from the positive orthant simplex gives
\[
\operatorname{vol}_d(C_t)
=\frac1{d!}\sum_{k=0}^d(-1)^k\binom{d}{k}(t-kn)_+^d. \tag{8}
\]
The chart has Jacobian factor \(2^d\), so
\[
V(m)=2^d\left(n^d-(d+1)\operatorname{vol}_d(C_t)\right).
\]
Substituting \(t=(dn-m)/2\) in (8) gives (1).

At \(m_j=(d-2j)n\), exactly the \(k=j\) positive-part term in (1) changes polynomial branch. A function \((a-m)_+^d\) is \(C^{d-1}\), while its \(d\)-th derivative changes by \(-(-1)^d d!\) when \(m\) crosses \(a\) from left to right. Multiplying by the coefficient of the \(j\)-th term gives (2), and therefore the magnitude in (3).

For the combinatorics, scale the cube to side length one and use Hamming distance from a cut center. At a nonintegral \(\tau\) with \(r=\lfloor\tau\rfloor\), exactly the cube vertices in Hamming layers \(0,\ldots,r\) are deleted. The cut facet crosses exactly the cube edges from layer \(r\) to layer \(r+1\), of which there are
\[
(d-r)\binom{d}{r}
\]
per center. Because \(2\tau<(d+1)/2\), the relevant neighborhoods and crossed edges for distinct Hadamard centers are disjoint. Counting surviving cube vertices plus new edge-cut vertices gives (6). Every such new vertex lies on one cut facet and \(d-1\) cube facets, so it is simple.

At \(\tau=j\), layers below \(j\) are deleted while every layer-\(j\) cube vertex lies on the cut hyperplane. The radius-\(j\) layers around distinct Hadamard centers are disjoint because
\[
2j<\frac{d+1}{2}.
\]
Hence there are exactly \((d+1)\binom{d}{j}\) such vertices, giving (3) and (7). Lebedev's local tangent-cone calculation at each such resonance vertex has \(d+1\) irredundant facets, so these vertices are nonsimple and no other upper-regime vertices are nonsimple.

To obtain (4), partition the inward coordinate directions into a set \(P\) of size \(j\) and a set \(N\) of size \(d-j\). The tangent cone is
\[
u_i\ge0,\qquad
\sum_{a\in N}u_a-\sum_{b\in P}u_b\ge0.
\]
Its extreme rays are precisely \(e_a\) for \(a\in N\) and \(e_a+e_b\) for \(a\in N\), \(b\in P\). Their number is
\[
(d-j)+j(d-j)=(j+1)(d-j),
\]
which is the degree of the corresponding polytope vertex. Combining (2) and (3) proves (5).

## Verification
The proof is exact and does not infer an infinite statement from finite enumeration. As a hand-check, for \(d=7\) the only internal upper resonance is \(j=1\), hence \(m=5n\). Formula (3) gives \(8\binom71=56\) nonsimple vertices, (4) gives degree \(12\), and (2) gives a seventh-derivative jump of magnitude \(56\). Formula (7) gives \(f_0=2^7-8=120\) at the resonance. These four independent consequences agree with the layer-count and tangent-cone descriptions.

## Relationship to prior work
Lebedev proves the upper-regime separated-corner description and the exact smoothness criterion: the lattice polytope is smooth precisely away from the odd ratios \(m/n=d-2j\) in the upper range. The same paper gives the local nonsimple tangent cone at the resonances. The present result keeps that geometric chart and derives the complete volume spline, the full vertex-count phase profile, the degree of every resonance vertex, and the equality (5) between an analytic derivative jump and the number of nonsimple vertices.

Santos introduced the cube-truncated Hadamard-simplex setting and records the equidistant Hamming geometry of the Hadamard vertices. The classical inclusion-exclusion formula (8) for a cube cap is not claimed as new. The new content here is its exact assembly over the disjoint Hadamard corner code together with the resonance combinatorics and the jump-count identity.

## Limitations
The argument uses strict separation of the deleted corner caps and therefore does not extend as stated below the upper threshold. The volume identity records Euclidean volume and does not by itself imply normality, integral closure, or Ehrhart properties. Originality has been checked against the lead paper, its direct Hadamard-simplex predecessor, targeted database searches, and the existing related records available for comparison; an unindexed general polyhedral-spline treatment could still contain an equivalent formulation.

## References
N. Lebedev, “Integrality, smoothness and normality bounds for cube-truncated Hadamard simplices,” arXiv:2609.32950v1, 2026. Relevant items: Theorem 2.6, the resonance tangent-cone analysis, and Corollary 3.2.

F. Santos, “Normality and Hadamard simplices,” Oberwolfach Reports 4 (2007), no. 3, 2306–2308, DOI 10.4171/OWR/2007/39.
