# Endogenous rate feedback destabilizes a Hurwitz SIR-ID endemic equilibrium

## Finding

For the five-equation SIR-ID model with the two rate-feedback laws used by Breidenich and colleagues, there are **strictly positive parameters and an endemic equilibrium in the interior of both rate-clamping intervals** at which the frozen-rate, three-population Jacobian is Hurwitz, but the Jacobian of the actual five-dimensional dynamics has **exactly two eigenvalues with positive real part**. This establishes that the three-variable local-stability calculation cannot be promoted to an unconditional endemic-stability claim for the five-equation model. It does not establish a Hopf bifurcation or a nonlinear periodic solution.

An exact witness is given below. Every number in the certificate is rational, and the instability is proved by an exact Routh array, not a simulation.

## Assumptions and scope

Let \(S,I,R\) denote susceptible, infected, and recovered populations, and let \(a,b\) denote the auxiliary death and infectivity variables. Put \(N=S+I+R\). Consider the following five ordinary differential equations with positive constants:

\[
\begin{aligned}
\dot S&=P-bIS/N-\mu S+rR,\\
\dot I&=bIS/N-(\mu+a+\sigma)I,\\
\dot R&=\sigma I-(\mu+r)R,\\
\dot a&=\delta^{+}I-\delta^{-}aR,\\
\dot b&=\gamma^{+}I-\gamma^{-}bR.
\end{aligned}
\]

These are the five equations of the source model with its stated simulation feedback functions, restricted to a neighborhood in which the clipping functions \(\Phi_\alpha\) and \(\Phi_\beta\) act as the identity. The equilibrium and a neighborhood of it lie in such an interior region; hence its Jacobian is also the local Jacobian of the original clipped system. No claim is made about arbitrary feedback functions.

Choose

\[
\begin{gathered}
\mu=\frac{2}{25},\quad r=\frac1{10},\quad \sigma=\frac15,\quad
P=\frac{313}{3800},\\
\delta^+=\frac1{45},\quad \delta^-=1,\quad
\gamma^+=\frac{80}{9},\quad \gamma^-=20.
\end{gathered}
\]

The equilibrium is

\[
E=\left(\frac34,\frac9{76},\frac5{38},\frac1{50},\frac25\right)
\quad\text{in the order }(S,I,R,a,b).
\]

Admissible clamping intervals include \(a\in[1/100,1/10]\) and \(b\in[1/5,4/5]\), so the equilibrium lies strictly inside both. At this point \(N=1\) and the frozen-rate reproduction ratio is \(b/(\mu+a+\sigma)=4/3>1\). All population components and parameters are strictly positive.

## Proof

First verify equilibrium exactly. The recovery balance gives
\[
\sigma\frac9{76}=(\mu+r)\frac5{38}=\frac9{380}.
\]
The infectious balance is
\[
\frac25\frac9{76}\frac34=(\mu+a+\sigma)\frac9{76}=\frac{27}{760}.
\]
Moreover, \(P-\mu N-aI=313/3800-2/25-9/3800=0\), which together with the previous balances implies \(\dot S=0\). Both feedback balances hold:
\[
\frac1{45}\frac9{76}=\frac1{50}\frac5{38}=\frac1{380},\qquad
\frac{80}{9}\frac9{76}=20\frac25\frac5{38}=\frac{20}{19}.
\]
Thus all five derivatives vanish and the cutoffs are inactive near \(E\).

Differentiating all five right-hand sides in the state-variable order above gives the exact full Jacobian
\[
J_5=\begin{pmatrix}
-349/3800&-201/760&103/760&0&-27/304\\
9/760&-27/760&-27/760&-9/76&27/304\\
0&1/5&-9/50&0&0\\
0&1/45&-1/50&-5/38&0\\
0&80/9&-8&0&-50/19
\end{pmatrix}.
\]
The upper-left \(3\times3\) block \(J_3\), corresponding to holding death and infectivity rates fixed, has characteristic polynomial
\[
p_3(z)=z^3+\frac{146}{475}z^2+\frac{6921}{190000}z+\frac{2817}{1900000}.
\]
Every nonleading coefficient is positive and \((146/475)(6921/190000)>2817/1900000\). The cubic Routh–Hurwitz criterion therefore makes \(J_3\) Hurwitz.

In contrast, the full characteristic polynomial is
\[
\begin{aligned}
p_5(z)={}&z^5+\frac{2917}{950}z^4+\frac{1606999}{3610000}z^3\\
&+\frac{33399687}{685900000}z^2+\frac{2478983}{274360000}z
+\frac{2817}{5487200}.
\end{aligned}
\]
For a monic quintic with coefficients \((1,c_4,c_3,c_2,c_1,c_0)\), the first three-column Hurwitz determinant is
\[
\Delta_3=c_4c_3c_2-c_4^2c_1-c_2^2+c_4c_0.
\]
Here it equals
\[
\Delta_3=-\frac{11422998795700081}{588073512500000000}<0.
\]
More strongly, exact rational Routh division yields the first-column signs, in descending polynomial order,
\[
(+,+,+,-,+,+).
\]
No first-column entry vanishes; the standard Routh root-count theorem therefore gives **two** roots in the open right half-plane, counted with algebraic multiplicity. Since all coefficients of \(p_5\) are positive, the polynomial has no positive real root; the two unstable roots consequently form a nonreal conjugate pair. The positive real parts make the full endemic equilibrium linearly unstable (and, by the linearization instability theorem, Lyapunov unstable) despite the stability of its frozen-rate population block.

## Verification

The accompanying `verify.py` differentiates the original five right-hand sides symbolically and independently checks the equilibrium, strict cutoff inequalities, both characteristic polynomials, the cubic Hurwitz inequalities, the exact negative determinant, and all six nonzero Routh pivots. Execute it with a Python installation containing SymPy:

```
python verify.py
```

The expected success marker is `VERIFY_OK`. The proof rests on exact rational arithmetic; no floating-point root approximations or finite-time integrations are needed.

## Relationship to prior work

Breidenich and coauthors' SIR-ID work states a five-equation model with endogenous death and infection rates and uses the displayed two rate-feedback laws in its computations. Its endemic-stability and no-Hopf discussion, including Theorem 7 of the 2026 journal version, evaluates a \(3\times3\) Jacobian of the population subsystem with the rates held fixed. The present example instead evaluates the full \(5\times5\) Jacobian, where the rate-to-population and population-to-rate couplings affect eigenvalues. It supplies a source-specific, exact instability witness; it does **not** claim that feedback-induced oscillations are unknown in epidemic modeling generally.

Kuniya and Inaba (2023) analyze Hopf bifurcations in an infection-age structured SIR model; Guan, Kopfová, and Rachinskii (2024) analyze SIRS behavior with a Preisach hysteresis operator. Both motivate examining endogenous epidemic feedback, but neither establishes this five-equation SIR-ID Jacobian certificate. The model-specific conclusion should not be inferred merely from the generic observation that feedback may destabilize otherwise stable systems.

## Limitations

The result is local and concerns a particular, mathematically admissible positive parameter set for the published simulation feedback laws. It says nothing about field-calibrated parameters, all admissible source functions, global attractors, the existence of periodic orbits, or Hopf bifurcation. Complex eigenvalues with positive real part show oscillatory **linear instability**, not a periodic orbit. The source's published stable trajectories for its own parameter choices are not disproved. The example illustrates a stability mechanism that must be included in a five-state assessment.

## References

1. E. Breidenich, J. Cooper, Q. Huang, C. Wagner, S. Kovács, and M. Shillor, *SIR Model with Dependent Infectivity and Death Rates*, **Axioms** 15 (2026), 603. https://doi.org/10.3390/axioms15080603. Relevant material: Remark 1; Model 1; Sections 4.5, 5 and 7.
2. E. Breidenich, J. Cooper, Q. Huang, M. Shillor, and C. Wagner, *SIR Model with Dependent Infectivity and Death Rates*, preprint posted 15 April 2026, https://doi.org/10.20944/preprints202604.1114.v1. The preprint provides the earliest verified public date and primary MSC 92C60.
3. T. Kuniya and H. Inaba, *Hopf bifurcation in a chronological age-structured SIR epidemic model with age-dependent infectivity*, Mathematical Biosciences and Engineering 20 (2023), 13036–13060. https://doi.org/10.3934/mbe.2023581.
4. R. Guan, J. Kopfová, and D. Rachinskii, *Global Stability of SIR Model with Heterogeneous Transmission Rate Modeled by the Preisach Operator*, SIAM Journal on Applied Dynamical Systems 23 (2024), 1199–1241. https://doi.org/10.1137/22M154274X.
