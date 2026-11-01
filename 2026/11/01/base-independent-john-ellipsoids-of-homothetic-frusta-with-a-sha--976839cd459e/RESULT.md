# Base-independent John ellipsoids of homothetic frusta with a sharp contact transition

## Finding
Let \(n\ge 2\), put \(m=n-1\), and let \(B\subset\mathbb R^m\) be any full-dimensional compact convex body whose unique maximum-volume inscribed ellipsoid is the Euclidean unit ball \(\mathbb B_m\). No symmetry, smoothness, or polyhedral hypothesis on \(B\) is required. For \(0\le\lambda\le1\) define its normalized homothetic frustum
\[
F_\lambda(B)=\{(t,y)\in\mathbb R\times\mathbb R^m:0\le t\le1,\ y\in(1-(1-\lambda)t)B\}.
\]
Write \(\lambda_c=(n-1)/(n+1)\), and put
\[
(a_\lambda,b_\lambda^2)=
\begin{cases}
\bigl(1/((n+1)(1-\lambda)),\ (n-1)/(n+1)\bigr),&0\le\lambda\le\lambda_c,\\
\bigl(1/2,\lambda\bigr),&\lambda_c\le\lambda\le1.
\end{cases}
\]
Then the **unique John ellipsoid** of \(F_\lambda(B)\) is exactly
\[
\boxed{J(F_\lambda(B))=(a_\lambda,0)+\operatorname{diag}(a_\lambda,b_\lambda I_m)\mathbb B_n.}
\]
In particular, its shape is independent of every feature of the base other than the base's John ellipsoid. The upper cap misses the ellipsoid for \(\lambda<\lambda_c\), becomes tangent at \(\lambda_c\), and participates with strictly positive weight in a John certificate for \(\lambda>\lambda_c\). The lower cap and lateral supports participate throughout. For the unit-ball volume constants \(\kappa_d=\operatorname{vol}_d(\mathbb B_d)\),
\[
\frac{\operatorname{vol}_n J(F_\lambda(B))}{\operatorname{vol}_m J(B)}
=\frac{\kappa_n}{\kappa_m}\begin{cases}
\dfrac1{(n+1)(1-\lambda)}\left(\dfrac{n-1}{n+1}\right)^{(n-1)/2},&0\le\lambda\le\lambda_c,\\
\dfrac12\lambda^{(n-1)/2},&\lambda_c\le\lambda\le1.
\end{cases}
\]
This volume profile is continuously differentiable but not twice differentiable at the sharp threshold \(\lambda_c\). Below that threshold the optimal ellipsoid is the one belonging to the untruncated pyramid with the same apex; above it the optimal ellipsoid touches both parallel bases. These statements also apply to arbitrary non-normalized bases by the affine shear described below.

## Assumptions and scope
Here and below, the John ellipsoid is the unique ellipsoid of largest ordinary Euclidean volume contained in a full-dimensional compact convex body. All sections \((1-(1-\lambda)t)B\) are scalar homothetic copies of the same base, with the copies aligned; nonconcentric copies related by linear center drift can be reduced to this case by an affine shear. The two regimes overlap at \(\lambda=\lambda_c\), where their formulas agree. When \(\lambda=0\), the upper copy degenerates to the pyramid apex. When \(\lambda=1\), the frustum is the cylinder \([0,1]\times B\). The ambient dimension is \(n=m+1\); \(n=2\) is included.

For a general base with \(J(B)=p+Q\mathbb B_m\), where \(Q\) is invertible, first set \(B'=Q^{-1}(B-p)\). The affine map
\[
T_\lambda(t,x)=\bigl(t,\ (1-(1-\lambda)t)p+Qx\bigr)
\]
sends \(F_\lambda(B')\) onto \(F_\lambda(B)\); thus \(J(F_\lambda(B))=T_\lambda(J(F_\lambda(B')))\). In particular, the normalized volume ratio above holds for every base \(B\), whether or not its John center is the origin.

## Proof
**1. Feasible candidate.** In John position \(\mathbb B_m\subseteq B\), so it suffices to fit the proposed ellipsoid inside \(F_\lambda(\mathbb B_m)\). An axis-aligned ellipsoid centered at \((a,0)\), with axial semiaxis \(a\) and transverse semiaxis \(b\), is in this round frustum if and only if its height lies in \([0,1]\) and
\[
(1-\lambda)a+\sqrt{(1-\lambda)^2a^2+b^2}\le1.
\]
The left inequality follows by taking the support in all lateral directions \(((1-\lambda),u)\), \(\|u\|=1\), of the exact defining inequalities \((1-\lambda)t+u\cdot y\le1\). For the specified \(a_\lambda,b_\lambda\), the lateral inequality is an equality in both regimes. In the lower regime, \((1-\lambda)a_\lambda=1/(n+1)\) and the square root is \(n/(n+1)\); moreover \(2a_\lambda\le1\) holds exactly when \(\lambda\le\lambda_c\). In the upper regime, the two terms are \((1-\lambda)/2\) and \((1+\lambda)/2\), and the height interval is exactly \([0,1]\). The candidate is therefore contained in the required frustum.

**2. Base contact frame.** By the classical John contact characterization, since \(J(B)=\mathbb B_m\), there are finitely many unit contact normals \(u_i\) and positive weights \(c_i\) such that \(\langle u_i,y\rangle\le1\) supports \(B\) and
\[
\sum_i c_i u_i=0,\qquad \sum_i c_i u_i u_i^\mathsf T=I_m,\qquad\sum_i c_i=m.
\]
Consequently the corresponding lateral supporting planes of \(F_\lambda(B)\) are \((1-\lambda)t+\langle u_i,y\rangle\le1\). In coordinates normalized by the candidate ellipsoid, their contact points are
\[
z_i=(q,\sqrt{1-q^2}\,u_i),\qquad
q=\frac{(1-\lambda)a_\lambda}{1-(1-\lambda)a_\lambda}.
\]
The lower-cap contact is \(-e_1\); the upper-cap contact, when present, is \(+e_1\).

**3. Exact finite John certificate.** Give each lateral point \(z_i\) weight \(d_i=c_i/(1-q^2)\). Their total weight is \(W=m/(1-q^2)\). Add the axial weights
\[
\alpha=\frac{1-W(q^2+q)}2=\frac{1-nq}{2(1-q)},\qquad
\beta=\frac{1-W(q^2-q)}2=\frac{1+nq}{2(1+q)}
\]
on \(+e_1\) and \(-e_1\), respectively; a zero weight is omitted. The transverse first moment and axial–transverse mixed second moment vanish by \(\sum_i c_i u_i=0\). The transverse second moment is \((1-q^2)\sum_i d_i u_i u_i^\mathsf T=I_m\). The axial identities read
\[
\alpha-\beta+Wq=0,\qquad\alpha+\beta+Wq^2=1.
\]
Hence the entire first moment is zero and the full second moment is \(I_n\).

If \(\lambda\le\lambda_c\), then \(q=1/n\), so \(\alpha=0\) and \(\beta=n/(n+1)>0\), and the lower-cap plus lateral contacts give the certificate. If \(\lambda\ge\lambda_c\), then \(q=(1-\lambda)/(1+\lambda)\le1/n\), \(\beta>0\), and
\[
\alpha=\frac{(n+1)\lambda-(n-1)}{4\lambda}\ge0,
\]
with strict positivity precisely when \(\lambda>\lambda_c\). For that regime both caps and lateral contacts certify maximality. The sufficient direction of John's theorem gives the global maximum-volume inscribed ellipsoid. Uniqueness of the John ellipsoid gives the asserted classification without any symmetry assumption on \(B\).

**4. Volume and transition.** The determinant of the diagonal semiaxis matrix equals \(a_\lambda b_\lambda^m\); affine changes multiply numerator and denominator by \(|\det Q|\), giving the displayed ratio. Omitting a constant independent of \(\lambda\), the logarithmic volume is \(-\log(1-\lambda)\) in the first regime and \((m/2)\log\lambda\) in the second. At \(\lambda_c=m/(m+2)\), their derivatives both equal \((n+1)/2\), while their second derivatives equal \((n+1)^2/4\) and \(-(n+1)^2/(2m)\), respectively. Thus the positive volume is \(C^1\), but not \(C^2\). Finally, for \(\lambda<\lambda_c\), the candidate lies strictly below the upper cap; removing that cap leaves the same ellipsoid and the same lateral-plus-lower contact certificate. This proves the untruncated-pyramid assertion.

## Verification
The standalone standard-library script `check_frusta.py` checks the two support equalities, cap inequalities, all axial and transverse contact-moment coefficients, and exact isotropy of regular-simplex contact frames for dimensions \(2\) through \(14\). It uses rational arithmetic for 197 distinct dimension/parameter pairs, including every transition value and both endpoints. Run `python check_frusta.py` from the directory containing this file. The script is a finite consistency check; the proof above, based on the exact John certificate for an arbitrary base, is the universal justification.

## Relationship to prior work
The source motivating the axial-cut problem, Longfei–Zou–Liu (arXiv:2609.28447, first version September 23, 2026), proves Khachiyan's dimension-uniform inequality and exhibits a feasible ellipsoid for one axial cut of a specific circular cone. A published mathematical record, *Exact John ellipsoid of the Khachiyan half-cone* (2026), separately verifies that the specific half-cone ellipsoid is optimal. The present theorem does not claim that special case anew; it classifies every normalized homothetic frustum, over **arbitrary** convex bases (including asymmetric and nonsmooth ones), and proves the sharp all-parameter contact transition.

Güler–Gürtuna (arXiv:0709.0707, first version September 2007) give the general John-ellipsoid optimality framework, solve inscribed ellipsoids for *slabs cut from ellipsoids*, and study **minimum-volume covering** ellipsoids of truncated second-order cones; they explicitly say that they do not solve the corresponding *inscribed* ellipsoid problem for truncated cones. Their covering results and slab results do not imply the base-independent inscribed classification asserted here. John's contact theorem is used as a standard foundational tool and is not claimed as new. No claim is made about arbitrary nonhomothetic cross-sectional deformations.

## Limitations
The result assumes the two bases are homothetic (and parallel), and concerns ordinary John ellipsoids, not Löwner covering ellipsoids or other volume functionals. The upper and lower cap conditions are exact; there is no assertion that all boundary contacts of a nonsmooth base have been enumerated, only an explicit sufficient contact measure. Relevant older or unindexed work on pyramidal-frustum inscribed ellipsoids could alter historical priority. 

## References
1. Zhou Longfei, Haijun Zou, and Tianhao Liu, *A Spectral Proof of Khachiyan's Ellipsoid Conjecture*, arXiv:2609.28447v1 (September 23, 2026), https://arxiv.org/html/2609.28447.
2. Osman Güler and Filiz Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707 (September 2007), https://arxiv.org/abs/0709.0707.
3. *Exact John ellipsoid of the Khachiyan half-cone*, public mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-john-ellipsoid-of-the-khachiyan-half-cone--12746f7a27eb.
4. Fritz John, *Extremum problems with inequalities as subsidiary conditions*, Studies and Essays Presented to R. Courant (1948), 187–204; contact-characterization exposition: https://mathworld.wolfram.com/JohnEllipsoid.html.
