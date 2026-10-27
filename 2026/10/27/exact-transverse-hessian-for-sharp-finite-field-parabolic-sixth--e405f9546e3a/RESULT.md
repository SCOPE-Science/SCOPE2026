# Exact transverse Hessian for sharp finite-field parabolic sixth moments

## Finding
For every finite field \(\mathbb F_q\) of characteristic \(p>3\), every nontrivial additive character \(\psi\), and every function \(f:\mathbb F_q\to\mathbb C\), set
\[
\mathcal E_qf(X,Y)=q^{-1}\sum_{x\in\mathbb F_q}f(x)\psi(Xx+Yx^2),\qquad
\mathcal J_q(f)=\frac{\sum_{X,Y\in\mathbb F_q}|\mathcal E_qf(X,Y)|^6}{\bigl(q^{-1}\sum_x|f(x)|^2\bigr)^3}.
\]
The quotient is defined for \(f\ne0\). A known sharp extension inequality gives
\(\mathcal J_q(f)\le C_q:=1+q^{-1}-q^{-2}\), with equality at constant functions [1].

**Exact transverse second variation.** For real-valued mean-zero \(u,v:\mathbb F_q\to\mathbb R\) and real \(\varepsilon\to0\),
\[
\boxed{\mathcal J_q(1+\varepsilon(u+iv))
=C_q-\varepsilon^2\left[\frac{3(q^2-2q+4)}{q^2}\|u\|_{2,q}^2+
\frac{3(q-2)}q\|v\|_{2,q}^2\right]+O_{q,u,v}(\varepsilon^3),}
\]
where \(\|w\|_{2,q}^2=q^{-1}\sum_x|w(x)|^2\). Thus the half-Hessian of the sharp deficit \(C_q-\mathcal J_q\), on the real Hilbert space with normalized \(L^2\) metric, has the eigenvalues \(0\) (multiplicity \(2\), complex constants), \(3(q-2)/q\) (multiplicity \(q-1\), imaginary mean-zero functions) and \(3(q^2-2q+4)/q^2\) (multiplicity \(q-1\), real mean-zero functions). Every nonzero constant is strictly locally maximizing modulo complex scaling, and the **sharp transverse local stability coefficient** is \(3(q-2)/q\), achieved asymptotically in every nonzero imaginary mean-zero direction. The same conclusion holds at any quadratic-character global maximizer by modulation symmetries.

## Assumptions and scope
The field order is an arbitrary prime power \(q=p^n\) with \(p\ge5\) and \(n\ge1\); the phase character \(\psi\) is any nontrivial additive character. The result concerns the sixth **power** of the extension norm, divided by the cube of normalized input energy. It is a fixed-field second-order, not a global quantitative stability theorem with a field-independent neighborhood radius. The known global sharp bound is used only to identify the local expansion as an extremal deficit. The two positive Hessian eigenvalues are distinct for every allowed \(q\), with the imaginary band smaller by exactly \(12/q^2\).

## Proof
**1. Convolution normalization and a two-valued fiber count.** For \((s,t)\in\mathbb F_q^2\), put
\[
T_f(s,t)=\sum_{x+y+z=s\atop x^2+y^2+z^2=t}f(x)f(y)f(z),\qquad
S(f)=\sum_{s,t}|T_f(s,t)|^2.
\]
Orthogonality of the additive characters gives exactly
\[
\mathcal J_q(f)=\frac{S(f)}{q\,(\sum_x|f(x)|^2)^3}.
\]
Let \(N(s,t)=T_1(s,t)\), and write \(\kappa=\chi_q(-3)\in\{\pm1\}\), where \(\chi_q(0)=0\) is the quadratic character. Translating by \(s/3\) and counting a nondegenerate binary quadratic form yields
\[
N(s,t)=q-\kappa+q\kappa\,\mathbf1_{\{t=s^2/3\}}.
\]
(The quadratic form is \(2(a^2+ab+b^2)\), of discriminant square class \(-3\).) Hence
\[
S(1)=q^2(q^2+q-1),\qquad \mathcal J_q(1)=q^{-2}(q^2+q-1)=C_q.
\]

**2. Hessian symmetry.** The affine group \(x\mapsto ax+b\), \(a\ne0\), acts doubly transitively on \(\mathbb F_q\) and preserves \(\mathcal J_q\): a change of spectral variable corresponds to an invertible affine change of \((X,Y)\) and an output factor of unit modulus. Complex conjugation also preserves \(\mathcal J_q\), so the real and imaginary Hessian blocks decouple. A real symmetric matrix invariant under a doubly transitive permutation action has constant diagonal and constant off-diagonal. Therefore each block is a scalar on mean-zero real functions, and its scalar is obtained by testing \(h=\mathbf1_{\{0\}}-\mathbf1_{\{1\}}\), whose counting-energy is \(\sum_xh(x)^2=2\). Homogeneity under nonzero complex scaling supplies exactly two null directions, the real and imaginary constants, once positivity of the mean-zero coefficients is proved.

**3. Exact test-vector coefficients.** Expand
\[
T_{1+\varepsilon h}=N+\varepsilon L+\varepsilon^2Q+O(\varepsilon^3),
\]
where \(L(s,t)=\sum_{x+y+z=s,\,\sum x^2=t}(h(x)+h(y)+h(z))\), and \(Q\) is the corresponding sum of \(h(x)h(y)+h(x)h(z)+h(y)h(z)\). The number of solutions in the remaining two variables when the first variable equals \(a\) is \(1+\chi_q(D_a)\), for \(D_a=2(t-a^2)-(s-a)^2\). Consequently
\[
L(s,t)=3[\chi_q(D_0)-\chi_q(D_1)],
\]
and
\[
Q(s,t)=3\Big[\mathbf1_{\{t=s^2\}}+\mathbf1_{\{t=2+(s-2)^2\}}-2\mathbf1_{\{t=1+(s-1)^2\}}\Big].
\]
As \(D_1-D_0=2s-3\), the elementary character identity \(\sum_{z\in\mathbb F_q}\chi_q(z(z+c))=q-1\) for \(c=0\), and \(-1\) otherwise, shows the mixed sum \(\sum_{s,t}\chi_q(D_0)\chi_q(D_1)=0\). It follows that
\[
\sum_{s,t}L(s,t)^2=18q(q-1).
\]
For fixed \(a,b\), the residual on the curve \(t=a^2+b^2+(s-a-b)^2\) is
\[
t-s^2/3=\frac23\left(s-\frac32(a+b)\right)^2+\frac12(a-b)^2.
\]
Thus \(\sum_sN(s,a^2+b^2+(s-a-b)^2)=q^2\) if \(a=b\), and \(q(q+1)\) if \(a\ne b\), because the residual has respectively \(1\) or \(1+\kappa\) zeros. Substituting the three curves defining \(Q\) gives
\[
\sum_{s,t}N(s,t)Q(s,t)=3[q^2+q^2-2q(q+1)]=-6q.
\]

**4. Real/imaginary curvature and full spectrum.** When \(h\) is real, the coefficient of \(\varepsilon^2\) in \(S(1+\varepsilon h)\) is \(\sum L^2+2\sum NQ\). When the perturbation is \(i\varepsilon h\), it is \(\sum L^2-2\sum NQ\). The denominator contributes \(-3S(1)\sum h^2/q=-6S(1)/q\) to the coefficient of the normalized convolution polynomial, in each case. Therefore the two coefficient values before division by \(q^4\) are respectively
\[
-6q(q^2-2q+4),\qquad -6q^2(q-2).
\]
Dividing by \(\sum h^2=2\), and using the doubly transitive symmetry from Step 2, yields for general real mean-zero \(u,v\) the claimed second-order expansion. The phase/amplitude mixed term vanishes by conjugation symmetry. Both coefficients are positive for \(q\ge5\), and their difference (in normalized \(L^2\) units) is \(12/q^2\).

**5. Sharp local stability.** Let \(\operatorname{dist}_{2,q}(f,\mathbb C1)=\inf_{c\in\mathbb C}\|f-c1\|_{2,q}\). Since the kernel consists of complex constants, finite-dimensional Taylor expansion and the strict curvature gap give
\[
\lim_{\rho\downarrow0}\inf_{0<\operatorname{dist}_{2,q}(f,\mathbb C1)/\|f\|_{2,q}\le\rho}
\frac{C_q-\mathcal J_q(f)}{\operatorname{dist}_{2,q}(f,\mathbb C1)^2/\|f\|_{2,q}^2}
=\frac{3(q-2)}q.
\]
The lower bound is the smallest positive Hessian band, and equality in the limit is realized by perturbations \(f=1+i\varepsilon v\) for any nonzero mean-zero real \(v\). A quadratic modulation \(f(x)\mapsto\psi(Ax+Bx^2)f(x)\) translates \((X,Y)\), preserving the quotient and transferring the local statement to all such global maximizers.

## Verification
The attached standalone Python checker computes the exact triple-fiber and perturbation sums by finite-field arithmetic for prime fields of orders \(5,7,11,13\) and the quadratic extension field of order \(25\). For each, it checks the symbolic identities \(S(1)=q^2(q^2+q-1)\), \(\sum L^2=18q(q-1)\), and \(\sum NQ=-6q\). Independent direct numerical evaluation of the normalized Fourier quotient at orders \(5\) and \(7\) confirms both predicted real and imaginary coefficients as the perturbation tends to zero. These finite checks corroborate, but do not replace, the all-prime-power argument in Steps 1–5. Run: `python3 verify_parabolic_hessian.py`.

## Relationship to prior work
González-Riquelme and Oliveira e Silva [1] proved the sharp \(L^2\to L^6\) extension bound on the finite-field parabola in characteristic greater than three; their main statements, triple-convolution count, and proof section concern the norm and extremizers, not the full constrained Hessian or its exact two-band local stability constant. An indexed characteristic-three result [2] gives the same formal Hessian coefficients in fields of characteristic three, but its hypothesis does not include any characteristic greater than three. The present nondegenerate conic argument covers precisely the complementary characteristic range and, using [1], identifies the *sharp deficit at global extremizers* there. An indexed anisotropic two-dimensional paraboloid Hessian [3] concerns \(L^4\) rather than the one-dimensional \(L^6\) parabola, and neither implies these coefficients. Phase-classification results for this parabola identify its maximizers but not their local curvature.

## Limitations
The expansion is pointwise in each fixed finite field and perturbation, with no uniform high-field Taylor remainder or claimed global stability modulus. It does not independently reprove the global extension inequality or the complete equality classification. Earlier unindexed or inaccessible specialized work may contain equivalent second-variation calculations; public indexing and database searches do not establish absolute novelty. No independent audit has been performed.

## References
[1] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (first posted 2024-05-26), Theorem 1.3, Proposition 3.3, and Section 6. https://arxiv.org/abs/2405.16647

[2] *Exact local sixth-moment stability of the parabola in characteristic three* (2026), publicly indexed mathematical result, identifier `158763dab4f3` (characteristic-three claim compared via its indexed statement).

[3] *Two-band Hessian and sharp local gap for anisotropic finite-field paraboloid extension* (2026), publicly indexed mathematical result, identifier `80ecd3989428` (two-dimensional fourth-moment comparison via its indexed statement).
