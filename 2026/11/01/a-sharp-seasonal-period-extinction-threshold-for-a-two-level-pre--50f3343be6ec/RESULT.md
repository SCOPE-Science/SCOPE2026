# A sharp seasonal-period extinction threshold for a two-level predator–prey flow

## Finding

A two-level carrying capacity produces **one and only one** transition in predator invasion as the environmental period increases, provided the harmonic mean capacity is below the predator's threshold and the arithmetic mean exceeds it. In the extinction regime there is convergence from **every** positive initial population, not merely local stability.

Consider
\[
\dot a=\lambda a(b-1),\qquad
\dot b=b\left(1-\frac{a+b}{K(t)}\right)-\lambda ab,
\]
with \(\lambda>0\), and \(K(t)=H\) for \(0\le t<T/2\) and \(K(t)=L\) for \(T/2\le t<T\), repeated with period \(T>0\), where \(H>L>0\). Put
\[
\epsilon=\frac{H-L}{H+L},\quad
A=\frac{H+L}{2},\quad B=\frac{2HL}{H+L}.
\]
On \(a=0\) the unique positive periodic prey orbit \(b_T\) has exact time mean
\[
 m(T)=\frac1T\int_0^T b_T(t)\,dt
 =A-\frac{2(H-L)}T\operatorname{artanh}\left(\epsilon\tanh\frac T4\right).
\]
For every \(T>0\), \(B<m(T)<A\), and \(m'(T)>0\). Therefore:

1. If \(B<1<A\), exactly one \(T_*>0\) solves \(m(T_*)=1\). The predator-free periodic orbit is locally exponentially stable for \(0<T<T_*\), has a transverse multiplier one at \(T=T_*\), and is transversely unstable for \(T>T_*\).
2. If \(A\le1\), it is locally exponentially stable for every finite \(T>0\).
3. If \(B\ge1\), it is transversely unstable for every finite \(T>0\).

Moreover, in **every** parameter regime where \(m(T)<1\), for every finite \(a(0)\ge0\) and \(b(0)>0\), the predator obeys \(a(t)\to0\) exponentially and the prey approaches the appropriate phase of \(b_T\). At \(m(T)>1\), the theorem asserts transverse linear invasion, not uniform persistence or existence of a coexistence attractor.

The transverse and prey Floquet multipliers, respectively, are **exactly**
\[
 \rho_a=e^{\lambda T(m(T)-1)},\qquad \rho_b=e^{-T}.
\]
The crossing in case 1 is transverse because \(d\log\rho_a/dT=\lambda T_*m'(T_*)>0\) at \(T_*\).

## Assumptions and scope

The equations are deterministic, nonspatial ordinary differential equations with one fixed positive predation coefficient. Population states satisfy \(a\ge0\), \(b>0\). Environmental switching is prescribed and has **equal-duration seasons**, with high capacity first. At switching instants the vector field changes but both populations remain continuous. Periodic solutions and stability are understood for the time-periodic flow, with Floquet multipliers for the \(T\)-return map at phase zero. The parameter \(T\) denotes the full environmental period; it is not a half-season duration.

## Proof

**1. Unique positive boundary cycle.** On \(a=0\), the prey solves \(\dot b=b(1-b/K(t))\). Set \(y=1/b\). Then
\[
 \dot y=-y+K(t)^{-1}.
\]
For a constant capacity \(k\) over time \(s\), \(y(s)=k^{-1}+[y(0)-k^{-1}]e^{-s}\). The full-period map of \(y\) is an affine contraction of slope \(e^{-T}\); it has precisely one positive fixed point. With \(q=e^{-T/2}\), the inverse prey levels at the beginning and midpoint of its orbit are
\[
 y_0=\frac{L^{-1}+qH^{-1}}{1+q},\qquad
 y_1=\frac{H^{-1}+qL^{-1}}{1+q}.
\]
The displayed phase-dependent inverse-linear flow thus constructs \(b_T\) explicitly. Because \(y_0,y_1>0\), the orbit is strictly positive.

**2. Exact mean.** On an interval with capacity \(k\), \(d\log b/dt=1-b/k\), hence
\[
\int_{t_0}^{t_1}b(t)\,dt
=k[(t_1-t_0)+\log(y(t_1)/y(t_0))].
\]
Adding the two seasons yields
\[
 Tm(T)=AT+(H-L)\log\frac{y_1}{y_0}.
\]
Since \(y_0/y_1=(1+\epsilon\tanh(T/4))/(1-\epsilon\tanh(T/4))\), this is the asserted formula.

**3. Strict period monotonicity and exact endpoints.** Write \(z=T/4\), \(g(z)=\operatorname{artanh}(\epsilon\tanh z)\). Direct differentiation gives
\[
 g'(z)=\frac{\epsilon\operatorname{sech}^{2}z}{1-\epsilon^{2}\tanh^{2}z},\qquad
 g''(z)=-\frac{2\epsilon(1-\epsilon^{2})\tanh z\operatorname{sech}^{2}z}{(1-\epsilon^{2}\tanh^{2}z)^2}<0\quad(z>0).
\]
As \(g(0)=0\), strict concavity makes \(g(z)/z\) strictly decrease, hence \(m(T)=A-(H-L)g(T/4)/(2(T/4))\) strictly increase. The limits \(g(z)/z\to\epsilon\) at zero and \(g(z)/z\to0\) at infinity give \(\lim_{T\downarrow0}m(T)=B\) and \(\lim_{T\to\infty}m(T)=A\). Strict inequalities hold at finite positive periods. The more precise endpoints are
\[
 m(T)=B+\frac{(H-L)\epsilon(1-\epsilon^2)}{96}T^2+O(T^4),\quad T\downarrow0,
\]
\[
 m(T)=A-\frac{2(H-L)\operatorname{artanh}\epsilon}{T}
+O(e^{-T/2}/T),\quad T\to\infty.
\]

**4. Floquet multipliers and the unique threshold.** Linearizing at \((a,b)=(0,b_T(t))\), in the coordinate order \((a,b)\), gives the lower-triangular time-dependent matrix
\[
\begin{pmatrix}
\lambda(b_T-1)&0\\
-b_T(1/K+\lambda)&1-2b_T/K
\end{pmatrix}.
\]
Integrating the diagonal coefficients produces \(\rho_a=e^{\lambda T(m(T)-1)}\) and \(\rho_b=e^{\int_0^T (1-2b_T/K)dt}\). The periodic logistic identity \(\int_0^T b_T/K\,dt=T\) shows \(\rho_b=e^{-T}\). As \(m(T)\) is strictly increasing between \(B\) and \(A\), the three cases and unique transverse crossing follow by the intermediate value theorem. For \(m(T)<1\) both multipliers have modulus below one; for \(m(T)>1\) the predator multiplier exceeds one. The boundary \(m(T)=1\) is nonhyperbolic, and no nonlinear conclusion there is used.

**5. Global predator extinction below threshold.** For any initial \(a(0)\ge0,b(0)>0\), let \(z\) solve the predator-free logistic equation with \(z(0)=b(0)\). Since
\[
 \dot b=b\left(1-\frac bK-a(\lambda+1/K)\right)
 \le b(1-b/K),
\]
the scalar comparison theorem gives \(0<b(t)\le z(t)\). Its inverse \(1/z(t)\) converges exponentially to the periodic inverse profile \(y_T(t)=1/b_T(t)\), so \(z(t)-b_T(t)=O(e^{-t})\) and \(\int_0^t[z(s)-1]ds=(m(T)-1)t+O(1)\). Hence
\[
 a(t)=a(0)\exp\left(\lambda\int_0^t(b(s)-1)ds\right)
 \le C\,e^{\lambda(m(T)-1)t}.
\]
When \(m(T)<1\), this proves exponential predator decay. Set \(w=1/b\); then
\[
 \dot w=-w+K^{-1}+a(t)(\lambda+K^{-1})w.
\]
As the decaying coefficient becomes uniformly small, scalar variation of constants bounds \(w\) for large time. Subtracting the periodic equation \(\dot y_T=-y_T+K^{-1}\) leaves a stable linear inhomogeneous equation driven by the exponentially decaying \(a(t)(\lambda+K^{-1})w(t)\). Thus \(w(t)-y_T(t)\to0\), and positivity of the periodic profile implies \(b(t)-b_T(t)\to0\). No global-attrition or persistence assertion is inferred in the other regimes. \(\square\)

For example, \(H=2\), \(L=1/2\) gives \(B=4/5\) and \(A=5/4\). The unique crossover is approximately \(T_*=7.901747381549\), independent of \(\lambda>0\).

## Verification

The standalone `verify.py` uses only Python's standard library. It independently integrates the explicit phasewise logistic solution by composite Simpson quadrature, compares the resulting mean against the closed hyperbolic formula at 60 tested parameter/period pairs, checks periodic endpoints, verifies strict inequalities at sampled periods, and brackets the unique threshold for \(H=2,L=1/2\). It has been run successfully. These finite numerical checks are **not** substitutes for the global proof above; in particular, numerical testing cannot establish universal monotonicity or global convergence.

To reproduce: run `python3 verify.py` in the directory containing the extracted files.

## Relationship to prior work

Swailem and Rucklidge, arXiv:2511.03521v1, introduce the same normalized mean-field predator–prey equations and analyze sinusoidal periodic forcing, Floquet instability and spatiotemporal complexity. The present two-level equal-duration model takes a different forcing profile and studies the predator-free periodic orbit, not coexistence resonance.

Swailem and Täuber, arXiv:2211.09276, study periodic switching between high and low capacities, including fast/slow asymptotic effective environments and stochastic spatial behavior. Their treatment does not give the present **strict all-period uniqueness of a predator invasion crossover together with global extinction in the stable regime**.

Taitelbaum, West, Assaf and Mobilia, arXiv:2002.10372, Supplemental Section S2.3, Eq. (S17), **already derive an explicit periodic solution of the identical scalar two-level logistic equation**, for arbitrary season durations. That scalar trajectory and its distribution are prior results and are not claimed as new. Our formula for its mean is algebraically obtainable from their solution; the assessed claim instead concerns its strict dependence on the switching period and the resulting sharp stability/global extinction classification when coupled to a predator. A previously unnoticed equivalent invasion theorem remains a residual priority risk.

Bargellini and Ritelli, DOI 10.3390/axioms15050355, treat periodic carrying capacities in scalar logistic growth. The retrieved description supports general periodic logistic solutions but not the specific coupled predator-invasion classification; the full publisher text was unavailable during this comparison.

López-Gómez, Ortega and Tineo (1996) develop broader periodic predator–prey stability theory. Their general results provide context but not this explicit two-level period threshold and its phase ordering.

## Limitations

This is a deterministic two-species, nonspatial model with precisely half-period high/low seasons and constant \(\lambda\). The threshold concerns the predator-free periodic solution and global extinction on the stable side. It does **not** establish a positive attractor, uniform persistence, a nonlinear bifurcation type at the neutral threshold, stochastic fixation behavior, or extension to arbitrary season ratios and nonlinear functional responses. Prior exact scalar logistic solution formulas are expressly acknowledged. The novelty assessment is limited by possible unindexed specialist work and one inaccessible publisher full text.

## References

1. M. Swailem and A. M. Rucklidge, *Parametric resonance, chaos and spatial structure in the Lotka-Volterra model*, arXiv:2511.03521v1 (first available 2025-11-05), https://arxiv.org/abs/2511.03521.
2. M. Swailem and U. C. Täuber, *Lotka–Volterra predator-prey model with periodically varying carrying capacity*, arXiv:2211.09276 (2022), https://arxiv.org/abs/2211.09276.
3. A. Taitelbaum, R. West, M. Assaf and M. Mobilia, *Population Dynamics in a Changing Environment: Random versus Periodic Switching*, arXiv:2002.10372 (2020), especially Supplement S2.3, https://arxiv.org/abs/2002.10372.
4. A. E. Bargellini and D. Ritelli, *A Carrying Capacity Periodically Variable in Logistic Growth Dynamics*, Axioms 15 (2026), 355, DOI 10.3390/axioms15050355.
5. J. López-Gómez, R. Ortega and A. Tineo, *The periodic predator-prey Lotka-Volterra model*, Advances in Differential Equations 1 (1996), 403–423, https://projecteuclid.org/journals/advances-in-differential-equations/volume-1/issue-3/The-periodic-predator-prey-Lotka-Volterra-model/ade/1366896045.pdf.
