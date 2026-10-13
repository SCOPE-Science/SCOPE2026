# Four variables attain the sharp scalar quadratic Rademacher-chaos constant
## Finding
Let \(\varepsilon_1,\ldots,\varepsilon_4\) be independent random signs, each taking \(\pm1\) with probability \(1/2\), and let
\[
h=\sum_{{1\le i<j\le4}} a_{{ij}}\varepsilon_i\varepsilon_j
\]
be a nonzero real scalar homogeneous quadratic Rademacher chaos. Then
\[
\|h\|_2\le 2\|h\|_1.
\]
The constant \(2\) is sharp. Equality holds exactly when, after permuting the coordinates,
\[
h=c(\varepsilon_i+s\varepsilon_j)(\varepsilon_k+t\varepsilon_l),
\]
where \(\{{i,j\}}\sqcup\{{k,l\}}=\{{1,2,3,4\}}\), \(s,t\in\{{-1,1\}}\), and \(c\ne0\).

The corresponding best constants for real scalar quadratic chaoses on \(2\), \(3\), and \(4\) variables are \(1\), \(\sqrt2\), and \(2\), respectively. Thus four variables are the first finite dimension in which the conjectured scalar degree-two constant is already attained.

## Assumptions and scope
The coefficients are real scalars. The result does not claim the vector-valued Pełczyński conjecture, the complex-scalar case, or any statement for arbitrary numbers of variables. The comparison uses the probability norms \(\|h\|_p=(\mathbb E|h|^p)^{1/p}\).

The literature motivation is Ivanisvili and Tkocz, arXiv:1807.04358, whose first public version is dated 2018-07-11 and whose primary classification is 60E15. Their Remark 6 records the conjectured degree-two constant \(C_{{1,2,2}}=2\), attained by the product \((x_1+x_2)(x_3+x_4)\), while Remark 7 states that sharp moment-comparison constants remain open in the relevant low-moment regime.

## Proof
Define
\[
u=\varepsilon_1\varepsilon_2,\qquad
v=\varepsilon_1\varepsilon_3,\qquad
w=\varepsilon_1\varepsilon_4.
\]
The triple \((u,v,w)\) is uniform on \(\{-1,1\}^3\), and
\[
h=q(u,v,w)=a_{{12}}u+a_{{13}}v+a_{{14}}w+a_{{23}}uv+a_{{24}}uw+a_{{34}}vw.
\]
Put \(\chi(u,v,w)=uvw\). Since \(q\) contains only Walsh characters of degrees one and two,
\[
\sum_{{(u,v,w)}}q(u,v,w)=0,
\qquad
\sum_{{(u,v,w)}}\chi(u,v,w)q(u,v,w)=0.
\]
Therefore the four values of \(q\) on each parity class \(\chi=1\) and \(\chi=-1\) separately have sum zero.

We use one elementary lemma. If \(y_1,\ldots,y_4\in\mathbb R\) and \(\sum_r y_r=0\), then
\[
\sum_r|y_r|\ge\sqrt2\left(\sum_r y_r^2\right)^{{1/2}}.
\]
Indeed, if \(P\) is the sum of the positive entries, then it is also the absolute sum of the negative entries, so \(\sum_r|y_r|=2P\). The sum of squares of the positive entries is at most \(P^2\), and the same is true for the negative entries, giving \(\sum_r y_r^2\le2P^2\). Equality in this lemma holds exactly when there is one positive nonzero entry, one negative nonzero entry, and the remaining two entries are zero.

Let \(y_+\) and \(y_-\) denote the four-value vectors of \(q\) on the two parity classes. Applying the lemma twice gives
\[
\|y_+\|_1+\|y_-\|_1
\ge\sqrt2(\|y_+\|_2+\|y_-\|_2)
\ge\sqrt2\sqrt{\|y_+\|_2^2+\|y_-\|_2^2}.
\]
Since \(q\) is uniform on eight points,
\[
\|h\|_1=\frac{\|y_+\|_1+\|y_-\|_1}{8},
\qquad
\|h\|_2=\frac{\sqrt{\|y_+\|_2^2+\|y_-\|_2^2}}{\sqrt8}.
\]
The displayed inequalities therefore yield \(\|h\|_2\le2\|h\|_1\).

For equality, equality in the second step forces one parity class to vanish identically. Equality in the zero-sum lemma on the other parity class then forces exactly two nonzero values, equal in magnitude and opposite in sign. Conversely, such a two-point reduced support gives equality. Any two distinct points in one parity class of \(\{-1,1\}^3\) differ in exactly two coordinates. Coordinate sign changes and permutations therefore reduce the support to \((1,1,1)\) and \((-1,-1,1)\). The unique reduced quadratic with values \(4c\), \(-4c\), and zero at the other six points is
\[
c(1+w)(u+v)=c(\varepsilon_1+\varepsilon_4)(\varepsilon_2+\varepsilon_3).
\]
Undoing the cube symmetries gives exactly the stated family \(c(\varepsilon_i+s\varepsilon_j)(\varepsilon_k+t\varepsilon_l)\). Every member of that family is nonzero with probability \(1/4\), takes magnitude \(4|c|\) there, and hence has \(\|h\|_2/\|h\|_1=2\).

For three variables, the same reduction gives four values of a mean-zero function \(a u+b v+cuv\). The zero-sum lemma directly yields \(\|h\|_2\le\sqrt2\|h\|_1\), with equality for \(h=\varepsilon_1(\varepsilon_2+\varepsilon_3)\). With two variables a nonzero quadratic chaos is a single monomial and has ratio \(1\). This proves the finite-dimensional profile and minimality statement.

## Verification
The proof is analytic. The accompanying checker constructs the eight-by-six Walsh evaluation matrix, verifies the two parity-class zero-sum identities symbolically over integer coefficient basis vectors, verifies all twelve factorized equality patterns, and exhaustively checks the equality-support correspondence among the twelve unordered pairs of reduced cube points lying in a common parity class. These checks support the bookkeeping and equality classification; they are not a substitute for the norm argument.

## Relationship to prior work
Ivanisvili and Tkocz prove improved general moment-comparison bounds for Rademacher chaoses. Their Remark 6 says that for \(p=1\), \(q=2\), the conjectured best degree-two constant is \(2\), and cites Oleszkiewicz's 1999 chapter for Pełczyński's conjecture. Their displayed sharpness example already uses four variables, but the inspected paper does not state that every real scalar quadratic chaos on four variables obeys the conjectured bound, nor does it classify equality in that finite dimension.

Targeted searches for a four-variable quadratic-chaos \(L^1\)-to-\(L^2\) theorem, the finite-dimensional Pełczyński constant, and an equivalent homogeneous Walsh-polynomial formulation did not locate a covering statement. The closest indexed Walsh results concern different support-size or phase-flatness questions and do not imply this norm comparison.

## Limitations
The result settles only the real scalar problem through four variables. It neither proves the conjecture for arbitrary dimension nor addresses arbitrary normed-space coefficients. The 1999 Oleszkiewicz chapter cited as the historical source of the conjecture was identifiable bibliographically but was not available in full through the inspected public sources, so an equivalent finite-four-variable observation there or in unindexed notes remains a residual originality risk.

## References
1. P. Ivanisvili and T. Tkocz, "Comparison of moments of Rademacher chaoses," arXiv:1807.04358, first public 2018-07-11; *Arkiv för Matematik* 57 (2019), 121–128, DOI:10.4310/ARKIV.2019.V57.N1.A7.
2. K. Oleszkiewicz, "Comparison of moments via Poincaré-type inequality," in *Advances in Stochastic Inequalities*, Contemporary Mathematics 234 (1999), 135–148.
