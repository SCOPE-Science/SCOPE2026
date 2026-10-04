# The reinfection threshold globally excludes subcritical endemic equilibria
## Finding
Consider the SEIRV model
\[
\begin{aligned}
S'&=\Lambda-\beta_1SI-(\alpha+\mu)S,\\
E'&=\beta_1SI+\beta_1\sigma IV+\beta_2RI-(\gamma+\mu)E,\\
I'&=\gamma E-(\delta+\mu+\theta)I,\\
R'&=\delta I-\beta_2RI-\mu R,\\
V'&=\alpha S-\beta_1\sigma IV-\mu V.
\end{aligned}
\]
Assume all rate parameters are positive and \(0<\sigma\le 1\). Let \(\beta_1^\ast\) denote the value of \(\beta_1\) at which the paper’s reproduction number satisfies \(R_0=1\), and let \(\beta_2^\ast\) be the reinfection threshold defined in its Equation (5.2). Then
\[
R_0\le 1,\qquad 0<\beta_2\le\beta_2^\ast
\quad\Longrightarrow\quad
\text{there is no positive endemic equilibrium.}
\]
Thus the first assertion in the paper’s Numerical Finding 7.1—absence of subcritical endemic equilibria when \(\beta_2\le\beta_2^\ast\)—is exact, and the exclusion also holds at \(R_0=1\).

## Assumptions and scope
Write
\[
A=\alpha+\mu,\qquad M=\mu+\alpha\sigma,\qquad
K=\frac{(\gamma+\mu)(\delta+\mu+\theta)}{\gamma},\qquad H=K-\delta.
\]
The source notes \(H>0\). Define
\[
P=\mu^2+\alpha^2\sigma^2+\alpha\mu\sigma(1+\sigma).
\]
The source thresholds can be written
\[
\beta_1^\ast=\frac{A\mu K}{\Lambda M},\qquad
\beta_2^\ast=\beta_1^\ast\frac{K}{\delta}\frac{P}{AM},
\]
and its reproduction number is \(R_0=\beta_1/\beta_1^\ast\). The result concerns positive equilibria only. It does not establish global attraction of the disease-free equilibrium, exclude periodic or other non-equilibrium invariant sets, or address parameter regimes with \(\beta_2>\beta_2^\ast\).

## Proof
The source’s Lemma B.1 gives a one-to-one correspondence between positive endemic equilibria and positive roots \(I>0\) of
\[
F(I;\beta,B)=
\frac{\Lambda\beta(M+\beta\sigma I)}{(A+\beta I)(\mu+\beta\sigma I)}
+\frac{\delta BI}{\mu+BI}-K,
\]
where \(\beta=\beta_1\) and \(B=\beta_2\).

For every fixed \(I>0\), the function is strictly increasing in both control parameters. Direct differentiation gives
\[
\frac{\partial F}{\partial B}
=\frac{\delta\mu I}{(\mu+BI)^2}>0
\]
and, using \(M=\mu+\alpha\sigma\) and \(A=\alpha+\mu\),
\[
\frac{\partial F}{\partial\beta}
=
\frac{\Lambda\mu\left(AM+2A\beta\sigma I+\beta^2\sigma^2I^2\right)}
{(A+\beta I)^2(\mu+\beta\sigma I)^2}>0.
\]
Consequently, whenever \(\beta\le\beta_1^\ast\) and \(B\le\beta_2^\ast\),
\[
F(I;\beta,B)\le F(I;\beta_1^\ast,\beta_2^\ast).
\]
It remains to determine the sign at this upper-right corner.

Set
\[
D(I)=(A+\beta_1^\ast I)(\mu+\beta_1^\ast\sigma I)(\mu+\beta_2^\ast I)>0.
\]
Substitution of the two threshold formulas followed by exact expansion gives
\[
D(I)F(I;\beta_1^\ast,\beta_2^\ast)
=-\frac{I^2K(\beta_1^\ast)^2}{AM^2\delta}\left(C_0+C_1I\right),
\]
where
\[
C_1=M\beta_1^\ast\sigma HP>0
\]
and
\[
C_0=HP^2+A\delta\mu\sigma(M-\mu)(M-A\sigma).
\]
Because
\[
M-\mu=\alpha\sigma>0,\qquad M-A\sigma=\mu(1-\sigma)\ge0,
\]
we have \(C_0>0\). Hence
\[
F(I;\beta_1^\ast,\beta_2^\ast)<0\qquad\text{for every }I>0.
\]
Monotonicity then gives \(F(I;\beta,B)<0\) for every \(I>0\) throughout \(\beta\le\beta_1^\ast\), \(B\le\beta_2^\ast\). By Lemma B.1 there is no positive endemic equilibrium there. Since \(R_0=\beta_1/\beta_1^\ast\), this is exactly the stated result.

## Verification
The proof is algebraic and does not rely on finite enumeration. The bundled `verify.py` re-evaluates the threshold definitions and the corner factorization with exact rational arithmetic for several nondegenerate rational parameter sets, then checks the parameter monotonicity inequality on exact rational test points. These calculations are consistency checks; the universal conclusion follows from the displayed symbolic identities and sign arguments above.

Boundary stress tests are explicit in the proof. At \(\sigma=1\), the second summand in \(C_0\) vanishes but \(HP^2>0\), so the conclusion remains strict. At \(R_0=1\) and \(\beta_2=\beta_2^\ast\), the scalar equation is tangent at \(I=0\) but is strictly negative for every \(I>0\). No inference about global disease-free convergence is made from equilibrium exclusion alone.

## Relationship to prior work
Khan, Wang, Liu, and Xiong derive the scalar equilibrium equation, the local bifurcation threshold \(\beta_2^\ast\), and a lower critical threshold when \(\beta_2>\beta_2^\ast\). Their Numerical Finding 7.1 states that simulations suggest no subcritical endemic equilibrium when \(\beta_2\le\beta_2^\ast\); it is not given as a theorem. The result above proves exactly that equilibrium-exclusion statement by combining parameter monotonicity with a factorization at the codimension-two corner.

Earlier reinfection models establish related forward/backward-bifurcation thresholds for different compartment structures. Wang et al. study an SEIRE model with a basic reinfection number and a lower critical threshold, while Wangari studies a different SEIR model with exogenous reinfection. Sulayman, Abdullah, and Mohd study an SVEIRE tuberculosis model. These works motivate the phenomenon but do not state the threshold identity or corner factorization for the present SEIRV equations.

## Limitations
The theorem excludes positive endemic equilibria; it does not prove that every trajectory converges to the disease-free equilibrium. In particular, the second, dynamical sentence of Numerical Finding 7.1 remains outside the claim. The proof uses the source model exactly as written, assumes \(0<\sigma\le1\), and does not address extensions with waning vaccine compartments, additional strains, delays, stochastic forcing, or alternative incidence functions.

The literature comparison is necessarily bounded by accessible and indexed sources. No correction or later source was found that already promotes this exact source-specific numerical observation to the stated theorem, but absence from the searches is not a proof of universal novelty.

## References
1. A. Khan, L. Wang, J. Liu, and M. Xiong, “Dynamics of an SEIRV endemic model: effects of reinfection,” *Journal of Biological Dynamics* 20 (2026), Article 2713881. DOI: 10.1080/17513758.2026.2713881. Published online 2026-08-08.
2. S. Wang, T. Wang, Y. Qi, and F. Xu, “Backward bifurcation, basic reinfection number and robustness of a SEIRE epidemic model with reinfection,” arXiv:2205.07258.
3. W. Wangari, “Condition for Global Stability for a SEIR Model Incorporating Exogenous Reinfection and Primary Infection Mechanisms,” *Computational and Mathematical Methods in Medicine* (2020), Article 9435819.
4. F. Sulayman, F. A. Abdullah, and M. H. Mohd, “An SVEIRE Model of Tuberculosis to Assess the Effect of an Imperfect Vaccine and Other Exogenous Factors,” *Mathematics* 9 (2021), 327.
