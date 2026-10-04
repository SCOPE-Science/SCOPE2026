# The aggregate hospital class destroys the COVID-free equilibrium
## Finding
Consider System (2.1) in Rao et al. (2026) exactly as printed. Assume \(\Lambda>0\), \(\beta_c>0\), \(\lambda_k>0\), \(\zeta_k>0\), \(0\le\varepsilon_v\le1\), and nonnegative states with \(N>0\). Then the system has no equilibrium with \(I_c=I_{ck}=0\). Thus, under the paper's positive-background-CKD regime, the printed system has no COVID-free equilibrium at all.

The obstruction is structural. The single hospitalized compartment \(H\) receives CKD-only hospitalizations through \(\zeta_k I_k\), while the entire \(H\) is simultaneously inserted into the COVID force of infection \(\beta_c(I_c+I_{ck}+H)/N\). Those two modeling choices prevent the COVID-free face from closing when \(\lambda_k>0\) and \(\zeta_k>0\).

In particular, the displayed point
\[
E_0=\left(\frac{\Lambda}{\eta+\mu},\frac{\eta\Lambda}{\mu(\eta+\mu)},0,0,0,0,0\right)
\]
is not a full-system equilibrium when \(\lambda_k>0\). At that point,
\[
\dot I_k=\frac{\lambda_k\Lambda}{\eta+\mu}>0.
\]
Therefore the local/global full-system stability statements formulated around \(E_0\) cannot apply to the printed calibrated system with positive background CKD incidence.

## Assumptions and scope
The state order is \(S,V,I_c,I_k,I_{ck},H,R\). The argument uses only the four printed equations needed below:
\[
\dot S=\Lambda+\pi R-\frac{\beta_c(I_c+I_{ck}+H)S}{N}-\lambda_kS-(\eta+\mu)S,
\]
\[
\dot I_c=\frac{\beta_c(I_c+I_{ck}+H)[S+(1-\varepsilon_v)V]}{N}-(\theta+\zeta_c+\gamma_c+\mu_c+\mu)I_c,
\]
\[
\dot I_k=\lambda_kS+\gamma_{ck}I_{ck}+(1-p)\gamma_hH-\frac{\alpha\beta_c(I_c+I_{ck}+H)I_k}{N}-(\zeta_k+\mu_k+\mu)I_k,
\]
and
\[
\dot H=\zeta_cI_c+\zeta_kI_k+\zeta_{ck}I_{ck}-(\gamma_h+\mu_h+\mu)H.
\]
All states are assumed nonnegative. The vaccine-efficacy range \(0\le\varepsilon_v\le1\) is the biological range used by the model. The theorem is about the printed equations, not about an intended unprinted split of the hospital population.

The strict assumptions \(\lambda_k>0\), \(\zeta_k>0\), and \(\beta_c>0\) matter. The proof does not assert the same obstruction on the special axes \(\lambda_k=0\), \(\zeta_k=0\), or \(\beta_c=0\).

## Proof
Suppose, toward a contradiction, that a nonnegative equilibrium satisfies \(I_c=I_{ck}=0\).

First, \(S>0\). If \(S=0\), then the printed susceptible equation reduces at equilibrium to
\[
\dot S=\Lambda+\pi R>0,
\]
because \(\Lambda>0\) and \(R\ge0\). Hence \(S=0\) is impossible at an equilibrium.

Second, the \(I_c\)-equation at \(I_c=I_{ck}=0\) becomes
\[
0=\frac{\beta_cH[S+(1-\varepsilon_v)V]}{N}.
\]
Here \(\beta_c>0\), \(N>0\), \(S>0\), \(V\ge0\), and \(0\le\varepsilon_v\le1\), so the bracket is strictly positive. Therefore \(H=0\).

Third, with \(I_c=I_{ck}=H=0\), the hospital equation becomes
\[
0=\zeta_kI_k.
\]
Since \(\zeta_k>0\), it follows that \(I_k=0\).

Finally, with \(I_c=I_{ck}=H=I_k=0\), the CKD equation reduces to
\[
0=\lambda_kS.
\]
But \(\lambda_k>0\) and the first step gave \(S>0\), a contradiction. Thus no equilibrium with \(I_c=I_{ck}=0\) exists.

The source's displayed \(E_0\) fails even more directly: substituting it into the printed \(I_k\)-equation leaves \(\dot I_k=\lambda_k\Lambda/(\eta+\mu)>0\).

## Verification
The proof is symbolic and does not depend on numerical simulation. A bundled standard-library checker verifies the exact residual at the paper's baseline positive parameters. Using the printed values \(\Lambda=0.89\), \(\eta=0.9\), \(\mu=0.0000425\), and \(\lambda_k=0.00234\), it obtains
\[
S^0=\frac{356000}{360017}
\]
and
\[
\left.\dot I_k\right|_{E_0}=\frac{20826}{9000425}>0.
\]
The checker also verifies positivity of the baseline \(\beta_c\) and \(\zeta_k\) used in the theorem.

## Relationship to prior work
Rao et al. explicitly note that their aggregate hospitalized class contains both COVID-active and CKD-only hospitalized patients, while only the COVID-active subpopulation is biologically infectious. Nevertheless, System (2.1) inserts the whole \(H\) into the COVID force of infection. The same paper's CKD-only submodel separately recognizes a positive CKD background when \(\lambda_k>0\), making the incompatibility in the full-system disease-free point especially consequential.

A related 2024 COVID-19/CKD co-infection model by Hye et al. uses a COVID force of infection built from explicitly COVID-infected compartments rather than an aggregate hospitalized CKD pool. It therefore does not imply this obstruction. The standard next-generation framework of van den Driessche and Watmough assumes a genuine disease-free equilibrium before its threshold theorem is applied; it likewise does not contain the source-specific contradiction proved here.

The closest semantic records checked concerned coupled SEIR movement, dengue switching, a reaction-diffusion boundary basin, resource-coupled mortality, and chemotactic parabolicity. None contains a statement that implies the no-COVID-free-equilibrium result for this printed COVID-19/CKD system.

## Limitations
The result diagnoses the printed 2026 system only. It does not compute a replacement reproduction number or prove stability of a repaired model. A natural repair is to split \(H\) into COVID-active and CKD-only hospital states, or otherwise remove CKD-only hospitalization from the COVID force of infection, and then linearize COVID invasion about the actual CKD-background equilibrium.

The theorem does not cover the special parameter axes \(\lambda_k=0\), \(\zeta_k=0\), or \(\beta_c=0\). It also does not claim that every intended interpretation of the authors' prose is inconsistent; it establishes a precise obstruction for System (2.1) as written.

## References
1. M. A. Rao, E. K. Jaradat, M. P. Devi, P. B. Dhandapani, C. Martin-Barreiro, and M. Al-Hmoud, “Mathematical modeling of COVID-19 and chronic kidney disease co-infection with vaccination and optimal control: a bifurcation and sensitivity analysis approach,” *AIMS Mathematics* 11(6), 17239–17292 (2026), DOI 10.3934/math.2026707. Published 15 June 2026.
2. M. A. Hye et al., “Mathematical modeling of the co-infection dynamics of COVID-19 and kidney failure,” *Scientific Reports* 14 (2024), DOI 10.1038/s41598-024-56399-2.
3. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Mathematical Biosciences* 180 (2002), 29–48, DOI 10.1016/S0025-5564(02)00108-6.
