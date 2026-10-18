# Exact finite-time analytic correlation norms for metallic cat maps

## Finding
For every integer \(s\ge1\), let
\[
M_s=\begin{pmatrix}s&1\\1&0\end{pmatrix},\qquad
A_s=M_s^2=\begin{pmatrix}s^2+1&s\\s&1\end{pmatrix},\qquad
T_s(x)=A_sx\pmod{\mathbb Z^2}.
\]
For \(0<\theta<1\), give zero-mean analytic Fourier series the Hilbert norm
\[
\|f\|_\theta^2=\sum_{k\in\mathbb Z^2\setminus\{0\}}|\widehat f(k)|^2\theta^{-2\|k\|_1},\qquad
\|k\|_1=|k_1|+|k_2|.
\]
Set
\[
\mathscr C_n(s,\theta)=\sup_{\substack{\int f=\int g=0\\\|f\|_\theta=\|g\|_\theta=1}}
\left|\int_{\mathbb T^2}f(T_s^nx)\overline{g(x)}\,dx\right|.
\]
Let \(G_0=0\), \(G_1=1\), and \(G_{n+1}=sG_n+G_{n-1}\) for \(n\ge1\).
Then, **for every integer \(n\ge1\)**,
\[
\boxed{\mathscr C_n(s,\theta)=\theta^{\,G_{n+1}+2G_n+G_{n-1}}.}
\]
The four and only four minimizing Fourier input frequencies are
\[
\boxed{k=\pm M_s^{-n}e_1\ \text{or}\ k=\pm M_s^{-n}e_2.}
\]
All norm-maximizing pairs have Fourier support within these frequencies, with matched output indices \(A_s^nk\) and the weighted normalized coefficient vectors aligned. In particular, single characters attain equality. For the standard cat map \(s=1\), the exponent is the Fibonacci number \(F_{n+3}\), with \(F_0=0,F_1=1\).

## Assumptions and scope
The torus carries normalized Haar measure. The functions are complex-valued, zero-mean members of the above isotropically weighted analytic Fourier Hilbert space. The automorphism \(A_s\) is unimodular and hyperbolic for every integer \(s\ge1\). Time \(n\) is a positive integer and \(\theta\) is strictly between zero and one. The correlation is a bilinear form between two separately normalized observables. This is not the supremum of autocorrelations using one common observable; the normalization and the distinction are essential. The claim concerns a Fourier-weighted norm, not the unweighted \(L^2\) norm.

## Proof
**Step 1: Reduce the analytic operator norm to an integer minimum.** Write \(e_k(x)=\exp(2\pi i k\cdot x)\). Since \(A_s\) is symmetric, \(e_k\circ T_s^n=e_{A_s^nk}\). Parseval therefore gives
\[
\int f(T_s^nx)\overline{g(x)}\,dx
=\sum_{k\ne0}\widehat f(k)\overline{\widehat g(A_s^nk)}.
\]
Define \(a_k=\widehat f(k)\theta^{-\|k\|_1}\) and \(b_j=\widehat g(j)\theta^{-\|j\|_1}\). Both normalized vectors have \(\ell^2\) norm one. Because the map \(k\mapsto A_s^nk\) is a bijection of the nonzero integer lattice, the displayed correlation is a weighted permutation pairing, with positive weights \(\theta^{\|k\|_1+\|A_s^nk\|_1}\). Cauchy--Schwarz, followed by testing a single Fourier character, proves exactly
\[
\mathscr C_n(s,\theta)=\theta^{L_n},\quad
L_n=\min_{k\in\mathbb Z^2\setminus\{0\}}
\bigl(\|k\|_1+\|A_s^nk\|_1\bigr).
\]
The minimum exists because the integer cost is positive and coercive.

**Step 2: Factor the hyperbolic iterate at its integer half-time.** Induction on \(n\ge1\) yields
\[
M_s^n=\begin{pmatrix}G_{n+1}&G_n\\G_n&G_{n-1}\end{pmatrix},\qquad
M_s^{-n}=(-1)^n\begin{pmatrix}G_{n-1}&-G_n\\-G_n&G_{n+1}\end{pmatrix}.
\]
Every entry of \(M_s^n\) and every absolute entry of \(M_s^{-n}\) is nonnegative; the relevant row-sums are strictly positive. The determinant of \(M_s\) is \(-1\), so the substitution \(v=M_s^nk\) permutes \(\mathbb Z^2\setminus\{0\}\). It converts the cost into
\[
L_n=\min_{v\ne0}\bigl(\|M_s^{-n}v\|_1+\|M_s^nv\|_1\bigr).
\]
Put \(\alpha=G_{n+1}+G_n\), \(\beta=G_n+G_{n-1}\), and \(t_n=\alpha+\beta\).

**Step 3: A sharp three-case sign inequality.** For \(v=(x,y)\) with \(xy>0\), the two entries of \(M_s^nv\) share a sign, and
\[
\|M_s^nv\|_1=\alpha|x|+\beta|y|\ge t_n.
\]
The other summand is strictly positive, so the total exceeds \(t_n\). For \(xy<0\), the two entries of \(M_s^{-n}v\) have opposite signs, but the absolute value of each entry is a sum of nonnegative terms (the common determinant factor has absolute value one), and
\[
\|M_s^{-n}v\|_1=\beta|x|+\alpha|y|\ge t_n.
\]
Again the other summand is strictly positive, giving a strict excess. If exactly one coordinate is nonzero, the cost equals \(t_n\) times the absolute value of that nonzero integer. Equality therefore holds exactly for \(v=\pm e_1,\pm e_2\), and \(L_n=t_n=G_{n+1}+2G_n+G_{n-1}\).

**Step 4: Characterize all equality cases.** Equality in the pairing bound requires the normalized Fourier input to vanish away from the four minimizing \(k=M_s^{-n}v\). Cauchy--Schwarz equality further requires the normalized Fourier output, reindexed by \(A_s^n\), to be a common complex scalar multiple of the normalized input. These conditions are also sufficient. Choosing just one minimizing \(k\) produces an equality case with \(f=\theta^{\|k\|_1}e_k\) and \(g=\theta^{\|A_s^nk\|_1}e_{A_s^nk}\). The theorem follows.

## Verification
The included standalone `checks.py` uses only exact integer arithmetic. It independently computes \(M_s^n\), \(M_s^{-n}\), the recurrence, and the orbit cost; for integers \(1\le s\le6\), \(1\le n\le7\), and every nonzero \(v\in[-9,9]^2\cap\mathbb Z^2\), it finds precisely the four predicted minimizing values and confirms the matrix identities. The diagnostic suite reports 15,456 successful exact assertions. These finite diagnostics do not prove the universal minimization statement; the proof is the sign argument of Step 3.

For \(s=1\), the exponent sequence begins \(3,5,8,13,21\). For \(s=2\), it begins \(4,10,24,58,140\). With \(\rho_s=(s+\sqrt{s^2+4})/2\), Binet's recurrence formula gives \(t_n\sim c_s\rho_s^n\), where
\[
c_s=\frac{\rho_s+2+\rho_s^{-1}}{\sqrt{s^2+4}}>0.
\]
Thus \(-\log\mathscr C_n=(-\log\theta)t_n\) has an exact leading coefficient as well as the familiar double-exponential timescale.

## Relationship to prior work
Chiem's 2025 preprint investigates Schrödinger cocycles over precisely the \(s=1\) cat automorphism, extending to general hyperbolic integer matrices, and supplies the eligible dated dynamical motivation. Its result concerns Lyapunov positivity, not the norm of the analytic correlation bilinear form. Axenides, Floratos and Nicolis compute smooth-observable correlation decay and entropy-related mixing times of cat-map lattices, but their stated function spaces, norms and conclusions do not give the exact Fourier-weighted finite-time operator norm above. Shchetka's later 2026 preprint uses analytic Fourier spaces and determines the sharp *double-exponential rate*, including for the \(s=2\) map, but its general bound and constructed lower-rate witnesses do not provide the all-time optimal coefficient, integer frequency minimizer set or equality characterization. These earlier and later rates are **not** claimed as new here. The newly assessed contribution is the sharp equality \(\mathscr C_n=\theta^{t_n}\) for the entire integer family and all times, including the complete extremizer support.

## Limitations
The result is specific to the symmetric positive integer family \(M_s^2\), the \(\ell^1\) Fourier exponential norm, and two freely chosen test functions. It does not establish analogous exact constants for every hyperbolic integer matrix, anisotropic/Euclidean weights, nonlinear perturbations, or autocorrelation optimization. The accessible literature comparison does not exclude an earlier equivalent result in older correlation-decay literature; Brini--Siboni's 2001 paper was located but its full text could not be inspected, so bibliographic priority remains provisional. No independent external audit has occurred.

## References
1. N. Chiem, *Uniform positivity of the Lyapunov exponent for \(C^1\) monotone potentials generated by the cat map*, arXiv:2502.18628v1 (first public 2025-02-25); *Ergodic Theory and Dynamical Systems* (2026), DOI 10.1017/etds.2026.10323.
2. M. Axenides, E. Floratos, and S. Nicolis, *Exponential mixing of all orders for Arnol'd cat map lattices*, arXiv:2401.08521v1 (2024), §§3--5.
3. E. Shchetka, *Mixing Rates for Analytic Observables: Toral Endomorphisms and Anosov Blaschke Deformations*, arXiv:2610.19019v1 (first public 2026-10-13), §§2--4, especially §4.5; used for current comparison, not as the eligibility-determining dated source.
4. F. Fannjiang and W. Wołowski, *Noise-induced dissipation in Lebesgue-measure preserving maps on \(d\)-dimensional torus*, arXiv:math/0209231 (2002); related quadratic-frequency optimization, but a different noise-dependent invariant.
5. F. Brini and S. Siboni, *Estimates of correlation decay in auto/endomorphisms of the \(n\)-torus*, *Computers & Mathematics with Applications* (2001), DOI 10.1016/S0898-1221(01)00210-3; full text not obtained for comparison.
