# Sharp sampling crossover for independently shifted near-boundary Poisson quadrature

## Finding

For the circular Poisson kernel
\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2},\qquad 0<r<1,
\]
consider a periodic trapezoidal grid with an independently uniform random origin each time it is evaluated. Average \(m\) such shifted-grid evaluations, each using \(N\) nodes. Every evaluation integrates to one on average, but when the kernel approaches the circle, consistency is governed sharply by the **single effective sampling parameter** \(m(1-r^N)\).

Specifically, let \(N=N_k\ge1\), \(r=r_k\in(0,1)\), and \(m=m_k\ge1\) be any triangular array with \(q_k=r_k^{N_k}\to1\). On repetition \(j\), sample an independent \(\Theta_{k,j}\sim\mathrm{Unif}[0,2\pi/N_k]\), and define
\[
Q_{N,r}(\Theta)=\frac1N\sum_{\ell=0}^{N-1}P_r\left(\Theta+\frac{2\pi\ell}{N}\right),\qquad
A_k=\frac1{m_k}\sum_{j=1}^{m_k} Q_{N_k,r_k}(\Theta_{k,j}).
\]
Write \(\varepsilon_k=1-q_k\) and \(L_k=m_k\varepsilon_k\). The integral to be approximated is \(\frac1{2\pi}\int_{-\pi}^{\pi}P_{r_k}(\theta)\,d\theta=1\).

**Exact finite-sample identities.** For every \(N,r,m\),
\[
Q_{N,r}(\Theta)=P_{r^N}(N\Theta),\quad
\mathbb EA_k=1,\quad
\operatorname{Var}(A_k)=\frac{2r^{2N}}{m(1-r^{2N})}.
\]
These identities imply three mutually exclusive sampling regimes:

1. If \(L_k\to0\), then \(A_k\to0\) **in probability**, even though \(\mathbb EA_k=1\) identically and \(\operatorname{Var}(A_k)\to\infty\).
2. If \(L_k\to\lambda\in(0,\infty)\), then \(A_k\) converges in distribution to the nondegenerate Poisson shot-noise variable
   \[
   S_\lambda=\frac2\lambda\sum_{x\in\Xi_\lambda}\frac1{1+x^2},
   \]
   where \(\Xi_\lambda\) is a homogeneous Poisson point process on \(\mathbb R\) of intensity \(\lambda/(2\pi)\). The sum is finite almost surely, \(\mathbb ES_\lambda=1\), \(\operatorname{Var}(S_\lambda)=1/\lambda\), and for every \(t\ge0\) its Laplace transform is
   \[
   \mathbb E e^{-tS_\lambda}
   =\exp\left[-\frac\lambda{2\pi}\int_{\mathbb R}\left(1-\exp\left(-\frac{2t}{\lambda(1+x^2)}\right)\right)dx\right].
   \]
3. If \(L_k\to\infty\), then \(A_k\to1\) in mean square and
   \[
   \sqrt{L_k}(A_k-1)\ \Longrightarrow\ N(0,1).
   \]

**Sharp necessary and sufficient consistency condition.** Among every triangular array with \(q_k\to1\), convergence \(A_k\to1\) in probability holds **if and only if** \(m_k(1-r_k^{N_k})\to\infty\). The same condition is necessary and sufficient for mean-square convergence. Moreover, since \(r_k^{N_k}\to1\) implies \(1-r_k^{N_k}\sim N_k(1-r_k)\), the condition is equivalently
\[
m_kN_k(1-r_k)\to\infty.
\]
It is a **total node-evaluation work threshold** for independently shifted grids; it does not hold automatically for one fixed shift reused across repetitions.

## Assumptions and scope

All variables are real, \(r_k\in(0,1)\), \(N_k,m_k\) are arbitrary positive integers, and the shifts are independent between repeated full-grid evaluations. Each shift is uniform over one grid cell. The near-boundary hypothesis is \(r_k^{N_k}\to1\), stronger than \(r_k\to1\) alone when \(N_k\) grows. The signal being integrated is exactly the normalized circular Poisson kernel; no arbitrary smoothness-class approximation or fixed-integrand uniformity is asserted.

## Proof

**1. Exact aliasing and moments.** The absolutely convergent Fourier expansion
\[
P_r(\theta)=\sum_{n\in\mathbb Z}r^{|n|}e^{in\theta}
\]
shows that averaging over all \(N\)-th roots of unity deletes every Fourier mode except multiples of \(N\). Thus \(Q_{N,r}(\Theta)=P_q(N\Theta)\), with \(q=r^N\). For a uniform shift, \(U=N\Theta\pmod{2\pi}\) is uniform on the circle. Orthogonality of Fourier modes therefore yields
\[
\mathbb E P_q(U)=1,\qquad
\mathbb E P_q(U)^2=1+2\sum_{n\ge1}q^{2n}=\frac{1+q^2}{1-q^2}.
\]
Independence of the \(m\) shifts gives the variance formula. In particular \(\varepsilon\operatorname{Var}(P_{1-\varepsilon}(U))\to1\).

**2. Vanishing effective budget.** Let \(q=1-\varepsilon\), and identify \(U\) with a uniform point in \([-\pi,\pi]\). For fixed \(K>0\), the event that any of the \(m\) sample angles satisfies \(|U_j|\le K\varepsilon\) has probability at most \(mK\varepsilon/\pi\), which tends to zero if \(m\varepsilon\to0\). Outside that small arc, the expected average is
\[
\frac1{2\pi}\int_{|u|>K\varepsilon} P_{1-\varepsilon}(u)\,du
\longrightarrow 1-\frac2\pi\arctan K.
\]
The limit follows from the change of variables \(u=\varepsilon x\), since
\[
\varepsilon P_{1-\varepsilon}(\varepsilon x)\to\frac2{1+x^2}
\]
with a uniform integrable bound \(C/(1+x^2)\) over \(|x|\le\pi/\varepsilon\). The probability of any exceptional core hit tends to zero; Markov's inequality on the nonnegative outer-arc contribution bounds its chance of exceeding a fixed positive threshold by a multiple of \(1-2\arctan K/\pi\). Letting \(K\to\infty\) proves \(A_k\to0\) in probability. The variance diverges by the exact formula.

**3. Critical Poisson limit.** Suppose \(m\varepsilon\to\lambda\in(0,\infty)\), so necessarily \(m\to\infty\). For \(t\ge0\), independence gives the exact Laplace transform
\[
\mathbb E e^{-tA_k}=(1-B_k(t))^{m},\qquad
B_k(t)=\frac1{2\pi}\int_{-\pi}^{\pi}
\left(1-e^{-tP_{1-\varepsilon}(u)/m}\right)du.
\]
Because \(1-e^{-z}\le z\) and \(\mathbb E P_q(U)=1\), \(0\le B_k(t)\le t/m\), so \(m\log(1-B_k)=-mB_k+o(1)\). Under \(u=\varepsilon x\),
\[
mB_k(t)=\frac{m\varepsilon}{2\pi}
\int_{-\pi/\varepsilon}^{\pi/\varepsilon}
\left(1-\exp\left[-\frac{t}{m\varepsilon}\,
\varepsilon P_{1-\varepsilon}(\varepsilon x)\right]\right)dx.
\]
Using \(m\varepsilon\to\lambda\) and the integrable bound from Step 2, dominated convergence identifies the stated Laplace exponent. By the Laplace functional of a homogeneous Poisson point process, this is exactly the transform of \(S_\lambda\), proving weak convergence. The Poisson integral is almost surely finite because \(\int_{\mathbb R}(1+x^2)^{-1}dx=\pi\). Campbell's first and second moment formulas, using \(\int_{\mathbb R}(1+x^2)^{-2}dx=\pi/2\), give expectation one and variance \(1/\lambda>0\).

**4. Many-shift limit and normal fluctuations.** If \(m\varepsilon\to\infty\), the exact variance implies \(\mathbb E(A_k-1)^2\sim 1/(m\varepsilon)\to0\). To prove the central limit theorem, write
\[
\sqrt{m\varepsilon}(A_k-1)
=\sum_{j=1}^{m}\sqrt{\frac\varepsilon m}
\left(P_{1-\varepsilon}(U_j)-1\right).
\]
Its total variance is \(\varepsilon\operatorname{Var}(P_{1-\varepsilon}(U))\to1\), while its largest possible summand magnitude is at most \(C/\sqrt{m\varepsilon}\to0\), since \(P_{1-\varepsilon}(u)\le(2-\varepsilon)/\varepsilon\). The Lindeberg condition holds, and the triangular-array central limit theorem applies.

**5. Necessity.** If \(m_k\varepsilon_k\) does not tend to infinity, it has a subsequence with a finite limit in \([0,\infty)\). By Step 2 or Step 3, that subsequence converges weakly to either the point mass at zero or the nondegenerate \(S_\lambda\), not to the point mass at one. Hence the original sequence cannot converge in probability to one. Mean-square consistency implies convergence in probability and the exact variance gives the reverse implication. Finally, \(q_k=r_k^{N_k}\to1\) gives \(N_k(-\log r_k)=-\log q_k\to0\) and the standard exponential and logarithmic first-order expansions yield \(1-q_k\sim N_k(1-r_k)\).

## Verification

Run `python3 VERIFIER.py` from the directory containing the two standalone files. The pure-standard-library verifier evaluates discrete Fourier aliasing on multiple grids; independently integrates the Poisson kernel's first two moments; checks single-shift quantiles, critical-window Laplace transforms, variance asymptotics, and seeded repeated-shift experiments. It passed 475 assertions. Such finite checks do not establish the limiting theorems; their proofs are Steps 1–5.

For an explicit triangular-array benchmark, take \(N_k=k\), \(r_k=\exp(-1/k^2)\). Then \(r_k^{N_k}=\exp(-1/k)\) and \(1-r_k^{N_k}\sim1/k\). Choosing respectively \(m_k=\lfloor\sqrt k\rfloor\), \(m_k=k\), and \(m_k=k^2\) produces the collapsed, Poisson, and Gaussian regimes.

## Relationship to prior work

Goda, Kazashi, and Suzuki established randomized trapezoidal quadrature bounds for fixed Gaussian-weighted Sobolev function classes; their randomization is an established ingredient, not claimed here. Trefethen and Weideman surveyed the classical Fourier-aliasing analysis of trapezoidal quadrature; the identity in Step 1 is also not claimed as new. Bao, Hua, Lai, and Zhang, and af Klinteberg, developed deterministic accuracy-restoration methods for nearly singular periodic quadrature. The finding instead concerns **independently shifted repeated quadrature on a family whose singularity moves toward the integration contour**, with a sharp joint boundary-distance/evaluation-count criterion and a non-Gaussian critical distribution.

## Limitations

This result applies to exactly one Poisson-kernel near-boundary family and independent uniform re-randomization of full grids. It does not imply a worst-case bound over arbitrary near-singular integrands, compare runtime or variance of singularity subtraction, or replace established analyses for fixed Sobolev-norm integrands. Critical distribution identification uses standard Poisson-process convergence principles, which are not claimed as new abstract probability theory. An equivalent special-case statement may exist in less-indexed numerical or point-process literature; publication priority is not independently established. Finite tests are illustrations, not an exhaustive or mechanized proof.

## References

1. T. Goda, Y. Kazashi, and Y. Suzuki, *Randomizing the trapezoidal rule gives the optimal RMSE rate in Gaussian Sobolev spaces*, arXiv:2212.11476v1 (2022-12-22), https://arxiv.org/abs/2212.11476.
2. A. Bao, L. Hua, J. Lai, and J. Zhang, *Singularity swapping method for nearly singular integrals based on trapezoidal rule*, arXiv:2305.05855 (2023), https://arxiv.org/abs/2305.05855.
3. L. af Klinteberg, *Singularity swap quadrature for nearly singular line integrals on closed curves in two dimensions*, arXiv:2304.11865 (2023), https://arxiv.org/abs/2304.11865.
4. L. N. Trefethen and J. A. C. Weideman, *The Exponentially Convergent Trapezoidal Rule*, SIAM Review 56 (2014), DOI 10.1137/130932132.
