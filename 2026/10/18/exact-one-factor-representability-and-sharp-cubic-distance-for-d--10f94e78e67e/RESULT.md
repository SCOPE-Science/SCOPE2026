# Exact one-factor representability and sharp cubic distance for diagonal Lyapunov Gramians

## Finding
Let \(n\ge3\), \(a_1,\ldots,a_n>0\), and \(u_i\ne0\). For \(0<t\le\infty\), define the (finite-time or stationary) rank-one-forced diagonal Lyapunov Gramian
\[
C_{ij}(t)=u_i u_j k_t(a_i,a_j),\qquad
k_t(x,y)=\int_0^t e^{-(x+y)s}\,ds,
\]
with \(t=\infty\) denoting integration over \([0,\infty)\). Let \(\mathcal F_{n,1}=\{\operatorname{diag}(d)+vv^{\mathsf T}:d_i\ge0,\ v\in\mathbb R^n\}\) be the nonnegative-uniqueness one-factor covariance model.

**Complete exact-representability classification.** The Gramian belongs to \(\mathcal F_{n,1}\) precisely when either (i) all damping rates coincide, or (ii) exactly two distinct damping rates occur and one of them occurs only once. This holds for **every** positive finite time and at stationarity. In every representable case, the residual diagonal of any decomposition has at least one zero entry; thus the strict-positive-uniqueness model never represents this Gramian for \(n\ge3\).

**Quantitative distance.** In every nonrepresentable case, the Frobenius distance \(\delta(t)=\inf_{Y\in\mathcal F_{n,1}}\|C(t)-Y\|_F\) is strictly positive at each \(0<t\le\infty\), and for fixed rates and loadings as \(t\downarrow0\),
\[
\delta(t)=\Theta(t^3).
\]
Both the lower and upper estimates are constructive. For three distinct rates \(a_1<a_2<a_3\), writing \(p_{ij}=|u_i u_j|k_t(a_i,a_j)\),
\[
\Delta=p_{12}p_{23}-p_{13}p_{22}>0,\qquad
S=p_{12}+p_{23}+p_{13}+p_{22},
\]
one explicit bound is
\[
\delta(t)\ge\min\left\{p_{13},\frac{\sqrt{S^2+8\Delta}-S}{4}\right\}>0.
\]
In particular, at stationarity the three-rate unit-loading example \((a_1,a_2,a_3)=(1,2,3)\) has \(\Delta=1/240\) and
\[
\delta(\infty)\ge\frac{\sqrt{991}-31}{120}>0.
\]
The example Gramian is strictly positive definite despite being separated from the entire one-factor model.

## Assumptions and scope
The continuous-time covariance equation is \(\dot C=-AC-CA+uu^{\mathsf T}\), \(C(0)=0\), where \(A=\operatorname{diag}(a_1,\ldots,a_n)\) is real and positive definite. Its exact solution is the specified integral. All \(u_i\) must be nonzero, but their signs are arbitrary. Diagonal uniqueness variances are constrained to be nonnegative, not freely signed. No claim concerns general nondiagonal generators, rank greater than one, or finite-precision matrix calculations. The distance uses the ordinary Frobenius norm of the unnormalized covariance matrix.

## Proof
**1. Kernel identities and strict positivity.** Let \(f_x(s)=e^{-xs}\) in \(L^2([0,t])\), where \(t\) may be infinite. Then \(k_t(x,y)=\langle f_x,f_y\rangle\). Strict Cauchy--Schwarz implies
\[
k_t(a,a)k_t(b,b)-k_t(a,b)^2>0\quad(a\ne b),
\]
since two distinct exponentials are linearly independent on every interval of positive length. In addition, the Laplace Gram kernel is strictly totally positive of order two: for \(x<y\), \(p<q\),
\[
k_t(x,p)k_t(y,q)-k_t(x,q)k_t(y,p)>0.
\]
Indeed the determinant equals half the double integral of
\[
\big(f_x(r)f_y(s)-f_x(s)f_y(r)\big)
\big(f_p(r)f_q(s)-f_p(s)f_q(r)\big).
\]
Both factors have the same strict sign whenever \(r\ne s\), and the integrals are absolutely convergent also for \(t=\infty\).

Conjugation by \(\operatorname{diag}(\operatorname{sgn}u_i)\) preserves membership of \(\mathcal F_{n,1}\) and the Frobenius norm, so throughout the sign arguments we may assume all \(u_i>0\).

**2. Exclusion with three distinct rates.** Choose indices with \(a_1<a_2<a_3\). Strict order-two positivity gives \(p_{12}p_{23}-p_{13}p_{22}>0\). If \(C=D+vv^{\mathsf T}\), the three strictly positive off-diagonal entries imply \(v_1v_3=p_{13}>0\) and
\[
p_{12}p_{23}-p_{13}p_{22}=-v_1v_3 d_2\le0,
\]
a contradiction. Equivalently, off-diagonal matching forces \(v_2^2=p_{12}p_{23}/p_{13}>p_{22}\), hence a negative uniqueness variance.

**3. Exclusion with two repeated rate groups.** If exactly two rates \(a\ne b\) each occur at least twice, choose distinct \(i,j\) at rate \(a\) and \(k,l\) at rate \(b\). Then
\[
p_{ij}p_{kl}-p_{ik}p_{jl}
=|u_i u_j u_k u_l|\big(k_t(a,a)k_t(b,b)-k_t(a,b)^2\big)>0.
\]
For every \(D+vv^{\mathsf T}\), the same off-diagonal tetrad vanishes identically, since each factor product is \(v_iv_jv_kv_l\). Hence no decomposition exists.

**4. The only representing patterns.** With one common rate \(a\), \(C=k_t(a,a)uu^{\mathsf T}\), so \(D=0\) suffices. With \(n-1\) indices at rate \(a\) and one exceptional index \(j\) at rate \(b\), take
\[
v_i=u_i\sqrt{k_t(a,a)}\quad(i\ne j),\qquad
v_j=\frac{u_j k_t(a,b)}{\sqrt{k_t(a,a)}}.
\]
All entries of \(C-vv^{\mathsf T}\) vanish except its \((j,j)\) entry,
\[
d_j=u_j^2\left(k_t(b,b)-\frac{k_t(a,b)^2}{k_t(a,a)}\right)>0,
\]
by strict Cauchy--Schwarz. Conversely, all patterns not covered by these two cases have either three distinct rates or two rate groups of multiplicity at least two, so steps 2--3 exhaust the classification. The off-diagonal products among any three indices in the repeated group, or among two repeated indices and the singleton, also force the repeated-group factor squares to equal \(u_i^2 k_t(a,a)\), so their diagonal uniqueness variances must vanish. For the all-equal case, the same three-index argument forces \(D=0\). No representation has a strictly positive diagonal uniqueness matrix.

**5. Strict and cubic distance.** In the three-rate case, set \(\varepsilon=\max_{i,j}|C_{ij}-Y_{ij}|\) after sign normalization. If \(Y_{13}\le0\), then \(\varepsilon\ge p_{13}\). If \(Y_{13}>0\), for \(Y=D+vv^{\mathsf T}\) one has \(Y_{12}Y_{23}-Y_{13}Y_{22}=-Y_{13}d_2\le0\); perturbing the four entries yields \(\Delta\le S\varepsilon+2\varepsilon^2\), and hence the displayed positive bound on \(\|C-Y\|_F\ge\varepsilon\). For the two-repeated-group case, the positive off-diagonal tetrad equals zero for all candidates. Perturbation of its four factors similarly gives \(\Delta_4\le S_4\varepsilon+2\varepsilon^2\), where \(\Delta_4=p_{ij}p_{kl}-p_{ik}p_{jl}>0\) and \(S_4=p_{ij}+p_{kl}+p_{ik}+p_{jl}\). This proves strictly positive distance without any closedness assumption on the model.

For three ordered rates \(a<b<c\), the kernel expansions give
\[
k_t(a,b)k_t(b,c)-k_t(a,c)k_t(b,b)
=\frac{(b-a)(c-b)}{12}t^4+O(t^5),
\]
while for the two-group tetrad,
\[
k_t(a,a)k_t(b,b)-k_t(a,b)^2
=\frac{(a-b)^2}{12}t^4+O(t^5).
\]
In both cases the sum \(S\) (or \(S_4\)) is of order \(t\), and the positivity-gap root is consequently bounded below by a positive constant times \(t^3\). Conversely set \(v_i(t)=u_i\sqrt t\,e^{-a_i t/2}\). The feasible approximation \(vv^{\mathsf T}\) obeys, entry by entry,
\[
C_{ij}(t)-v_i(t)v_j(t)
=\frac{u_i u_j(a_i+a_j)^2}{24}t^3+O(t^4),
\]
so its Frobenius error is \(O(t^3)\). The upper and lower estimates prove \(\Theta(t^3)\).

**6. Exact stationary witness.** Taking \((a_1,a_2,a_3)=(1,2,3)\), \(u=(1,1,1)\), \(t=\infty\),
\[
C=\begin{pmatrix}1/2&1/3&1/4\\1/3&1/4&1/5\\1/4&1/5&1/6\end{pmatrix}.
\]
The leading principal minors are positive by the independent-exponential Gram argument; direct arithmetic gives \(\Delta=1/240\), \(v_2^2=4/15\), forced \(d_2=-1/60\), and \(S=31/30\). Substituting in the lower bound gives \((\sqrt{991}-31)/120\).

## Verification
The accompanying `verify.py` uses exact rational and symbolic algebra for the stationary witness, forced negative diagonal, two-group tetrad, and cubic short-time minor coefficients. It also performs reproducible seeded floating-point checks for the positive kernel and constructive singleton representation. Replay: `python verify.py`; the verified run returned `PASS 4002 checks`. Numerical sampling does not prove any universal assertion: those assertions follow from steps 1--5. The script requires Python, SymPy and NumPy.

## Relationship to prior work
The low-rank-plus-diagonal covariance approximation class and numerical tangent-projection methods are established in Bonnabel, Lambert and Bach (2024). General nonnegative-diagonal factor-analysis and matrix-decomposition optimization are established in Bertsimas, Copenhaver and Mazumder (2017) and Saunderson et al. (2012). Classical one-factor tetrad identities, Cauchy--Schwarz inequalities, and Laplace-kernel order-two positivity are used as background. The statement assessed here is the exact representability classification **for rank-one-forced diagonal differential Lyapunov Gramians at every finite positive time and at stationarity**, plus the sharp order-three separation from the factor model. No claim of priority is made for the underlying factor-analysis formulation, tetrad identity, kernel positivity, or general approximation algorithms.

## Limitations
The claim assumes one noise input, zero initial covariance, diagonal strictly stable dynamics and nonzero components of the noise direction. The source paper's algorithms address much broader Riccati-like systems; this calculation neither analyzes their convergence nor proves their failure. The distance bound is explicit but not an exact value of the optimal Frobenius distance. The asymptotic exponent applies with fixed positive damping rates and nonzero loadings. Literature not indexed or accessible may contain equivalent specializations; independent publication-priority confirmation is absent.

## References
1. S. Bonnabel, M. Lambert and F. Bach, *Low-Rank Plus Diagonal Approximations for Riccati-Like Matrix Differential Equations*, SIAM Journal on Matrix Analysis and Applications 45(3) (2024), 1669--1688; arXiv:2407.03373, initial public submission 2024-07-01. https://arxiv.org/abs/2407.03373 . Author-accessible full text: https://www.di.ens.fr/~fbach/low-rank-simax.pdf .
2. D. Bertsimas, M. S. Copenhaver and R. Mazumder, *Certifiably Optimal Low Rank Factor Analysis*, Journal of Machine Learning Research 18 (2017), 1--53. https://www.jmlr.org/papers/volume18/15-613/15-613.pdf .
3. J. Saunderson, V. Chandrasekaran, P. A. Parrilo and A. S. Willsky, *Diagonal and Low-Rank Matrix Decompositions, Correlation Matrices, and Ellipsoid Fitting*, arXiv:1204.1220 (2012). https://arxiv.org/abs/1204.1220 .
4. A. Shapiro, *Rank-reducibility of a symmetric matrix and sampling theory of minimum trace factor analysis*, Psychometrika 47 (1982), 187--199. Cited for general factor-analysis background; the complete text was unavailable for this comparison.
