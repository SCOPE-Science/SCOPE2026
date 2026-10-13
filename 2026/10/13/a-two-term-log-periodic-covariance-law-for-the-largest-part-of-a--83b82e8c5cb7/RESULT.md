# A two-term log-periodic covariance law for the largest part of a random composition

## Finding

Let a composition of the positive integer \(N\ge 2\) be selected uniformly from its \(2^{N-1}\) ordered compositions. Let \(K_N\) count its parts and \(M_N\) be its largest part. Put \(n=N-1\), \(x_n=\{\log_2 n\}\), and, for \(x\in[0,1]\), define the absolutely convergent series

\[
P(x)=\sum_{k\in\mathbb Z}2^{x-k}e^{-2^{x-k}},\qquad
Q(x)=\sum_{k\in\mathbb Z}(k-x)2^{x-k}e^{-2^{x-k}}.
\]

**Theorem.** As \(N\to\infty\) through the integers,

\[
\boxed{\operatorname{Cov}(K_N,M_N)
=-\tfrac12\big[(\log_2 n-2)P(x_n)+Q(x_n)\big]+o(1).}
\]

The remainder is absolute \(o(1)\), not merely small relative to \(\log n\). The smooth one-periodic function \(P\) is positive and nonconstant, with Fourier coefficients

\[
\widehat P(\ell)=\frac1{\ln2}\Gamma\!\left(1-\frac{2\pi i\ell}{\ln2}\right),\qquad \ell\in\mathbb Z.
\]

The covariance is strictly negative for every \(N\ge2\), and its leading coefficient has no scalar limit: \(\operatorname{Cov}(K_N,M_N)/\ln N\) has the nonconstant phase profile \(-P(x)/(2\ln2)\). Moreover,

\[
\operatorname{Corr}(K_N,M_N)=-\Theta\!\left(\frac{\ln N}{\sqrt N}\right),
\]

where \(-\Theta\) means the correlation is negative and its absolute value is bounded above and below by positive constant multiples of the stated quantity for all sufficiently large \(N\). The result is for *unrestricted* compositions, not the different ensemble excluding parts of size one.

## Assumptions and scope

A composition is an ordered list of positive integer parts summing to \(N\), and every composition has probability \(2^{1-N}\). It corresponds to \(n=N-1\) independent fair separator bits \(B_1,\ldots,B_n\), with \(1\) indicating a cut: \(K_N=1+\sum_i B_i\), while \(M_N=1+L_n\), where \(L_n\) is the longest run of consecutive zeros in the bitstring (possibly zero). All stated asymptotics hold along the full integer sequence, including every logarithmic lattice phase. No assumption on an external data-generating distribution is involved.

## Proof

**1. Covariance is a probability derivative.** Temporarily let the separator bits be independent Bernoulli with success probability \(p\in(0,1)\), and put \(q=1-p\). For any bounded statistic \(G\) of the \(n\) bits, direct differentiation of the product measure yields

\[
\operatorname{Cov}_p\!\left(\sum_i B_i,G\right)=pq\,\partial_p\mathbb E_pG.
\]

Write \(f_{n,r}(p)=\Pr_p(L_n<r)\) for \(1\le r\le n\). Since \(\mathbb E_pL_n=\sum_{r=1}^n(1-f_{n,r}(p))\), at \(p=q=1/2\),

\[
C_n:=\operatorname{Cov}(K_N,M_N)=-\tfrac14\sum_{r=1}^n f'_{n,r}(1/2).\tag{1}
\]

Every event \(\{L_n<r\}\) is increasing in the bits and has a positive-probability pivotal bit, so all its derivatives are positive. This already proves strict finite-size negativity.

**2. Exact avoidance generating function.** A binary word avoiding a run of \(r\) zeros is empty or begins with one of \(1,01,\ldots,0^{r-1}1\), possibly followed by a final shorter zero suffix. Summing their probabilities proves, for every fixed \(r\ge1\),

\[
\sum_{m\ge0}f_{m,r}(p)z^m
=\frac{1-(qz)^r}{1-z+pq^r z^{r+1}}.\tag{2}
\]

The coefficient identity can also be verified by the recurrence \(f_{m,r}=f_{m-1,r}-pq^r f_{m-r-1,r}\) for \(m\ge r+1\), with \(f_{m,r}=1\) for \(m<r\) and \(f_{r,r}=1-q^r\).

**3. A uniform differentiated pole estimate.** Let \(r\) lie in the central window

\[
\log_2 n-3\log_2\ln n\le r\le\log_2 n+3\log_2\ln n.\tag{3}
\]

At \(p=1/2\), set \(\varepsilon=pq^r=2^{-r-1}\), \(\lambda=n\varepsilon\). Then \(r=O(\ln n)\), \(\varepsilon=O((\ln n)^3/n)\), and \(\lambda=O((\ln n)^3)\). For \(p\) in a small fixed neighborhood of \(1/2\), Rouché's theorem on \(|z|=3/2\) shows that \(1-z+pq^rz^{r+1}\) has precisely one zero inside the circle: the perturbation has modulus at most \(C(3q/2)^r=o(1)\), whereas \(|1-z|\ge1/2\). The real simple zero and residue satisfy

\[
z_r=1+\varepsilon+O(r\varepsilon^2),\quad
z_r'=\varepsilon'+O(r^2\varepsilon^2),\quad
A_r=-\frac{1-(qz_r)^r}{z_r D'(z_r)}=1+O(r\varepsilon),\quad A_r'=O(r^2\varepsilon),
\]

where \(D(z)=1-z+pq^rz^{r+1}\), primes denote \(p\)-derivatives, and \(\varepsilon'=q^r-prq^{r-1}\). The contour integral on \(|z|=3/2\), including its \(p\)-derivative, is \(O((3/2)^{-n})\) uniformly in (3). Thus

\[
f_{n,r}(p)=A_r(p)z_r(p)^{-n}+O((3/2)^{-n}),
\]

and differentiation followed by \(\ln z_r=\varepsilon+O(r\varepsilon^2)\) gives

\[
f'_{n,r}(1/2)=-n\varepsilon'e^{-n\varepsilon}+o((\ln n)^{-2})
\tag{4}
\]

uniformly in the central window. To check the error rather than assuming it, the terms after differentiation are bounded by a fixed polynomial in \(r\) and \(n\varepsilon\), divided by \(n\): specifically, their sum is
\(O(r^2\varepsilon+n r^2\varepsilon^2+n^2r^2\varepsilon^3)\), and the residue/contour terms satisfy the same or stronger bounds. Under (3), this is \(O((\ln n)^{11}/n)=o((\ln n)^{-2})\). There are only \(O(\ln\ln n)\) central values of \(r\).

**4. Tails of the differentiated series.** For \(r\) below the lower endpoint in (3), selecting \(\lfloor n/r\rfloor\) disjoint length-\(r\) blocks gives \(f_{n,r}(1/2)\le\exp[-\lfloor n/r\rfloor 2^{-r}]\le\exp[-c(\ln n)^2]\). Direct differentiation of the product measure gives \(|f'_{n,r}(1/2)|\le2n f_{n,r}(1/2)\), so their entire contribution in (1) is \(o(1)\). For \(r\) above the upper endpoint, Russo's pivotal-bit formula gives \(0\le f'_{n,r}(1/2)\le nr2^{1-r}\): a pivotal position must belong to one of at most \(r\) windows whose other \(r-1\) entries are zero. Summing \(nr2^{1-r}\) over this upper tail is \(O((\ln n)^{-2})\). The corresponding tails of \(\sum_r(r-1)\lambda e^{-\lambda}\) are also \(o(1)\), by geometric decay for small \(\lambda\) and superexponential decay for large \(\lambda\).

At \(p=1/2\), \(\varepsilon'=(2-2r)\varepsilon\). Inserting (4) into (1), with the verified tail bounds, proves

\[
C_n=-\tfrac12\sum_{r\ge1}(r-1)\lambda_r e^{-\lambda_r}+o(1),
\qquad\lambda_r=n2^{-r-1}.\tag{5}
\]

**5. Lattice expansion and nonconstant phase.** Put \(t=\log_2 n-1\), \(x=\{t\}=x_n\), and reindex \(r=\lfloor t\rfloor+k\). Then \(\lambda_r=2^{x-k}\) and \(r-1=(\log_2n-2)+(k-x)\). Extending the finite lower index to \(k\in\mathbb Z\) changes (5) by \(o(1)\). Equation (5) becomes the theorem. Reindexing shows one-periodicity, and termwise differentiation is justified by exponential and superexponential tail decay. Period integration with \(u=2^{x-k}\) yields

\[
\widehat P(\ell)=\frac1{\ln2}\int_0^\infty u^{-2\pi i\ell/\ln2}e^{-u}\,du
=\frac{\Gamma(1-2\pi i\ell/\ln2)}{\ln2}.
\]

Gamma has no zeros, so \(P\) is nonconstant. It is also positive and continuous on a compact period, hence bounded above and below by strictly positive constants. The phases \(\{\log_2n\}\) are dense, using integer sequences nearest \(2^{j+x}\), proving the absence of a constant covariance-to-\(\ln n\) limit.

**6. Correlation scale.** The separator representation gives \(\operatorname{Var}(K_N)=n/4\). We verify \(0<c\le\operatorname{Var}(L_n)\le C<\infty\) for all large \(n\). For \(r_0=\lfloor\log_2n\rfloor\), the pole estimate gives \(\Pr(L_n<r_0)=e^{-n2^{-r_0-1}}+o(1)\), bounded away from zero and one, hence a positive variance lower bound. For the upper bound, the union bound yields \(\Pr(L_n\ge r_0+t)\le n2^{-r_0-t}\le 2^{1-t}\). For the lower tail, count occurrences of \(1\) followed by \(r\) zeros at interior starting sites. Indicators with starting indices within \(r\) positions are mutually exclusive, and those farther apart are independent; therefore the count \(W_r\) satisfies \(\operatorname{Var}(W_r)\le\mathbb EW_r=(n-r)2^{-r-1}\). Since \(L_n<r\) entails \(W_r=0\), Chebyshev gives \(\Pr(L_n<r)\le 1/\mathbb EW_r=O(2^r/n)\) for \(r\le r_0\) and \(r\le n/2\). These geometric tails imply bounded second moments for \(L_n-r_0\). The covariance expansion and variance bounds yield the stated correlation rate.

## Verification

The standalone `artifacts/verify.py` independently enumerates all fair binary strings for lengths \(1\le n\le12\) and checks their covariance against exact rational derivatives of recurrence (2). It also evaluates the exact recurrence for lengths \(100,1000,10000\) at machine precision and compares it with both the two-term periodic expression and the predicted leading logarithmic scale; this numerical check corroborates but does not prove the infinite asymptotic. The critical infinite argument is the uniform differentiated residue estimate plus the explicit tail bounds in Proof steps 3–4.

## Relationship to prior work

The classical longest-run framework and enumerative generating functions for compositions are established. Bender and Canfield (2005) prove growth results for large parts and normal limits for part counts, not their mixed two-term covariance. Lou (1996) provides finite joint distributions of longest runs and success counts using Markov-chain embedding, which covers the possibility of finite exact computations, not the present phase-dependent asymptotic. Finch (2020, Section 1 and Table 1) studies exactly the pair of composition statistics in this theorem, gives exact finite recurrences, and expressly proposes a different asymptotic correlation decay, proportional to \((\ln N)^{-5/2}\). The present theorem yields instead the order \((\ln N)/\sqrt N\) and a nonconstant periodic covariance profile. An earlier analysis of the **same** part-count/largest-part pair established strict negative regression, an exact coordinate-influence identity, and an upper bound of order \(O((\log N)^2)\) on the absolute covariance; it did **not** establish the sharp log-linear scale, an absolute \(o(1)\) two-term expansion, or log-periodic modulation. Those earlier structural properties are not claimed as new here. Separately, a mixed-covariance result for the number of **distinct** part sizes concerns a different statistic and does not determine the covariance with the **maximum** part, although its leading periodic kernel coincides. The new claim is solely the proved two-term covariance expansion and resulting correlation-rate distinction, not the established finite generating function, run law, or marginal limit.

## Limitations

The result is for fair separators (uniform unrestricted compositions). It does not establish a universal expansion under nonuniform cuts or 1-free compositions. There is no asserted scalar constant limit for the covariance divided by \(\ln N\). The periodic modulation is extremely small and difficult to distinguish numerically from a constant. The full text of Lou (1996) could not be obtained; implicit coverage by an earlier general asymptotic theorem remains a historical-priority risk. No independent scientific audit has been performed.

## References

1. E. A. Bender and E. R. Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electron. J. Combin. 12 (2005), R57, published 2005-11-07, https://doi.org/10.37236/1954. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v12i1r57/pdf/.
2. W. Y. W. Lou, *On Runs and Longest Run Tests: A Method of Finite Markov Chain Imbedding*, J. Amer. Statist. Assoc. 91 (1996), 1595–1601, https://doi.org/10.1080/01621459.1996.10476727.
3. S. Finch, *Covariance within Random Integer Compositions*, arXiv:2010.06643v2 (2020-10-19), https://arxiv.org/html/2010.06643v2.
4. M. F. Schilling, *The Longest Run of Heads*, College Math. J. 21 (1990), 196–207.
