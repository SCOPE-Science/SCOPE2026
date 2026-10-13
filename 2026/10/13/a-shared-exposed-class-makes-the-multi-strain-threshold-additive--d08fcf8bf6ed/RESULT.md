# A shared exposed class makes the multi-strain threshold additive
## Finding
The multi-strain COVID-19/diabetes model of Casimir, Abibelaye, and Somdouda has one shared exposed class \(E\), strain-specific infectious classes \(I_j\), and one common infected-diabetic class \(C\). Its force of infection is proportional to
\[
C+\sum_{j=1}^{n} I_j.
\]
The article states a basic reproduction number obtained by taking the maximum of strainwise square-root expressions. That is not the next-generation threshold of the printed system.

Define
\[
\phi=\sum_{j=1}^{n}\varphi_j,\qquad
 a=\mu+\phi,
\]
\[
d_j=\mu_j+\gamma_j+\mu,
\qquad
 d_C=\mu+\delta_1+\gamma.
\]
At the disease-free equilibrium,
\[
N^0=S^0+D^0.
\]
The correct basic reproduction number is
\[
\boxed{
\mathcal R_{\mathrm{pool}}
=
\frac{\beta}{a}
\left[
\alpha\sum_{j=1}^{n}\frac{\varphi_j}{d_j}
+
(1-\alpha)\frac{\phi}{d_C}
\right]
}.
\]
The disease-free equilibrium is locally asymptotically stable for
\[
\mathcal R_{\mathrm{pool}}<1
\]
and unstable for
\[
\mathcal R_{\mathrm{pool}}>1.
\]

If
\[
A_j=\frac{\beta\alpha\varphi_j}{a d_j}
\quad\text{and}\quad
C_0=\frac{\beta(1-\alpha)\phi}{a d_C},
\]
then the source's equation (3.8) is equivalent to
\[
\mathcal R_{\mathrm{src}}=
\max_j\sqrt{C_0+A_j},
\]
while the printed model has
\[
\mathcal R_{\mathrm{pool}}=C_0+\sum_{j=1}^{n}A_j.
\]
For \(n=1\), these give the same threshold because
\[
\mathcal R_{\mathrm{src}}^2=\mathcal R_{\mathrm{pool}}.
\]
For \(n\ge2\), the source condition can miss the cumulative contribution of several infectious strains feeding the same exposed compartment.

An exact two-strain example has
\[
\mathcal R_{\mathrm{src}}=\frac9{10}<1
\qquad\text{but}\qquad
\mathcal R_{\mathrm{pool}}=\frac{27}{20}>1.
\]
The corresponding infected Jacobian has a positive eigenvalue
\[
-1+\frac{3\sqrt{15}}{10}>0.
\]
Thus the published disease-free stability criterion is false for the printed multi-strain system.

## Assumptions and scope
The result concerns equations (2.1)--(2.7) as printed in the 2026 article. The infected variables are
\[
(E,I_1,\ldots,I_n,C),
\]
with \(n\ge1\). All transition and demographic parameters are positive, \(0<\alpha<1\), and \(\beta>0\).

The model has a single exposed class \(E\). New infections caused by any \(I_j\) or by \(C\) enter this same class. Progression from \(E\) then feeds every \(I_j\) through \(\alpha\varphi_jE\) and feeds \(C\) through \((1-\alpha)\phi E\).

The correction is specific to that pooled-exposure architecture. In a different multi-strain model with separate exposed classes \(E_j\), the infected subsystem can decompose by strain and a maximum of strain-specific reproduction numbers can be correct.

The finding corrects the disease-free invasion threshold. It does not reassess the article's endemic-equilibrium Lyapunov argument or its optimal-control adjoint system.

## Proof
Let
\[
x=(E,I_1,\ldots,I_n,C)^\top.
\]
At the disease-free equilibrium, the total population contains only the susceptible and diabetic-uninfected classes, so
\[
N^0=S^0+D^0.
\]
Therefore the derivative of the incidence term with respect to each infectious class is exactly \(\beta\).

Following the standard next-generation decomposition, only newly generated infections belong in the matrix \(F\). Progression of an already infected individual from \(E\) into \(I_j\) or \(C\) belongs in the transition matrix \(V\). Hence
\[
F=
\begin{pmatrix}
0&\beta&\cdots&\beta&\beta\\
0&0&\cdots&0&0\\
\vdots&\vdots&&\vdots&\vdots\\
0&0&\cdots&0&0
\end{pmatrix}
\]
and
\[
V=
\begin{pmatrix}
a&0&\cdots&0&0\\
-\alpha\varphi_1&d_1&\cdots&0&0\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
-\alpha\varphi_n&0&\cdots&d_n&0\\
-(1-\alpha)\phi&0&\cdots&0&d_C
\end{pmatrix}.
\]
The matrix \(FV^{-1}\) has rank one. Its only nonzero eigenvalue is its first diagonal entry, equivalently the first component of the first row of \(FV^{-1}\). Solving
\[
Vz=e_1
\]
gives
\[
z_E=\frac1a,
\qquad
z_{I_j}=\frac{\alpha\varphi_j}{a d_j},
\qquad
z_C=\frac{(1-\alpha)\phi}{a d_C}.
\]
Therefore
\[
\rho(FV^{-1})
=
\frac{\beta}{a}
\left[
\alpha\sum_{j=1}^{n}\frac{\varphi_j}{d_j}
+
(1-\alpha)\frac{\phi}{d_C}
\right].
\]
This is \(\mathcal R_{\mathrm{pool}}\).

The infected linearization is the Metzler matrix
\[
M=
\begin{pmatrix}
-a&\beta&\cdots&\beta&\beta\\
\alpha\varphi_1&-d_1&\cdots&0&0\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
\alpha\varphi_n&0&\cdots&-d_n&0\\
(1-\alpha)\phi&0&\cdots&0&-d_C
\end{pmatrix}.
\]
The next-generation threshold theorem gives negative spectral bound when
\[
\mathcal R_{\mathrm{pool}}<1
\]
and positive spectral bound when
\[
\mathcal R_{\mathrm{pool}}>1.
\]
The remaining disease-free linear modes belong to the uninfected demographic subsystem and have negative real parts under the source's positive parameter assumptions, so this is also the disease-free stability threshold of the full model.

For a direct counterexample, take two strains and set
\[
\alpha=\frac45,
\quad
\beta=\frac32,
\quad
\mu=\frac1{10},
\quad
\varphi_1=\varphi_2=\frac9{20},
\]
\[
\mu_1=\mu_2=\frac15,
\quad
\gamma_1=\gamma_2=\frac7{10},
\quad
\delta_1=\frac15,
\quad
\gamma=\frac7{10}.
\]
Then
\[
a=d_1=d_2=d_C=1.
\]
The common diabetic-infection contribution is
\[
C_0=\frac{27}{100},
\]
and each strain contribution is
\[
A_1=A_2=\frac{54}{100}.
\]
Consequently,
\[
\mathcal R_{\mathrm{src}}
=
\sqrt{\frac{81}{100}}
=
\frac9{10},
\]
but
\[
\mathcal R_{\mathrm{pool}}
=
\frac{27}{100}+2\frac{54}{100}
=
\frac{27}{20}.
\]
The infected Jacobian becomes
\[
M=
\begin{pmatrix}
-1&\frac32&\frac32&\frac32\\
\frac9{25}&-1&0&0\\
\frac9{25}&0&-1&0\\
\frac9{50}&0&0&-1
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
(\lambda+1)^2
\left(\lambda^2+2\lambda-\frac7{20}\right),
\]
so the eigenvalues are
\[
-1,\quad -1,\quad -1-\frac{3\sqrt{15}}{10},\quad -1+\frac{3\sqrt{15}}{10}.
\]
Because
\[
\frac{3\sqrt{15}}{10}>1,
\]
the final eigenvalue is positive. This explicitly disproves the source criterion for two strains.

## Verification
The bundled script `verification/verify.py` uses exact rational arithmetic to verify the counterexample parameters, the source threshold, the corrected threshold, and the factorization of the infected characteristic polynomial. It also checks the sign of the positive eigenvalue.

The general reproduction-number formula is analytic and follows from the rank-one next-generation matrix above. The finite counterexample is a certificate that the two threshold conditions are not equivalent for the printed multi-strain model.

## Relationship to prior work
Van den Driessche and Watmough's next-generation framework defines \(F\) from new-infection terms and places transfers among already infected compartments in \(V\). Applying that framework to the printed 2026 system gives the rank-one matrix above.

A maximum of strain-specific reproduction numbers is standard in multi-strain models whose strain infection chains are dynamically separated. For example, Khyar and Allali's two-strain SEIR model has distinct exposed and infectious compartments for each strain, and its next-generation matrix is block-separated, yielding
\[
\mathcal R_0=\max\{\mathcal R_0^1,\mathcal R_0^2\}.
\]
Arruda et al. likewise use strain-specific infection structure and obtain a maximum over strain thresholds.

The 2026 model differs structurally: all infectious strains feed one pooled exposed class \(E\), and that class then feeds all strain-specific infectious classes. The cumulative return paths therefore add in the single nonzero next-generation eigenvalue. Searches using the exact DOI, title, reproduction-number formula, pooled exposed compartment, and disease-free stability claim did not locate a published correction of this source-specific threshold.

## Limitations
The result applies to the equations as printed. If the intended biological model had separate exposed classes \(E_j\) but they were collapsed typographically into one \(E\), a re-specified model would require a fresh next-generation calculation and could recover a maximum-of-strains threshold.

The result corrects the local disease-free threshold only. It does not establish existence or stability of every endemic equilibrium in the pooled-exposure model, and it does not assess the article's optimal-control conclusions.

The exact counterexample uses admissible positive parameters chosen to isolate the threshold discrepancy; it is not claimed to be a calibrated COVID-19 parameter set.

## References
1. M. Casimir, S. M. Abibelaye, S. Somdouda, “Modeling and Optimal Control of a Multi-Strain Epidemic Applied to COVID-19 with an Underlying Chronic Disease Condition,” Asia Pacific Journal of Mathematics 13 (2026), 47. DOI: 10.28924/APJM/13-47.
2. P. van den Driessche, J. Watmough, “Reproduction Numbers and Sub-Threshold Endemic Equilibria for Compartmental Models of Disease Transmission,” Mathematical Biosciences 180 (2002), 29–48. DOI: 10.1016/S0025-5564(02)00108-6.
3. O. Khyar, K. Allali, “Global Dynamics of a Multi-Strain SEIR Epidemic Model with General Incidence Rates: Application to COVID-19 Pandemic,” Nonlinear Dynamics 102 (2020), 489–509. DOI: 10.1007/s11071-020-05929-4.
4. E. F. Arruda, S. S. Das, C. M. Dias, D. H. Pastore, “Modelling and Optimal Control of Multi Strain Epidemics, with Application to COVID-19,” PLOS ONE 16 (2021), e0257512. DOI: 10.1371/journal.pone.0257512.
