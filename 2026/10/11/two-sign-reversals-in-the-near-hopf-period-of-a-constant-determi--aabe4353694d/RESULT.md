# Two sign reversals in the near-Hopf period of a constant-determinant Selkov oscillator

## Finding

Consider the polynomial glycolysis oscillator
\[
\dot x=-x+ay+x^2y,\qquad \dot y=b-ay-x^2y.
\]
For every fixed \(K\in(0,1)\), set
\[
a=\frac{K(1-K-\mu)}2,\qquad
b=\sqrt{\frac{K(1+K+\mu)}2},\qquad 0<\mu<1-K.
\]
The unique equilibrium \(E=(b,b/K)\) has Jacobian determinant exactly \(K\), independent of \(\mu\), and trace exactly \(\mu\). For each fixed \(K\), there exists \(\varepsilon_K>0\) such that for every \(0<\mu<\varepsilon_K\), the equilibrium is unstable and a locally unique, orbitally asymptotically stable, nonconstant periodic orbit bifurcates from it. Its least period satisfies
\[
\boxed{T_K(\mu)=\frac{2\pi}{\sqrt K}\left[1+
\frac{(2K-1)(4K^2+3K-2)}{6K(1+2K-2K^2)}\,\mu+O_K(\mu^2)\right].}
\]
Writing \(K_*=(\sqrt{41}-3)/8\), the right derivative of the branch period at \(\mu=0\) is positive precisely when \(0<K<K_*\) or \(1/2<K<1\), and negative precisely when \(K_*<K<1/2\). It vanishes precisely at \(K=K_*\) and \(K=1/2\). Thus preserving the small-oscillation frequency does not preserve the leading nonlinear period shift; the shift reverses sign twice within the positive-kinetic-parameter Hopf family.

## Assumptions and scope

All states and parameters are real. \(K\) is fixed in the open interval \((0,1)\); all asymptotics are for \(\mu\downarrow0\) at that fixed \(K\), with \(a>0\) and \(b>0\) as prescribed above. The branch is the small-amplitude periodic orbit in a sufficiently small neighborhood of its equilibrium; no assertion of global uniqueness of cycles, global attraction, or finite-\(\mu\) monotonicity is made. \(O_K(\mu^2)\) means the remainder is bounded in absolute value by a constant depending on \(K\) times \(\mu^2\) for sufficiently small positive \(\mu\).

The date attached to the historical Sel'kov source refers to the founding glycolysis model. That paper uses a different explicit choice of state variables and rate law. The polynomial form displayed here is explicitly documented in the 1994 textbook of Strogatz and in later studies, so it must not be identified term-by-term with the differential equations printed in the 1968 source.

## Proof

**Exact equilibrium and linearization.** Summing the differential equations yields \(\dot x+\dot y=b-x\). Hence every equilibrium has \(x=b\), and the second equation then forces \(y=b/(a+b^2)=b/K\). Direct differentiation of the vector field gives, at this equilibrium,
\[
\det DF(E)=a+b^2=K,\qquad
\operatorname{tr}DF(E)=-1-K+\frac{2b^2}{K}=\mu.
\]
At \(\mu=0\) the simple characteristic roots are \(\pm i\sqrt K\), and the real part crosses with derivative \(1/2\). Consequently a Hopf bifurcation is possible; determining the cubic amplitude coefficient is essential for its direction and the period shift.

**Exact scalar reduction.** Define \(q=x+y-b-b/K\) and \(v=b-x\). Then \(\dot q=v\) and an algebraic expansion of \(-\dot x\) gives the exact equation
\[
\ddot q+Kq=\mu\dot q+2bq\dot q+d(\dot q)^2-q(\dot q)^2-(\dot q)^3,
\qquad d=2b-\frac bK.
\]
No truncation occurs in this reduction. At the Hopf point write
\[
\omega=\sqrt K,\quad b_0=\sqrt{K(1+K)/2},\quad d_0=b_0(2K-1)/K.
\]

**Third-order solvability.** Let \(\epsilon>0\) be the first cosine Fourier amplitude of \(q\), with time origin chosen so the first sine Fourier coefficient is zero. The analytic Poincaré–Lindstedt equations near the nondegenerate Hopf point can be solved with
\[
\theta=\Omega t,\quad q=\epsilon Q_1(\theta)+\epsilon^2Q_2(\theta)+O(\epsilon^3),\quad
\mu=\mu_2\epsilon^2+O(\epsilon^4),\quad
\Omega=\omega+\nu_2\epsilon^2+O(\epsilon^4),
\]
where the equalities for \(\mu\) and \(\Omega\) hold along the nontrivial branch. The leading equation gives \(Q_1(\theta)=\cos\theta\). The nonresonant order-two equation gives exactly
\[
Q_2(\theta)=\frac{d_0}{2}+\frac{d_0}{6}\cos 2\theta
+\frac{b_0}{3\omega}\sin 2\theta.
\]
At order three, the nonparametric forcing is
\[
R=2b_0\omega(Q_1Q_2'+Q_2Q_1')+2d_0\omega^2Q_1'Q_2'
-\omega^2Q_1(Q_1')^2-\omega^3(Q_1')^3,
\]
with primes denoting derivatives with respect to \(\theta\). The resonant Fourier coefficients are computed directly from
\[
C=\frac1\pi\int_0^{2\pi}R\cos\theta\,d\theta,
\qquad S=\frac1\pi\int_0^{2\pi}R\sin\theta\,d\theta.
\]
Writing temporarily \(B=b_0\), \(D=d_0\), and \(w=\omega\), elementary trigonometric integration gives
\[
C=\frac{4B^2+4D^2w^2-3w^2}{12},\qquad
S=-\frac{w(2BD-3w^2)}4.
\]
The order-three cosine and sine solvability conditions are respectively \(-2\omega\nu_2=C\) and \(\mu_2\omega=S\). Substituting the Hopf-point parameters yields
\[
\boxed{\mu_2=\frac{1+2K-2K^2}{4}>0},\qquad
\boxed{\nu_2=-\frac{(2K-1)(4K^2+3K-2)}{24\sqrt K}}.
\]
The strict positivity of \(\mu_2\) on \((0,1)\), together with the transverse eigenvalue crossing, proves that the Hopf bifurcation is nondegenerate and supercritical, with a stable small cycle for positive \(\mu\). This conclusion is also obtained from the leading radial equation \(\dot\epsilon=(\mu\epsilon-\mu_2\epsilon^3)/2+\cdots\); no numerical orbit search is used to infer existence.

**Physical period and its sign.** Dividing the frequency expansion by the amplitude relation gives
\[
\Omega_K(\mu)=\sqrt K-\frac{(2K-1)(4K^2+3K-2)}{6\sqrt K(1+2K-2K^2)}\mu+O_K(\mu^2).
\]
The least period is \(2\pi/\Omega_K(\mu)\), proving the claimed expansion. Its first-order coefficient has the sign of \((2K-1)(4K^2+3K-2)\), since every other factor is strictly positive for \(0<K<1\). The quadratic \(4K^2+3K-2\) has exactly one zero in this interval, \(K_*=(\sqrt{41}-3)/8\), which lies strictly below \(1/2\). The two factors supply the stated sign intervals and precisely two vanishing locations. At those two points the theorem asserts only that the linear correction is zero; it does not assert exact isochrony or determine the quadratic correction.

## Verification

The standalone `checker.py` reproduces the Jacobian determinant and trace, the exact oscillator conjugacy, all four resonant Fourier coefficient identities, the first-order period coefficient, and the two critical roots using symbolic arithmetic in SymPy. Run `python checker.py` from the directory containing this result; successful execution prints `VERIFY_OK`. The program checks finite algebraic identities, not the validity of the Hopf theorem in general. The mathematical argument above supplies the nondegeneracy, branch existence, stability, and scope. Independent numerical shooting was used as an exploratory cross-check, not as evidence for existence or uniqueness.

## Relationship to prior work

Sel'kov (1968) initiated the glycolysis model family; the printed vector field of that paper is not literally the polynomial vector field above. Strogatz (1994), Examples 7.3.2–7.3.3, treats exactly this polynomial system, gives its equilibrium Jacobian and constructs a trapping region/periodic-orbit existence criterion, but does not calculate the constant-determinant near-Hopf nonlinear period derivative. Artés, Llibre and Valls (2018), Theorem 2 and Section 3, treat the same polynomial system after rescaling, analyzing phase portraits and Hopf bifurcation rather than a parameter-uniform exact period response. Al Noufaey (2021), Section 6, develops Lindstedt–Poincaré expansions for Galerkin approximations to the related Selkov–Schnakenberg reaction–diffusion system, with parameter-dependent numerical frequency corrections; the two exact neutral-sensitivity parameters and the determinant-constrained analytic coefficient here are not stated there. Llibre and Nabavi (2022) analyze phase portraits of the same equations; their accessible abstract and figures do not assert this coefficient or its two sign reversals, but a complete comparison with their inaccessible manuscript remains a residual priority risk. Brechmann and Rendall (2018/2019) study a different Selkov normalization with a different polynomial vector field, so its stability results do not imply the present coefficient.

## Limitations

The expansion is asymptotic with \(K\) fixed strictly between zero and one and does not give a uniform error bound as \(K\) approaches either endpoint. The vanishing first-order terms at the two special \(K\) values do not imply constant period. No global phase portrait, higher periodic branch, chaotic behavior, or experimental fitting is claimed. The date of the 1968 founding paper is represented by a bibliographic date-only catalog entry, not an independently established day of first dissemination of the later polynomial normalization. Priority is conditional on the inspected public literature; not every equivalent period-function computation is searchable.

## References

- E. E. Sel'kov, *Self-Oscillations in Glycolysis 1. A Simple Kinetic Model*, European Journal of Biochemistry 4 (1968), 79–86. DOI: 10.1111/j.1432-1033.1968.tb00175.x. Historical model, distinct printed rate law.
- S. H. Strogatz, *Nonlinear Dynamics and Chaos*, Addison-Wesley (1994), pp. 205–209. Polynomial system and basic periodic-orbit existence argument.
- J. C. Artés, J. Llibre, and C. Valls, *Dynamics of the Higgins–Selkov and Selkov systems*, Chaos, Solitons & Fractals 114 (2018), 145–150. DOI: 10.1016/j.chaos.2018.07.007.
- K. S. Al Noufaey, *Stability analysis for Selkov-Schnakenberg reaction-diffusion system*, Open Mathematics 19 (2021), 46–62. DOI: 10.1515/math-2021-0008.
- J. Llibre and A. Nabavi, *Phase portraits of the Selkov model in the Poincaré disc*, Discrete and Continuous Dynamical Systems B 27 (2022), 7607–7623. DOI: 10.3934/dcdsb.2022056.
- P. Brechmann and A. D. Rendall, *Dynamics of the Selkov oscillator*, Mathematical Biosciences 306 (2018), 152–159. arXiv:1803.10579. Different vector field.
