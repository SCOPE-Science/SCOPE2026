# A sharp adoption fold and robust bistability in the homogeneous adoption–opinion model

## Finding
Consider a homogeneous instance of a coupled susceptible–adopter–dissatisfied (SAD) population model with Friedkin–Johnsen opinions. Every full-system equilibrium is spatially uniform. At zero predisposition, the exact positive-adoption threshold is
\[
\beta_c=\frac{27\delta}{4q^2H^3},\qquad q=\frac{\xi}{1-\lambda},\qquad H=1-\frac{\delta}{gq},
\]
provided \(H>0\). For \(\beta<\beta_c\) there is no positive-adoption equilibrium; for equality there is one folded equilibrium; above the threshold there are two distinct positive-adoption equilibria. If \(H\le0\), none exists.

In particular, for any integer \(n\ge2\), the admissible rational parameter tuple
\[
(\beta,\delta,g,\alpha,\lambda,\xi)=\left(\frac49,\frac1{128},\frac18,\frac38,\frac14,\frac38\right)
\]
exhibits three equilibria, each repeated uniformly across individuals:
\[
E_0=(u,v,y)=(0,1,0),\quad
E_-=(3/8,17/32,3/16),\quad
E_+=(3/4,13/64,3/8).
\]
The first and third are hyperbolic sinks of the entire \(3n\)-dimensional map, and the middle one is a hyperbolic saddle with exactly one expanding eigenvalue. The same three-equilibrium stability pattern persists when a sufficiently small strictly positive homogeneous predisposition is introduced.

## Assumptions and scope
Let \(u_i\) and \(v_i\) be adopter and dissatisfied fractions at node \(i\), \(s_i=1-u_i-v_i\) its susceptible fraction, and \(y_i\in[0,1]\) its opinion. For \(i=1,\ldots,n\), take both row-stochastic mixing matrices to be \(J_n/n\), including self-contact, and set
\[
\begin{aligned}
u_i'&=(1-\delta)u_i+\beta y_i s_i\bar u,\\
v_i'&=v_i+\delta u_i-g y_i v_i+g(1-y_i)s_i,\\
y_i'&=\alpha r+\lambda\bar y+\xi\bar u,
\end{aligned}
\]
where \(\bar u=n^{-1}\sum_i u_i\) and \(\bar y=n^{-1}\sum_i y_i\). Parameters satisfy \(\beta,\delta,g>0\), \(0<\lambda<1\), \(\xi,\alpha>0\), \(\alpha+\lambda+\xi=1\), \(\beta+g\le1\), and \(2g\le1\). The common baseline opinion is \(r\in[0,1]\). The physical domain has \(u_i,v_i,s_i\ge0\), \(u_i+v_i+s_i=1\), and \(0\le y_i\le1\). The explicit choice above obeys these restrictions strictly where appropriate.

Here a 'positive-adoption equilibrium' means every agent has a strictly positive adopter fraction. Local stability refers to all \(3n\) state directions; no global basin shape is asserted.

## Proof
**1. Homogeneity of every equilibrium.** At any equilibrium, the opinion equation gives one common value \(y_i=y=\alpha r+\lambda\bar y+\xi\bar u\), so \(y=p+q\bar u\), where \(p=\alpha r/(1-\lambda)\) and \(q=\xi/(1-\lambda)\). The dissatisfied equation is equivalent to
\[
s_i=y-(y+\delta/g)u_i.
\]
If \(\bar u=0\), nonnegativity gives \(u_i=0\) for all \(i\), hence also common \(s_i,v_i\). Otherwise the adopter fixed-point equation becomes
\[
[\delta+\beta y\bar u(y+\delta/g)]u_i=\beta y^2\bar u,
\]
whose coefficient is independent of \(i\) and strictly positive. Hence the \(u_i\), and therefore \(s_i,v_i\), are all equal. This proves that no heterogeneous equilibrium was omitted.

**2. Complete algebraic equilibrium count.** Write the common adopter fraction as \(a>0\). The adopter equation yields \(\delta=\beta y s\). For the zero baseline \(r=0\), \(y=qa\) and
\[
s=y(1-a)-(\delta/g)a=qa(H-a),\qquad H=1-\delta/(gq).
\]
A physical positive solution must have \(0<a<H\), and consequently \(H>0\). Conversely every root \(a\in(0,H)\) of
\[
\beta q^2 a^2(H-a)=\delta
\]
gives \(y=qa\), \(s=qa(H-a)>0\), and \(v=1-a-s=(\delta/g)a+(1-qa)(1-a)>0\). Because \(q<1\) and \(H<1\), all physical bounds hold. The function \(a^2(H-a)\) increases strictly until \(a=2H/3\), decreases strictly afterward, and has maximum \(4H^3/27\). This proves the exact zero/one/two count and the threshold formula. The adoption-free equilibrium is uniquely \((a,v,y)=(0,1,0)\).

For a positive common baseline \(r\), eliminating \(y=p+qa\) gives the exact equilibrium polynomial
\[
\beta(p+qa)[(p+qa)(1-a)-(\delta/g)a]=\delta.
\]
The adoption-free equilibrium is \((u,v,y)=(0,1-p,p)\). The distinct positive roots in the explicit example continue by the implicit-function theorem for small positive \(p\), staying physical.

**3. Exact rational example.** For the stated parameters \(q=1/2\), \(H=7/8\), and \(\beta_c=108/343<4/9\). The positive-root equation is equivalent to
\[
128a^3-112a^2+9=(4a-3)(4a+1)(8a-3)=0.
\]
Its only positive roots are \(a=3/8\) and \(a=3/4\). Their state triples are those given in Finding; all physical coordinates are positive.

**4. Stability in all dimensions.** Complete mixing splits the derivative into a homogeneous \(3\times3\) Jacobian and \(n-1\) identical transverse blocks. In coordinate order \((u,v,y)\), the homogeneous block at adoption fraction \(a\), susceptibility \(s\), and opinion \(y\) is
\[
J_h=\begin{pmatrix}
1-\delta+\beta y(s-a)&-\beta ya&\beta as\\
\delta-g(1-y)&1-g&-g(1-a)\\
\xi&0&\lambda
\end{pmatrix}.
\]
Each transverse block has eigenvalue zero and the remaining eigenvalues of
\[
J_t=\begin{pmatrix}1-\delta-\beta ya&-\beta ya\\ \delta-g(1-y)&1-g\end{pmatrix}.
\]
At \(E_-\), their characteristic polynomials are
\[
\det(zI-J_h)=\frac{16384z^3-34304z^2+21296z-3391}{16384},\quad
\det(zI-J_t)=z^2-\frac{235}{128}z+\frac{429}{512}.
\]
For the cubic, exact endpoint sign changes isolate its three real roots in \((0,1/4)\), \((4/5,9/10)\), and \((1,21/20)\). The quadratic has roots in \((4/5,9/10)\) and \((19/20,1)\). Thus exactly one eigenvalue of the full map lies outside the unit disk at \(E_-\).

At \(E_+\), the characteristic polynomials are
\[
\det(zI-J_h)=\frac{1024z^3-2048z^2+1217z-190}{1024},\quad
\det(zI-J_t)=z^2-\frac{223}{128}z+\frac34.
\]
The three cubic roots lie respectively in \((0,1/4)\), \((3/4,4/5)\), and \((19/20,1)\); the two quadratic roots lie in \((3/4,4/5)\) and \((19/20,1)\). Every eigenvalue is therefore inside the unit disk. At \(E_0\), the homogeneous eigenvalues are \(1-\delta=127/128\), \(1-g=7/8\), and \(\lambda=1/4\); transverse eigenvalues are \(127/128,7/8,0\). Hence \(E_0\) is also a hyperbolic sink. The interval calculations and Jacobian identities are reproducible in `verify.py` with exact rational arithmetic. Because all three fixed points are hyperbolic and the positive equilibria solve a polynomial with simple roots, their stability types and positivity persist for every sufficiently small \(r>0\). At the adoption-free continuation, the adopter eigenvalue \(1-\delta+\beta p^2\) remains below one for sufficiently small \(p\).

## Verification
Run `python verify.py` with Python 3 and no external packages. The program independently evaluates the admissibility inequalities, cubic threshold and factor identities, each equilibrium's fixed-point equations and physical simplex constraints, both characteristic polynomials, and rational root-sign brackets for the homogeneous and transverse matrices. Signs at disjoint intervals establish an exhaustive real-root count because the relevant polynomial degrees are three and two. Exact finite arithmetic checks here support, rather than replace, the symbolic arguments about all \(n\ge2\) and persistence for sufficiently small positive predispositions.

## Relationship to prior work
Alutto–Xu–Dabbene–Ishii–Ravazzi (2025), arXiv:2509.01457, introduced and analyzed the coupled SAD/Friedkin–Johnsen system, proved existence under conditions and supplied sufficient uniqueness and stability conditions (particularly their Theorem 3.14 and associated equilibrium equations). Alutto et al. (2026), arXiv:2601.16722, studied its feedback-control version. The present statement is the zero-baseline complete-mixing all-equilibrium cubic classification together with an explicit full-dimensional two-sink coexistence example that persists under strictly positive baseline opinions. The 2024 Xu–Ishii model, arXiv:2401.04556, has a different polar-opinion rule and does not state this complete-mixing criterion. Saddle-node phenomena and bistability are well established in broader population dynamics; no novelty is claimed for those concepts in isolation.

## Limitations
The threshold classification requires equal dissatisfied-transition rates \(\gamma=\theta\) and uniform all-to-all mixing with self-contact. It is not a global convergence theorem and does not determine basin volumes or separatrices, nor does it extend automatically to arbitrary graphs, heterogeneous parameters, interventions, or persistent stochastic fluctuations. The no-baseline saddle-node classification has \(r=0\), which falls outside the motivating paper's assumption of some positive baseline predisposition; the separate explicit hyperbolic coexistence example persists for \(r>0\) small and thus covers that admissibility requirement. General mathematical bifurcation results may imply parts of the statement; independent historical-priority confirmation is outstanding.

## References
1. M. Alutto, Q. Xu, F. Dabbene, H. Ishii, and C. Ravazzi, *Predictive Control Strategies for Sustaining Innovation Adoption on Multilayer Social Networks*, arXiv:2509.01457v1 (first public September 1, 2025), https://arxiv.org/abs/2509.01457 .
2. M. Alutto and collaborators, *Model Predictive Control for Coupled Adoption-Opinion Dynamics*, arXiv:2601.16722v1 (January 23, 2026), https://arxiv.org/abs/2601.16722 .
3. Q. Xu and H. Ishii, *On a Discrete-Time Networked SIV Epidemic Model with Polar Opinion Dynamics*, arXiv:2401.04556 (January 2024), https://arxiv.org/abs/2401.04556 .
