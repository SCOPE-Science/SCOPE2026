# A sharp total-variation phase diagram for reinforced binary sampling

## Finding

Fix \(p\in(0,1)\), set \(q=1-p\), and let \(n\to\infty\) through integers. For each \(n\), choose a real concentration \(A_n>0\) with \(A_n\to\infty\). Let \(X_n\) count the color-one draws in a two-color, unit-reinforcement Pólya urn whose initial color masses are \(A_np\) and \(A_nq\). Let \(B_n\sim\operatorname{Bin}(n,p)\) be the independent-draw comparison, and write \(d_n=d_{\mathrm{TV}}(\mathcal L(X_n),\mathcal L(B_n))\), with \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_k|P\{k\}-Q\{k\}|\).

Put \(\rho_n=n/A_n\). The following three-regime statement is sharp:

\[
\begin{array}{ll}
\rho_n\to0:&\displaystyle \frac{d_n}{\rho_n}\longrightarrow\frac{e^{-1/2}}{\sqrt{2\pi}},\\[2mm]
\rho_n\to\rho\in(0,\infty):&\displaystyle d_n\longrightarrow F(\rho),\\[2mm]
\rho_n\to\infty:&d_n\longrightarrow1,
\end{array}
\]

where \(\Phi\) is the standard Gaussian distribution function and

\[
F(\rho)=2\left[\Phi\!\left(\sqrt{\frac{(1+\rho)\log(1+\rho)}{\rho}}\right)-\Phi\!\left(\sqrt{\frac{\log(1+\rho)}{\rho}}\right)\right].
\]

In particular, the constant in the regime \(A_n\gg n\) is independent of the fixed interior color fraction \(p\). The critical regime has a genuine nonzero error, even though both count distributions satisfy central limit theorems. The large-reinforcement regime becomes asymptotically perfectly distinguishable from independent sampling.

**Finite-sample structural assertion.** For every integer \(n\ge2\), every \(p\in(0,1)\), and every real \(A>0\), the likelihood ratio of the beta-binomial law to its same-mean binomial law is strictly log-convex as a function of the count. More precisely, the indices at which the beta-binomial probability is strictly smaller than the binomial probability form exactly one nonempty consecutive block. Therefore the total-variation distance equals the binomial-minus-beta-binomial probability of that block. This exact finite-sample fact is used in the critical-regime argument; it is not represented as a separately new general principle.

## Assumptions and scope

The Pólya urn uses unit reinforcement after each draw. Nonintegral initial masses are interpreted through the equivalent beta-mixture law; integral masses give the literal ball urn. The count probability is

\[
 b_{n,k}=\binom nk p^kq^{n-k},\qquad
 x_{n,k}=\binom nk\frac{(Ap)^{\overline{k}}(Aq)^{\overline{n-k}}}{A^{\overline n}},\quad 0\le k\le n,
\]

where the rising factorial is \(u^{\overline j}=\prod_{i=0}^{j-1}(u+i)\), with empty product one. Thus \(X_n\) is beta-binomial with beta shape parameters \(A_np,A_nq\). All assertions quantify over arbitrary positive real concentrations satisfying the indicated limits; no uniform claim is made as \(p\) approaches zero or one. The first-order constant applies specifically when \(n/A_n\to0\), not merely when \(A_n\to\infty\).

## Proof

**1. Exact two-crossing structure.** Fix \(n\ge2\) and omit the \(n\) subscript. Since every binomial mass is positive, set \(R_k=x_{n,k}/b_{n,k}\). A direct rising-factorial calculation gives

\[
\frac{R_{k+1}}{R_k}=\frac{q(Ap+k)}{p(Aq+n-k-1)}\quad(0\le k<n).
\]

The right side increases strictly with \(k\), proving strict log-convexity of \(R_k\). If \(P\sim\operatorname{Beta}(Ap,Aq)\), then \(x_{n,k}=\mathbb E[\binom nkP^k(1-P)^{n-k}]\). Strict Jensen convexity of the maps \(u\mapsto u^n\) and \(u\mapsto(1-u)^n\) yields \(R_0>1\) and \(R_n>1\). Moreover

\[
\operatorname{Var}(X)=npq\left(1+\frac{n-1}{A+1}\right)>npq=\operatorname{Var}(B).
\]

Thus the mass arrays cannot agree; because they both sum to one, some \(R_k<1\). The strictly convex logarithmic sequence \(\log R_k\) has a single nonempty interval of indices below zero. Call it \(I_{n,A}\); endpoint indices with equality are excluded harmlessly. Then

\[
d_{\mathrm{TV}}(X,B)=\Pr(B\in I_{n,A})-\Pr(X\in I_{n,A})
=\sup_{I\text{ integer interval}}|\Pr(B\in I)-\Pr(X\in I)|.
\]

The last equality follows because any signed mass array has its positive total equal to minus its negative total, and the negative part here is exactly one interval.

**2. Gaussian transition.** Let \(P_n\sim\operatorname{Beta}(A_np,A_nq)\), conditionally draw \(X_n\mid P_n\sim\operatorname{Bin}(n,P_n)\). The gamma representation of beta laws (or their characteristic functions) gives

\[
\frac{\sqrt{A_n}(P_n-p)}{\sqrt{pq}}\Rightarrow N(0,1).
\]

On the other hand, conditional on \(P_n\), the characteristic function of \((X_n-nP_n)/\sqrt{npq}\) tends in probability to \(\exp(-t^2/2)\) for each fixed \(t\), since \(P_n\to p\) in probability. Multiplying this conditional characteristic function by any bounded function of \(P_n\) proves joint asymptotic independence with the displayed beta fluctuation. For \(\rho_n\to\rho\in[0,\infty)\), therefore,

\[
\frac{X_n-np}{\sqrt{npq}}\Rightarrow N(0,1+\rho),\qquad
\frac{B_n-np}{\sqrt{npq}}\Rightarrow N(0,1).
\]

Weak convergence of real distribution functions to continuous limits is uniform in their argument. Hence interval-probability differences converge *uniformly over all intervals*, even intervals depending on \(n\). By Step 1, \(d_n\) converges to the largest absolute difference between the probabilities assigned to an interval by \(N(0,1)\) and \(N(0,1+\rho)\). For \(\rho>0\), their density curves cross precisely at \(\pm a\), where \(a^2=(1+\rho)\log(1+\rho)/\rho\). The maximizing interval is \([-a,a]\), and integrating the two densities gives exactly \(F(\rho)\) stated above. When \(\rho=0\), the same argument gives \(d_n\to0\), but not yet its leading constant.

**3. Complete separation for \(\rho_n\to\infty\).** In this regime, use the scale \(n/\sqrt{A_n}\). Conditional binomial noise satisfies

\[
\mathbb E\left[\left(\frac{\sqrt{A_n}(X_n-nP_n)}{n}\right)^2\right]
\le \frac{A_n}{4n}\longrightarrow0.
\]

Consequently \(\sqrt{A_n}(X_n/n-p)/\sqrt{pq}\Rightarrow N(0,1)\). For each fixed \(K>0\), the binomial law puts asymptotic mass \(\Pr\{|Z|\le K\}\) on \(|k-np|\le K\sqrt{npq}\), whereas the beta-binomial law puts asymptotically zero mass there because this window shrinks to a single point on the wider scale and the limiting normal has no atom at zero. Therefore \(\liminf d_n\ge\Pr\{|Z|\le K\}\) for every \(K\); letting \(K\to\infty\) gives \(d_n\to1\).

**4. Exact small-reinforcement first order.** Suppose \(\rho_n\to0\). For \(0\le k\le n\), put \(f_{n,k}(u)=\binom nk u^k(1-u)^{n-k}\). Beta centering and variance give

\[
\mathbb E(P_n-p)=0,\qquad v_n:=\mathbb E(P_n-p)^2=\frac{pq}{A_n+1}.
\]

The beta fourth central moment is \(O(A_n^{-2})\) and its third absolute central moment is \(O(A_n^{-3/2})\), constants depending on fixed \(p\) only. On a fixed closed subinterval of \((0,1)\) around \(p\), the binomial score identities and standard binomial central-moment bounds give

\[
\sum_{k=0}^n|\partial_u^3 f_{n,k}(u)|\le C_p n^{3/2},\quad
\sum_{k=0}^n|\partial_u f_{n,k}(p)|\le C_p n,
\quad \sum_{k=0}^n|\partial_u^2 f_{n,k}(p)|\le C_p n^2.
\]

Here the third-derivative estimate follows by writing \(\partial_u f=fS\), \(\partial_u^3f=f(S^3+3SS'+S'')\), with \(S=(k-nu)/(u(1-u))\), \(S'=-k/u^2-(n-k)/(1-u)^2\), and \(S''=2k/u^3-2(n-k)/(1-u)^3\). On the complement of the fixed parameter interval, Chebyshev applied to the fourth beta moment gives probability \(O(A_n^{-2})\). Taylor's theorem, summed over \(k\), then yields the **global \(\ell^1\) expansion**

\[
\sum_{k=0}^n\left|x_{n,k}-b_{n,k}-\frac{v_n}{2}\partial_p^2f_{n,k}(p)\right|
=O_p\!\left((n/A_n)^{3/2}+n^2/A_n^2\right)=o(n/A_n).
\]

For completeness, the complement contribution can be bounded termwise using \(\sum_k f_{n,k}(u)=1\) and the displayed bounds at \(p\); the bound is \(O((1+n+n^2)A_n^{-2})\). This is negligible relative to \(n/A_n\) because \(A_n\gg n\).

Writing \(U_n=(B_n-np)/\sqrt{npq}\), direct differentiation gives

\[
\partial_p^2 f_{n,k}(p)
= f_{n,k}(p)\frac{(k-np)^2-(q-p)(k-np)-npq}{p^2q^2}.
\]

Consequently, by the binomial central limit theorem and uniform integrability (bounded binomial fourth moments),

\[
\frac1n\sum_{k=0}^n|\partial_p^2f_{n,k}(p)|
\longrightarrow\frac{\mathbb E|Z^2-1|}{pq}
=\frac{4\varphi(1)}{pq},
\]

where \(Z\sim N(0,1)\) and \(\varphi(1)=e^{-1/2}/\sqrt{2\pi}\). The final equality is the integral identity \(\mathbb E|Z^2-1|=4\varphi(1)\), obtained by integration by parts on \(\{|Z|>1\}\). Using the global \(\ell^1\) expansion and the factor \(1/2\) in total variation gives

\[
 d_n\sim\frac{v_n}{4}\frac{4n\varphi(1)}{pq}
=\frac{n\varphi(1)}{A_n+1}\sim\varphi(1)\rho_n.
\]

This completes all regimes and the finite-sample assertion.

## Verification

The accompanying `verify.py` is standalone Python 3 standard-library code. It enumerates 200 exact rational beta-binomial/binomial parameter configurations (\(n=2,\ldots,11\), five initial-success masses, four initial-failure masses), verifying normalization, strict likelihood-ratio log-convexity, the connected negative block, and equality of its mass gap to the exact total-variation distance. A further 24 numerical checks compare finite-sample distances with the predicted critical profile or the small-reinforcement constant. The numerical calculations use log-gamma probability masses to avoid integer overflow. Run `python3 verify.py` in a directory containing this file. The finite tests do **not** establish any asymptotic theorem; the proof above establishes the quantified claims.

## Relationship to prior work

Meleşteu, Pascu and Pascu (2022, arXiv:2201.05870) establish a convex-order monotonicity theorem for Pólya counts and Bernstein–Stancu approximation errors; it supplies the motivating reinforced-sampling framework, not this exact total-variation phase diagram. Borovkov (2019, arXiv:1912.09665) gives strong Gaussian approximations for multicolor Pólya urns in joint long-time/large-initial-mass regimes, including the variance-inflation transition; this already covers the general probabilistic **Gaussian fluctuation picture** used in Step 2, but its stated results do not provide the sharp beta-binomial-versus-binomial total-variation profile or the universal small-reinforcement coefficient. Teerapabolarn (2008) derives a general, nonsharp total-variation upper bound of order \(n/A\), and Teerapabolarn (2014) develops a first-order improved binomial probability approximation for fixed count parameters. Those ingredients are explicitly treated as prior information, not independent novelty of the current argument. The finite-sample sign-interval mechanism permits passage from weak Gaussian convergence to sharp total variation without invoking a separate uniform local limit theorem.

## Limitations

The parameters \(p\) and \(q\) are fixed strictly between zero and one; boundary or varying-color-proportion regimes are not asserted. The small-reinforcement expansion is joint in \(n\) and \(A_n\), with \(n/A_n\to0\), and its error constants may depend on \(p\). No uniform convergence rate is supplied in the critical \(n/A_n\to\rho>0\) regime. Identifying a sharp coefficient is not an independent audit or a claim of absolute historical priority: more distant literature under different terminology may exist. The mathematical evidence consists of the analytic argument and its finite corroborating script, not exhaustive automated enumeration of all concentrations.

## References

1. D. Meleşteu, M. N. Pascu, N. R. Pascu, *Convex ordering of Pólya random variables and monotonicity of the error estimate of Bernstein-Stancu operators* (2022), arXiv:2201.05870, https://arxiv.org/abs/2201.05870; primary MSC2020 60E15, first posted 2022-01-15.
2. K. Borovkov, *Gaussian process approximations for multicolor Pólya urn models* (2019), arXiv:1912.09665, https://arxiv.org/abs/1912.09665.
3. K. Teerapabolarn, *A bound on the binomial approximation to the beta binomial distribution*, International Mathematical Forum **3** (2008), 1355–1358, author-hosted full text at https://www.researchgate.net/publication/228886368_A_bound_on_the_binomial_approximation_to_the_beta_binomial_distribution.
4. K. Teerapabolarn, *An improved binomial approximation for the beta binomial distribution*, International Journal of Pure and Applied Mathematics **97** (2014), 511–514, doi:10.12732/ijpam.v97i4.10, full text https://pdfs.semanticscholar.org/962b/6a442c5b724bfbdd44100444fd6518286d00.pdf.
