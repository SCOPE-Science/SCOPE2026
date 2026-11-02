# Exact Euclidean distortion on the long-edge deformation of a four-cycle

## Finding
Let \(1<t<3\), and let \(C_4(t)\) be the four-vertex shortest-path metric of a weighted cycle whose consecutive edge lengths are \(1,1,1,t\). For its **real** Lipschitz-free (transportation-cost) space, the exact squared Banach–Mazur distance to three-dimensional Euclidean space is
\[
 d_{\mathrm{BM}}\!\left(\mathcal F(C_4(t)),\ell_2^3\right)^2
 = \begin{cases}
 \displaystyle\frac{3(5t^2+3)}{t^2(9-t^2)},&1<t\le 3/\sqrt5,\\[4pt]
 \displaystyle\frac{25}{9},&3/\sqrt5\le t\le2,\\[4pt]
 \displaystyle\frac{(t+3)(7-t)}{(t+1)(5-t)},&2\le t<3.
 \end{cases}
\]
The expressions coincide at the shared endpoints. In particular the distance is exactly \(5/3\) throughout the nontrivial interval \([3/\sqrt5,2]\), despite the changing metric. The values tend to \(\sqrt3\) both as \(t\downarrow1\) and as \(t\uparrow3\).

The **short-edge** range \(0<t\le1\) is **not claimed as a new result**: it is covered by the published all-dimension theorem *Opposite parity laws for exact Hilbert distortion of one-edge weighted cycles*. Setting its cycle parameter \(n=4\) gives \(d_{\mathrm{BM}}^2=3(7+t^2)/(9-t^2)\) on that range. The present finding is specifically the exact long-edge continuation \(1<t<3\), its two transition points, and its plateau. At \(t=3\) the fourth edge is redundant and the metric is a weighted path, an established tree endpoint.

## Definitions and scope
For equal-dimensional real Banach spaces, \(d_{\mathrm{BM}}(X,Y)=\inf_T\|T\|\|T^{-1}\|\), with \(T\) ranging over all invertible linear maps. Four distinct labelled vertices are equipped with shortest-path distances from the stated positive edge weights. Every edge is metrically essential for \(1<t<3\). No assertion concerns complex scalars, arbitrary four-point metrics, several independent edge weights, or longer cycles. Optimization is unrestricted over all Euclidean Hilbert norms, not merely symmetric or diagonal maps.

## Proof
**1. Dual representation.** For a real-valued Lipschitz function on the metric vertices, orient the four edges cyclically and divide each signed edge increment by its edge length. The normalized increments \((x_1,x_2,x_3,y)\) satisfy \(x_1+x_2+x_3+ty=0\); conversely every such tuple integrates to a vertex function, uniquely modulo constants. Bounding these edge increments is equivalent to bounding all pairwise Lipschitz quotients, since the shortest-path distance is induced by the weighted graph. Eliminating \(y\) gives the dual norm
\[
 N_t(x)=\max\{ |x_1|,|x_2|,|x_3|,|x_1+x_2+x_3|/t\},
 \quad K_t=[-1,1]^3\cap\{|x_1+x_2+x_3|\le t\}.
\]
The dual of the three-dimensional Lipschitz space is \(\mathcal F(C_4(t))\). Finite-dimensional Banach–Mazur duality and the self-duality of Hilbert space reduce the asserted distance to \(d_{\mathrm{BM}}((\mathbb R^3,N_t),\ell_2^3)\).

**2. Symmetric Hilbert norms suffice globally.** Any pulled-back Hilbert norm has square \(Q(x)\), a positive-definite quadratic form. After rescaling, the distortion inequality reads \(N_t(x)^2\le Q(x)\le D^2N_t(x)^2\) for all \(x\). Because \(N_t\) is invariant under all six coordinate permutations, averaging this quadratic form over those permutations preserves both inequalities and cannot increase \(D\). Hence an optimal form exists in the permutation-invariant two-parameter family. Up to positive scaling it is
\[
 Q_\alpha(x)=x_1^2+x_2^2+x_3^2+\alpha(x_1+x_2+x_3)^2,\qquad \alpha>-\tfrac13.
\]
For \(M_t(\alpha)=\max_{N_t(x)=1}Q_\alpha(x)\) and \(L_t(\alpha)=\min_{N_t(x)=1}Q_\alpha(x)\), the **unrestricted** squared distance is \(\inf_{\alpha>-1/3}M_t(\alpha)/L_t(\alpha)\).

**3. Maximum on the norm sphere.** A positive quadratic form is convex, so its maximum over the clipped cube occurs at a vertex. When \(1<t<3\), all vertices are of two types: cube corners with coordinate sum \(\pm1\), or intersections of a slab face with two signed cube facets, represented up to permutation and global sign by \((1,1,t-2)\). Thus
\[
 M_t(\alpha)=\max\{3+\alpha,\ 2+(t-2)^2+\alpha t^2\}.
\]
The two expressions cross at \(\alpha_\times(t)=(3-t)/(1+t)\); the first wins for \(\alpha\le\alpha_\times\), the second for \(\alpha\ge\alpha_\times\).

**4. Minimum on the norm sphere.** The boundary of \(K_t\) consists of cube facets \(x_i=\pm1\) and sum facets \(x_1+x_2+x_3=\pm t\). On a sum facet, Cauchy–Schwarz gives the attained minimum \(L_1=t^2(\alpha+1/3)\), with \(x_1=x_2=x_3=\pm t/3\), feasible because \(t<3\). On a cube facet, take \(x_1=1\); symmetrizing the remaining two coordinates at fixed sum cannot increase \(Q_\alpha\). The unconstrained minimum over the sum \(s=x_1+x_2+x_3\) of \(1+(s-1)^2/2+\alpha s^2\) equals \(L_2=(1+3\alpha)/(1+2\alpha)\), at \(s_0=1/(1+2\alpha)\). It is always a lower bound for cube-facet values.

Put \(\alpha_1(t)=(3-t^2)/(2t^2)\). Since \(\alpha>-1/3\), comparing the positive quantities \(L_1,L_2\) gives \(L_1\le L_2\) precisely for \(\alpha\le\alpha_1\). There the feasible sum-facet witness proves \(L_t=L_1\), irrespective of cube-facet feasibility. When \(\alpha\ge\alpha_1\), we have \(0<s_0\le t^2/3<t\) and \((s_0-1)/2\in[-1,1]\); the point \((1,(s_0-1)/2,(s_0-1)/2)\) is a feasible cube-facet minimizer. Therefore, for **all** \(\alpha>-1/3\),
\[
 L_t(\alpha)=\min\left\{t^2(\alpha+\tfrac13),\frac{1+3\alpha}{1+2\alpha}\right\}.
\]

**5. Scalar optimization and phase boundaries.** On \(1<t<3\),
\[
 -\tfrac13<\alpha_1(t)<\alpha_\times(t),\qquad
 \alpha_1-\tfrac13=\frac{9-5t^2}{6t^2},\qquad
 \alpha_\times-\tfrac13=\frac{4(2-t)}{3(1+t)}.
\]
On \(\alpha\le\alpha_1\), the quotient \((3+\alpha)/L_1\) decreases strictly. On \(\alpha_1\le\alpha\le\alpha_\times\), \((3+\alpha)/L_2\) decreases up to \(\alpha=1/3\) and increases afterward: its derivative is
\[
 \frac{2(\alpha+1)(3\alpha-1)}{(3\alpha+1)^2}.
\]
On \(\alpha\ge\alpha_\times\), the quotient \([2+(t-2)^2+\alpha t^2]/L_2\) increases strictly; its derivative is
\[
 \frac{2(\alpha t+1)(3\alpha t+2t-3)}{(3\alpha+1)^2}>0,
\]
where both factors are positive already at \(\alpha=\alpha_\times\) for \(1<t<3\). Consequently the minimizer is the median of \(\alpha_1,1/3,\alpha_\times\):
\[
 \alpha_*(t)=\begin{cases}
 (3-t^2)/(2t^2),&1<t\le3/\sqrt5,\\
 1/3,&3/\sqrt5\le t\le2,\\
 (3-t)/(1+t),&2\le t<3.
 \end{cases}
\]
Substituting into \(M_t/L_t\) yields exactly the three asserted branches. Symmetric averaging at step 2 proves no nonsymmetric Euclidean norm can improve them. No uniqueness of optimal nonsymmetric positions is asserted.

## Computational corroboration
An independently implemented exact-rational vertex enumeration and cube-facet minimization checked 660 form/parameter pairs, including all three claimed regimes. It also symbolically verified the two derivative identities and the vertex-switch identity. These are finite checks, not proofs for all real \(t\) or all positive-definite quadratic forms; the preceding argument establishes the continuous statement. The original package's `verify_weighted_cycle.py` remains a valid broader diagnostic, including the known short-edge segment, but its short-edge output is not part of the new claim.

## Prior-work comparison and limitations
- *Opposite parity laws for exact Hilbert distortion of one-edge weighted cycles* (public Resultary record, 2026) gives the **entire** short-edge branch \(0<t\le1\) via the specialization \(n=4\). The present theorem does not claim that branch or the general cycle method.
- Godard, *Tree metrics and their Lipschitz-free spaces* (arXiv:0904.3178), Corollary 3.6, identifies the free space of a weighted tree with \(\ell_1^3\); this covers the tree endpoint \(t=3\), not the essential long-edge interval.
- Alexander–Fradelizi–García-Lirola–Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces* (arXiv:1911.10642), Theorem 4.1 gives the finite graph edge-quotient model, Proposition 3.9 identifies the equal-weight four-cycle cube case, and Section 5 addresses volume products. These results do not evaluate the long-edge distortion.
- Grundbacher–Kobos, *On certain extremal Banach–Mazur distances and Ader's characterization of distance ellipsoids* (DOI:10.1112/mtk.70062), treats optimal ellipsoid conditions and dimension-three maximizers, not the three-branch long-edge profile.

The result is limited to \(1<t<3\) and real scalars. A fully historical comparison with differently indexed three-dimensional cube-section/ellipsoid formulas remains a bibliographic limitation; no human priority certification is asserted. 
