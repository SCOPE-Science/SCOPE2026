# Sharp mean-zero Sobolev interpolation on finite star graphs

## Finding
For each integer \(n\ge2\), let \(S_n=K_{1,n}\) be the unweighted star with center \(o\) and leaves \(v_1,\ldots,v_n\). Every real- or complex-valued vertex function satisfying \(\sum_v f(v)=0\) obeys the **sharp** multiplicative inequality
\[
\|f\|_\infty^2\le C_n\Bigl(\sum_v|f(v)|^2\Bigr)^{1/2}\Bigl(\sum_{i=1}^n|f(v_i)-f(o)|^2\Bigr)^{1/2}.
\]
Put
\[
M_n(c)=\frac{nc^2+2c+n}{n-1},\qquad E_n(c)=\frac{(n^2+n-1)c^2+2c+n}{n-1},
\]
and
\[
p_n(c)=2n(n^2+n-1)c^3+3(n^2+2n-1)c^2+(n^3+2n^2-n+4)c+2n.
\]
The polynomial \(p_n\) has exactly one real zero \(c_n\), which lies in \((-1/n,0)\). The **exact** optimum is
\[
\boxed{C_n=\bigl(M_n(c_n)E_n(c_n)\bigr)^{-1/2}.}
\]
Every nonzero equality case is a scalar multiple of the following configuration after relabelling the leaves: one leaf has value \(1\), every other leaf has value \(-(1+c_n)/(n-1)\), and the center has value \(c_n\). The constant satisfies \(0<C_n<1\), and its high-valence expansion is
\[
C_n=1-\frac1n+\frac{2}{n^3}+O(n^{-4}).
\]
In particular, \(C_2=0.5849284893761858\ldots\).

## Assumptions and scope
The vertex-counting \(\ell^2\) norm and unit-conductance, unoriented graph energy are **not normalized by vertex or edge count**. The mean is the unweighted arithmetic mean over all \(n+1\) vertices. The result holds for all integers \(n\ge2\), both real and complex scalar fields, with no positivity hypothesis. The zero function gives equality trivially. No claim is made for arbitrary non-star graphs, weighted stars, or other interpolation exponents.

## Proof
Write \(M(f)=\sum_v|f(v)|^2\) and \(E(f)=\sum_i|f(v_i)-f(o)|^2\). Since the graph is connected and \(\sum_v f(v)=0\), both are positive for each nonzero \(f\).

**Reduction for a leaf.** Fix a leaf \(v_1\) with \(f(v_1)\ne0\), rescale by its complex value so that \(f(v_1)=1\), and write \(c=f(o)\). The other \(n-1\) leaf values have prescribed average \(b=-(1+c)/(n-1)\). The equality identities
\[
\sum_{i=2}^n|f(v_i)|^2=(n-1)|b|^2+\sum_{i=2}^n|f(v_i)-b|^2,
\]
\[
\sum_{i=2}^n|f(v_i)-c|^2=(n-1)|b-c|^2+\sum_{i=2}^n|f(v_i)-b|^2
\]
show that replacing these values by \(b\) decreases both nonnegative quadratic quantities, strictly unless they were already equal. For \(c=u+iv\), the remaining mass and energy are
\[
M_n(u)+\frac{n}{n-1}v^2,\qquad
E_n(u)+\frac{n^2+n-1}{n-1}v^2,
\]
so a minimizing \(c\) is real. Consequently the optimal pointwise coefficient at any leaf is \(\max_{c\in\mathbb R}[M_n(c)E_n(c)]^{-1/2}\).

**Existence and uniqueness of the scalar optimum.** Both quadratics are strictly positive and have positive leading coefficient; their product tends to infinity with \(|c|\). Direct differentiation gives
\[
\frac{d}{dc}\bigl(M_n(c)E_n(c)\bigr)=\frac{2p_n(c)}{(n-1)^2}.
\]
The discriminant of \(p_n\) as a cubic in \(c\) is
\[
-(n-1)^3(n+1)^3 R(n),\qquad
R(n)=8n^6+56n^5+127n^4-32n^3-167n^2+80n+144.
\]
Writing \(m=n-2\ge0\) gives the manifestly positive expression
\[
R(n)=8m^6+152m^5+1167m^4+4504m^3+9089m^2+9108m+3716>0.
\]
Thus \(p_n\) has exactly one distinct real zero. Because
\[
p_n(-1/n)=-\frac{(n-1)^2(n+1)^2}{n^2}<0,\qquad p_n(0)=2n>0,
\]
its zero \(c_n\) belongs to \((-1/n,0)\). The derivative changes sign from negative to positive there, so \(c_n\) is the **unique global minimizer**.

**The center never determines the sharp constant.** If the center value is \(1\), the mean-zero constraint makes the average leaf value \(-1/n\). Averaging the leaves decreases both \(M\) and \(E\), giving sharp center evaluation coefficient \(n/(n+1)^{3/2}\). But the mean-zero test configuration with one leaf \(1\) and all other vertices \(-1/n\) gives leaf coefficient \((n/(n+1))^{3/2}\), which is \(\sqrt n\) times the center coefficient and strictly larger for \(n\ge2\). Therefore the global \(\ell^\infty\) coefficient is the leaf optimum above. Strict equality in the averaging identities and uniqueness of \(c_n\) classify all nonzero extremizers. Since \(-1/n<c_n<0\), all other leaf and center magnitudes are strictly below \(1\); the singled-out leaf is indeed the maximizing vertex.

**Strict bound and asymptotics.** For a normalized leaf, \(M_n(c)\ge(n+1)/n>1\), and \(E_n(c)\) has minimum \([n-(n^2+n-1)^{-1}]/(n-1)>1\). This proves \(C_n<1\). Set \(h=1/n\) in \(p_n(c_n)=0\), multiply by \(h^3\), and solve the analytic small-\(h\) root with limit zero: the derivative with respect to \(c\) at \((h,c)=(0,0)\) is \(1\), permitting the analytic implicit-function theorem. Coefficient matching yields
\[
c_n=-2h^2+4h^3-10h^4+O(h^5).
\]
Substituting into \(M_nE_n\) gives \(M_n(c_n)E_n(c_n)=1+2h+3h^2+O(h^4)\). Its inverse square root is \(1-h+2h^3+O(h^4)\), as claimed.

## Verification
The standalone `check_star.py` uses high-precision decimal root bracketing, verifies the explicit equality witnesses for \(2\le n\le50\), checks the center/leaf strict gap, and checks 150 reproducible random mean-zero real input vectors for each dimension. Direct, separate floating-point optimization of the unrestricted finite-dimensional quotient for \(n=2,3,4,7,15\) agreed with the polynomial formula to numerical precision. These finite computations confirm implementation and examples; the proof for every integer \(n\ge2\) is the exact averaging/discriminant/asymptotic argument above.

## Relationship to prior work
Ilyin–Laptev–Zelik (2014, originally public on 2 July 2014) develop sharp discrete pointwise interpolation via Green functions on the infinite lattices \(\mathbb Z^d\), especially \(d=1,2,3\). Ilyin–Zelik (2013) establish a general resolvent approach for Sobolev interpolation on Riemannian manifolds. Their general variational methodology motivates asking for an **explicit branching-graph constant**, but the examined text does not evaluate the star family, its cubic equality profile, or the cancellation of its second-order asymptotic coefficient. General existence/optimization procedures should not be mistaken for evaluation of this exact family. Public research-index comparisons found related half-line boundary and lattice embedding constants, not this mean-zero finite-star product inequality. The absence of an indexed match is not a proof that an equivalent unindexed result does not exist.

## Limitations
The finite-star family is one canonical graph geometry, not a universal graph theorem. The result depends on the specified unnormalized energy and counting mass. Only the exponent \(1/2\)–\(1/2\) product is treated. A potentially unindexed exact finite-star result is the residual originality risk; the general Green-function literature may provide another derivation but not the displayed closed classification in the material examined. The numeric script is a finite check, not an exhaustive verification of the infinite-dimensional-parameter statement.

## References
1. A. Ilyin, A. Laptev, S. Zelik, *Sharp interpolation inequalities for discrete operators and applications*, arXiv:1407.0675v1 (first public 2014-07-02), https://arxiv.org/abs/1407.0675, esp. §§1–2 and Theorem 2.2.
2. A. A. Ilyin, S. V. Zelik, *Green's function asymptotics and sharp point-wise interpolation inequalities*, arXiv:1303.0957v1 (first public 2013-03-05), https://arxiv.org/abs/1303.0957, esp. §2 and formula (1.4).
