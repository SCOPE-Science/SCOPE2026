# Sharp high-order Birkhoff–Takahashi envelope for Radon planes

## Finding

**Theorem (sharp Radon-plane power-mean profile, all orders at least one).** Let \(X\) be a two-dimensional real Radon normed plane (Birkhoff–James orthogonality is symmetric), and let \(1\le t<\infty\). For \(a,b>0\) let
\[
 M_t(a,b)=\left(\frac{a^t+b^t}{2}\right)^{1/t}.
\]
Define the Birkhoff-restricted profile and constant
\[
 J^B_{X,t}(\tau)=\sup_{\substack{x,y\in S_X\\x\perp_B y}}M_t(\|x+\tau y\|,\|x-\tau y\|),
 \quad C^B_t(X)=\sup_{0\le\tau\le1}\frac{J^B_{X,t}(\tau)^2}{1+\tau^2}.
\]
For every \(0\le\tau\le1\), the **sharp universal Radon-plane profile** is
\[
 J^B_{X,t}(\tau)\le M_t(1,1+\tau),
\]
and the affine-regular hexagonal plane attains equality **at every** \(\tau\).

Precisely, let \(\tau_t\in[1/2,1)\) be the unique solution of
\[
 \tau_t=(1-\tau_t)(1+\tau_t)^{t-1}.
\]
Then
\[
 \boxed{C^B_t(X)\le \mathcal B(t):=
 \frac{\bigl([1+(1+\tau_t)^t]/2\bigr)^{2/t}}{1+\tau_t^2}.}
\]
Equality holds if and only if the unit circle of \(X\) is an affine-regular hexagon. In particular,
\[
 \mathcal B(1)=\frac54,\qquad
 \tau_2=\frac{\sqrt5-1}{2},\qquad
 \mathcal B(2)=\frac{3+\sqrt5}{4}.
\]
The sharp envelope \(\mathcal B(t)\) and its unique maximizing scale \(\tau_t\) increase strictly with \(t\) on \([1,\infty)\); as \(t\to\infty\),
\[
 1-\tau_t\sim2^{1-t},\qquad
 \lim_{t\to\infty} t\,[2-\mathcal B(t)]=4\log2.
\]
For the same affine-regular hexagonal plane \(G\), the *direct isosceles-orthogonal* constant \(C^I_t(G)\) from Li–Zhang–Qi–Liu equals \(5/4\) at every finite order \(t\). Consequently \(C^B_t(G)>C^I_t(G)\) for every \(t>1\): these two natural orthogonality restrictions diverge immediately above the arithmetic-mean order.

## Assumptions and scope

A real normed plane is Radon if \(x\perp_B y\Rightarrow y\perp_B x\), where \(x\perp_B y\) means \(\|x+\lambda y\|\ge\|x\|\) for every \(\lambda\in\mathbb R\). All pairs in the displayed suprema are **ordered**, have unit norm, and satisfy this orthogonality condition; the deformation parameter lies in the closed interval \([0,1]\). The power-mean order is finite and \(t\ge1\), with no claim about infinite or smaller orders beyond previously published results. Two-dimensionality and real scalars are essential to the cited sharp Radon-plane geometric input.

We use the established geometric fact (Qi–Yin–Liu, 2026, their equation (23) and Theorem 16, citing the Birkhoff arithmetic triangle literature) that, for every real Radon plane,
\[
 A^B_2(X):=\sup_{\substack{x,y\in S_X\\x\perp_B y}}
 \frac{\|x+y\|+\|x-y\|}{2}\le\frac32,
\]
with equality if and only if \(X\)'s unit circle is an affine-regular hexagon. This established theorem is an **external premise**, not proved afresh here; the new argument independently derives the high-order profile and its sharp optimization conditional on that published geometric result.

## Proof

**1. Radon chord constraints.** Fix \(x,y\in S_X\) with \(x\perp_B y\) and \(\tau\in[0,1]\). Set \(a=\|x+\tau y\|\), \(b=\|x-\tau y\|\). Birkhoff orthogonality and the triangle inequality give
\[
 1\le a,b\le1+\tau.
\]
Convexity of the norm, applied separately to the two signs, yields
\[
 a\le1-\tau+\tau\|x+y\|,\quad
 b\le1-\tau+\tau\|x-y\|.
\]
Therefore the quoted Radon arithmetic-chord bound implies
\[
 a+b\le2(1-\tau)+3\tau=2+\tau.
\]
These are the only geometric constraints needed for the power-mean estimate.

**2. Sharp power-mean majorization.** For \(t\ge1\), the function \(s\mapsto s^t\) is convex and increasing on the positive reals. Under \(1\le a,b\le1+\tau\), \(a+b\le2+\tau\), increasing either coordinate until the sum reaches \(2+\tau\) cannot decrease \(a^t+b^t\). On the resulting segment, write \(b=2+\tau-a\) with \(a\in[1,1+\tau]\). The convex function \(a^t+(2+\tau-a)^t\) takes its maximum at a segment endpoint. Thus
\[
 a^t+b^t\le1+(1+\tau)^t,
\]
proving \(J^B_{X,t}(\tau)\le M_t(1,1+\tau)\). In the affine-regular hexagonal norm
\[
 \|(u,v)\|_G=\max\{|u|,|v|,|u-v|\},
\]
the explicit vectors \(x=(1,0)\), \(y=(0,1)\) are unit, and \(\|(1,\lambda)\|_G\ge1\) for every real \(\lambda\), so \(x\perp_B y\). Direct evaluation gives
\[
 \|x+\tau y\|_G=1,\qquad \|x-\tau y\|_G=1+\tau.
\]
Hence the profile bound is attained for every \(\tau\in[0,1]\), simultaneously for all finite \(t\ge1\).

**3. Exact one-variable optimum and uniqueness.** Define
\[
 F_t(u)=\frac{\left([1+(1+u)^t]/2\right)^{2/t}}{1+u^2},\qquad 0\le u\le1.
\]
For \(0\le u<1\), direct logarithmic differentiation shows that the sign of \(F_t'(u)\) is precisely the sign of
\[
 D_t(u)=(1-u)(1+u)^{t-1}-u.
\]
For \(u\le1/2\) and \(t\ge1\), \(D_t(u)\ge0\), with equality only for \(t=1,u=1/2\). For \(u\in(1/2,1)\), the equation \(D_t(u)=0\) is equivalent to \(T(u)=t\), with
\[
 T(u)=1+\frac{\log[u/(1-u)]}{\log(1+u)}.
\]
The derivative \(T'(u)\) has the sign of
\[
 (1+u)\log(1+u)-u(1-u)\log\frac{u}{1-u}.
\]
Using \(\log v\le v-1\) for positive \(v\) gives
\[
 u(1-u)\log\frac{u}{1-u}\le u(2u-1)\le u,
\]
whereas \((1+u)\log(1+u)>u\) for every positive \(u\). Therefore \(T'(u)>0\) on \((1/2,1)\). Since \(T(1/2)=1\) and \(T(u)\to\infty\) as \(u\uparrow1\), there is exactly one root \(u=\tau_t\) for each \(t\ge1\). The sign of \(F_t'\) changes from positive to negative there, proving the unique global maximizer and the formula for \(\mathcal B(t)\). This also proves strict increase of \(\tau_t\) in \(t\).

**4. Equality rigidity across Radon planes.** The hexagon achieves equality by Step 2. Conversely, for fixed \(t\ge1\), the sphere \(S_X\), the set of Birkhoff-orthogonal ordered pairs, and \([0,1]\) form compact admissible data in dimension two: the orthogonality relation is closed since it is an intersection of closed norm inequalities for all real \(\lambda\). Hence the constant's defining supremum is attained. If \(C^B_t(X)=\mathcal B(t)\), uniqueness of the scalar maximizer forces \(\tau=\tau_t>0\). Equality in the bound of Step 2 forces \(a+b=2+\tau_t\), since \(s\mapsto s^t\) is strictly increasing and the endpoint majorant is attained only on the sum boundary. Equality in the convex-interpolation estimate therefore gives \(\|x+y\|+\|x-y\|=3\). Consequently \(A^B_2(X)=3/2\); the quoted sharp Radon-plane characterization forces the unit circle to be an affine-regular hexagon. No assumption of strict convexity is used.

**5. Quadratic instance, order dependence, and large orders.** At \(t=1\), Step 3 gives \(\tau_1=1/2\), \(\mathcal B(1)=5/4\). At \(t=2\), the critical equation is \(\tau=(1-\tau)(1+\tau)=1-\tau^2\), so \(\tau_2=(\sqrt5-1)/2\); substitution gives \(\mathcal B(2)=(3+\sqrt5)/4\). The power mean of two *unequal* positive numbers is strictly increasing in its finite order. Since at every \(\tau>0\) the arguments \(1\) and \(1+\tau\) are unequal, \(\mathcal B(t)\) strictly increases with \(t\) by evaluation at the earlier order's maximizer.

For asymptotics write \(\delta_t=1-\tau_t\). The root relation becomes
\[
 \delta_t=(1-\delta_t)(2-\delta_t)^{1-t}.
\]
As \(\tau_t\ge1/2\), \(0<\delta_t\le(3/2)^{1-t}\), so \(t\delta_t\to0\). Dividing the displayed equation by \(2^{1-t}\) and using \(t\delta_t\to0\) proves \(\delta_t/2^{1-t}\to1\). Because the normalized two-point \(\ell_t\) mean is 1-Lipschitz in each argument for \(t\ge1\) (an immediate consequence of the reverse triangle inequality for \(\ell_t\) norms), the functions \(F_t\) have uniformly bounded Lipschitz constants on \([0,1]\). Therefore
\[
 0\le F_t(\tau_t)-F_t(1)\le O(\delta_t)=o(1/t).
\]
Finally,
\[
 F_t(1)=2^{1-2/t}(1+2^{-t})^{2/t}
 =2-\frac{4\log2}{t}+O(t^{-2}),
\]
which establishes the announced asymptotic limit. The companion 2026 isosceles-orthogonal theorem gives \(C_t^I(G)=5/4\) for all finite \(t\); since \(\mathcal B(t)>\mathcal B(1)=5/4\) for \(t>1\), the claimed strict comparison follows.

## Verification

The complete proof uses only the quoted Radon-plane arithmetic-chord theorem, elementary norm convexity, convex majorization of a two-point power mean, calculus, compactness, and asymptotic estimates. The standalone standard-library Python checker `check.py` performs 5,942 deterministic checks: exact rational hexagonal norm identities, Birkhoff feasibility samples, convex endpoint majorization for integer orders, and numerical consistency tests of the unique scalar maximizer, quadratic closed form, and large-order expansion. All tests passed. They are finite cross-checks only; Steps 1–5 above establish the universal quantified statements.

Reproduce with `python3 check.py` from the directory containing this file. No numerical optimization, discretization of the sphere, or external repository is required in the proof.

## Relationship to prior work

Qi–Yin–Liu (arXiv:2608.07146v1, first public 2026-08-07) introduce the same Birkhoff-restricted constant and prove the sharp Radon-plane value \(5/4\) for orders \(t\le1\) (Theorem 16), by means of the published arithmetic-chord bound. Their Theorem 8 gives a general James-constant envelope and Theorem 10 treats the arithmetic-or-lower order; neither yields the sharp \(t>1\) formula or its unique scale. The present theorem uses their geometric input but solves the **unaddressed higher-order scalar majorization problem** for every real Radon plane.

Li–Zhang–Qi–Liu (Axioms 15(9), 684, 2026, DOI 10.3390/axioms15090684) obtain the *different, direct isosceles-restriction* profile, which stays at \(5/4\) for the affine-regular hexagon at all finite orders. The strict disagreement for every \(t>1\) distinguishes the two restrictions at the sharp Radon model. Martín–Papini (2024) treat extremal sums of Birkhoff-orthogonal unit vectors, but not this high-order deformation optimum. The 2025 Du–Liang–Li article concerns the arithmetic-chord geometric input. Related publicly indexed calculations of Takahashi-type constants for classical \(\ell_p\) and \(L_p\) spaces, and unrelated von Neumann–Jordan generalizations on the hexagon, do not assert this all-Radon, Birkhoff-restricted high-order extremal formula in the inspected material.

## Limitations

The theorem concerns finite orders \(t\ge1\), real two-dimensional Radon spaces, and the particular power-mean normalization defined above. It does not provide a quantitative stability estimate for *nearly* extremal planes, classify all extremizing pairs, or establish a universal formula for non-Radon spaces. The arithmetic-chord rigidity theorem is a cited external premise. An older equivalent result expressed via convex majorization or Radon-plane chord geometry remains a possible publication-priority risk.

## References

1. J. Qi, Z. Yin, Q. Liu, *Birkhoff-Orthogonal Takahashi-von Neumann-Jordan Type Constants in Banach Spaces*, arXiv:2608.07146v1 (submitted 2026-08-07), especially Lemma 1, Theorems 8, 10, 16 and Eq. (23). https://arxiv.org/abs/2608.07146
2. Y. Li, W. Zhang, J. Qi, Q. Liu, *Isosceles-Orthogonal Takahashi–von Neumann–Jordan-Type Constants in Banach Spaces*, Axioms 15 (2026), article 684, DOI:10.3390/axioms15090684. https://doi.org/10.3390/axioms15090684
3. P. Martín, P. L. Papini, *Moving around the sums of orthogonal unit vectors*, Mathematical Inequalities & Applications 27(2) (2024), 401–415, DOI:10.7153/mia-2024-27-28. https://files.ele-math.com/articles/mia-27-28.pdf
4. D. Du, R. Liang, Y. Li, *Some moduli of convexity and smoothness related to Birkhoff orthogonality in Banach spaces*, RACSAM 119 (2025), article 110, DOI:10.1007/s13398-025-01779-0.
