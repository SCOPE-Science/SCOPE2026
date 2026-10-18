# A logarithmic limit law for integrals of normalized partition polynomials

## Finding
For each integer \(n\ge 1\), choose an ordinary integer partition \(\Lambda_n\) of \(n\) uniformly from all \(p(n)\) possibilities. Let \(m_j=m_j(\Lambda_n)\) count its parts of size \(j\), and \(L_n=\sum_{j\ge1}m_j\). Define the normalized partition polynomial and its integral by
\[
 \widehat f_{\Lambda_n}(x)=L_n^{-1}\sum_{j\ge1}m_jx^j,
 \qquad I_n=\int_0^1\widehat f_{\Lambda_n}(x)\,dx
 =\frac{\sum_{j\ge1}m_j/(j+1)}{L_n}.
\]
Then, with natural logarithms and convergence in distribution,
\[
 (\log n)I_n\ \xrightarrow{\mathrm d}\ Z
 :=2\sum_{j=1}^{\infty}\frac{E_j}{j(j+1)},
\]
where the \(E_j\) are independent exponential random variables of rate one. The sum converges almost surely and in \(L^1\). The limit is nondegenerate, with
\[
 \mathbb E Z=2,\qquad
 \operatorname{Var}(Z)=\frac{4\pi^2}{3}-12>0.
\]
Its Laplace transform, for every real \(t\ge0\), is the convergent product
\[
 \mathbb E e^{-tZ}=\prod_{j=1}^{\infty}
 \left(1+\frac{2t}{j(j+1)}\right)^{-1}
 =\Gamma\!\left(\frac{3+\sqrt{1-8t}}2\right)
 \Gamma\!\left(\frac{3-\sqrt{1-8t}}2\right).
\]
For \(t>1/8\), the square roots on the right are complex conjugates, and their Gamma factors give the indicated positive real product. In particular \(I_n\to0\) in probability, but its natural logarithmic rescaling has a nonconstant limit law.

## Assumptions and scope
A partition is a nonincreasing finite sequence of positive integers with sum \(n\); multiplicities are unrestricted. The probability is uniform on partitions of exactly \(n\), **not** on compositions, partitions of varying sizes, or Plancherel-weighted partitions. Natural logarithms are essential to the constants. No assertion of convergence of the finite-\(n\) means or variances of \((\log n)I_n\) is needed. The result does not prove monotonicity of fixed-length averages.

## Proof
Set \(c=\pi/\sqrt6\) and \(K=2c\), and let \(p(0)=1\). Two classical inputs are used with their precise consequences: the Hardy--Ramanujan asymptotic
\[
 p(v)=\frac{e^{K\sqrt v}}{4\sqrt3\,v}\bigl(1+O(v^{-1/2})\bigr)
 \qquad(v\to\infty),
\]
and the Erdős--Lehner theorem for the largest part of a uniformly sampled partition (equivalently, by conjugation, its number \(L_n\) of parts):
\[
 \frac{cL_n}{\sqrt n}-\log\!\left(\frac{\sqrt n}{c}\right)
 \xrightarrow{\mathrm d}G,
\]
where \(G\) has the standard Gumbel law. The latter implies
\[
 \frac{L_n}{\sqrt n\log n}\ \xrightarrow{\mathbb P}\ \frac1{2c}.
\tag{1}
\]

**Step 1: exact finite-dimensional tail identity.** For distinct fixed positive integers \(j_1,\ldots,j_d\) and nonnegative integers \(r_1,\ldots,r_d\), removing \(r_i\) copies of each part \(j_i\) gives a bijection from partitions with \(m_{j_i}\ge r_i\) to partitions of \(n-s\), where \(s=\sum_i j_i r_i\). Thus
\[
 \mathbb P\{m_{j_i}\ge r_i\text{ for every }i\}
 =\frac{p(n-s)}{p(n)}\quad(0\le s\le n),
\tag{2}
\]
with probability zero if \(s>n\). For fixed \(x_i\ge0\), take \(r_i=\lceil x_i\sqrt n\rceil\). Then \(s=\sqrt n\sum_i j_ix_i+O(1)\), so the Hardy--Ramanujan formula gives
\[
 \frac{p(n-s)}{p(n)}\longrightarrow
 e^{-c\sum_i j_ix_i}.
\]
These are exactly the joint survival probabilities of independent exponentials of respective rates \(cj_i\). Continuity of the limiting joint distribution yields
\[
 (m_1,\ldots,m_d)/\sqrt n
 \xrightarrow{\mathrm d}
 (E_1/c,\ldots,E_d/(cd)).
\tag{3}
\]
The \(x_i=0\) boundary is compatible with (2), and the use of ceilings instead of floors has no effect on the limit.

**Step 2: a uniform tail bound for the weighted part sum.** The partition asymptotic, with finitely many small arguments absorbed into constants, implies the existence of constants \(C,\delta>0\), independent of \(n\ge1\) and \(0\le s\le n\), such that
\[
 \frac{p(n-s)}{p(n)}\le C\exp(-\delta s/\sqrt n).
\tag{4}
\]
To verify this explicitly, the asymptotic gives upper and lower constant multiples of \(e^{K\sqrt v}/(v+1)\) for every \(v\ge0\). Their ratio is bounded by
\[
 C_0\frac{n+1}{n-s+1}
 \exp\{-K(\sqrt n-\sqrt{n-s})\}.
\]
For \(s\le n/2\), the prefactor is at most two and \(\sqrt n-\sqrt{n-s}\ge s/(2\sqrt n)\). For \(s>n/2\), the prefactor is at most \(n+1\), while \(\sqrt n-\sqrt{n-s}\ge(1-1/\sqrt2)\sqrt n\); an exponential in \(\sqrt n\) absorbs the linear prefactor. Therefore (4) holds, for example with a sufficiently enlarged \(C\) and \(\delta=K/8\).

Define
\[
 A_n=\frac1{\sqrt n}\sum_{j\ge1}\frac{m_j}{j+1}.
\]
The tail-sum formula for a nonnegative integer random variable and (2)--(4) give, for every \(J\ge1\),
\[
 \begin{aligned}
 \mathbb E\left[\frac1{\sqrt n}\sum_{j>J}\frac{m_j}{j+1}\right]
 &=\frac1{\sqrt n}\sum_{j>J}\frac1{j+1}
  \sum_{r\ge1:jr\le n}\frac{p(n-jr)}{p(n)}\\
 &\le\frac C{\sqrt n}\sum_{j>J}\frac1{j+1}
  \sum_{r\ge1}e^{-\delta jr/\sqrt n}\\
 &\le\frac C\delta\sum_{j>J}\frac1{j(j+1)}
 =\frac C{\delta(J+1)}.
 \end{aligned}
\tag{5}
\]
Here the penultimate inequality uses \((e^u-1)^{-1}\le u^{-1}\) for \(u>0\). The bound is uniform in \(n\).

For fixed \(J\), (3) implies
\[
 \frac1{\sqrt n}\sum_{j=1}^{J}\frac{m_j}{j+1}
 \xrightarrow{\mathrm d}\frac1c\sum_{j=1}^{J}\frac{E_j}{j(j+1)}.
\]
The expected tail of the right-hand infinite series equals \(1/[c(J+1)]\). With (5), truncation and the converging-together theorem therefore give
\[
 A_n\xrightarrow{\mathrm d}
 A:=\frac1c\sum_{j\ge1}\frac{E_j}{j(j+1)}.
\tag{6}
\]
This step provides the uniform control absent from merely knowing the limits of finitely many multiplicities.

**Step 3: normalize and identify the law.** Since
\[
 (\log n)I_n
 =\frac{A_n}{L_n/(\sqrt n\log n)},
\]
equations (1) and (6), together with Slutsky's theorem, give the claimed limit \(Z=2cA\). Because \(\sum_{j\ge1}1/[j(j+1)]=1\), its mean equals \(2\). Independence and
\[
 \sum_{j\ge1}\frac1{j^2(j+1)^2}=2\zeta(2)-3
\]
give variance \(4(2\zeta(2)-3)=4\pi^2/3-12\). Independence also yields the Laplace product. Put \(\alpha+\beta=1\) and \(\alpha\beta=2t\); the finite gamma identity
\[
 \prod_{j=1}^{N}\frac{j(j+1)}{(j+\alpha)(j+\beta)}
 =\frac{\Gamma(N+1)\Gamma(N+2)\Gamma(1+\alpha)\Gamma(1+\beta)}
 {\Gamma(N+1+\alpha)\Gamma(N+1+\beta)}
\]
has prefactor tending to one by the Gamma ratio asymptotic, establishing the closed form. Finally, tightness of \((\log n)I_n\) and \(\log n\to\infty\) imply \(I_n\to0\) in probability.

## Verification
The accompanying standalone file `verify.py` checks, by exact enumeration of every integer partition through \(n=18\), the bijection identity (2) for all \(r_1,r_2,r_3\in\{0,1,2\}\) and verifies a separate marked-part expectation identity. It also computes weighted-part expectations from exact partition numbers through \(n=1200\) and compares partial Laplace products with the Gamma expression for four values of \(t\). The script uses no external dependencies. Invoke `python verify.py`. Finite computations do not establish either Hardy--Ramanujan or Erdős--Lehner and are not substituted for steps (1)--(6).

## Relationship to prior work
Dawsey, Russell, and Urban introduced these normalized partition polynomials, proved that their integrals are dense in \([0,1/2]\), and formulated a fixed-length-average monotonicity conjecture; their treatment does not formulate the logarithmically rescaled random-integral law above. The Hardy--Ramanujan asymptotic, the Erdős--Lehner length theorem, and Fristedt's limits for small-part multiplicities are prior foundational inputs, not claimed here as discoveries. The new, specifically identified claim concerns the random normalized *integral*, its infinite weighted-exponential distribution and explicit Gamma transform; the proof supplies a uniform weighted-tail estimate (5). It is not a solution of the fixed-length monotonicity conjecture.

## Limitations
The conclusion is weak convergence only; it does not assert almost-sure convergence of \((\log n)I_n\) on a coupled sequence of partitions, nor convergence of all its finite-sample moments. The argument uses classical partition asymptotics and the Erdős--Lehner theorem rather than proving them from scratch. Because broad probabilistic partition limit theorems exist, an implicit result or an unindexed specialization could overlap; no independent priority or independent audit is claimed.

## References
1. M. Locus Dawsey, T. Russell, D. Urban, *Derivatives and Integrals of Polynomials Associated with Integer Partitions*, arXiv:2108.00943, first submitted 2021-08-02; Journal of Integer Sequences 25 (2022), Article 22.5.1. https://arxiv.org/abs/2108.00943
2. G. H. Hardy and S. Ramanujan, *Asymptotic formulæ in combinatory analysis*, Proceedings of the London Mathematical Society (1918). https://doi.org/10.1112/plms/s2-17.1.75
3. P. Erdős and J. Lehner, *The distribution of the number of summands in the partitions of a positive integer*, Duke Mathematical Journal 8 (1941), 335–345. https://doi.org/10.1215/S0012-7094-41-00826-8
4. B. Fristedt, *The structure of random partitions of large integers*, Transactions of the American Mathematical Society 337 (1993), 703–735. https://doi.org/10.1090/S0002-9947-1993-1094553-1
5. H. T. Ngo and R. C. Rhoades, *Integer partitions, probabilities and quantum modular forms*, Research in the Mathematical Sciences (2017), open full text. https://doi.org/10.1186/s40687-017-0102-4
