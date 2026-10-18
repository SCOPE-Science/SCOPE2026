# Sharp two-thirds anisotropy in resistance-optimal rectangular tori

## Finding

Let \(m,n\ge3\) be integers, and form the undirected Cartesian-product graph \(G_{m,n}=C_m\square C_n\). Assign independently chosen nonnegative conductances \(w_e\) to its \(2mn\) edges under \(\sum_e w_e=B>0\). For connected conductance support minimize \(\mathcal T(w)=\operatorname{tr}L(w)^+\), where \(L(w)^+\) is the Moore–Penrose pseudoinverse; assign infinite cost to disconnected support. This is equivalently total pairwise effective resistance divided by \(mn\), or twice the sum of steady-state mean-zero variances of unit-noise diffusion.

**Exact finite-network optimum.** There is a *unique* global optimum even among all independently adjustable, nonsymmetric edge conductances. Every edge in the \(C_m\) direction has a common positive weight \(x\), and every edge in the \(C_n\) direction has a common positive weight \(y\). Put
\[
 a_k=4\sin^2(\pi k/m),\quad b_\ell=4\sin^2(\pi\ell/n),\quad h=B/(mn),
\]
and let \(\sum'\) exclude only \((k,\ell)=(0,0)\). The scalar equation
\[
 \Phi_{m,n}(\tau):=\sum_{k=0}^{m-1}\sum_{\ell=0}^{n-1}{}'
 \frac{a_k-b_\ell}{(a_k+\tau b_\ell)^2}=0
\]
has exactly one root \(\tau_{m,n}\in(0,\infty)\), and the unrestricted global optimum is
\[
 x_* =\frac{h}{1+\tau_{m,n}},\qquad
 y_* =\frac{h\tau_{m,n}}{1+\tau_{m,n}},\qquad
 \mathcal T_* =\frac{1+\tau_{m,n}}{h}\sum'\frac1{a_k+\tau_{m,n}b_\ell}.
\]
For \(m=n\), one has exactly \(\tau_{m,n}=1\).

**Sharp fixed-width long-torus law.** For every *fixed* integer \(n\ge3\), set
\[
 S_n=\sum_{\ell=1}^{n-1}\frac1{2\sin(\pi\ell/n)},\qquad
 z_n=(3S_n)^{2/3}.
\]
Then, as the integer \(m\to\infty\),
\[
 \boxed{\tau_{m,n}=z_n m^{-2/3}(1+o(1))},
 \qquad
 \boxed{\mathcal T_* =\frac{mn}{B}\left[\frac{m^2}{12}+\frac{z_n}{4}m^{4/3}+o(m^{4/3})\right]}.
\]
In particular the narrow-direction budget fraction is asymptotically \(z_nm^{-2/3}\), yet remains strictly positive for every finite \(m\). If \(\mathcal T_{\rm equal}\) denotes the trace obtained by assigning \(B/(2mn)\) to *every* edge, then
\[
 \boxed{\lim_{m\to\infty}\frac{\mathcal T_*}{\mathcal T_{\rm equal}}=\frac12}
 \qquad (n\text{ fixed}).
\]
No asymptotic assertion is made when \(n\) grows with \(m\).

## Assumptions and scope

The graph is finite and simple, with both cycle lengths at least three. The two orientation classes each contain exactly \(mn\) undirected edges. All edges have identical cost per unit conductance; an optimizer may assign zero to edges in the feasible set, but zero-weight support that disconnects the graph is excluded by the infinite-cost convention. The measure \(\mathcal T\) is based on the combinatorial weighted Laplacian, not the normalized Laplacian. The asymptotic fixes the short circumference \(n\) and lets only \(m\) increase; \(B\) may vary with \(m\), since the formula explicitly factors out its homogeneous scaling.

## Proof

**1. Unrestricted optimum and strict symmetry.** Write \(N=mn\), \(J=\mathbf1\mathbf1^\top/N\), and \(X(w)=L(w)+J\). For connected support, \(X(w)\succ0\) and \(\mathcal T(w)=\operatorname{tr}X(w)^{-1}-1\). Along any nonzero edge-conductance variation \(v\), the symmetric matrix \(H=\sum_e v_e(\mathbf e_i-\mathbf e_j)(\mathbf e_i-\mathbf e_j)^\top\) is nonzero: its off-diagonal entry on any simple-graph edge equals \(-v_e\). The second directional derivative is
\[
 \frac{d^2}{ds^2}\operatorname{tr}(X+sH)^{-1}\bigg|_{s=0}
 =2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0,
\]
because this trace is that of \(X^{-1/2}(X^{-1/2}HX^{-1/2})^2X^{-1/2}\). Hence the objective is strictly convex on the set of connected-support conductances. A finite minimizer exists: the budget simplex is compact, the positive-weight uniform point is feasible, and the objective tends to infinity as the spectral gap vanishes on approaching disconnected support. Every graph translation and coordinate reflection preserves the budget and objective. Averaging an optimum over these automorphisms, or using strict uniqueness directly, gives equal conductances within each orientation. Neither common weight can vanish, because removing a whole orientation disconnects \(G_{m,n}\). Thus the unrestricted optimum has \(x,y>0\) and \(x+y=h\), and it is unique.

**2. Exact scalar equation.** Fourier diagonalization of the two cycle Laplacians gives the nonzero weighted eigenvalues \(xa_k+yb_\ell\). With \(\tau=y/x\), the constraint gives \(x=h/(1+\tau)\), and therefore
\[
 \mathcal T(\tau)=\frac{1+\tau}{h}\sum'\frac1{a_k+\tau b_\ell},\qquad
 h\mathcal T'(\tau)=\Phi_{m,n}(\tau).
\]
The derivative is negative for sufficiently small \(\tau>0\), because the terms with \(k=0,\ell>0\) diverge negatively as \(-\tau^{-2}\sum_{\ell>0}b_\ell^{-1}\). It is positive for sufficiently large \(\tau\), because the terms \(\ell=0,k>0\) contribute the fixed positive sum \(\sum_{k>0}a_k^{-1}\), whereas all terms with \(\ell>0\) decay to zero. Strict convexity in \(y/h\in(0,1)\) implies exactly one stationary point. Its unique positive ratio is \(\tau_{m,n}\), proving the finite-network formula. Coordinate exchange gives \(\tau_{m,m}=1\).

**3. Periodic Green kernel.** For any \(c>0\), define
\[
 G_m(c)=\sum_{k=0}^{m-1}\frac1{a_k+c},\quad
 \theta(c)=2\operatorname{arsinh}(\sqrt c/2).
\]
The exact finite-cycle resolvent identity is
\[
 G_m(c)=\frac{m}{\sqrt{c(c+4)}}\coth\!\left(\frac{m\theta(c)}2\right).
\]
Indeed, the infinite-line inverse kernel for \(cI+L_{\mathbb Z}\) is \(e^{-\theta(c)|r|}/\sqrt{c(c+4)}\); its sum over the periodized indices \(r=qm\) is the diagonal of the cyclic inverse. Multiplying this diagonal by \(m\) gives the eigenvalue sum. This proves the identity without invoking an unverified asymptotic integral. Differentiation also yields \(-G_m'(c)=\sum_k(a_k+c)^{-2}\).

**4. Singular fixed-width balance.** The exact cycle identity \(\sum_{k=1}^{m-1}a_k^{-1}=(m^2-1)/12\) follows, for example, by comparing the coefficient of \(c\) in the cycle characteristic polynomial or by the standard cosecant-square identity. Splitting the derivative by the transverse Fourier index gives
\[
 \Phi_{m,n}(\tau)=\frac{m^2-1}{12}
 +\sum_{\ell=1}^{n-1}\bigl[G_m(\tau b_\ell)
 +(1+\tau)b_\ell G_m'(\tau b_\ell)\bigr].
\]
For any fixed \(z>0\), set \(\tau=z m^{-2/3}\). As \(m\to\infty\), every \(c=\tau b_\ell\) tends to zero but \(m\sqrt c\to\infty\). Uniformly over the finitely many \(1\le\ell<n\), the exact resolvent formula and its derivative give
\[
 G_m(c)=\frac{m}{2\sqrt c}(1+o(1)),\qquad
 -G_m'(c)=\frac{m}{4c^{3/2}}(1+o(1)).
\]
Consequently,
\[
 \frac{\Phi_{m,n}(zm^{-2/3})}{m^2}
 \longrightarrow \frac1{12}-\frac{S_n}{4z^{3/2}}.
\]
This limit is strictly negative below \(z_n=(3S_n)^{2/3}\) and strictly positive above it. Since the finite scalar objective has exactly one stationary point, bracketing its root by \((z_n\pm\varepsilon)m^{-2/3}\) for each \(0<\varepsilon<z_n\) gives \(m^{2/3}\tau_{m,n}\to z_n\).

**5. Sharp cost and uniform-design comparison.** Separating the transverse zero mode gives
\[
 h\mathcal T_*= (1+\tau_{m,n})\left[\frac{m^2-1}{12}
 +\sum_{\ell=1}^{n-1}G_m(\tau_{m,n}b_\ell)\right].
\]
Using \(\tau_{m,n}=z_nm^{-2/3}(1+o(1))\) and the Green asymptotics gives
\[
 h\mathcal T_* = \frac{m^2}{12}
 +m^{4/3}\left(\frac{z_n}{12}+\frac{S_n}{2\sqrt{z_n}}\right)
 +o(m^{4/3})
 =\frac{m^2}{12}+\frac{z_n}{4}m^{4/3}+o(m^{4/3}),
\]
using \(z_n^{3/2}=3S_n\). At equal orientation weights \(x=y=h/2\), the same exact decomposition gives \(h\mathcal T_{\rm equal}=2[(m^2-1)/12+\sum_{\ell>0}G_m(b_\ell)]=m^2/6+O_n(m)\). The ratio therefore tends to \(1/2\). All assertions follow.

## Verification

The included `verify.py` independently assembles the full Laplacian for small rectangular tori, compares its eigenspectrum and pseudoinverse trace with the Fourier formula, solves the scalar root, tests independent asymmetric feasible competitors, checks the exact periodic Green identity, and tests finite-size approach to both limiting constants. Execution completed with **1,296 passing assertions**. These finite checks are supplementary; the unrestricted and asymptotic conclusions follow from the proof above. Requires Python 3, NumPy, and SciPy; run `python verify.py` from the extracted directory.

## Relationship to prior work

Ghosh, Boyd, and Saberi (2006 conference paper; 2008 extended article) established the general convex all-pairs resistance design problem, strict uniqueness, and symmetry reductions, as well as examples on wheels, barbell graphs, trees, and numerically designed meshes. Those general optimization principles are used here; the new assertion is the exact two-orientation torus equation **together with its sharp fixed-width fractional-power allocation and two-term optimum**. The examined full conference and extended papers do not give this long-period/tiny-transverse-coupling theorem.

Bamieh, Jovanović, Mitra, and Patterson (2011 arXiv) studied Fourier-mode coherence scaling on regular discrete tori under local-feedback assumptions and bounded control effort. Their fixed-feedback Fourier analysis motivates this problem but does not optimize independent edge conductances under a total budget or derive the \(m^{-2/3}\) allocation law.

Tovar and collaborators (2026 arXiv) consider resistance-optimal networks under linear and nonlinear conductance costs and formulate general marginal optimality conditions. Their examined paper does not treat two-orientation rectangular tori or the singular finite-width exponent. The present theorem is not asserted to establish novel *general-purpose* convexity; its substantive content is the explicit family-dependent singular optimization and constant. It remains possible that an unindexed or differently formulated source contains the same specialization.

## Limitations

The graph model requires two cyclic factors of lengths at least three and uniform linear edge prices. The asymptotic is only in the long circumference at **fixed** short circumference; it neither addresses two jointly diverging circumferences nor nonperiodic boundaries. The implicit finite optimizer generally requires one-dimensional numerical root solving, and this theorem does not assert a radical closed form for arbitrary \(m,n\). Literature indexing is incomplete; an equivalent specialization in an unindexed paper cannot be excluded. The mathematical proof is not a formal computer-verified theorem.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, 24–28 July 2006, pp. 1185–1196. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf . Extended version: *SIAM Review* **50** (2008), 37–66, https://doi.org/10.1137/050645452 .
2. B. Bamieh, M. R. Jovanović, P. Mitra, S. Patterson, *Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback*, arXiv:1112.4011v1 (public 17 December 2011), https://arxiv.org/abs/1112.4011 .
3. H. Tovar, G. Vázquez-Victorio, E. Hernández-Lemus, A. Cervera, D. Pérez-Calixto, *Cost convexity controls the architecture of resistance-optimal networks*, arXiv:2610.03627v1 (public 2 October 2026), https://arxiv.org/abs/2610.03627 .
