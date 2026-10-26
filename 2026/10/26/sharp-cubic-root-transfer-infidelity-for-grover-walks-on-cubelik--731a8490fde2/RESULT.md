# Sharp cubic-root transfer infidelity for Grover walks on cubelike graphs

## Finding

For every set \(\Omega\subset\mathbb F_2^d\setminus\{0\}\) of \(\Delta\ge1\) distinct generators, consider the moving-shift, Grover-coined discrete-time quantum walk initialized at the origin with the uniform coin. Put \(\sigma=\bigoplus_{\omega\in\Omega}\omega\), and choose any positive integer \(T\) with \(T\equiv\Delta\pmod 2\) and \(\lvert T-\pi\Delta/2\rvert\le1\). If \(p_T(\sigma)\) is the probability of observing position \(\sigma\) after \(T\) unmeasured steps, then

\[
0\le 1-p_T(\sigma)\le16\Delta^{-1/3}.
\]

The cubic-root exponent is **optimal over arbitrary connected cubelike graphs**. Specifically, for every \(k\ge1\), set \(h=2^k\), \(b=h^2\), \(d=k+b+1\), and

\[
\Omega_h=\bigl\{(u,e_j,0):u\in\mathbb F_2^k,\ 1\le j\le b\bigr\}\cup\bigl\{(0,0,1)\bigr\}\subset\mathbb F_2^k\times\mathbb F_2^b\times\mathbb F_2.
\]

This is a connected simple cubelike generating set of degree \(\Delta_h=h^3+1\), whose XOR target is the **nonzero** vertex \(\sigma_h=(0,0,1)\). For every permitted choice of \(T_h\),

\[
\lim_{k\to\infty}h\bigl(1-p_{T_h}(\sigma_h)\bigr)
= c_*:=2\mathbb E\left[1-\cos\left(\frac{\pi Z^3}{12}\right)\right]>0,
\qquad Z\sim\mathcal N(0,1).
\]

Numerically, \(c_*\approx0.3340087115\). Equivalently, \(\Delta_h^{1/3}(1-p_{T_h}(\sigma_h))\to c_*\). The obstruction is a positive fraction, of order \(\Delta_h^{-1/3}\), of Fourier modes with a nontrivial cubic Gaussian phase. Thus the previously established general exponent \(1/5\) can be sharpened to \(1/3\), but no uniform larger exponent can hold for the same model and observation window.

## Assumptions and scope

The position space is \(\ell^2(\mathbb F_2^d)\); the coin space has basis \(\{|\omega\rangle:\omega\in\Omega\}\). Let

\[
|D\rangle=\Delta^{-1/2}\sum_{\omega\in\Omega}|\omega\rangle,\qquad
C=2|D\rangle\langle D|-I,\qquad
S|\omega,x\rangle=|\omega,x\oplus\omega\rangle,
\]

with one-step unitary \(U=S(C\otimes I)\) and initial state \(|\psi_0\rangle=|D,0\rangle\). We measure *only position* at the final time, with no intermediate measurement or noise:

\[
p_T(v)=\sum_{\omega\in\Omega}|\langle\omega,v|U^T|\psi_0\rangle|^2.
\]

No assumption of a specific generating-set geometry, dimension-to-degree relation, or bounded Hamming weight is imposed for the uniform inequality. The lower-bound construction spans the entire ambient group, so it is connected. The observation time is parity matched; choosing it is always possible because integers with one prescribed parity occur every two steps.

## Proof

**1. Exact phase representation.** For every Fourier character \(a\in\mathbb F_2^d\), put

\[
\chi_a(x)=(-1)^{a\cdot x},\quad M(a)=\sum_{\omega\in\Omega}\chi_a(\omega),\quad m(a)=M(a)/\Delta,\quad \theta_a=\arccos m(a).
\]

Fourier diagonalization of the moving shift gives \(U_a=D_a C\), with \(D_a\) diagonal of entries \(\chi_a(\omega)\). The span of \(|D\rangle,D_a|D\rangle\) is invariant, and \(\langle D|U_a^T|D\rangle=\cos(T\theta_a)\). The scalar amplitude in coin direction \(|D\rangle\) at the target is therefore

\[
A_T(\sigma)=2^{-d}\sum_a\chi_a(\sigma)\cos(T\theta_a),\qquad p_T(\sigma)\ge |A_T(\sigma)|^2.
\]

Since \(\chi_a(\sigma)=(-1)^{(\Delta-M(a))/2}\), the parity condition on \(T\) gives the **exact**, not asymptotic, identity

\[
A_T(\sigma)=\kappa\,\mathbb E_a\cos\rho(a),\quad
\kappa=(-1)^{(\Delta-T)/2},\quad
\rho(a)=\frac{\pi M(a)}2-T\arcsin\frac{M(a)}\Delta,
\]

where \(a\) is uniform in \(\mathbb F_2^d\). This identity holds also at \(m(a)=\pm1\) by continuity. Distinctness of the generators yields the exact second moment

\[
\mathbb E_a[m(a)^2]=\Delta^{-1}
\]

by character orthogonality.

**2. Uniform cubic-root estimate.** Write \(T=\pi\Delta/2+\eta\), with \(|\eta|\le1\), and \(m=m(a)\). For \(|m|\le1/2\), elementary calculus gives \(|\arcsin m|\le2|m|\) and \(|\arcsin m-m|\le|m|^3\), hence

\[
|\rho|\le2|m|+2\Delta|m|^3.
\]

If \(|m|\le\Delta^{-1/3}\), the elementary inequality \(1-\cos\rho\le\rho^2/2\) yields

\[
1-\cos\rho\le4m^2+4\Delta^2m^6\le8\Delta^{2/3}m^2.
\]

If \(|m|>\Delta^{-1/3}\), the trivial bound \(1-\cos\rho\le2\) gives \(1-\cos\rho\le2\Delta^{2/3}m^2\) without any restriction on \(m\). The small-\(m\) argument applies whenever \(\Delta\ge8\); for smaller degrees the displayed final bound is trivially at least one. Thus, when \(\Delta\ge8\),

\[
e:=\mathbb E_a[1-\cos\rho(a)]\le8\Delta^{2/3}\mathbb E_a[m(a)^2]=8\Delta^{-1/3}.
\]

As \(A_T(\sigma)=\kappa(1-e)\), we have

\[
1-p_T(\sigma)\le1-(1-e)^2=2e-e^2\le16\Delta^{-1/3}.
\]

For \(\Delta<8\), \(1-p_T(\sigma)\le1\le16\Delta^{-1/3}\) completes the assertion.

**3. Connected sharpness family.** Fix \(k\ge1\) and the explicitly defined \(\Omega_h\) above. The vectors \((0,e_j,0)\) belong to \(\Omega_h\); their differences with \((u,e_j,0)\) generate the first \(k\) coordinates, while the exceptional generator supplies the last coordinate. Thus \(\Omega_h\) spans. Each \(e_j\) occurs \(h\) times and \(b=h^2\) is even, implying \(\sigma_h=(0,0,1)\).

Write a uniform Fourier mode as \(a=(\alpha,\beta,\gamma)\), let \(\xi=(-1)^\gamma\), and define

\[
S_b=\sum_{j=1}^b(-1)^{\beta_j}.
\]

Character factorization gives

\[
M(a)=h\,\mathbf1_{\{\alpha=0\}}S_b+\xi.
\]

The event \(\alpha=0\) has probability \(1/h\). Off this event, \(M(a)=\xi\), so \(\rho(a)=O(\Delta_h^{-1})\) uniformly. On this event, \(S_b/h\Rightarrow Z\sim\mathcal N(0,1)\) by the elementary iid central limit theorem, because \(b=h^2\). On every bounded range of \(S_b/h\), Taylor expansion with remainder gives

\[
\rho(a)
=-\frac{\pi\Delta_h}{2}\left(\arcsin m-m\right)-\eta\arcsin m
=-\frac{\pi}{12}\left(\frac{S_b}{h}\right)^3+o(1),
\quad m=\frac{hS_b+\xi}{h^3+1}.
\]

The event outside each bounded range has asymptotically arbitrarily small probability, so bounded continuity of cosine and the central limit theorem imply

\[
\mathbb E[\cos\rho\mid\alpha=0]\longrightarrow
c_0:=\mathbb E\cos(\pi Z^3/12)<1.
\]

Consequently, the exact scalar amplitude satisfies

\[
\kappa A_{T_h}(\sigma_h)
=1-\frac{1-c_0}{h}+o(h^{-1}).
\]

To convert this into a statement about the **full position probability**, not merely one coin projection, let

\[
v_h=(I\otimes\langle\sigma_h|)U^{T_h}|\psi_0\rangle
=2^{-d}\sum_a\chi_a(\sigma_h)U_a^{T_h}|D\rangle.
\]

For \(|m(a)|<1\), the Fourier block rotates \(|D\rangle\) into \(\cos(T\theta_a)|D\rangle+\sin(T\theta_a)|E_a\rangle\), where \(|E_a\rangle\) is a unit vector orthogonal to \(|D\rangle\). The parity identity also gives \(|\sin(T\theta_a)|=|\sin\rho(a)|\). On \(\alpha\ne0\), \(|\rho(a)|=O(\Delta_h^{-1})\); the remaining modes have total probability \(1/h\) and their orthogonal coin component has norm at most one, including the degenerate \(|m|=1\) cases. Therefore

\[
\|(I-|D\rangle\langle D|)v_h\|
\le O(\Delta_h^{-1})+h^{-1}=O(h^{-1}).
\]

Since \(\langle D|v_h\rangle=A_{T_h}(\sigma_h)\), Pythagoras now gives

\[
p_{T_h}(\sigma_h)=\|v_h\|^2
=|A_{T_h}(\sigma_h)|^2+O(h^{-2})
=1-\frac{2(1-c_0)}h+o(h^{-1}).
\]

The limiting constant is strictly positive because a nondegenerate Gaussian does not concentrate on the discrete set where \(\cos(\pi Z^3/12)=1\). Since \(\Delta_h^{1/3}/h\to1\), the exponent \(1/3\) cannot be uniformly increased.

## Verification

The standalone standard-library program `verification.py` implements two logically separate finite checks. First, it directly evolves all \(576\) coin-position amplitudes for the \(h=2\) graph through its parity-matched \(15\) steps, comparing the probability at its nonzero XOR target against the Fourier/binomial calculation to better than \(10^{-12}\). Second, it evaluates the exact binomial Fourier reduction at \(h\in\{2,4,8,16,32,64,128\}\), checking the universal inequality and reporting \(h(1-p_T)\), which approaches the predicted positive constant. Run from the directory containing this document with `python3 verification.py`.

Numerical evaluation of the one-dimensional Gaussian integral gives \(c_*\approx0.3340087115\). Finite cases and floating-point quadrature do not prove the arbitrary-degree inequality or the Gaussian limit; those follow from the analytic argument above.

## Relationship to prior work

Mulherkar (2026), arXiv:2609.04503v1, proves convergence at the parity-matched observation time with the uniform error bound \(O(\Delta^{-1/5})\), using the exact Fourier-character representation and its second-moment identity. The cited work specifically identifies improvement of the exponent as a further direction. Those Fourier identities are **previously known** and are not claimed here. The present claim replaces the threshold good/bad-mode estimate by a direct bound on nonlinear phase loss and proves that the resulting exponent is optimal through a connected, nonzero-target family with a Gaussian cubic asymptotic constant.

Kempe (2002/2005) treats the hypercube and derives a much stronger error bound restricted to that highly structured generating set; this does not imply a uniform estimate over all cubelike graphs, and is consistent with the sharp worse-case family here. Mulherkar, Rajdeepak and Sunitha (2021) study hypercubes and augmented cubes computationally and conjecture universal near-perfect hitting; their finite-family calculations do not identify the sharp worst-case decay. Continuous-time perfect state transfer on cubelike graphs concerns a different evolution operator and does not imply this discrete-time sharpness statement.

## Limitations

The sharpness statement concerns the specified one-shot parity-matched time window, not an optimization over all observation times. The extremal graphs have dimensions growing much faster than their degrees, and the constructed target is adjacent to the origin; the result does **not** assert slow convergence in hypercubes or in all natural low-dimensional families. The analytic construction proves only the optimal decay *exponent* and the displayed constant for the specified family, not an optimal universal numerical coefficient. It says nothing about concurrent measurements, noise, partial dephasing, or hardware costs. Literature-wide novelty beyond the explicitly compared sources is not independently certified.

## References

1. J. Mulherkar, *One-Shot and Concurrent Hitting Times for Grover-Coined Quantum Walks on Cubelike Graphs*, arXiv:2609.04503v1 (first submitted 3 September 2026), especially Sections 2–5 and Section 8. https://arxiv.org/html/2609.04503
2. J. Kempe, *Quantum Random Walks Hit Exponentially Faster*, arXiv:quant-ph/0205083v1 (2002); journal version *Probability Theory and Related Fields* **133** (2005), 215–235, especially Theorem 1. https://arxiv.org/pdf/quant-ph/0205083
3. J. Mulherkar, R. Rajdeepak and V. Sunitha, *Implementation of Hitting Times of Discrete Time Quantum Random Walks on Cubelike Graphs*, arXiv:2108.13769v1 (2021), especially Section 5.3 and Conjecture 1. https://arxiv.org/pdf/2108.13769
