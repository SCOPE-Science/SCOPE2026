# Contact-rank laws for the disappearing volume gap of spherical Minkowski sums

## Finding

Let \(d\ge2\) and let \(Q=-Q\subset\mathbb R^d\) be a full-dimensional convex polytope centered at the origin. Write \(B=B_2^d\), \(S=\partial B\), and
\[
G_Q(\lambda)=\operatorname{vol}_d\bigl((B+\lambda Q)\setminus(S+\lambda Q)\bigr),\qquad\lambda>0.
\]
This is the volume missed when the spherical boundary, rather than the solid ball, is added to the polytope. Let \(R=\max_{q\in Q}\|q\|_2\) and let \(F\) be all vertices of \(Q\) of norm \(R\). Put \(W=\operatorname{span}F\), \(s=\dim W\), and \(P=\operatorname{conv}F\subset W\). The polar \(P_W^\circ\) is taken intrinsically in the Euclidean space \(W\):
\[
P_W^\circ=\{y\in W:\langle y,v\rangle\le1\ \text{for all }v\in P\}.
\]
Then \(G_Q(\lambda)>0\) precisely for \(0<\lambda<1/R\), and \(G_Q(\lambda)=0\) for \(\lambda\ge1/R\). With \(\delta=1-\lambda^2R^2\), its sharp critical asymptotic is
\[
\boxed{G_Q(\lambda)=C_Q\,\delta^{(d+s)/2}\bigl(1+O_Q(\delta)\bigr),\quad\lambda\uparrow1/R,}
\]
where the positive, explicit coefficient is
\[
\boxed{C_Q=\left(\frac R2\right)^s\operatorname{vol}_s(P_W^\circ)
\frac{\pi^{(d-s)/2}\Gamma(s+1)}{\Gamma\!\left(s+1+(d-s)/2\right)}.}
\]
In particular, the critical exponent depends only on the dimension of the linear span of the farthest vertices. No generic-position or simplicity assumption is needed.

**Sharp planar phase transition.** For \(a\ge b>0\), let \(Q_{a,b}=\operatorname{conv}\{(\pm a,0),(0,\pm b)\}\) and \(0<\lambda<1/a\). If \(a>b\), define
\[
\lambda_0=\frac{2b}{a^2+b^2}.
\]
For every \(\lambda_0\le\lambda<1/a\), the missing region is exactly the interior of the lens of two closed unit disks centered at \((\pm\lambda a,0)\), and
\[
\boxed{G_{Q_{a,b}}(\lambda)=2\left[\arccos(\lambda a)-\lambda a\sqrt{1-\lambda^2a^2}\right].}
\]
The formula strictly overestimates \(G_{Q_{a,b}}(\lambda)\) for all \(0<\lambda<\lambda_0\), so the threshold is exact. For \(a>b\),
\[
G_{Q_{a,b}}(\lambda)=\frac43(1-\lambda^2a^2)^{3/2}\bigl(1+O_{a,b}(1-\lambda^2a^2)\bigr).
\]
At the symmetric boundary \(a=b\), the exponent changes sharply:
\[
G_{Q_{a,a}}(\lambda)=(1-\lambda^2a^2)^2\bigl(1+O_a(1-\lambda^2a^2)\bigr).
\]
This rank jump explains why the two-disk lens approximation cannot persist all the way to the threshold for the square diamond.

## Assumptions and scope

All volumes use standard Lebesgue measure, and volumes and polars inside \(W\) use its induced Euclidean metric. The sum \(S+\lambda Q\) is a compact, not necessarily convex set. Its convex hull is \(B+\lambda Q\), because \(\operatorname{conv}S=B\) and \(Q\) is convex. The set \(F\) is nonempty, antipodally symmetric, and its convex hull has nonempty intrinsic interior containing \(0\), so \(P_W^\circ\) is bounded with positive intrinsic volume. The parameters \(d\), \(Q\), and its vertex set are fixed during \(\lambda\uparrow1/R\). The implied constants need not be uniform when the shape of \(Q\) changes, especially when another vertex norm approaches \(R\). The theorem makes no claim about nonsymmetric polytopes or smooth convexifiers.

## Proof

**1. The missing set is an erosion.** For \(x\in B+\lambda Q\), the convex set \(x-\lambda Q\) intersects \(B\). It intersects \(S\) exactly when it is not wholly contained in \(\operatorname{int}B\): if some point is inside \(B\) and another is outside its interior, a segment within \(x-\lambda Q\) reaches \(S\). Hence
\[
(B+\lambda Q)\setminus(S+\lambda Q)=H_\lambda
:=\{x:x-\lambda Q\subset\operatorname{int}B\}.
\]
Since \(Q=-Q\), the latter is an open, centrally symmetric convex set, and
\[
H_\lambda=\left\{x:\max_{q\in\operatorname{vert}Q}\|x+\lambda q\|_2^2<1\right\}.
\]
The reduction to vertices is valid because the squared norm is convex. If \(0<\lambda<1/R\), then \(0\in H_\lambda\) and the gap has positive volume. If \(\lambda\ge1/R\), pick \(v\in F\); the average of \(\|x+\lambda v\|_2^2\) and \(\|x-\lambda v\|_2^2\) equals \(\|x\|_2^2+\lambda^2R^2\ge1\), so \(H_\lambda\) is empty.

**2. Localization to the farthest vertices.** Put \(\delta=1-\lambda^2R^2>0\) and \(h_P(y)=\max_{v\in P}\langle y,v\rangle\). The antipodal pairs in \(F\) imply that every \(x\in H_\lambda\) satisfies
\[
\|x\|_2^2+2\lambda h_P(\Pi_W x)<\delta.
\]
Since \(0\) lies in the intrinsic interior of \(P\), there exists \(c>0\) such that \(h_P(y)\ge c\|y\|_2\) for \(y\in W\). Consequently \(\|x\|_2\le\sqrt\delta\) and \(\|\Pi_W x\|_2=O_Q(\delta)\) when \(\lambda\) stays near \(1/R\).

Every vertex \(q\notin F\) has \(\|q\|_2^2\le R^2-\gamma\), with one uniform \(\gamma>0\) if such vertices exist. On the ball \(\|x\|_2\le\sqrt\delta\),
\[
\|x+\lambda q\|_2^2\le\delta+2\lambda R\sqrt\delta+\lambda^2(R^2-\gamma)<1
\]
for sufficiently small \(\delta>0\). Thus all the shorter-vertex inequalities are strictly redundant near the critical point. For such \(\lambda\), the exact defining inequality is just
\[
\|x\|_2^2+2\lambda h_P(\Pi_W x)<\delta.
\]

**3. Anisotropic blow-up and coefficient.** Set \(m=d-s\) and use the orthogonal decomposition \(\mathbb R^d=W\oplus W^\perp\). Substitute \(x=\delta y+\sqrt\delta\,z\), where \(y\in W\) and \(z\in W^\perp\). The Jacobian is \(\delta^{s+m/2}\), and the exact rescaled domain is
\[
D_\delta=\{(y,z):\delta\|y\|_2^2+\|z\|_2^2+2\lambda h_P(y)<1\}.
\]
As \(\lambda=R^{-1}\sqrt{1-\delta}\), these bounded domains tend to
\[
D_0=\{(y,z):\|z\|_2^2+(2/R)h_P(y)<1\}.
\]
All \(D_\delta\) for small \(\delta\) lie in a fixed bounded set, by the positive lower bound on \(h_P(y)/\|y\|\). On that bounded set the two defining functions differ by at most \(C\delta\). Thus, for some \(C>0\),
\[
\{\|z\|^2+(2/R)h_P(y)<1-C\delta\}
\subset D_\delta\subset
\{\|z\|^2+(2/R)h_P(y)<1+C\delta\}.
\]
The volume of \(\{\|z\|^2+(2/R)h_P(y)<t\}\) scales as \(t^{s+m/2}\). It follows that \(\operatorname{vol}_d(D_\delta)=\operatorname{vol}_d(D_0)(1+O_Q(\delta))\). For fixed \(z\) in the unit ball of \(W^\perp\), the \(y\)-slice is \((R/2)(1-\|z\|^2)P_W^\circ\). Hence
\[
\operatorname{vol}_d(D_0)=\left(\frac R2\right)^s\operatorname{vol}_s(P_W^\circ)
\int_{\|z\|<1}(1-\|z\|^2)^s\,dz.
\]
The beta integral is
\[
\int_{\|z\|<1}(1-\|z\|^2)^s\,dz
=\frac{\pi^{m/2}\Gamma(s+1)}{\Gamma(s+1+m/2)},
\]
including \(m=0\) with the convention that the zero-dimensional unit ball has volume one. Multiplying by the Jacobian proves the theorem and positivity of \(C_Q\).

**4. Exact rhombus cutoff.** The four vertices of \(Q_{a,b}\) yield, in the first quadrant, exactly the inequalities
\[
x^2+y^2+2\lambda a x+\lambda^2a^2<1,\qquad
x^2+y^2+2\lambda b y+\lambda^2b^2<1.
\]
Ignoring the second pair produces the interior of the lens \(L_\lambda\) formed by intersecting the two closed unit disks centered at \((\pm\lambda a,0)\). On the closed lens the maximum of \(x^2+(|y|+\lambda b)^2\) is attained at \(x=0\), \(|y|=\sqrt{1-\lambda^2a^2}\). Indeed, for \(x\ge0\), the lens has \(|y|\le\sqrt{1-(x+\lambda a)^2}\), and the resulting squared expression
\[
1-\lambda^2a^2-2\lambda a x+2\lambda b\sqrt{1-(x+\lambda a)^2}+\lambda^2b^2
\]
is strictly decreasing in \(x\). Therefore the short-vertex constraints are redundant throughout \(L_\lambda\) exactly when
\[
\sqrt{1-\lambda^2a^2}+\lambda b\le1
\ \Longleftrightarrow\ \lambda\ge\frac{2b}{a^2+b^2}.
\]
Below this threshold, a neighborhood just inside the upper lens tip violates a short-vertex constraint; the removed set has positive area. In the redundant regime the two-disk intersection has standard exact area \(2[\arccos(\lambda a)-\lambda a\sqrt{1-\lambda^2a^2}]\). The asymptotic coefficients follow from the general theorem: for \(a>b\), \(s=1\), \(P=[-a,a]\), and \(\operatorname{vol}_1(P^\circ)=2/a\), giving \(C_Q=4/3\). For \(a=b\), \(s=2\), \(P^\circ=[-1/a,1/a]^2\), giving \(C_Q=1\).

## Verification

The companion program `verify.py` independently integrates the quadrant cross-sections for the rhombus, compares them with the two-disk lens formula on both sides of the sharp threshold, and checks the predicted \(3/2\)-power and \(2\)-power laws. It also verifies a three-dimensional two-ball lens coefficient and the full-rank cross-polytope coefficient. The actual run returned `PASS: 20 quadrature/asymptotic checks and rank-3 coefficient check`. Execute from the package directory using `python verify.py` with SciPy installed as specified in `requirements.txt`. These finite tests detect normalization and sign errors; the theorem for every dimension and every polytope is proved by the preceding argument, not by numerical samples.

## Relationship to prior work

Van Hintum (2026) obtains sharp thresholds for convexification in **equal-weight repeated Minkowski averages** and measures Hausdorff nonconvexity. Fradelizi, Madiman, Marsiglietti, and Zvavitch (2018) treat several measures of nonconvexity, including the volume deficit, primarily for sequences of repeated averages. Neither argument specializes to an exact critical volume expansion for the **two-summand** set \(S+\lambda Q\), whose summands are a sphere and a polytope.

Hernández Cifre and Saorín (2010) study the volumes and quermassintegrals of general relative inner parallel bodies and bounds involving alternating Steiner polynomials. The identification of the cavity with such an erosion is standard and is not claimed as original here. The contribution is the farthest-vertex contact-rank law, its explicit polar coefficient and remainder, and the sharp rhombus shielding transition.

Meyer (preprint first available October 19, 2026) treats qualitative finite convexification of compact-plus-convex sums by exposed-face criteria. It covers the general qualitative question of when a sum becomes convex but provides no volume-gap contact-rank asymptotic in the inspected statements and proofs. This later work is a comparison, not the source establishing the present work's chronological classification.

## Limitations

The asymptotic is for fixed centrally symmetric full-dimensional *polytopes*; it need not be uniform as vertex radii coalesce. The exact rhombus lens formula is only asserted at and above the derived shielding cutoff; below it the true gap is strictly smaller. The spherical-boundary-to-erosion identity is classical. The date and classification of the motivating 2026 preprint are directly verified, but bibliographic completeness cannot be proved by finite database searches; possible older equivalent special cases or general erosion asymptotics remain a priority risk. The result has received an self-review only; no independent audit or formal certification is represented.

## References

- Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815 (first posted June 9, 2026), https://arxiv.org/abs/2606.10815.
- Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, Artem Zvavitch, *The convexification effect of Minkowski summation*, EMS Surveys in Mathematical Sciences 5 (2018), https://arxiv.org/abs/1704.05486.
- M. A. Hernández Cifre and E. Saorín, *On the volume of inner parallel bodies*, Advances in Geometry 10 (2010), 275–286, https://webs.um.es/mhcifre/preprints/saorin%20vol_inner.pdf.
- M. A. Hernández Cifre and E. Saorín, *On inner parallel bodies and quermassintegrals*, Israel Journal of Mathematics 177 (2010), 29–47, https://doi.org/10.1007/s11856-010-0037-6.
- Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744 (first posted October 19, 2026), https://arxiv.org/abs/2610.26744 (qualitative later-priority comparison only).
