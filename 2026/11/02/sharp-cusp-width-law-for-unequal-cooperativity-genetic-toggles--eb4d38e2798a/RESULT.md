# Sharp cusp-width law for unequal-cooperativity genetic toggles

## Finding

In the classical dimensionless two-repressor toggle of Gardner, Cantor and Collins, allow the two positive Hill exponents to be arbitrary and unequal. At the least synthesis rate where two asymptotically stable states are possible, the admissible interval of the second synthesis rate opens with a **sharp, explicit three-halves power law**. The result gives the quantitative prefactor and the first-order synthesis-balance line, not merely the qualitative existence of the previously known cusp.

Let \(p,q>0\), \(r=pq>1\), and write
\[
x_c=\left(\frac{q+1}{r-1}\right)^{1/q},\quad
y_c=\left(\frac{p+1}{r-1}\right)^{1/p},\quad
\alpha_c=p x_c^{q+1},\quad \beta_c=q y_c^{p+1}.
\]
Define \(D=p(r-1)x_c^{2q-1}>0\) and the explicit coefficient
\[
\boxed{C_{p,q}=\frac{4q}{3p x_c^2 y_c^{p-1}}\sqrt{\frac{2}{p(r-1)x_c^{2q-1}}}>0.}
\]
For \(\alpha=\alpha_c+\varepsilon\), \(\varepsilon\downarrow0\), the two fold synthesis rates obey
\[
\boxed{\beta_\pm(\alpha_c+\varepsilon)=\beta_c+\frac{q y_c}{p x_c}\varepsilon\ \pm\ \frac{C_{p,q}}2\varepsilon^{3/2}+O_{p,q}(\varepsilon^2).}
\]
Consequently, the open interval of \(\beta\) producing precisely two asymptotically stable positive equilibria has **width**
\[
\boxed{\beta_+(\alpha_c+\varepsilon)-\beta_-(\alpha_c+\varepsilon)=C_{p,q}\varepsilon^{3/2}+O_{p,q}(\varepsilon^2).}
\]
The coefficient is sharp in the sense of a positive limit after division by \(\varepsilon^{3/2}\). For equal Hill exponents \(p=q=2\), it becomes exactly \(C_{2,2}=4/(3\sqrt3)\).

## Assumptions and scope

The model is the autonomous system on the positive quadrant
\[
\dot x=\frac{\alpha}{1+y^p}-x,\qquad
\dot y=\frac{\beta}{1+x^q}-y,
\]
with synthesis rates \(\alpha,\beta>0\) and real Hill exponents \(p,q>0\). Units and degradation rates have been normalized to one, as in the cited original model. The result classifies **positive equilibria**, their linear types, and the local geometry of the synthesis-rate bistable window. It makes no claims about stochastic switching rates, biochemical calibration, inducer effects, or transcriptional noise. The asymptotic remainder is for fixed \(p,q\) with \(pq>1\); it is not uniform as \(pq\downarrow1\).

The complete threshold construction used in the proof is as follows. If \(pq\le1\), every positive synthesis-rate pair has exactly one positive equilibrium. If \(pq>1\), again there is exactly one for every \(\alpha\le\alpha_c\). If \(\alpha>\alpha_c\), set
\[
F(x)=\frac{pq x^{q+1}}{(pq-1)x^q-1},\quad x>(pq-1)^{-1/q}.
\]
There are exactly two solutions \(x_-<x_c<x_+\) to \(F(x)=\alpha\); both lie below \(\alpha\). With
\[
B_\alpha(x)=\left(\frac\alpha x-1\right)^{1/p}(1+x^q),\qquad
\beta_-=B_\alpha(x_-),\quad\beta_+=B_\alpha(x_+),
\]
one has \(0<\beta_-<\beta_+\). For \(\beta\in(\beta_-,\beta_+)\) there are three positive equilibria (two attracting and one saddle); for \(\beta\) outside the closed interval there is one attracting equilibrium. At either boundary \(\beta=\beta_\pm\) there are two distinct equilibria, one nonhyperbolic, with Jacobian eigenvalues \(0,-2\). At the cusp \((\alpha_c,\beta_c)\), the single equilibrium is nonhyperbolic, with the same two eigenvalues. These global equilibrium-count statements are provided to specify the width, not presented as the novel contribution independently of previous bifurcation literature.

## Proof

**1. Exact elimination and fold structure.** The first steady-state equation gives \(y=(\alpha/x-1)^{1/p}\), where \(0<x<\alpha\); substituting into the second yields \(\beta=B_\alpha(x)\). Direct differentiation gives
\[
\frac{B_\alpha'(x)}{B_\alpha(x)}=
\frac{\alpha[(pq-1)x^q-1]-pq x^{q+1}}
{p x(\alpha-x)(1+x^q)}.
\]
For \(pq\le1\) the numerator is negative. For \(pq>1\) it is also negative for \(x\le(pq-1)^{-1/q}\). Above this threshold its sign is that of \(\alpha-F(x)\). A second differentiation gives
\[
F'(x)=\frac{pq x^q[(pq-1)x^q-(q+1)]}{[(pq-1)x^q-1]^2}.
\]
Thus \(F\) decreases and then increases with unique minimum at \(x_c\), and \(F(x_c)=\alpha_c\). If \(\alpha>\alpha_c\), the two roots \(x_-\), \(x_+\) of \(F(x)=\alpha\) satisfy \(x_\pm<\alpha\), because \(F(x)>x\). The sign pattern of \(B_\alpha'\) is negative, positive, negative, proving the stated single/three/two-root counts and \(\beta_-<\beta_+\).

**2. Linear stability.** At a positive equilibrium, the Jacobian has trace \(-2\) and determinant
\[
\det J=1-\frac{pq x^q y^p}{(1+x^q)(1+y^p)}
=-\frac{p x y^{p-1}}{(1+y^p)(1+x^q)}B_\alpha'(x).
\]
Hence negative-slope equilibria are linearly asymptotically stable (both eigenvalues have negative real part), while the middle positive-slope equilibrium is a saddle. At each stationary point of \(B_\alpha\), the eigenvalues are exactly \(0,-2\). No claim of hyperbolicity is made at folds or at the cusp.

**3. Sharp cusp expansion.** Fix \(p,q>0\) with \(pq>1\). Denote \(\alpha=\alpha_c+\varepsilon\) and \(s=x-x_c\). The derivative of \(F\) vanishes at \(x_c\) and its curvature is
\[
D=F''(x_c)=p(pq-1)x_c^{2q-1}>0.
\]
Smoothness at the strictly positive cusp point implies the two fold positions satisfy
\[
x_\pm=x_c\pm\sqrt{2\varepsilon/D}+O_{p,q}(\varepsilon).
\]
On the \(O(\sqrt\varepsilon)\) scale between them, factor the exact numerator of \(B_\alpha'\) as \([(pq-1)x^q-1](\alpha-F(x))\), and Taylor-expand its positive prefactor. Uniformly in that interval,
\[
B_\alpha'(x)=K\left[\varepsilon-\frac D2s^2\right]+O_{p,q}(\varepsilon^{3/2}),\qquad K=\frac{q}{p x_c^2 y_c^{p-1}}>0.
\]
Integrating from \(x_-\) to \(x_+\), the error contributes \(O(\varepsilon^2)\), while the leading polynomial integral equals
\[
\frac43 K\sqrt{2/D}\,\varepsilon^{3/2}.
\]
This proves the positive sharp width coefficient \(C_{p,q}=\frac43 K\sqrt{2/D}\). Finally, at fixed \(x=x_c\),
\[
\partial_\alpha B_\alpha(x_c)\big|_{\alpha=\alpha_c}
=\frac{1+x_c^q}{p x_c y_c^{p-1}}=\frac{q y_c}{p x_c}.
\]
Integrating the local derivative from \(x_c\) to each endpoint, together with this first-order change in \(B_\alpha(x_c)\), yields the two individual expansions with their opposite \(\varepsilon^{3/2}\) coefficients. The integration errors are \(O(\varepsilon^2)\), proving the displayed remainders.

## Verification

A standalone Python 3 standard-library checker, `verify.py`, tests the determinant-versus-fold derivative identity exactly in rational arithmetic at 36 positive equilibrium configurations. It tests the critical formulas and fold tangencies for ten integer and fractional exponent pairs, verifies small-\(\varepsilon\) width ratios and the analytic curvature coefficient, and checks the exact \(p=q=2\) benchmark. It reports `VERIFY_OK 337 exact/rational-and-numerical-assertions` on execution. These finite computational tests are sanity checks; the proof above establishes the all-parameter theorem.

## Relationship to prior work

Gardner, Cantor and Collins (2000), Box 1 and Figure 2, introduced the same mutually repressive dimensionless equations, depicted the bistable synthesis-rate region, and described the qualitative balance/cooperativity requirements. Li and Zhang (online 2019) established exact equilibrium classifications and a codimension-two cusp for a three-parameter restriction with one Hill exponent equal to one. Guilberteau, Pouchol and Pouradier Duteil (2021) provided broader monostability/bistability criteria for biological two-species switches including Hill responses. The known **existence of the cusp, bistability and generic cusp exponent** are not claimed as new.

The narrowly assessed contribution is the explicit model-specific sharp coefficient \(C_{p,q}\) for the \(\beta\)-window at fixed \(\alpha\), together with its first-order balance-line slope, **simultaneously for arbitrary unequal positive Hill exponents**. This gives the leading quantitative rate tolerance in the original synthesis-rate coordinates and is not an immediate conclusion of the cited equilibrium-number statements alone. The accessible primary texts inspected did not state the coefficient. This is a best-knowledge literature comparison, not a claim of exhaustive historical priority.

## Limitations

The model assumes deterministic, well-mixed, dimensionless two-gene repression with identical normalized degradation rates and no basal expression, noise, resource competition, delays, unequal degradation scaling, or induction. Parameter perturbations vary the synthesis rates while keeping \(p,q\) fixed. The result does not imply that experimental cellular expression tolerances follow this coefficient. There remains a priority risk from other full-length bifurcation analyses or unpublished calculations; in particular the 2021 general two-species-switch article was accessible through its abstract and appendix material, but its complete main body was not accessible for review. The result has not been independently audited.

## References

1. T. S. Gardner, C. R. Cantor and J. J. Collins, “Construction of a genetic toggle switch in Escherichia coli,” *Nature* **403**, 339–342 (20 January 2000), DOI: https://doi.org/10.1038/35002131. Original Box 1 equations and Figure 2; author's public full-text copy inspected.
2. J. Li and W. Zhang, “Transition between monostability and bistability of a genetic toggle switch in Escherichia coli,” *Discrete and Continuous Dynamical Systems B* **25**, 1871–1894 (online 4 December 2019), DOI: https://doi.org/10.3934/dcdsb.2020007. Open author-uploaded text inspected, including Theorems 3.1 and 4.1.
3. J. Guilberteau, C. Pouchol and N. Pouradier Duteil, “Monostability and bistability of biological switches,” *Journal of Mathematical Biology* **83**, article 65 (2021), DOI: https://doi.org/10.1007/s00285-021-01687-y. Abstract and publisher-accessible appendix inspected; full main body inaccessible.
4. S. B. Cahn and S. G. J. Mochrie, “Biologic: Gene circuits and feedback in an introductory physics sequence for biology and premedical students” (11 July 2013), https://arxiv.org/abs/1307.3126. Abstract inspected, not the full document.
