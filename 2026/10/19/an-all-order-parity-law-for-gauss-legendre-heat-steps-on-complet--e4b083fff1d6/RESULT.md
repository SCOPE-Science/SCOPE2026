# An all-order parity law for Gauss–Legendre heat steps on complete multipartite graphs

## Finding

For every integer \(s\ge1\), let \(R_s\) be the stability function of the classical \(s\)-stage Gauss–Legendre Runge–Kutta method. For an unweighted connected complete multipartite graph \(G=K_{n_1,\ldots,n_k}\), with \(k\ge2\), all \(n_i\ge1\), and \(n=\sum_i n_i\ge2\), write \(L_G\) for the combinatorial Laplacian. The completed heat step is \(T_{s,G}(h)=R_s(-hL_G)\), for real \(h>0\).

**All-stage parity theorem.** If \(s\) is even, \(T_{s,G}(h)\) is strictly entrywise positive, symmetric positive definite, and doubly stochastic for every \(h>0\), regardless of the part sizes. If \(s\) is odd and \(n\ge3\), then \(T_{s,G}(h)\) has negative diagonal entries for all sufficiently large \(h\), so unconditional positivity fails. For the exceptional graph on two vertices, the step is strictly positive for every finite \(h>0\) for either parity.

The key all-stage scalar result, independently meaningful for Padé approximants, is that
\[
\Phi_s(x)=\frac{1-R_s(-x)}{x}
\]
is **strictly decreasing** for \(x>0\), for every integer \(s\ge1\). For even \(s\), also \(0<R_s(-x)<1\) for all \(x>0\). The graph positivity theorem follows by applying these two inequalities to the exact complete-multipartite spectral projectors.

Unconditional positivity does not extend from complete multipartite graphs to every connected bipartite graph. On the four-vertex path \(P_4\), for every even \(s\ge2\), the endpoint-neighbor entry has the large-step expansion
\[
(T_{s,P_4}(h))_{1,2}=-\frac{s(s+1)}{4h}+O_s(h^{-2}),
\qquad h\longrightarrow\infty,
\]
and is consequently negative for sufficiently large \(h\). Vertices of \(P_4\) are indexed here by \(1,2,3,4\).

## Assumptions and scope

The graph is finite, connected, simple, undirected, and has unit conductance on every edge between distinct parts, with no intra-part edges. Its Laplacian \(L_G\) uses diagonal degrees and off-diagonal values \(-1\) on edges. Time \(h\) and the stage count \(s\) are unrestricted within the stated ranges. The theorem concerns the **completed** linear Runge–Kutta step for \(u'=-L_Gu\), not its intermediate stage vectors. Weighted, normalized, directed, and arbitrary graph Laplacians are not covered by the positive assertion.

## Proof

**1. Stability polynomial and scalar monotonicity.** The Gauss–Legendre stability function is the diagonal Padé approximant to the exponential:
\[
R_s(-x)=\frac{Q_s(-x)}{Q_s(x)},\qquad
Q_s(x)=\sum_{j=0}^{s} a_{s,j}x^j,\qquad
a_{s,j}=\frac{s!(2s-j)!}{(2s)!(s-j)!j!}>0.
\]
Write \(Q_s(x)=E_s(x^2)+xO_s(x^2)\), where \(E_s(z)=\sum_{i\ge0}e_i z^i\), \(O_s(z)=\sum_{i\ge0}o_i z^i\), \(e_i=a_{s,2i}\), and \(o_i=a_{s,2i+1}\) when those indices exist, with missing coefficients zero. In particular \(O_s(z)>0\) for \(z\ge0\). Direct subtraction gives
\[
\Phi_s(x)=\frac{2O_s(x^2)}{Q_s(x)}
=\frac{2}{x+E_s(x^2)/O_s(x^2)}.
\]
For every index \(i\) with \(o_i>0\),
\[
\frac{e_i}{o_i}=
(2i+1)\frac{2s-2i}{s-2i}
=(2i+1)\left(1+\frac{s}{s-2i}\right).
\]
These ratios strictly increase with \(i\). If \(s\) is even, the highest nonzero even coefficient has no matching odd coefficient; treating its ratio as \(+\infty\) preserves the ordering. Therefore whenever \(i>j\), \(e_i o_j-e_j o_i\ge0\), including zero-padded indices. The identity
\[
E_s'(z)O_s(z)-E_s(z)O_s'(z)
=\sum_{i>j}(i-j)(e_i o_j-e_j o_i)z^{i+j-1}\ge0
\]
shows that \(E_s(z)/O_s(z)\) is nondecreasing for \(z\ge0\). Hence the positive denominator \(x+E_s(x^2)/O_s(x^2)\) strictly increases on \(x>0\). Thus \(\Phi_s(x)\) strictly decreases for *every* \(s\ge1\).

For even \(s\), an integral identity supplies strict positivity:
\[
Q_s(-x)=\frac{1}{(2s)!}\int_0^\infty e^{-t}t^s(t-x)^s\,dt>0
\qquad(x\ge0).
\]
Indeed, expand the binomial and integrate its factorial moments to recover each coefficient of \(Q_s(-x)\); the integrand is nonnegative and nonzero on a set of positive measure when \(s\) is even. Since \(Q_s(x)>Q_s(-x)>0\) for \(x>0\) (the difference is \(2xO_s(x^2)>0\)), one has \(0<R_s(-x)<1\). For any \(s\), positivity of \(E_s(x^2)\) and \(xO_s(x^2)\) also implies \(-1<R_s(-x)<1\).

**2. Complete-multipartite spectral projectors.** Put \(F_s(x)=1-R_s(-x)=x\Phi_s(x)\). The Laplacian eigenvalues are \(0\) on constants, \(n\) on partwise constants with total sum zero, and \(n-r\) on contrasts within any part of size \(r\ge2\). For vertices \(i\ne j\) in *different* parts,
\[
(T_{s,G}(h))_{ij}=\frac{F_s(nh)}{n}>0.
\]
For \(i\ne j\) in the *same* part of size \(r\ge2\), spectral projector multiplication gives
\[
(T_{s,G}(h))_{ij}
=\frac{F_s((n-r)h)-\frac{n-r}{n}F_s(nh)}{r}
=\frac{(n-r)h}{r}\bigl[\Phi_s((n-r)h)-\Phi_s(nh)\bigr]>0.
\]
Here \(0<n-r<n\) since the graph has at least two nonempty parts, and strict monotonicity of \(\Phi_s\) was proved in step 1. For even \(s\), the multiplier \(R_s(-h\lambda)\) is strictly positive at every nonnegative Laplacian eigenvalue \(\lambda\), so the symmetric matrix \(T_{s,G}(h)\) is positive definite and each diagonal entry is strictly positive. Since \(L_G\mathbf 1=0\) and \(R_s(0)=1\), every row sums to one; symmetry yields the same for columns. This proves the even-stage assertion.

**3. Odd stages and the two-vertex exception.** For odd \(s\), the highest-degree terms in \(Q_s(-x)/Q_s(x)\) give \(\lim_{x\to\infty}R_s(-x)=-1\). Every connected \(n\)-vertex graph has a simple zero Laplacian eigenvalue with projector \(J/n\), and all other eigenvalues are positive. Thus, for any connected graph (not just complete multipartite),
\[
\lim_{h\to\infty}R_s(-hL_G)=\frac{2J}{n}-I.
\]
If \(n\ge3\), its diagonal entries are \(2/n-1<0\), proving eventual failure of positivity. For \(n=2\) the step has entries \((1+R_s(-2h))/2\) and \((1-R_s(-2h))/2\), both strictly positive by the scalar bound \(-1<R_s(-x)<1\).

**4. Large-step obstruction on the path \(P_4\).** For even \(s\), the two leading polynomial coefficients satisfy \(a_{s,s-1}/a_{s,s}=s(s+1)\). Consequently
\[
R_s(-x)=1-\frac{2s(s+1)}{x}+O_s(x^{-2}),\qquad x\to\infty.
\]
Functional calculus on a fixed connected graph gives
\[
R_s(-hL_G)=I-\frac{2s(s+1)}{h}L_G^\dagger+O_s(h^{-2}),
\]
where \(L_G^\dagger\) is its Moore–Penrose inverse and the error is entrywise. On the unit path \(P_4\), direct multiplication verifies
\[
L_{P_4}^\dagger=\frac18
\begin{pmatrix}
7&1&-3&-5\\
1&3&-1&-3\\
-3&-1&3&1\\
-5&-3&1&7
\end{pmatrix}.
\]
Its \((1,2)\) entry equals \(1/8\), yielding the stated negative asymptotic and completing the proof.

## Verification

The standalone `verify.py` program uses exact fractions. It independently reconstructs Padé coefficients and checks coefficient-order inequalities for stages \(1\) through \(35\), inverts the full rational matrices on nine complete-multipartite graph families for stages \(2,4,6,8\) at four positive timesteps, compares each off-diagonal with the claimed spectral projector formula, and checks positivity and stochasticity. It also calculates large-step negative entries for odd stages on \(K_3\) and even stages on \(P_4\). The observed output is:

`VERIFY_OK coefficient_pairs=1938 positive_entries=4656 projector_comparisons=3904 odd_diagonal_witnesses=12 path_witnesses=4`

These are finite exact checks, not a replacement for the preceding all-stage mathematical argument.

## Relationship to prior work

The Padé representation of Gauss–Legendre Runge–Kutta methods and the use of absolute-monotonicity radii as general positivity criteria are classical. Horváth establishes positivity-radius and order-barrier results for broad classes of positive ordinary differential equations, while Lóczi and Ketcheson analyze rational-function absolute monotonicity in detail. Fekete, Ketcheson, and Lóczi analyze positivity for explicit Runge–Kutta methods and selected spatial discretizations. Their inspected results do not give the all-stage scalar deficit-monotonicity inequality or the even–odd complete-multipartite conclusion proved here.

A previously established general criterion for matrix-function positivity on unweighted complete multipartite graphs supplies the natural spectral context. The projector reduction itself is not asserted as novel. The contribution here is the uniform-in-stage Padé coefficient-ratio proof, its even/odd dichotomy, and the graph-specific positive and negative consequences. The familiar two-stage Padé instance is subsumed rather than claimed independently. This is not an assertion of definitive historical priority.

## Limitations

Only the completed step is nonnegative; no claim concerns internal stage nonnegativity, arbitrary spatial meshes, weighted graphs, time-dependent or nonlinear problems, or a universal SSP radius. The path \(P_4\) demonstrates that the positive graph class cannot be replaced by all connected bipartite graphs. The asymptotic obstruction specifies negative entries eventually but not their first zero. Related Padé or graph-functional-calculus literature may contain equivalent statements not located in the checked sources.

## References

1. Z. Horváth, *Positivity of Runge-Kutta and diagonally split Runge-Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326. DOI: `10.1016/S0168-9274(98)00050-6`.
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (first posted 2013-03-26), later LMS Journal of Computation and Mathematics 17 (2014), 159–205. `https://arxiv.org/abs/1303.6651`.
3. I. Fekete, D. I. Ketcheson, and L. Lóczi, *Positivity for convective semi-discretizations*, arXiv:1610.00228v1 (first posted 2016-10-02). `https://arxiv.org/abs/1610.00228`.
