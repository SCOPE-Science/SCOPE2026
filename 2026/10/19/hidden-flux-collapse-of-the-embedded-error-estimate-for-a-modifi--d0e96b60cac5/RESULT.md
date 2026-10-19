# Hidden-flux collapse of the embedded error estimate for a modified Patankar step

## Finding

An exactly cancelling, positive bidirectional production--destruction flux can make the second-order MPRK22(1) update and its first-order embedded output almost indistinguishable **without changing the differential equation**. For every fixed positive step size and fixed strictly positive initial state, both numerical outputs approach the unchanged initial state at rate inverse to the artificial flux coefficient, while the exact solution moves by a fixed nonzero amount. The estimator-to-true-error ratio therefore tends to zero even though both numerical outputs remain positive and conservative.

More precisely, fix \(u,v,a,h>0\). For every \(c\geq0\), on the positive quadrant use the production and destruction fluxes
\[
 p_{12}(y)=a y_2+c y_1y_2,\qquad p_{21}(y)=c y_1y_2,
 \qquad d_{12}=p_{21},\quad d_{21}=p_{12},
\]
with diagonal fluxes zero. All these nonnegative, donor-vanishing flux choices give precisely the same initial-value problem
\[
 y_1'=a y_2,\qquad y_2'=-a y_2,
 \qquad (y_1(0),y_2(0))=(u,v).
\]
Let \(z=(u+\delta_c,v-\delta_c)\) be the first-order embedded output (the second MPRK22(1) stage) and \(Y=(u+\Delta_c,v-\Delta_c)\) the second-order output after one step of length \(h\). Put \(s=u+v\). Then
\[
 \boxed{\lim_{c\to\infty}c\delta_c=\frac{av}{s},\qquad
 \lim_{c\to\infty}c(\Delta_c-\delta_c)=\frac{av}{s},\qquad
 \lim_{c\to\infty}c\Delta_c=\frac{2av}{s}.}
\]
In particular, with \(E_c=\|Y-z\|_\infty=\Delta_c-\delta_c\) and the exact one-step error \(T_c=\|Y-y(h)\|_\infty\),
\[
 \boxed{E_c\sim \frac{av}{cs},\qquad
 T_c\longrightarrow v(1-e^{-ah})>0,\qquad
 \lim_{c\to\infty}\frac{T_c}{cE_c}=\frac{s(1-e^{-ah})}{a}.}
\]
Thus, no positive constant depending only on the differential equation, its initial state, and \(h\) can bound the true one-step error by a constant times this embedded discrepancy **uniformly over its positive conservative flux decompositions**. With fixed positive absolute tolerance and finite relative tolerance, the usual two-component weighted root-mean-square embedded estimate also tends to zero.

## Assumptions and scope

The method is the conservative two-stage MPRK22(1), i.e. the second-order modified Patankar--Runge--Kutta method built from the explicit Heun tableau and positive Patankar weight denominators \(\pi^{(2)}=y^n\), \(\sigma=z\). Each stage solves its corresponding two-by-two linear system exactly, in real arithmetic. The input \((u,v)\), physical rate \(a\), and step \(h\) are fixed and strictly positive; the cancellation coefficient \(c\) ranges over all nonnegative reals. The exact flow is \(y(h)=(u+v(1-e^{-ah}),ve^{-ah})\). The numerical flux representation is allowed to vary, but the continuous vector field and its Jacobian remain constant as functions of \(c\).

The theorem concerns a **single** step and an embedded discrepancy, not the reliability of every possible a posteriori estimator. The optional weighted estimate uses \(\mathrm{atol}>0\) and finite \(\mathrm{rtol}\geq0\). The full method remains well defined, positive, and mass conserving for each finite \(c\).

## Proof

Write \(s=u+v\). The stage system is
\[
 z_1=u+h\left[p_{12}(u,v)\frac{z_2}{v}-p_{21}(u,v)\frac{z_1}{u}\right],\qquad z_1+z_2=s.
\]
Substituting \(z=(u+\delta_c,v-\delta_c)\) and the displayed fluxes gives the **exact** formula
\[
 \boxed{\delta_c=\frac{hav}{1+h(a+cs)}.}\tag{1}
\]
The denominator exceeds \(ha\); hence \(0<\delta_c<v\), and \(z\) is positive.

Set \(U=u+\delta_c\), \(V=v-\delta_c\), and let the trapezoidal averaged fluxes be
\[
 Q_c=\frac c2(uv+UV),\qquad
 P_c=Q_c+\frac a2(v+V),\qquad
 K_c=\frac{P_c}{V}+\frac{Q_c}{U}.
\]
The final stage, with denominators \((U,V)\), is
\[
 Y_1=u+h\left[P_c\frac{Y_2}{V}-Q_c\frac{Y_1}{U}\right],\qquad Y_1+Y_2=s.
\]
Solving for the transfer \(\Delta_c=Y_1-u=v-Y_2\) yields
\[
 \boxed{\Delta_c=\frac{h(P_c v/V-Q_c u/U)}{1+hK_c}.}\tag{2}
\]
Since \(v=V+\delta_c\) and \(u=U-\delta_c\), direct subtraction of \(\delta_c\) from (2) cancels the Patankar-denominator terms and gives the particularly useful **exact identity**
\[
 \begin{aligned}
 \Delta_c-\delta_c
 &=\frac{h(P_c-Q_c)-\delta_c}{1+hK_c}\\
 &=\boxed{\frac{h^2av(a/2+cs)}{[1+h(a+cs)](1+hK_c)}}>0.
 \end{aligned}\tag{3}
\]
The final transfer is positive. Moreover, rearranging (2) proves
\[
 v-\Delta_c=\frac{v+hQ_c s/U}{1+hK_c}>0.
\]
Thus \(Y\), like \(z\), is strictly positive and exactly conservative for every \(c\ge0\).

Keeping \(u,v,a,h\) fixed, (1) gives \(c\delta_c\to av/s\). Consequently \(U\to u\), \(V\to v\), \(Q_c/c\to uv\), \(P_c/c\to uv\), and \(K_c/c\to s\). In (3), the numerator tends to \(hav\) while the denominator behaves as \(hcs\); hence \(c(\Delta_c-\delta_c)\to av/s\). Addition gives \(c\Delta_c\to2av/s\). This proves the three exact asymptotic limits.

The error vector relative to the embedded output is \(Y-z=(\Delta_c-\delta_c,-\Delta_c+\delta_c)\); the exact solution has nonzero displacement \((v(1-e^{-ah}),-v(1-e^{-ah}))\). As \(\Delta_c\to0\), the displayed true-error and estimator limits follow. For a normalized two-component embedded estimate with denominators \(\mathrm{atol}+\mathrm{rtol}\max(|Y_i|,|z_i|)\), the positive lower bound \(\mathrm{atol}\) implies an \(O(c^{-1})\) bound and convergence to zero. The underlying ODE has not changed, so the failure cannot be attributed to increasing stiffness of its vector field.

For a simple finite parameter comparison, at \(u=v=a=h=1\), \(c=0\) gives \(\delta_0=1/2\), \(\Delta_0=3/5\), whereas \(c\to\infty\) gives \(\Delta_c\to0\). This explicitly establishes representation dependence even though the original ODE and starting state are the same.

## Verification

The standalone `verify.py` uses only Python's standard-library exact rational arithmetic to solve both independent two-by-two linear stage systems. For a product grid of positive rational rates, steps and states and nonnegative flux parameters it compares the independently solved stages with (1)--(3), checks conservation and strict positivity, and tests the asymptotic constants and an absolute/relative tolerance example. Run with `python verify.py`. Its output reports 2,937 successful assertions; these are consistency checks, not substitutes for the general proof.

## Relationship to prior work

The MPRK22 family and its positivity/conservation property are established, not new here. The original nonlinear two-species stability calculation of Izgin, Kopecz and Meister considers a different two-pool production--destruction system and establishes local fixed-point stability, not equivalence of representations or error-estimator collapse. The adaptive-controller study of Izgin-Melnikov and Ranocha displays the exact MPRK22 stage and endpoint formulae, notes that a production--destruction representation is nonunique, and uses the embedded discrepancy for tolerance control; this theorem establishes a precise nonuniformity not asserted there. The 2026 flux-balanced analysis of Izgin, Meister, Shu and Torlo addresses spatial Euler flux balance, contact equilibria and physical positivity, not this unchanged-vector-field family or the masking limit. All three sources motivated the comparison; none is claimed to establish the asymptotic theorem above.

## Limitations

This is an analytical obstruction for a specific, widely used positivity-preserving embedded pair. It does not show that a particular physical reaction network is necessarily encoded with artificially cancelling fluxes, or that all step controllers actually accept the bad step under all safeguard configurations. Large \(c\) is an artificial splitting parameter, not a large eigenvalue of the underlying ODE Jacobian. The convergence estimates are for fixed \(u,v,a,h>0\) as \(c\to\infty\), not uniform in vanishing states, vanishing timesteps, or floating-point arithmetic. Exact algebra and standard positive-state assumptions are essential; no extension to other MPRK tableaux is claimed.

## References

1. T. Izgin, A. Meister, C.-W. Shu and D. Torlo, *Flux-Balanced Patankar-type Schemes for the Compressible Euler Equations*, arXiv:2602.14392, public preprint 2026-02-16; full manuscript at `https://bpb-us-w2.wpmucdn.com/sites.brown.edu/dist/0/348/files/2026/02/Flux-Balanced-Patankar-type-Schemes-for-the-Compressible-Euler-Equations.pdf`.
2. T. Izgin-Melnikov and H. Ranocha, *Using Machine Learning to Design Time Step Size Controllers for Stable Time Integrators*, Journal of Scientific Computing (2026), doi:10.1007/s10915-026-03496-1, §§2.2.1, 2.2.3, 3. Earlier public preprint arXiv:2312.01796; this work is cited as prior methodology, not as a 2026-first source.
3. T. Izgin, S. Kopecz and A. Meister, *A Stability Analysis of Modified Patankar--Runge--Kutta Methods for a Nonlinear Production--Destruction System*, arXiv:2210.11845 (2022), §§1--2.
