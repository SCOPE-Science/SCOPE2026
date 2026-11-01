# All heterogeneous equilibria are hyperbolically attracting in a two-patch chemotaxis system

## Finding
For the positive-parameter two-patch logistic Keller–Segel metapopulation model specified below, **every strictly positive spatially heterogeneous equilibrium is exponentially asymptotically stable in the full four-dimensional dynamics**. This holds for every positive growth, migration, chemoattractant production, removal, and diffusion rate and every chemotactic sensitivity for which such an equilibrium exists. Thus an asymmetric equilibrium cannot subsequently lose local stability through a Hopf bifurcation, a zero-eigenvalue crossing, or another eigenvalue crossing as chemotactic sensitivity increases. The theorem concerns local stability, not global attractivity.

More precisely, write \(\eta=\eta_n\), \(\delta=\beta+\eta_c/2\), and \(\kappa=2r/\eta\). The asymmetric equilibria exist exactly when
\[
\chi>\chi_c:=\frac{\delta(1+\kappa)}{\alpha K}.
\]
At each of the two symmetry-related equilibria all four eigenvalues have strictly negative real parts. The new assertion here is the **uniform-in-parameters stability classification along the entire heterogeneous branch**; the equilibrium enumeration and the threshold themselves are known antecedents and are not claimed as new.

## Assumptions and scope
Let \(r,\eta_n,\eta_c,\alpha,\beta,K>0\) and \(\chi\ge0\). For \(\{i,j\}=\{1,2\}\), let
\[
\begin{aligned}
\dot n_i&=\frac{\eta_n}{2}\frac{e^{\chi c_i}n_j-e^{\chi c_j}n_i}{e^{\chi c_i}+e^{\chi c_j}}+r n_i(1-n_i/K),\\
\dot c_i&=\frac{\eta_c}{4}(c_j-c_i)+\alpha n_i-\beta c_i.
\end{aligned}
\]
This is the two-vertex, unit-edge-weight, logistic-reaction specialization of the graph metapopulation model of Kim, Zhang, Zhao, and Cooney. A *positive heterogeneous equilibrium* has both populations strictly positive and unequal; all four state variables are dynamic and no quasi-steady chemical approximation is made. The two patch labels can be exchanged, so take \(n_1>n_2\) without loss of generality.

Set \(M=(n_1+n_2)/2\), \(z=(n_1-n_2)/2\), \(C=(c_1+c_2)/2\), and \(w=(c_1-c_2)/2\). The transformed equations are
\[
\begin{aligned}
\dot M&=r[M-(M^2+z^2)/K],\\
\dot z&=\frac\eta2[M\tanh(\chi w)-z]+rz(1-2M/K),\\
\dot C&=\alpha M-\beta C,\\
\dot w&=\alpha z-\delta w.
\end{aligned}
\]

## Proof
**1. Positive-equilibrium parameter.** At an asymmetric equilibrium put \(t=z/M\), so \(0<t<1\). The equilibrium equations imply
\[
M=\frac{K}{1+t^2},\quad z=\frac{Kt}{1+t^2},\quad
w=\frac{\alpha z}{\delta},\quad C=\frac{\alpha M}{\beta}.
\]
The remaining scalar equation is
\[
\tanh\!\left(\frac{\chi\alpha Kt}{\delta(1+t^2)}\right)=h(t),\qquad
h(t):=t\left(1+\kappa\frac{1-t^2}{1+t^2}\right).
\]
The admissible interval is \(0<t<t_{\max}\), where \(t_{\max}=1\) if \(\kappa\le1\), and, if \(\kappa>1\), \(t_{\max}\) is the unique root in \((0,1)\) of \((\kappa-1)t^2+\kappa t=1\). On this interval \(0<h(t)<1\). Consequently
\[
\chi=\frac\delta{\alpha K}X(t),\qquad
X(t):=\frac{1+t^2}{t}\operatorname{artanh}h(t).
\]
The identity
\[
h(t)=\frac{t+v(t)}{1+tv(t)},\qquad
v(t)=\frac{\kappa t}{1+(1-\kappa)t^2}
\]
shows that \(0<v(t)<1\) and \(v'(t)>0\) on the admissible interval. The addition law for \(\operatorname{artanh}\) gives
\[
X(t)=(1+t^2)\frac{\operatorname{artanh}t}{t}
+\kappa\frac{1+t^2}{1+(1-\kappa)t^2}
\frac{\operatorname{artanh}v(t)}{v(t)}.
\]
Every factor in each summand is positive and increasing, and the prefactors are strictly increasing: for the second rational factor its derivative is \(2\kappa t/[1+(1-\kappa)t^2]^2>0\). The function \(\operatorname{artanh}s/s\) is increasing on \((0,1)\). Hence \(X'(t)>0\), and \(X(0+)=1+\kappa\). This establishes the monotone branch and its threshold; these are needed here to certify the sign of the Jacobian determinant, not claimed as the main new result.

**2. Four-dimensional linearization.** Because \(\dot C=\alpha M-\beta C\) and no other equation depends on \(C\), the eigenvalues are \(-\beta\) and those of the \((M,z,w)\) block. At an asymmetric equilibrium introduce
\[
\begin{gathered}
a=\frac{r(1-t^2)}{1+t^2}>0,\quad e=a+\frac\eta2>0,\quad
b=\frac{\eta\kappa t}{1+t^2}>0,\quad d=\frac{\eta t(1-\kappa)}2,\\
F=\frac\eta2 M\chi[1-h(t)^2]>0,\qquad
q=\frac{\alpha F}{\delta}.
\end{gathered}
\]
The block is exactly
\[
J=\begin{pmatrix}-a&-b&0\\ d&-e&F\\0&\alpha&-\delta\end{pmatrix}.
\]
The equilibrium identity \(e=\eta h(t)/(2t)\) gives
\[
q=e\frac{1-h(t)^2}{h(t)}\operatorname{artanh}h(t).
\]
For \(0<h<1\),
\[
(1-h^2)\operatorname{artanh}h<h,
\]
because \(\operatorname{artanh}h=\int_0^h(1-s^2)^{-1}\,ds<h/(1-h^2)\). Therefore \(0<q<e\).

**3. The decisive determinant identity.** Define
\[
G(t,\chi)=\tanh\!\left(\frac{\chi\alpha Kt}{\delta(1+t^2)}\right)-h(t).
\]
On the equilibrium branch \(G(t,\chi(t))=0\) and \(G_\chi>0\). Since \(\chi'(t)>0\), implicit differentiation yields \(G_t=-G_\chi\chi'(t)<0\). Direct substitution of the definitions above gives the exact identity
\[
D:=ae+bd-aq=-\frac{r\eta}{2}G_t>0,
\]
with \(G_t\) taken at fixed \(\chi\). This identity is algebraically checked in the accompanying reproducibility script; the displayed formulas also permit direct differentiation and cancellation by hand.

**4. Strict Routh–Hurwitz inequalities.** The characteristic polynomial of \(J\) is
\[
\begin{aligned}
p(\lambda)&=(\lambda+\delta)[(\lambda+a)(\lambda+e)+bd]-\delta q(\lambda+a)\\
&=\lambda^3+A\lambda^2+B\lambda+C_0,
\end{aligned}
\]
where, setting \(T=ae+bd=D+aq>0\),
\[
A=a+e+\delta>0,\quad B=T+\delta(a+e-q)>0,\quad C_0=\delta D>0.
\]
Moreover
\[
AB-C_0=(a+e)T+\delta(a+e+\delta)(a+e-q)+\delta aq>0,
\]
since \(a>0\) and \(0<q<e\). The strict cubic Routh–Hurwitz conditions hold, so all roots of \(p\) have negative real part. The remaining eigenvalue is \(-\beta<0\). Thus the two heterogeneous equilibria are hyperbolic sinks for every admissible positive parameter set. Hyperbolicity and the standard linearization theorem give local exponential asymptotic stability. Since no eigenvalue can meet the imaginary axis at a finite point on either branch, no secondary local stability loss occurs there. \(\square\)

## Verification
The accompanying standalone `verify.py` uses SymPy to check the exact common-branch, Jacobian-characteristic-polynomial, and determinant identities. It also tests 164 independently recovered heterogeneous equilibria across positive rates and coupling strengths by computing their full three-dimensional reduced Jacobian eigenvalues. Run using `python verify.py` in an environment with Python, SymPy, NumPy, and SciPy. Numerical experiments are consistency checks only; the infinite-parameter assertion follows from the strict inequalities in the proof, not from sampling.

## Relationship to prior work
Kim, Zhang, Zhao, and Cooney (2026) formulate this biased-random-walk metapopulation model and examine loss of the spatially uniform equilibrium and related pattern-formation phenomena. An earlier complete two-patch equilibrium census establishes the two symmetry-broken branches, their threshold, monotonicity, and strong-bias population limits. **That census does not assert or imply the full four-dimensional local stability theorem proved here:** counting roots and excluding folds do not exclude complex-eigenvalue crossings. The additional ingredient is the strict Routh–Hurwitz certificate using \(0<q<e\) and the branch-derivative identity for \(D\). Prior logistic Keller–Segel studies on *metric graphs* involve PDE transport on edges rather than this finite-vertex exponential-comparison ODE, so their bifurcation theorems do not give the claimed all-parameter conclusion.

## Limitations
The statement is local to each positive heterogeneous stationary solution; it does not show that all positive trajectories converge to an equilibrium, nor exclude distant periodic or chaotic attractors. It does not address larger graphs, other demographic reactions, zero rates, or non-logistic kernels. At the symmetry-breaking threshold itself, the heterogeneous equilibria coalesce with the uniform state and strict hyperbolicity is not asserted. Historical novelty remains provisional against literature not available in full; no independent validation has been performed.

## References
- D. Kim, Y. Zhang, Y. Zhao, and D. B. Cooney, *The Keller–Segel Model for Chemotaxis on Metapopulation Graphs and Graphons*, arXiv:2610.31049v1 (first posted 2026-10-22), https://arxiv.org/abs/2610.31049.
- H. Shemtaga, W. Shen, and S. Sukhtaiev, *Stability and bifurcation for logistic Keller–Segel models on compact graphs*, arXiv:2310.00756 (first posted 2023-10-01), https://arxiv.org/abs/2310.00756.
