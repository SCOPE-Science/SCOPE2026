# A flux-offset gauge-stalling law for finite-correction modified Patankar deferred correction

## Finding

Let two periodic upwind cells carry strictly positive masses \(a,b\), with \(a\ne b\), and take a fixed step \(h>0\). A spatially constant additive offset \(C\ge0\) in the numerical face flux leaves the underlying conservative semidiscretization exactly unchanged. Nevertheless, for every fixed finite correction count \(M\ge1\), the unmodified conservative modified-Patankar deferred-correction (mPDeC) update for this flux representation approaches the **identity** as \(C\to\infty\), with a sharp universal leading coefficient.

More precisely, let \(0=\eta_0<\cdots<\eta_r=1\), \(r\ge1\), be fixed interpolation nodes, and let
\[
\theta_{k\ell}=\int_0^{\eta_\ell}L_k(t)\,dt,\qquad
B_\ell=\sum_{k=0}^{r}|\theta_{k\ell}|>0,
\]
where \(L_k\) are the corresponding Lagrange polynomials. Then the first component of every mPDeC correction stage obeys, for each fixed \(1\le\ell\le r\) and \(1\le m\le M\),
\[
Y_1^{\ell,m}=a+\frac{m\eta_\ell}{B_\ell}\frac{ab(b-a)}{(a+b)C}+O(C^{-2}),\quad C\to\infty,
\]
and \(Y_2^{\ell,m}=a+b-Y_1^{\ell,m}\). The implicit constants depend on the fixed data, including \(h\) and the node set, but not on \(C\).

For Gauss–Lobatto nodes, all terminal quadrature weights are nonnegative, so \(B_r=\eta_r=1\); consequently
\[
\boxed{\lim_{C\to\infty} C(Y_1^{r,M}-a)=\frac{Mab(b-a)}{a+b}.}
\]
This nonzero limit is independent of the time step and the number of Gauss–Lobatto nodes. The one-correction endpoint formula, exact for every \(C\ge0\), is
\[
Y_1^{r,1}-a=\frac{h(b-a)}{1+h\left(2+C/a+C/b\right)}.
\]
All stages remain strictly positive and conserve \(a+b\) exactly.

The true ODE flow satisfies
\[
y_1(h)=a+\frac{b-a}{2}(1-e^{-2h}),\qquad y_2(h)=a+b-y_1(h).
\]
Therefore, for fixed \(h>0\), \(a\ne b\), every finite-correction Gauss–Lobatto mPDeC update has the strictly positive limiting Euclidean local error
\[
\boxed{\lim_{C\to\infty}\|Y^{r,M}-y(h)\|_2
=\frac{|b-a|}{\sqrt2}(1-e^{-2h}).}
\]
In particular, exact positivity and conservation do not imply accuracy bounds uniform over additive flux offsets.

## Assumptions and scope

The physical semidiscretization consists of two periodic finite-volume cells of unit width with upwind face fluxes \(K_{3/2}(y)=y_1+C\) and \(K_{5/2}(y)=y_2+C\). It is
\[
\dot y_1=K_{5/2}-K_{3/2}=y_2-y_1,\quad
\dot y_2=K_{3/2}-K_{5/2}=y_1-y_2.
\]
All offset values \(C\ge0\) encode the same ODE. The flux-based conservative production–destruction decomposition is
\[
p_{12}(y)=d_{21}(y)=y_2+C,\qquad
p_{21}(y)=d_{12}(y)=y_1+C,
\]
with other off-diagonal rates zero. It is precisely the positive-face-flux specialization of the flux-to-production/destruction splitting used in flux-based mPDeC; it is not a claim about arbitrary flux discretizations. The system starts at \((a,b)\in(0,\infty)^2\), and all results concern exact arithmetic, the standard mPDeC signed-weight exchange rule, fixed \(h>0\), fixed nodes, and a fixed **finite** number of correction iterations. The theorem allows negative intermediate-node quadrature weights and only requires \(B_\ell>0\). The Gauss–Lobatto endpoint specialization uses the positivity of its terminal quadrature weights.

## Proof

**Exact reduction and stage solvability.** At correction \(m\), denote the previous iterate at stage \(\ell\) by \(z=(z_1,z_2)=Y^{\ell,m-1}\), and previous iterates at interpolation nodes by \(v^k=Y^{k,m-1}\), with \(Y^{0,m}=(a,b)\) and all \(Y^{k,0}=(a,b)\). Set
\[
R_+=\frac{1}{z_2}\left(\sum_{\theta_{k\ell}\ge0}\theta_{k\ell}(v_2^k+C)
+\sum_{\theta_{k\ell}<0}|\theta_{k\ell}|(v_1^k+C)\right),
\]
\[
R_-=\frac{1}{z_1}\left(\sum_{\theta_{k\ell}\ge0}\theta_{k\ell}(v_1^k+C)
+\sum_{\theta_{k\ell}<0}|\theta_{k\ell}|(v_2^k+C)\right).
\]
These are nonnegative, and the sign-dependent index rule of mPDeC gives the two-equation linear system
\[
x_1=a+h(R_+x_2-R_-x_1),\qquad
x_2=b+h(R_-x_1-R_+x_2).
\]
With \(s=a+b\), solving yields
\[
x_1=\frac{a+h sR_+}{1+h(R_++R_-)},\quad
x_2=\frac{b+h sR_-}{1+h(R_++R_-)},\quad
x_1-a=\frac{h(bR_+-aR_-)}{1+h(R_++R_-)}.
\]
Both components are strictly positive and sum to \(s\); induction therefore constructs all stages uniquely for every \(C\ge0\).

**Large-offset induction.** Fix \(\ell\). Since Lagrange interpolation reproduces constants,
\(\sum_k\theta_{k\ell}=\eta_\ell\). Write \(B=B_\ell\), \(\eta=\eta_\ell\), and \(S=1/a+1/b\). Assume at the preceding correction each stage equals its initial value plus \(O(C^{-1})\). Write \(z_1=a+q/C+O(C^{-2})\), \(z_2=b-q/C+O(C^{-2})\); other previous-node values similarly equal their initial values plus \(O(C^{-1})\). From the displayed rates,
\[
R_++R_-=CBS+O(1),
\]
\[
bR_+-aR_-=\eta(b-a)+BSq+O(C^{-1}).
\]
To see the second equality, note that the \(C\)-parts contribute
\(CB[b/(b-q/C)-a/(a+q/C)]=BSq+O(C^{-1})\); the finite parts contribute
\((\sum_{\theta\ge0}\theta-\sum_{\theta<0}|\theta|)(b-a)=\eta(b-a)\).
Hence the exact update identity yields
\[
x_1-a=\frac{1}{C}\left(q+\frac{\eta(b-a)}{BS}\right)+O(C^{-2}).
\]
At correction zero all stage coefficients are zero, so induction gives
\(q=m\eta(b-a)/(BS)=m\eta ab(b-a)/[B(a+b)]\). This proves the stage formula, including negative quadrature weights. All rational functions in \(C\) have strictly positive denominators for \(C\ge0\); the displayed expansions hold at every fixed finite correction count.

**Terminal and accuracy consequences.** On Gauss–Lobatto nodes, the full-step weights are nonnegative and integrate the constant to one, so \(B_r=\eta_r=1\). At \(m=1\), every prior stage is \((a,b)\), giving \(R_+=(b+C)/b\) and \(R_-=(a+C)/a\); the exact one-correction formula follows. The ODE difference \(y_1-y_2\) decays as \(e^{-2t}\), proving the exact solution and its strictly positive distance from \((a,b)\) for \(a\ne b\). Since the numerical endpoint tends to that initial state, the claimed limiting error follows.

## Verification

The standalone `checker.py` uses exact rational arithmetic to construct every signed-coefficient mPDeC stage. It checks the linearly implicit two-cell equations directly, positivity, mass conservation, the one-correction identity, and approach to the leading coefficient for two- and three-node Gauss–Lobatto schemes, three positive initial states, five correction counts, and six offsets: 180 configurations. Its finite tests do not prove the asymptotic statement; the induction above supplies the infinite-offset proof.

## Relationship to prior work

Öffner and Torlo (arXiv:1905.09237) introduced conservative, positive high-order mPDeC for production–destruction systems. Izgin and Öffner (arXiv:2206.07371) analyzed local stability of several modified Patankar schemes, especially linear rate representations \(p_{ij}(y)=a_{ij}y_j\). Öffner, Redle, and Torlo (arXiv:2610.21857, §§2–4) combine flux globalization with flux-based mPDeC and use the positive and negative parts of global numerical fluxes. None of the inspected results establishes this offset-asymptotic, finite-correction stalling law. The dependence is on the **chosen representation** of a fixed ODE, not instability of its exact flow; the representation used here has nonlinear positive rates \(y_j+C\), outside the linear-rate stability setting. A historically equivalent result outside the compared sources cannot be excluded.

## Limitations

The counterexample concerns one two-cell periodic semidiscretization and its specified flux-based production–destruction representation, exact arithmetic, a fixed positive step size, and a fixed finite number of mPDeC corrections. It does not imply loss of positivity or conservation, failure at fixed \(C\) under time-step refinement, failure of steady-state preservation (the case \(a=b\) is preserved), or failure of the particular gauge convention adopted in any specific shallow-water implementation. The large-\(C\) and large-\(M\) limits are not interchangeable. Floating-point desingularization and general multidimensional numerical fluxes are not considered.

## References

1. P. Öffner, M. Redle, D. Torlo, *High-order positivity-preserving well-balanced schemes: combining flux globalization with modified Patankar deferred correction methods*, arXiv:2610.21857v1 (first public 2026-10-15), https://arxiv.org/html/2610.21857v1.
2. P. Öffner, D. Torlo, *Arbitrary high-order, conservative and positive preserving Patankar-type deferred correction schemes*, arXiv:1905.09237v2 (2019), https://arxiv.org/abs/1905.09237.
3. T. Izgin, P. Öffner, *A study of the local dynamics of modified Patankar DeC and higher order modified Patankar–RK methods*, arXiv:2206.07371v4 (2023), https://arxiv.org/html/2206.07371v4.
