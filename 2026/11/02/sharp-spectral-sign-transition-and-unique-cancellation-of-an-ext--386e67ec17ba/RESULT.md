# Sharp spectral sign transition and unique cancellation of an extrapolated symmetric-energy monitor

## Finding

For the exactly sampled positive-definite quadratic gradient flow, the extrapolated symmetric-energy discrepancy has a **sharp spectral comparison with the physical energy drop** and exactly one positive sign-change time when the terminal state is held fixed. A two-mode example makes the discrepancy exactly zero despite an energy loss of \(24\).

Let \(D_h(v)\) denote the symmetric-minus-physical energy defect and \(\Delta_h(v)\) the true positive energy drop over the preceding interval. If \(a\) and \(b\) are the least and greatest eigenvalues of the positive-definite flow matrix, then for every \(v\ne0\) and \(h>0\),
\[
\boxed{\frac{e^{ah}-3}{2(e^{ah}+1)}\le\frac{D_h(v)}{\Delta_h(v)}\le\frac{e^{bh}-3}{2(e^{bh}+1)}}.
\]
Each bound is attained on its corresponding eigenvector. Consequently \(D_h(v)<0\) for every nonzero \(v\) if and only if \(0<h<\log(3)/b\). The endpoint is sharp and the defect can change sign beyond it.

Furthermore, **for every fixed terminal vector** \(v\ne0\), the defect has exactly one positive zero as \(h\) varies. Writing \(a_*\le b_*\) for the extreme *active* eigenvalues of \(v\), the unique root satisfies
\[
\frac{\log3}{b_*}\le h_*(v)\le\frac{\log3}{a_*},
\]
strictly on both sides when \(a_*<b_*\). Before the zero the defect is negative; afterward it is positive.

## Assumptions and scope

Work in \(\mathbb R^n\), \(n\ge1\). Let \(A=A^{\mathsf T}\succ0\). Its ordered eigenvalues are \(0<a=\lambda_{\min}(A)\le\lambda_{\max}(A)=b\). Set \(E(u)=\frac12u^{\mathsf T}Au\) and consider the exact Euclidean gradient flow \(u'(t)=-Au(t)\), with \(u(0)=v\ne0\). For each lookback \(h>0\), the previous exact state is \(w=u(-h)=e^{hA}v\). Define
\[
S_h(v)=\frac12\left[E(v)+E(2v-w)\right],\quad D_h(v)=S_h(v)-E(v),\quad\Delta_h(v)=E(w)-E(v)>0.
\]
Thus \(S_h\) is evaluated on exact trajectory samples, not approximate solver output. The terminal vector \(v\) is **fixed when \(h\) varies**. Active eigenvalues are those whose orthogonal spectral projections of \(v\) are nonzero. Repeated eigenvalues are combined into single spectral projectors.

## Proof

**Step 1: exact modal decomposition.** Choose an orthonormal eigenbasis and write \(v=(v_j)\), \(A=\operatorname{diag}(\lambda_j)\). Set \(c_j=\lambda_jv_j^2\ge0\), \(z_j=e^{h\lambda_j}>1\). At least one \(c_j\) is positive. Direct quadratic expansion gives
\[
\Delta_h(v)=\frac12\sum_jc_j(z_j^2-1),\qquad
D_h(v)=\frac14\sum_jc_j(z_j-1)(z_j-3).
\]
In particular each active modal energy drop is strictly positive.

**Step 2: sharp relative-drop envelope.** Every nonzero modal contribution satisfies
\[
\frac{D_{h,j}}{\Delta_{h,j}}=r(h\lambda_j),\qquad r(x)=\frac{e^x-3}{2(e^x+1)}.
\]
The derivative \(r'(x)=2e^x/(e^x+1)^2\) is strictly positive. Since \(D_h/\Delta_h\) is the average of the modal ratios weighted by the strictly positive modal drops, it lies between the endpoint values. Restricting \(v\) to the least or greatest eigenspace attains the corresponding bound, including repeated-eigenvalue cases. If \(h<\log3/b\), all modal factors \(z_j-3\) are negative. Conversely at \(h=\log3/b\), a greatest-eigenvalue vector gives zero, so the stated uniform strict-sign threshold is exact.

**Step 3: unique crossover for an arbitrary number of active modes.** Put \(y_j=e^{h\lambda_j}-1>0\) and
\[
M(h)=\frac{\sum_jc_j y_j^2}{\sum_jc_j y_j}.
\]
Then \(4D_h(v)=(\sum_jc_jy_j)(M(h)-2)\): the defect and \(M(h)-2\) have the same sign. Define probabilities \(p_j(h)=c_jy_j/(\sum_kc_ky_k)\) on active modes and logarithmic growth rates
\[
\ell_j(h)=\frac{y_j'(h)}{y_j(h)}=\frac{\lambda_je^{h\lambda_j}}{e^{h\lambda_j}-1}.
\]
Differentiating the probability-weighted mean \(M(h)=\sum_jp_j(h)y_j(h)\) yields
\[
M'(h)=\sum_jp_jy_j'+\operatorname{Cov}_{p}(y_j,\ell_j).
\]
The first term is strictly positive. Both \(y_j\) and \(\ell_j\) increase with \(\lambda_j\): for \(x>0\),
\[
\frac{d}{dx}\left(\frac{x}{1-e^{-x}}\right)=\frac{1-(1+x)e^{-x}}{(1-e^{-x})^2}>0,
\]
by \(e^x>1+x\). Therefore their weighted covariance is nonnegative, as follows from the identity \(\operatorname{Cov}_p(f,g)=\frac12\sum_{i,j}p_ip_j(f_i-f_j)(g_i-g_j)\). Thus \(M'(h)>0\) for every \(h>0\). Also \(M(h)\to0\) as \(h\downarrow0\), while \(M(h)\to\infty\) as \(h\to\infty\). The intermediate value theorem proves the unique root of \(M(h)=2\), together with the sign on either side.

At \(h=\log3/b_*\), every active \(y_j\le2\), and at \(h=\log3/a_*\), every active \(y_j\ge2\). The strict weighted-mean inequalities for two distinct active rates give the claimed strict root bracket. A single active rate gives equality \(h_*=\log3/\lambda\).

**Step 4: exact two-mode cancellation.** Take \(A=\operatorname{diag}(1,2)\), \(h=\log2\), \(v=(\sqrt6,1)^{\mathsf T}\). Then \(w=e^{hA}v=(2\sqrt6,4)^{\mathsf T}\) and \(2v-w=(0,-2)^{\mathsf T}\). Exactly,
\[
E(v)=4,\quad E(w)=28,\quad E(2v-w)=4,\quad S_h(v)=4.
\]
Hence \(\Delta_h(v)=24>0\) but \(D_h(v)=0\). Both eigenspaces are active. The physical loss can be made arbitrarily large by scaling \(v\), while the defect remains zero; this scaling observation concerns absolute loss, not relative loss.

## Verification

The accompanying standalone `verify.py` uses only the Python 3 standard library. It checks the two-mode witness with exact rational squared amplitudes and exponential factors, then tests direct energy identities, strict spectral ratio envelopes, increasing effective amplification means, and the unique zero bracket on seeded random spectra. The code reports the number of assertions passed and has been replayed from the embedded file bytes. These checks support reproducibility but do not replace the continuous-parameter proof above.

## Relationship to prior work

Shergill and Williams (2026), Section 3.1, equation (7) and Proposition 1, define the same symmetric energy and prove a small-step asymptotic dissipation relation. Their result is correct in its stated small-step regime. The present finding instead gives an **exact finite-lookback** characterization on the natural self-adjoint quadratic test class: a sharp spectral error-to-drop envelope, a unique sign transition for every terminal state, and an explicit two-mode cancellation. None of these exact statements is identified in the inspected paper, including its later algorithm and convergence sections.

The standard modified-energy inequalities in quadratic BDF2/SAV schemes and related energy-stability results concern discrete stability or auxiliary energies; they do not by themselves imply this exact continuous-trajectory sign law. Relevant source comparisons and remaining priority risks are stated in `REVIEW.md` and `AUDIT.json`.

## Limitations

The assumptions require an exactly sampled finite-dimensional **symmetric positive-definite** quadratic gradient flow, and the sign transition keeps the terminal state fixed while varying the backward lookback. The theorem says nothing directly about nonlinear gradient flows, non-self-adjoint generators, internal SAV variables, variable-step acceptance logic, or numerical accuracy and stability of SSAV–BDF2. It does **not** contradict the original small-step theorem. Independent review and exhaustive historical-priority confirmation have not been carried out.

## References

1. S. Shergill and JF Williams, *Energy-rate equidistribution for adaptive SSAV–BDF2 integration of gradient flows*, arXiv:2610.30454v1, first posted 2026-10-21. https://arxiv.org/html/2610.30454v1 — Sections 2–4, particularly equation (7) and Proposition 1.
2. *An Energy-Stable S-SAV Finite Element Method for the Generalized Poisson–Nernst–Planck Equation*, Axioms 15(2), 126 (2026), https://www.mdpi.com/2075-1680/15/2/126 — contextual modified-energy treatment; complete manuscript was not accessible during comparison.
