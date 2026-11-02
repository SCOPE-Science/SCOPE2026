# Exact essential norms and finite-rank rigidity for composition sums on discrete Hardy trees

## Finding

Let \(T\) be a \((q+1)\)-homogeneous rooted tree, \(q\ge2\), with sphere \(D_n\) of cardinality \(c_0=1\) and \(c_n=(q+1)q^{n-1}\) for \(n\ge1\). On the complex discrete Hardy space \(\mathbb T_p\), \(1\le p\le\infty\), suppose the pointwise-defined finite composition sum
\[
(Qf)(v)=\sum_{i=1}^r a_i f(\varphi_i(v))
\]
acts boundedly. The individual composition operators need not separately be assumed bounded. Put
\[
 A(v,w)=\sum_{\{i:\varphi_i(v)=w\}}a_i,
 \qquad B_{n,l}=(A(v,w))_{v\in D_n,w\in D_l},
\]
and let \(P_R\) retain precisely the input levels \(D_0,\dots,D_R\). Let \(p'\) be conjugate to \(p\) for finite \(p\), including \(p'=\infty\) at \(p=1\).

**Exact essential-norm theorem.** For every \(1\le p<\infty\),
\[
\boxed{\|Q\|_{\mathrm{ess},p}=
\lim_{R\to\infty}\sup_{n\ge0}\;c_n^{-1/p}
\sup_{\|y\|_{\ell_{p'}(D_n)}\le1}
\sum_{l>R}c_l^{1/p}\|B_{n,l}^{*}y\|_{\ell_{p'}(D_l)}.}
\]
The sum over \(l\) is finite for each fixed \(n\). For \(p=\infty\),
\[
\boxed{\|Q\|_{\mathrm{ess},\infty}
=\lim_{R\to\infty}\sup_{v\in T}
\sum_{\substack{w\in T\\ |w|>R}}|A(v,w)|.}
\]
Both formulas are exact rather than upper and lower estimates. In each case the expression before taking the limit equals \(\|Q(I-P_R)\|\).

**Endpoint rigidity.** For fixed coefficients \(a_1,\ldots,a_r\), the nonincreasing \(p=\infty\) tail-norm sequence takes values in a finite set and therefore is eventually constant. Consequently, within this class,
\[
\boxed{Q:\mathbb T_\infty\to\mathbb T_\infty\text{ is compact}\quad
\Longleftrightarrow\quad Q\text{ has finite rank}\quad
\Longleftrightarrow\quad Q=QP_R\text{ for some }R.}
\]
Thus no infinite-rank compact finite composition sum exists on \(\mathbb T_\infty\).

**Sharp endpoint example.** Use the two maps of Liu and Ma, Example 4.1: at one vertex \(v_n\in D_n\) for every sufficiently large \(n\), the maps send \(v_n\) to distinct \(x_n,y_n\in D_{\lfloor n/2\rfloor}\) and agree elsewhere. For \(Q=C_\varphi-C_\psi\), at every sufficiently large integer \(R\),
\[
\boxed{\|Q(I-P_R)\|_{\mathbb T_p}
=2^{1-1/p}q^{-(R+1)/p}\quad(1\le p<\infty),\qquad
\|Q(I-P_R)\|_{\mathbb T_\infty}=2.}
\]
Therefore \(\|Q\|_{\mathrm{ess},p}=0\) at every finite \(p\), but \(\|Q\|_{\mathrm{ess},\infty}=2\). The two orders of taking \(R\to\infty\) and \(p\to\infty\) have different limits, respectively \(0\) and \(2\).

## Assumptions and scope

The tree is countably infinite and locally finite, with \(q\ge2\). For \(1\le p<\infty\), set
\[
\|f\|_{\mathbb T_p}=\sup_{n\ge0}
\left(c_n^{-1}\sum_{v\in D_n}|f(v)|^p\right)^{1/p};
\quad \|f\|_{\mathbb T_\infty}=\sup_{v\in T}|f(v)|.
\]
Each \(\varphi_i:T\to T\) is an arbitrary map; \(r\) is finite, \(a_i\in\mathbb C\), and the displayed linear combination itself is assumed bounded on the indicated space. Vanishing coefficients, repeated maps, and cancellations are allowed. The essential norm is the distance to all compact linear operators on that Banach space. The adjoint \(B_{n,l}^{*}\) is the conjugate transpose of the finite coefficient matrix; no Hilbert-space adjoint of the whole operator is required.

## Proof

**1. Exact tail principle.** As a Banach space, \(\mathbb T_p\) is the \(\ell_\infty\)-direct sum of finite-dimensional level spaces \(E_n\), each with its indicated normalized \(\ell_p\)-norm. Its subspace of elements whose level norms tend to zero is the corresponding \(c_0\)-direct sum. The coordinate truncation \(P_R\) is a norm-one finite-rank projection. Hence \(QP_R\) has finite rank and
\[
\|Q\|_{\mathrm{ess},p}\le\inf_R\|Q(I-P_R)\|.
\]
For each \(R\), choose a tail-supported unit vector whose image under \(Q\) almost realizes \(\|Q(I-P_R)\|\). Choose an output level at which the image nearly realizes the output norm. The finite set of vertices in that output level samples at most \(r c_n\) input vertices. Erasing all other input values leaves the chosen output level unchanged and does not increase the input norm. Thus one can choose finitely supported \(f_R\) with support at levels strictly above \(R\), \(\|f_R\|\le1\), and
\[
\|Qf_R\|\ge\|Q(I-P_R)\|-R^{-1}
\]
for \(R\ge1\). Every such sequence is weakly null: an arbitrary functional on the \(\ell_\infty\)-sum restricts to an \(\ell_1\)-summable family of functionals on the \(c_0\)-sum, and its action on \(f_R\) is bounded by the corresponding tail sum. Each compact \(K\) therefore satisfies \(\|Kf_R\|\to0\). Consequently
\[
\|Q-K\|\ge\lim_{R\to\infty}\|Q(I-P_R)\|.
\]
Taking the infimum over compact \(K\) proves exact equality. The tail norms decrease, so their limit exists.

**2. Finite block duality.** Fix an output level \(n\). Each of its finitely many vertices samples at most \(r\) input vertices, so only finitely many levels \(l>R\) contribute. The norm of the map from the \(\ell_\infty\)-sum of these input levels to the \(n\)-th output level is, by finite-dimensional \(\ell_p\)-duality and independently optimizing each input level,
\[
c_n^{-1/p}\sup_{\|y\|_{p'}\le1}
\sum_{l>R}c_l^{1/p}\|B_{n,l}^*y\|_{p'}.
\]
The full output norm is the supremum over \(n\), yielding the finite-\(p\) formula. For \(p=\infty\), each output vertex is a finite scalar row and its operator norm on bounded input functions is the sum of the absolute grouped coefficients, giving the second formula.

**3. Discrete endpoint stabilization.** Fix the finite coefficient list. At any vertex and cutoff, collect indices \(i\) with \(|\varphi_i(v)|>R\), and partition them according to equal image vertices. Each row sum \(\sum_{|w|>R}|A(v,w)|\) equals
\[
\sum_{G\in\pi}\left|\sum_{i\in G}a_i\right|
\]
for some partition \(\pi\) of a subset of \(\{1,\ldots,r\}\). There are only finitely many such values. The supremum over vertices also belongs to that finite set, and it decreases as \(R\) increases. Thus it stabilizes exactly after some finite cutoff. If \(Q\) is compact, its essential norm is zero; hence the stabilized tail norm is zero, so \(Q=QP_R\), which is finite rank. The converse is automatic.

**4. The endpoint separation.** In the cited construction, \((Qf)(v_n)=f(x_n)-f(y_n)\), and \(Qf\) vanishes at all other output vertices. For finite \(p\), two-point \(\ell_p\)-duality gives the exact norm of this output coordinate as
\[
2^{1-1/p}\left(\frac{c_{\lfloor n/2\rfloor}}{c_n}\right)^{1/p}.
\]
Its tail restriction is nonzero exactly when \(\lfloor n/2\rfloor>R\). Because \(c_{\lfloor n/2\rfloor}/c_n=q^{-\lceil n/2\rceil}\) for the relevant levels, the largest value is at \(n=2(R+1)\), for all sufficiently large \(R\). This proves the stated exact finite-\(p\) tail law. On bounded functions two independent values \(1\) and \(-1\) produce \(2\), and arbitrarily high levels survive every cutoff. Thus the \(p=\infty\) essential norm is exactly \(2\), completing the endpoint comparison.

## Verification

The complete finite-dimensional dual formula was reconstructed directly from the level norms, including the \(p=1\) and \(p=\infty\) endpoints. The weakly null argument applies to the full nonseparable \(\ell_\infty\)-sum because it uses restrictions of arbitrary dual functionals to the \(c_0\)-subspace; no unproved weak convergence of arbitrary bounded pointwise-null sequences is assumed. The separate script `verify.py` passed 3494 finite assertions, testing level counts, two-point extremal norms, exact finite tails, explicit dual block examples, and finite coefficient-partition palettes. These finite checks are supplementary; the four analytical steps above establish the infinite claims.

## Relationship to prior work

Liu and Ma, arXiv:2610.33717v1 (first public October 24, 2026), Theorem 3.3, characterize compactness of bounded sums of composition operators for finite \(p\), using a vanishing scalar tail criterion. Their Theorem 3.8 proves finite-exponent compactness invariance. Their Example 4.1 supplies the two-map cancellation construction and its finite-exponent compactness. These are prior results, not claimed here as new. The present finding instead gives the **numerically exact essential norm** for arbitrary bounded finite composition sums at every Banach exponent, the finite-set stabilization/finite-rank rigidity at \(p=\infty\), and the exact sharp tail profile of their example showing the endpoint discontinuity.

Muthukumar and Ponnusamy's 2016/2017 preprint already proves that a **single** composition operator is compact on \(\mathbb T_\infty\) precisely when its inducing map has finite range (Corollary 5), and such operators are finite rank (Theorem 6). This one-map endpoint result is explicitly prior mathematics; the present finite-rank rigidity is an extension to arbitrary **finite linear combinations**, with complete coefficient cancellation and exact essential norm. Their 2020 article further treats single-operator norms and compactness. General results on essential norms of composition operators in analytic Hardy or Bergman spaces and on multipliers of tree Lipschitz spaces concern different function-space norms. The proof here explicitly derives the needed level-block tail equality rather than importing those results.

## Limitations

The exact formula is an infinite cutoff limit and an output-level supremum of finite dual optimizations; it need not reduce to a single closed-form scalar for arbitrary maps. The stabilization cutoff at \(p=\infty\) exists but need not be effectively bounded from the coefficients alone without information about the maps. The example uses a pre-existing pair of inducing maps and does not claim their construction as new. The theorem is for a finite number of maps and \(1\le p\le\infty\), not for infinite sums or quasi-Banach exponents below one. A more general unpublished or differently indexed finite-row matrix theorem could imply the tail formula; publication priority and independent correctness review remain open.

## References

1. L. Liu and W. Ma, *Compactness of composition operators on Hardy spaces of homogeneous rooted trees*, arXiv:2610.33717v1 (2026), Sections 2–4, Theorems 3.3 and 3.8 and Example 4.1. https://arxiv.org/html/2610.33717v1
2. P. Muthukumar and S. Ponnusamy, *Composition operators on the discrete analogue of generalized Hardy space on homogenous trees*, arXiv:1609.09729v1 (2016); *Bulletin of the Malaysian Mathematical Sciences Society* 40 (2017), 1801–1815. https://arxiv.org/abs/1609.09729
3. P. Muthukumar and S. Ponnusamy, *Composition operators on Hardy spaces of the homogenous rooted trees*, arXiv:2004.03171v1 (2020); *Monatshefte für Mathematik* 192 (2020), 721–743. https://arxiv.org/abs/2004.03171
