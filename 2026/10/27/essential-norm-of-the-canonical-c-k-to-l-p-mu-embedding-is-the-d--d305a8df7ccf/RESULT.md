# Essential norm of the canonical \(C(K)\)-to-\(L^p(\mu)\) embedding is the diffuse mass

## Finding

For every compact metric space \(K\), finite positive Radon measure \(\mu\) on \(K\), and \(1\le p<\infty\), decompose \(\mu=\mu_{\mathrm{at}}+\mu_{\mathrm{c}}\) into its atomic and nonatomic parts. Let \(J_\mu:C(K)\to L^p(\mu)\) be the canonical inclusion. Then

\[
\|J_\mu\|_{\mathrm{ess}}=\inf_{S\in\mathcal K(C(K),L^p(\mu))}\|J_\mu-S\|=\mu_{\mathrm{c}}(K)^{1/p}.
\]

Thus the atomic part is compactly approximable, while the nonatomic mass is exactly the irreducible distance to compact operators. In particular, \(J_\mu\) is compact if and only if \(\mu\) is purely atomic.

## Assumptions and scope

The space \(K\) is compact metric, \(\mu\) is a finite positive Radon measure, and \(1\le p<\infty\). Write
\[
\mu_{\mathrm{at}}=\sum_{j\ge1}a_j\delta_{x_j},\qquad a_j>0,\quad \sum_j a_j<\infty,
\]
with an empty or finite sum allowed, and let \(\mu_{\mathrm{c}}=\mu-\mu_{\mathrm{at}}\), which is nonatomic. The target splits isometrically as
\[
L^p(\mu)\cong L^p(\mu_{\mathrm{at}})\oplus_p L^p(\mu_{\mathrm{c}}).
\]
The theorem does not cover \(p=\infty\), noncompact domains, or arbitrary nonstandard measure spaces.

## Proof

Let \(J_{\mathrm{at}}:C(K)\to L^p(\mu_{\mathrm{at}})\) be restriction to the atoms. Truncating after the first \(N\) atoms gives a finite-rank operator, and the remaining tail has norm at most
\[
\left(\sum_{j>N}a_j\right)^{1/p}\longrightarrow0.
\]
Hence \(J_{\mathrm{at}}\) is compact. Under the displayed direct-sum identification, \(J_\mu\) differs by a compact operator from \(f\mapsto(0,J_{\mathrm{c}}f)\), where \(J_{\mathrm{c}}:C(K)\to L^p(\mu_{\mathrm{c}})\) is the nonatomic inclusion. Essential norm is unchanged by adding a compact operator, so it suffices to prove
\[
\|J_{\mathrm{c}}\|_{\mathrm{ess}}=m^{1/p},\qquad m=\mu_{\mathrm{c}}(K).
\]
The upper bound follows from \(\|J_{\mathrm{c}}\|=m^{1/p}\) by approximating with the zero operator. If \(m=0\), the lower bound is immediate. Suppose \(m>0\) and normalize \(\nu=\mu_{\mathrm{c}}/m\).

Because \((K,\nu)\) is a standard nonatomic probability space, it supports independent Rademacher functions \((r_n)\) generating its measure algebra. Density of \(C(K)\) in \(L^p(\mu_{\mathrm{c}})\), followed by continuous clipping to the unit disk (or interval in the real case), gives \(f_n\in C(K)\) with \(\|f_n\|_\infty\le1\) and \(\|f_n-r_n\|_{L^p(\mu_{\mathrm{c}})}\to0\).

Fix any \(y\in L^p(\mu_{\mathrm{c}})\) and \(\varepsilon>0\). Choose a function \(g\) measurable with respect to the first \(N\) Rademacher coordinates such that \(\|y-g\|_{L^p(\nu)}<\varepsilon\); such finite-coordinate functions are dense because the Rademachers generate the measure algebra. For \(n>N\), independence and convexity give
\[
\|r_n-g\|_{L^p(\nu)}^p
=\int\frac{|1-g|^p+|-1-g|^p}{2}\,d\nu\ge1,
\]
since \(1=|(1-g)-(-1-g)|/2\le(|1-g|+|-1-g|)/2\). Therefore \(\liminf_n\|r_n-y\|_{L^p(\mu_{\mathrm{c}})}\ge m^{1/p}(1-\varepsilon)\), and letting \(\varepsilon\downarrow0\) yields a lower bound of \(m^{1/p}\).

Now let \(S:C(K)\to L^p(\mu_{\mathrm{c}})\) be compact. Since \((f_n)\) is bounded, some subsequence \((Sf_{n_k})\) converges in norm to a vector \(y\). The preceding bound and \(\|f_n-r_n\|_p\to0\) imply
\[
\|J_{\mathrm{c}}-S\|\ge\liminf_k\|f_{n_k}-Sf_{n_k}\|_{L^p(\mu_{\mathrm{c}})}\ge m^{1/p}.
\]
This holds for every compact \(S\), proving the lower bound. Combining it with the upper bound and the compact atomic component proves the formula.

## Verification

The proof uses no numerical experiment. The atomic-tail estimate is an operator-norm estimate; the nonatomic lower bound is obtained for every compact operator by extracting a norm-convergent subsequence of its image of a bounded Rademacher-approximating sequence. The assumptions \(p<\infty\), compact metrizability, and finite Radon measure are used respectively for the \(L^p\) norm, standardness of the nonatomic probability space, and density of continuous functions in \(L^p\).

## Relationship to prior work

Hencl's 2003 paper and Lang, Musil, Olšák, and Pick's 2020 preprint concern measures of noncompactness for Sobolev embeddings and report maximal-noncompactness phenomena for different domains and targets. They motivate the exact essential-norm question but do not, in their accessible abstracts, state this mixed atomic/nonatomic formula for \(C(K)\to L^p(\mu)\). The comparison is limited to the stated abstracts; it is not a claim that their complete texts have been exhaustively excluded as sources of a general implication.

## Limitations

The formula is proved only for compact metric \(K\), finite positive Radon \(\mu\), and \(1\le p<\infty\). No assertion is made for \(p=\infty\), noncompact \(K\), arbitrary nonstandard measure spaces, or other approximation numbers. A residual priority risk remains that an unindexed classical essential-norm theorem for this exact inclusion already implies the formula.

## References

- Stanislav Hencl, “Measures of non-compactness of classical embeddings of Sobolev spaces,” *Mathematische Nachrichten* 258 (2003), 28–43. DOI: 10.1002/mana.200310085. First published 2003-08-14.
- Jan Lang, Vít Musil, Miroslav Olšák, and Luboš Pick, “Maximal non-compactness of Sobolev embeddings,” arXiv:2003.11854, first public version 2020-03-26.
