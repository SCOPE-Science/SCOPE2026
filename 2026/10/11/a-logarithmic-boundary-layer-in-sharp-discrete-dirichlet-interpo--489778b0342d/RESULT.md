# A logarithmic boundary layer in sharp discrete Dirichlet interpolation

## Finding
For every integer \(m\ge 1\), let \(K_m\) be the best constant in the pointwise interpolation inequality
\[
 |u_m|^2\le K_m\left(\sum_{j=1}^{\infty}|u_j|^2\right)^{1/2}
 \left(\sum_{j=0}^{\infty}|u_{j+1}-u_j|^2\right)^{1/2},
 \qquad u_0=0,\quad u\in\ell^2(\mathbb N;\mathbb R).
\]
Let \(r_m\in(0,1)\) denote the unique solution of
\[
 (1-r_m)(1-r_m^{2m})=4m\,r_m^{2m}(1+r_m).
\]
Then every constant and every equality case is explicit:
\[
 \boxed{K_m=\frac{2\sqrt{r_m}}{1+r_m}(1-r_m^{2m})},\qquad
 \boxed{u_j=c\bigl(r_m^{|j-m|}-r_m^{j+m}\bigr)\ (j\ge1),\ c\in\mathbb R\setminus\{0\}.}
\]
In particular, \(K_1=4/(3\sqrt3)\), the constants are strictly increasing, and \(K_m<1\) for each finite site. The exact leading boundary deficit is logarithmic, not a pure power:
\[
 \boxed{\lim_{m\to\infty}\frac{m^2(1-K_m)}{(\log m)^2}=\frac18.}
\]
More precisely, as \(m\to\infty\),
\[
 \boxed{8m^2(1-K_m)
 = (\log m)^2-(\log m)\log\log m+(1+\log8)\log m+o(\log m).}
\]
The bulk full-lattice sharp constant is \(1\), but each fixed site at finite distance from the Dirichlet boundary has a strict quantitative deficit.

## Assumptions and scope
All sums are over the indicated countably infinite index sets; the scalar field is real. The sequence \(u=(u_j)_{j\ge1}\) is square summable, is extended to \(u_0=0\), and has \((u_{j+1}-u_j)_{j\ge0}\in\ell^2\) automatically because the first-difference operator is bounded. The index \(m\) ranges over **all** positive integers. There are no continuum-limit assumptions or numerical cutoff assumptions. The asymptotics concern \(m\to\infty\) at fixed unit lattice spacing.

## Proof
**1. Resolvent reproducing inequality.** Let \(L\) be the Dirichlet discrete Laplacian on \(\ell^2(\mathbb N)\),
\[
 (Lu)_j=2u_j-u_{j-1}-u_{j+1},\qquad u_0=0.
\]
It is bounded, positive, self-adjoint, and satisfies \(\langle u,Lu\rangle=\|Du\|_2^2\). For \(t>0\), write \(g_t=(L+tI)^{-1}e_m\) and \(G_m(t)=\langle e_m,g_t\rangle\). Cauchy–Schwarz in the strictly positive quadratic form \(L+tI\) gives
\[
 |u_m|^2\le G_m(t)\bigl(t\|u\|_2^2+\|Du\|_2^2\bigr),
\]
with equality precisely when \(u\) is proportional to \(g_t\). For nonzero \(u\), put \(q=\|Du\|_2^2/\|u\|_2^2>0\) and choose \(t=q\). This yields
\[
 \frac{|u_m|^2}{\|u\|_2\|Du\|_2}
 \le 2\sqrt q\,G_m(q),\qquad
 K_m\le\sup_{t>0}2\sqrt t\,G_m(t).
\]

**2. Exact half-line Green kernel.** Put
\[
 r=r(t)=\frac{2+t-\sqrt{t(t+4)}}2\in(0,1),
 \qquad t=\frac{(1-r)^2}{r}.
\]
The image construction on the full-line resolvent gives
\[
 (L+tI)^{-1}_{ij}=
 \frac{r^{|i-j|}-r^{i+j}}{\sqrt{t(t+4)}},\qquad i,j\ge1.
\]
Indeed this kernel satisfies the difference equation with unit source at \(i=j\), decays geometrically at infinity, and vanishes at \(i=0\); uniqueness follows from strict positivity of \(L+tI\). Therefore
\[
 G_m(t)=\frac{1-r^{2m}}{\sqrt{t(t+4)}},\qquad
 2\sqrt t\,G_m(t)=h_m(r):=\frac{2\sqrt r}{1+r}(1-r^{2m}).
\]
Both endpoint limits of \(h_m\) on \([0,1]\) are zero, so its maximum is attained strictly inside \((0,1)\).

**3. Unique maximizing parameter.** Logarithmic differentiation gives
\[
 \frac{2r h_m'(r)}{h_m(r)}=
 \frac{1-r}{1+r}-\frac{4m r^{2m}}{1-r^{2m}}.
\]
Thus stationarity is equivalent to
\[
 \frac{1-r}{1+r}\bigl(r^{-2m}-1\bigr)=4m.
\]
The left side is a product of two strictly positive, strictly decreasing factors on \((0,1)\), and decreases continuously from infinity to zero. Consequently, \(r_m\) exists uniquely and is the global maximum. At \(m=1\), cancellation reduces the stationary equation to \((1-r)^2=4r^2\), hence \(r_1=1/3\) and \(K_1=4/(3\sqrt3)\).

**4. Attainment, uniqueness, and comparison of sites.** Differentiating the resolvent identity in \(t\) gives \(G_m'(t)=-\|g_t\|_2^2\). Also
\[
 \|Dg_t\|_2^2=G_m(t)-t\|g_t\|_2^2.
\]
At the unique stationary maximum of \(\sqrt tG_m(t)\), the derivative equation is \(G_m(t)+2tG_m'(t)=0\). Substitution yields \(\|Dg_t\|_2^2=t\|g_t\|_2^2\). Thus \(q=t\) for \(u=g_t\), so **both** inequalities in Step 1 become equalities. The Green function formula yields the stated equality sequences. Conversely, equality in Step 1 forces a Green vector, and the maximizing parameter is unique, proving exhaustiveness up to nonzero scalar multiples.

For each fixed \(r\in(0,1)\), \(h_{m+1}(r)>h_m(r)\). Evaluating the left side at the unique maximizer for site \(m\) gives \(K_{m+1}>K_m\). Since \(2\sqrt r/(1+r)<1\) and \(1-r^{2m}<1\), each \(K_m<1\). Choosing \(r\) close to \(1\) and then increasing \(m\) proves \(K_m\nearrow1\).

**5. Sharp boundary asymptotics.** Introduce \(a_m=-m\log r_m>0\). The stationary equation becomes
\[
 e^{2a_m}-1=4m\coth\frac{a_m}{2m},
 \qquad
 K_m=(1-e^{-2a_m})\operatorname{sech}\frac{a_m}{2m}.
\]
Since \(K_m\to1\), both factors on the right converge to \(1\). Hence \(a_m\to\infty\) and \(a_m/m\to0\). Expanding the hyperbolic cotangent in the stationary equation first gives
\[
 e^{2a_m}=\frac{8m^2}{a_m}(1+o(1)).
\]
Taking logarithms shows \(a_m=O(\log m)\) and then \(a_m/\log m\to1\). Substitution back yields the sharper asymptotic
\[
 a_m=\log m-\tfrac12\log\log m+\tfrac12\log8+o(1).
\]
Finally, the elementary expansions of \(e^{-2a_m}\) and \(\operatorname{sech}(a_m/(2m))\) give
\[
 8m^2(1-K_m)=a_m^2+a_m+o(1).
\]
Using the previous estimate of \(a_m\) proves the displayed three-term expansion, and division by \((\log m)^2\) proves the exact limiting coefficient \(1/8\). All limits are along positive integers.

## Verification
The standalone script `check_halfline.py` checks the one-site identity symbolically, solves the strictly monotone stationary equation numerically for ten sites, compares the analytic constants with direct norms of truncated exact extremizers, tests randomly sampled finite sequences, and displays normalized large-site deficits. It reports **1007 successful checks**. The script uses NumPy, SciPy, and SymPy. Its finite tests corroborate but do not prove the universal inequality, uniqueness, or infinite-site asymptotic, which follow from the arguments above.

Representative sharp values are \(K_1=0.769800358920\), \(K_2=0.887489786756\), \(K_3=0.930687820886\), and \(K_{20}=0.995289781909\). Truncated extremizers are used only to test numerically convergent infinite-series formulas, with no assertion that finite truncation is a proof.

## Relationship to prior work
Ilyin, Laptev, and Zelik [1] give the sharp constant \(1\) for point evaluation on the **whole** lattice \(\mathbb Z\), with no nonzero extremizer, and establish the general Green-function variational technique. This broader technique is acknowledged as prior, not rebranded as a new principle. Liao [2] develops discrete Hardy-summation inequalities with different single-norm formulations; it does not give the two-norm Dirichlet point-evaluation profile. Krejčiřík, Laptev, and Štampach [3] provide the half-line Dirichlet/Robin Jacobi resolvent kernel as part of spectral and Hardy-weight results; their kernel is a direct antecedent of Step 2, so the Green kernel itself is **not** a novelty claim. Neither inspected treatment states or derives the unique all-site sharp multiplicative constants together with the non-power \((\log m)^2/m^2\) boundary deficit and its three-term expansion. The contribution is the complete **boundary-layer optimization and asymptotic law**, not the existence of a resolvent formula.

## Limitations
The result concerns a one-dimensional, homogeneous nearest-neighbor **Dirichlet** difference energy and real square-summable sequences. No assertion is made for variable lattice spacing, general graph Laplacians, other boundary conditions, or nonquadratic energies. The formula for each sharp constant is given by a unique algebraic root rather than radicals at general \(m\). Numerical testing neither certifies novel priority nor replaces the infinite-dimensional proof; a historically unindexed equivalent boundary-interpolation result remains possible.

## References
[1] A. Ilyin, A. Laptev, and S. Zelik, “Sharp interpolation inequalities for discrete operators and applications,” arXiv:1407.0675 (first public 2014-07-02); *Bulletin of Mathematical Sciences* 5 (2015), 19–57, doi:10.1007/s13373-014-0060-8.

[2] Z.-W. Liao, “Discrete Hardy-type Inequalities,” arXiv:1406.1984 (first public 2014-06-08).

[3] D. Krejčiřík, A. Laptev, and F. Štampach, “Spectral enclosures and stability for non-self-adjoint discrete Schrödinger operators on the half-line,” arXiv:2111.08265 (2021); *Bulletin of the London Mathematical Society* 54 (2022), 2379–2403, doi:10.1112/blms.12700.
