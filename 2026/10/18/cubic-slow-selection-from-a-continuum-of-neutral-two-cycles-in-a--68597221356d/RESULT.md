# Cubic slow selection from a continuum of neutral two-cycles in a quadratic fractional map

## Finding

Consider the homogeneous rational recurrence
\[
 x_{n+1}=\frac{x_{n-1}^{2}}{a x_n^{2}+b x_nx_{n-1}+c x_{n-1}^{2}},\qquad n\geq0,
\]
with \(b>0\), \(a>0\), and the critical relation \(c=b+3a\). Put \(\varepsilon=a/b\) and \(y_n=bx_n\). Given any fixed \(u_0\in(0,1)\), prescribe \(y_{-1}=u_0\), \(y_0=1-u_0\). For \(j\geq0\), write \((u_j,v_j)=(y_{2j-1},y_{2j})\).

**Slow-flow theorem.** As \(\varepsilon\downarrow0\), the piecewise-constant paths \(u_{\lfloor t/\varepsilon\rfloor}\) and \(v_{\lfloor t/\varepsilon\rfloor}\) converge, uniformly on every compact time interval on which the limiting solution remains in \((0,1)\), to \(U(t)\) and \(1-U(t)\), respectively. Here \(U(0)=u_0\) and
\[
 \dot U=\frac{(2U-1)^3}{U^2-U+1}.
\]
For \(u_0\ne1/2\), set \(D(t)=2U(t)-1\) and \(D_0=2u_0-1\). Until \(|D(t)|=1\), the solution is characterized exactly by
\[
 t=\frac{3}{16}\left(D_0^{-2}-D(t)^{-2}\right)+\frac18\log\frac{|D(t)|}{|D_0|}.
\]
In particular, \(U\) moves strictly away from \(1/2\). For any fixed threshold \(u_1\in(0,1)\) farther from \(1/2\) on the same side as \(u_0\), let \(J_\varepsilon\) be the first two-step index at which \(u_j\) crosses \(u_1\) in that outward direction. With \(D_1=2u_1-1\),
\[
 \boxed{\lim_{\varepsilon\downarrow0}\varepsilon J_\varepsilon
 =\frac{3}{16}\left(D_0^{-2}-D_1^{-2}\right)
  +\frac18\log\frac{|D_1|}{|D_0|}.}
\]
Thus the corresponding **original iteration count** is asymptotic to \(2b/a\) times the displayed positive constant. The theorem applies to fixed interior initial data and thresholds; it does not assert uniformity as \(u_0\to1/2\), \(u_0\to0,1\), or the threshold approaches an endpoint.

## Assumptions and scope

All initial data in the theorem are strictly positive. The map is well-defined for every forward iterate. The critical relation \(c=b+3a\) is the nonhyperbolic equilibrium boundary in the original rational family. At \(a=0\), \(c=b\), the normalized planar map becomes
\[
 T_0(u,v)=(v,u/(u+v)),
\]
so its entire open line segment \(\{(u,1-u):0<u<1\}\) consists of two-step fixed points (equilibria at \(u=1/2\), genuine two-cycles otherwise). The theorem describes precisely how positive but small \(a/b\) resolves this neutral family over long observation times. The primary mathematical subject is planar dynamical bifurcation and singularly slow orbit selection, not a claim about arbitrary rational recurrences.

## Proof

**1. Normalize the dynamics.** With \(\varepsilon=a/b\) and \(c=b+3a\), the normalized recurrence reads
\[
 y_{n+1}=\frac{y_{n-1}^2}{\varepsilon y_n^2+y_ny_{n-1}+(1+3\varepsilon)y_{n-1}^2}.
\]
Define
\[
 Q_\varepsilon(u,v)=\frac{u^2}{\varepsilon v^2+uv+(1+3\varepsilon)u^2},\qquad
 T_\varepsilon(u,v)=(v,Q_\varepsilon(u,v)),\qquad F_\varepsilon=T_\varepsilon^2.
\]
For \(v=1-u\), direct substitution gives \(F_0(u,v)=(u,v)\). For \(u\in(0,1)\), its Jacobian along this line is
\[
 DF_0(u,v)=\begin{pmatrix}v&-u\\-v^2&u(1+v)\end{pmatrix}.
\]
Its eigenvalues are \(1\) along the tangent \((1,-1)\) and \(uv\) transversally, with \(0<uv\leq1/4\). This uniform spectral gap is the mechanism behind the slow reduction.

**2. Determine the first-order map without discarding the fast variable.** Write \(s=u+v-1\), so \(v=1-u+s\), and denote \((u^+,s^+)\) the corresponding coordinates of \(F_\varepsilon(u,v)\). On a compact interior segment, rational Taylor expansion at \((s,\varepsilon)=(0,0)\) gives, with uniform remainders,
\[
 \begin{split}
 u^+&=u-us+\varepsilon H_1(u)+O(s^2+\varepsilon|s|+\varepsilon^2),\\
 s^+&=\lambda(u)s+\varepsilon H_s(u)+O(s^2+\varepsilon|s|+\varepsilon^2),
 \end{split}
\]
where \(v=1-u\) in the coefficient functions and
\[
 \lambda(u)=u(1-u),\qquad
 H_1(u)=-\bigl(v^2+3u^2\bigr),\qquad
 H_s(u)=-u\bigl(v^2+3u^2\bigr)-u^2-3v^2.
\]
These identities follow by differentiating the explicit rational map; in particular, the transverse forcing \(H_s\) cannot be omitted when computing the tangent drift.

**3. Eliminate the contracted direction rigorously.** Fix \(T>0\) such that the claimed limiting solution, once constructed, stays within a compact interval \(K\Subset(0,1)\) up to time \(T\). Work first on a slightly larger compact interval. The initial transverse coordinate is \(s_0=0\). Because \(\lambda(u)\leq1/4\), the second expansion and a bootstrap argument show \(|s_j|\leq C\varepsilon\) as long as \(u_j\) remains in this interval and \(j\varepsilon\leq T\). Put
\[
 h(u)=\frac{H_s(u)}{1-\lambda(u)},\qquad r_j=s_j-\varepsilon h(u_j).
\]
The first expansion implies \(u_{j+1}-u_j=O(\varepsilon)\). Hence the smoothness of \(h\), the transverse expansion, and \(s_j=O(\varepsilon)\) imply
\[
 r_{j+1}=\lambda(u_j)r_j+O(\varepsilon^2).
\]
Consequently \(|r_j|\leq C(q^j\varepsilon+\varepsilon^2)\) for a fixed \(q<1\), and \(\sum_{j\leq T/\varepsilon}|r_j|=O(\varepsilon)\). Substitution in the first expansion therefore yields
\[
 u_{j+1}=u_j+\varepsilon g(u_j)-u_jr_j+O(\varepsilon^2),\qquad
 g(u)=H_1(u)-\frac{uH_s(u)}{1-\lambda(u)}.
\]
Using \(u+v=1\), an exact simplification produces
\[
 (1-uv)g(u)=-v(v^2+3u^2)+u^3+3uv^2=(u-v)^3,
\]
so \(g(u)=(2u-1)^3/(u^2-u+1)\). The cumulative perturbation \(\sum_j[-u_jr_j+O(\varepsilon^2)]\) is \(O(\varepsilon)\) over \(O(\varepsilon^{-1})\) steps. Ordinary Euler-scheme comparison and the discrete Grönwall inequality therefore prove uniform convergence to \(\dot U=g(U)\) up to time \(T\). This estimate simultaneously shows \(s_j\to0\) uniformly. A continuation argument justifies the compact-interval bootstrap.

**4. Integrate and extract the first-crossing clock.** With \(D=2U-1\),
\[
 \dot D=\frac{8D^3}{3+D^2},\qquad
 dt=\left(\frac{3}{8D^3}+\frac1{8D}\right)dD.
\]
Integration from \(D_0\) to \(D(t)\) gives the asserted inverse-square plus logarithm identity. The vector field is nonzero and outward-pointing on either side of \(1/2\); the solution crosses each strictly outward interior threshold exactly once and transversely. Uniform convergence of the trajectories on compact intervals immediately before and after the crossing implies convergence of their first-crossing times. This establishes the formula for \(\varepsilon J_\varepsilon\) and finishes the proof.

## Verification

The bundled `verify.py` checks rational Taylor coefficients at several exact rational positions, tests the algebraic drift reduction, integrates the explicit slow ODE numerically, and directly iterates the original rational recurrence for decreasing \(\varepsilon\). A checker passing does **not** establish the infinite-parameter limit; the preceding estimates do. At the test initial condition \(u_0=3/4\) and outward threshold \(u_1=4/5\), the predicted rescaled first-crossing time is
\[
 \frac{11}{48}+\frac18\log(6/5)\approx0.251956861265911.
\]
(The rational term is \(3(4-25/9)/16=11/48\).) Exact coefficient checks and numerical convergence are separately reported in `VERIFICATION.md`.

## Relationship to prior work

Garić-Demirović, Kulenović, and Nurkanović (2013) study the **same** quadratic fractional recurrence. Their Theorem 14 identifies the critical surface \(3a+b-c=0\), the nonhyperbolic equilibrium, two boundary attracting period-two states, and basin separation. These are treated here as prior results, not new claims. The new claim is the exact long-time scaling limit as \(a/b\downarrow0\), the reduced cubic drift derived after a nontrivial transverse correction, and its inverse-square/logarithmic first-exit constant. The earlier qualitative basin theorem does not state these quantities. General invariant-manifold results of Kulenović and Merino (2009/2010) establish invariant curves under spectral hypotheses but do not compute the slow flow or first-crossing law for this parameter-singular family. A general normal-hyperbolicity theorem can support the *method*, not supply the displayed coefficient without calculation.

## Limitations

The result concerns fixed positive interior initial states on the limiting neutral two-cycle segment and fixed interior first-crossing thresholds. It does not provide a uniform asymptotic if the initial phase approaches the midpoint on the \(\sqrt\varepsilon\) scale, nor does it determine the final approach to the boundary two-cycle after the limiting path reaches an endpoint. The originality assessment is based on identified literature and searches, not an independent priority determination; some source full-text access was limited. No mathematical statement of this note has received independent audit.

## References

1. M. Garić-Demirović, M. R. S. Kulenović, and M. Nurkanović, “Global Dynamics of Certain Homogeneous Second-Order Quadratic Fractional Difference Equation,” *The Scientific World Journal* (first publicly available 4 December 2013), article 210846, DOI: 10.1155/2013/210846. https://pmc.ncbi.nlm.nih.gov/articles/PMC3867926/
2. M. R. S. Kulenović and O. Merino, “Invariant Manifolds for Competitive Systems in the Plane,” arXiv:0905.1772 (12 May 2009), later *International Journal of Bifurcation and Chaos* 20 (2010), 2471–2486. https://arxiv.org/abs/0905.1772
3. M. R. S. Kulenović and O. Merino, “Competitive-exclusion versus competitive-coexistence for systems in the plane,” *Discrete and Continuous Dynamical Systems B* 6 (2006), 1141–1156. https://doi.org/10.3934/dcdsb.2006.6.1141
