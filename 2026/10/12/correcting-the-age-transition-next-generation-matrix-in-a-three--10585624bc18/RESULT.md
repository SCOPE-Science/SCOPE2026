# Correcting the age-transition next-generation matrix in a three-age-class HIV model
## Finding

In the three-age-class HIV/AIDS model of Zhao, Wu, and Ruan, the basic reproduction number printed in equations (3)-(4) is not the next-generation reproduction number of the model displayed as equation (1).

The source writes the infected-state equations as
\[
\dot z=\mathcal F(z)-\mathcal V(z),
\]
but assigns the aging terms
\[
\alpha_y I_y,\qquad \alpha_a I_a
\]
to \(\mathcal F\) while retaining the same transfers with negative sign in \(\mathcal V\). For example, its displayed decomposition gives
\[
\mathcal F_{I_a}
=
\phi_aS_a+\alpha_yI_y,
\qquad
\mathcal V_{I_a}
=
\eta_3I_a-\alpha_yI_y.
\]
Therefore
\[
\mathcal F_{I_a}-\mathcal V_{I_a}
=
\phi_aS_a+2\alpha_yI_y-\eta_3I_a,
\]
whereas model (1) contains only
\[
\phi_aS_a+\alpha_yI_y-\eta_3I_a.
\]
The same doubling occurs for the adult-to-elder aging term.

For a valid next-generation decomposition, aging and other progression among already infected individuals belong to \(\mathcal V\), while \(\mathcal F\) contains only genuinely new infections. Define
\[
\eta_1=\alpha_y+r_y+\mu_y+\beta_y,
\qquad
\eta_3=\alpha_a+r_a+\mu_a+\beta_a,
\qquad
\eta_5=\mu_e+r_e.
\]
After eliminating infected compartments that do not themselves create new infections, the correct next-generation matrix on
\[
(I_y,I_a,I_e)
\]
is
\[
K=
\begin{pmatrix}
\frac{\beta_{11}}{\eta_1}+\frac{\beta_{21}\alpha_y}{\eta_1\eta_3}
&
\frac{\beta_{21}}{\eta_3}
&
0
\\[4pt]
\frac{\beta_{12}}{\eta_1}+\frac{\beta_{22}\alpha_y}{\eta_1\eta_3}
&
\frac{\beta_{22}}{\eta_3}
&
0
\\[4pt]
\frac{\beta_{23}\alpha_y}{\eta_1\eta_3}
+\frac{\beta_{33}\alpha_y\alpha_a}{\eta_1\eta_3\eta_5}
&
\frac{\beta_{23}}{\eta_3}
+\frac{\beta_{33}\alpha_a}{\eta_3\eta_5}
&
\frac{\beta_{33}}{\eta_5}
\end{pmatrix}.
\]
It follows that
\[
\mathcal R_0^{\mathrm{corr}}
=
\max\!\left\{
\frac{\beta_{33}}{\eta_5},
\rho(B)
\right\},
\]
where
\[
B=
\begin{pmatrix}
\frac{\beta_{11}}{\eta_1}+\frac{\beta_{21}\alpha_y}{\eta_1\eta_3}
&
\frac{\beta_{21}}{\eta_3}
\\[4pt]
\frac{\beta_{12}}{\eta_1}+\frac{\beta_{22}\alpha_y}{\eta_1\eta_3}
&
\frac{\beta_{22}}{\eta_3}
\end{pmatrix}.
\]

The source's printed entry \(A_{31}\) has an additional defect: besides the spurious new-infection contribution \(\alpha_y/\eta_1\), it contains
\[
\frac{\beta_{22}\alpha_a}{\eta_1\eta_3},
\]
where multiplication of the source's own displayed matrices would use \(\alpha_y\), not \(\alpha_a\).

The discrepancy is not merely a change in the numerical value assigned to a threshold. There are positive parameters for which the source's printed \(\mathcal R_0\) exceeds one while the actual disease-free equilibrium is locally asymptotically stable.

Take
\[
\eta_1=\eta_3=\eta_5=\frac1{20},
\qquad
\alpha_y=\alpha_a=\frac1{40},
\]
and
\[
\beta_{21}=\frac3{50},
\qquad
\beta_{11}=\beta_{12}=\beta_{22}=\beta_{23}=\beta_{33}
=
\frac1{20000}.
\]
The unused components of \(\eta_1\) and \(\eta_3\) can all be chosen strictly positive; for example,
\[
r_y=\mu_y=\beta_y=\frac1{120},
\qquad
r_a=\mu_a=\beta_a=\frac1{120},
\]
and one may take
\[
\mu_e=r_e=\frac1{40}.
\]

For these rates the corrected youth-adult block is
\[
B=
\begin{pmatrix}
\frac{601}{1000} & \frac65\\[2pt]
\frac3{2000} & \frac1{1000}
\end{pmatrix},
\]
with
\[
\det(I-B)
=
\frac{396801}{1000000}>0.
\]
Its diagonal entries are below one, so \(I-B\) is a nonsingular \(M\)-matrix and
\[
\rho(B)<1.
\]
The elder branch is
\[
\frac{\beta_{33}}{\eta_5}
=
\frac1{1000}<1.
\]

The source's printed formula instead gives
\[
B_{\mathrm{printed}}
=
\begin{pmatrix}
\frac{601}{1000} & \frac65\\[2pt]
\frac{1003}{2000} & \frac1{1000}
\end{pmatrix},
\]
for which
\[
\det(I-B_{\mathrm{printed}})
=
-\frac{203199}{1000000}<0.
\]
Hence its Perron root is greater than one.

At the same parameter choice, the actual youth-adult infected linearization is
\[
J_{ya}
=
\begin{pmatrix}
-\frac{999}{20000} & \frac3{50}\\[2pt]
\frac{501}{20000} & -\frac{999}{20000}
\end{pmatrix}.
\]
It has negative trace and
\[
\det J_{ya}
=
\frac{396801}{400000000}>0,
\]
so both eigenvalues have negative real part. The elder infected eigenvalue is also negative. Thus the disease-free equilibrium is locally asymptotically stable although the reproduction number printed in the source is greater than one.

## Assumptions and scope

The correction concerns the exact nine-dimensional ODE system printed as model (1), with nonnegative state variables and positive demographic, aging, progression, and removal rates.

The next-generation calculation uses the source's infected compartments
\[
(I_y,A_y,I_a,A_a,I_e,A_e)
\]
but notes that the AIDS compartments do not appear in the force of infection. Eliminating their zero-producing rows leaves the three-state matrix above without changing the nonzero spectrum.

No empirical re-estimation is performed. The counterexample is a mathematical parameter choice showing that the published threshold can misclassify invasion. It is not asserted to equal the source's fitted Chinese data set.

The result does not claim that every theorem in the article fails. It establishes that conclusions whose hypothesis is solely the printed
\[
\mathcal R_0>1
\]
cannot be justified by that quantity as written. In particular, the article's persistence and endemic-existence implications from this threshold require reassessment with the corrected next-generation number.

## Proof

The source defines the forces of infection
\[
\phi_y=\frac{\beta_{11}I_y+\beta_{21}I_a}{N_y},
\qquad
\phi_a=\frac{\beta_{22}I_a+\beta_{12}I_y}{N_a},
\qquad
\phi_e=\frac{\beta_{33}I_e+\beta_{23}I_a}{N_e}.
\]
At the disease-free equilibrium,
\[
S_y=N_y,\qquad S_a=N_a,\qquad S_e=N_e.
\]
Therefore the genuinely new-infection part of the linearized infectious subsystem is
\[
F=
\begin{pmatrix}
\beta_{11} & \beta_{21} & 0\\
\beta_{12} & \beta_{22} & 0\\
0 & \beta_{23} & \beta_{33}
\end{pmatrix}.
\]

Aging is progression of an already infected individual, not appearance of a new infected individual. The transition matrix on
\[
(I_y,I_a,I_e)
\]
is consequently
\[
V=
\begin{pmatrix}
\eta_1 & 0 & 0\\
-\alpha_y & \eta_3 & 0\\
0 & -\alpha_a & \eta_5
\end{pmatrix}.
\]
Its inverse is
\[
V^{-1}
=
\begin{pmatrix}
\frac1{\eta_1} & 0 & 0\\[4pt]
\frac{\alpha_y}{\eta_1\eta_3} & \frac1{\eta_3} & 0\\[4pt]
\frac{\alpha_y\alpha_a}{\eta_1\eta_3\eta_5}
&
\frac{\alpha_a}{\eta_3\eta_5}
&
\frac1{\eta_5}
\end{pmatrix}.
\]
Multiplication gives the stated \(K=FV^{-1}\).

Because \(K\) is block lower triangular,
\[
\rho(K)
=
\max\!\left\{
\frac{\beta_{33}}{\eta_5},
\rho(B)
\right\}.
\]

For the youth-adult block,
\[
\det(I-B)
=
\frac{
(\eta_1-\beta_{11})(\eta_3-\beta_{22})
-\beta_{21}(\beta_{12}+\alpha_y)
}{\eta_1\eta_3}.
\]
This is exactly the normalized determinant controlling the actual disease-free youth-adult linearization
\[
\begin{pmatrix}
\beta_{11}-\eta_1 & \beta_{21}\\
\beta_{12}+\alpha_y & \beta_{22}-\eta_3
\end{pmatrix}.
\]
Thus the corrected next-generation threshold agrees with the direct local-stability threshold, as required.

For the explicit counterexample, exact substitution gives
\[
\det(I-B)
=
\frac{396801}{1000000}>0,
\]
whereas the printed matrix gives
\[
\det(I-B_{\mathrm{printed}})
=
-\frac{203199}{1000000}<0.
\]
The direct linearization has negative trace and positive determinant, completing the threshold-reversal certificate.

## Verification

The bundled `verify.py` uses exact rational arithmetic.

It reconstructs the corrected and printed youth-adult matrices for the counterexample, checks
\[
\det(I-B)
=
\frac{396801}{1000000},
\]
checks
\[
\det(I-B_{\mathrm{printed}})
=
-\frac{203199}{1000000},
\]
and verifies the direct disease-free linearization has negative trace and positive determinant.

It also verifies that all component rates used to realize
\[
\eta_1=\eta_3=\eta_5=\frac1{20}
\]
are strictly positive.

The checker is a replay of the exact certificate. The general next-generation formula is established analytically from the displayed matrices.

## Relationship to prior work

Van den Driessche and Watmough define the next-generation construction by separating rates of appearance of new infections from all other changes in infected compartments. Their treatment-model example explicitly treats progression between infected stages as a transition rather than a new infection. They also explain that an epidemiologically incorrect decomposition may yield a different reproduction-number value.

The present issue is sharper than merely choosing an unconventional but algebraically valid decomposition. In the motivating article, the displayed \(\mathcal F\) and \(\mathcal V\) do not reconstruct model (1): aging appears on both sides and is therefore doubled in \(\mathcal F-\mathcal V\). The printed entry \(A_{31}\) additionally uses \(\alpha_a\) in a product where the displayed matrices require \(\alpha_y\).

Searches by exact DOI and title, by the printed \(\beta_{12}+\alpha_y\) term, by aging/progression and next-generation terminology, and by correction or erratum terminology did not locate a published repair of this source-specific threshold.

## Limitations

The result concerns the reproduction-number derivation and the threshold conclusions that depend on it.

It does not refit the model to the Chinese HIV/AIDS data, recompute the article's sensitivity analysis, or determine which numerical parameter set was used in every figure.

The explicit counterexample establishes that the printed threshold is not merely a harmless rescaling: it can put a locally stable disease-free equilibrium on the source's \(\mathcal R_0>1\) side. It does not claim that the paper's fitted baseline parameter set lies on opposite sides of the two thresholds.

An unindexed author correction could exist outside the searched records.

## References

1. H. Zhao, P. Wu, S. Ruan, “Dynamic analysis and optimal control of a three-age-class HIV/AIDS epidemic model in China,” Discrete and Continuous Dynamical Systems - B 25 (2020), 3491–3521. DOI: 10.3934/dcdsb.2020070.
2. P. van den Driessche, J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” Mathematical Biosciences 180 (2002), 29–48. DOI: 10.1016/S0025-5564(02)00108-6.
