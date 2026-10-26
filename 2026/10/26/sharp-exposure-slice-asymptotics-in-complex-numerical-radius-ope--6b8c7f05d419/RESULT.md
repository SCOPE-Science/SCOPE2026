# Sharp exposure-slice asymptotics in complex numerical-radius operator duals

## Finding

Let \(d\ge2\) and \(1<p<\infty\). Equip \(X=\ell_p^d(\mathbb C)\) with its usual complex norm and \(V=\mathcal L(X)\) with the *spatial numerical-radius norm* \(w\). Let \(P\) denote projection onto the first coordinate and let \(F_0(A)=A_{11}\). Define the radius of the exposed dual slice
\[
\Omega_{p,d}(\varepsilon)=\sup\big\{\|F-F_0\|_{V^*}:\|F\|_{V^*}\le1,\ \operatorname{Re}F(P)\ge1-\varepsilon\big\}.
\]
With \(q=p/(p-1)\) and \(\alpha_p=1/\max\{p,q\}\), the **sharp full-dual-ball asymptotic** is
\[
\lim_{\varepsilon\downarrow0}\frac{\Omega_{p,d}(\varepsilon)}{\varepsilon^{\alpha_p}}=
\begin{cases}
\dfrac{p}{(p-1)^{(p-1)/p}},&p\ne2,\\
\sqrt6,&p=2.
\end{cases}
\]
The answer is independent of dimension \(d\). In particular, the sharp coefficient jumps at the Hilbert exponent: its two one-sided limits as \(p\to2\) equal \(2\), but the value at \(p=2\) is \(\sqrt6\). The same exponent and coefficient apply to arbitrary elements of the **whole dual unit ball**, not just its rank-one state functionals.

## Assumptions and scope

All spaces, operators, and functionals are **complex**. We regard \(V^*\) as the complex-linear dual of \((V,w)\), using \(\operatorname{Re}F(P)\) to define a real convex slice. Set
\[
j_p(x)(z)=\sum_{k=1}^d |x_k|^{p-2}\overline{x_k}z_k\qquad (\|x\|_p=1),
\]
interpreting a zero-coordinate summand as zero. Then \(\|j_p(x)\|_q=j_p(x)(x)=1\), and
\[
w(A)=\max_{\|x\|_p=1}|j_p(x)(Ax)|.
\]
It is a norm in the stated complex finite-dimensional setting. Indeed, if \(w(A)=0\), tests on individual coordinate vectors give all diagonal entries zero, and the tests \(e_j+r e^{i\phi}e_k\), with arbitrary phase \(\phi\), force both off-diagonal entries in every two-coordinate block to vanish. (Normalization of these test vectors is immaterial for a zero numerical radius.) Thus, by norm equivalence, there is \(M_{p,d}<\infty\) such that \(\|A\|\le M_{p,d}w(A)\).

The full dual unit ball is the ordinary convex hull of the compact circled set of normalized states
\[
F_{x,\theta}(A)=e^{i\theta}j_p(x)(Ax),\quad \|x\|_p=1,\quad \theta\in[-\pi,\pi].
\]
This follows from the definition of \(w\) and the finite-dimensional bipolar theorem; the states are norm-one functionals because they take modulus one on the identity. Finally, \(w(P)=1\) and \(F_0=F_{e_1,0}\) expose the stated slice center.

## Proof

**Step 1: exact one-row and one-column dual norms.** Write \(x=(s,y)\) with \(s\ge0\), \(y\in\mathbb C^{d-1}\), \(t=\|y\|_p\), and \(s^p+t^p=1\). The common phase of \(x\) can be changed without changing \(F_{x,\theta}\). For a tail vector \(y\) and a tail covector \(h\), define
\[
R_y(A)=(Ay)_1,\qquad C_h(A)=h(Ae_1).
\]
Both functionals disregard all matrix entries except, respectively, the first off-diagonal row or column. Let
\[
c_p=\max_{0\le u\le1}u^{p-1}(1-u^p)^{1/p}
=\max_{0\le u\le1}u(1-u^p)^{(p-1)/p}
=\frac{(p-1)^{(p-1)/p}}p.
\]
The expressions are the numerical radii of normalized rank-one first-row and first-column operators. More precisely, \(w(e_1\otimes b)=c_p\|b\|_q\), for \(b\) supported on the tail, and \(w(z\otimes e_1^*)=c_p\|z\|_p\), for \(z\) supported on the tail. To bound general operators, average conjugation by the coordinate-phase isometries \(U_\phi=\operatorname{diag}(e^{i\phi},1,\ldots,1)\) against the two first Fourier characters. This produces contractive numerical-radius projections onto precisely those row and column operator subspaces. Consequently the dual norms are **exactly**
\[
\|R_y\|_{V^*}=\frac{\|y\|_p}{c_p}=\frac{t}{c_p},\qquad
\|C_h\|_{V^*}=\frac{\|h\|_q}{c_p}.
\]
The lower bounds come from tail Hölder-norming rank-one rows and columns, respectively, so neither is merely a norm estimate.

**Step 2: expansion of a pure state near the exposed point.** Put \(h=j_p(y)|_{\{2,\ldots,d\}}\), so \(\|h\|_q=t^{p-1}\). For every operator \(A\),
\[
F_{x,\theta}(A)-F_0(A)
=(e^{i\theta}s^p-1)A_{11}
+e^{i\theta}s^{p-1}R_y(A)
+e^{i\theta}s C_h(A)
+e^{i\theta}h(Ay).
\]
The slice deficit of this pure state is exactly
\[
\delta=1-\operatorname{Re}F_{x,\theta}(P)=1-s^p\cos\theta
=t^p+s^p(1-\cos\theta).
\]
It follows that \(t\le\delta^{1/p}\), the phase is \(O(\sqrt\delta)\) as \(\delta\downarrow0\), and
\[
|e^{i\theta}s^p-1|\le\sqrt{2\delta},\qquad
\|h(Ay)\|_{V^*}\le M_{p,d}t^p.
\]
Combining these with Step 1 gives the uniform pure-state bound
\[
\|F_{x,\theta}-F_0\|_{V^*}
\le\sqrt{2\delta}+c_p^{-1}\big(s^{p-1}t+s t^{p-1}\big)+M_{p,d}t^p.
\]
For \(p>2\), only the first off-diagonal term survives after dividing by \(\delta^{1/p}\); for \(1<p<2\), only the second survives after dividing by \(\delta^{(p-1)/p}\). Hence for all \(p\ne2\)
\[
\limsup_{\delta\downarrow0}\sup_{F_{x,\theta}:\,1-\operatorname{Re}F_{x,\theta}(P)=\delta}
\frac{\|F_{x,\theta}-F_0\|_{V^*}}{\delta^{\alpha_p}}\le c_p^{-1}.
\]
For sharpness, take \(x=(s,t,0,\ldots,0)\), \(s=(1-t^p)^{1/p}\), \(\theta=0\); then \(\delta=t^p\). If \(p>2\), test against the matrix \(A=E_{12}/c_p\), whose numerical radius is one: \(\|F_{x,0}-F_0\|\ge s^{p-1}t/c_p\). If \(p<2\), use \(A=E_{21}/c_p\) instead: \(\|F_{x,0}-F_0\|\ge st^{p-1}/c_p\). These match the upper bound.

**Step 3: the coupled Hilbert-exponent term.** When \(p=2\), the two off-diagonal terms have the same order, and treating their norms separately would lose sharpness. For \(h=y/t\perp e_1\) of Hilbert norm one, the functional \(R_h+C_{j_2(h)}\) is the difference of the vector states at \((e_1+h)/\sqrt2\) and \((e_1-h)/\sqrt2\); therefore its dual norm is at most \(2\). Equality holds on the self-adjoint swap \(A=e_1\otimes h^*+h\otimes e_1^*\), which has \(w(A)=1\). Thus
\[
\|R_y+C_{j_2(y)}\|_{V^*}=2t.
\]
The pure-state expansion now yields, uniformly as \(t,\theta\to0\),
\[
\|F_{x,\theta}-F_0\|_{V^*}\le |\theta|+2t+O(t^2+\theta^2),\quad
\delta=t^2+\tfrac12\theta^2+o(t^2+\theta^2).
\]
Cauchy--Schwarz gives the sharp upper bound \((|\theta|+2t)/\sqrt{t^2+\theta^2/2}\le\sqrt6\). For a matching **single-state** witness, work in the first two coordinates, take \(x=(\sqrt{1-t^2},t,0,\ldots)\), \(\theta=t\), and the operator with leading block
\[
A_* =\begin{pmatrix}-i&1\\1&i\end{pmatrix}
\]
and every other entry zero. Here \(w(A_*)=1\): on the two-coordinate Hilbert sphere its numerical values are \(i(|z_2|^2-|z_1|^2)+2\operatorname{Re}(\overline z_1z_2)\), of modulus at most one, and the value at \(e_1\) has modulus one. Direct expansion gives
\[
F_{x,t}(A_*)-F_0(A_*)=3t+O(t^2),\qquad
\delta=\tfrac32t^2+O(t^4),
\]
so the ratio tends to \(\sqrt6\). This argument also applies unchanged in higher dimension by zero extension.

**Step 4: pass from pure states to the entire dual ball.** Fix \(0<\alpha=\alpha_p<1\) and the corresponding coefficient \(C_p\) from Steps 2--3. The pure-state estimates imply that for any \(\eta>0\) there is \(r>0\) such that a state with deficit \(0\le\delta_i\le r\) satisfies \(\|F_i-F_0\|\le(C_p+\eta)\delta_i^\alpha\); states with \(\delta_i>r\) always satisfy \(\|F_i-F_0\|\le2\). Write an arbitrary dual-ball element as \(F=\sum_i\lambda_iF_i\), with \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\). Its deficit \(\delta=1-\operatorname{Re}F(P)\) is \(\sum_i\lambda_i\delta_i\). The large-deficit total weight is at most \(\delta/r\), while the concavity of \(u\mapsto u^\alpha\) gives \(\sum_i\lambda_i\delta_i^\alpha\le\delta^\alpha\). Therefore
\[
\|F-F_0\|_{V^*}\le(C_p+\eta)\delta^\alpha+2\delta/r
\le(C_p+\eta)\varepsilon^\alpha+2\varepsilon/r
\]
whenever \(\operatorname{Re}F(P)\ge1-\varepsilon\). Divide by \(\varepsilon^\alpha\), let \(\varepsilon\downarrow0\), and then \(\eta\downarrow0\). The pure-state examples in Steps 2--3 give the opposite limiting inequality, proving the claimed exact formula.

## Verification

The proof uses exact rank-one numerical-radius maxima, contractive Fourier averaging, an explicit two-by-two Hilbert witness, and the finite-dimensional bipolar representation of the whole dual ball. The values of the non-Hilbert coefficient are approximately \(1.889881574\) at \(p=3/2\), \(1.99723056\) at \(p=1.9\), and \(1.75476535\) at \(p=4\); the Hilbert coefficient is exactly \(\sqrt6\approx2.449489743\). These decimals are checks, not proof inputs. No finite enumeration or numerical experiment is used to infer the infinite limiting statement. All remainders are for fixed \(p,d\) with \(\varepsilon\downarrow0\), and the witnesses require only the first two coordinates.

## Relationship to prior work

Pal--Roy--Sain (2026), in particular Theorems 2.16 and 2.20 of their first preprint, determine the extreme dual states and establish qualitative exposure for finite-dimensional smooth strictly convex spaces. This result asks a different, quantitative question about the **norm diameter from the exposed point inside a depth-\(\varepsilon\) slice** and computes its exact leading power and coefficient. Their convex-hull representation is compatible with Step 4; it does not itself furnish that sharp asymptotic. Martín--Merí--Quero--Roy--Sain (2024), Section 3.6, study numerical-radius norming states and Birkhoff--James orthogonality, including smoothness; no sharp dual-slice coefficient follows from their statements. The two-link weighted-shift radius literature contains the same scalar mixed-exponent factor underlying Step 1, but not the entire-dual-slice asymptotic or its Hilbert-exponent coupling.

## Limitations

The result concerns the complex finite-dimensional spaces \(\ell_p^d\) with \(1<p<\infty\), and the particular exposed point \(A\mapsto A_{11}\) exposed by \(P\). Coordinate permutations give the corresponding statement for other individual diagonal coordinate states. It does not assert a dimension-uniform finite-\(\varepsilon\) error bound, does not treat real scalars or endpoint exponents, and does not characterize every exposed point. The literature comparison cannot establish absolute publication priority against every unindexed source; the stated original contribution is this exact combined quantitative asymptotic, not the norming-state convex-hull description or the rank-one scalar maximization individually.

## References

1. Subhadip Pal, Saikat Roy, and Debmalya Sain, *A characterization of Banach spaces with numerical index one*, arXiv:2604.03690v1 (first posted 2026-04-04), Theorems 2.16 and 2.20. https://arxiv.org/html/2604.03690v1
2. Miguel Martín, Javier Merí, Alicia Quero, Saikat Roy, and Debmalya Sain, *A numerical range approach to Birkhoff--James orthogonality with applications*, Banach Journal of Mathematical Analysis 18 (2024), article 24, Section 3.6; arXiv:2306.02638v3. https://link.springer.com/article/10.1007/s43037-024-00333-1
