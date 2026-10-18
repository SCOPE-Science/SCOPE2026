# Sharp disconnected network Turing windows with strict local prey and predator biomass loss

## Finding

**Theorem (exact modal thresholds and local demographic cost of patterning).** Let \(G\) be a finite connected, simple, undirected graph with \(n\ge2\) vertices, and let \(L=D-A\) be its nonnegative combinatorial Laplacian. For \(t>0\) and predator-to-prey mobility ratio \(r>0\), consider the network ecological system
\[
\dot u_i=u_i(-u_i^2+3u_i-1-v_i)-t(Lu)_i,\qquad
\dot v_i=v_i(4u_i-3v_i-1)-rt(Lv)_i. \tag{1}
\]
The strictly positive spatially uniform equilibrium is \(u_i=v_i=1\). Write the distinct positive Laplacian eigenvalues, with multiplicities when necessary, as \(\lambda>0\).

For every \(0<r<9\), the uniform equilibrium is linearly exponentially stable for all \(t>0\). At \(r=9\) it has no exponentially growing modes; it is nonhyperbolic precisely at \(t=1/(3\lambda)\) for a positive Laplacian eigenvalue. For \(r>9\), set
\[
z_\pm(r)=\frac{r-3\pm\sqrt{(r-1)(r-9)}}{2r},\qquad 0<z_-<z_+<1.
\]
The uniform equilibrium has a positive-real-part eigenvalue **if and only if**
\[
t\in\bigcup_{\lambda>0}\left(\frac{z_-}{\lambda},\frac{z_+}{\lambda}\right). \tag{2}
\]
It is exponentially stable outside the union of the corresponding **closed** intervals. Any remaining endpoints are nonhyperbolic unless another mode is unstable.

At a threshold \(t_*=z_\pm/\lambda\), assume \(\lambda>0\) is a simple Laplacian eigenvalue and no other Laplacian eigenmode has zero modal determinant there. If \(L\phi=\lambda\phi\) and \(\phi\ne0\), there is a locally unique smooth branch, up to choice of scalar parametrization, of strictly positive *nonuniform stationary solutions*
\[
u_i(s)=1+s\phi_i+O(s^2),\quad v_i(s)=1+h s\phi_i+O(s^2),\quad t(s)=t_*+O(s),\quad h=1-z_\pm\in(0,1). \tag{3}
\]
Let \(\bar u=n^{-1}\sum_i u_i\), \(\bar v=n^{-1}\sum_i v_i\), and \(\sigma^2=n^{-1}\sum_i\phi_i^2>0\). **Both population means fall strictly below the homogeneous level** along every sufficiently small nonzero point of this branch:
\[
\bar u(s)=1-(7h-3h^2)\sigma^2s^2+o(s^2),\qquad
\bar v(s)=1-(8h-3h^2)\sigma^2s^2+o(s^2). \tag{4}
\]
In particular, the predator mean has the larger quadratic deficit by \(h\sigma^2s^2+o(s^2)\). This is a claim about equilibria, not about their attraction or global persistence.

The stronger, exact finite-amplitude balance law holds at **every** stationary configuration of (1), with \(U_i=u_i-1\), \(V_i=v_i-1\) and angle brackets denoting vertex averages:
\[
\bar u-1=-7\langle UV\rangle+3\langle V^2\rangle-3\langle U^3\rangle,\qquad
\bar v-1=-8\langle UV\rangle+3\langle V^2\rangle-4\langle U^3\rangle. \tag{5}
\]
Formula (5) by itself does not assert global negativity for arbitrary, far-from-uniform equilibria.

**Arbitrarily many separated threshold crossings.** On the path \(P_n\), the \(n-1\) positive Laplacian eigenvalues are simple and are exactly
\[
\lambda_j=2-2\cos(j\pi/n),\qquad 1\le j\le n-1.
\]
For every \(n\ge3\), choose \(r>9\) sufficiently close to \(9\) that
\[
\frac{z_+(r)}{z_-(r)}<\min_{1\le j<n-1}\frac{\lambda_{j+1}}{\lambda_j}. \tag{6}
\]
Such a choice always exists. Then (2) consists of **exactly \(n-1\) disjoint open instability intervals**, separated by nonempty intervals of exponential stability, and all \(2(n-1)\) endpoints give branches satisfying (4). For \(n=2\), there is one interval and two such endpoints for every \(r>9\). Thus no graph-independent finite bound exists on the number of stability losses and recoveries as the scalar dispersal intensity varies.

For example, with \(P_3\) and \(r=91/10\), \(z_-=2/7\), \(z_+=5/13\), and the two disjoint unstable intervals are exactly \((2/21,5/39)\) and \((2/7,5/13)\).

## Assumptions and scope

The system is deterministic, finite dimensional, and has an undirected unweighted connected graph; the same graph carries both species, with constant migration rates in ratio \(r\). The positive quadrant is forward invariant because local reaction terms vanish when the corresponding species is absent and graph diffusion has nonnegative off-diagonal contributions. With predators absent, prey per-capita growth is \(-u^2+3u-1\), which is negative near zero and positive on an intermediate positive interval, giving a strong Allee effect. The predator reaction includes reproduction proportional to prey and quadratic intraspecific regulation. All assertions are about the specified polynomial model, **not** an exact reduction of the motivating weak-Allee/hyperbolic-mortality model.

Statements (3)–(4) use a simple critical spatial eigenvalue and exclude coincident critical modes. The path construction ensures both hypotheses automatically at every endpoint. In (3), eigenvector normalization determines the scale of \(s\) and \(\sigma^2\). In the cosine eigenvector normalization \(\phi_i=\cos((i-1/2)j\pi/n)\) on \(P_n\), \(\sigma^2=1/2\).

## Proof

**1. Exact linear phase diagram.** The local Jacobian at \((1,1)\) is
\[
J=\begin{pmatrix}1&-1\\4&-3\end{pmatrix},\quad \operatorname{tr}J=-2,\quad \det J=1.
\]
Decomposing perturbations into orthogonal \(L\)-eigenvectors yields a \(2\)-by-\(2\) mode matrix for \(z=t\lambda\):
\[
M(z)=\begin{pmatrix}1-z&-1\\4&-3-rz\end{pmatrix},\quad
\operatorname{tr}M=-2-(1+r)z<0,\quad
\det M=1-(r-3)z+rz^2.
\]
The positive-eigenvalue modes are exactly those with negative determinant; this gives (2). When \(r\le3\) the determinant is manifestly positive for \(z\ge0\), and when \(3<r<9\) its discriminant \((r-1)(r-9)\) is negative. At \(r=9\) the determinant is \((1-3z)^2\). When \(r>9\), the two simple positive roots above give a negative-determinant interval. Both roots are strictly below one. This proves the stability assertions (strictly positive determinant and negative trace are equivalent to exponential stability for each finite-dimensional real mode).

**2. Local patterned branch.** Define the stationary map \(F(u,v,t)\) using the right sides of (1). At a stated isolated threshold, its derivative in state has a one-dimensional kernel spanned by \((\phi,h\phi)\), where the first modal equation gives \(h=1-z_\pm\). All other modal blocks are invertible, and the critical block has one simple zero and one strictly negative eigenvalue. Differentiation in the scalar parameter \(t\) gives the crossing determinant
\[
\frac{\mathrm d}{\mathrm dt}\det M(t\lambda)\bigg|_{t=t_*}
=\lambda(2rz_\pm-(r-3))=\pm\lambda\sqrt{(r-1)(r-9)}\ne0.
\]
Because the critical zero eigenvalue is simple, its derivative is nonzero if and only if this determinant derivative is nonzero. This is precisely the transversality condition \(D_tD_{(u,v)}F\,p\notin\operatorname{Range}D_{(u,v)}F\). The finite-dimensional simple-eigenvalue bifurcation theorem therefore yields a smooth nontrivial local solution curve (3), unique near the uniform branch under the stated normalization. Positivity holds by continuity from \((1,1)\), and \(\sum_i\phi_i=0\) because \(\lambda>0\) and \(G\) is connected.

**3. Exact spatial means.** Put \(U=u-\mathbf 1\) and \(V=v-\mathbf 1\). Direct polynomial expansion gives
\[
u_i(-u_i^2+3u_i-1-v_i)=U_i-V_i-U_iV_i-U_i^3,\]
\[
v_i(4u_i-3v_i-1)=4U_i-3V_i+4U_iV_i-3V_i^2.
\]
At equilibrium, summing each equation over vertices eliminates both migration terms because \(\mathbf 1^\mathsf TL=0\). Writing \(a=\bar u-1\) and \(b=\bar v-1\), the two scalar equations are \(a-b=\langle UV\rangle+\langle U^3\rangle\) and \(4a-3b=-4\langle UV\rangle+3\langle V^2\rangle\). Invert this nonsingular \(2\)-by-\(2\) system to obtain the exact identities (5). Along the branch (3), \(\langle UV\rangle=h\sigma^2s^2+o(s^2)\), \(\langle V^2\rangle=h^2\sigma^2s^2+o(s^2)\), and \(\langle U^3\rangle=O(s^3)\). Substitution gives (4). Both factors \(7h-3h^2\) and \(8h-3h^2\) are positive for \(0<h<1\), establishing strict local loss.

**4. Path reentry.** The path spectrum above follows by direct substitution of cosine eigenvectors into the endpoint/interior Laplacian equations. It is positive and strictly increasing in \(j\) and every eigenvalue is simple. The ratio of successive positive eigenvalues has a minimum \(q_n>1\) for each fixed \(n\ge3\). By continuity \(z_+(r)/z_-(r)\to1\) as \(r\downarrow9\), so (6) can always be arranged. With (6), the interval for \(\lambda_{j+1}\) ends strictly before that for \(\lambda_j\) begins, yielding exactly \(n-1\) mutually disjoint instability intervals with stable gaps. Each endpoint has exactly one zero mode, so Steps 2–3 apply. For \(n=2\) only \(\lambda_1=2\) appears. The \(P_3\) example follows by exact substitution.

## Verification

Run `python verify.py` with Python 3, SymPy, and NumPy. The program checks the reaction expansions, Jacobian and determinant identities, both spatial-mean identities, exact rational roots for the \(P_3\) example, and path spectra/disjoint intervals for \(2\le n\le40\). These finite numerical spectral checks do **not** certify all graph orders: the analytic spectrum proof and continuity argument above cover all finite \(n\). The simple-eigenvalue local bifurcation uses a standard analytic theorem, not a computational continuation certificate.

## Relationship to prior work

Nakao and Mikhailov (2010) derive network-Laplacian modal instability for activator-inhibitor systems. Ye and Zhou (2023, arXiv:2306.11818, full HTML inspected) derive a Turing instability interval and numerical patterns for a **different** weak-Allee, hyperbolic-mortality predator-prey model on random graphs. Shi, Zhou, and Ye (2023) extend that setting to multiplex networks and track spatial densities numerically. Accordingly, the generic modal criterion, generic network Turing phenomenon, and local bifurcation theorem are **prior knowledge**; they are not new claims here. The assessed contribution is the exact nonlinear two-species mean-deficit law tied to every simple threshold of the stated strong-Allee polynomial ecological system, together with its fully resolved disconnected path-scale phase diagram and strict mobility threshold. Related 2024 work on clustering and Turing patterns was found only in abstract-accessible form and creates residual literature-coverage uncertainty, not a claim of proved noncoverage.

## Limitations

The modeled reaction kinetics are an intentionally tractable strong-Allee variant, not the source's original rational weak-Allee equations, so the derived coefficients must not be attributed to those equations. The small patterned branches need not be stable, observable long-term states; stability here refers to the homogeneous equilibrium except where explicitly stated. Formula (5) does not force negative biomass change for all distant stationary states. This analysis does not address stochastic networks, directed graphs, nonlinear mobility, global attraction, or empirical calibration. Published-literature priority remains subject to independent verification.

## References

1. Yong Ye and Jiaying Zhou, *Pattern formation in a predator-prey model with Allee effect and hyperbolic mortality on networked and non-networked environments*, arXiv:2306.11818, first submitted 2023-06-20. https://arxiv.org/html/2306.11818v2
2. Lei Shi, Jiaying Zhou, and Yong Ye, *Pattern Formation in a Predator-Prey Model with Allee Effect and Hyperbolic Mortality on Multiplex Networks*, 2023-06-27. https://www.preprints.org/manuscript/202306.1868
3. Hiroya Nakao and Alexander S. Mikhailov, *Turing patterns in network-organized activator-inhibitor systems*, 2010. https://arxiv.org/abs/1005.1986
4. Xiaofeng Luo et al., *The relationship between clustering and networked Turing patterns*, Chaos 34, 073114 (2024), doi:10.1063/5.0195450 (abstract consulted; full text not verified).
