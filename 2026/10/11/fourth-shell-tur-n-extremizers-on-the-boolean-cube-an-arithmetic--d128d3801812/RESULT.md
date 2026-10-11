# Fourth-shell Turán extremizers on the Boolean cube: an arithmetic resonance

## Finding

Let \(d\ge13\), \(G_d=\mathbb F_2^d\), and \(S_4=\{x\in G_d:|x|=4\}\), with \(|x|\) the Hamming weight. Let \(\mathcal T_d\) be the largest **counting-measure** mass \(\sum_{x\in G_d}f(x)\) among positive-definite \(f:G_d\to\mathbb C\) satisfying \(f(0)=1\) and \(\operatorname{supp}f\subseteq\{0\}\cup S_4\). These functions are real because every element of \(G_d\) is its own inverse.

Define
\[
K_4^{(d)}(k)=\sum_{j=0}^4(-1)^j\binom{k}{j}\binom{d-k}{4-j},\qquad
m_d=\min_{0\le k\le d}K_4^{(d)}(k)<0,\qquad a_d=-1/m_d.
\]
Then the sharp mass is
\[
\boxed{\mathcal T_d=1+\binom d4 a_d.}
\]
The complete equality theory exhibits an infinite arithmetic resonance: the sole extremizer is \(f(0)=1\), \(f(s)=a_d\) for \(s\in S_4\), and zero elsewhere, **unless**
\[
\boxed{3d-8=t^2\quad\text{for an integer }t\ge7\text{ with }3\nmid t.}
\]
At those and only those exceptional dimensions, every extremizer has the form
\[
f_w(0)=1,\qquad f_w(s)=a_d+\sum_{i\in s}w_i\quad(s\in S_4),\qquad f_w(x)=0\quad(x\notin\{0\}\cup S_4),
\]
where \(w\in\mathbb R^d\) satisfies \(\sum_{i=1}^dw_i=0\) and all the explicit Fourier inequalities
\[
1+a_d K_4^{(d)}(k)
-\frac{(d-2k)((d-2k)^2-3d+8)}{3}
\sum_{i\in Y}w_i\ \ge0
\quad\text{for every }Y\subseteq\{1,\ldots,d\}\text{ of size }k,
\quad 0\le k\le d.
\]
This optimizer set is a full-dimensional compact convex polytope in the \((d-1)\)-dimensional space \(\sum_iw_i=0\), with the origin in its relative interior. The first exceptional dimensions are \(d=19,24,36,43,59,68\). In particular, the exceptional/nonexceptional distinction is not simply the parity of the dimension.

## Assumptions and scope

The Walsh transform is unnormalized: \(\widehat f(Y)=\sum_{x\in G_d}f(x)(-1)^{|x\cap Y|}\), identifying vectors with subsets of \(\{1,\ldots,d\}\). Positive definiteness is equivalent to \(\widehat f(Y)\ge0\) for every \(Y\). The objective uses a sum, not the mean \(2^{-d}\sum f\). No assumption of pointwise nonnegativity of \(f\) is made. The theorem covers every integer \(d\ge13\), all complex-valued admissible positive-definite functions (which are automatically real), and all equality cases. It does not claim a formula for dimensions below \(13\) or for other Hamming shells.

## Proof

**1. Radial sharpness.** Average any feasible \(f\) over permutations of the \(d\) coordinates. Write the resulting value on \(S_4\) as \(c\). Coordinate permutations preserve positive definiteness, normalization, support and total mass. The unnormalized Walsh transform of the radial average at a character of weight \(k\) is \(1+cK_4^{(d)}(k)\). Writing \(m_d<0\) for the minimum gives \(c\le-1/m_d=a_d\). Conversely, the radial function with value \(a_d\) on \(S_4\) has nonnegative Walsh transform at all weights by the definition of \(m_d\). Hence the stated sharp mass and a radial extremizer follow.

**2. Character-zero constraints for every extremizer.** If \(f\) is an extremizer, its mean value on \(S_4\) is \(a_d\). For any \(k\) minimizing \(K_4^{(d)}\), the average of \(\widehat f(Y)\) over \(|Y|=k\) is \(1+a_dm_d=0\). Each summand is nonnegative, so it vanishes separately. Setting \(h(s)=f(s)-a_d\) for \(s\in S_4\), this says
\[
\sum_{|s|=4}(-1)^{|s\cap Y|}h(s)=0\qquad\text{for all }Y\text{ with }|Y|=k.
\]

**3. The restricted Walsh transform on harmonic slices.** The standard harmonic multilinear decomposition of functions on the Boolean level \(\binom{[d]}4\) is the orthogonal sum of its degrees \(j=0,1,2,3,4\); the degree-\(j\) component is spanned by the products
\[
q_j(s)=\prod_{\ell=1}^j\bigl(\mathbf1_{u_\ell\in s}-\mathbf1_{v_\ell\in s}\bigr)
\]
for disjoint pairs \((u_\ell,v_\ell)\). These components have respective dimensions \(\binom dj-\binom d{j-1}\) (interpreting \(\binom d{-1}=0\)). This is the explicit harmonic-slice basis theorem; see Filmus in the references (his Theorem 9 and preceding basis construction). Whenever \(4\le k\le d-4\), its restriction to the \(k\)-th Boolean level remains injective and distinct harmonic degrees remain independent there.

For one such product, Fourier summation over each paired choice shows exactly that
\[
\sum_{|s|=4}(-1)^{|s\cap Y|}q_j(s)
=(-2)^j K_{4-j}^{(d-2j)}(k-j)q_j(Y),\qquad |Y|=k.
\]
Indeed, a pair separated by \(Y\) contributes \(-2\) times its signed incidence difference, while an unseparated pair gives zero; the remaining \(4-j\) choices yield the indicated Krawtchouk sum. Writing \(t=d-2k\), the five multipliers are
\[
\begin{array}{c|c}
j&\lambda_j(k)\\\hline
0&K_4^{(d)}(k)\\
1&-t(t^2-3d+8)/3\\
2&2(t^2-d+4)\\
3&-8t\\
4&16
\end{array}.
\]
Therefore the kernel of the weight-\(k\) restriction is exactly the sum of those harmonic-degree subspaces where the corresponding multiplier vanishes.

**4. Arithmetic of minimizing levels.** A direct expansion gives
\[
24K_4^{(d)}(k)=\bigl(t^2-(3d-4)\bigr)^2-(6d^2-18d+16).
\]
Thus a minimizing weight is one for which \(t^2\), with \(t\equiv d\pmod2\) and \(|t|\le d\), is closest to \(3d-4\). For \(d=13,14,15,16\), direct substitution gives minimizing weights, respectively, \(\{4,9\}\), \(\{4,10\}\), \(\{4,11\}\), and \(\{5,11\}\). For \(d\ge17\), the two adjacent nonnegative parity-compatible integers surrounding \(\sqrt{3d-4}\) are at most \(\sqrt{3d-4}+2\le d-8\). A minimum therefore occurs only at \(4\le k\le d-4\). Choosing a parity-compatible integer within distance one of the square root also gives \(K_4^{(d)}(k)<0\): the squared discrepancy is at most \((d+1)^2\), strictly less than \(6d^2-18d+16\). A minimizing \(t\) cannot be zero, since its allowed neighbor \(2\) has a closer square to \(3d-4\).

At a minimizing level the \(j=4\) multiplier is always \(16\), while the \(j=3\) multiplier is nonzero by \(t\ne0\). The \(j=2\) multiplier cannot vanish: if \(t^2=d-4\), then \((|t|+2)^2\) is strictly closer than \(t^2\) to \(3d-4\), contradicting minimality. The only possible extra kernel is consequently degree one, and this occurs exactly when \(t^2=3d-8\). In that case the vertex \(3d-4=t^2+4\) lies closer to \(t^2\) than to either adjacent parity-compatible square, since their squared-distance deviations are \(4|t|\) rather than \(4\) (and \(|t|\ge7\)). There are exactly two minimizing weights, \((d-t)/2\) and \((d+t)/2\), and both annihilate degree one. The integer equation is equivalent to \(d=(t^2+8)/3\) with \(t\ge7\) and \(3\nmid t\); its solutions automatically have the required parity. All other dimensions give trivial kernel in step 2 and hence a unique radial extremizer.

**5. The full exceptional face.** Degree one consists precisely of the functions \(h(s)=\sum_{i\in s}w_i\) with \(\sum_iw_i=0\). The degree-one transform identity gives the explicit inequalities in the finding. They are both necessary and sufficient for positive definiteness. At the minimizing weights their left sides vanish identically for every \(w\). At all other weights, the radial value \(1+a_dK_4^{(d)}(k)\) is strictly positive. Since there are finitely many weights and subsets, a sufficiently small open neighborhood of \(w=0\) in \(\sum_iw_i=0\) satisfies every remaining inequality. The representation \(w\mapsto h\) is injective, giving a full-dimensional polytope of dimension \(d-1\). Positivity of the Walsh transform together with normalization implies \(|f(s)|\le1\), so the optimizer set is bounded and closed, hence a compact polytope.

## Verification

The supplied standalone `checker.py` uses exact integer and rational arithmetic only. Running `python checker.py` reports `CHECK_PASS`. It checks 5,115 identities between the binomial Krawtchouk formula and the polynomial expression for dimensions \(8\)–\(100\), the minimizing-weight and exceptional-dimension pattern in all 988 dimensions \(13\)–\(1000\), 16,438 nonzero product-contrast Walsh identities for dimensions \(10\)–\(13\), and 72 distinct rational Fourier inequalities for a nonradial extremizer at \(d=19\) with \(w_1=1/601008\), \(w_2=-1/601008\), and all other weights zero. These checks test stated identities and a nonradial witness; the universal conclusion rests on the preceding proof and the cited harmonic-slice theorem, not on extrapolation.

## Relationship to prior work

The Turán problem for positive-definite functions on locally compact abelian groups is studied by Kolountzakis and Révész and, in a general Delsarte framework, by Berdysheva and Révész. Their general packing and spectral estimates do not directly characterize this particular fourth Hamming shell's full optimizer set. Polyanskiy's spherical-average analysis supplies standard Krawtchouk-Fourier context. Filmus's harmonic-slice orthogonal basis is used here as a known structural input. The new assertion is the all-dimension equality-face classification and its specific arithmetic resonance, rather than the classical underlying spectral-basis machinery. An analogous known weight-two Boolean shell result concerns a different allowed Fourier support and does not state the fourth-shell resonance.

## Limitations

The constant \(m_d\) is defined by an explicit finite minimum; a single closed residue-class formula for the mass is not asserted. The classification is for exact support restriction \(\{0\}\cup S_4\), with no requirement that \(f(s)\ge0\). The theorem excludes \(d<13\), where minimizing levels can be too small for the stated slice argument. Prior literature on Johnson association schemes or Krawtchouk rank criteria might contain equivalent formulations; the literature comparison is substantial but cannot certify absolute novelty.

## References

1. E. Berdysheva and S. G. Révész, *Delsarte's Extremal Problem and Packing on Locally Compact Abelian Groups*, arXiv:1904.03614 (first public version 2019-04-07), https://arxiv.org/abs/1904.03614.
2. M. N. Kolountzakis and S. G. Révész, *Turán's extremal problem for positive definite functions on groups* (2004), https://eigen-space.org/ps/turan-groups.pdf.
3. Y. Filmus, *An Orthogonal Basis for Functions over a Slice of the Boolean Hypercube*, Electronic Journal of Combinatorics 23 (2016), P1.23, doi:10.37236/4567, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p23/pdf/.
4. Y. Polyanskiy, *Hypercontractivity of Spherical Averages in Hamming Space*, https://people.lids.mit.edu/yp/homepage/data/hc_hamming.pdf.
