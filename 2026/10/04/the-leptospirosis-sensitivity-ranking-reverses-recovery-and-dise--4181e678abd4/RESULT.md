# The leptospirosis sensitivity ranking reverses recovery and disease-mortality effects

## Finding

Consider the host-vector leptospirosis system
\[
\begin{aligned}
S_h'&=b_1-\mu_hS_h-\beta_1S_hI_h-\beta_2S_hI_v+\lambda_hR_h,\\
I_h'&=\beta_1S_hI_h+\beta_2S_hI_v-(\mu_h+\delta_h+\gamma_h)I_h,\\
R_h'&=\gamma_hI_h-(\mu_h+\lambda_h)R_h,\\
S_v'&=b_2-\gamma_vS_v-\beta_3S_vI_h,\\
I_v'&=\beta_3S_vI_h-(\gamma_v+\delta_v)I_v.
\end{aligned}
\]

The disease-free equilibrium has
\[
S_h^0=\frac{b_1}{\mu_h},
\qquad
S_v^0=\frac{b_2}{\gamma_v}.
\]
Set
\[
q_h=\mu_h+\delta_h+\gamma_h,
\qquad
q_v=\gamma_v+\delta_v,
\]
\[
a=\frac{\beta_1S_h^0}{q_h},
\qquad
c=\frac{\beta_2\beta_3S_h^0S_v^0}{q_hq_v}.
\]

The next-generation matrix for the infectious states
\[
(I_h,I_v)
\]
is
\[
K=
\begin{pmatrix}
\beta_1S_h^0/q_h & \beta_2S_h^0/q_v\\
\beta_3S_v^0/q_h & 0
\end{pmatrix},
\]
so its spectral radius is
\[
\mathcal R_{\mathrm{NGM}}
=
\frac{a+\sqrt{a^2+4c}}2.
\]

The earlier leptospirosis literature for this model family uses the human-generation threshold
\[
\mathcal T=a+c.
\]
These two normalizations have the same invasion boundary because the characteristic polynomial of \(K\) is
\[
z^2-az-c,
\]
and therefore
\[
\mathcal R_{\mathrm{NGM}}<1
\quad\Longleftrightarrow\quad
1-a-c>0
\quad\Longleftrightarrow\quad
\mathcal T<1.
\]

The source's Section 7 sensitivity conclusions are incompatible with either convention. In particular,
\[
\frac{\partial\mathcal R_{\mathrm{NGM}}}{\partial\lambda_h}
=
\frac{\partial\mathcal T}{\partial\lambda_h}
=
0,
\]
whereas
\[
\frac{\partial\mathcal R_{\mathrm{NGM}}}{\partial\delta_h}<0,
\qquad
\frac{\partial\mathcal R_{\mathrm{NGM}}}{\partial\gamma_h}<0,
\]
and the same strict inequalities hold for \(\mathcal T\).

Thus loss of immunity has zero invasion-threshold sensitivity, while faster human recovery and larger disease-induced human removal decrease the invasion threshold. The published paragraph instead groups
\[
\lambda_h,\delta_h,\gamma_h
\]
among parameters with positive impact and then, in the same paragraph, says that \(\lambda_h\) has no impact.

Using the source's numerical parameter set gives
\[
\mathcal T
\approx
1.318852151697663
\]
and
\[
\mathcal R_{\mathrm{NGM}}
\approx
1.318680846306750.
\]

For the type threshold, the normalized sensitivity indices are
\[
\begin{array}{c|r}
\Gamma&S_\Gamma^{\mathcal T}\\ \hline
b_1&1\\
\mu_h&-1.011392524244421\\
\beta_2&0.000537475477681\\
\beta_1&0.999462524522319\\
\lambda_h&0\\
\delta_h&-0.753224743432822\\
\gamma_h&-0.235382732322757\\
b_2&0.000537475477681\\
\gamma_v&-0.001072624221693\\
\beta_3&0.000537475477681\\
\delta_v&-0.000002326733670
\end{array}
\]

The next-generation sensitivities have the same signs and are numerically close. Consequently the source parameter set is dominated by the direct human transmission route rather than the vector-mediated route.

## Assumptions and scope

All parameters are positive except that the conclusion
\[
S_{\lambda_h}=0
\]
also remains valid at
\[
\lambda_h=0.
\]

The result concerns invasion about the disease-free equilibrium of the exact host-vector system printed in equation (1.1) of the source. The Caputo-Fabrizio reformulation has the same disease-free states and the same epidemiological transmission and removal parameters, but no claim is made here about fractional linear-stability regions beyond the reproduction-threshold sensitivity itself.

Two threshold conventions are stated explicitly because earlier literature on this model family uses the human-generation quantity
\[
\mathcal T=a+c,
\]
whereas the standard next-generation definition is the spectral radius
\[
\mathcal R_{\mathrm{NGM}}.
\]
The correction of signs is robust to this convention choice.

## Proof

At the disease-free equilibrium,
\[
R_h=I_h=I_v=0.
\]
The susceptible balances give
\[
S_h^0=\frac{b_1}{\mu_h},
\qquad
S_v^0=\frac{b_2}{\gamma_v}.
\]

For infected state vector
\[
x=(I_h,I_v)^\mathsf{T},
\]
the new-infection Jacobian and transition Jacobian are
\[
F=
\begin{pmatrix}
\beta_1S_h^0&\beta_2S_h^0\\
\beta_3S_v^0&0
\end{pmatrix},
\qquad
V=
\begin{pmatrix}
q_h&0\\
0&q_v
\end{pmatrix}.
\]
Thus
\[
K=FV^{-1}
\]
has characteristic polynomial
\[
z^2-az-c.
\]
Its Perron root is the displayed \(\mathcal R_{\mathrm{NGM}}\).

For the type threshold,
\[
\mathcal T=a+c.
\]
Because \(a,c>0\), the Perron root crosses \(1\) exactly when
\[
1-a-c=0.
\]
This proves threshold equivalence.

Now write the normalized elasticity as
\[
S_\Gamma^{\mathcal T}
=
\frac{\Gamma}{\mathcal T}
\frac{\partial\mathcal T}{\partial\Gamma}.
\]
The dependence of \(a\) and \(c\) gives
\[
S_{b_1}^{\mathcal T}=1,
\]
\[
S_{\mu_h}^{\mathcal T}
=
-1-\frac{\mu_h}{q_h},
\]
\[
S_{\lambda_h}^{\mathcal T}=0,
\]
\[
S_{\delta_h}^{\mathcal T}
=
-\frac{\delta_h}{q_h},
\qquad
S_{\gamma_h}^{\mathcal T}
=
-\frac{\gamma_h}{q_h}.
\]

If
\[
\theta=\frac{c}{a+c},
\]
then
\[
S_{\beta_2}^{\mathcal T}
=
S_{\beta_3}^{\mathcal T}
=
S_{b_2}^{\mathcal T}
=
\theta,
\]
\[
S_{\beta_1}^{\mathcal T}=1-\theta,
\]
\[
S_{\gamma_v}^{\mathcal T}
=
-\theta
\left(
1+\frac{\gamma_v}{q_v}
\right),
\qquad
S_{\delta_v}^{\mathcal T}
=
-\theta\frac{\delta_v}{q_v}.
\]

These formulas immediately establish the sign statements. Substitution of the source's parameter values gives the numerical table above.

For the spectral-radius convention, let
\[
D=\sqrt{a^2+4c}.
\]
Then
\[
\frac{\partial\mathcal R_{\mathrm{NGM}}}{\partial a}
=
\frac{\mathcal R_{\mathrm{NGM}}}{D}
\]
and
\[
\frac{\partial\mathcal R_{\mathrm{NGM}}}{\partial c}
=
\frac1D.
\]
Since \(\lambda_h\) enters neither \(a\) nor \(c\), its sensitivity is again zero. Since both \(a\) and \(c\) decrease with either \(\delta_h\) or \(\gamma_h\), the corresponding spectral sensitivities are strictly negative.

## Verification

The bundled `verify.py` uses exact rational arithmetic for
\[
a,\quad c,\quad\mathcal T,
\]
and every type-threshold sensitivity.

It separately evaluates
\[
\mathcal R_{\mathrm{NGM}}
\]
at high precision and checks the Perron eigenvalue equation
\[
\mathcal R_{\mathrm{NGM}}^2
-a\mathcal R_{\mathrm{NGM}}
-c=0.
\]

It also performs centered finite-difference checks of the normalized sensitivities for
\[
\beta_1,\quad\beta_2,\quad\lambda_h,\quad\delta_h,\quad\gamma_h
\]
against the analytic formulas.

The calculations do not infer novelty or stability from numerical experiments; they only replay the exact algebra at the source parameter set.

## Relationship to prior work

Khan, Raouf, Zarin, Yusuf, and Humphries print the five-equation host-vector model, the parameter set used in their simulations, and a Section 7 sensitivity discussion intended to identify parameters useful for reducing infection spread. That section states positive impact for \(\lambda_h,\delta_h,\gamma_h\), while later in the same paragraph stating that \(\lambda_h\) has no impact.

Zaman, Khan, Islam, Chohan, and Jung analyze an earlier leptospirosis host-vector model in the same family. Their disease-free threshold is written as a direct human-transmission contribution plus a vector-mediated contribution. This is the earlier-model analogue of
\[
\mathcal T=a+c.
\]
It establishes that the type-threshold convention is prior art and is not claimed as new here.

Khan, Islam, Khan, and Zaman later analyze global stability of a related variable-population host-vector model and again use a reproduction threshold to separate extinction and persistence regimes.

Engida and Mamo give sensitivity indices for a different leptospirosis human-rodent model and interpret positive and negative sensitivity signs in the standard way. Their model is not the system corrected here.

The contribution here is therefore narrow: it reconstructs the invasion threshold of the exact 2022 model, proves the sign structure under both common threshold conventions, and provides the corrected sensitivity ranking at the source's own parameter set.

## Limitations

The result does not claim that the source's numerical epidemic trajectories are incorrect. It corrects the threshold-sensitivity conclusions.

The type threshold
\[
\mathcal T
\]
and spectral radius
\[
\mathcal R_{\mathrm{NGM}}
\]
are numerically different away from the threshold even though they have the same \(1\)-crossing. The report therefore keeps their sensitivity tables conceptually separate.

Disease-induced mortality has a mathematically negative threshold sensitivity, but increasing mortality is not advocated as a public-health intervention.

No claim is made about sensitivity indices for quantities other than the invasion threshold.

## References

1. A. Khan, A. Raouf, R. Zarin, A. Yusuf, U. W. Humphries, “Existence theory and numerical solution of leptospirosis disease model via exponential decay law,” AIMS Mathematics 7 (2022), 8822–8846. DOI: 10.3934/math.2022492.
2. G. Zaman, M. A. Khan, S. Islam, M. I. Chohan, I. H. Jung, “Modeling dynamical interactions between leptospirosis infected vector and human population,” Applied Mathematical Sciences 6 (2012), 1287–1302.
3. M. A. Khan, S. Islam, S. A. Khan, G. Zaman, “Global Stability of Vector-Host Disease with Variable Population Size,” BioMed Research International 2013 (2013), 710917. DOI: 10.1155/2013/710917.
4. S. Engida, D. K. Mamo, “A Mathematical Model Analysis for the Transmission Dynamics of Leptospirosis Disease in Human and Rodent Populations,” Computational and Mathematical Methods in Medicine 2022 (2022), 1806585. DOI: 10.1155/2022/1806585.
