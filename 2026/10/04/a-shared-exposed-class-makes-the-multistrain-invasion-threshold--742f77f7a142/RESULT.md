# A shared exposed class makes the multistrain invasion threshold additive
## Finding
For the Casimir--Abibelaye--Somdouda system (2.1)--(2.6), let \(\phi=\sum_{j=1}^n\varphi_j\), \(a_E=\mu+\phi\), \(a_j=\mu+\mu_j+\gamma_j\), \(b=\mu+\delta_1+\gamma\), and \(\kappa=\beta(S^0+D^0)/N^0=\beta\). With infected coordinates \(E,I_1,\ldots,I_n,C\), only the inflow into \(E\) is a new-infection term, so the epidemiological next-generation matrix has rank one and the disease-free invasion threshold is \[\mathcal R_*=\frac{\kappa}{a_E}\left(\alpha\sum_{j=1}^n\frac{\varphi_j}{a_j}+\frac{(1-\alpha)\phi}{b}\right).\] The disease-free equilibrium is locally asymptotically stable exactly when \(\mathcal R_*<1\). Equation (3.8) instead gives \(\mathcal R_{\mathrm{print}}=\max_j\sqrt{A+B_j}\), where \(A=\kappa(1-\alpha)\phi/(ba_E)\) and \(B_j=\kappa\alpha\varphi_j/(a_ja_E)\). Thus for \(n\ge2\) the printed criterion can declare stability while the actual infected linearization is unstable; for example, \(n=2\), \(\alpha=1/2\), \(\mu=1\), \(\varphi_1=\varphi_2=1\), \(\mu_j=\gamma_j=1\), \(\delta_1=\gamma=1\), and \(\beta=5\) give \(\mathcal R_{\mathrm{print}}=\sqrt{5/6}<1\) but \(\mathcal R_*=10/9>1\), with infected eigenvalue \(-3+\sqrt{10}>0\).

## Assumptions and scope
Consider the deterministic system (2.1)--(2.6) of Casimir, Abibelaye, and Somdouda with \(n\ge1\), positive demographic and removal rates, \(0\le\alpha\le1\), and \(\varphi_j\ge0\). Write
\[
\phi=\sum_{{j=1}}^n\varphi_j,\qquad
a_E=\mu+\phi,\qquad
a_j=\mu+\mu_j+\gamma_j,\qquad
b=\mu+\delta_1+\gamma.
\]
At the disease-free equilibrium, \(E=I_1=\cdots=I_n=C=R=0\), so equation (2.7) gives \(N^0=S^0+D^0\). Hence
\[
\kappa:=\frac{\beta(S^0+D^0)}{{N^0}}=\beta.
\]
The claim concerns only the local disease-free invasion threshold and the corresponding local stability statement. It does not assess endemic equilibria, extinction theorems away from the disease-free linearization, numerical fits, or the optimal-control section.

## Proof
Use the infected coordinate vector \(x=(E,I_1,\ldots,I_n,C)^\top\). The model linearized at the disease-free equilibrium has infected block
\[
\dot E=-a_EE+\kappa\left(\sum_{{j=1}}^n I_j+C\right),
\]
\[
\dot I_j=\alpha\varphi_jE-a_jI_j,\qquad
\dot C=(1-\alpha)\phi E-bC.
\]
In the next-generation construction, a term belongs to the new-infection vector only when it creates newly infected individuals. The terms \(\alpha\varphi_jE\) and \((1-\alpha)\phi E\) move already infected exposed individuals into later infected states; they are transfers, not new infections. Therefore the new-infection Jacobian has only its first row nonzero:
\[
F=\begin{{pmatrix}}
0&\kappa&\cdots&\kappa&\kappa\\
0&0&\cdots&0&0\\
\vdots&\vdots&&\vdots&\vdots\\
0&0&\cdots&0&0
\end{{pmatrix}}.
\]
The transfer matrix is lower triangular:
\[
V=\begin{{pmatrix}}
a_E&0&\cdots&0&0\\
-\alpha\varphi_1&a_1&\cdots&0&0\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
-\alpha\varphi_n&0&\cdots&a_n&0\\
-(1-\alpha)\phi&0&\cdots&0&b
\end{{pmatrix}}.
\]
Its first column in \(V^{{-1}}\) is
\[
\left(\frac1{{a_E}},
\frac{{\alpha\varphi_1}}{{a_Ea_1}},\ldots,
\frac{{\alpha\varphi_n}}{{a_Ea_n}},
\frac{{(1-\alpha)\phi}}{{a_Eb}}\right)^\top.
\]
Thus \(FV^{{-1}}\) has rank at most one and its only possible nonzero eigenvalue is its \((1,1)\) entry,
\[
\mathcal R_*=
\frac{{\kappa}}{{a_E}}
\left(
\alpha\sum_{{j=1}}^n\frac{{\varphi_j}}{{a_j}}
+\frac{{(1-\alpha)\phi}}{{b}}
\right).
\]
This is nonnegative, so it is the spectral radius.

The same threshold follows directly from the infected Jacobian. For any real \(z> -\min\{{a_1,\ldots,a_n,b\}}\), an eigenvector with nonzero exposed component must satisfy
\[
I_j=\frac{{\alpha\varphi_j}}{{z+a_j}}E,\qquad
C=\frac{{(1-\alpha)\phi}}{{z+b}}E,
\]
so its real characteristic equation is
\[
g(z):=z+a_E-\kappa\left(
\alpha\sum_{{j=1}}^n\frac{{\varphi_j}}{{z+a_j}}
+\frac{{(1-\alpha)\phi}}{{z+b}}
\right)=0.
\]
On that interval,
\[
g'(z)=1+\kappa\left(
\alpha\sum_{{j=1}}^n\frac{{\varphi_j}}{{(z+a_j)^2}}
+\frac{{(1-\alpha)\phi}}{{(z+b)^2}}
\right)>0,
\]
and
\[
g(0)=a_E(1-\mathcal R_*).
\]
Because the infected block is Metzler, its spectral bound is a real eigenvalue. Hence the infected block is Hurwitz exactly when \(\mathcal R_*<1\). The disease-free demographic block has diagonal eigenvalues \(-\mu-\lambda\), \(-\mu-\delta_2\), and \(-\mu-\delta\), so the full disease-free equilibrium has the same threshold.

To compare with equation (3.8), define
\[
A=\frac{{\kappa(1-\alpha)\phi}}{{ba_E}},\qquad
B_j=\frac{{\kappa\alpha\varphi_j}}{{a_ja_E}}.
\]
Then the correct threshold is
\[
\mathcal R_*=A+\sum_{{j=1}}^nB_j,
\]
whereas the printed quantity is
\[
\mathcal R_{{\mathrm{print}}}=\max_j\sqrt{{A+B_j}}.
\]
For \(n=1\), \(\mathcal R_*=\mathcal R_{{\mathrm{print}}}^2\), so both quantities cross one at the same parameter value. For \(n\ge2\) with at least two positive \(B_j\), the two threshold statements differ: \(A+\sum_jB_j>A+\max_jB_j\), so there is a nonempty transmission-rate interval in which \(\mathcal R_{{\mathrm{print}}}<1<\mathcal R_*\).

For an exact witness choose \(n=2\), \(\alpha=1/2\), \(\mu=1\), \(\varphi_1=\varphi_2=1\), \(\mu_1=\mu_2=1\), \(\gamma_1=\gamma_2=1\), \(\delta_1=1\), \(\gamma=1\), and \(\beta=5\). All remaining demographic parameters may be any positive values. Then \(a_E=a_1=a_2=b=3\),
\[
A=\frac59,\qquad B_1=B_2=\frac5{{18}},
\]
so
\[
\mathcal R_{{\mathrm{print}}}=\sqrt{{\frac56}}<1,
\qquad
\mathcal R_*=\frac{{10}}9>1.
\]
The infected matrix is
\[
\begin{{pmatrix}}
-3&5&5&5\\
1/2&-3&0&0\\
1/2&0&-3&0\\
1&0&0&-3
\end{{pmatrix}}.
\]
Writing \(q=z+3\), its nontrivial characteristic factor is \(q^2-10\), hence it has the positive eigenvalue \(-3+\sqrt{{10}}>0\). The printed criterion therefore gives the wrong local-stability verdict for this admissible two-strain instance.

## Verification
The algebra above was independently replayed with exact rational arithmetic in `verify.py`. The script verifies the rank-one threshold decomposition, the exact values \(A=5/9\), \(B_1=B_2=5/18\), \(\mathcal R_*=10/9\), the inequality \(\mathcal R_{{\mathrm{print}}}^2=5/6<1\), and the characteristic factor \((z+3)^2-10\). A successful replay prints `VERIFY_OK`.

The finite replay is a check of the displayed witness, not the proof of the all-parameter formula; that formula follows from the symbolic next-generation and characteristic-equation derivations above.

## Relationship to prior work
Casimir, Abibelaye, and Somdouda define the infected classes as \(E,I_j,C\), but their displayed new-infection vector includes the progression terms \(\alpha\varphi_jE\) and \((1-\alpha)\phi E\). Their equation (3.8) consequently reports a maximum of square-root expressions and Theorem 3.4 uses that quantity as the local disease-free threshold.

The standard next-generation construction instead separates appearance of genuinely new infections from transfers among infected compartments. Brouwer's exposition of the method makes this distinction explicit and identifies \(FV^{{-1}}\) as counting new infections generated during residence in infected states. Applying that definition to the published equations yields the rank-one matrix above.

Published multistrain SEIR models with strain-specific exposed classes are not equivalent to this source's single shared exposed compartment. For example, Arruda et al. use separate \(E_j\) and \(I_j\) states for each strain. Their architecture therefore does not imply the additive shared-exposure formula proved here.

Semantic searches for the source DOI, the printed maximum-square-root expression, shared/common exposed-compartment aliases, and progression-versus-new-infection formulations found no statement equivalent to the formula and counterexample above. The nearest indexed result concerned patch-coupled SEIR movement and does not contain a shared exposed class or this next-generation split.

## Limitations
The result is local and deterministic. It corrects the invasion threshold for the equations exactly as printed; it does not decide whether the single exposed class is the intended biological architecture, nor does it revise any separate model the authors might have intended. It does not prove global persistence, endemic-equilibrium uniqueness, or validity or invalidity of the paper's later optimal-control calculations.

The general next-generation literature establishes the methodological rule used here, but the source-specific additive formula and exact false-stability witness are deductions from the 2026 model equations. No independent audit has been performed.

## References
1. M. Casimir, S. M. Abibelaye, and S. Somdouda, “Modeling and Optimal Control of a Multi-Strain Epidemic Applied to COVID-19 with an Underlying Chronic Disease Condition,” *Asia Pacific Journal of Mathematics* 13 (2026), article 47. DOI:10.28924/APJM/13-47.
2. A. F. Brouwer, “Why the Spectral Radius? An intuition-building introduction to the basic reproduction number,” *Bulletin of Mathematical Biology* 84 (2022), 96. DOI:10.1007/s11538-022-01057-9.
3. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Mathematical Biosciences* 180 (2002), 29–48.
4. E. F. Arruda et al., “Modelling and optimal control of multi strain epidemics, with application to COVID-19,” *PLOS ONE* 16 (2021), e0257512. DOI:10.1371/journal.pone.0257512.
