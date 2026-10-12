# Exact EBV invasion boundary and the absence of a dysplasia-free state in a nasopharyngeal carcinoma model

## Finding
For the six-compartment ODE system published by Mutijah and Sugiyanto in 2026, the unique nonnegative equilibrium with no invasive carcinoma contains a strictly positive dysplastic population whenever the spontaneous conversion rate \(\alpha\) and normal-cell influx \(a_1\) are positive. A second purported carcinoma-free equilibrium at which dysplasia vanishes is not stationary.

Furthermore, the true local stability condition at the viable carcinoma-free equilibrium includes an independent Epstein–Barr virus (EBV) amplification factor. When its reproduction ratio exceeds one, that equilibrium is linearly unstable even if every cell apoptosis rate exceeds its corresponding proliferation rate. This corrects the article's stated sufficiency of apoptosis dominance for stability.

Precisely, with the definitions below, the exact boundary is
\[
\mathcal R_{\mathrm{EBV}}=\frac{\beta ea_3\alpha a_1}{(d_1+\alpha)(d_2-a_2)(d_3+\gamma-a_3)d_6}=1.
\]
At the boundary linearization is inconclusive about nonlinear asymptotic stability.

## Assumptions and scope
All rate parameters \(a_1,\ldots,a_5,d_1,\ldots,d_6,\alpha,\beta,\gamma,\mu,e\) are positive real numbers, and all six initial compartment values are nonnegative. The published model, in the order \((N,D,I,H,C,V)\), is
\[
\begin{aligned}
\dot N&=a_1-(d_1+\alpha)N,\\
\dot D&=(a_2-d_2)D+\alpha N-\beta DV,\\
\dot I&=(a_3-d_3-\gamma)I+\beta DV,\\
\dot H&=(a_4-d_4-\mu)H+\gamma I,\\
\dot C&=(a_5-d_5)C+\mu H,\\
\dot V&=ea_3I-d_6V.
\end{aligned}
\]
Here \(H\) is the source's high-grade dysplasia variable, also denoted \(D_H\) there. The terms \(a_i\) are proliferation rates except for the normal-cell supply \(a_1\); the \(d_i\) are removal rates.

For the stability classification assume
\[
q=d_2-a_2>0,\qquad k=d_3+\gamma-a_3>0,\qquad
h=d_4+\mu-a_4>0,\qquad c=d_5-a_5>0.
\]
These inequalities follow from the stronger source hypothesis \(d_i>a_i\) for all cellular compartments. They are sufficient to make the healthy-side, nonviral rates negative, but do not control the infection-feedback loop.

A **carcinoma-free equilibrium** here is a nonnegative equilibrium with \(C=0\). A **dysplasia-free equilibrium** is one with \(D=0\). Local asymptotic stability refers to the full continuous-time ODE, not merely the infected block.

## Proof
### 1. Unique carcinoma-free equilibrium
At any nonnegative equilibrium with \(C=0\), the \(C\)-equation \(\dot C=\mu H\), with \(\mu>0\), gives \(H=0\). Then the \(H\)-equation gives \(\gamma I=0\), hence \(I=0\). The viral equation yields \(V=0\) since \(d_6>0\).

The normal-cell equation yields the unique value
\[
N_0=\frac{a_1}{d_1+\alpha}>0.
\]
With \(I=V=0\), the dysplasia equation yields
\[
-qD+\alpha N_0=0,\qquad D_0=\frac{\alpha a_1}{(d_1+\alpha)q}>0.
\]
Thus exactly one nonnegative carcinoma-free equilibrium exists under \(q>0\):
\[
E_0=(N_0,D_0,0,0,0,0).
\]
The source additionally lists
\[
E_{02}=(a_1/d_1,0,0,0,0,0)
\]
as a second carcinoma-free state. Substituting into the published vector field gives
\[
\dot N=-\frac{\alpha a_1}{d_1}\ne0,\qquad
\dot D=\frac{\alpha a_1}{d_1}>0,
\]
so this purported equilibrium is not stationary. More generally, at any nonnegative equilibrium with \(D=0\) the dysplasia equation would force \(\alpha N=0\), and hence \(N=0\); the normal-cell equation would then give \(\dot N=a_1>0\), a contradiction. No dysplasia-free equilibrium exists for \(a_1,\alpha>0\), even without assuming \(q>0\).

### 2. Exact viral-invasion threshold
The Jacobian at \(E_0\) can be reordered into four scalar stable directions and the \((I,V)\) coupling. The four scalar eigenvalues are
\[
-(d_1+\alpha),\quad-q,\quad-h,\quad-c.
\]
The remaining infected-cell/virus block is
\[
B=\begin{pmatrix}
-k&\beta D_0\\ea_3&-d_6
\end{pmatrix}.
\]
The full Jacobian includes feed-forward couplings from \(N\) into \(D\), from \(I\) into \(H\), from \(H\) into \(C\), and from \(V\) into \(D\); these do not alter the characteristic factorization. Direct expansion gives
\[
\det(\lambda I-J)=
(\lambda+d_1+\alpha)(\lambda+q)(\lambda+h)(\lambda+c)
\left[(\lambda+k)(\lambda+d_6)-\beta D_0ea_3\right].
\]
Define the dimensionless viral invasion ratio
\[
\mathcal R_{\mathrm{EBV}}:=\frac{\beta ea_3D_0}{kd_6}
=\frac{\beta ea_3\alpha a_1}{(d_1+\alpha)qkd_6}.
\]
The final quadratic is then
\[
\lambda^2+(k+d_6)\lambda+kd_6(1-\mathcal R_{\mathrm{EBV}}).
\]
For \(\mathcal R_{\mathrm{EBV}}<1\) its coefficients are strictly positive and its two roots have negative real parts. For \(\mathcal R_{\mathrm{EBV}}>1\) its constant term is negative, so it has a positive real root. At equality there is a zero root; no nonlinear conclusion is claimed there.

### 3. Exact contradiction to apoptosis-only stability
Choose the following positive parameters:
\[
a_1=a_2=a_3=a_4=a_5=1,\quad
d_1=d_2=d_3=d_4=d_5=d_6=2,\quad
\alpha=\gamma=\mu=e=1,\quad \beta=20.
\]
Every cellular apoptosis rate exceeds the corresponding proliferation rate. Nevertheless
\[
N_0=D_0=\frac13,\quad k=d_6=2,\quad
\mathcal R_{\mathrm{EBV}}=\frac53>1.
\]
The infected block has the exact eigenvalues
\[
\lambda_{\pm}=-2\pm\sqrt{20/3},
\]
one of which is strictly positive. In particular the larger is \(-2+\sqrt{20/3}>0\), while the other four eigenvalues are \(-3,-1,-2,-1\). The carcinoma-free equilibrium is therefore linearly unstable despite apoptosis dominance.

### 4. Persistent dysplastic background after virus clearance
Assume \(q>0\) and a global nonnegative solution with \(V(t)\to0\). The normal equation has exact solution
\[
N(t)=N_0+(N(0)-N_0)e^{-(d_1+\alpha)t}\longrightarrow N_0.
\]
Since \(V,D\ge0\),
\[
\dot D\le-qD+\alpha N.
\]
As \(N\) is bounded and \(q>0\), the scalar comparison formula bounds \(D\) uniformly. Thus \(\beta D(t)V(t)\to0\). The exact inhomogeneous equation
\[
\dot D+qD=\alpha N-\beta DV
\]
has forcing converging to \(\alpha N_0\). Variation of constants therefore yields
\[
\lim_{t\to\infty}D(t)=\frac{\alpha N_0}{q}=D_0>0.
\]
This is conditional on virus clearance; it does not prove that clearance occurs for all initial data.

## Verification
Run `python verification/verify.py` with SymPy. The script constructs the six published right-hand sides and Jacobian, verifies both the unique carcinoma-free equilibrium and the source's nonstationary candidate by exact substitution, and checks the complete six-degree characteristic polynomial against the factorized formula. It checks the exact positive-eigenvalue witness, together with a stable, below-threshold comparison obtained by setting \(\beta=5\) and leaving all other parameters fixed. Expected output: `VERIFY_OK`.

The stability conclusions rely on exact algebra and elementary quadratic root criteria, not finite numerical experiments. The virus-clearance conditional limit is proved analytically by boundedness and variation of constants.

## Relationship to prior work
The motivating paper's Equations (1a)–(1f) and Theorem 1 give the first carcinoma-free state correctly but also introduce the nonstationary second state in the discussion after Theorem 1 and label it stable in Section 5. Its local stability proof further asserts that apoptosis dominance alone makes the first carcinoma-free state stable; the infected/virus feedback determinant shows an additional necessary condition. This finding is therefore a source-specific correction, not a claim to have invented within-host reproduction thresholds.

Smith and De Leenheer (2003) and the established target-cell virus-dynamics literature already describe reproduction-number thresholds for within-host infection. That general principle is fully acknowledged here; it does not itself report this six-compartment NPC paper's nonexistent equilibrium, its precise six-dimensional factorization, or the exact apoptosis-dominance counterexample.

## Limitations
No inference is made about real cancer patients or clinical risk from these parameters. No global disease-eradication or global stability theorem is asserted. The threshold case \(\mathcal R_{\mathrm{EBV}}=1\) is not classified beyond nonhyperbolicity. The definition of carcinoma-free follows the paper's mathematical convention \(C=0\); it is not an assertion of the absence of premalignant dysplastic cells. The paper's figure-generation implementation was not inspected; conclusions concern the published differential equations only.

The original article's publisher-layout full text was accessed as an open-licensed author-uploaded text transcription, with the relevant model, equilibrium, and stability sections examined. Formula glyph extraction is imperfect; equations were checked against repeated appearances in those sections and against the specified variables. A separate full-page rendered PDF could eliminate any remaining transcription risk.

## References
1. Mutijah and Sugiyanto, “Mathematical modeling of nasopharyngeal carcinoma,” *Far East Journal of Mathematical Sciences* 143(9) (2026), 2935–2964, DOI: 10.17654/0972087126163. Published online July 16, 2026. Open-licensed source: https://www.researchgate.net/publication/410114499_MATHEMATICAL_MODELING_OF_NASOPHARYNGEAL_CARCINOMA.
2. H. L. Smith and P. De Leenheer, “Virus Dynamics: A Global Analysis,” *SIAM Journal on Applied Mathematics* 63(4) (2003), 1313–1327, DOI: 10.1137/S0036139902406905.
3. D. Wodarz and M. A. Nowak, “Mathematical models of HIV pathogenesis and treatment,” *BioEssays* 24 (2002), 1178–1187, DOI: 10.1002/bies.10196.
