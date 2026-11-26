# Endpoint rigidity and an exact tail profile for composition sums on discrete Hardy trees

## Finding

Let \(T\) be a \((q+1)\)-homogeneous rooted tree, \(q\ge2\), with level \(D_n\), \(c_0=1\) and \(c_n=(q+1)q^{n-1}\) for \(n\ge1\). Let \(Qf(v)=\sum_{i=1}^r a_i f(\varphi_i(v))\) be a finite complex composition sum and put \(A(v,w)=\sum_{i:\varphi_i(v)=w}a_i\). Let \(P_R\) retain the input levels \(0,\ldots,R\). On \(\mathbb T_\infty=\ell_\infty(T)\), the norm of \(Q(I-P_R)\) is
\[
 s_R=\sup_{v\in T}\sum_{|w|>R}|A(v,w)|.
\]
This sequence eventually stabilizes at \(\|Q\|_{\mathrm{ess},\infty}\). In particular,
\[
 Q\text{ compact}\quad\Longleftrightarrow\quad Q\text{ finite rank}\quad\Longleftrightarrow\quad Q=QP_R\text{ for some }R.
\]
The statement allows arbitrary maps and exact cancellation among coefficients.

In Liu and Ma's Example 4.1, the maps \(\varphi,\psi\) agree except at one vertex \(v_n\) on each sufficiently large level, where the images \(x_n,y_n\) are distinct and both lie on level \(\lfloor n/2\rfloor\). For \(Q=C_\varphi-C_\psi\), at every sufficiently large integer \(R\),
\[
 \|Q(I-P_R)\|_{\mathbb T_p}=2^{1-1/p}q^{-(R+1)/p}\quad(1\le p<\infty),\qquad
 \|Q(I-P_R)\|_{\mathbb T_\infty}=2.
\]
Thus the essential norm is zero at every finite exponent and two at infinity. For this example, taking the cutoff to infinity before the exponent gives zero, whereas taking the exponent to infinity before the cutoff gives two. The claims of distinct contribution are the endpoint stabilization and finite-rank characterization for finite sums, and the quantitative tail profile of this example. The finite-exponent block formula below is shared with a separate recorded result; no priority for that formula is asserted.

## Assumptions and scope

For \(1\le p<\infty\), the norm of \(f\) in \(\mathbb T_p\) is \(\sup_n c_n^{-1/p}\|f|_{D_n}\|_{\ell_p(D_n)}\). Essential norm means distance to the compact operators on the full space. At a finite exponent the following tail argument only assumes boundedness of the sum. There is no assumption that its displayed summands are individually bounded, that the maps preserve levels, or that they are graph homomorphisms.

## Proof

**Exact finite-row tail principle.** At every indicated exponent the space is an \(\ell_\infty\)-sum of finite-dimensional normalized level spaces. Since \(QP_R\) has finite rank, \(\|Q\|_{\rm ess}\le\inf_R\|Q(I-P_R)\|\). Conversely, to nearly attain the tail norm, select a tail-supported input of norm at most one and an output level giving its image norm to within the desired error. A fixed output level uses only finitely many input vertices. Set all other coordinates to zero without changing the image on that level or increasing the input norm. Taking errors tending to zero gives finitely supported near-norming inputs whose minimum support levels tend to infinity. These belong to the \(c_0\)-sum of levels and are weakly null in the full space: each functional on the full space restricts to a functional represented by an \(\ell_1\)-summable family on the \(c_0\)-sum. A compact operator sends this sequence to a norm-null sequence, giving the reverse inequality. Therefore \(\|Q\|_{\rm ess}=\lim_R\|Q(I-P_R)\|\).

**Endpoint norm and stabilization.** The \(\ell_\infty\)-operator norm of a finite row is the sum of its absolute coefficients, obtained by aligning the finitely many input phases. This gives \(\|Q(I-P_R)\|=s_R\). In any row, group the retained indices \(i\) according to equal values of \(\varphi_i(v)\). The row norm is \(\sum_{G\in\pi}|\sum_{i\in G}a_i|\) for a partition \(\pi\) of some subset of the fixed \(r\) indices. There are only finitely many possible values. Their supremum over all rows is one of those values, and it is nonincreasing in \(R\). It is therefore eventually constant, and its limit is the essential norm. For a compact sum the limit is zero, so a sufficiently late tail is exactly zero, yielding \(Q=QP_R\). This is finite rank, and a finite-rank bounded operator is compact.

**Exact tails of the example.** There is one nonzero output coordinate per relevant level, namely \(f(x_n)-f(y_n)\) at \(v_n\). If \(\lfloor n/2\rfloor\le R\), its tail vanishes. Otherwise the exact contribution at finite \(p\), including \(p=1\), is \(2^{1-1/p}(c_{\lfloor n/2\rfloor}/c_n)^{1/p}\) by two-coordinate duality. In the relevant range the cardinality ratio equals \(q^{-\lceil n/2\rceil}\); its largest value among the retained levels is attained at \(n=2(R+1)\) for large \(R\). This gives the stated finite-exponent profile. With the supremum norm, any surviving row has norm two, and arbitrarily high rows survive. The essential norm and both iterated limits now follow.

**Finite-exponent context.** Put \(B_{n,l}=(A(v,w))_{v\in D_n,w\in D_l}\) and let \(p'\) be conjugate to \(p\) (\(p'=\infty\) for \(p=1\)). At a fixed output level, dualizing its \(\ell_p\) norm and maximizing independently over each input-level ball gives
\[
 \|Q(I-P_R)\|_{\mathbb T_p}=
 \sup_n c_n^{-1/p}\sup_{\|y\|_{\ell_{p'}(D_n)}\le1}
 \sum_{l>R}c_l^{1/p}\|B_{n,l}^*y\|_{\ell_{p'}(D_l)}.
\]
There are only finitely many summands at fixed \(n\). Combining with the exact tail principle gives the finite-exponent block formula, as also expressed in [3] for individually bounded composition operators.

The difference in how boundedness is stated does not by itself distinguish the finite-exponent operator class. To see this, fix a nonempty subset \(G\) with \(b_G=\sum_{i\in G}a_i\ne0\). In a row \(v\), if there is an image \(w\) whose full index group is exactly \(G\), define \(S_G f(v)=f(w)\); otherwise put \(S_G f(v)=0\). At each fixed output level, multiply the finitely many sampled input values by independent symmetric signs. At a row belonging to \(G\), condition on the sign at its image \(w\) and use Jensen's inequality for \(|\cdot|^p\) to obtain \(\mathbb E|Q(\epsilon f)(v)|^p\ge|b_G f(w)|^p\), since all other terms have mean zero. Sum over the rows of that level and use \(\|\epsilon f\|=\|f\|\). Consequently \(\|S_G\|\le\|Q\|/|b_G|\). Let \(\theta_G\) agree with this choice of \(w\) where it exists and send the other rows to the root; let \(\eta\) send all rows to the root. Each \(C_{\theta_G}\) is bounded, since it adds only root evaluation on the rows where \(G\) is absent. In the sum over groups, the coefficient total of present groups is \(\sum_i a_i\) in every row (zero-weight groups contribute zero), so the extra root terms have a combined coefficient independent of the row. Hence
\[
 Q=\sum_{G:b_G\ne0} b_G C_{\theta_G}+
 \left(\sum_i a_i-\sum_{G:b_G\ne0} b_G\right)C_\eta .
\]
This expresses the same operator in the class of [3], without requiring the original presentation to have bounded summands.

## Verification

The infinite-dimensional identities follow from the weakly null finite-support test and finite-dimensional norm computations above. The original `verify.py` is a supplementary finite checker for level cardinalities, two-point dual norms, explicit block examples, and finite coefficient-partition sets. Finite checks are not a proof of the essential-norm identity.

## Relationship to prior work and limitations

Liu and Ma [1] already give finite-exponent compactness criteria and the map construction; neither that construction nor its finite-exponent compactness is claimed as new. Muthukumar and Ponnusamy [2] give bounded image depth as the compactness criterion for an individual composition operator on \(\mathbb T_\infty\), which implies finite rank. The endpoint result here concerns finite sums with grouped coefficient cancellation and gives stabilization of the exact norm, not solely the zero/nonzero test. The full finite-exponent block formula also appears in [3]; this overlap does not establish chronology, and the claim of distinct contribution does not rely on chronology. The stabilization cutoff depends on the maps and is not bounded here by the coefficient list alone. Infinite sums and quasi-Banach exponents are outside the result.

## References

1. L. Liu and W. Ma, *Compactness of composition operators on Hardy spaces of homogeneous rooted trees*, arXiv:2610.33717v1, Theorems 3.3 and 3.8, Example 4.1. https://arxiv.org/html/2610.33717v1
2. P. Muthukumar and S. Ponnusamy, *Composition operators on the discrete analogue of generalized Hardy space on homogenous trees*, arXiv:1609.09729v1, Theorem 6 and Corollary 5. https://arxiv.org/abs/1609.09729
3. *Exact essential norms of finite composition sums on discrete Hardy trees*, Resultary record d387124a6acb, Finding. https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exact-essential-norms-of-finite-composition-sums-on-discrete-har--d387124a6acb/RESULT.md
