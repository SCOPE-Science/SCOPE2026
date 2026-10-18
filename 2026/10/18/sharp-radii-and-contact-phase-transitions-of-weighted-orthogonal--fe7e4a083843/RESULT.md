# Sharp radii and contact phase transitions of weighted orthogonal discotopes

## Finding

For every integer \(d\geq 3\), choose strictly positive real radii \(a_1,\ldots,a_d\). In the standard Euclidean space \(\mathbb R^d\), let
\[
D_i(a_i)=\{x\in\mathbb R^d:x_i=0,\ \|x\|_2\leq a_i\},
\qquad K(a)=D_1(a_1)+\cdots+D_d(a_d).
\]
The following gives the exact Euclidean inradius, circumradius, and **all** contacts of the centered optimal balls, including every parameter-boundary case.

Put \(W=\sum_{i=1}^d a_i\), \(a_{\max}=\max_i a_i\), and order the weights as \(0<a_{(1)}\leq\cdots\leq a_{(d)}\). The maximum radius of a Euclidean ball contained in \(K(a)\) is
\[
\boxed{r(K(a))=W-a_{\max}.}
\]
The centered radius-\(r(K(a))\) ball contacts \(K(a)\) in exactly the points \(\pm r(K(a))e_i\) with \(a_i=a_{\max}\); there are exactly twice as many contacts as largest-weight coordinates.

There is a **unique** integer \(k\in\{2,\ldots,d\}\) such that, on defining
\[
\tau_k=\sqrt{\frac{\sum_{j=1}^k a_{(j)}^2}{k-1}},
\qquad a_{(d+1)}=+\infty,
\]
one has \(a_{(k)}<\tau_k\leq a_{(k+1)}\). The Euclidean circumradius is
\[
\boxed{R(K(a))=\sum_{j=k+1}^d a_{(j)}+
\sqrt{(k-1)\sum_{j=1}^k a_{(j)}^2}.}
\]
Its minimum enclosing Euclidean ball has the origin as its **unique** center. This sphere contacts \(K(a)\) in precisely \(2^k\) points \(R(K(a))u\), where
\[
u_{(j)}=\begin{cases}
\pm\sqrt{1-a_{(j)}^2/\tau_k^2},&1\leq j\leq k,\\
0,&k<j\leq d.
\end{cases}
\]
All sign choices in the first \(k\) coordinates occur independently. This description remains exact when an inactive weight equals \(\tau_k\), because that coordinate still has zero normal component. Every contact count \(2^2,2^3,\ldots,2^d\) is realized by a strictly positive weight profile.

For \(d=3\), if the weights are ordered \(a\leq b\leq c\), the complete sharp phase diagram reduces to
\[
R=\begin{cases}
\sqrt{2(a^2+b^2+c^2)},&c<\sqrt{a^2+b^2}\quad(8\text{ contacts}),\\
c+\sqrt{a^2+b^2},&c\geq\sqrt{a^2+b^2}\quad(4\text{ contacts}).
\end{cases}
\]
Thus a genuine four-to-eight contact bifurcation occurs exactly at the Pythagorean threshold; the boundary case has four distinct contacts.

Finally, among all positive weight vectors with prescribed total \(W\), the equal-weight discotope **simultaneously maximizes the inradius and minimizes the circumradius**, uniquely in each case:
\[
\boxed{r\leq\frac{d-1}{d}W,\qquad
R\geq\sqrt{\frac{d-1}{d}}\,W,\qquad
\frac Rr\geq\sqrt{\frac d{d-1}}.}
\]
Equality in any of these three sharp inequalities occurs if and only if \(a_1=\cdots=a_d\). In contrast, every weight vector of total \(W\) has the same mean Euclidean width,
\[
\operatorname{mw}(K(a))=
2W\frac{\Gamma(d/2)^2}{\Gamma((d-1)/2)\Gamma((d+1)/2)}.
\]

## Assumptions and scope

The summands are **full Euclidean \((d-1)\)-balls in the coordinate hyperplanes**, not ellipsoids, their convex hull, or a collection of arbitrarily oriented discs. Weights are finite and strictly positive. The Euclidean balls and their radii are measured in the ambient Euclidean norm. The term contact refers to a common point of the convex body's boundary and the relevant centered radius-optimal sphere. The inradius permits any center, while the circumradius minimizes over all centers. The theorem does not classify all centers of largest inscribed balls.

## Proof

**1. Support function and symmetry.** For any unit vector \(u\), the orthogonal projection of \(u\) onto the hyperplane \(x_i=0\) has length \(\sqrt{1-u_i^2}\). Support-function additivity therefore gives
\[
h_{K(a)}(u)=\sum_{i=1}^d a_i\sqrt{1-u_i^2}.
\]
Every summand is centrally symmetric and their sum has interior, so \(K(a)=-K(a)\). Its largest centered inscribed ball has radius \(\min_{\|u\|_2=1}h_{K(a)}(u)\); no off-center ball has larger radius because the two support constraints at \(u\) and \(-u\) give \(r+|c\cdot u|\leq h_{K(a)}(u)\) for any inscribed radius-\(r\) ball centered at \(c\). Likewise the minimum enclosing ball has center zero: for every \(x\in K(a)\), the points \(x,-x\) both lie in \(K(a)\), and averaging their squared distances to a proposed center \(c\) gives \(\|x\|_2^2+\|c\|_2^2\). Taking \(x\) of largest norm shows strictly worse radius unless \(c=0\).

**2. Smallest support and inner contacts.** Set \(s_i=u_i^2\). The vector \(s\) ranges exactly over the probability simplex \(s_i\geq0\), \(\sum_i s_i=1\), and the support is
\[
F(s)=\sum_{i=1}^d a_i\sqrt{1-s_i}.
\]
Because every \(a_i>0\), \(F\) is strictly concave on this simplex. A concave function has its minimum at a vertex, and strict concavity makes the minimizers **only** vertices. At vertex \(e_i\) its value is \(W-a_i\). Hence the inradius and the complete list of inner contact normals and contact points follow. A radius-\(r\) centered ball cannot have an additional contact direction, because its support is exactly \(r\) in every unit direction.

**3. Largest support and active set.** By the preceding reduction, the circumradius is \(\max_{s\in\Delta}F(s)\). At a vertex \(e_i\), transferring a small mass \(\varepsilon>0\) to any other coordinate increases the term \(a_i\sqrt\varepsilon\), whereas the loss elsewhere is of order \(\varepsilon\); thus no maximizer is a vertex. Strict concavity gives one maximizing \(s\), with each \(s_i<1\).

The Karush–Kuhn–Tucker equality and one-sided inequalities for maximizing \(F\) imply that for a common \(\tau>0\),
\[
s_i>0\ \Longrightarrow\ \frac{a_i}{\sqrt{1-s_i}}=\tau
\ \Longrightarrow\ s_i=1-\frac{a_i^2}{\tau^2},\quad a_i<\tau;
\]
\[
s_i=0\ \Longrightarrow\ a_i\geq\tau.
\]
Consequently the active indices are exactly the \(k\) smallest weights, and \(k\geq2\). Summing their coordinates gives
\[
1=k-\frac{\sum_{j\leq k}a_{(j)}^2}{\tau^2},
\qquad \tau=\tau_k.
\]
This proves the displayed threshold rule. Existence follows from the maximizer and uniqueness from strict concavity. Evaluating \(F\) at this point yields \(\sum_{j>k}a_{(j)}+\sum_{j\leq k}a_{(j)}^2/\tau_k\), the stated radius. When an inactive weight is exactly \(\tau_k\), its optimum coordinate remains zero, so there is no extra active sign choice.

**4. All outer contacts.** For every maximizing unit normal \(u\), a supporting point \(x\in K(a)\) exists and satisfies \(u\cdot x=h_{K(a)}(u)=R\). Since \(\|x\|_2\leq R\), equality in Cauchy–Schwarz forces \(x=Ru\). Conversely any point \(x\in K(a)\) with \(\|x\|_2=R\) forces \(u=x/R\) to maximize the support. The unique optimal square-coordinate vector \(s\), with exactly \(k\) positive entries, therefore gives exactly \(2^k\) outer contact points and no others.

Each phase actually occurs: for a prescribed \(2\leq k<d\), choose the first \(k\) weights equal to one and all remaining weights equal to a number strictly larger than \(\sqrt{k/(k-1)}\); then the active size is \(k\). All equal weights give the \(k=d\) phase. The tridisc threshold is obtained by comparing \(a_{(3)}\) with \(\sqrt{a_{(1)}^2+a_{(2)}^2}\).

**5. Sharp fixed-mean-width roundness.** For any positive weights, \(a_{\max}\geq W/d\), so \(r=W-a_{\max}\leq W(d-1)/d\), with equality only for equal weights. Testing the unit normal with every squared coordinate \(1/d\) gives
\[
R\geq\sqrt{1-1/d}\,W,
\]
and equal weights make that direction maximizing by the strict-concavity argument. Conversely, equality in this circumradius bound forces the all-equal-squares direction to maximize \(F\), whose interior stationarity equations require every \(a_i\) to be equal. Dividing the two bounds proves the sharp radius ratio and its equality classification. The standard spherical beta integral gives
\[
\mathbb E_{u\in S^{d-1}}\sqrt{1-u_i^2}
=\frac{\Gamma(d/2)^2}{\Gamma((d-1)/2)\Gamma((d+1)/2)},
\]
so twice the average support is the asserted mean width. This last observation highlights that the sharp roundness extremizer cannot be deduced from mean width alone.

## Verification

Run the standalone file `check_geometry.py` with Python 3 from the extracted package. It checks 390 deterministic strictly positive weight profiles in dimensions three through eight, comparing the claimed formula with the maximum among candidates on **all** active-coordinate faces. It additionally checks 136,500 direct random support evaluations and the sharp radius-ratio inequality, and prints the four-to-eight tridisc transition and its boundary. Its computations use floating point and random sampling; they are consistency checks only. The proof above supplies the all-dimensional statements and equality cases.

## Relationship to prior work

Gesmundo and Meroni's *The Geometry of Discotopes* introduced and analyzed semialgebraic discotopes and, in Section 7, treated the unit-weight sum of three coordinate-plane discs through an algebraic boundary of degree 24. Mathis and Meroni's *Fiber Convex Bodies*, Section 5.2, established discotope support-function and fiber-body machinery. Those works supply the natural objects and preceding structural theory. The present statement is the exact Euclidean radius, all-weight/all-dimensional outer-contact phase classification, and simultaneous sharp fixed-mean-width extremal property; the generic support-function principle and the standard concave-programming conditions are not claimed to be new.

## Limitations

No claim is made for arbitrarily tilted summand hyperplanes, ellipsoidal rather than spherical summands, or any volume-optimal John or Löwner ellipsoid. All optimal-center loci of inscribed balls are not described. The comparison with earlier literature is under best-knowledge access; an equivalent older geometric radius theorem may exist. Numerical checks establish no result beyond their finite tested inputs. There has been no independent mathematical audit.

## References

1. L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406, initial public version 26 May 2021; full text: https://link.springer.com/article/10.1007/s00454-022-00451-3 .
2. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241, initial public version 1 November 2021; full text: https://arxiv.org/html/2111.01241v2 .
