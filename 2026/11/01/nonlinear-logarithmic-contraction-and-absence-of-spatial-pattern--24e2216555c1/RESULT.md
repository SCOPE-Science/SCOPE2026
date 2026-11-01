# Nonlinear logarithmic contraction and absence of spatial patterns in diffusing Michaelis–Menten networks

## Finding
Consider a finite network of species coupled by unit-Hill activation or inhibition, each with an arbitrary positive constant diffusivity and no-flux boundary conditions on a bounded connected smooth domain. Assume the directed interaction graph is strongly connected and that at least one basal input is positive or one edge is inhibitory. Then **any two strictly positive solutions contract exponentially in the supremum of their logarithmic ratios**, with an explicit rate depending only on the initial multiplicative bounds and the reaction parameters, not on the diffusivities or domain. Every nonnegative solution converges to the same spatially homogeneous positive equilibrium, and no nonconstant nonnegative stationary Neumann profile exists.

For any two strictly positive solutions \(u,v\), set
\[
\rho_\infty(u,v)=\max_{1\le i\le n}\max_{z\in\overline\Omega}\left|\log\frac{u_i(z)}{v_i(z)}\right|.
\]
Let \(\bar x\) denote the positive homogeneous equilibrium, let \(R\ge0\) bound both initial logarithmic distances from \(\bar x\), and put \(L_i=e^{-R}\bar x_i\), \(U_i=e^R\bar x_i\). For every interaction edge \(j\to i\) with saturation amplitude \(a_{ij}\), define
\[
q_{i,R}=b_i+\sum_{j\to i}\frac{\min\{h_{ij}(L_j),h_{ij}(U_j)\}^2}{a_{ij}},\qquad
\lambda_R=\min_i\frac{q_{i,R}}{U_i}>0.
\]
The exact contraction estimate, valid for every \(t\ge0\), is
\[
\boxed{\rho_\infty(u(t),v(t))\le e^{-\lambda_Rt}\rho_\infty(u(0),v(0)).}
\]
In particular, \(\rho_\infty(u(t),\bar x)\le e^{-\lambda_Rt}\rho_\infty(u(0),\bar x)\).

## Assumptions and scope
Let \(n\ge2\), \(\Omega\subset\mathbb R^m\) be bounded, connected, and have \(C^2\) boundary, with \(m\ge1\). For each species \(i\), fix \(\delta_i>0\), \(d_i>0\), and \(b_i\ge0\). For each ordered pair \(j\ne i\), its interaction is either absent, or has amplitude \(a_{ij}>0\), scale \(k_{ij}>0\), and one of the forms
\[
h_{ij}(s)=a_{ij}\frac{s}{k_{ij}+s}\quad\text{or}\quad
h_{ij}(s)=a_{ij}\frac{k_{ij}}{k_{ij}+s},\qquad s\ge0.
\]
The full initial–boundary value problem is
\[
\begin{aligned}
\partial_t u_i(t,z)&=\delta_i\Delta u_i(t,z)-d_i u_i(t,z)+b_i+\sum_{j\ne i}h_{ij}(u_j(t,z)),\\
\partial_\nu u_i(t,z)&=0,\qquad z\in\partial\Omega.
\end{aligned}
\]
The graph with an edge \(j\to i\) for a nonzero \(h_{ij}\) is strongly connected; additionally, \(b_i>0\) for at least one \(i\), or some edge is inhibitory. These are the existence/nondegeneracy conditions in E. D. Sontag (2026). For the stated estimate, the two initial profiles are continuous, strictly positive, and compatible with classical Neumann evolution (or interpreted as mild solutions and then obtained by approximation). Nonnegative continuous initial profiles, including the zero profile, are admitted for the convergence corollary.

**Quantifiers:** the claims hold for every number of species, every graph and rate constants satisfying the conditions, every bounded connected \(C^2\) spatial domain, every set of positive diagonal diffusion coefficients, and every permitted initial condition. There is no small-coupling, equal-diffusivity, monotone-graph, or one-dimensional-domain assumption.

## Proof
**1. Equilibrium and global solutions.** Define \(f_i(x)=b_i+\sum_{j\ne i}h_{ij}(x_j)\). The associated well-mixed ODE is \(\dot x_i=-d_i x_i+f_i(x)\). By the precise positivity, connectivity, and nondegeneracy assumptions, its unique nonnegative equilibrium \(\bar x\) exists and is strictly positive (Sontag, 2026, Sections 4–7). The reaction terms are locally Lipschitz in the nonnegative orthant, uniformly bounded above by \(b_i+\sum_j a_{ij}\), and inward-pointing on its coordinate boundary. Componentwise parabolic comparison yields global, bounded, nonnegative solutions. For strictly positive initial profiles, comparison with positive scalar lower solutions implies strict positivity at every finite time.

**2. The exact row-margin identity.** For either allowed nonzero interaction function and every \(s>0\), direct differentiation gives
\[
h_{ij}(s)-s|h'_{ij}(s)|=\frac{h_{ij}(s)^2}{a_{ij}}>0.
\]
Write \(y_i=\log u_i\) and define the log-reaction field
\[
G_i(y)=-d_i+e^{-y_i}f_i(e^y).
\]
Because \(f_i\) has no dependence on its own \(x_i\), its Jacobian satisfies
\[
\frac{\partial G_i}{\partial y_i}=-\frac{f_i(x)}{x_i},\quad
\frac{\partial G_i}{\partial y_j}=\frac{x_jh'_{ij}(x_j)}{x_i}\ (j\ne i),
\]
and therefore
\[
\frac{\partial G_i}{\partial y_i}+\sum_{j\ne i}\left|\frac{\partial G_i}{\partial y_j}\right|
=-\frac{q_i(x)}{x_i},\qquad
q_i(x)=b_i+\sum_{j\to i}\frac{h_{ij}(x_j)^2}{a_{ij}}>0.
\]
This identity is the nonlinear reaction-side observation of Sontag (2026); the new step below is the spatial comparison.

**3. A common invariant multiplicative box and an explicit rate.** Fix \(R>0\) containing both initial profiles and the equilibrium in \(K_R=\prod_i[L_i,U_i]\). Each \(h_{ij}\) is monotone, so the exact minimum of \(q_i(x)/x_i\) on \(K_R\) is \(q_{i,R}/U_i\); the variables in the numerator are distinct from \(x_i\). Thus the Jacobian row margins of \(G\) are at most \(-\lambda_R\) on \(\log K_R\). At the first point where some \(y_i\) might cross the upper face \(\log\bar x_i+R\), the mean-value formula applied to \(G(y)-G(\log\bar x)\), together with all other log-deviations having modulus at most \(R\), gives \(G_i(y)\le-\lambda_RR\). At this point, the diffusion term in the logarithmic equation, \(\delta_i(\Delta y_i+|\nabla y_i|^2)\), is nonpositive by the Neumann maximum principle. The upper face cannot be crossed. The lower face has the reversed signs and likewise cannot be crossed. Standard first-contact/\(\varepsilon\)-barrier arguments justify this for continuous solutions. The case \(R=0\) is the constant equilibrium by uniqueness. Both evolving profiles remain in \(K_R\).

**4. Contraction with diffusion.** For any two positive solutions set \(y_i=\log u_i\), \(z_i=\log v_i\), and \(w_i=y_i-z_i\). Subtraction of their exact logarithmic equations gives
\[
\partial_t w_i=\delta_i\left(\Delta w_i+(\nabla y_i+\nabla z_i)\cdot\nabla w_i\right)+\sum_j A_{ij}(t,\xi)w_j,
\]
where
\[
A_{ij}(t,\xi)=\int_0^1\frac{\partial G_i}{\partial y_j}\bigl(z(t,\xi)+s(y(t,\xi)-z(t,\xi))\bigr)\,ds.
\]
The integrand lies in the logarithmic box, and \(A_{ii}+\sum_{j\ne i}|A_{ij}|\le-\lambda_R\). At a point and component attaining \(M(t)=\max_{i,\xi}|w_i(t,\xi)|\), multiply the component equation by \(\operatorname{sgn}(w_i)\). The Neumann maximum principle makes the Laplacian term nonpositive, the first-order spatial term vanishes, and the reaction term is bounded by \(-\lambda_R M(t)\). The upper-right Dini derivative therefore satisfies \(D^+M(t)\le-\lambda_R M(t)\), including component or spatial ties. Gronwall's lemma gives the displayed estimate.

**5. Global convergence and exclusion of patterns.** Applying the estimate with \(v(t,\xi)=\bar x\) proves exponential convergence of positive solutions. Every nonnegative initial profile becomes strictly positive in every species for every \(t>0\): a positive basal input or inhibitory interaction supplies one species, parabolic positivity and the strong connectedness of the directed graph propagate strict positivity through all species, and uniqueness prevents loss of it. Restart the contraction at any fixed positive time. Any nonnegative stationary profile must then be positive and, by convergence, identical to the homogeneous equilibrium. Consequently nonconstant stationary patterns, nontrivial recurrent attractors, and diffusion-driven instability of that equilibrium are excluded within this PDE class.

## Verification
The accompanying standalone `verify.py` uses only Python's standard library and exact rational arithmetic. Running `python verify.py` checks 54 saturation-derivative identities at positive rational parameters, nine three-node Jacobian-margin identities, an explicit box-rate evaluation, and a counterexample to globally negative constant-norm Jacobian measures. It prints `PASS 65 exact rational identities; fixed-norm spectral obstacle 19/18` on success. The infinite-dimensional maximum-principle argument is analytical; these finite algebraic checks are supporting diagnostics, not a numerical proof.

For a concrete two-node mutually inhibitory example, let \(d_1=d_2=1/3\), \(b_1=b_2=0\), and \(h(s)=1/(1+2s)\). Then \(\bar x=(1,1)\), and the box \([1/2,2]^2\) gives the diffusion-independent explicit rate \(\lambda_{\log2}=1/50\). Moreover, at the positive state \((1/10,1/10)\) the Jacobian of the **untransformed reaction ODE** has positive eigenvalue \(19/18\). Thus no fixed vector norm can have a globally negative matrix measure for this reaction system, distinguishing this theorem from the usual fixed weighted \(L^p\)-norm criterion.

## Relationship to prior work
Sontag (2026, arXiv:2610.24351v1) proves the global nonlinear logarithmic contraction for well-mixed ODEs and gives the exact reaction-side row-margin identity; it does **not** treat spatial diffusion. Blanchini, Breda, Giordano and Liessi (2023) prove structural existence, uniqueness and local stability in the same well-mixed network class, including a delay extension, but do not establish the displayed spatial result.

Aminzare and Sontag (2012/2013, arXiv:1208.0326v2, Theorem 2) prove inheritance of contraction under diffusion for **fixed diagonally weighted \(L^p\)** norms, a closely related and important theorem. It does not imply the present full-class theorem under its stated hypotheses: the explicit inhibitory example above has a Jacobian with positive spectral abscissa at a positive state and therefore cannot satisfy any uniform strictly negative constant-norm logarithmic measure on the whole orthant. The new point is to carry a state-dependent logarithmic metric through the nonlinear diffusion operator, where gradient-square terms cancel at extrema of log differences.

## Limitations
The theorem requires diagonal, positive, constant diffusion and homogeneous Neumann conditions; it makes no assertion for cross-diffusion, chemotaxis, advective boundary flux, nonlocal reactions, or Hill exponents exceeding one. The contraction rate depends on the initial multiplicative box and can be small near the positive-orthant boundary; no globally uniform rate across all strictly positive data is asserted. A full independent review or historical-priority certification has not been performed. Older or differently formulated nonlinear-metric spatial contraction theorems may provide a broader implication, beyond the inspected fixed-norm literature.

## References
1. Eduardo D. Sontag, *Global stability of Michaelis–Menten networks*, arXiv:2610.24351v1, publicly submitted 17 October 2026. https://arxiv.org/html/2610.24351v1
2. Zahra Aminzare and Eduardo D. Sontag, *Logarithmic Lipschitz norms and diffusion-induced instability*, arXiv:1208.0326v2 (2012), *Nonlinear Analysis* 83 (2013), 31–49. https://arxiv.org/html/1208.0326v2
3. Franco Blanchini, Dimitri Breda, Giulia Giordano, and Davide Liessi, *Michaelis–Menten networks are structurally stable*, *Automatica* 147 (2023), 110683. https://iris.unitn.it/bitstream/11572/364267/3/Automatica_MichaelisMenten.pdf
4. Shodhan Rao and Manvel Gasparyan, *On the stability of a class of Michaelis–Menten networks*, *Automatica* 169 (2024), 111837. https://doi.org/10.1016/j.automatica.2024.111837
