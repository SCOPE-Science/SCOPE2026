# Arithmetic norm-convergence rates for quasiperiodic Aluthge weighted shifts

## Finding
Let \(\Delta(T)=|T|^{1/2}U|T|^{1/2}\), where \(T=U|T|\) is the polar decomposition. Fix irrational \(\theta\in\mathbb R\setminus\mathbb Q\) and a real continuous mean-zero function \(g\) on the circle \(\mathbb T=\mathbb R/\mathbb Z\). On \(\ell^2(\mathbb N_0)\) define the positive unilateral weighted shift
\[
W_{\theta,g}e_n=e^{g(n\theta)}e_{n+1},\qquad n\ge0,
\]
and denote the usual unweighted shift by \(S\). Then \(\Delta^k(W_{\theta,g})\to S\) in **operator norm**.

For a natural fixed analytic observable, the centered Poisson kernel
\[
g_\rho(x)=2\sum_{m=1}^\infty e^{-\rho m}\cos(2\pi mx)
=\frac{1-e^{-2\rho}}{1-2e^{-\rho}\cos(2\pi x)+e^{-2\rho}}-1,
\qquad \rho>0,
\]
write \(E_k(\theta,\rho)=\|\Delta^k(W_{\theta,g_\rho})-S\|\), and \(M_\rho=2/(e^\rho-1)\). For **every** irrational \(\theta\) and integer \(k\ge64\),
\[
\boxed{E_k(\theta,\rho)\ge
 \exp\!\bigl[-M_\rho-(\rho+10)k^{1/3}\bigr].}
\]
If \(\theta\) is badly approximable, meaning \(c_\theta=\inf_{m\ge1}m\|m\theta\|_{\mathbb R/\mathbb Z}>0\), then
\[
\boxed{e^{-C_{\theta,\rho}k^{1/3}}\le E_k(\theta,\rho)
\le C'_{\theta,\rho}e^{-c'_{\theta,\rho}k^{1/3}}}
\]
for all sufficiently large integers \(k\), with positive constants. Hence the stretched-exponential **exponent \(1/3\) is sharp** for these Poisson-profiled shifts. More generally, the upper estimate applies to any mean-zero real analytic \(g\) with \(|\widehat g(m)|\le C e^{-\rho|m|}\), at every badly approximable \(\theta\).

At the opposite arithmetic extreme, for **each** positive sequence \(\varepsilon_k\to0\), there exist a Liouville irrational \(\theta\), a nonzero mean-zero real-analytic \(g\) extending holomorphically to \(|\operatorname{Im}z|<1/(4\pi)\), and integers \(k_j\to\infty\) such that
\[
\boxed{\|\Delta^{k_j}(W_{\theta,g})-S\|\ge\varepsilon_{k_j}.}
\]
Thus convergence persists throughout this quasiperiodic class, but no universal quantitative rate survives even with analytic logarithmic weights when the rotation is allowed to be Liouville.

## Assumptions and scope
All operators act on the complex Hilbert space \(\ell^2(\mathbb N_0)\). Every weight is strictly positive and lies between \(e^{-\|g\|_\infty}\) and \(e^{\|g\|_\infty}\); thus all shifts and Aluthge iterates are bounded, injective, and noncompact. The Aluthge transform is the standard \(1/2\)-transform. Write \(\|t\|_{\mathbb R/\mathbb Z}=\min_{j\in\mathbb Z}|t-j|\). The rate constants in the bounded-type result depend on the fixed rotation and observable. The slow-rate construction allows both the rotation and observable to depend on the prescribed sequence.

## Proof
**1. Exact logarithmic iteration and norm formula.** For a positive weighted shift \(We_n=w_ne_{n+1}\), the polar partial isometry is \(S\) and \(|W|e_n=w_ne_n\). Consequently
\[
\Delta(W)e_n=\sqrt{w_nw_{n+1}}\,e_{n+1}.
\]
Define \(R_\theta h(x)=h(x+\theta)\) and \(B_\theta=(I+R_\theta)/2\). Induction gives, without approximation,
\[
\Delta^k(W_{\theta,g})e_n
=\exp((B_\theta^kg)(n\theta))e_{n+1},
\quad
B_\theta^kg(x)=2^{-k}\sum_{j=0}^k\binom{k}{j}g(x+j\theta).
\]
Because \(\{n\theta:n\ge0\}\) is dense in \(\mathbb T\),
\[
\|\Delta^k(W_{\theta,g})-S\|
=\max_{x\in\mathbb T}|e^{B_\theta^kg(x)}-1|.
\tag{1}
\]
Set \(M=\|g\|_\infty\). Since \(\|B_\theta^kg\|_\infty\le M\), the real mean-value theorem gives the two-sided comparison
\[
e^{-M}\|B_\theta^kg\|_\infty\le
\|\Delta^k(W_{\theta,g})-S\|
\le e^M\|B_\theta^kg\|_\infty.
\tag{2}
\]
For \(m\in\mathbb Z\), the Fourier multiplier of \(B_\theta\) is
\[
\lambda_m=\frac{1+e^{2\pi im\theta}}2,
\qquad |\lambda_m|=|\cos(\pi m\theta)|.
\tag{3}
\]
For irrational \(\theta\), \(|\lambda_m|<1\) whenever \(m\ne0\). The zero Fourier mode of \(g\) vanishes. Finite trigonometric polynomial approximation and \(\|B_\theta\|_{C(\mathbb T)\to C(\mathbb T)}\le1\) imply \(\|B_\theta^kg\|_\infty\to0\), proving the stated operator-norm convergence for every continuous mean-zero observable.

**2. Upper bound under bounded type.** Let \(\theta\) be badly approximable and let \(|\widehat g(m)|\le C e^{-\rho|m|}\). Elementary calculus shows for \(\delta\in[0,1/2]\) that \(|\cos(\pi\delta)|\le e^{-2\delta^2}\). Since \(\|m\theta\|_{\mathbb R/\mathbb Z}\ge c_\theta/|m|\), (3) gives
\[
|\lambda_m|^k\le \exp(-2c_\theta^2k/m^2).
\]
Write \(u=k^{1/3}\). Split the absolutely convergent Fourier sum at \(m=u\). For \(1\le m\le u\), the multiplier is at most \(e^{-2c_\theta^2u}\), while the coefficient tail \(m>u\) is at most a constant times \(e^{-\rho u}\). Thus
\[
\|B_\theta^kg\|_\infty
\le \frac{2C}{1-e^{-\rho}}\Bigl(e^{-\rho}e^{-2c_\theta^2u}+e^{-\rho u}\Bigr).
\tag{4}
\]
Equations (2) and (4) yield the asserted upper \(e^{-c'k^{1/3}}\) rate. For \(g=g_\rho\), take \(C=1\).

**3. Universal lower bound for the Poisson observable.** Let \(q_j\) be the increasing denominators of the continued-fraction convergents of an arbitrary irrational \(\theta\), including \(q_0=1\). Given \(k\ge64\), put \(u=k^{1/3}\) and select \(j\) with \(q_j\le u<q_{j+1}\). The convergent inequality gives
\[
\delta_j=\|q_j\theta\|_{\mathbb R/\mathbb Z}
<1/q_{j+1}<1/u\le1/4.
\]
For \(0\le\delta\le1/4\), Taylor's formula and \((\log\cos(\pi\delta))''=-\pi^2\sec^2(\pi\delta)\ge-2\pi^2\) give
\[
\log\cos(\pi\delta)\ge-\pi^2\delta^2\ge-10\delta^2.
\]
The \(q_j\)-th Fourier coefficient of \(B_\theta^kg_\rho\) has modulus
\[
e^{-\rho q_j}|\cos(\pi q_j\theta)|^k
\ge\exp[-\rho u-10k/u^2]
=\exp[-(\rho+10)u].
\]
A Fourier coefficient cannot exceed the \(L^\infty\) norm. Since \(\|g_\rho\|_\infty=M_\rho\), (2) proves the universal lower bound. This also proves that the exponent \(1/3\) in the bounded-type upper estimate cannot be replaced by any larger stretched-exponential exponent for this fixed Poisson observable.

**4. Analytic arbitrarily slow convergence at Liouville rotations.** Let \(\varepsilon_k>0\) tend to zero. Construct positive integers \(q_1=10,q_2,\ldots\) and increasing integers \(k_1,k_2,\ldots\) recursively. After \(q_j\) is chosen, take \(k_j>k_{j-1}\) so large that \(\varepsilon_{k_j}\le e^{-q_j}/4\), then choose an integer multiple \(q_{j+1}\) of \(q_j\) satisfying
\[
q_{j+1}\ge\max\{q_j^{j+4},\;100q_j\sqrt{k_j}\}.
\tag{5}
\]
Let
\[
\theta=\sum_{j=1}^\infty\frac1{q_j},\qquad
 g(x)=2\sum_{j=1}^\infty e^{-q_j}\cos(2\pi q_jx).
\]
The finite partial sums of \(\theta\) are rationals with denominator \(q_j\), and their positive errors are at most \(2/q_{j+1}\le2/q_j^{j+4}\). Hence \(\theta\) is irrational and Liouville. The series for \(g\) is real and mean zero, is not identically zero, and converges normally in each closed strip of width smaller than \(1/(2\pi)\). In particular it is holomorphic in the specified strip. Further,
\[
\|g\|_\infty\le2\sum_{m\ge10}e^{-m}<1.
\]
From (5),
\[
\|q_j\theta\|_{\mathbb R/\mathbb Z}
\le2q_j/q_{j+1}\le1/(50\sqrt{k_j}).
\]
The \(q_j\)-th Fourier coefficient of \(B_\theta^{k_j}g\) has modulus at least \(e^{-q_j}e^{-10/2500}\). Applying (2) and \(\|g\|_\infty<1\),
\[
\|\Delta^{k_j}(W_{\theta,g})-S\|
\ge e^{-1-10/2500}e^{-q_j}>\frac14e^{-q_j}\ge\varepsilon_{k_j}.
\]
Part 1 still gives operator-norm convergence, so no contradiction arises. This establishes the arbitrarily slow subsequential convergence with an analytic noncompact weighted shift.

## Verification
A standalone standard-library Python program `verify.py` recomputes the binomial/Fourier identities for finite truncations, the norm comparison at sample points, the continued-fraction resonance inequality at selected large iterations, and a finite near-resonant example. It reports 428 successful supplementary checks. The infinite-dimensional convergence, exact rate exponent, and Liouville construction are proven analytically above; finite tests are not used as substitutes for those proofs.

For reproduction, run `python verify.py` from the directory containing the extracted files. The primary equations to inspect independently are (1)--(5), especially the exact shift-polar calculation, continued-fraction selection, and construction (5).

## Relationship to prior work
Lahiri, Ojha and Birbonshi (2026, arXiv:2604.27762v1) study Aluthge iterates of particular composition operators on weighted Bergman and Hardy spaces and obtain strong-operator convergence in their families. Their explicit setting is different from analytic quasiperiodic unilateral weighted shifts, and their inspected computations and final questions do not yield the sharp rotation-arithmetic norm rates stated here.

Rion (Houston Journal of Mathematics 42 (2016), 1217--1226) supplies an earlier qualitative classification of strong-operator limits of Aluthge iterates of weighted shifts bounded away from zero; that qualitative convergence machinery and the elementary binomial averaging identity are not represented as novel. Only the journal abstract and table-of-contents description were accessible for this particularly close source: the full text could contain further quantitative statements, so publication-priority uncertainty remains.

Bala (2026, arXiv:2602.07916v1) treats iterates of compact operators; the present shifts are never compact. Tong and Li (2022, arXiv:2205.09496v1) study weighted Birkhoff averages with fixed smooth window weights \(w(j/N)\); their formula (2.6) uses weights different from the iteration-forced binomial kernel \(2^{-k}\binom{k}{j}\), and their accelerated convergence theorems do not supply the universal Poisson lower barrier or the slow analytic Aluthge construction. Classical Fourier multipliers and continued fractions are explicitly part of the proof input.

## Limitations
The two-sided stretched-exponential law is in the exponent sense, not an exact leading constant. The lower rate bound uses the centered Poisson observable specifically, whereas the upper rate extends to a general analytic observable. The arbitrary-slow statement concerns an infinite subsequence and allows rotation and observable to depend on the rate; it does not claim slow convergence for every prescribed rotation. Potential unlocated equivalent formulations in older weighted-shift, summability, and quasiperiodic averaging literature remain a priority risk, heightened by the inaccessible full text of the 2016 weighted-shift article. No independent scientific validation has been performed.

## References
1. S. Lahiri, S. Ojha, R. Birbonshi, *Iterated Aluthge transforms of some composition operators on weighted Bergman spaces*, arXiv:2604.27762v1 (first submitted 2026-04-30), https://arxiv.org/abs/2604.27762.
2. K. Rion, *Convergence Properties of the Aluthge Sequence of Weighted Shifts*, Houston Journal of Mathematics **42** (2016), 1217--1226; publisher issue index https://www.math.uh.edu/~hjm/Vol42-4.html.
3. N. Bala, *The iterated Aluthge transforms of compact operators*, arXiv:2602.07916v1 (2026), https://arxiv.org/abs/2602.07916.
4. Z. Tong and Y. Li, *Exponential convergence of weighted Birkhoff average*, arXiv:2205.09496v1 (2022), https://arxiv.org/abs/2205.09496.
