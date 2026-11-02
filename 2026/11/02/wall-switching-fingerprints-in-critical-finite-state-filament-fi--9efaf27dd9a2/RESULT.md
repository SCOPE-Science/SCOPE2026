# Wall-switching fingerprints in critical finite-state filament first passage

## Finding
Consider the capped two-state elongation/shortening chain defined below. The wall-induced growth-to-shortening conversion rate \(\gamma\geq0\) strictly increases the Laplace transform of absorption time at every finite size, for every positive Laplace parameter and either initial internal state. At zero mean drift, different fixed wall rates have a common, explicit reflected-Brownian absorption-time limit, but their Laplace transforms have a *nonzero, exactly computable first-order difference* on the quadratic-time scale.

Fix positive rates \(k_d,k_e,\lambda_+,\lambda_-\) with \(k_d\lambda_-=k_e\lambda_+\). Put
\[
D=\frac{k_e(k_d+\lambda_+)}{\lambda_++\lambda_-},\qquad
\delta_\gamma=\frac1{k_d}\left(1+\frac{\lambda_+}{\lambda_-+\gamma}\right),\qquad
h=\sqrt{\frac{\sigma}{D}}.
\]
For each \(N\ge2\), let \(\tau_{N,\gamma}\) denote the time to absorption from length \(j_N\) with either initial internal state. If \(j_N/N\to x\in(0,1]\), then for every \(\sigma>0\),
\[
\lim_{N\to\infty}\mathbb E_\gamma\!\left[e^{-\sigma\tau_{N,\gamma}/N^2}\right]
=\frac{\cosh(h(1-x))}{\cosh h}.
\tag{1}
\]
For any two fixed wall rates \(\gamma_1,\gamma_2\ge0\), with the same initial state and length sequence,
\[
\boxed{\lim_{N\to\infty}N\left(\mathbb E_{\gamma_1}e^{-\sigma\tau_{N,\gamma_1}/N^2}-\mathbb E_{\gamma_2}e^{-\sigma\tau_{N,\gamma_2}/N^2}\right)
=-\sigma(\delta_{\gamma_1}-\delta_{\gamma_2})\frac{\sinh(hx)}{h\cosh^2h}.}
\tag{2}
\]
The limits hold for both initially elongating and initially shortening filaments. The first expression is the Laplace transform of the first hit of zero by a diffusion of generator \(D\partial_x^2\), reflected at one. For \(\gamma_1\ne\gamma_2\), the right-hand side of (2) is nonzero for every \(\sigma>0\) and \(x>0\).

There is also an *exact, nonasymptotic* difference of mean lifetimes. From the shortening state at length \(j\),
\[
\mathbb E_\gamma\tau_{N,\gamma}
=\delta_\gamma j+\frac{Nj-j(j+1)/2}{D};
\tag{3}
\]
from the elongating state it is \(((k_d+\lambda_+)m_j-k_dm_{j-1}-1)/\lambda_+\), with \(m_j\) the right side of (3) and \(m_0=0\). Thus the difference between wall prescriptions is exactly \((\delta_{\gamma_1}-\delta_{\gamma_2})j\) in the shortening state and \((\delta_{\gamma_1}-\delta_{\gamma_2})(j+k_d/\lambda_+)\) in the elongating state. A change of microscopic wall chemistry can therefore alter the mean lifetime by order \(N\) while leaving its leading order-\(N^2\) behavior unchanged.

## Assumptions and scope
The Markov chain has length \(j\in\{1,\ldots,N\}\) and internal state \(i\) (shortening) or \(a\) (elongating). For \(j\ge2\), state \(i\) loses one unit of length at rate \(k_d\); from \(j=1\), this event absorbs at zero. It changes to state \(a\) at rate \(\lambda_+\). State \(a\) grows by one unit at rate \(k_e\) for \(j<N\), and changes to \(i\) at rate \(\lambda_-\). At the cap \(j=N\), growth is suppressed and the \(a\to i\) rate is \(\lambda_-+\gamma\). All rates are constant and independent of length, and are positive except that \(\gamma\) may vanish. The original cap rule corresponds to \(\gamma=k_e\); \(\gamma=0\) is a blocked-growth, no-extra-conversion cap.

The zero-drift condition \(k_d\lambda_-=k_e\lambda_+\) is needed for (1)–(3), but *not* for the strict finite-size Laplace ordering in \(\gamma\). No stochastic-pathwise order is asserted. The diffusion limit keeps the kinetic rates and wall rates fixed while the maximal length \(N\) diverges; it is not a fast-switching or continuum-ballistic limit.

## Proof
For \(s>0\), write \(f_j=\mathbb E_{(j,i)}e^{-s\tau}\) and \(g_j=\mathbb E_{(j,a)}e^{-s\tau}\). Finite-state absorption is almost sure, and first-step equations give
\[
(s+k_d+\lambda_+)f_j=k_df_{j-1}+\lambda_+g_j,\qquad f_0=1,
\]
\[
(s+k_e+\lambda_-)g_j=k_eg_{j+1}+\lambda_-f_j\quad(j<N),
\qquad (s+\lambda_-+\gamma)g_N=(\lambda_-+\gamma)f_N.
\]
Eliminating \(g_j\) yields
\[
A_sf_{j+1}-B_sf_j+C_sf_{j-1}=0\quad(1\le j<N),
\]
where
\[
A_s=k_e(s+k_d+\lambda_+),\quad C_s=k_d(s+k_e+\lambda_-),
\]
\[
B_s=k_ek_d+(s+k_e+\lambda_-)(s+k_d+\lambda_+)-\lambda_-\lambda_+.
\]
The cap becomes \(f_{N-1}=b_\gamma(s)f_N\), with
\[
b_\gamma(s)=1+\frac{s}{k_d}\left(1+\frac{\lambda_+}{s+\lambda_-+\gamma}\right).
\]
Since \(B_s-A_s-C_s=s(s+\lambda_++\lambda_-)>0\), the two characteristic roots \(z_-(s),z_+(s)\) of \(A_sz^2-B_sz+C_s=0\) are real, positive, and satisfy \(0<z_-<1<z_+\). Set
\[
E_\pm=z_\pm^{N-1}(1-b_\gamma z_\pm).
\]
Uniqueness of the finite transient resolvent gives \(E_--E_+\ne0\), and the exact solution is
\[
f_j=\frac{E_-z_+^j-E_+z_-^j}{E_--E_+},\qquad
g_j=\frac{(s+k_d+\lambda_+)f_j-k_df_{j-1}}{\lambda_+}.
\tag{4}
\]
Differentiate (4) with respect to \(b=b_\gamma(s)\):
\[
\frac{\partial f_j}{\partial b}=
\frac{z_+^{N-1}z_-^{N-1}(z_--z_+)(z_+^j-z_-^j)}{(E_--E_+)^2}<0.
\tag{5}
\]
For the elongating transform the derivative is the same strictly negative prefactor, multiplied by
\((s+k_d+\lambda_+)(z_+^j-z_-^j)-k_d(z_+^{j-1}-z_-^{j-1})\) divided by \(\lambda_+\). This factor is positive since the sequence \(z_+^j-z_-^j\) strictly increases with \(j\). Because \(\partial_\gamma b_\gamma=-s\lambda_+/[k_d(s+\lambda_-+\gamma)^2]<0\), both \(f_j\) and \(g_j\) increase strictly with \(\gamma\), proving the finite-size Laplace ordering.

At criticality set \(P=k_e(k_d+\lambda_+)=k_d(k_e+\lambda_-)\), so \(D=P/(\lambda_++\lambda_-)\). With \(s=\sigma/N^2\), the two characteristic roots satisfy
\[
z_\pm=1\pm\frac{h}{N}+O(N^{-2}),\qquad
b_\gamma=1+\frac{\sigma\delta_\gamma}{N^2}+O(N^{-4}).
\]
Consequently \(E_-\sim he^{-h}/N\) and \(E_+\sim-he^h/N\). Formula (4) immediately gives (1), uniformly when \(j/N\) remains in a compact subset of \([0,1]\). The difference between elongating and shortening transforms is \(O(N^{-1})\).

For two values \(b_1,b_2\), subtraction of the two instances of (4) gives the *exact identity*
\[
f_j(b_1)-f_j(b_2)
=(b_1-b_2)\frac{z_+^{N-1}z_-^{N-1}(z_--z_+)(z_+^j-z_-^j)}{(E_-^{(1)}-E_+^{(1)})(E_-^{(2)}-E_+^{(2)})}.
\tag{6}
\]
Use \(b_1-b_2=\sigma(\delta_{\gamma_1}-\delta_{\gamma_2})/N^2+O(N^{-4})\), \(z_--z_+\sim-2h/N\), \(z_+^{j_N}-z_-^{j_N}\to2\sinh(hx)\), and \(E_-^{(r)}-E_+^{(r)}\sim2h\cosh(h)/N\). This proves (2) for the shortening state. Applying the expression for \(g_j\) in (4) proves the same limit for the elongating state because the difference between the two adjacent values of (6) is \(O(N^{-2})\).

Finally differentiate the backward equations at \(s=0\). If \(m_j=\mathbb E_{(j,i)}\tau\) and \(d_j=m_j-m_{j-1}\), criticality gives \(d_{j+1}=d_j-1/D\) and the cap gives \(d_N=\delta_\gamma\). Thus \(d_j=\delta_\gamma+(N-j)/D\), whose sum yields (3). The active-state mean formula follows directly from its backward equation. This also independently fixes the normalization in (1): the reflected-diffusion mean is \(x(2-x)/(2D)\), exactly the leading term of (3).

## Verification
Run `python verify.py` with Python 3, NumPy, SciPy and mpmath. The script constructs the complete killed continuous-time Markov generator for multiple rate sets, solves its resolvent directly, and independently compares against the characteristic-root formula (4). It also solves the mean-time linear equations directly, verifies monotonicity for both states, and checks convergence in (1) and (2) over growing caps for several values of the scaled Laplace variable and starting positions. The bundled script completed 3,960 finite consistency checks in the reported replay. Numerical checks illustrate and stress-test the proof; they are not proofs of all-size or all-parameter claims.

## Relationship to prior work
Singh, Garai and Chowdhury, arXiv:2610.29270 (first posted 2026-10-21), formulate this two-state lattice filament model with the particular cap conversion \(\gamma=k_e\), derive finite-length mean first-passage formulas and discuss critical slowing as the cap grows. Their exact mean already contains the \(\gamma=k_e\) specialization of (3), so neither that specialization nor the critical order-\(N^2\) scaling is claimed as new. The present result concerns an independently tunable cap-conversion mechanism, its strict Laplace ordering, and the *first cap-sensitive correction to the full quadratic-scale first-passage transform*.

Angelani, arXiv:1601.04845, analyzes a continuum telegrapher model with absorbing/reflecting boundaries and its Brownian limit; this gives important established precedent for leading diffusion-limit first-passage laws. The continuum model uses instantaneous directional reflections rather than this lattice process's cap-induced change of elongation state. Bicout's Phys. Rev. E 56 (1997) treats microtubule dynamic instability and first-passage distributions for continuum persistent motion. Those contributions are not claimed as new. The available Bicout material did not suffice to exclude all implicit variants of the present cap correction; this remains a publication-priority risk.

## Limitations
The results require finite positive internal switching and stepping rates. The explicit scaling laws assume exact zero bulk drift and fixed \(\gamma\) as \(N\to\infty\). They do not cover growing wall rates, position-dependent transition rates, multiple filament ends, or nonlinear physical cap mechanics. Laplace-transform ordering does not establish sample-path ordering or ordinary first-order stochastic dominance. The numerical verifier is finite and cannot certify the infinite limit. The originality assessment is based on the stated inspected sources and a best-knowledge search; independent mathematical and publication-priority validation have not been performed.

## References
1. M. Singh, A. Garai and D. Chowdhury, *Stochastic model of elongation-shortening-switching kinetics of a polymeric filament: Critical slowing down of first-passage and finite-size regularization*, arXiv:2610.29270v1 (first posted 2026-10-21), https://arxiv.org/abs/2610.29270; full article https://arxiv.org/html/2610.29270v1.
2. L. Angelani, *Run-and-tumble particles, telegrapher's equation and absorption problems with partially reflecting boundaries*, arXiv:1601.04845v1 (2016), https://arxiv.org/html/1601.04845v1.
3. D. J. Bicout, *Green's functions and first passage time distributions for dynamic instability of microtubules*, Physical Review E 56, 6656–6667 (1997), https://doi.org/10.1103/PhysRevE.56.6656.
4. H. J. Leydolt, *First-passage times and solutions of the telegrapher equation with boundaries*, Physical Review E 47, 3988–3995 (1993), https://doi.org/10.1103/PhysRevE.47.3988.
