# Positive critical periodic content for complete prefix-coded similarities

## Finding

**Theorem.** Let \(q\ge2\) be an integer and let \(C=\{c_1,\ldots,c_m\}\) be a finite complete prefix code of \(m\ge2\) words over a \(q\)-letter alphabet. Write \(\ell_i=|c_i|\), \(L=\max_i\ell_i\), and fix \(0<r<1\). Let \(\mathcal F=\{f_1,\ldots,f_m\}\) be any self-similar iterated function system in \(\mathbb R^d\) whose similarity ratios are \(r^{\ell_i}\), and assume the strong separation condition. Write \(K\) for its compact attractor, \(T\) for the corresponding inverse expanding map on \(K\), and
\[
\delta=\min_{i\ne j}\operatorname{dist}(f_i(K),f_j(K))>0,
\qquad s=\frac{\log q}{\log(1/r)}.
\]
Then \(s\) is the similarity and Hausdorff dimension of \(K\). For every integer \(n\ge1\) there exists a point \(x_n\in K\) of least period \(p_n\), with orbit gap \(\eta_n\) (minimum Euclidean distance between distinct orbit points), satisfying
\[
\boxed{p_n\ge\frac{q^n}{L},\qquad \eta_n\ge\delta r^{n-1}.}
\]
Consequently the critical periodic content introduced by Kong, Wang and Yu satisfies
\[
\boxed{\mathfrak P^{s}(K,|\cdot|,T)
\ge\frac{1}{L}\left(\frac{\delta}{r}\right)^s>0.}
\]
The associated uniform periodic-orbit measures converge weakly to the normalized \(s\)-dimensional Hausdorff measure on \(K\), by their Theorem 1.3. Their general finiteness theorem also gives \(\mathfrak P^s<\infty\).

**Concrete inhomogeneous example.** For \(q=2\), take the complete prefix code \(C=\{0,10,11\}\), \(r=1/2\), and three planar similarities
\[
f_0(z)=\tfrac12 z,\qquad
f_{10}(z)=\tfrac14 z+(3,0),\qquad
f_{11}(z)=\tfrac14 z+(0,3).
\]
The invariant square \([0,4]^2\) contains the attractor. Its three first-level images lie in the disjoint rectangles \([0,2]^2\), \([3,4]\times[0,1]\), and \([0,1]\times[3,4]\). Their minimum separation is exactly \(\delta=1\). Thus this genuinely inhomogeneous, strongly separated system has \(s=1\) and
\[
\boxed{\mathfrak P^1(K,|\cdot|,T)\ge1.}
\]
This solves the positive-critical-content question for an infinite prefix-coded family beyond the previously treated two-map contraction pair.

## Assumptions and scope

A *complete finite prefix code* means that no codeword is a proper prefix of another and every one-sided infinite word over the \(q\)-symbol source alphabet begins with exactly one codeword. Equivalently its cylinders partition the full one-sided shift, so the Kraft identity holds:
\[
\sum_{i=1}^{m}q^{-\ell_i}=1.
\]
The inverse expanding map is defined piecewise by \(T|_{f_i(K)}=f_i^{-1}\). Strong separation makes this a well-defined continuous map on \(K\). The quantity \(\mathfrak P^s\) is
\[
\mathfrak P^s=\lim_{N\to\infty}\sup\big\{p\,\eta(\mathcal O)^s:\ \mathcal O\text{ a periodic orbit with }p=|\mathcal O|\ge N\big\}.
\]
No restriction on orientations or translations of the similarities is imposed beyond strong separation. The theorem applies to unequal codeword lengths, hence genuinely inhomogeneous contraction systems.

## Proof

**1. Critical dimension from completeness.** By the Kraft identity,
\[
\sum_{i=1}^{m}(r^{\ell_i})^s
=\sum_{i=1}^{m}q^{-\ell_i}=1,
\]
where \(r^s=q^{-1}\). The strongly separated similarity dimension and Hausdorff dimension coincide with this \(s\).

**2. A circular prefix parsing of a de Bruijn word.** For each \(n\ge1\), take a cyclic \(q\)-ary de Bruijn word \(B_n\) of span \(n\) and length \(N=q^n\). It exists by an Euler tour of the directed overlap graph of all words of length \(n\). Exactly one occurrence of every length-\(n\) word begins among its \(N\) cyclic positions. Repeat \(B_n\) periodically in both directions and identify its positions with \(\mathbb Z/N\mathbb Z\).

At each position \(t\), completeness and prefix-freeness identify a unique codeword \(c_{i(t)}\) beginning at \(t\). Define
\[
g(t)=t+\ell_{i(t)}\pmod N.
\]
This is a self-map of a finite set, so it has at least one directed cycle with distinct vertices \(t_0,\ldots,t_{p-1}\), ordered by \(g(t_j)=t_{j+1}\), indices modulo \(p\). The total number of source letters consumed along the cycle is the positive multiple
\[
\sum_{j=0}^{p-1}\ell_{i(t_j)}=kN,\qquad k\in\mathbb N.
\]
Because every codeword has length at most \(L\), \(pL\ge kN\ge N\), hence \(p\ge q^n/L\).

Let \(w_n\) be the \(p\)-letter cyclic word \(i(t_0)\cdots i(t_{p-1})\) over the *IFS symbol* alphabet, and let \(\mathbf w_n=w_n^{\infty}\). Its codeword expansion is exactly the periodic source word \(B_n^\infty\) viewed from the bit/digit position \(t_0\). Every cyclic shift of \(w_n\) corresponds to a distinct starting position \(t_j\) in \(B_n\). If two such codeword-symbol shifts were identical, their infinite source expansions would be identical; but the length-\(n\) factors at distinct source positions are different. Therefore \(w_n\) is primitive and \(\mathbf w_n\) has least shift-period exactly \(p\).

**3. Metric orbit separation.** Take two distinct shifts of \(\mathbf w_n\). If their longest common initial *IFS-symbol* string had total source-code length at least \(n\), then their expanded source strings would share the first \(n\) source letters, contradicting the de Bruijn property. Therefore their common IFS-symbol prefix has total source length \(v\le n-1\).

Let \(\pi\) be the coding map from the full IFS-symbol shift to \(K\). Under strong separation, two different tails beginning with distinct IFS symbols have Euclidean images at distance at least \(\delta\). Composing the \(v\)-source-letter common prefix scales this distance by exactly \(r^v\), including arbitrary orthogonal parts. Thus the distinct orbit points satisfy
\[
|\pi(\sigma^a\mathbf w_n)-\pi(\sigma^b\mathbf w_n)|
\ge\delta r^v\ge\delta r^{n-1}.
\]
As \(\pi\) is injective and conjugates the shift to \(T\), this establishes the two bounds for the true dynamical orbit \(\mathcal O_n\) of \(x_n=\pi(\mathbf w_n)\).

**4. Positive periodic content and distribution.** Using \(r^s=q^{-1}\),
\[
p_n\eta_n^s\ge\frac{q^n}{L}(\delta r^{n-1})^s
=\frac{1}{L}\left(\frac{\delta}{r}\right)^s>0.
\]
Since \(p_n\ge q^n/L\to\infty\), the definition of periodic content yields the claimed lower bound. The periodic-measure convergence follows from Theorem 1.3 of Kong–Wang–Yu, whose hypothesis is precisely a sequence of periods tending to infinity with a positive lower bound on this normalized gap. The cited source also supplies finiteness of the critical content.

For the planar example, the specified square is forward invariant under all three maps, proving \(K\subset[0,4]^2\). Each of the three image rectangles is disjoint from the others by at least \(1\). Equality of the minimum gap follows, for instance, from the points \((2,0)\in f_0(K)\) and \((3,0)\in f_{10}(K)\). The general bound becomes \((1/2)(1/(1/2))^1=1\).

## Verification

The bundled standard-library checker `artifacts/verify_prefix_orbits.py` generates independent \(q\)-ary de Bruijn words, checks all cyclic length-\(n\) factors, parses codeword-boundary cycles, verifies primitive codeword periods, and checks the initial-common-prefix separation for every pair of parsed shifts. Cases include four binary complete prefix codes through \(n=9\) or \(10\), and two ternary codes through \(n=7\). Its execution finished with `VERIFY_OK pair_checks 5091068`.

These are finite tests of the combinatorial mechanism, not an exhaustive proof over all code lengths or periods. The infinite assertion is proved by the four steps above; the planar separation uses exact rectangle inequalities.

## Relationship to prior work

Kong, Wang and Yu, arXiv:2609.16296v1, define periodic content, prove the equality of periodic and similarity dimensions under strong separation, and prove critical-content positivity for homogeneous IFSs. Their Question 5.1 asks for positivity in the inhomogeneous setting; their Section 3 inhomogeneous argument only reaches subcritical exponents. Their Lemma 3.2 and Theorem 1.3 provide, respectively, the coding conjugacy and periodic-measure implication invoked here.

The published work *Positive critical periodic content for the \(\{\rho,\rho^2\}\) contraction pair* proves positivity for two strongly separated similarities with unequal ratios using a Golden-Mean de Bruijn cycle. That two-map result does **not** imply the present three-map case with ratios \(\{\rho,\rho^2,\rho^2\}\), because its critical exponent is strictly smaller; a lower bound at the two-map exponent vanishes after raising gaps to the larger three-map exponent. The present construction instead starts with an unrestricted \(q\)-ary de Bruijn cycle and uses a *cycle of the deterministic complete-prefix decoder* to obtain a well-separated orbit in the variable-length IFS time coordinate. It covers every finite complete prefix-code length profile, not just one contraction pair.

Classical de Bruijn theory supplies the underlying universal cycles. Moreno's work on universal cycles in restricted languages is relevant combinatorial background, but no result from that paper is used in the proof.

## Limitations

The contractive ratios must be powers of a common \(r\) with exponents arising as lengths of a finite *complete prefix code*; arbitrary commensurable ratios and incommensurable ratios are not resolved. Strong separation is essential to the stated uniform Euclidean gap. The lower bound on critical content is not claimed to be optimal. The result classifies a nontrivial family of instances of the inhomogeneous question, not all inhomogeneous IFSs. Prior-literature comparisons cannot rule out unindexed equivalent theorems, particularly in variable-length symbolic suspension literature. Independent external review has not been performed.

## References

1. D. Kong, Z. Wang, D. Yu, *Asymptotic separation of periodic orbits and fractal dimension*, arXiv:2609.16296v1, first posted 2026-09-14. https://arxiv.org/abs/2609.16296
2. *Positive critical periodic content for the \(\{\rho,\rho^2\}\) contraction pair*, published research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-positive-critical-periodic-content-for-the-rho-rho-2-contraction--f867b43e8ea4
3. E. Moreno, *De Bruijn sequences and De Bruijn graphs for a general language*, Information Processing Letters 96 (2005), 214–219. DOI: 10.1016/j.ipl.2005.05.028.
