# A single anchor repairs every real Rademacher phase-retrieval ambiguity

## Finding
Fix an integer \(d\ge2\), and let \(\mathcal E_d=\{-1,1\}^d\). For real \(x\in\mathbb R^d\) define the full sign-frame magnitude measurements
\[
\mathcal B(x)=\bigl(|\langle\varepsilon,x\rangle|\bigr)_{\varepsilon\in\mathcal E_d}.
\]
For a fixed auxiliary measurement vector \(a=(a_1,\ldots,a_d)\in\mathbb R^d\), set
\[
\mathcal F_a(x)=\bigl(\mathcal B(x),|\langle a,x\rangle|\bigr).
\]
The following classification is valid **in every finite dimension**:

**Exact equality fibers.** If \(\mathcal B(x)=\mathcal B(y)\) and \(x\ne y,-y\), then there exist distinct coordinates \(i,j\), a sign \(\eta\in\{-1,1\}\), and nonzero real scalars \(\alpha,\beta\) such that
\[
\frac{x+y}{2}=\alpha(e_i+\eta e_j),\qquad
\frac{x-y}{2}=\beta(e_i-\eta e_j).
\tag{1}
\]
Conversely, every pair given by (1) has identical full sign-frame magnitudes.

**One-measurement completion.** The augmented family \(\mathcal F_a\) determines every real signal up to its unavoidable global sign exactly when
\[
|a_i|\ne |a_j|\quad\text{for every }i\ne j.
\tag{2}
\]
Thus one additional non-flat measurement always repairs the full sign-frame failure, and no additional measurement is needed beyond that one. The unaugmented family never has phase retrieval when \(d\ge2\).

**Sharp separation of the pre-existing ambiguity fibers.** Let \(d_\pm(x,y)=\min\{\|x-y\|_2,\|x+y\|_2\}\), and define
\[
\Gamma_d(a)=\inf_{\substack{x\ne\pm y\\\mathcal B(x)=\mathcal B(y)}}
\frac{\bigl||\langle a,x\rangle|-|\langle a,y\rangle|\bigr|}{d_\pm(x,y)}.
\]
Then
\[
\boxed{\Gamma_d(a)=\frac1{\sqrt2}\min_{1\le i<j\le d}\bigl||a_i|-|a_j|\bigr|.}
\tag{3}
\]
The infimum is attained by \(x=e_i\), \(y=e_j\) whenever \(i,j\) minimize the right-hand side. Formula (3) is a **restricted fiberwise** separation constant, not a purported exact global stability constant for arbitrary input pairs.

## Assumptions and scope
All signals, measurement rows, and inner products are real. The full sign family contains all \(2^d\) sign vectors; antipodal pairs give redundant but harmless measurements. A phase-retrievable family means that equality of every magnitude implies equality of signals up to a common real sign. No random-sampling claim is made. The supplementary separation ratio in (3) is evaluated only over pairs already indistinguishable by the unaugmented sign family; these pairs are parametrized in (1). No normalization of \(a\) is imposed, so both sides of (3) scale linearly with its magnitude.

The natural frame-theoretic viewpoint places the result in the functional-analytic study of finite real Hilbert frames. Its subject is the exact geometry of the nonlinear magnitude analysis map, rather than an algorithm for recovering a signal from a small random subset of signs.

## Proof
**Step 1: translate equality of magnitudes into Walsh coefficients.** Given a nontrivial pair \(x\ne\pm y\), define
\[
u=\frac{x+y}{2},\qquad v=\frac{x-y}{2}.
\]
Both vectors are nonzero. For each \(\varepsilon\in\mathcal E_d\), equality of the two absolute sign-frame measurements is equivalent, after squaring and subtracting, to
\[
0=|\langle\varepsilon,x\rangle|^2-|\langle\varepsilon,y\rangle|^2
=4\langle\varepsilon,u\rangle\langle\varepsilon,v\rangle.
\]
Expanding gives the degree-two Walsh polynomial
\[
\langle\varepsilon,u\rangle\langle\varepsilon,v\rangle
=\sum_i u_i v_i+\sum_{i<j}(u_i v_j+u_j v_i)\varepsilon_i\varepsilon_j.
\tag{4}
\]
The constant character and the characters \(\varepsilon_i\varepsilon_j\) are distinct and orthogonal on the uniform sign cube. Therefore vanishing for **every** sign vector forces
\[
\sum_i u_i v_i=0,\qquad u_i v_j+u_j v_i=0\quad(i<j).
\tag{5}
\]
Conversely, these relations force (4) to vanish and hence imply equality of all sign-frame magnitudes.

**Step 2: classify the solutions of (5).** If \(u_i\ne0\) but \(v_i=0\), choose a coordinate \(j\) with \(v_j\ne0\). Necessarily \(j\ne i\), and (5) would give \(u_iv_j=0\), a contradiction. Interchanging \(u,v\) shows that their nonzero supports coincide, say in a set \(S\). On this support write \(r_i=v_i/u_i\ne0\). The off-diagonal equations are exactly \(r_i+r_j=0\) for distinct \(i,j\in S\). Three indices in \(S\) would force \(r_i=r_j=r_k=0\), impossible. The set \(S\) cannot have just one index because \(\sum_i u_i v_i=0\) but \(u_i v_i\ne0\). Hence it contains **exactly two** indices \(i,j\). Their ratios are opposite, and the remaining inner-product equation reads
\[
0=u_iv_i+u_jv_j=r_i(u_i^2-u_j^2),
\]
so \(|u_i|=|u_j|\). Writing \(u_i=\alpha\), \(u_j=\eta\alpha\) and \(v_i=\beta\) yields \(v_j=-\eta\beta\). Thus (1) holds with \(\alpha\beta\ne0\). Substitution in (5) verifies the converse.

**Step 3: exact criterion for the anchor.** For any real numbers \(p,q\), the elementary identity
\[
\bigl||p+q|-|p-q|\bigr|=2\min\{|p|,|q|\}
\tag{6}
\]
holds. For a pair (1), put \(p=\langle a,u\rangle=\alpha(a_i+\eta a_j)\) and \(q=\langle a,v\rangle=\beta(a_i-\eta a_j)\). The anchor magnitudes agree precisely when \(p=0\) or \(q=0\). Since \(\alpha,\beta\ne0\), this occurs precisely when \(a_i=-\eta a_j\) or \(a_i=\eta a_j\). Hence a nontrivial pair survives the anchor exactly if \(|a_i|=|a_j|\) for some \(i\ne j\). Conversely, if such indices exist, the signals \(e_i\) and \(e_j\) have the same magnitude under every sign row and also under \(a\). This proves (2) and one-measurement minimality.

**Step 4: sharp auxiliary separation.** For a pair (1), the denominator is
\[
d_\pm(x,y)=2\min\{\|u\|_2,\|v\|_2\}=2\sqrt2\min\{|\alpha|,|\beta|\}.
\]
By (6), the auxiliary magnitude difference is
\[
2\min\{|\alpha|\,|a_i+\eta a_j|,\,|\beta|\,|a_i-\eta a_j|\}.
\]
Their ratio is therefore at least
\[
\frac{\min\{|a_i+\eta a_j|,|a_i-\eta a_j|\}}{\sqrt2}
=\frac{\bigl||a_i|-|a_j|\bigr|}{\sqrt2}.
\tag{7}
\]
Minimizing (7) over indices proves the lower bound in (3). For an index pair attaining the minimum, take \(x=e_i\), \(y=e_j\). Then \(\mathcal B(x)=\mathcal B(y)\), the auxiliary magnitude difference is \(\bigl||a_i|-|a_j|\bigr|\), and \(d_\pm(x,y)=\sqrt2\), proving equality and attainment.

**Step 5: qualitative global stability, without conflating constants.** Whenever condition (2) holds, the finite-dimensional magnitude analysis map is globally lower-Lipschitz on signals modulo sign for its ordinary Euclidean measurement norm. Indeed, for an arbitrary finite measurement family \((\phi_k)_k\), set \(u=(x+y)/2\), \(v=(x-y)/2\). The squared ratio of the Euclidean magnitude difference to \(d_\pm(x,y)\) is
\[
\frac{\sum_k\min\{|\langle\phi_k,u\rangle|^2,|\langle\phi_k,v\rangle|^2\}}{\min\{\|u\|_2^2,\|v\|_2^2\}}.
\]
Scaling the longer one of \(u,v\) down shows this is bounded below by the same continuous expression evaluated on unit vectors \(u,v\). By phase retrieval, that expression is never zero on the compact product of unit spheres: otherwise every measurement row would annihilate at least one of \(u,v\), contradicting injectivity of the two signals \(u+v\) and \(u-v\). Compactness gives a positive lower bound. This proves stability in principle; it does not evaluate the exact global lower Lipschitz constant.

## Verification
The analytic proof above uses finite Walsh orthogonality and elementary real algebra and holds for every integer \(d\ge2\). It does not rely on finite experiments. An accompanying reproducible Python script, `verify_rademacher_anchor.py`, performs rational-arithmetic rank tests of every complementary partition of the projectively distinct sign rows, with and without anchors, in dimensions \(2,3,4\). It also checks equation (3) against a finite grid of ambiguity parameters and an explicit equality witness. Run with `python3 verify_rademacher_anchor.py`. Successful output terminates in `PASS: all finite checks`. These diagnostics are **not** taken as proof of a general dimensional claim, and the grid is not a global optimization.

## Relationship to prior work
Abdalla, de Dios Pont, Ramos, and Taylor investigate stable phase retrieval on spans of independent random variables. Their July 2026 manuscript explicitly identifies the Rademacher obstruction and develops positive results under hypotheses absent from the pure sign case; it does not classify what one additional deterministic measurement repairs. Krahmer and Stöger likewise observe that Rademacher measurements fail uniform full-signal injectivity and treat algorithmic recovery of restricted signal families under subgaussian measurements. Their published results do not imply the all-signal one-anchor completion criterion or the sharp restricted separation law.

The classical real complement-property characterization of phase retrieval (Balan, Casazza, Edidin) is compatible with this theorem but does not itself specify which partitions of the full Boolean sign frame fail to span or determine the quantitative margin in (3). A stronger direct precedent is Cahill, Casazza, Jasper, and Woodland: their Theorems 4.1–4.2 give the minimal number of generic extra vectors required to repair an arbitrary real frame. In particular, the **abstract existence of an added vector is not claimed as new**. Their results do not give the explicit pairwise-magnitude criterion for this Boolean frame, the complete collision fibers, or the attained numerical auxiliary separation margin. A separate published classification of projective flat sign-line full-spark subfamilies in dimension five considers **only flat rows**, whereas completion here uses an auxiliary generally non-flat row and imposes full phase retrieval. Other published work computes the global stability constant for a particular planar three-vector frame; that is a different family and a different global invariant. The present result is a structural specialization requiring a full Walsh-coefficient and equality-fiber analysis.

## Limitations
The theorem is real and finite-dimensional; complex signals have additional conjugation ambiguities when all rows are real. It assumes **all** sign vectors are measured, not a random proper subset. The sharp constant (3) measures the additional observation along the previously colliding fibers only; it does not provide the exact global Lipschitz constant for arbitrary signal pairs, nor a noise-tolerant recovery algorithm. The leading source deals with random variables and wider infinite-dimensional questions not settled here. An obscure earlier equivalent treatment under Boolean quadratic-form or frame-completion terminology remains a priority risk; none was identified in the searched and materially inspected sources.

## References
1. P. Abdalla, J. de Dios Pont, J. P. G. Ramos and M. A. Taylor, *Stable Phase Retrieval for Spans of Independent Random Variables*, arXiv:2607.06693v1 (first public version 2026-07-07); see the Rademacher obstruction and main hypotheses.
2. F. Krahmer and D. Stöger, *Complex Phase Retrieval from Subgaussian Measurements*, Journal of Fourier Analysis and Applications 26 (2020), article 89, DOI:10.1007/s00041-020-09797-9, particularly the Introduction and subgaussian recovery theorems.
3. R. Balan, P. G. Casazza and D. Edidin, *On signal reconstruction without noisy phase*, Applied and Computational Harmonic Analysis 20 (2006), 345–356, preprint arXiv:math/0412411; real complement-property criterion.
4. J. Cahill, P. G. Casazza, J. Jasper and L. M. Woodland, *Phase retrieval*, arXiv:1508.06687 (2015), Theorems 4.1–4.2 on minimal phase-retrieval frame completion.
5. *Full-spark capacity of five-dimensional flat sign lines*, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-full-spark-capacity-of-five-dimensional-flat-sign-lines--dae2935843e5.
6. *The Mercedes frame has exact global phase-retrieval stability constant* \(\sqrt2\), 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-mercedes-frame-has-exact-global-phase-retrieval-stability-co--ea5fecd0ccbb.
