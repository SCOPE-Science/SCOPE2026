# Sharp reciprocal-moment phase transition and logarithmic crossover for a minimal random walk

## Finding
Fix \(0<p<1\). In the zero-restart minimal random walk, let \(K_1=1\) and \(K_{n+1}=K_n+I_{n+1}\), where conditionally on the past, \(I_{n+1}\) is Bernoulli with parameter \(pK_n/n\). For \(u>0\), write \(D_n(u)=\mathbb E[K_n^{-u}]\). The inverse moments obey a sharp phase transition:

\[
\lim_{n\to\infty}n^{pu}D_n(u)=\frac{\Gamma(1-u)}{\Gamma(1-pu)},\qquad 0<u<1;
\]
\[
D_n(1)=\frac{p}{\Gamma(1-p)}n^{-p}\bigl(\log n-\psi(1-p)\bigr)+o(n^{-p});
\]
\[
\lim_{n\to\infty}n^p D_n(u)=\frac{\zeta(u)}{\Gamma(1-p)},\qquad u>1.
\]
Here \(\psi\) is the digamma function and \(\zeta\) the Riemann zeta function. The critical-window interpolation is explicit: for each fixed real \(b\), with \(u_n=1-b/\log n>0\) for all sufficiently large \(n\),
\[
\lim_{n\to\infty}\frac{n^p}{\log n}D_n(u_n)=\frac{e^{pb}-1}{b\,\Gamma(1-p)},
\]
where the quotient at \(b=0\) is defined continuously as \(p/\Gamma(1-p)\). This includes the precise finite part at the critical inverse exponent one.

## Assumptions and scope
The sole parameters are fixed \(p\in(0,1)\), \(u>0\) in the three fixed-exponent assertions, and fixed \(b\in\mathbb R\) in the moving-exponent assertion. There is exactly one initial movement, no new movement after recalling a stop, and movement probabilities are \(pK_n/n\). All limits concern expectations over the endogenous movement-count process. The bounds are not asserted uniformly in \(p\), in unbounded \(b\), or in arbitrary time-dependent memory parameters.

## Proof
Set \(h_{n,k}=\Pr(K_n=k)\), with \(h_{n,k}=0\) outside \(1\le k\le n\). The exact forward equations are
\[
h_{n+1,k}=(1-pk/n)h_{n,k}+p(k-1)h_{n,k-1}/n\quad(1\le k\le n),
\qquad h_{n+1,n+1}=p h_{n,n}.
\]
Thus \(h_{n,1}=\prod_{j=1}^{n-1}(1-p/j)=\Gamma(n-p)/(\Gamma(1-p)\Gamma(n))\). In particular, \(n^p h_{n,1}\to c_p:=1/\Gamma(1-p)\). The nonnegative interior recurrence and the exceptional endpoint \(h_{n,n}=p^{n-1}\) imply
\[
\sup_{1\le k\le n}h_{n,k}\le C_p n^{-p}.
\]
Indeed, for interior indices the two coefficients sum to \(1-p/n\le(n/(n+1))^p\); the endpoint term \(p^n\) is exponentially small and may be absorbed by increasing \(C_p\).

**Local mass lemma.** For each *fixed* integer \(k\ge1\),
\[
n^p h_{n,k}\longrightarrow c_p.
\]
For \(k=1\) this was shown above. For \(k\ge2\) put \(r_{n,k}=h_{n,k}/h_{n,1}\), for \(n\ge k\). Dividing the forward recurrence by \(h_{n+1,1}=(1-p/n)h_{n,1}\) yields
\[
r_{n+1,k}=\bigl(1-a_{n,k}\bigr)r_{n,k}+a_{n,k}r_{n,k-1},\qquad a_{n,k}=\frac{p(k-1)}{n-p}.
\]
For fixed \(k\) and \(n\ge k\), \(0<a_{n,k}<1\) and \(\sum_{n\ge k}a_{n,k}=\infty\). If \(r_{n,k-1}\to1\), this stable averaging recursion forces \(r_{n,k}\to1\): iterate, discard a finite initial segment using the vanishing product \(\prod(1-a_{n,k})\), then bound the remaining driving error by its supremum. Induction proves the lemma.

**Subcritical powers.** For \(0<u<1\), let \(g_u(k)=\Gamma(k-u)/\Gamma(k)\). The relation \(g_u(k+1)=(1-u/k)g_u(k)\) and the movement recursion give the exact finite-time identity
\[
\mathbb E[g_u(K_n)]=\frac{\Gamma(1-u)\Gamma(n-pu)}{\Gamma(1-pu)\Gamma(n)}.
\]
The uniform gamma-ratio estimate \(g_u(k)=k^{-u}+O_u(k^{-u-1})\) for \(k\ge2\), together with the local probability bound, shows that \(\mathbb E[g_u(K_n)]-D_n(u)=O_{p,u}(n^{-p})\). Since \(pu<p\), this is negligible compared with \(n^{-pu}\). The gamma-ratio asymptotic proves the first limit.

**Supercritical powers.** The local mass lemma and \(n^p h_{n,k}\le C_p\) allow dominated convergence against \(k^{-u}\) for every \(u>1\), proving the zeta constant.

**Exact critical finite part.** Introduce \(R_n(s)=\Gamma(n-p+ps)/(\Gamma(n)\Gamma(1-p+ps))\), analytic near \(s=0\). For \(s>0\), the preceding gamma identity is \(\mathbb E[\Gamma(K_n-1+s)/\Gamma(K_n)]=\Gamma(s)R_n(s)\). Since the \(k=1\) term is \(h_{n,1}\Gamma(s)\) and \(R_n(0)=h_{n,1}\), subtraction and passage to \(s\downarrow0\) give
\[
\sum_{k=2}^n\frac{h_{n,k}}{k-1}
=R'_n(0)
=p h_{n,1}[\psi(n-p)-\psi(1-p)].
\]
The elementary identity \(k^{-1}=(k-1)^{-1}-[k(k-1)]^{-1}\) now gives the *exact* expression
\[
D_n(1)=h_{n,1}+p h_{n,1}[\psi(n-p)-\psi(1-p)]-\sum_{k=2}^n\frac{h_{n,k}}{k(k-1)}.
\]
Dominated convergence yields \(n^p\sum_{k\ge2}h_{n,k}/[k(k-1)]\to c_p\sum_{k\ge2}1/[k(k-1)]=c_p\). This cancels the term \(n^p h_{n,1}\to c_p\). Since \(\psi(n-p)=\log n+o(1)\) and \(h_{n,1}=c_p n^{-p}(1+O_p(n^{-1}))\), the stated two-term formula follows.

**Logarithmic crossover.** For real \(s\ne0\) sufficiently close to zero, the gamma identity continues analytically after subtraction of the \(k=1\) pole:
\[
\mathbb E\left[\frac{\Gamma(K_n-1+s)}{\Gamma(K_n)};\ K_n\ge2\right]
=\Gamma(s)[R_n(s)-R_n(0)].
\]
Uniformly for \(|s|\le\varepsilon_0<1/2\), the difference between the summand and \(k^{-1+s}\), for \(k\ge2\), is bounded by \(C k^{-2+\varepsilon_0}\). The uniform point-mass bound therefore implies
\[
D_n(1-s)=\Gamma(s)[R_n(s)-R_n(0)]+h_{n,1}+O_p(n^{-p})
\]
uniformly in that interval (with the value at zero interpreted by continuity). Put \(s=b/\log n\). The gamma-ratio formula gives \(R_n(s)/R_n(0)\to e^{pb}\) for fixed \(b\), \(n^p R_n(0)\to c_p\), and \(\Gamma(s)/\log n\to1/b\) for \(b\ne0\). Division by \(n^{-p}\log n\) proves the crossover for nonzero \(b\); the exact critical expansion supplies its \(b=0\) value. All limiting interchanges above were justified either by summable domination or by uniform point-mass control, not by distributional convergence alone.

## Verification
`checker.py` is a standalone Python 3 script using rational transition recurrences. It checks the exact normalized gamma identity for three discounts and three fractional exponents at every \(1\le n\le34\), and the exact critical derivative identity. Its 612 rational assertions pass. It also compares direct floating-point recursions at \(n=800,1600,3200\) with the two-term asymptotic, without treating finite computation as a proof. The recorded run is included in `checker_output.txt`.

## Relationship to prior work
Liang, *Normal approximation and self-normalized moderate deviations for the minimal random walk with random step sizes* (arXiv:2610.29156v1, Section 3.2, Lemma 3.2), provides the exact gamma expectation used here and upper bounds of precisely the three inverse-moment orders; those facts are not novel claims. The present statement supplies sharp multiplicative constants in all regimes, a critical finite-part correction and a moving-exponent interpolation. Miyazaki and Takei, *Limit theorems for the 'laziest' minimal random walk model of elephant type* (arXiv:2003.04441v1), establish positive moments and the Mittag--Leffler weak limit, which by itself does not control unbounded reciprocal moments. The process is also equivalent to a zero-concentration Pitman--Yor block-count chain, so possible implicit coverage by general partition asymptotics remains a historical-priority risk. The contribution is not a new Mittag--Leffler law or the gamma-transform identity.

## Limitations
The formulas concern the zero-restart chain with one initial movement and fixed discount strictly between zero and one; they do not prove analogous results for positive restart probability or general random initial counts. The crossing is pointwise for each finite \(b\), not uniform in an expanding window. No independence certificate or claim of historical uniqueness is made. Exact finite checks alone cannot establish the infinite limits. An independently checked literature-priority assessment is outstanding.

## References
1. Shuyuan Liang (2026), *Normal approximation and self-normalized moderate deviations for the minimal random walk with random step sizes*, arXiv:2610.29156v1, first posted 21 October 2026. https://arxiv.org/html/2610.29156v1
2. Tatsuya Miyazaki and Masato Takei (2020), *Limit theorems for the 'laziest' minimal random walk model of elephant type*, arXiv:2003.04441v1. https://arxiv.org/html/2003.04441v1
3. Dolera and Favaro (2018), *A Berry--Esseen theorem for Pitman's alpha-diversity*, arXiv:1809.09276; background on exchangeable-partition block counts, not a source for the present critical reciprocal-moment expansion. https://arxiv.org/abs/1809.09276
