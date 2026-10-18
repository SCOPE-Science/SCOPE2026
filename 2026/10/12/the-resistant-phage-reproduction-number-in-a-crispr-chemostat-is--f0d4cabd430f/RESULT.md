# Correcting the resistant-phage invasion threshold in a CRISPR chemostat

## Finding
In the chemostat system of Shu, Fu, and Wang, *A bacteriophage model based on CRISPR/Cas immune system in a chemostat* (2017), the printed resistant-phage reproduction number omits a factor of the adsorption coefficient \(k\). With the paper's convention of writing a square-root two-stage threshold, the correct quantity at the resistant-only, phage-free equilibrium is
\[
\widehat{\mathcal R}_0^M
=\sqrt{\frac{b\delta\kappa k M_2}{(D+\delta)(D+k M_2)}},
\qquad M_2=R^0-\lambda_2,
\qquad \lambda_2=\frac{Da}{\mu m-D}.
\]
The corresponding conventional next-generation spectral radius is **the square** of this displayed quantity, not the square root:
\[
\rho(FV^{-1})=(\widehat{\mathcal R}_0^M)^2.
\]
Both have the same threshold at one. The source instead prints the above square-root expression **without** \(k\) in the numerator. This discrepancy changes its literal threshold-based existence claim.

For instance, the strictly positive parameters
\[
D=\delta=a=1,\quad b=10,\quad k=\tfrac1{100},\quad
\kappa=\mu=\epsilon=\tfrac12,\quad m=4,\quad R^0=11
\]
meet the source's resistant equilibrium assumptions. Here \(\lambda_2=1\), \(M_2=10\), and
\[
(\mathcal R_{0,\mathrm{printed}}^M)^2=\tfrac{250}{11}>1,
\qquad (\widehat{\mathcal R}_0^M)^2=\tfrac5{22}<1.
\]
The phage invasion block is Hurwitz, and no strictly positive resistant-phage equilibrium \(E_3\) of the source's stated form exists, despite the **printed** threshold exceeding one. Inserting the missing \(k\) also restores the source's own later equilibrium identity.

## Definitions and scope
The five-compartment model has resource \(R\), susceptible bacteria \(S\), resistant bacteria \(M\), infected cells \(I\), and free phage \(P\). The model's resistant infection coefficient is \(k'=\kappa k\), and resistant phage adsorption removes phage at rate \(kMP\). The growth law is the Monod function \(f(R)=mR/(a+R)\), with \(0<\kappa\le1\), \(0<\mu<1\), all kinetic parameters positive. The resistant-only phage-free equilibrium is \(E_2=(\lambda_2,0,M_2,0,0)\). The correction is about its resistant/phage invasion threshold and the theorem's literal use of the printed formula. It does not assert complete stability of \(E_2\) against susceptible-strain perturbations or invalidate every numerical result in the source.

## Proof
At \(E_2\), the linearized infected-cell/free-phage system is
\[
\begin{pmatrix}\dot I\\\dot P\end{pmatrix}
=\begin{pmatrix}-(D+\delta)&\kappa kM_2\\ b\delta&-(D+kM_2)\end{pmatrix}
\begin{pmatrix}I\\P\end{pmatrix}.
\]
Under the standard next-generation decomposition, write
\[
F=\begin{pmatrix}0&\kappa kM_2\\0&0\end{pmatrix},
\qquad V=\begin{pmatrix}D+\delta&0\\-b\delta&D+kM_2\end{pmatrix}.
\]
Direct multiplication gives the eigenvalues of \(FV^{-1}\) as zero and
\[
\frac{b\delta\kappa kM_2}{(D+\delta)(D+kM_2)}.
\]
Thus its spectral radius is precisely the displayed ratio, whereas the source's two-stage square-root convention gives \(\widehat{\mathcal R}_0^M\) above. Both yield the same invasion test
\[
\det J_{IP}=(D+\delta)(D+kM_2)-b\delta\kappa kM_2>0,
\]
because the trace of \(J_{IP}\) is always negative.

The source itself defines \(A_2=b\delta\kappa/(D+\delta)-1\) and asserts an identity involving \(G(\lambda_2)=-D+kA_2M_2\). Algebraically,
\[
-D+kA_2M_2
=(D+kM_2)\bigl((\widehat{\mathcal R}_0^M)^2-1\bigr).
\]
The identity is false if the printed square of the reproduction number is used without \(k\).

For the stated witness, \(\mu m=2>D=1\), and \(\mu f(R^0)=11/6>1\). Its infection block is
\[
J_{IP}=\begin{pmatrix}-2&1/20\\10&-11/10\end{pmatrix},
\quad \operatorname{tr}J_{IP}=-31/10<0,
\quad\det J_{IP}=17/10>0.
\]
So small phage perturbations of the resistant equilibrium decay.

Further, the paper's positive resistant-phage equilibrium \(E_3=(R_3,0,M_3,I_3,P_3)\) requires \(kA_2M_3=D\). Since the witness has \(A_2=3/2\), this gives \(M_3=200/3\). On the other hand, positivity of \(P_3\) implies \(\mu f(R_3)>D\) and therefore \(R_3>\lambda_2=1\). Nutrient balance implies
\[
M_3=\frac{D(R^0-R_3)}{\mu f(R_3)}<R^0-R_3<10,
\]
contradicting \(M_3=200/3\). This disproves the literal implication from the **printed** \(\mathcal R_0^M>1\) to existence of \(E_3\), without claiming that the correctly interpreted threshold theorem is false.

## Verification and relationship to prior work
All numerical witnesses above use exact rational arithmetic. The model's infected-cell and phage equations, the omitted adsorption coefficient, the published definition of the reproduction number, the subsequent \(G(\lambda_2)\) identity, and the existence theorem were checked against the 2017 paper, including its original mathematical PDF. The exact spectral-radius calculation distinguishes the next-generation spectral radius from its square root, avoiding a conflation of these two normalizations.

Van den Driessche and Watmough (2002) establish the general next-generation framework; it supplies the standard calculation but does not identify this source-specific missing factor. Han and Smith (2012) describe the predecessor chemostat model, not this specific CRISPR threshold misprint. A later author clarification or unindexed erratum remains possible; no such correction was located in the checked searches.

## Limitations
The corrected expression is not a new general theorem on chemostat thresholds. The contribution is the precise source-specific formula diagnosis and a strict admissible counterexample to reading the associated printed existence statement literally. The source's downstream equilibrium algebra already appears to use the corrected coefficient, so not all of its results are thereby invalidated. The linear invasion block does not establish stability to all five-variable perturbations.

## References
1. M. Shu, R. Fu and W. Wang, *A bacteriophage model based on CRISPR/Cas immune system in a chemostat*, Mathematical Biosciences and Engineering **14** (2017), 1361–1377, DOI: 10.3934/mbe.2017070.
2. P. van den Driessche and J. Watmough, *Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission*, Mathematical Biosciences **180** (2002), 29–48, DOI: 10.1016/S0025-5564(02)00108-6.
3. Z. Han and H. L. Smith, *Bacteriophage-resistant and bacteriophage-sensitive bacteria in a chemostat*, Mathematical Biosciences and Engineering **9** (2012), 737–765, DOI: 10.3934/mbe.2012.9.737.
