# Sharp two-point sensitivity of optimal Lipschitz extension on weighted stars

## Finding

Let \(T\) be a compact metric star with \(m\ge 2\) leaves \(p_1,\ldots,p_m\) and arm lengths \(\ell_i>0\), and put \(B=\{p_1,\ldots,p_m\}\). For every real leaf datum \(v\), let \(E(v)\) denote its unique absolutely minimizing Lipschitz extension to the entire metric tree. Equip leaf data and extended functions with their respective Lipschitz seminorms. Then the sharp *two-data* stability modulus is

\[
K_T:=\sup_{\|v-w\|_{\mathrm{Lip}(B)}>0}
\frac{\|E(v)-E(w)\|_{\mathrm{Lip}(T)}}{\|v-w\|_{\mathrm{Lip}(B)}}
=\begin{cases}
1,&m=2,\\[3pt]
1+\displaystyle\max_{\substack{i,a,b\ \mathrm{pairwise\ distinct}}}
\frac{2\ell_a\ell_b}{(\ell_a+\ell_b)\ell_i},&m\ge3.
\end{cases}
\]

If \(m\ge3\) and the arm lengths in nondecreasing order are \(\ell_{[1]}\le\cdots\le\ell_{[m]}\), this is equivalently
\[
K_T=1+\frac{2\ell_{[m-1]}\ell_{[m]}}
{(\ell_{[m-1]}+\ell_{[m]})\ell_{[1]}}.
\]
Every displayed sharp value is attained by two distinct boundary data; no limiting sequence is required. In particular, for equal arm lengths, \(K_T=2\) for every \(m\ge3\), although each individual extension satisfies \(\|E(v)\|_{\mathrm{Lip}(T)}=\|v\|_{\mathrm{Lip}(B)}\).

## Assumptions and scope

The star is the geometric realization of \(m\) closed line segments of lengths \(\ell_i\), joined at a single center \(o\), with intrinsic path metric. The distance between distinct leaves is \(d(p_i,p_j)=\ell_i+\ell_j\). For \(u\in\mathbb R^m\), define
\[
\|u\|_{\mathrm{Lip}(B)}=\max_{i<j}\frac{|u_i-u_j|}{\ell_i+\ell_j}.
\]
For continuous \(h:T\to\mathbb R\), \(\|h\|_{\mathrm{Lip}(T)}=\sup_{x\ne y}|h(x)-h(y)|/d(x,y)\). Both are seminorms modulo constants. The map \(E\) is the canonical real-valued absolutely minimizing Lipschitz extension, not an arbitrary extension and not a linear averaging operator. Every datum is finite and every \(\ell_i\) is strictly positive.

## Proof

**1. The unique center value.** Set \(L(v)=\|v\|_{\mathrm{Lip}(B)}\). Every extension with Lipschitz seminorm at most \(L(v)\) must give the center a value in the interval
\[
I(v)=\bigcap_i[v_i-L(v)\ell_i,\ v_i+L(v)\ell_i].
\]
Choose a pair \(a,b\) attaining \(L(v)=|v_a-v_b|/(\ell_a+\ell_b)\). If \(v_a\le v_b\), their two center-constraints meet at precisely
\[
c(v)=\frac{\ell_bv_a+\ell_av_b}{\ell_a+\ell_b};
\]
the same formula holds with reversed order. Hence \(I(v)=\{c(v)\}\). (If \(L(v)=0\), the datum is constant and the conclusion is immediate.) Affine interpolation from \(c(v)\) to each leaf realizes the original boundary Lipschitz seminorm. It is the unique absolutely minimizing extension: on each open arm, absolute minimality forces the affine interpolant between its endpoints, and the center value has already been forced. This also agrees with the classical uniqueness theorem for bounded data on compact length spaces.

**2. Piecewise-linear selectors.** The center map \(c:\mathbb R^m\to\mathbb R\) is continuous, because the feasible intervals above meet at one point and each endpoint is a continuous function of \(v\). On every region where a fixed pair \(a,b\) attains the unique maximal boundary slope, it has linear form
\[
c(v)=C_{ab}(v):=\frac{\ell_bv_a+\ell_av_b}{\ell_a+\ell_b}.
\]
The regions are defined by finitely many linear slope comparisons (including signs); along any line segment in data space there are finitely many selector changes, or identically tied selectors with the same center value. Thus differences of \(c\) can be bounded by integrating the finite collection of linear selector slopes.

**3. Sharp local operator bound.** Fix one active pair \(a,b\) and a perturbation \(h\). Write \(C=C_{ab}(h)\). If \(i=a\), then
\[
\frac{|h_a-C|}{\ell_a}=\frac{|h_a-h_b|}{\ell_a+\ell_b}\le\|h\|_{\mathrm{Lip}(B)},
\]
and analogously for \(i=b\). If \(i\notin\{a,b\}\), express \(h_i-C\) as the convex combination of \(h_i-h_a\) and \(h_i-h_b\), obtaining
\[
\frac{|h_i-C|}{\ell_i}
\le\left(1+\frac{2\ell_a\ell_b}{(\ell_a+\ell_b)\ell_i}\right)\|h\|_{\mathrm{Lip}(B)}.
\]
For an affine-on-arms extension, the Lipschitz seminorm is exactly the largest absolute arm slope. Applying this bound on each selector piece along the line segment from \(w\) to \(v\), then summing, proves the stated global upper bound. The case \(m=2\) has only one pair and has modulus one.

**4. Exact attaining pairs.** Choose any pairwise distinct indices \(a,b,i\). Define a base datum \(u\) by \(u_a=-\ell_a\), \(u_b=\ell_b\), and \(u_j=0\) for all other leaves. Its boundary Lipschitz seminorm is one and \(a,b\) is the unique maximizing pair: every other ratio is strictly below one because arm lengths are positive. The center equals zero. Define a perturbation \(h\) by \(h_a=-\ell_a\), \(h_b=-\ell_b\), \(h_i=\ell_i\), and \(h_j=0\) otherwise. Then \(\|h\|_{\mathrm{Lip}(B)}=1\). For all sufficiently small positive \(\varepsilon\), the pair \(a,b\) remains the unique maximizing pair for \(u+\varepsilon h\), so
\[
c(u+\varepsilon h)-c(u)
=-\varepsilon\frac{2\ell_a\ell_b}{\ell_a+\ell_b}.
\]
The slope of \(E(u+\varepsilon h)-E(u)\) along the \(i\)-th arm is exactly
\[
\varepsilon\left(1+\frac{2\ell_a\ell_b}{(\ell_a+\ell_b)\ell_i}\right).
\]
Its boundary difference has Lipschitz seminorm \(\varepsilon\), proving equality for every triple. Select a maximizing triple. Since the two-arm case is an isometry, the entire formula is established.

**5. Length ordering.** The harmonic mean \(2rs/(r+s)\) is increasing in each positive argument. In every triple, its numerator is bounded by the harmonic mean of the two largest lengths, while the denominator is at least the shortest length. With at least three arms these three positions can be chosen distinctly, so the ordered-length formula is exact.

## Verification

The standalone `check_amle_star.py` separately benchmarks every selector's coordinate slope over the boundary Lipschitz unit polytope using linear programming. It also tests explicit achieving pairs and random two-data inequalities with rational input. An executed run reported `PASS` with 3,220 independent linear-program selector comparisons, 50 attaining-pair identities, 3,000 random pair inequalities, and 13 equilateral cases (6,283 checks total). This computation corroborates finite instances but is not used to infer the all-dimensional formula; the proof above supplies that implication.

To reproduce, install Python with SciPy and run `python check_amle_star.py`. The script is standalone except for SciPy and the Python standard library.

## Relationship to prior work

Classical McShane–Whitney constructions give scalar minimal Lipschitz extensions. Juutinen (2002) studies existence on metric spaces; Peres–Schramm–Sheffield–Wilson (first public preprint 2006) establish uniqueness and game interpretations of absolutely minimizing extensions on length spaces. Matoušek (1990) and Ambrosio–Puglisi study (principally linear) extension-operator bounds on metric spaces. These results give context for the object \(E\); none of the inspected statements supplies the exact two-data Lipschitz-seminorm amplification on a weighted star. The bound in this note concerns the **difference of two optimally extended data**, not the Lipschitz seminorm of an individual extension, the sup-norm dependence of solutions, or the best norm of an arbitrary linear extension operator.

## Limitations

The assertion concerns finite weighted metric stars with scalar real boundary data and the canonical absolutely minimizing extension. It does not assert the same formula on general metric trees with multiple branch points, for vector-valued targets, or under data norms different from the Lipschitz seminorm. A matching result may exist in unindexed classical extension-operator literature; bibliographic uniqueness is not certified. The numerical tests are finite and are not an exhaustive proof.

## References

1. Y. Peres, O. Schramm, S. Sheffield, D. B. Wilson, *Tug-of-war and the infinity Laplacian*, arXiv:math/0605002, first publicly posted 2006-04-28; J. Amer. Math. Soc. 22 (2009), 167–210. https://arxiv.org/abs/math/0605002.
2. P. Juutinen, *Absolutely minimizing Lipschitz extensions on a metric space*, Ann. Acad. Sci. Fenn. Math. 27 (2002), 57–67. https://www.acadsci.fi/mathematica/Vol27/juutinen.pdf.
3. J. Matoušek, *Extension of Lipschitz mappings on metric trees*, Comment. Math. Univ. Carolin. 31 (1990), 99–104. https://dml.cz/handle/10338.dmlcz/106823.
4. L. Ambrosio, D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, https://cvgmt.sns.it/media/doc/paper/3155/weak@Lee-Naor.pdf.
