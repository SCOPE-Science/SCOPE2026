# Exact flux optimization of mean capture time on even quantum rings

## Finding

For every even integer \(n=2m\ge4\), a homogeneous nearest-neighbor quantum ring carrying a total magnetic phase \(\phi\) and a single positive-rate local absorber has the following exact mean absorption time from a maximally mixed initial excitation. If \(J>0\), \(\kappa>0\), and \(\phi\notin\pi\mathbb Z\), then eventual absorption is certain and

\[
T_n(\kappa,\phi)=\frac{n}{\kappa}+\frac{\kappa}{32J^2}\left[\frac{m^2-1}{3\sin^2(\phi/2)}+\frac{m^2}{\cos^2(\phi/2)}\right].
\]

Put \(a=(m^2-1)/3\) and \(b=m^2\). For **every fixed** \(\kappa,J>0\), the only globally optimal fluxes modulo \(2\pi\) are \(\phi=\phi_m\) and \(\phi=2\pi-\phi_m\), where

\[
\phi_m=2\arctan\left(\frac{m^2-1}{3m^2}\right)^{1/4},\qquad 0<\phi_m<\frac{\pi}{2}.
\]

The optimal fixed-rate value and its strictly positive advantage over the quarter-flux choice are

\[
T_n(\kappa,\phi_m)=\frac n\kappa+\frac{\kappa}{32J^2}(\sqrt a+\sqrt b)^2,\qquad
T_n(\kappa,\pi/2)-T_n(\kappa,\phi_m)=\frac{\kappa}{32J^2}(\sqrt b-\sqrt a)^2.
\]

If the absorber rate is also optimized, the unique optimal rate for either optimal flux is

\[
\kappa_m^*=\frac{\sqrt{32n}\,J}{\sqrt a+\sqrt b},\qquad
T_n^*=\frac{\sqrt{n/8}}{J}(\sqrt a+\sqrt b).
\]

The optimal reduced flux \(\phi_m/\pi\) increases strictly with \(m\) and tends to \(2\arctan(3^{-1/4})/\pi\), approximately \(0.4136540654\), not \(1/2\). The ratio of the jointly optimized time at this flux to the best time obtainable at quarter flux tends to \(\cos(\pi/12)\), approximately \(0.9659258263\).

At the exceptional exact phases \(\phi=0\) and \(\phi=\pi\) modulo \(2\pi\), the capture probabilities from the maximally mixed state are respectively \((m+1)/(2m)\) and \(m/(2m)=1/2\). The *unconditional* mean absorption time is infinite at these phases because a positive dark fraction remains. As nonexceptional phases approach them, the leading fixed-rate divergences are

\[
T_n(\kappa,\phi)\sim\frac{\kappa(m^2-1)}{24J^2\phi^2}\quad(\phi\to0),\qquad
T_n(\kappa,\phi)\sim\frac{\kappa m^2}{8J^2(\pi-\phi)^2}\quad(\phi\to\pi).
\]

These statements apply only to even ring sizes; no odd-ring mean-time formula or optimizer is claimed here.

## Assumptions and scope

The Hilbert space is \(\mathbb C^n\) with site basis \(\{|r\rangle:r\in\mathbb Z/n\mathbb Z\}\). The number of vertices is even, \(n=2m\ge4\). The coherent Hamiltonian and the trace-decreasing single-excitation evolution are

\[
H_\phi=J\sum_{r\in\mathbb Z/n\mathbb Z}
\left(e^{i\phi/n}|r+1\rangle\langle r|+e^{-i\phi/n}|r\rangle\langle r+1|\right),
\]
\[
\dot\rho=-i[H_\phi,\rho]-\frac\kappa2\{|0\rangle\langle0|,\rho\},\qquad \rho(0)=I_n/n,
\]

with \(J>0\), \(\kappa>0\), \(\phi\in\mathbb R/(2\pi\mathbb Z)\). Here \(\kappa\) is the *population* loss rate, not the imaginary onsite Hamiltonian coefficient (which is \(\kappa/2\)). Define survival \(s(t)=\operatorname{tr}\rho(t)\); when capture is certain, the mean absorption time is \(T=\int_0^\infty s(t)\,dt\). At fluxes with a dark subspace this integral is infinite; finite conditional-on-capture means are not part of the assertion.

The Fourier eigenvalues are \(E_k=2J\cos((2\pi k+\phi)/n)\), \(k\in\mathbb Z/n\mathbb Z\), and the squared absorber overlap of every Fourier mode is \(1/n\).

## Proof

**1. Full capture away from integer half-flux.** If \(E_j=E_k\) for distinct indices modulo \(n\), the cosine equality gives \(j+k+\phi/\pi\in n\mathbb Z\). Hence a degeneracy requires \(\phi\in\pi\mathbb Z\). Away from those phases, the spectrum is simple. Each Fourier eigenvector has nonzero overlap with \(|0\rangle\), so the absorber-cyclic subspace contains all \(n\) eigenvectors. Equivalently there is no nonzero eigenvector of \(H_\phi\) annihilated by the absorber. Any eigenvalue of \(-iH_\phi-\kappa|0\rangle\langle0|/2\) on the imaginary axis would have an eigenvector annihilated by the absorber, which is impossible. Thus all modes decay and \(T\) is finite.

**2. Integrated-density identity.** For any finite Hermitian Hamiltonian with simple energies \(E_j\) and a rank-one absorber having all spectral overlaps equal in magnitude to \(1/\sqrt n\), choose phases so that the absorber's spectral vector has all entries \(1/\sqrt n\). Write \(X=\int_0^\infty\rho(t)\,dt\), which solves

\[
i[H,X]+\frac\kappa2\{P,X\}=I_n/n,\qquad P=\frac1n\mathbf1\mathbf1^{\mathsf T}.
\]

Set \(r_j=\sum_\ell X_{j\ell}\). The diagonal equations show \(\operatorname{Re}r_j=1/\kappa\). Let \(z_j=\operatorname{Im}r_j\), and \(\Delta_{jk}=E_j-E_k\). For \(j\ne k\), the off-diagonal equations give

\[
X_{jk}=\frac{i}{n\Delta_{jk}}-\frac\kappa{2n\Delta_{jk}}(z_j-z_k),\qquad
z_j=\frac1n\sum_{k\ne j}\frac1{\Delta_{jk}}.
\]

Because \(X_{jj}\) is real, the row-sum identities give

\[
X_{jj}=\frac1\kappa+\frac\kappa{2n}\sum_{k\ne j}\frac{z_j-z_k}{\Delta_{jk}},\qquad
\operatorname{tr}X=\frac n\kappa+\kappa\sum_j z_j^2.
\]

In \(\sum_j z_j^2\), the terms involving three distinct energies cancel by the exact identity

\[
\frac1{(x-y)(x-z)}+\frac1{(y-x)(y-z)}+\frac1{(z-x)(z-y)}=0.
\]

The two-index terms survive twice. Consequently,

\[
T=\frac n\kappa+\frac{2\kappa}{n^2}\sum_{j<k}\frac1{(E_j-E_k)^2}.
\]

This general inverse-gap relation is a prerequisite, not the novelty asserted here; the new step is the all-even-cycle evaluation and optimization of its spectral sum.

**3. Even-cycle spectral-sum factorization.** Write \(n=2m\). Since

\[
(E_j-E_k)^2=16J^2\sin^2\!\left(\frac{\pi(j-k)}n\right)
\sin^2\!\left(\frac{\pi(j+k)+\phi}{n}\right),
\]

put \(d=j-k\) and \(s=j+k\) modulo \(2m\). These indices satisfy \(d\equiv s\pmod2\). For each parity-compatible pair \((d,s)\) there are exactly two ordered solutions \((j,k)\), and passing to unordered pairs divides by two. Hence, with \(Q=\sum_{j<k}(E_j-E_k)^{-2}\),

\[
16J^2Q=\left[\sum_{r=1}^{m-1}\csc^2\!\left(\frac{\pi r}{m}\right)\right]
\left[\sum_{r=0}^{m-1}\csc^2\!\left(\frac{\pi r}{m}+\frac\phi{2m}\right)\right]
+\left[\sum_{r=0}^{m-1}\csc^2\!\left(\frac{(2r+1)\pi}{2m}\right)\right]
\left[\sum_{r=0}^{m-1}\csc^2\!\left(\frac{(2r+1)\pi+\phi}{2m}\right)\right].
\]

The cotangent multiplication identity, differentiated once, gives

\[
\sum_{r=0}^{m-1}\csc^2(x+r\pi/m)=m^2\csc^2(mx).
\]

Its expansion at \(x=0\) also yields \(\sum_{r=1}^{m-1}\csc^2(\pi r/m)=(m^2-1)/3\). Thus the four bracketed sums, in order, are \((m^2-1)/3\), \(m^2\csc^2(\phi/2)\), \(m^2\), and \(m^2\sec^2(\phi/2)\). Therefore

\[
Q=\frac{m^2}{16J^2}\left[\frac{m^2-1}{3\sin^2(\phi/2)}+\frac{m^2}{\cos^2(\phi/2)}\right].
\]

Substitution into the inverse-gap relation proves the stated mean-time formula.

**4. Unique global flux and rate optima.** On \(0<\phi<\pi\), set \(x=\sin^2(\phi/2)\in(0,1)\). The flux-dependent objective is \(f(x)=a/x+b/(1-x)\), strictly convex because \(f''(x)=2a/x^3+2b/(1-x)^3>0\). Its unique critical point is \(x_* =\sqrt a/(\sqrt a+\sqrt b)\); this yields the stated \(\phi_m\) and minimal value \((\sqrt a+\sqrt b)^2\). Reflection \(\phi\mapsto2\pi-\phi\) supplies the only other optimizer modulo \(2\pi\). Since \(b>a>0\), neither optimizer is quarter flux. The reduction to \(n/\kappa+C\kappa\), \(C>0\), proves the unique rate optimizer and joint minimum by strict arithmetic-geometric mean. The quarter-flux gain follows by subtracting \((\sqrt a+\sqrt b)^2\) from \(2(a+b)\). Monotonicity of \(\phi_m\) follows from monotonicity of \((m^2-1)/m^2\); the limit and time ratio follow directly, using \(\cos(\pi/12)=(1+1/\sqrt3)/\sqrt{8/3}\).

**5. Exceptional-flux boundary and singularity.** At \(\phi=0\) the Fourier energies have exactly \(m+1\) distinct values, and at \(\phi=\pi\) exactly \(m\) values. The site-zero absorber has a nonzero projection onto every distinct energy space, but each space contributes only one accessible direction, giving the stated capture fractions from \(I_n/n\). Positive dark mass remains at each phase and makes the unconditional integral infinite. Expanding the exact nonexceptional formula at either endpoint gives the two different inverse-square coefficients.

## Verification

Run `python check_even_flux.py` with NumPy and SciPy. The script constructs the full complex magnetic Hamiltonian and independently solves its continuous Lyapunov equation; it also sums the Fourier energy gaps directly, compares the closed-form minimizers with numerical bounded optimization, and counts distinct energies at the two exceptional fluxes. The included `CHECK_RESULTS.txt` records 168 direct spectral-gap comparisons, 150 independent full complex Lyapunov comparisons, 14 optimizer checks, and 28 exceptional-energy counts, all passing. The checks are finite tests; the all-size conclusion rests on the exact proof above.

## Relationship to prior work

Continuous quantum-walk hitting-time definitions and symmetry-induced infinite hitting times were studied by Varbanov, Krovi and Brun [1]. The invariant-subspace criterion for trapping efficiency in finite quantum networks is developed by Novo and collaborators [2]. Flux-dependent quantum transport and waiting-time statistics appear in the distinct three-site dephased and lead-coupled models of Engelhardt and Cao [3], and flux-controlled transport through an open, dissipative three-site ring is studied by Gou and collaborators [4]. None of those inspected results gives the exact even-cycle maximally mixed capture-time formula, its non-quarter-flux optimum, or its two inequivalent exceptional-endpoint singularities. An existing general inverse-energy-gap lifetime formula supplies a useful starting identity; this result does **not** assert that the general identity itself is new. The phase-dependent even-cycle evaluation and global optimizer are the assessed contribution.

## Limitations

The theorem assumes a finite homogeneous even cycle, one Markovian local population-loss channel, a maximally mixed one-excitation initial state, and no additional dephasing, disorder or many-particle interactions. It does not determine conditional capture times at exact dark-state fluxes, localized-source optimization, transport through attached leads, or finite-time capture quantiles. It does not claim a new general inverse-gap theorem or an odd-cycle result. Historical priority for the specialized even-cycle optimization is based on the literature actually inspected and is not independently certified.

## References

[1] M. Varbanov, H. Krovi, T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446, initially public 2008-03-24. https://arxiv.org/abs/0803.3446

[2] L. Novo, S. Chakraborty, M. Mohseni, H. Neven, Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209. https://arxiv.org/abs/1412.7209

[3] G. Engelhardt, J. Cao, *Tuning the Aharonov-Bohm effect with dephasing in nonequilibrium transport*, arXiv:1808.03368. https://arxiv.org/abs/1808.03368

[4] W. Gou and collaborators, *Tunable non-reciprocal quantum transport through a dissipative Aharonov-Bohm ring in ultracold atoms*, arXiv:2001.01859. https://arxiv.org/abs/2001.01859
