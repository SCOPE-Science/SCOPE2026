# The Gavish coexistence polynomial is cubic, not quartic
## Finding
Adenane, Avram, and Halanay reduce coexistence in the waning-immunity Feng–Gavish two-strain epidemic model to a scalar polynomial
\[
P_G(s)=-\Delta(s)F_G(s).
\]
Immediately before their Question 2 on feasible root multiplicity, they state that \(P_G\) has degree four.

Using their own reconstruction formulas, the degree is in fact at most three for every parameter choice. The bound is sharp: positive parameter values exist for which the cubic coefficient is nonzero.

This changes the algebraic complexity of the open problem. Before feasibility is imposed, the scalar coexistence equation has at most three roots, not four. Consequently, any exact root-count or multiple-root classification may be carried out with a cubic rather than a quartic.

## Assumptions and scope
The model is the eight-compartment waning-immunity Feng–Gavish system in Equation (6) of the source. All epidemiological parameters appearing in the source reconstruction are positive:
\[
\beta_i,\eta_i,\sigma_i,\gamma_i,\mu>0,
\qquad
\theta_1,\theta_2,\theta_{12}\ge0.
\]
Following the source, set
\[
v_i=\gamma_i+\mu,
\qquad
d_i=\mu+\theta_i,
\qquad
d_{12}=\mu+\theta_{12},
\qquad
s_i=\frac{v_i}{\beta_i}.
\]

The claim concerns the algebraic degree of the exact scalar equation after the source's rational-univariate reconstruction. It does not claim a complete root-count classification on the feasible interval
\[
(s_\Delta,\bar s),
\qquad
\bar s=\min\{s_1,s_2\},
\]
and it does not classify stability of the reconstructed coexistence equilibria.

## Proof
The source's rank-one coexistence conditions give
\[
r_2(s)=\frac{s_1-s}{\eta_1\sigma_1},
\qquad
r_1(s)=\frac{s_2-s}{\eta_2\sigma_2}.
\]
Both are affine functions of \(s\).

Its Cramer determinant is
\[
\Delta(s)
=
\gamma_1\gamma_2s^2
-\sigma_1\sigma_2v_1v_2r_1(s)r_2(s),
\]
so
\[
\deg\Delta\le2.
\]

Define
\[
N_1(s)
=
r_1(s)
\bigl(
\gamma_2sd_1+\sigma_2v_2d_2r_2(s)
\bigr),
\]
\[
N_2(s)
=
r_2(s)
\bigl(
\gamma_1sd_2+\sigma_1v_1d_1r_1(s)
\bigr).
\]
Because each \(r_i\) is affine, both \(N_1\) and \(N_2\) have degree at most two. The source's Cramer formulas are exactly
\[
c_1(s)=\frac{N_1(s)}{\Delta(s)},
\qquad
c_2(s)=\frac{N_2(s)}{\Delta(s)}.
\]

The recovered-immunity coordinate is
\[
r_{12}(s)
=
\frac{
\gamma_1\sigma_1r_2(s)c_1(s)
+
\gamma_2\sigma_2r_1(s)c_2(s)
}{d_{12}},
\]
hence
\[
r_{12}(s)
=
\frac{
\gamma_1\sigma_1r_2(s)N_1(s)
+
\gamma_2\sigma_2r_1(s)N_2(s)
}{
d_{12}\Delta(s)
}.
\]

Now use the susceptible equation from Equation (6):
\[
s'
=
\Lambda-\mu s
-\beta_1J_1s
-\beta_2J_2s
+\theta_1r_1+\theta_2r_2+\theta_{12}r_{12}.
\]
At coexistence,
\[
J_1=c_1(s+\eta_1\sigma_1r_2),
\qquad
J_2=c_2(s+\eta_2\sigma_2r_1).
\]
The rank-one singularity equations imply
\[
\beta_1(s+\eta_1\sigma_1r_2)=v_1,
\qquad
\beta_2(s+\eta_2\sigma_2r_1)=v_2.
\]
Therefore
\[
\beta_1J_1s=v_1sc_1,
\qquad
\beta_2J_2s=v_2sc_2.
\]

Put
\[
A(s)=
\Lambda-\mu s+\theta_1r_1(s)+\theta_2r_2(s).
\]
Then the scalar residual produced by the source reconstruction is
\[
F_G(s)
=
A(s)
-\frac{v_1sN_1(s)+v_2sN_2(s)}{\Delta(s)}
+
\frac{\theta_{12}}{d_{12}\Delta(s)}
\bigl(
\gamma_1\sigma_1r_2(s)N_1(s)
+
\gamma_2\sigma_2r_1(s)N_2(s)
\bigr).
\]
Thus, with the source's sign convention,
\[
\begin{aligned}
P_G(s)
=&-\Delta(s)F_G(s)\\
=&-\Delta(s)A(s)
+v_1sN_1(s)
+v_2sN_2(s)\\
&-\frac{\theta_{12}}{d_{12}}
\bigl(
\gamma_1\sigma_1r_2(s)N_1(s)
+
\gamma_2\sigma_2r_1(s)N_2(s)
\bigr).
\end{aligned}
\]

Every displayed summand has degree at most three:
\[
\deg(\Delta A)\le3,
\qquad
\deg(sN_i)\le3,
\qquad
\deg(r_jN_i)\le3.
\]
Hence
\[
\deg P_G\le3.
\]

The upper bound is attained. Choose
\[
\mu=1,\quad
\gamma_1=2,\quad
\gamma_2=3,\quad
\beta_1=3,\quad
\beta_2=2,
\]
\[
\eta_1=\eta_2=\sigma_1=\sigma_2=
\theta_1=\theta_2=\theta_{12}=1,
\qquad
\Lambda=10.
\]
Then
\[
v_1=3,\quad v_2=4,\quad
d_1=d_2=d_{12}=2,\quad
s_1=1,\quad s_2=2,
\]
and direct exact expansion gives
\[
P_G(s)=s^3+53s^2-356s+260.
\]
The cubic coefficient is \(1\), so degree three genuinely occurs.

## Verification
The bundled `verification/verify.py` implements the source reconstruction with exact rational polynomial arithmetic.

For the positive parameter point used in the proof it reconstructs
\[
\Delta,\ N_1,\ N_2,\ r_{12}
\]
through their numerator formulas and verifies exactly that
\[
P_G(s)=s^3+53s^2-356s+260.
\]
At several rational values of \(s\) away from \(\Delta(s)=0\), it also evaluates the original rational residual \(F_G(s)\) and checks the defining identity
\[
P_G(s)=-\Delta(s)F_G(s)
\]
with exact fractions.

The finite replay is not the proof of the universal degree bound. That bound follows from the degree bookkeeping in the proof above.

## Relationship to prior work
The motivating 2026 paper itself supplies all reconstruction formulas used here and explicitly poses the feasible root count of \(P_G\) as an open problem. It states immediately before that question that \(P_G\) has degree four. The source-specific algebra above shows that multiplying the reconstructed susceptible residual by the single quadratic denominator \(\Delta\) produces only cubic terms.

The earlier Gavish–Rabiu waning-immunity preprint studies a closely related two-strain model and reports an asymptotic regime governed by a quadratic equation. That work was later withdrawn because its perturbative analysis relied on unfulfilled asymptotic assumptions. Its quadratic asymptotic reduction does not establish the exact cubic degree of the 2026 eight-compartment RUR polynomial.

Published-finding searches using the exact DOI, the notation \(P_G\), the Gavish coexistence polynomial, cubic/quartic degree aliases, and Question 2 returned no equivalent correction. The closest hits were unrelated results involving cubic or quartic polynomials.

## Limitations
The finding corrects the degree count and reduces the open root-count problem from quartic to cubic. It does not give the complete semialgebraic conditions for one, two, or three feasible roots.

A cubic can still have multiple roots, and feasibility additionally requires
\[
s\in(s_\Delta,\bar s).
\]
Therefore the source's proposed use of discriminants, resultants, or Sturm methods remains appropriate, but the objects to be analyzed are cubic rather than quartic.

The result also does not revisit the source's persistence theorem, boundary relay theorem, or local-stability partition.

## References
1. R. Adenane, F. Avram, A.-D. Halanay, “Persistence, Coexistence, and Boundary Transcritical Relays for Multi-Strain Epidemic Models,” Mathematics 14 (2026), 3271. DOI: 10.3390/math14183271. Earliest public preprint: 5 August 2026, Preprints.org 202608.0347.
2. N. Gavish, M. Rabiu, “Dynamics of a two-strain epidemic model with waning immunity—A perturbative approach,” arXiv:2311.11318 (2023; withdrawn in 2026).
