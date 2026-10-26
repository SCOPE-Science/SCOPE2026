# Sharp moment threshold for random mixed-norm Dirichlet series below the fourth exponent

## Finding

**Theorem.** Fix \(\alpha>-1\), \(0<p<\infty\), and \(0<q<4\). Let \((X_n)_{n\ge1}\) be independent identically distributed, nonconstant complex-valued random variables. With the definitions below, the coefficient-randomization symbol space satisfies

\[
(\mathscr H^{p,q}_{\alpha})_{*,X}=\mathscr H^{2,q}_{\alpha}
\quad\Longleftrightarrow\quad
\mathbb E|X_1|^{\max\{2,q\}}<\infty
\ \text{and}\ \bigl(p\le2\ \text{or}\ \mathbb E X_1=0\bigr).
\]

In fact the following *unconditional reverse inclusion* holds for every \(p,q>0\), not only \(q<4\):

\[
(\mathscr H^{p,q}_{\alpha})_{*,X}\subseteq\mathscr H^{2,q}_{\alpha}
\]

for each nonconstant iid coefficient law \(X\), with **no** integrability or centering hypothesis. Consequently the fourth-moment assumption in the reverse-inclusion statement of [1, Theorem 3.7] can be removed. The complete characterization for \(q<4\) strengthens the partial statements of [1, Theorems 1.4--1.5].

## Assumptions and scope

Write \(f(s)=\sum_{n\ge1}a_n n^{-s}\) for a Dirichlet series converging on some right half-plane and let \(f_\sigma(s)=f(s+\sigma)\). If \(\mathscr H^p\) denotes the \(p\)-Hardy space obtained from the Bohr lift to the infinite torus, set

\[
\|f\|_{\mathscr H^{p,q}_\alpha}^{q}
=\int_0^\infty\|f_\sigma\|_{\mathscr H^p}^{q}\,d\mu_\alpha(\sigma),
\qquad
 d\mu_\alpha(\sigma)=\frac{2^{\alpha+1}}{\Gamma(\alpha+1)}\sigma^\alpha e^{-2\sigma}\,d\sigma.
\]

The mixed space is the completion of Dirichlet polynomials in this quasi-norm. Define

\[
(\mathscr H^{p,q}_\alpha)_{*,X}
=\left\{f:\ \mathbb P\left(\sum_{n\ge1}a_nX_n n^{-s}\in\mathscr H^{p,q}_\alpha\right)=1\right\}.
\]

The randomization is interpreted by its coefficients; coefficient membership in the mixed space entails the usual holomorphic Dirichlet-series realization. The coefficient law is not assumed symmetric, real, bounded, or to have any finite moment before the hypotheses in the theorem are invoked. No independence conclusion is asserted for arbitrary coefficient laws.

Write \(r=q/2\). Parseval yields the concrete quadratic moment

\[
\|f\|_{\mathscr H^{2,q}_\alpha}^{q}
=\int_0^\infty\left(\sum_{n\ge1}|a_n|^2n^{-2\sigma}\right)^r d\mu_\alpha(\sigma).
\]

The established logarithmic-dyadic criterion [1, Theorem 3.1], recalled below, is used only where cited; all new probabilistic estimates are proved here. A source-independent formulation uses \(\mathscr H^p\) on the infinite torus, not the one-variable Hardy space.

## Proof

**Step 1. Universal reverse inclusion in the Hilbert mixed norm.** Let \(Y_n\) be nonconstant iid complex random variables with arbitrary law and fix a Dirichlet series \(f\notin\mathscr H^{2,q}_\alpha\). Choose \(\delta>0\) such that \(\pi=\mathbb P(|Y_1|\ge\delta)>0\), and put \(\eta_n=\mathbf1_{\{|Y_n|\ge\delta\}}\). The indicators are independent Bernoulli variables with parameter \(\pi\). For \(N\ge1\), define the deterministic and thinned quadratic sums

\[
A_N(\sigma)=\sum_{n\le N}|a_n|^2n^{-2\sigma},\qquad
B_N(\sigma)=\sum_{n\le N}\eta_n|a_n|^2n^{-2\sigma}.
\]

For every \(\sigma\) with \(A_N(\sigma)>0\), independence and nonnegativity give

\[
\mathbb EB_N=\pi A_N,
\qquad \mathbb EB_N^2
=\pi^2 A_N^2+\pi(1-\pi)\sum_{n\le N}|a_n|^4n^{-4\sigma}
\le\pi A_N^2.
\]

Paley--Zygmund at one half the mean therefore gives

\[
\mathbb P\bigl(B_N(\sigma)\ge\tfrac\pi2 A_N(\sigma)\bigr)\ge\tfrac\pi4.
\]

In particular, for every \(r>0\),

\[
\mathbb E B_N(\sigma)^r\ge c_{\pi,r} A_N(\sigma)^r,
\quad c_{\pi,r}=\tfrac\pi4(\tfrac\pi2)^r>0.
\]

Set \(U_N=\int A_N^r\,d\mu_\alpha\) and \(V_N=\int B_N^r\,d\mu_\alpha\). Tonelli yields \(\mathbb EV_N\ge c_{\pi,r}U_N\); pointwise \(0\le V_N\le U_N\). Hence

\[
\mathbb P\bigl(V_N\ge\tfrac{c_{\pi,r}}2 U_N\bigr)\ge\tfrac{c_{\pi,r}}2.
\]

Because \(f\notin\mathscr H^{2,q}_\alpha\), monotone convergence gives \(U_N\uparrow\infty\). Therefore \(\mathbb P(\lim_N V_N=\infty)\ge c_{\pi,r}/2>0\). This divergence event is a tail event: altering finitely many indicators adds or removes only a finite Dirichlet polynomial, which has finite quadratic mixed norm, and membership in the vector or quasi-Banach space is invariant under such alterations. Kolmogorov's zero--one law raises its probability to one. Since \(|Y_n|^2\ge\delta^2\eta_n\), it follows that

\[
\mathbb P\bigl(\mathcal R_Y f\in\mathscr H^{2,q}_\alpha\bigr)=0.
\]

Thus \((\mathscr H^{2,q}_\alpha)_{*,Y}\subseteq\mathscr H^{2,q}_\alpha\) for every nonconstant iid law \(Y\), with no moment requirement.

**Step 2. Universal reverse inclusion for arbitrary Hardy exponent.** Take independent copies \(X_n'\) of \(X_n\). If \(\mathcal R_X f\in\mathscr H^{p,q}_\alpha\) almost surely, then \(\sum a_n(X_n-X_n')n^{-s}\in\mathscr H^{p,q}_\alpha\) almost surely, because the space is linear. The differences \(Y_n=X_n-X_n'\) are iid symmetric and nonconstant. The established symmetry lemma [1, Lemma 3.3] identifies their \(\mathscr H^{p,q}\)- and \(\mathscr H^{2,q}\)-symbol spaces for all positive exponents, without moment hypotheses. Therefore \(\mathcal R_Y f\in\mathscr H^{2,q}_\alpha\) almost surely. Step 1 implies \(f\in\mathscr H^{2,q}_\alpha\). This proves the unconditional reverse inclusion.

**Step 3. An infinite-second-moment obstruction when \(0<q<2\).** Suppose \(\mathbb E|Y_1|^2=\infty\) for iid nonnegative-magnitude coefficients \(Y_n\); only the distribution of \(|Y_n|^2\) matters. Here \(0<r=q/2<1\). Truncate \(|Y_n|^2\) at a finite level and apply the weak law of large numbers; since the truncation means can be made arbitrarily large, the averages of \(|Y_n|^2\) diverge to infinity in probability. In particular, for each \(j\ge1\) there is a positive integer \(N_j\) for which

\[
\mathbb P\left(\frac1{N_j}\sum_{\ell=1}^{N_j}|Y_\ell|^2\ge K_j\right)>1-2^{-j},
\qquad K_j=2^{2j/r}.
\]

Let \(I_k=\{n\ge1:2^k\le\log n<2^{k+1}\}\). Choose strictly increasing \(k_j\ge1\) with \(|I_{k_j}|\ge N_j\), and select distinct \(n_{j,\ell}\in I_{k_j}\) for \(1\le\ell\le N_j\). Define a Dirichlet series by assigning

\[
|a_{n_{j,\ell}}|^2=\frac{A_j}{N_j},\quad
A_j=\left(2^{-j}2^{k_j(\alpha+1)}\right)^{1/r},
\]

and making all other coefficients zero. The logarithmic-dyadic characterization [1, Theorem 3.1] gives

\[
\sum_{k\ge0}2^{-k(\alpha+1)}\left(\sum_{n\in I_k}|a_n|^2\right)^r
=\sum_{j\ge1}2^{-j}<\infty,
\]

hence \(f\in\mathscr H^{2,q}_\alpha\). This coefficient series also converges absolutely in a right half-plane: \(|I_k|<\exp(2^{k+1})\), so, for any fixed \(\sigma>1\), the absolute sum over block \(j\) is at most \(\sqrt{N_jA_j}e^{-\sigma 2^{k_j}}\le\sqrt{A_j}e^{-(\sigma-1)2^{k_j}}\), which is summable, since \(A_j\) grows at most exponentially in \(k_j\) and \(k_j\) grows strictly. The construction thus lies in the stipulated Dirichlet-series domain.

The selected iid random coefficients within each block have the same law as the sample of length \(N_j\) displayed above. By the first Borel--Cantelli lemma, with probability one, all but finitely many blocks satisfy

\[
\frac1{N_j}\sum_{\ell=1}^{N_j}|Y_{n_{j,\ell}}|^2\ge K_j.
\]

For every such sample, the randomized logarithmic-dyadic criterion has lower bound

\[
\sum_{j\text{ good}}2^{-k_j(\alpha+1)}
\left(\sum_{\ell=1}^{N_j}|a_{n_{j,\ell}}Y_{n_{j,\ell}}|^2\right)^r
\ge\sum_{j\text{ good}}2^{-j}K_j^r
=\sum_{j\text{ good}}2^j=\infty.
\]

Consequently \(\mathcal R_Y f\notin\mathscr H^{2,q}_\alpha\) almost surely. The proof is constructive at the distributional level; the requisite \(N_j\) are finite but depend on the iid law.

**Step 4. Necessity of the sharp moment and centering conditions.** Assume the equality of symbol spaces in the theorem. When \(2\le q<4\), the already established necessity in [1, Theorem 3.5] gives \(X_1\in L^q\), and additionally \(\mathbb EX_1=0\) if \(p>2\). For \(0<q<2\), suppose to the contrary \(\mathbb E|X_1|^2=\infty\). An independent copy \(X_1'\) then has \(\mathbb E|X_1-X_1'|^2=\infty\): for any \(M\) with \(\mathbb P(|X_1'|\le M)>0\), the event \(|X_1|>2M\) and \(|X_1'|\le M\) forces \(|X_1-X_1'|\ge|X_1|/2\); independence and infinite second moment finish the argument. Apply the block construction in Step 3 to the symmetric law \(Y_1=X_1-X_1'\). The constructed \(f\in\mathscr H^{2,q}_\alpha\) cannot have \(\mathcal R_Yf\in\mathscr H^{2,q}_\alpha\) almost surely. But equality assumed for \(X\), independent-copy subtraction, and [1, Lemma 3.3] would imply exactly that almost-sure membership. Contradiction. Thus \(X_1\in L^2\) is necessary.

If additionally \(p>2\), the mean now exists. The strict embedding \(\mathscr H^{p,q}_\alpha\subsetneq\mathscr H^{2,q}_\alpha\) for \(p>2\) is established by the mixed-space embedding theorem [2, Theorem 1.6]. Choose \(g\) in the difference. If \(\mathbb E X_1=m\ne0\), the centered law \(X_1-m\) is in \(L^2\). The established sufficiency theorem [1, Theorem 3.4] gives \(\mathcal R_{X-m}g\in\mathscr H^{p,q}_\alpha\) almost surely, but \(m g+\mathcal R_{X-m}g\notin\mathscr H^{p,q}_\alpha\) on those outcomes by linearity, contradicting the assumed inclusion. Thus \(m=0\).

**Step 5. Sufficiency.** The randomization sufficiency result [1, Theorem 3.4] states that, for all positive \(p,q\), the moment \(\mathbb E|X_1|^{\max\{2,q\}}<\infty\) gives \(\mathscr H^{2,q}_\alpha\subseteq(\mathscr H^{p,q}_\alpha)_{*,X}\) when \(p\le2\); for \(p>2\) it gives the same inclusion under the additional mean-zero condition. Combine with Step 2 to obtain equality. The theorem follows. \(\square\)

## Verification

All probability estimates have explicit dependence on the Bernoulli success probability \(\pi\), with no moment constant or truncation of the coefficient law hidden in the universal reverse inclusion. The divergence in Step 3 follows from the exact identity \(2^{-j}(2^{2j/r})^r=2^j\). The dyadic weights satisfy the finite total \(\sum_{j\ge1}2^{-j}=1\) and the random-block lower bound tends to infinity along almost every sample by Borel--Cantelli. These are analytic identities rather than extrapolations from a finite computation.

The domain restriction \(0<q<4\) selects the regime left partially characterized in [1]; Steps 1--2 in fact apply to all finite positive \(q\). The proof invokes exact published supporting lemmas with identifiers and numerical hypotheses stated in Steps 2, 3, 4, 5. No computer-assisted infinite claim, external certification, or independent validation is asserted.

## Relationship to prior work

[1] first characterized the equality criterion for \(q\ge4\) and obtained only one-sided conditions when \(0<q<4\). In particular [1, Theorem 3.7] assumed \(L^4\) for the general reverse inclusion. The new universal reverse-inclusion lemma removes that hypothesis; the infinite-variance dyadic-block construction supplies the missing second-moment necessity for \(q<2\). The sufficiency and the symmetry transfer principle themselves are credited to [1].

[2] treats canonical Bernoulli, Steinhaus, and Gaussian randomizations and proves strict mixed-space embeddings; its canonical-law result does not classify arbitrary iid coefficient distributions. [3] concerns ordinary random analytic Taylor series in the disk and ball, not the infinite-torus Bohr lift of general Dirichlet series; its accessible abstract describes an exact characterization for \(q\ge4\), not this sub-four statement. The full text of [3] was not available in the inspected source, leaving a limited historical-priority risk. No comprehensive historical uniqueness claim is made.

## Limitations

The theorem requires identically distributed independent nonconstant scalar coefficient variables and finite positive \(p,q\). Its full if-and-only-if classification is stated for \(q<4\) to separate it from [1]'s established \(q\ge4\) theorem. The universal reverse inclusion holds for arbitrary positive exponents but does not itself imply sufficient randomization without an integrability condition. The \(N_j\) in the infinite-variance witness depend on the coefficient law and are not a uniform numerical cutoff. Independent mathematical validation has not been performed. Historical priority beyond the inspected primary sources is not established.

## References

[1] Jiale Chen, Min He, Maofa Wang, *A converse to Littlewood-type theorem for random Dirichlet series*, arXiv:2610.17876v1, first posted 13 October 2026, https://arxiv.org/html/2610.17876v1. Specifically Theorem 3.1, Lemma 3.3, Theorems 3.4, 3.5, 3.7, and the Introduction.

[2] Jiale Chen, Xin Guo, Maofa Wang, *Littlewood-type theorems for random Dirichlet series*, arXiv:2402.00314v1, first posted 1 February 2024, https://arxiv.org/html/2402.00314v1. Specifically Theorem 1.6, Theorem 3.2 and Corollary 3.3.

[3] Liangwei Chen and Chao Liu, *A converse of Littlewood-type theorem on random analytic functions in mixed norm spaces*, *Canadian Journal of Mathematics*, first online 21 July 2026, doi:10.4153/S0008414X26102399; only the publisher's accessible abstract and bibliographic material were used in the comparison.
