# Sharp polarization crossover of geometric discord in reset scar states

## Finding

The Poisson-reset stationary state of coherent scar-tower trajectories carries **strictly positive two-site quantum discord without two-site entanglement** at every nonzero, finite resetting rate. For any finite chain length \(L\ge2\), any pair of distinct sites, any \(0<|\alpha|<\infty\), any \(r>0\), and any nonzero tower spacing \(\omega\), its two-site state is separable but is not classical-quantum on either site.

For the one-sided *squared Hilbert--Schmidt* geometric discord \(D_{\mathrm{HS}}\), the sparse-reset limit yields a sharp, separation-independent polarization optimum. Put
\[
 t=\left(\frac{1-|\alpha|^2}{1+|\alpha|^2}\right)^2\in[0,1],\quad
 k(t)=\frac{(1-t)^2}{4},\quad h(t)=t+t^2.
\]
Then the stationary two-site geometric discord converges as \(r\downarrow0\) to
\[
 D_0(t)=\frac{2k(t)+h(t)-\max\{k(t),h(t)\}}4
 =\begin{cases}\frac{k(t)+h(t)}4,&0\le t\le t_*,\\ \frac{k(t)}2,&t_*\le t\le1,\end{cases}
\]
where
\[
 t_*=\frac{2\sqrt3-3}{3},\qquad \max_{0\le t\le1}D_0(t)=D_0(t_*)=\frac{2-\sqrt3}{3}.
\]
The unique maximizing *squared polarization* is \(t_*\); the two optimal amplitudes are reciprocal and correspond to opposite signs of the polarization. The geometric-discord minimizing measurement direction switches at \(t_*\): any equatorial axis below the threshold, the longitudinal axis above, and every axis exactly at the threshold. This is a measurement-optimization crossover, **not** a nonanalyticity in the underlying state or a thermodynamic phase transition.

For equatorial preparations \(|\alpha|=1\), the exact finite-rate result, with \(x=|\omega|/r\), is
\[
D_{\mathrm{HS}}(x)=\frac18\left[\frac{2x^4+7x^2+2}{(1+x^2)(1+4x^2)}
-\frac{\sqrt{x^4+12x^2+4}}{(1+x^2)\sqrt{1+4x^2}}\right]>0 \quad(x>0).
\]
It obeys \(D_{\mathrm{HS}}(x)=x^4/4-11x^6/8+O(x^8)\) as \(x\downarrow0\), and \(D_{\mathrm{HS}}(x)=1/16-1/(16x)+O(x^{-2})\) as \(x\to\infty\). The quantity here is an explicit squared Hilbert--Schmidt diagnostic; no data-processing monotonicity is claimed.

## Assumptions and scope

We use the product coherent state of Gotta, Kulkarni and Perfetto, *Towers of quantum many-body scars under stochastic resetting*, arXiv:2603.13165v1 (2026). Their Eq. (10) gives, in the local two-dimensional scar subspace, the tensor product of \((|0\rangle+\alpha e^{ikj}|1\rangle)/\sqrt{1+|\alpha|^2}\). Their restricted spectrum-generating algebra gives \(\alpha(\tau)=\alpha e^{i\omega\tau}\), up to an irrelevant choice of the sign of \(\omega\); their Eq. (13) gives the stationary renewal mixture weighted by \(re^{-r\tau}\). The local Hilbert space may have additional unused levels (as in spin one); all density operators and measurement statements are restricted to their occupied two-level subspace. A projective measurement of the occupied qubit may be extended on the unused levels without changing the restricted calculation.

After local diagonal phase rotations, each two-site state is
\[
\rho_{AB}(r)=\int_0^\infty re^{-r\tau}
 (|q_{\omega\tau}\rangle\langle q_{\omega\tau}|)^{\otimes2}\,d\tau,
\quad |q_\phi\rangle=\frac{|0\rangle+|\alpha|e^{i\phi}|1\rangle}{\sqrt{1+|\alpha|^2}}.
\]
This formula applies identically to all pairs of distinct sites and finite \(L\ge2\). The squared Hilbert--Schmidt geometric discord is defined explicitly as
\[
D_{\mathrm{HS}}(\rho)=\min_{\chi\in\mathrm{CQ}_A}\operatorname{Tr}(\rho-\chi)^2,
\]
where \(\mathrm{CQ}_A\) denotes the two-qubit states classical on the measured subsystem \(A\). We do not identify it with entropic discord or trace-norm geometric discord, which generally have different values.

## Proof

**1. Exact two-site reduction and separability.** The coherent state is a product in real space at each age \(\tau\); taking a pairwise partial trace commutes with the positive, normalized renewal integral. Therefore \(\rho_{AB}(r)\) is explicitly a convex mixture of pure product states and hence separable for all parameters. The two-site construction is exact, not a thermodynamic approximation.

**2. Strict positivity of ordinary discord.** Define \(z=(1-|\alpha|^2)/(1+|\alpha|^2)\), \(s=\sqrt{1-z^2}>0\), and \(x=|\omega|/r>0\). In a sign convention chosen so that the local Bloch vector at age \(\tau\) is \(v(\tau)=(s\cos(\omega\tau),s\sin(\omega\tau),z)\), the normalized phase moments are
\[
g_j=\int_0^\infty re^{-r\tau}e^{ij\omega\tau}\,d\tau=\frac1{1-ij\omega/r}\quad(j=1,2).
\]
Let \(T_{ab}=\mathbb E[v_av_b]\) be the Pauli correlation matrix. Its transverse principal minor is \(s^2 C\), where
\[
 C=\frac12\begin{pmatrix}1+\operatorname{Re}g_2&\operatorname{Im}g_2\\ \operatorname{Im}g_2&1-\operatorname{Re}g_2\end{pmatrix},\qquad
 \det C=\frac{1-|g_2|^2}{4}=\frac{x^2}{1+4x^2}>0.
\]
Thus \(\operatorname{rank}T\ge2\). Every two-qubit state classical on \(A\) has \(T=n b^\mathsf{T}\) for some Bloch direction \(n\) and vector \(b\), hence \(\operatorname{rank}T\le1\). Consequently this state has nonzero ordinary discord on \(A\). Exchange symmetry (after local rotations) gives the same for \(B\). This applies to finite, nonzero reset rates; \(r=\infty\), \(\omega=0\) and \(\alpha=0\) or its infinite-amplitude limit are excluded.

**3. Sparse-rate geometric-discord law.** For fixed \(\omega\ne0\) and \(r\downarrow0\), the Fourier moments \(g_1,g_2\) tend to zero. Hence \(u=\mathbb E[v]\to(0,0,z)\) and \(T\to\operatorname{diag}(s^2/2,s^2/2,z^2)\). By the two-qubit formula of Dakić, Vedral and Brukner, the squared Hilbert--Schmidt geometric discord is
\[
D_{\mathrm{HS}}=\frac14\left(|u|^2+\|T\|_F^2-\lambda_{\max}(uu^\mathsf T+TT^\mathsf T)\right).
\]
At the limit, \(K=uu^\mathsf T+TT^\mathsf T\) has eigenvalues \(k(t),k(t),h(t)\), with \(t=z^2\), yielding the displayed piecewise formula. The switch is determined exactly by \(k(t)=h(t)\), or \(3t^2+6t-1=0\), whose unique root in \([0,1]\) is \(t_*\). For \(t<t_*\), the maximum eigenvalue is the twofold-degenerate equatorial one; for \(t>t_*\), it is longitudinal, and at equality all three eigenvalues coincide. On the first interval \(D_0'(t)=(1+5t)/8>0\), and on the second \(D_0'(t)=(t-1)/4<0\) for \(t<1\). This proves the unique maximizing \(t\), and substitution gives the exact stated optimum. The asymmetry \(z\mapsto-z\) accounts for the two optimal amplitudes.

**4. Equatorial finite-rate formula.** With \(z=0\), the Bloch vector and nonzero correlation block are
\[
u=\left(\frac1{1+x^2},\frac{x}{1+x^2},0\right),\qquad
T_{xy}=\begin{pmatrix}
\frac12\left(1+\frac1{1+4x^2}\right)&\frac{x}{1+4x^2}\\
\frac{x}{1+4x^2}&\frac12\left(1-\frac1{1+4x^2}\right)
\end{pmatrix}.
\]
The sole nonzero eigenvalues of \(K=uu^\mathsf T+TT^\mathsf T\) are those of its real symmetric transverse block, whose trace and determinant are
\[
\operatorname{tr}K_{xy}=\frac{2x^4+7x^2+2}{(1+x^2)(1+4x^2)},\qquad
\det K_{xy}=\frac{x^4(x^4+6x^2+2)}{(1+x^2)^2(1+4x^2)^2}.
\]
Its discriminant is \((x^4+12x^2+4)/[(1+x^2)^2(1+4x^2)]\). The nonzero smaller eigenvalue is positive since trace and determinant are positive, and \(D_{\mathrm{HS}}\) equals a quarter of that smaller eigenvalue. The elementary quadratic formula gives the exact expression. Taylor expansion at zero and expansion in \(1/x\) give the stated rates. No finite-system approximation, numerical extrapolation or hidden normalization constant enters.

## Verification

Run `python verify_discord.py` with `numpy` and `sympy` (versions specified by `requirements.txt`). The standalone code reconstructs density matrices from explicit Pauli moments, independently compares selected values with phase-integral quadrature, verifies positivity and PPT for sampled parameters, checks the optimized sparse-rate formula, and proves the required rational identities and limiting coefficients symbolically. The checked script completed with `PASS 395 analytic and numerical assertions`. The symbolic proof in this document is the evidence for all parameter values; the finite tests do not certify an infinite quantifier by themselves.

## Relationship to prior work

Gotta, Kulkarni and Perfetto (arXiv:2603.13165v1) supply the exact coherent-scar factorization, renewal mixture, long-range order, and Rényi-entropy asymptotics. Their main text and technical appendices were examined. Their paper does not present the pairwise geometric-discord optimization or the polarization-dependent measurement-axis crossover; these, not the reset process or its separability, are the candidate contribution. Dakić, Vedral and Brukner (arXiv:1004.0190) derive the general two-qubit geometric-discord formula used here. Generation of discord by classical noise and collective twirling is established in earlier work (e.g. Lanyon and coworkers, arXiv:1304.3632, and Wu and Zhou, *Scientific Reports* 5, 13365, 2015); the general phenomenon of separable discord or its interpretation is NOT claimed to be new. The contribution consists of the **exact physical-family law**, its sharp reset-polarization optimum, measurement-axis transition, and finite-rate equatorial profile. More general results on collective phase averaging could subsume this particular calculation; this residual overlap risk remains.

## Limitations

The squared Hilbert--Schmidt quantity is not a monotone under arbitrary local channels on the unmeasured subsystem and should not be advertised as an operational entanglement monotone. The exact optimum concerns the sparse-reset limit and does not state that the same polarization remains optimal for finite positive rates. The ordinary discord positivity result is qualitative, not a closed formula for entropic discord. The model assumes exactly coherent scar-tower product trajectories, global Poisson resets, a nonzero equally spaced gap and access only to the occupied two-dimensional local subspaces. It makes no claim about realistic reset implementation errors or arbitrary scarred Hamiltonians.

## References

1. L. Gotta, M. Kulkarni, G. Perfetto, *Towers of quantum many-body scars under stochastic resetting*, arXiv:2603.13165v1 (first publicly posted 2026-03-13), https://arxiv.org/pdf/2603.13165.
2. B. Dakić, V. Vedral, Č. Brukner, *Necessary and sufficient condition for non-zero quantum discord*, Phys. Rev. Lett. 105, 190502 (2010), arXiv:1004.0190, https://arxiv.org/pdf/1004.0190.
3. P. J. P. Lanyon et al., *Generation of quantum discord between ionic qubits via noisy processes*, arXiv:1304.3632, https://arxiv.org/pdf/1304.3632.
4. X. Wu, T. Zhou, *Geometric discord: A resource for increments of quantum key generation through twirling*, Scientific Reports 5, 13365 (2015), https://www.nature.com/articles/srep13365.
5. M. Piani, *Problem with geometric discord*, Phys. Rev. A 86, 034101 (2012), https://doi.org/10.1103/PhysRevA.86.034101.
