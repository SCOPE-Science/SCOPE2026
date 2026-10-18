# Sharp large-opinion instability rate and extremist boundary layer in incremental voting

## Finding

For every integer \(k\ge1\), the uniform equilibrium of the reflecting mean-field incremental voter model on \(\{-k,\ldots,k\}\) has one positive linear growth eigenvalue \(\lambda_k\). Write \(t_k=\operatorname{arcosh}(1+\lambda_k)\). Its exact characterization is the unique positive solution of
\[
\sinh((k+1)t_k)-\sinh(kt_k)=\frac{4}{k(2k+1)}\sum_{j=1}^{k}j\sinh(jt_k).
\]
The new quantitative statement is
\[
\boxed{\lambda_k=\frac1k-\frac{1}{\sqrt2\,k^{3/2}}+o(k^{-3/2})}\qquad (k\to\infty),
\]
and the exact unstable eigenvector, normalized to \(h_k=1\), is
\[
h_j=\frac{\sinh(jt_k)}{\sinh(kt_k)},\qquad -k\le j\le k.
\]
For every fixed \(x\ge0\),
\[
\boxed{\lim_{k\to\infty}h_{k-\lfloor x\sqrt k\rfloor}=e^{-\sqrt2 x}}.
\]
By antisymmetry the left extreme has the opposite profile. Thus the initial unstable linear response concentrates in extreme-opinion boundary layers of width \(\sqrt k\), although its linear growth time increases as \(k\).

## Assumptions and scope

Let \(k\) be an arbitrary positive integer and let \(p=(p_{-k},\ldots,p_k)\) be a probability vector. Write \(m=\sum_{j=-k}^kjp_j\), \(a=(k+m)/(2k)\), and \(b=(k-m)/(2k)\). The continuous-time mean-field flow is
\[
\dot p_{-k}=bp_{-k+1}-ap_{-k},\qquad
\dot p_j=ap_{j-1}+bp_{j+1}-p_j\ (-k<j<k),\qquad
\dot p_k=ap_{k-1}-bp_k.
\]
This is precisely the normalization of Cao and Gong's mean-field equation (2.1), without added exploration. The uniform probability \(u_j=1/(2k+1)\) is an equilibrium. All eigenvalues below are those of its Jacobian restricted to the mass-zero tangent space \(\{h:\sum_jh_j=0\}\); the full Jacobian also has the uninformative mass-direction zero eigenvalue. The statement concerns a local, infinitesimal instability and makes no nonlinear escape-time assertion for arbitrary initial conditions.

## Proof

**1. Exact Jacobian.** Let \(L\) be the symmetric nearest-neighbor reflecting random-walk generator: for interior indices \((Lh)_j=(h_{j-1}+h_{j+1})/2-h_j\), and at the endpoints \((Lh)_{-k}=(h_{-k+1}-h_{-k})/2\) and \((Lh)_k=(h_{k-1}-h_k)/2\). Linearizing the displayed nonlinear equations at \(u\) makes all interior drift derivatives cancel. The sole mean feedback is at the endpoints:
\[
Jh=Lh+\frac{m_h}{k(2k+1)}(e_k-e_{-k}),\qquad m_h=\sum_{j=-k}^kjh_j.
\]
Reflection-even mass-zero perturbations therefore evolve under the strictly negative reflecting-Laplacian spectrum; the odd subspace contains every growing eigenmode.

**2. One positive mode and the characteristic equation.** Represent an odd vector by \(z_j=h_j\), \(1\le j\le k\), with \(h_0=0\), \(h_{-j}=-h_j\). On this subspace let \(A=-L_{\mathrm{odd}}\). Then \(A\) is symmetric positive definite (Dirichlet at zero, reflecting at \(k\)) and
\[
J_{\mathrm{odd}}=-A+\frac{2}{k(2k+1)}e_kw^{\mathsf T},\qquad w=(1,2,\ldots,k)^{\mathsf T}.
\]
A direct difference-equation calculation gives \(A^{-1}e_k=2w\), hence
\[
J_{\mathrm{odd}}=-A+\frac{1}{k(2k+1)}e_ke_k^{\mathsf T}A^{-1}.
\]
The similar matrix \(A^{-1/2}J_{\mathrm{odd}}A^{1/2}\) is the symmetric rank-one update
\[
-A+\frac{1}{k(2k+1)}(A^{-1/2}e_k)(A^{-1/2}e_k)^{\mathsf T}.
\]
It has at most one positive eigenvalue. Its zero-crossing criterion is
\[
\frac{1}{k(2k+1)}e_k^{\mathsf T}A^{-2}e_k
=\frac{4}{k(2k+1)}\sum_{j=1}^kj^2
=\frac{2(k+1)}3>1.
\]
Thus exactly one eigenvalue is positive and all remaining tangent eigenvalues are negative. For any positive eigenvalue write \(\lambda=\cosh t-1\), \(t>0\). The interior recurrence has the odd solution \(z_j=C\sinh(jt)\). The boundary row at \(j=k\) gives
\[
(2\lambda+1)\sinh(kt)-\sinh((k-1)t)=\frac4{k(2k+1)}\sum_{j=1}^kj\sinh(jt),
\]
which is the stated characteristic equation by the hyperbolic addition identity. Existence and uniqueness of the positive eigenvalue already establish existence and uniqueness of \(t_k>0\) in this equation. For \(k=1\) it yields \(\lambda_1=1/6\).

**3. Large-\(k\) growth law.** Set \(\Delta=\sinh((k+1)t)-\sinh(kt)\). The exact finite sum identity
\[
\sum_{j=1}^{k}j\sinh(jt)=\frac{k\sinh((k+1)t)-(k+1)\sinh(kt)}{2(\cosh t-1)}
\]
converts the eigenvalue equation into
\[
\lambda_k=\frac2{2k+1}\left(1-R_k\right),\quad
R_k=\frac{\sinh(kt_k)}{k\Delta_k}
=\frac{1}{k\{\lambda_k+\coth(kt_k)\sinh t_k\}}.
\]
Since \(0<R_k<1\), it follows that \(0<\lambda_k<2/(2k+1)\), so \(t_k\to0\). We now prove \(kt_k\to\infty\). Otherwise on a subsequence \(kt_k\le C\); the left side of the characteristic equation is at most \(t_k\cosh(C+1)\), while its right side is at least
\[
\frac{4t_k}{k(2k+1)}\sum_{j=1}^kj^2=\frac{2(k+1)}3\,t_k,
\]
a contradiction for large \(k\). Consequently \(\coth(kt_k)\to1\) and \(R_k\sim1/(kt_k)\to0\). Hence \(k\lambda_k\to1\) and \(t_k\sim\sqrt{2/k}\). Inserting this back into the exact expression gives
\[
\sqrt{k}(1-k\lambda_k)=\frac{\sqrt{k}}{2k+1}+\frac{2k}{2k+1}\sqrt{k}\,R_k\longrightarrow \frac1{\sqrt2},
\]
proving the claimed two-term asymptotic.

**4. Extreme-opinion boundary layer.** Put \(d_k=\lfloor x\sqrt{k}\rfloor\). Since \(kt_k\to\infty\), \(d_kt_k\to x\sqrt2\), and \((k-d_k)t_k\to\infty\),
\[
\frac{\sinh((k-d_k)t_k)}{\sinh(kt_k)}
=e^{-d_kt_k}\frac{1-e^{-2(k-d_k)t_k}}{1-e^{-2kt_k}}
\longrightarrow e^{-\sqrt2 x}.
\]
All claims follow.

## Verification

The standalone script `verification/check.py` independently differentiates the nonlinear mean-field vector field numerically for every \(1\le k\le14\), computes the Jacobian eigenvalues, and compares its unique positive eigenvalue and eigenvector with the exact root formula. It additionally checks the proposed large-\(k\) coefficients and boundary profile at \(k=100,1000,10000\). Run `python -m pip install -r verification/requirements.txt` followed by `python verification/check.py`. These finite checks supplement, but are not used in place of, the proof for all \(k\).

## Relationship to prior work

Cao and Gong (2026, Eq. (2.1), Sections 3.1–3.2) derived this mean-field model, proved global qualitative behavior and special quantitative estimates for three opinion states, and discussed the difficulty of obtaining general quantitative information when the number of opinion states grows. The mere existence of a one-dimensional unstable direction is also covered by earlier analysis of an exploration-regularized version specialized to zero exploration and is not claimed as a new result. The new quantitative assertion is the exact characteristic equation together with its two-term large-opinion growth law and a universal localized unstable eigenvector. Reflecting Laplacian spectral-gap statements for symmetric perturbations do not give this positive-growth rate or its localized eigenfunction. Comparisons with potentially stronger unlocated results remain a priority risk.

## Limitations

The asymptotic concerns the linearized deterministic mean-field model as the number \(2k+1\) of opinion states grows; it does not provide global nonlinear convergence rates, finite-population mixing estimates, stochastic escape times, or a result with nonzero exploratory noise. The boundary-layer profile is pointwise for fixed nonnegative \(x\), not a uniform profile on growing windows. Historical priority beyond the inspected sources has not been independently certified.

## References

Cao, F., and Gong, X. (2026), *The incremental voter model: mean-field analysis and convergence to equilibrium*, arXiv:2605.28984v1 (first posted 2026-05-27), https://arxiv.org/pdf/2605.28984 . Relevant material: full text, particularly equation (2.1), Sections 3.1–3.2 and the conclusion.
