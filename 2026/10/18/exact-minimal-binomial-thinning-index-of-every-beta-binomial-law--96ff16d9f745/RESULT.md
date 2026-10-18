# Exact minimal binomial-thinning index of every beta-binomial law

## Finding
Let \(n\geq1\) be an integer and \(a,b>0\). Let \(W\sim\operatorname{Beta}(a,b)\) and, conditionally on \(W\), let \(X\sim\operatorname{Binomial}(n,W)\). For \(0<\alpha\leq1\), call \(X\) \(\alpha\)-thinnable if \(X\stackrel{d}{=}\alpha\circ Z\) for some nonnegative integer-valued \(Z\), where \(\alpha\circ Z\), given \(Z=j\), has law \(\operatorname{Binomial}(j,\alpha)\).

**Theorem.** The exact set of admissible thinning parameters is
\[
\boxed{\{\alpha\in(0,1]:X\stackrel{d}{=}\alpha\circ Z\}=\left[\frac{a+n-1}{a+b+n-1},\,1\right].}
\]
In particular, the minimal thinning index is
\[
\boxed{\rho(X)=\frac{a+n-1}{a+b+n-1}.}
\]
The representing law \(Z\) is unique for each admissible \(\alpha\). At the sharp endpoint, \(\Pr(Z=n-1)=0\); below the endpoint the formal inverse-thinning coefficient at \(n-1\) is negative. The distance from maximal scale has the exact form \(1-\rho(X)=b/(a+b+n-1)\).

## Assumptions and scope
The shapes \(a,b\) are arbitrary **real** positive numbers, not only integers. The count \(n\) is any positive integer. The Beta law has density \(w^{a-1}(1-w)^{b-1}/B(a,b)\) on \((0,1)\). No assumption of log-concavity or unimodality of the beta-binomial mass is imposed. Only classical independent Bernoulli thinning with fixed survival probability \(\alpha\) is considered; this does not classify generalized Pólya or beta-binomial thinning operators.

For \(n=1\), the result reduces to the sharp Bernoulli thinning threshold \(a/(a+b)\). For \(a=b=1\), the beta-binomial law is uniform on \(\{0,\ldots,n\}\) and the threshold is \(n/(n+1)\), a previously established special case.

## Proof
**1. Unique inverse law.** The probability-generating polynomial of \(X\) is
\[
P_X(z)=\mathbb E[(1-W+Wz)^n].
\]
If \(X\stackrel d=\alpha\circ Z\) with \(\alpha>0\), then \(Z\leq n\) almost surely: otherwise some mass of \(Z\) above \(n\) would give \(\alpha\circ Z\) positive mass above \(n\). Hence its generating polynomial is uniquely determined by
\[
Q_\alpha(z)=P_X\!\left(1-\frac1\alpha+\frac z\alpha\right)
=\sum_{k=0}^{n}q_k(\alpha)z^k,
\quad q_k(\alpha)=\binom nk\alpha^{-n}
\mathbb E[W^k(\alpha-W)^{n-k}].
\]
It satisfies \(Q_\alpha(1)=P_X(1)=1\). Thus \(X\) is \(\alpha\)-thinnable exactly when all \(q_k(\alpha)\geq0\), in which case \(Q_\alpha\) is the unique probability-generating polynomial of \(Z\).

**2. The odd Beta moment lemma.** For \(A,B>0\) and an odd positive integer \(m\), put
\[
L(A,B,m)=\frac{A+m-1}{A+B+m-1}.
\]
If \(V\sim\operatorname{Beta}(A,B)\), then
\[
\mathbb E[(c-V)^m]\geq0\qquad\text{for every real }c\geq L(A,B,m).
\]
We prove the assertion by induction over odd \(m\). Write \(\mu=A/(A+B)\). At \(m=1\) the claim is \(c-\mu\geq0\), and \(L(A,B,1)=\mu\). For odd \(m\geq3\), integration by parts against the Beta density gives the elementary Stein identity
\[
\mathbb E[(V-\mu)f(V)]=\frac1{A+B}\mathbb E[V(1-V)f'(V)]
\]
for every polynomial \(f\). Set \(f(v)=(c-v)^{m-1}\); rearranging yields
\[
\mathbb E[(c-V)^m]=(c-\mu)\mathbb E[(c-V)^{m-1}]
+\frac{m-1}{A+B}\mathbb E[V(1-V)(c-V)^{m-2}].
\]
The first term is nonnegative because \(m-1\) is even and \(c\geq L(A,B,m)\geq\mu\). For the second, weighting the Beta density by \(v(1-v)\) produces a positive multiple of the \(\operatorname{Beta}(A+1,B+1)\) density. The inductive threshold for its odd exponent \(m-2\) equals
\[
L(A+1,B+1,m-2)=\frac{A+m-2}{A+B+m-1}<L(A,B,m)\leq c.
\]
The induction hypothesis makes the second term nonnegative as well. The boundary terms in the integration-by-parts identity vanish for all positive \(A,B\), completing the lemma.

**3. Every coefficient is nonnegative at the candidate threshold.** Take
\[
\alpha_*=\frac{a+n-1}{a+b+n-1}.
\]
For \(k\in\{0,\ldots,n\}\), write \(m=n-k\). A Beta size-biasing identity gives
\[
\mathbb E[W^k(\alpha-W)^m]
=\frac{B(a+k,b)}{B(a,b)}\mathbb E[(\alpha-V_k)^m],
\quad V_k\sim\operatorname{Beta}(a+k,b).
\]
If \(m\) is even, the expectation is nonnegative for every real \(\alpha\). If \(m\) is odd, the lemma applies because
\[
L(a+k,b,m)=\frac{(a+k)+m-1}{(a+k)+b+m-1}
=\alpha_*,
\]
independently of \(k\). Therefore all \(q_k(\alpha)\geq0\) for every \(\alpha\in[\alpha_*,1]\). By Step 1, every such scale is admissible, including the endpoint.

**4. Sharpness.** The \(k=n-1\) inverse coefficient is
\[
q_{n-1}(\alpha)=\frac{n}{\alpha^n}\mathbb E[W^{n-1}]
\left(\alpha-\frac{\mathbb E[W^n]}{\mathbb E[W^{n-1}]}\right).
\]
The Beta moments satisfy \(\mathbb E[W^n]/\mathbb E[W^{n-1}]=(a+n-1)/(a+b+n-1)=\alpha_*\). Hence \(q_{n-1}(\alpha)<0\) for every \(0<\alpha<\alpha_*\), and \(q_{n-1}(\alpha_*)=0\). No smaller scale can be a thinning parameter. This completes the proof for all stated parameters.

## Verification
The standalone `check_beta_binomial.py` uses only the Python standard library. It evaluates the exact inverse coefficients via the Beta rising-factorial moment formula, checks nonnegative coefficients at the claimed endpoint, checks that the \(n-1\) coefficient vanishes there and turns negative at a strictly smaller scale, verifies normalization, and reconstructs every beta-binomial probability through forward thinning. It passed all 288 cases with \(1\le n\le8\) and \(a,b\in\{1/3,1/2,1,2,5/2,3\}\) using exact rational arithmetic. These finite checks are diagnostic; they do not establish the real-parameter theorem, which follows from the Beta integration-by-parts induction above.

## Relationship to prior work
Kella and Löpker [1] introduce the minimal binomial-thinning index, prove an **implicit general root-maximization characterization** for binomial mixtures in their Theorem 19, and explicitly calculate \(n/(n+1)\) for the uniform discrete law in Example 10. Their characterization supplies a nearby general framework, but the inspected article does not give a closed formula for arbitrary Beta mixing shapes or prove the odd Beta moment inequality used here. The displayed formula specializes to that known uniform case and evaluates the general root characterization over the full beta-binomial family.

Peyhardi [2] and Jones [3] study *quasi-Pólya/convolution thinning* and related closure/dual relationships involving beta-binomial conditional laws. The operation and target question here are different: **the sharp inverse scale for ordinary Bernoulli thinning when the marginal count itself is beta-binomial**. The identified results do not provide that threshold. These comparisons do not establish absolute priority; a differently named earlier de-thinning calculation may still exist.

## Limitations
This is a finite-support theorem. It does not treat random sample size, arbitrary non-Beta mixing laws, or quasi-Pólya thinning. The odd Beta lemma gives a sufficient common positivity threshold; it does not assert that its bound is optimal for each individual odd exponent. The endpoint is sharp for the beta-binomial **joint coefficient system** because the \(n-1\) coefficient becomes negative below it. Exact-rational tests only cover the specified finite grid. Novelty was assessed against relevant accessible primary literature and mathematical records, not established by an exhaustive literature theorem; unindexed equivalent results remain possible. Independent validation has not been performed.

## References
[1] O. Kella and A. Löpker, *On Binomial Thinning and Mixing*, arXiv:2202.10296 (first public version 21 February 2022); later *Indagationes Mathematicae* 34 (2023), 1121–1145. https://arxiv.org/abs/2202.10296 . See Theorem 19 and Example 10.

[2] J. Peyhardi, *On quasi Pólya thinning operator*, *Brazilian Journal of Probability and Statistics* 37 (2023), 643–666, doi:10.1214/23-BJPS585. https://doi.org/10.1214/23-BJPS585 .

[3] M. C. Jones, *Duals of convolution thinned relationships*, *Statistica Neerlandica* 78 (2024), 563–568, doi:10.1111/stan.12337. https://doi.org/10.1111/stan.12337 .
