# An exact coupled reproduction threshold for a fifteen-compartment COVID–Mpox model

## Finding
For the **printed fifteen-equation model** of Acheneje and collaborators [1, Eq. (1)], the disease-free equilibrium is locally asymptotically stable precisely when \(\mathcal R_{\mathrm{full}}<1\), and is linearly unstable when \(\mathcal R_{\mathrm{full}}>1\), where
\[
\mathcal R_{\mathrm{full}}=\max\left\{\frac{A+D+\sqrt{(A-D)^2+4BC}}2,\ \frac{\beta_r\theta_r}{gh}\right\},
\]
with \(A,B,C,D\) explicitly defined below. The published rule \(\max\{\mathcal R_C,\mathcal R_M,\mathcal R_r\}\) is not the threshold for the complete printed equations. In particular, there are **strictly positive** admissible model parameters for which all three published component reproduction numbers are below one but the full disease-free equilibrium is unstable. The discrepancy arises from linear pathways through the exposed co-infection and co-infected infectious compartments, which transmit both pathogens.

## Assumptions and scope
Use the susceptible-human, susceptible-rodent, exposed, infectious, treated and recovered compartments and forces of infection exactly as specified in [1, Eq. (1)]. In particular,
\[
\lambda_C=\beta_a(I_C+I_{CM})/N_h,\quad
\lambda_M=[\beta_bI_r+\beta_c(I_M+I_{CM})]/N_h,\quad
\lambda_r=\beta_rI_r/N_r.
\]
Here the co-exposed class receives \(\phi_C E_C+\phi_M E_M\), and the co-infected infectious class receives \(\theta_{CM}E_{CM}\), in addition to quadratic cross-infection terms. Assume positive recruitment, positive natural mortality and strictly positive progression, transmission, treatment and disease-removal rates. The other parameters may take any biologically permitted positive values. The equilibrium is the state with \(S_h=\Lambda_h/\mu_h\), \(S_r=\Lambda_r/\mu_r\), and all other compartments zero.

For compactness, define positive removal constants
\[
\begin{aligned}
a&=\mu_h+\phi_C+\theta_C,&b&=\mu_h+\phi_M+\theta_M,\\
c&=\mu_h+\theta_{CM},&d&=\mu_h+\rho_C+\delta_C,\\
e&=\mu_h+\rho_M+\delta_M,&u&=\mu_h+\rho_{CM}+\delta_{CM},\\
g&=\mu_r+\theta_r,&h&=\mu_r+\delta_r,\\
w&=\theta_{CM}/(cu).&&
\end{aligned}
\]
Define the four nonnegative coefficients
\[
A=\frac{\beta_a}{a}\left(\frac{\theta_C}{d}+\phi_Cw\right),\quad
B=\frac{\beta_a\phi_Mw}{b},\quad
C=\frac{\beta_c\phi_Cw}{a},\quad
D=\frac{\beta_c}{b}\left(\frac{\theta_M}{e}+\phi_Mw\right).
\]
The formula concerns **local linear stability** of the disease-free equilibrium, not global convergence or the existence of endemic equilibria.

## Proof
**Step 1: Linear infected subsystem.** At the disease-free equilibrium, \(S_h/N_h=S_r/N_r=1\). Terms in the forces of infection that multiply already-infected compartments become quadratic and drop out of the linearization. In the order
\[
(E_C,E_M,E_{CM},I_C,I_M,I_{CM},E_r,I_r),
\]
the infected Jacobian is \(F-V\), where \(V\) is lower triangular with diagonal \((a,b,c,d,e,u,g,h)\) and exactly these nonzero negative off-diagonal entries:
\[
V_{31}=-\phi_C,\ V_{32}=-\phi_M,\ V_{41}=-\theta_C,\
V_{52}=-\theta_M,\ V_{63}=-\theta_{CM},\ V_{87}=-\theta_r.
\]
The only nonzero entries of the nonnegative new-infection matrix \(F\) are
\[
F_{14}=F_{16}=\beta_a,\quad F_{25}=F_{26}=\beta_c,\quad
F_{28}=\beta_b,\quad F_{78}=\beta_r.
\]
The omitted treated, recovered and susceptible variables form stable downstream/feedback-to-susceptible blocks at linear order; none feeds the infected subsystem at the disease-free equilibrium. Consequently, its growth rate determines the equilibrium's stability.

**Step 2: Reduce the reproduction operator.** The matrix \(V\) is a nonsingular \(M\)-matrix. Since new infections enter only \(E_C,E_M,E_r\), the nonzero spectrum of \(FV^{-1}\) is that of the three-by-three next-generation matrix on these entry states:
\[
G=\begin{pmatrix}
 A&B&0\\
 C&D&\beta_b\theta_r/(gh)\\
 0&0&\beta_r\theta_r/(gh)
\end{pmatrix}.
\]
For example, one individual starting in \(E_C\) passes on average \(\theta_C/(ad)\) time units in \(I_C\), and \(\phi_C\theta_{CM}/(ac u)\) time units in \(I_{CM}\); both classes create new \(E_C\) infections at rate \(\beta_a\), giving entry \(A\). The other entries follow by the same path accounting. The rodent-to-human term \(\beta_b\theta_r/(gh)\) does not alter the eigenvalues, because the printed model has no human-to-rodent transmission.

The human block has eigenvalues \((A+D\pm\sqrt{(A-D)^2+4BC})/2\), and the third eigenvalue is \(\beta_r\theta_r/(gh)\). The standard nonsingular-\(M\)-matrix threshold theorem for compartmental infection systems [2,3] gives negative infected spectral bound exactly if \(\rho(G)<1\), and positive spectral bound if \(\rho(G)>1\). This proves the asserted local criterion.

**Step 3: An exact all-positive counterexample.** Set
\[
\begin{gathered}
\mu_h=\mu_r=1,\quad \theta_C=\theta_M=\theta_r=1,\quad
\theta_{CM}=4,\quad\phi_C=\phi_M=1,\\
\rho_C=\rho_M=2,\quad\delta_C=\delta_M=1,\quad
\rho_{CM}=\delta_{CM}=\tfrac14,\quad\delta_r=1,\\
\beta_a=7,\quad\beta_b=\beta_c=\beta_r=1.
\end{gathered}
\]
Choose the remaining positive rates, recruitment parameters and admissible fractions, for example, all recovery and waning rates equal to one, all mortality-reduction and cross-susceptibility factors equal to one-half, and the sequential-recovery fraction equal to one-half. Then
\[
G=\begin{pmatrix}
329/180&56/45&0\\8/45&47/180&1/4\\0&0&1/4
\end{pmatrix},\quad
\mathcal R_{\mathrm{full}}=\frac{47}{45}+\frac{\sqrt{27049}}{180}>\frac{329}{180}>1.
\]
By contrast, the three printed separate-model reproduction numbers [1, Sections 3.1, 3.2, 3.3] equal
\[
\mathcal R_C=\frac78,\qquad \mathcal R_M=\frac18,\qquad
\mathcal R_r=\frac14,
\]
so their proposed maximum is \(7/8<1\), while the actual equilibrium is linearly unstable. The strict inequalities persist on an open neighborhood of this positive parameter vector.

**Step 4: Why separate submodels cannot replace this computation.** Even if every Mpox transmission coefficient is set to zero and an exposed COVID class is positive, the printed equation gives \(\dot E_{CM}=\phi_C E_C>0\) at a nominally Mpox-free state. Likewise, \(\phi_M E_M>0\) creates co-exposure from an Mpox-only state. Thus those putative single-pathogen faces are not invariant at positive \(\phi_C,\phi_M\), which explains why deleting the cross-progressions before forming the next-generation matrix changes the threshold.

## Verification
Run the standalone exact-symbolic script `python verify.py` with SymPy. It constructs the eight-by-eight matrices \(F,V\) from the displayed equations, evaluates the relevant block of \(FV^{-1}\), checks every symbolic entry against \(G\), substitutes the positive rational witness, and checks all published and corrected inequalities. The observed replay output begins `VERIFY_OK`; its exact matrix and Perron eigenvalue agree with the expressions above. The general step that translates the next-generation spectral radius into a local stability boundary is the standard theorem in [2,3], not a finite simulation claim.

## Relationship to prior work
Acheneje et al. [1, Eq. (1)] specify the cross-progression paths, but in Sections 3.1–3.3 replace their complete next-generation problem with the maximum of three separately computed component reproduction numbers. The matrix \(G\) above treats the source's *combined* linearization instead. Diekmann–Heesterbeek–Roberts [2] and van den Driessche–Watmough [3] give the general next-generation-matrix method; neither provides this source-specific reduced matrix or this positive-parameter contradiction. Mgonja et al. [4] analyze a different COVID–typhoid co-infection system using a combined reproduction operator, without deriving the present COVID–Mpox coefficients. General examples showing that coupling can invalidate maximum-of-isolated-subsystem bounds do not imply the specific formula or witness for [1].

## Limitations
This is an exact statement about the **equations as printed**, not a verified description of the simulation implementation or observed epidemic dynamics. The parameter witness proves linear instability and failure of the printed subcritical criterion; it does not establish endemic persistence, backward bifurcation, a numerical epidemic forecast, or what biological correction should replace the unforced cross-progression terms. At the equality threshold the theorem deliberately makes no stability assertion. Distinct authors might independently obtain the same calculation; search cannot establish uniqueness.

## References
[1] G. O. Acheneje et al., “Mathematical modelling on the transmission dynamics of the co-infection of COVID-19 and Monkeypox with treatment as a control strategy,” *Discover Public Health* 22, article 535 (published 11 September 2025), https://doi.org/10.1186/s12982-025-00893-z; especially Eq. (1), Sections 3.1–3.3 and Theorem 11.

[2] O. Diekmann, J. A. P. Heesterbeek, M. G. Roberts, “The construction of next-generation matrices for compartmental epidemic models,” *J. R. Soc. Interface* 7 (2010), 873–885, https://doi.org/10.1098/rsif.2009.0386.

[3] P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Math. Biosci.* 180 (2002), 29–48, https://doi.org/10.1016/S0025-5564(02)00108-6.

[4] D. S. Mgonja et al., “Mathematical modeling and analysis of COVID-19 and typhoid fever co-dynamics with treatment,” *Scientific Reports* 15, article 33206 (2025), https://doi.org/10.1038/s41598-024-82955-x.
