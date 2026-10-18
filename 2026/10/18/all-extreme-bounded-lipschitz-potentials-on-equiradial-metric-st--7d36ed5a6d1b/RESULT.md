# All extreme bounded-Lipschitz potentials on equiradial metric stars

## Finding

Fix an integer \(m\ge 2\) and a real \(\rho>0\). Let \(S=\{o,v_1,\ldots,v_m\}\) have the metric
\[
d(o,v_i)=\rho,\qquad d(v_i,v_j)=2\rho\quad(i\ne j).
\]
Write a real function as \(f=(f_0,f_1,\ldots,f_m)\), with \(f_0=f(o)\), and equip \(\mathbb R^{m+1}\) with the **sum-normalized** bounded-Lipschitz norm
\[
N_\rho(f)=\max_{0\le j\le m}|f_j|+\rho^{-1}\max_{1\le i\le m}|f_i-f_0|.
\]
Set \(a=\rho/(\rho+2)\) and \(b=\rho/(\rho+1)\). The unit ball \(B_\rho=\{f:N_\rho(f)\le1\}\) has *exactly* the following extreme points:

1. The two constant functions \(f=\mathbf1\) and \(f=-\mathbf1\).
2. The functions \(f=a(s_0,s_1,\ldots,s_m)\), for signs \(s_j\in\{-1,1\}\) with at least one leaf sign different from the center sign.
3. The functions \(f=b(0,s_1,\ldots,s_m)\), for leaf signs \(s_i\in\{-1,1\}\) which include **both** signs.

All displayed points are distinct and exposed. In particular,
\[
\boxed{|\operatorname{ext}(B_\rho)|=3\cdot 2^m-2,}
\]
independently of \(\rho>0\). The three families contain respectively \(2\), \(2(2^m-1)\), and \(2^m-2\) points.

The classification also gives a closed-form dual norm for **every** real signed atomic measure, including nonzero-total-mass measures. Given \(\mu=\sum_{j=0}^m c_j\delta_{v_j}\), where \(v_0=o\), and a vector \(c=(c_1,\ldots,c_k)\) of length \(k\ge2\), define
\[
H_k(c)=\begin{cases}
\sum_j|c_j|-2\min_j|c_j|,&\text{if all }c_j>0\text{ or all }c_j<0,\\
\sum_j|c_j|,&\text{otherwise.}
\end{cases}
\]
Then the dual norm is precisely
\[
\boxed{\|\mu\|_{\mathrm{BL}}^*=\max\!\left\{
\left|\sum_{j=0}^m c_j\right|,
\frac{\rho}{\rho+2}H_{m+1}(c_0,\ldots,c_m),
\frac{\rho}{\rho+1}H_m(c_1,\ldots,c_m)
\right\}.}
\]
The same ball has **exactly**
\[
\boxed{2m(m+1)\text{ facets}.}
\]
An irredundant complete facet list is obtained from the valid inequalities
\[
\alpha f_v+\frac{\beta}{\rho}(f_i-f_0)\le1,
\qquad 0\le v\le m,\quad 1\le i\le m,\quad \alpha,\beta\in\{-1,1\},
\]
by retaining **precisely** the cases: \(v=0\) with \(\alpha=-\beta\); \(v=i\) with \(\alpha=\beta\); and \(v\notin\{0,i\}\) with \(\alpha=-\beta\). Both face counts are independent of the common arm length.

The dual formula uses only \(O(m)\) real arithmetic and comparisons, rather than a linear program or an exponential vertex list.

## Assumptions and scope

All functions, coefficients and convex combinations are **real**. The star includes only its center and \(m\) leaves, not the edge interiors. All arms have the same positive length. The Lipschitz seminorm is the maximum over center–leaf edges; every leaf–leaf quotient is bounded by that edge maximum because of the tree metric. The norm is the **sum** of supremum and Lipschitz terms, not their maximum. The unit ball is full-dimensional and compact in \(\mathbb R^{m+1}\).

## Proof

**1. Lift the ball to an elementary polytope.** Introduce a scalar \(t\), and let
\[
Q_\rho=\left\{(f,t):0\le t\le1,\quad |f_j|\le t\ (0\le j\le m),\quad |f_i-f_0|\le\rho(1-t)\ (1\le i\le m)\right\}.
\]
This is a bounded polytope in \(\mathbb R^{m+2}\). Its projection to the \(f\)-coordinates is exactly \(B_\rho\): a point \(f\) admits such a \(t\) exactly when
\[
\max_j|f_j|\le t\le1-\rho^{-1}\max_i|f_i-f_0|.
\]
If \(N_\rho(f)=1\), the interval collapses, so the lift is unique and equals \(t=\max_j|f_j|\). Furthermore, a boundary point \(f\) is extreme in \(B_\rho\) **if and only if** its unique lift is a vertex of \(Q_\rho\). For the nontrivial direction, suppose the lift is a vertex and \(f\) is a midpoint of two points in \(B_\rho\). Lift those two points to \(Q_\rho\). Their midpoint lies over \(f\), hence coincides with the unique boundary lift; vertex extremality forces the two lifts to coincide. The reverse direction follows because a nontrivial segment through the unique lift projects to a nontrivial segment through \(f\).

**2. Locate vertices with \(0<t<1\).** None of the two bounds on \(t\) is active. If a leaf coordinate \(f_i\) satisfies both \(|f_i|<t\) and \(|f_i-f_0|<\rho(1-t)\), it can be perturbed independently, so the point is not a vertex. Consequently, at every vertex each leaf satisfies at least one of the two *equalities* \(|f_i|=t\) and \(|f_i-f_0|=\rho(1-t)\). Choose one active equality per leaf. These yield \(m\) independent rows because each row has a coefficient \(\pm1\) in its own leaf coordinate, absent from all other chosen rows. Since the ambient dimension is \(m+2\), two further independent active conditions are necessary.

The only possible further conditions are (a) the center equality \(|f_0|=t\), and (b) a *double-saturated leaf* satisfying both \(|f_i|=t\) and \(|f_i-f_0|=\rho(1-t)\). For \(0<t<1\) and \(|f_0|\le t\), the only double-saturation patterns are
\[
\begin{aligned}
 f_i=t,\quad f_0&=t-\rho(1-t)\quad\text{(positive)},\\
 f_i=-t,\quad f_0&=-t+\rho(1-t)\quad\text{(negative)}.
\end{aligned}
\]
Indeed, the two opposite combinations would require \(|f_0|>t\).

If the center equality is active, a further independent condition demands a double-saturated leaf. If \(f_0=t\), only negative double saturation is possible, yielding \(2t=\rho(1-t)\), hence \(t=a\). The allowed interval for every leaf is then exactly \([-a,a]\); to be a vertex, every leaf is an endpoint \(\pm a\), and at least one is \(-a\). The case \(f_0=-t\) is its negative. These are exactly family 2.

If the center equality is *not* active, two independent double-saturation constraints are necessary. Two positive doubles yield the same scalar equation for \((f_0,t)\), as do two negative doubles, so there must be at least one of each. Their two equations give \(f_0=0\) and \(t=\rho/(\rho+1)=b\). Both the box and edge constraints on every leaf then reduce to \(|f_i|\le b\), and leaf activity forces each \(f_i\in\{-b,b\}\). Both signs occur by the two required doubles. These are exactly family 3.

Conversely, every listed point in family 2 has \(m\) independent leaf-box equalities, one center-box equality and one extra opposite-leaf edge equality, giving \(m+2\) independent active equations. Every point in family 3 has \(m\) independent leaf-box equalities and two extra edge equalities at opposite-signed leaves, again of rank \(m+2\). Hence the lifts are vertices of \(Q_\rho\). Direct substitution gives \(N_\rho(f)=1\) in both families, so their projections are extreme.

**3. Endpoint levels.** At \(t=0\), every coordinate must vanish, so the only lift is \((0,0)\), whose projection is the *interior* point \(f=0\); it is not a vertex of \(B_\rho\). At \(t=1\), all leaf values equal the center, with center in \([-1,1]\). The only endpoint vertices are the lifts of the constant functions \(\pm\mathbf1\). Both constants are exposed by the linear functionals \(\pm\sum_j f_j\). Thus families 1–3 exhaust the extreme points, and every such point is exposed because a vertex of a full-dimensional finite polytope is exposed. Counting the disjoint sign families gives \(2+2(2^m-1)+(2^m-2)=3\cdot2^m-2\).

**4. Classify the facets.** Since the sum of two finite maxima equals the maximum over all pairs of maximizing terms, the norm condition is equivalent to the inequalities indexed by \((v,i,\alpha,\beta)\). A particular inequality supports a facet exactly when its signed coordinate \(\alpha f_v\) can be the **unique** maximizer of \(\max_j|f_j|\), while its signed edge \(\beta(f_i-f_0)\) is the **unique** maximizer of \(\max_j|f_j-f_0|\). Simultaneous strict uniqueness gives a relatively open portion of the supporting hyperplane and hence a facet. Conversely, if strict simultaneous uniqueness is impossible, every equality point lies in the finite union of intersections with other distinct supporting hyperplanes and cannot contain a facet's relative interior. The normals of distinct inequalities in the three retained families are distinct for all \(\rho>0\).

For \(v=0\), strict uniqueness is possible exactly when \(\alpha=-\beta\): a center attaining the supremum cannot have an edge continuing farther outward. For \(v=i\), strict uniqueness requires \(\alpha=\beta\), since an edge pointing inward toward the leaf would put the center farther outward. For \(v\notin\{0,i\}\), strict uniqueness requires \(\alpha=-\beta\): if \(\alpha=\beta\), a largest-sign leaf \(v\) has an edge difference at least as large as that of leaf \(i\), forcing a Lipschitz tie.

All three permitted types have strict witnesses. Up to global negation, choose respectively: \(f_0=-2\), \(f_i=-1\), all other leaves \(-3/2\) for \(v=0,\alpha=-1,\beta=1\); \(f_0=0\), \(f_i=2\), all other leaves \(1/2\) for \(v=i,\alpha=\beta=1\); or \(f_0=1\), \(f_i=-1\), \(f_v=2\), all remaining leaves \(1\) for \(v\notin\{0,i\},\alpha=1,\beta=-1\). Rescaling each witness by its positive \(N_\rho\) makes the target inequality an equality, still uniquely. The total number of facets is therefore
\[
2m+2m+2m(m-1)=2m(m+1),
\]
with no degeneracy at any positive arm length.

**5. Dual formula.** A linear functional attains its maximum over \(B_\rho\) at a vertex. The constant family contributes \(|\sum_{j=0}^m c_j|\). The other two families contribute \(a\) and \(b\) times, respectively, the maximal signed scalar product among sign vectors which are *not constant*. For an arbitrary real coefficient vector of length \(k\ge2\), that maximum equals \(H_k\): if its coefficients have opposite signs or include a zero, the signed \(\ell_1\) maximum can be obtained by a nonconstant sign vector; if all coefficients share one strict sign, at least one sign must be reversed, and reversing a smallest-magnitude coefficient loses exactly twice its magnitude. This proves the dual formula and its linear arithmetic complexity.

## Verification

The complete standalone verification program is `verify.py`. Its standard-library exact-rational procedure independently enumerates all vertices directly from the original halfspace description for five small cases, including a three-leaf star; all match the claimed lists. The script separately checks 1,500 exact-rational dual-norm values over sample integer measures and positive rational radii. When SciPy and NumPy are installed, it also performs 288 independent primal linear-program checks across up to seven leaves, compares numerical halfspace intersections with the entire predicted vertex lists, and verifies the irredundant facet counts by active-rank computations. Run `python verify.py` (NumPy/SciPy are optional).

The infinite family theorem, both face counts, the polynomial-time dual formula and exposure assertion follow from the proof above. Finite computations alone would not establish any of those general claims.

## Relationship to prior work

Hille and Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions* (first arXiv public version of 15 May 2023), prove general extremal/norming constructions and treat finite metric spaces in their Section 6; that section emphasizes the difficulty of a full elementary finite-space classification, and does not give the equiradial-star facet list or its exact count. A general finite-metric face-dimension criterion can be specialized to recover vertex membership; the point here is the explicit simultaneous vertex/facet census and all-mass formula, not a new general-purpose extremality test.

The previously available *Exact Dudley norms and mass-imbalance thresholds on equiradial stars* gives a sharp two-branch formula for **zero-total-mass** signed measures on finite or countable stars. It explicitly does not cover nonzero-total-mass measures or identify all extreme points. For \(\sum_j c_j=0\), the dual formula above reduces to its known value
\[
\max\left\{\frac{\rho}{\rho+1}\sum_{i=1}^m|c_i|,\ \frac{\rho}{\rho+2}\left(\sum_{i=1}^m|c_i|+\left|\sum_{i=1}^m c_i\right|\right)\right\}.
\]
**No originality is claimed for this zero-total-mass specialization**; the contribution here is the exact irredundant facet system and count, the complementary vertex census, and the nonzero-total-mass dual norm for finite equiradial stars. The 2023 general finite-dimensional LP method can evaluate such measures numerically but does not itself state the displayed explicit all-mass formula or vertex count.

## Limitations

The theorem is restricted to finite *equiradial* stars, real functions, and sum-normalization. It does not treat unequal arm radii, complex-valued potentials, or infinite stars at the level of extreme-point counting. The algorithm uses ordinary exact arithmetic/real comparisons and is not a claim about finite-precision numerical stability. The zero-total-mass dual subcase was already known. Although relevant searchable literature and public research records were compared, an equivalent finite-polytope description in unindexed work cannot be categorically excluded. No independent audit is asserted.

## References

1. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500v1, first publicly submitted 2023-05-15, https://arxiv.org/abs/2305.08500.
2. *Exact Dudley norms and mass-imbalance thresholds on equiradial stars*, publicly available research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-dudley-norms-and-mass-imbalance-thresholds-on-equiradial-s--ecc3b6450a54.
3. S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet-Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234, https://arxiv.org/abs/2206.12234 (context for earlier computational approaches; not a source of the star vertex theorem).
