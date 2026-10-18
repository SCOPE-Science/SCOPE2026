# A five-cycle blossom transition in the John ellipsoids of odd-cycle matching polytopes

## Finding

For every odd integer \(n\ge5\), let \(P_n\subset\mathbb R^n\) be the matching polytope of the cycle \(C_n\), in standard edge-incidence coordinates with the ordinary Euclidean metric. Its unique maximum-volume inscribed (John) ellipsoid is \(E_n=\{x:(x-c_n)^\mathsf T Q_n^{-1}(x-c_n)\le1\}\). Write \(A_n\) for the adjacency matrix of \(C_n\) and \(J_n=\mathbf1\mathbf1^\mathsf T\).

**For \(n=5\):** Put
\[
 t_5=\frac{21-\sqrt6}{60},\qquad
 a_5=12-2\sqrt6,\quad b_5=8\sqrt6-18,\quad d_5=252-102\sqrt6.
\]
Then \(c_5=t_5\mathbf1\), and
\[
 Q_5^{-1}=a_5I+b_5(2I+A_5)+d_5J_5.
\]
All eleven facets of \(P_5\) touch \(E_5\): its five nonnegativity facets, five vertex-degree facets, and its global odd-set (blossom) facet.

**For every odd \(n\ge7\):** There is a unique \(h_n>0\) solving
\[
 \frac1n\sum_{j=0}^{n-1}
 \frac{h_n(h_n+2)}{2(h_n+1+\cos(2\pi j/n))}=1.
\]
Then \(h_n>1\), and
\[
 c_n=\frac{\mathbf1}{h_n+2},\qquad
 Q_n^{-1}=\frac{h_n+2}{h_n}\bigl(2(h_n+1)I+A_n\bigr).
\]
Exactly the \(2n\) nonnegativity and vertex-degree facets touch \(E_n\). The global odd-set facet, although a genuine facet of \(P_n\), is **strictly separated** from \(E_n\) for every odd \(n\ge7\). Therefore \(n=5\) is the unique odd-cycle size at which a blossom facet changes the John ellipsoid relative to the fractional matching relaxation. All displayed ellipsoids are unique, without any symmetry assumption on competing ellipsoids.

## Assumptions and scope

The graph is the simple cycle on \(n\) vertices and \(n\) edges, \(n\) odd and \(n\ge5\); the coordinates correspond to edges cyclically indexed modulo \(n\). The standard matching-polytope description (the cycle case of the Edmonds--Pulleyblank inequalities) is
\[
 P_n=\left\{x\in\mathbb R^n:\; x_i\ge0,\quad x_i+x_{i+1}\le1\ \forall i,\quad
 \sum_{i=1}^n x_i\le \frac{n-1}{2}\right\}.
\]
Its fractional relaxation \(F_n\) omits the last inequality. These are full-dimensional polytopes: a sufficiently small positive constant vector is strictly feasible. The John ellipsoid is measured in the given edge-coordinate Euclidean structure; an arbitrary affine-equivalent realization need not have the same shape. The theorem excludes the triangle and even cycles.

For a positive-definite shape matrix \(Q\), the ellipsoid \(c+Q^{1/2}B_2^n\) is feasible for an inequality \(a^\mathsf Tx\le b\) exactly when \(a^\mathsf Tc+\sqrt{a^\mathsf TQa}\le b\). This also gives the precise definition of facet tangency used below.

## Proof

**1. An explicit John certificate.** Write \(B=Q^{1/2}\). If a feasible ellipsoid has touching facets with outward normals \(a_s\), positive weights \(w_s\), and gaps \(g_s=b_s-a_s^\mathsf Tc=\|Ba_s\|\), its unit-ball contact points are \(u_s=Ba_s/g_s\). John's sufficient contact identities are
\[
 \sum_s w_su_s=0,\qquad \sum_s w_su_su_s^\mathsf T=I.
\]
Equivalently, because \(B\) is invertible,
\[
 \sum_s\frac{w_s}{g_s}a_s=0,\qquad
 \sum_s\frac{w_s}{g_s^2}a_sa_s^\mathsf T=Q^{-1}.
\]
These identities certify maximum volume among **all** inscribed ellipsoids, and uniqueness follows from uniqueness of the John ellipsoid of a full-dimensional convex body.

**2. All odd-cycle fractional relaxations.** For an odd \(n\ge5\), set \(\theta_j=2\pi j/n\) and define
\[
 F_n(h)=\frac1n\sum_{j=0}^{n-1}
 \frac{h(h+2)}{2(h+1+\cos\theta_j)},\qquad h>0.
\]
Each summand is strictly increasing: after differentiation its numerator, up to a positive constant, is \(h^2+2(h+1)(1+\cos\theta_j)>0\). Because \(n\) is odd, no \(\cos\theta_j\) equals \(-1\), so \(F_n(h)\to0\) as \(h\downarrow0\); also \(F_n(h)\to\infty\) as \(h\to\infty\). Thus \(F_n(h)=1\) has a unique positive root \(h=h_n\).

Put \(t=1/(h+2)\) and \(Q^{-1}=((h+2)/h)(2(h+1)I+A_n)\). Since all eigenvalues of \(2(h+1)I+A_n\) are \(2(h+1+\cos\theta_j)>0\), \(Q\) is positive definite. Let \(q_0=Q_{ii}\), \(q_1=Q_{i,i+1}\). The Fourier-diagonal formula and \(F_n(h)=1\) give
\[
 q_0=t^2,\qquad 2(q_0+q_1)=(1-2t)^2,
 \qquad \mathbf1^\mathsf TQ\mathbf1=\frac{nh}{2(h+2)^2}.
\]
For completeness, write \(U=\frac1n\sum_j [2(h+1+\cos\theta_j)]^{-1}=1/[h(h+2)]\) and \(V=\frac1n\sum_j\cos\theta_j[2(h+1+\cos\theta_j)]^{-1}\). The resolvent identity \(2(h+1)U+2V=1\) yields both formulas for \(q_0,q_1\). Thus the ellipsoid \(t\mathbf1+Q^{1/2}B_2^n\) touches all \(n\) lower facets and all \(n\) degree facets of \(F_n\).

The outward normals are \(-e_i\) and \(e_i+e_{i+1}\), with gaps \(t\) and \(1-2t\) respectively. Assign **each** lower facet weight \(2t\), and **each** degree facet weight \(1-2t\); they are strictly positive. Their weighted normal sum is
\[
 -\frac{2t}{t}\mathbf1+\frac{1-2t}{1-2t}\sum_i(e_i+e_{i+1})=0.
\]
Their weighted normal-moment matrix is
\[
 \frac{2t}{t^2}I+\frac{1-2t}{(1-2t)^2}(2I+A_n)
 =\frac{h+2}{h}\bigl(2(h+1)I+A_n\bigr)=Q^{-1}.
\]
The contact identities prove that this is the unique John ellipsoid of \(F_n\), independently of any previously published formula for the fractional relaxation.

**3. Screening the global blossom facet in all higher odd dimensions.** Let \(\rho=2-\sqrt3\). The elementary Poisson-kernel identity
\[
 \frac1{2+\cos\theta}=\frac1{\sqrt3}\left(1+2\sum_{k\ge1}(-\rho)^k\cos(k\theta)\right)
\]
and orthogonality of roots of unity show, for odd \(n\),
\[
 \frac1n\sum_{j=0}^{n-1}\frac1{2+\cos\theta_j}
 =\frac1{\sqrt3}\frac{1-\rho^n}{1+\rho^n}<\frac1{\sqrt3}.
\]
Hence \(F_n(1)<\sqrt3/2<1\) and \(h_n>1\). The exact clearance from the blossom plane in the direction \(\mathbf1\) is
\[
 \delta_n=\frac{n-1}{2}-\frac{n}{h_n+2}
 -\frac{\sqrt{nh_n/2}}{h_n+2}.
\]
Indeed the last term is \(\sqrt{\mathbf1^\mathsf TQ\mathbf1}\). Multiplying by \(h_n+2\), the assertion \(\delta_n>0\) becomes
\[
 \frac{(n-1)h_n-2}{2}>\sqrt{nh_n/2}.
\]
For \(h_n>1\), its left side divided by \(\sqrt{h_n}\) exceeds \((n-3)/2\), while the right side divided by \(\sqrt{h_n}\) is \(\sqrt{n/2}\). The inequality \((n-3)/2\ge\sqrt{n/2}\) holds for every integer \(n\ge7\) (squaring gives \(n^2-8n+9\ge0\)). Thus \(\delta_n>0\) for every odd \(n\ge7\). The fractional John ellipsoid lies strictly inside the additional blossom halfspace, so is also the unique John ellipsoid of \(P_n\). Its two orbit families are the complete list of contacts.

**4. The exceptional pentagon, including the blossom contact.** Let \(t=t_5\), \(a=a_5\), \(b=b_5\), \(d=d_5\), and define \(Q=(aI+b(2I+A_5)+dJ_5)^{-1}\). All \(a,b,d\) are strictly positive; hence \(Q^{-1}\), and therefore \(Q\), are positive definite. Direct exact radical algebra, using \(\cos(2\pi/5)=(\sqrt5-1)/4\) and \(\cos(4\pi/5)=-(\sqrt5+1)/4\), proves
\[
 Q_{ii}=t^2,\quad 2(Q_{ii}+Q_{i,i+1})=(1-2t)^2,\quad
 \mathbf1^\mathsf TQ\mathbf1=(2-5t)^2.
\]
Thus \(t\mathbf1+Q^{1/2}B_2^5\) is feasible and touches all eleven facets. Assign each lower facet weight \(\alpha=at^2\), each degree facet weight \(\beta=b(1-2t)^2\), and the single blossom facet weight \(\gamma=d(2-5t)^2\). All are positive. The first John identity reduces to
\[
 -at+2b(1-2t)+d(2-5t)=0,
\]
which follows exactly from the displayed radicals. The second identity is the defining relation \(Q^{-1}=aI+b(2I+A_5)+dJ_5\). John's theorem now proves both global optimality and uniqueness, with all eleven contacts. Moreover, \(d_5>0\) gives nonzero inverse-shape entries at distance two around the pentagon, unlike the exact fractional-ellipsoid inverse from Step 2 (whose nonedge entries vanish); thus the pentagon blossom really changes the optimum, rather than merely adding a redundant contact.

## Verification

The delivered standalone `EXACT_CHECK.py` reconstructs the full \(5\times5\) pentagon matrix with exact radicals, verifies the three support equalities and John balance identity symbolically, and checks the positivity of the three orbit coefficients. It requires SymPy. `CHECK.py` requires only the Python standard library; it independently evaluates the unique-root equation, every spectral support identity, the explicit John weights, and the strict blossom clearance for all odd dimensions from \(7\) to \(301\), plus the pentagon case. On the test execution, the exact certificate and all 148 higher odd dimensions passed. These finite checks are not the proof of the all-dimensional assertions; Steps 1--4 above supply that proof.

## Relationship to prior work

Eisley, Matsushita and Vindas-Meléndez study matching polytopes of graphs, including cycles, their Gorenstein properties and integer decomposition property (arXiv:2407.08820, first public July 11, 2024; primary MSC 52B05). Kafer, Pashkovich and Sanità study circuit diameters of matching and fractional stable-set polytopes (arXiv:1709.09642, first public September 27, 2017; primary MSC 52B05). These primary sources provide the natural polyhedral setting, not a John-ellipsoid classification.

The indexed result *An exact John ellipsoid and sharp exponential law for odd-cycle fractional stable-set polytopes* (publicly indexed October 11, 2026) treats the larger fractional relaxation. Its full underlying source could not be inspected through the available public link, so its precise notation and proofs are not claimed checked. The fractional formula is independently reconstructed here. The additional integer matching-polytope blossom facet is absent from that relaxation; the strict all-\(n\ge7\) facet-screening assertion and the explicit rank-one pentagon correction are not stated in the indexed summary. An indexed result on vertex-/edge-transitive **fractional matching** polytopes likewise does not directly cover the integral odd-cycle blossom halfspace.

## Limitations

The domain is odd simple cycles of length at least five, in standard incidence coordinates. The result does not apply to arbitrary graphs, even cycles, or arbitrary affine metrics. The odd-cycle facet screening is a specific additional result beyond the known fractional ellipsoid, not a claim that the fractional result itself is new. Bibliographic searches and comparisons do not establish absolute uniqueness in the literature; an inaccessible older treatment of odd-cycle matching ellipsoids may exist. Independent mathematical validation has not been performed.

## References

1. B. Eisley, K. Matsushita and A. R. Vindas-Meléndez, *Matching polytopes, Gorensteinness, and the integer decomposition property*, arXiv:2407.08820 (first public 2024-07-11), https://arxiv.org/abs/2407.08820.
2. S. Kafer, K. Pashkovich and L. Sanità, *On the Circuit Diameter of Some Combinatorial Polytopes*, arXiv:1709.09642 (first public 2017-09-27), https://arxiv.org/abs/1709.09642.
3. J. Edmonds and W. Pulleyblank, *Facets of 1-matching polyhedra* (1974), cited in Reference 1 for the standard integral matching-polytope inequalities.
4. *An exact John ellipsoid and sharp exponential law for odd-cycle fractional stable-set polytopes*, published mathematical record 2026-10-11, indexed in public mathematical research records; https://github.com/published-finding corpus/2026.
