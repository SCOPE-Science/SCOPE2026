# A conserved-mass zero mode corrects endemic-equilibrium stability in a cognitive SIS model
## Finding
Liu, Wang, and Zhang study two quasilinear SIS diffusion systems with conserved total population
\[
\int_\Omega (S(x,t)+I(x,t))\,dx=N.
\]
For spatially homogeneous transmission and recovery, or the corresponding constant-ratio case described in the article, they identify the constant endemic equilibrium
\[
(\widehat S,\widehat I)
=
\left(
\frac{N}{\mathcal R_0|\Omega|},
\left(1-\frac1{\mathcal R_0}\right)\frac{N}{|\Omega|}
\right),
\qquad
\mathcal R_0=\frac{\beta}{\gamma}>1.
\]

The full Neumann linearization at this equilibrium has a simple zero eigenvalue. The proof of Lemma 4.1 instead states that both coefficients of its modal quadratic are positive for every Neumann mode and concludes local asymptotic stability. That positivity assertion fails for the constant mode.

Writing
\[
q=1-\frac1{\mathcal R_0},
\qquad
f_*=f(\beta,\widehat S,\widehat I)>0,
\qquad
g_*=g(\gamma)>0,
\]
the modal matrix is
\[
M_l=
\begin{pmatrix}
-f_*l^2-\beta q^2 & \gamma q\\
\beta q^2 & -g_*l^2-\gamma q
\end{pmatrix}.
\]
For \(l=0\),
\[
\sigma(M_0)=\{0,-\gamma(\mathcal R_0-1)\}.
\]
The zero eigenvector is proportional to
\[
(1,\mathcal R_0-1).
\]

This is not an accidental degeneracy. Varying the conserved mass produces the exact equilibrium family
\[
E_M=
\left(
\frac{M}{\mathcal R_0|\Omega|},
\left(1-\frac1{\mathcal R_0}\right)\frac{M}{|\Omega|}
\right),
\qquad M>0,
\]
and the zero eigenvector is tangent to this family. Hence a single equilibrium \(E_N\) cannot be locally asymptotically stable in an ambient function space that permits perturbations changing total mass.

The correct stability statement is relative to the invariant mass leaf
\[
\int_\Omega(S+I)\,dx=N.
\]
On that codimension-one manifold, the neutral mass-changing direction is excluded, while the remaining homogeneous direction and every nonconstant Neumann mode are linearly damped.

## Assumptions and scope
The claim concerns the constant endemic equilibrium and linearization printed in Section 4 of the motivating article. The source assumes a bounded smooth spatial domain with zero-flux boundary conditions and positive diffusion functions. For the spectral statement here, \(\Omega\) is taken to be connected so that the Neumann zero mode is simple.

The endemic regime satisfies
\[
\mathcal R_0>1.
\]
For the Fickian model, the source imposes the constant-ratio condition needed for its constant equilibrium; for the Fokker–Planck model it assumes spatially constant \(\beta\) and \(\gamma\). The calculation uses the source's displayed linearized system and therefore applies to both cases covered by Lemma 4.1.

The result is a correction of the stability domain, not a rejection of the fixed-mass threshold dynamics. It does not claim instability within the mass-conserving state space.

## Proof
Set
\[
q=1-\frac1{\mathcal R_0}>0.
\]
For a Neumann Laplacian mode with wave number \(l\ge0\), the source gives
\[
M_l=
\begin{pmatrix}
-f_*l^2-\beta q^2 & \gamma q\\
\beta q^2 & -g_*l^2-\gamma q
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\lambda^2+A_l\lambda+B_l,
\]
where
\[
A_l=(f_*+g_*)l^2+\beta q^2+\gamma q
\]
and
\[
B_l=f_*g_*l^4+
\bigl(f_*\gamma q+g_*\beta q^2\bigr)l^2.
\]

For every \(l>0\), all displayed factors are positive, so
\[
A_l>0,\qquad B_l>0.
\]
The two roots therefore have negative real part.

For the constant mode \(l=0\),
\[
B_0=0,
\]
so the characteristic polynomial factors as
\[
\lambda\left(\lambda+\beta q^2+\gamma q\right).
\]
Because
\[
\beta=\gamma\mathcal R_0,
\]
we have
\[
\beta q^2+\gamma q
=
\gamma\bigl(\mathcal R_0q^2+q\bigr)
=
\gamma(\mathcal R_0-1).
\]
Thus
\[
\sigma(M_0)=\{0,-\gamma(\mathcal R_0-1)\}.
\]

Moreover,
\[
M_0
\begin{pmatrix}
1\\
\mathcal R_0-1
\end{pmatrix}
=0,
\]
whereas
\[
M_0
\begin{pmatrix}
1\\
-1
\end{pmatrix}
=
-\gamma(\mathcal R_0-1)
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
\]
The first vector changes the total population, while the second has zero total perturbation.

The nonlinear explanation is exact. For every \(M>0\),
\[
E_M=
\left(
\frac{M}{\mathcal R_0|\Omega|},
q\frac{M}{|\Omega|}
\right)
\]
is a constant endemic equilibrium, and
\[
\frac{dE_M}{dM}
=
\frac1{\mathcal R_0|\Omega|}
\begin{pmatrix}
1\\
\mathcal R_0-1
\end{pmatrix}.
\]
Hence the zero mode is tangent to the equilibrium family created by conservation of
\[
\int_\Omega(S+I)\,dx.
\]

If \(M\ne N\) is arbitrarily close to \(N\), the initial state \(E_M\) is arbitrarily close to \(E_N\) but remains equal to \(E_M\) for all time. Therefore it cannot converge to \(E_N\). This rules out local asymptotic stability of \(E_N\) in the unrestricted ambient phase space.

On the invariant leaf with fixed mass \(N\), perturbations satisfy
\[
\int_\Omega(\delta S+\delta I)\,dx=0.
\]
The neutral eigenvector is excluded, the homogeneous tangent direction has eigenvalue
\[
-\gamma(\mathcal R_0-1)<0,
\]
and all \(l>0\) modes have eigenvalues with negative real part. This yields the corrected transverse spectral statement.

## Verification
The bundled script `verification/verify.py` checks symbolically, using exact rational arithmetic over a finite family of positive rational parameter values, that:

1. the zero-mode determinant vanishes;
2. the zero-mode trace equals \(-\gamma(\mathcal R_0-1)\);
3. the vectors \((1,\mathcal R_0-1)\) and \((1,-1)\) are respectively the neutral and stable homogeneous eigenvectors;
4. the source's coefficient \(B_l\) is strictly positive for positive modes but equals zero at \(l=0\).

The general identities are proved algebraically above; the script is a replay check rather than the proof itself.

## Relationship to prior work
The motivating article explicitly proves conservation of total population and defines its constant endemic equilibrium using that initial mass. In the proof of Lemma 4.1 it nevertheless states that both coefficients of the modal characteristic polynomial are positive for every Neumann mode \(l\ge0\). Its own formula shows that the constant term is proportional to \(l^2\) and therefore vanishes at \(l=0\).

Classical SIS reaction-diffusion literature, including Allen et al. (2008), studies threshold dynamics under conserved population, and Li, Peng, and Xiang (2020) studies related constant-total-population cross-diffusion models. These works establish the broader fixed-mass setting. They are not used here to claim a source-specific error; the correction follows directly from the 2026 article's conservation law, equilibrium formula, and displayed characteristic polynomial.

Searches using the exact DOI together with aliases for conserved mass, zero Neumann mode, neutral eigenvalue, endemic equilibrium, and local asymptotic stability did not locate an indexed source-specific correction.

## Limitations
The result does not invalidate convergence results formulated on a fixed-total-population state space. It makes that state-space restriction explicit and corrects the full modal spectrum.

The proof does not establish a nonlinear orbital-stability theorem for the entire equilibrium family. It establishes the exact equilibrium family, the structural neutral direction, and exponential damping of the remaining linear modes under the hypotheses used by the source.

If the spatial domain is disconnected, the Neumann zero eigenspace has higher multiplicity and the neutral-mode bookkeeping requires componentwise refinement.

## References
1. G. Liu, H. Wang, X. Zhang, “Cognitive diffusion of susceptibles driven by new infection cases in SIS epidemic models: frequency-dependent incidence,” European Journal of Applied Mathematics (2026), 1–29. DOI: 10.1017/S0956792526100448.
2. L. J. S. Allen, B. M. Bolker, Y. Lou, A. L. Nevai, “Asymptotic profiles of the steady states for an SIS epidemic reaction-diffusion model,” Discrete and Continuous Dynamical Systems 21 (2008), 1–20. DOI: 10.3934/dcds.2008.21.1.
3. H. Li, R. Peng, T. Xiang, “Dynamics and asymptotic profiles of endemic equilibrium for two frequency-dependent SIS epidemic models with cross-diffusion,” European Journal of Applied Mathematics 31 (2020), 26–56. DOI: 10.1017/S0956792518000463.
