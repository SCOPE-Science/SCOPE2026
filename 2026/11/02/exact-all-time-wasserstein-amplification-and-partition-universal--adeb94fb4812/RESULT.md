# Exact all-time Wasserstein amplification and partition universality for multipartite graph heat flow

## Finding
For every complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) with \(r\ge3\) and positive part sizes, write \(N=\sum_i n_i\) and \(m=\max_i n_i\). The exact norm of the continuous-time combinatorial heat semigroup on the real Lipschitz seminorm, equivalently its induced Wasserstein-one contraction/amplification coefficient on probability measures, is
\[
C_G(t)=\frac{2(m-1)}m e^{-(N-m)t}-\frac{m-2}m e^{-Nt},\qquad t\ge0.
\]
In particular, the entire time profile depends only on \(N\) and the largest part \(m\), not the number or sizes of the remaining parts. It is at most one for every \(t\ge0\) exactly when \(2m\le N+2\). Otherwise it has a unique interior maximum strictly above one at
\[
t_*=\frac1m\log\frac{N(m-2)}{2(m-1)(N-m)},
\qquad
C_G(t_*)=\frac{2(m-1)}N\left(\frac{2(m-1)(N-m)}{N(m-2)}\right)^{(N-m)/m}.
\]
The initial infinitesimal coarse-Wasserstein curvature is \(N+2-2m\). This includes an explicit sharp boundary between all-time nonexpansivity and transient amplification. As a concrete case, \(K_{5,1,1}\) has
\[
C_G(t)=\frac85e^{-2t}-\frac35e^{-7t},\qquad
t_*=\frac15\log\frac{21}{16},\qquad C_G(t_*)>1.
\]

## Assumptions and scope
The vertex set is a disjoint union of \(r\ge3\) nonempty independent sets \(V_i\) with \(|V_i|=n_i\). Vertices in distinct parts are adjacent with graph distance one, and distinct vertices in a common part have graph distance two. Each edge carries jump rate one in both directions. The generator acting on functions is \(-L\), where \((Lf)(x)=\sum_{y\sim x}(f(x)-f(y))\); no degree normalization is used. The time parameter satisfies \(t\ge0\). For probability measures \(\mu,\nu\), the distance \(W_1\) is the optimal transportation cost for this graph distance. At \(t=0\), \(C_G(0)=1\).

## Proof
**1. Exact heat-kernel decomposition.** Let \(u_i\) denote the uniform probability row vector on \(V_i\), let \(\Pi_i\) be the projection onto functions supported in \(V_i\) with zero sum there, let \(\Pi_{\mathrm{cl}}\) project onto functions constant on each part, and let \(\Pi_0\) project onto global constants. The Laplacian has eigenvalue zero on constants, eigenvalue \(N\) on \(\operatorname{ran}(\Pi_{\mathrm{cl}}-\Pi_0)\), and eigenvalue \(N-n_i\) on \(\operatorname{ran}\Pi_i\). Hence, with \(c=e^{-Nt}\) and \(a_i=e^{-(N-n_i)t}\),
\[
P_t=\Pi_0+c(\Pi_{\mathrm{cl}}-\Pi_0)+\sum_i a_i\Pi_i.
\]
For vertices \(x\in V_i\) and \(y\in V_j\) from distinct parts,
\[
(\delta_x-\delta_y)P_t=c(u_i-u_j)+a_i(\delta_x-u_i)-a_j(\delta_y-u_j).
\]
All four coefficient types have fixed signs because \(a_i,a_j\ge c\): positive mass \(A_i=(1-1/n_i)a_i+c/n_i\) at \(x\); negative mass \(C_i=(1-1/n_i)(a_i-c)\) spread over \(V_i\setminus\{x\}\); negative mass \(D_j=(1-1/n_j)a_j+c/n_j\) at \(y\); and positive mass \(B_j=(1-1/n_j)(a_j-c)\) spread over \(V_j\setminus\{y\}\). Here these symbols denote total masses. They obey \(A_i+B_j=C_i+D_j\). If a part is a singleton, its corresponding spread mass is zero.

**2. Exact transportation between distinct parts.** Define
\[
f_i(t)=2\left(1-\frac1{n_i}\right)a_i-\left(1-\frac2{n_i}\right)c.
\]
The function taking value \(1\) at \(x\), \(-1\) at every other vertex of \(V_i\), and zero elsewhere is one-Lipschitz. Evaluating it against the preceding signed measure gives \(A_i+C_i=f_i(t)\). The symmetric function supported on \(V_j\), with the opposite orientation, gives \(B_j+D_j=f_j(t)\). Therefore Kantorovich duality gives
\[
W_1(\delta_xP_t,\delta_yP_t)\ge\max\{f_i(t),f_j(t)\}.
\]
For the reverse bound, if \(A_i\ge D_j\), first transport \(D_j\) from \(x\) to \(y\), then transport \(B_j\) from the positive sites in \(V_j\setminus\{y\}\) to the negative sites in \(V_i\setminus\{x\}\), and transport the residual \(A_i-D_j=C_i-B_j\) within \(V_i\) from \(x\). These transportation legs cost respectively one, one, and two per mass unit. Thus the cost is \(D_j+B_j+2(A_i-D_j)=A_i+C_i=f_i(t)\). If \(A_i<D_j\), exchange \(i,x\) with \(j,y\) and obtain the cost \(f_j(t)\). In both cases the inequality above is equality:
\[
W_1(\delta_xP_t,\delta_yP_t)=\max\{f_i(t),f_j(t)\}.
\]
The same construction remains valid for singleton parts, with all zero-mass terms omitted.

**3. Same-part pairs and the induced coefficient.** If \(x,y\in V_i\) are distinct, then the decomposition gives \((\delta_x-\delta_y)P_t=a_i(\delta_x-\delta_y)\). Since \(d(x,y)=2\), their Wasserstein-distance ratio equals \(a_i\). For \(n_i\ge2\),
\[
f_i(t)-a_i=\left(1-\frac2{n_i}\right)(a_i-c)\ge0.
\]
Thus no same-part pair exceeds the largest cross-part ratio. For any finite metric and Markov kernel, the induced \(W_1\) coefficient over all probability measures equals the maximum of the Dirac-pair ratios: transport an optimal coupling of \(\mu,\nu\) through optimal couplings of their kernel rows and use the triangle inequality, while Dirac pairs attain the reverse inequality. Consequently,
\[
C_G(t)=\max_i f_i(t).
\]
This also proves the dual statement for the Lipschitz seminorm.

**4. Largest-part universality.** For fixed \(N,t\ge0\), extend the part-size parameter to real \(z\ge1\) and put \(a(z)=e^{-(N-z)t}\). Direct differentiation gives
\[
\frac{\partial}{\partial z}\left[2(1-z^{-1})a(z)-(1-2z^{-1})c\right]
=\frac{2(a(z)-c)}{z^2}+2t(1-z^{-1})a(z)\ge0
\]
for \(z\le N\). Thus \(C_G(t)=f_m(t)\), proving the asserted closed formula. For \(t>0\), the derivative is positive whenever \(z>1\), so only maximum part sizes can attain the largest ratio.

**5. Sharp time regimes.** Differentiate the closed formula at zero:
\[
C_G'(0)=2m-N-2.
\]
For \(m=1\) or \(m=2\), the formula is a single decaying exponential. For \(m\ge3\), differentiating shows that a positive critical time exists precisely when \(2m>N+2\), and then it is the unique zero of \(C_G'\), namely the displayed \(t_*\). Since both exponential rates are positive and \(C_G(t)\to0\), this is the unique global maximum and it exceeds the initial value one. When \(2m\le N+2\), the derivative is nonpositive for all \(t\ge0\) (strictly negative for \(t>0\)), so the semigroup is nonexpansive. The sharp initial curvature is the negative of the derivative at zero. Substituting the critical-point identity yields the stated maximum.

## Verification
The numerical supplement `CHECK.py` independently forms the combinatorial Laplacian and computes its matrix exponential. For ten multipartite partitions and five nonnegative times each, it solves finite transportation linear programs for every Dirac pair using the graph-distance cost matrix, and checks the maximum against the exact formula. There are 50 graph/time comparisons; additional checks verify critical-time and peak formulas for three amplifying examples. Run `python CHECK.py` with NumPy and SciPy available; the package includes `requirements.txt`. These finite computations are supplementary and do not substitute for Steps 1–5.

## Relationship to prior work
Münch and Wojciechowski (arXiv:1712.00875, first public 2017-12-04) establish the general equivalence between graph curvature lower bounds and exponential Wasserstein/Lipschitz semigroup estimates. Pedrotti (arXiv:2308.00516, first public 2023-08-01) treats contractive couplings, curvature, and exponential Wasserstein bounds on Markov chains. Neither of the inspected relevant statements supplies this exact time-dependent multipartite norm or the largest-part partition universality. The standard complete bipartite two-class computation gives a related special case but does not determine the heat flow on three or more independent vertex classes, where additional edges alter both the generator and its metric. These mathematical distinctions do not establish worldwide historical priority.

## Limitations
All graph edges have unit jump rates and unit graph length; normalized random-walk generators, edge-dependent rates, other Wasserstein exponents, and arbitrary graphs are not addressed. Results on irregular multipartite graphs require exactly the combinatorial normalization above. The exact all-time formula is proved here, but possible equivalent historical presentations under Dobrushin coefficients, Ollivier curvature, or Lipschitz contraction terminology remain an originality risk. Numerical checks are finite and not a proof; no independent mathematical audit has been performed.

## References
- F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, first public 2017-12-04, arXiv:1712.00875, https://arxiv.org/abs/1712.00875.
- F. Pedrotti, *Contractive coupling rates and curvature lower bounds for Markov chains*, first public 2023-08-01, arXiv:2308.00516, https://arxiv.org/abs/2308.00516.
