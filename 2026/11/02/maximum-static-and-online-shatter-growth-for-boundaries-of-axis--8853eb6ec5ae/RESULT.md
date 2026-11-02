# Maximum static and online shatter growth for boundaries of axis-aligned ellipses

## Finding

Let \(\mathcal E\) denote the class of the **boundaries**, rather than the filled interiors, of all nondegenerate real axis-aligned ellipses in \(\mathbb R^2\). For every integer \(n\geq0\), there are \(n\) distinct points \(X_n\) whose ellipse-boundary traces are **exactly** the subsets of size at most four:

\[\{E\cap X_n:E\in\mathcal E\}=\{S\subseteq X_n:|S|\leq4\}.\]

For any prescribed \(n\) distinct points on the unit circle in its open first-quadrant arc, \(X_n\) can be chosen arbitrarily close to those points. As a result the VC and Littlestone shatter functions simultaneously attain the maximum bound, for all integers \(n\geq0\):

\[\pi_{\mathcal E}(n)=\rho_{\mathcal E}(n)=\sum_{j=0}^{\min\{4,n\}}\binom nj.\]

In particular \(\operatorname{VCdim}(\mathcal E)=\operatorname{Ldim}(\mathcal E)=4\). The latter equality itself was known; the all-length maximum shatter-function assertion for this **positive diagonal-parameter subfamily** is the contribution here.

## Assumptions and scope

An axis-aligned ellipse boundary is the nonempty real zero locus of a quadratic polynomial

\[a x^2+b y^2+c x+d y+e\quad(a>0,\ b>0),\]

whose minimum value is strictly negative, so its real locus is a nondegenerate ellipse. The coefficient vector is considered only up to a nonzero scalar. Membership is equality to zero, not positivity or interior containment. The trace of an ellipse on a finite point set records exactly those points on its boundary.

The VC shatter function is the maximum number of distinct traces on an \(n\)-point set. The Littlestone shatter function is the maximum number of realizable leaves of a complete binary query tree of depth \(n\), with arbitrary sample-point queries at internal nodes and a separate ellipse concept allowed for each realizable leaf. No constraints are placed on the relative location of the ellipses, only on their axes.

## Proof

**1. Four-point rank on a quarter-circle.** Introduce the lift \(v(x,y)=(x^2,y^2,x,y,1)\in\mathbb R^5\). Let \(p_i=(t_i,\sqrt{1-t_i^2})\) be distinct points, \(0<t_i<1\). On the unit circle every lifted row satisfies \(v(p_i)\cdot w_0=0\) for \(w_0=(1,1,0,0,-1)\). Every four distinct rows are linearly independent. Indeed, using \(y^2=1-x^2\), a linear combination of the lift coordinates restricts to a function \(A+Bt+Ct^2+D\sqrt{1-t^2}\). If it vanishes at four distinct arguments, Rolle's theorem forces its third derivative to vanish somewhere strictly between them. That derivative is \(-3Dt/(1-t^2)^{5/2}\); hence \(D=0\). The remaining quadratic has four zeros and is identically zero. Thus the only coefficient dependence among the four underlying functions on this arc is the circle equation; every four distinct lift rows have rank four. For fewer than four rows, independence follows by extension to a four-point subset of the arc.

**2. Positivity-preserving interpolation.** Fix finitely many distinct points of the arc. Every four-row matrix has rank four and one-dimensional nullspace spanned by \(w_0\). Under small simultaneous perturbations of their point coordinates, the rank remains four and its normalized kernel varies continuously near \(w_0\); in particular its first two entries stay positive and its corresponding real conic stays nondegenerate and nonempty. There are only finitely many quadruples, so one common open neighborhood preserves all these properties.

**3. Avoiding all five-fold incidence.** For each five-element index set \(I\), the determinant \(\det(v(q_i))_{i\in I}\) is a polynomial in the coordinates of the five points. It is not the zero polynomial: the five points \((0,0),(1,0),(-1,0),(0,1),(0,-1)\) have independent lifts. Consequently the nonzero set of each such determinant is dense open. Intersect these finitely many dense open sets with the common interpolation neighborhood from step 2. The intersection contains arbitrarily close perturbations \(X_n\) in which every four rows are independent, every four points lie on a nondegenerate axis-aligned ellipse, and every five lift rows are independent. The case \(n<5\) requires no five-row determinants, and the case \(n<4\) uses any small generic perturbation of its given circle points.

**4. Every trace of size at most four.** Fix any index subset \(S\) with \(|S|\le4\). The linear coefficient subspace \(L_S=\{w:v(q_i)\cdot w=0\text{ for all }i\in S\}\) contains a coefficient vector of a nondegenerate axis-aligned ellipse: for \(n\ge4\), extend \(S\) to a four-subset and use step 2; for \(n<4\), the unchanged unit circle or a sufficiently small perturbation of it solves the constraints. The valid-ellipse coefficients form a relatively open nonempty subset of \(L_S\). For each \(j\notin S\), the condition \(v(q_j)\cdot w=0\) defines a **proper** hyperplane inside \(L_S\), since the rows indexed by \(S\cup\{j\}\) are independent (at most five rows, and all five independent for \(n\ge5\)). A finite union of proper linear hyperplanes cannot contain a nonempty relative open subset of \(L_S\). Choose a valid ellipse coefficient vector outside their union: this ellipse meets \(X_n\) in exactly \(S\). Conversely no ellipse meets five sample points, since no nonzero coefficient vector annihilates five independent lifted rows. Thus the trace family is precisely the claimed down-set of order four.

**5. Upper bounds and online maximality.** For any five distinct planar sample points, if their lifted rows are independent no nonzero quadratic coefficient can vanish at all five. If dependent, a minimal dependence has some lifted row in the span of the others, preventing a Boolean labeling with zeros on those others but a nonzero value at the chosen row. Hence no five points are shattered, even by the larger class of *all* nontrivial zero sets of linear combinations of the five lift coordinates. For online depth five, consider the five queries on an all-positive branch. At each node the negative child requires some coefficient annihilating the previously queried positive rows but not the new row. Thus the next row is not in the span of the previous ones, and the five rows along this path must be independent. The all-positive leaf would then require a nonzero coefficient annihilating five independent rows, impossible. This proves both dimensions at most four. Since the traces on \(X_4\) include all 16 patterns, both dimensions are at least four. For arbitrary \(n\), the \(n\)-point configurations of step 4 exhibit \(\sum_{j=0}^{\min(4,n)}\binom nj\) distinct traces, and a level-balanced decision tree with these queries exhibits the same number of realizable leaves. The Sauer–Shelah and thicket (online Sauer) bounds give the matching upper bounds from dimension four. This proves both equalities for all \(n\ge0\).

## Verification

The standalone standard-library Python program `verify_ellipse_maximum.py` uses exact rational arithmetic and fraction-free determinants. For ten explicit rational points, it checks every one of the \(\binom{10}{4}=210\) quadruple-interpolation kernels for positive diagonal quadratic coefficients and every one of the \(\binom{10}{5}=252\) five-row determinants for nonvanishing. It also checks that the four-point ellipse kernels contain no extraneous points. These checks prove the claimed **386** traces on that particular ten-point configuration when combined with proof step 4. The program is not used as proof for arbitrary \(n\): the general result follows from the rank, perturbation and hyperplane arguments.

Run `python3 verify_ellipse_maximum.py` using Python 3 with no nonstandard dependencies. Expected lines:

```text
AXIS_ELLIPSE_EXACT_WITNESS_PASS points=10 quadruples=210 quintets=252 traces=386
ALL_DETERMINANT_CHECKS_RATIONAL_PASS
```

## Relationship to prior work

Guingona, Kolesnikov, Nierwinski and Soucy (arXiv:2109.04805v1, September 2021), Theorem 3.10 and Example 6.2, established that boundaries of axis-aligned ellipses have VC and Littlestone dimensions four; the source gives separate maximum shatter-function results for the **larger unrestricted five-function zero-set class**. Example 6.2 explicitly distinguishes that unrestricted class from the positive diagonal-parameter ellipse subfamily and notes the difficulty of transferring the maximality result. The present result establishes maximum growth for the restricted ellipse class using a new circle-arc rank and perturbation argument. It does not claim that the earlier dimension equality was unknown. Mészáros's 2019 work on shattering-extremal set systems studies a distinct finite-system notion and does not yield the restricted ellipse-boundary theorem in the inspected material.

## Limitations

The construction for every sample size is nonconstructive in its generic perturbation choice, although a ten-point exact rational instance is provided. The assertion is specifically about **ellipse boundaries**, not filled ellipses, rotated ellipses or other conics. Maximum growth means the best attainable trace count at every cardinality, not that every generic planar point configuration attains this count. Independent validation has not been performed; historical-priority risk remains for differently phrased geometry or zero-set maximality results.

## References

1. Vincent Guingona, Alexei Kolesnikov, Julie Nierwinski, Richard Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1 (first posted 2021-09-10), particularly Theorems 3.10, 5.6 and Example 6.2; https://arxiv.org/html/2109.04805v1.
2. Tamás Mészáros, *Standard monomials and extremal point sets*, arXiv:1908.03045v1 (2019), Sections 1–3; https://arxiv.org/html/1908.03045v1.
3. S. Bhaskar, *Thicket density*, Journal of Symbolic Logic 86 (2021), 110–127; online Sauer inequality as quoted in reference 1.
