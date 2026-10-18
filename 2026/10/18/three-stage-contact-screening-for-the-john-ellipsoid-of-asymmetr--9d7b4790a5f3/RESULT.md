# Three-stage contact screening for the John ellipsoid of asymmetric book metrics

## Finding
Fix an integer \(m\ge3\), positive distances \(0<A<B\), and
\[
 B-A<t<A+B.
\]
Let \(M=\{u,v,z_1,\ldots,z_m\}\) carry the shortest-path metric on the graph with \(m\) triangles sharing \(uv\): the edges \(uz_i\) have length \(A\), the edges \(vz_i\) have length \(B\), and the common edge \(uv\) has length \(t\). In the canonical Euclidean hyperplane \(H=\{x\in\mathbb R^{m+2}:\sum x_j=0\}\), let \(K\) be the real Lipschitz unit ball, defined by \(|x_i-x_j|\le d(i,j)\). The maximum-volume inscribed (John) ellipsoid \(E_{m,A,B,t}\) is unique and has the following exact three-stage description.

Set \(\Delta=B^2-A^2>0\) and
\[
 t_1=\sqrt\Delta,\qquad
 t_2=\sqrt{\frac{A^2+B^2+\sqrt{(A^2+B^2)^2+(m^2-1)\Delta^2}}{m+1}}.
\]
These thresholds satisfy \(B-A<t_1<t_2<A+B\). Define
\[
 X(t)=\frac{t^2-\Delta}{2t},\quad
 Y(t)=\frac{t^2+\Delta}{2t},\quad
 U(t)=A^2-X(t)^2=B^2-Y(t)^2.
\]
Write \(b_{ij}=e_i-e_j\), and define a weighted Laplacian
\[
 L(a,b,c)=a\sum_{i=1}^m b_{uz_i}b_{uz_i}^{\mathsf T}
 +b\sum_{i=1}^m b_{vz_i}b_{vz_i}^{\mathsf T}
 +c\,b_{uv}b_{uv}^{\mathsf T}.
\]
All its restrictions below are positive definite on \(H\); a zero *conductance* does not denote a zero metric distance. The **unique John ellipsoid** is
\[
 \boxed{E_{m,A,B,t}=\{x\in H:x^{\mathsf T}L(a,b,c)x\le1\}},
\]
where \((a,b,c)\) is obtained from exactly one of the following continuous formulas:

**I. Short common edge, \(B-A<t\le t_1\):**
\[
 a=A^{-2},\qquad b=0,\qquad c=t^{-2}.
\]
**II. All-edge contact, \(t_1\le t\le t_2\):**
\[
 a=\frac{Y(t)}{tU(t)},\qquad
 b=\frac{X(t)}{tU(t)},\qquad
 c=\frac{U(t)-mX(t)Y(t)}{U(t)t^2}.
\]
**III. Large common edge, \(t_2\le t<A+B\):** writing
\[
 r=\frac{2A^2}{m\Delta+\sqrt{m^2\Delta^2+4A^2B^2}},
\]
set
\[
 a=\frac{m+r}{mA^2(1+r)},\qquad b=ra,\qquad c=0.
\]
On shared endpoints the formulas coincide exactly. In the three *open* phases, respectively, precisely \(m+1\), \(2m+1\), and \(2m\) distinct **unoriented edge pairs** yield tangent facets (twice these counts if oriented facets are counted). At both transition parameters all \(2m+1\) edge pairs are tangent, even though a supporting conductance vanishes there.

Let \(\kappa_d=\pi^{d/2}/\Gamma(d/2+1)\) be the Euclidean unit-ball volume. The intrinsic \((m+1)\)-volume is
\[
 \boxed{\operatorname{vol}_{m+1}(E_{m,A,B,t})=
 \frac{\kappa_{m+1}}{\sqrt{m+2}}
 \begin{cases}
 tA^m,&B-A<t\le t_1,\\
 tU(t)^{m/2},&t_1\le t\le t_2,\\
 t_2U(t_2)^{m/2},&t_2\le t<A+B.
 \end{cases}}
\]
In particular the optimal ellipsoid and its volume **remain exactly fixed** for \(t\ge t_2\), while the surrounding Lipschitz ball continues to enlarge strictly. The logarithmic volume is continuously differentiable but not twice differentiable at either threshold. Its one-sided curvature jumps are
\[
 (\log V)''(t_1^+)-(\log V)''(t_1^-)=-\frac{m}{A^2},
\]
\[
 (\log V)''(t_2^+)-(\log V)''(t_2^-)
 =\frac{(m+1)+(m-1)\Delta^2/t_2^4}{2U(t_2)}>0.
\]
At fixed \(A<B\), the intermediate phase narrows according to the sharp limit
\[
 \boxed{\lim_{m\to\infty}m(t_2-t_1)=\frac{A^2}{\sqrt{B^2-A^2}}.}
\]
These statements are collectively one exact ellipsoid, contact-transition and regularity theorem for this natural metric deformation.

## Assumptions and scope
The graph has \(m+2\) vertices, \(2m+1\) graph edges and dimension \(m+1\) after removing constant potentials. Because \(B-A<t<A+B\), the specified edge lengths are metrically essential: none is shortened by a competing path. The remaining distances are \(d(z_i,z_j)=2A\) for distinct leaves; their Lipschitz inequalities follow from the \(uz_i\) edges, so the listed \(2m+1\) constraints describe all of \(K\). The Euclidean metric throughout is inherited by the **zero-sum hyperplane** \(H\), not the anchored-coordinate Lebesgue metric. All assertions hold for every positive real \(A<B\), not only rational weights or normalized parameters. The strict inequalities exclude metric-degenerate endpoints; values and derivatives are understood one-sided inside this open parameter domain.

## Proof
**1. Global John criterion.** Let \(Q\) be any positive definite covariance operator on \(H\). The centered ellipsoid \(\{x\in H:x^{\mathsf T}Q^{-1}x\le1\}\) lies in \(K\) exactly when
\[
 b_{uz_i}^{\mathsf T}Qb_{uz_i}\le A^2,\qquad
 b_{vz_i}^{\mathsf T}Qb_{vz_i}\le B^2,\qquad
 b_{uv}^{\mathsf T}Qb_{uv}\le t^2.
\]
Maximizing \(\log\det_H Q\) over these linear inequalities is strictly concave and has a unique maximizer. If a feasible \(Q\) has \(Q^{-1}=L(a,b,c)\) with nonnegative conductances \(a,b,c\) and each positive conductance multiplies a tight inequality, then for any feasible \(Q'\),
\[
 \log\det_H Q'-\log\det_H Q
 \le\operatorname{tr}_H[Q^{-1}(Q'-Q)]
 =\sum_e w_e\bigl(b_e^{\mathsf T}Q'b_e-b_e^{\mathsf T}Qb_e\bigr)\le0.
\]
Strict concavity gives global uniqueness without restricting competitors to symmetry-invariant ellipsoids. No translated ellipsoid can do better: containment of both support directions implies \(\sqrt{b_e^{\mathsf T}Qb_e}+|b_e^{\mathsf T}y|\le\ell_e\), so recentering at zero preserves volume and feasibility; moreover the positively weighted tight edge vectors in all three phases span \(H\), forcing \(y=0\) in any equality case. Thus a feasible positive-weight support certificate is sufficient for the unique John ellipsoid.

**2. Three effective-resistance identities.** Put \(S=a+b\), \(T=mab+cS\) and let \(Q=L(a,b,c)^{-1}\) on \(H\). Whenever the positively weighted edges connect the graph, \(S,T>0\). Eliminating the \(m\) leaves by a Schur complement gives the effective resistance of the common edge:
\[
 R_{uv}=b_{uv}^{\mathsf T}Qb_{uv}=\frac{S}{T}.
\]
Conditioning an individual leaf on the two hubs, or evaluating the same Schur complement with that leaf retained, yields
\[
 R_{uz}=\frac1S+\left(\frac bS\right)^2\frac ST,\qquad
 R_{vz}=\frac1S+\left(\frac aS\right)^2\frac ST.
\]
These identities hold equally if exactly one of \(b,c\) vanishes, provided the remaining weighted graph is connected. Because leaf permutations preserve \(L\), the resistance does not depend on the choice of leaf. Set \(k=R_{uv}\), \(p=a/S\), and \(u_0=1/S\); the identities become
\[
 R_{uz}=u_0+(1-p)^2 k,\quad
 R_{vz}=u_0+p^2 k,\quad R_{uv}=k.
\]
They give all possible support values needed for the global optimality certificate.

**3. First regime and first threshold.** Let \(a=A^{-2}\), \(b=0\), \(c=t^{-2}\). The resulting graph is a spanning tree: the \(m\) short spokes and the hub edge. Its effective resistances are \(R_{uz}=A^2\), \(R_{uv}=t^2\), and \(R_{vz}=A^2+t^2\). Feasibility of the remaining long-spoke constraints is precisely \(t^2\le B^2-A^2=\Delta\). All positive conductances correspond to tight constraints, and the global John criterion proves the first formula. At \(t=t_1\), the long-spoke constraints become tangent despite carrying zero multipliers.

**4. Middle regime and the second threshold.** Require all three resistances to equal their squared lengths. The resistance differences give \(k=t^2\), \(1-p=X(t)/t\), \(p=Y(t)/t\), and \(u_0=U(t)\). Hence \(S=1/U\) and \(a,b\) are precisely the middle-regime formulas. Solving \(T=S/t^2=mab+cS\) gives \(c=(U-mXY)/(Ut^2)\). The equality
\[
 4\bigl(U(t)-mX(t)Y(t)\bigr)
 =2(A^2+B^2)-(m+1)t^2+(m-1)\frac{\Delta^2}{t^2}
\]
shows that the numerator of \(c\) is strictly decreasing for \(t>0\), is positive at \(t_1\), and negative at \(A+B\). It vanishes exactly once, at \(t=t_2\) above. Also \(X\ge0\) iff \(t\ge t_1\); \(Y>0\), and \(U>0\) throughout \((B-A,A+B)\). Therefore \(a,b,c\ge0\) exactly on \([t_1,t_2]\), and the global John criterion applies.

**5. Third regime and the strict plateau.** Put \(c=0\) and \(r=b/a>0\). The resistance identities simplify to
\[
 R_{uz}=\frac{m+r}{ma(1+r)},\quad
 R_{vz}=\frac{mr+1}{mar(1+r)},\quad
 R_{uv}=\frac{1+r}{mar}.
\]
Setting the first two equal to \(A^2\) and \(B^2\) produces
\[
 B^2r(r+m)=A^2(1+mr),
\]
which has exactly one positive root, the displayed radical expression. The corresponding \(a,b\) are therefore positive and both spoke orbits tangent. At \(t=t_2\) the middle formula has \(c=0\) and must equal this unique two-spoke solution; hence \(R_{uv}=t_2^2\). At any \(t\ge t_2\), the same \(Q\) is feasible, with strict hub slack for \(t>t_2\), and meets the global John criterion. Thus the ellipsoid does not depend on \(t\) in this regime. All \(2m\) spoke vectors span \(H\), so the centered optimum is the unique global optimum. A strict enlargement of \(K\) for two different \(t\) follows from choosing a potential with \(x_u-x_v=s\), all \(x_{z_i}=x_u-A\), and \(B-A<s<A+B\); subtracting its mean places it in \(H\). The long-spoke values are \(s-A\), within \([-B,B]\), so increasing the hub bound admits genuinely new points.

**6. Volume and contact counts.** The weighted spanning-tree polynomial of this book graph equals
\[
 \tau(a,b,c)=S^{m-1}(mab+cS)=S^{m-1}T.
\]
This follows by choosing either the common hub edge and one spoke for every leaf, or excluding the hub edge and choosing exactly one leaf with both spokes; in the latter case the other leaves choose independently. The matrix-tree theorem gives \(\det_H L=(m+2)\tau\). The ellipsoid volume is therefore \(\kappa_{m+1}/\sqrt{(m+2)\tau}\). In the first phase \(\tau=1/(A^{2m}t^2)\). In the middle phase \(S=1/U\), \(T=1/(Ut^2)\), and \(\tau=1/(U^m t^2)\). In the last phase the conductances equal those at \(t_2\), giving \(\tau=1/(U(t_2)^m t_2^2)\). This proves the three volume branches. The resistance inequalities above also give the precise tangent edge pairs: first the short spokes and common edge; then all edges; finally both spoke orbits but not the common edge. At both thresholds the limiting inactive orbit is tight, yielding the stated contact counts.

**7. Smoothness and shrinking middle regime.** Write \(V(t)\) for the intrinsic ellipsoid volume. Inside the middle phase,
\[
 \frac{d}{dt}\log V(t)=\frac{U(t)-mX(t)Y(t)}{tU(t)}.
\]
This equals \(1/t_1\) at the first threshold, agreeing with the first-branch derivative; it vanishes at the second threshold, agreeing with the constant final branch. At \(t=t_1\), \(U(t_1)=A^2\), \(U'(t_1)=0\) and \(U''(t_1)=-2\), yielding the first displayed second-derivative jump. Let \(G(t)=U(t)-mX(t)Y(t)\). Direct differentiation gives
\[
 G'(t)=-\frac{(m+1)t+(m-1)\Delta^2/t^3}{2}.
\]
Since \(G(t_2)=0\), the second derivative from the left is \(G'(t_2)/(t_2U(t_2))<0\), while the right second derivative is zero. Both jumps are nonzero, proving the sharp \(C^1\)-but-not-\(C^2\) conclusion. Finally, rewriting the positive root equation as
\[
 t_2^2-\Delta=\frac{2A^2}{m+1}
 +\frac{4A^2B^2}{(m+1)\bigl(\sqrt{m^2\Delta^2+4A^2B^2}+m\Delta\bigr)}
\]
shows \(m(t_2^2-\Delta)\to2A^2\), hence \(m(t_2-t_1)\to A^2/\sqrt\Delta\). This completes the proof.

## Verification
Run the standalone, standard-library-only program `verify_asymmetric_book.py` with `python3 verify_asymmetric_book.py` in the directory containing this document. Its 102 tested configurations encompass 96 full grounded-Laplacian inverse comparisons across all three phases, one exact-fraction middle-phase matrix check, four additional dimension/plateau checks, and one pair of independent finite-difference curvature checks. In addition, numerical optimization over unrestricted covariance matrices (not needed for the proof) was performed in 20 cases, and 80 parameter configurations were checked against full zero-sum Euclidean inverses. The determinant identities, KKT optimality certificate and strict differentiability statements are analytical proofs for all parameters; finite computations do not establish universal quantifiers.

## Relationship to prior work
Aliaga's 2021 study establishes the extreme-molecule framework for Lipschitz-free spaces; this theorem instead evaluates an ellipsoidal invariant of the dual Lipschitz ball for a specific metric deformation. Alexander and coauthors study finite Lipschitz-free polytopes and volume products; their statements do not evaluate the present optimal covariance. Suliman and Weinstein establish general effective-resistance and optimal-design machinery connecting graph Laplacians with ellipsoidal extremal problems; the KKT resistance approach here is an explicit **application of their framework**, not a newly claimed general theory.

The published *A sharp Löwner ellipsoid edge-invisibility threshold for book-graph symmetric edge polytopes* computes an outer ellipsoid for the **unit-edge** book graph. By polarity this is the corresponding symmetric member of the present type of John problem, but it does not cover \(A<B\) or the two continuous contact transitions. Previous weighted-book volume/covariance and cycle-projection calculations likewise concern different invariants. The present contribution is the exact global three-stage solution with unequal spoke classes, its strict pre-endpoint plateau, curvature jumps, and dimension-dependent boundary layer. No general novelty is claimed for the log-determinant criterion, matrix-tree theorem or effective-resistance identities.

## Limitations
The theorem is restricted to finite real Lipschitz spaces, equal lengths within each spoke orbit, integer \(m\ge3\), positive unequal spoke lengths \(A<B\), and the strict triangle domain. Its intrinsic Euclidean ellipsoid is **not** a claim of affine-normalized extremality or of a John ellipsoid for arbitrary book-graph edge weights. A similar formulation hidden under effective-resistance or optimal-design terminology remains a bibliographic possibility despite the specified comparisons. Finite tests and self-review are not independent scientific validation.

## References
1. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first posted 2021-02-01; primary MSC2020 46B20), https://arxiv.org/abs/2102.01219.
2. S. Alexander, M. Fradelizi, A. García-Lirola, and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (2019), https://arxiv.org/abs/1911.10642.
3. M. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966 (2023), https://arxiv.org/abs/2302.05966.
4. A. D'Alì, E. Delucchi, and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019), https://arxiv.org/abs/1910.05193.
5. A. Mori, K. Mori, and H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287 (2023), https://arxiv.org/abs/2312.11287.
6. *A sharp Löwner ellipsoid edge-invisibility threshold for book-graph symmetric edge polytopes*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-l-wner-ellipsoid-edge-invisibility-threshold-for-book-gr--87e035ae5886.
