# Complete complex extremizers for the anisotropic finite-field paraboloid

## Finding
Let \(q=p^n\equiv3\pmod4\) be any odd prime power. Write \(V=\mathbb F_q^2\), \(Q(u)=u_1^2+u_2^2\), and \(\psi(s)=\exp(2\pi i\,\mathrm{Tr}_{\mathbb F_q/\mathbb F_p}(s)/p)\). Define the finite paraboloid extension operator by
\[
\mathcal E_q f(X,t)=q^{-2}\sum_{u\in V}f(u)\psi(X\cdot u+tQ(u)),\qquad (X,t)\in V\times\mathbb F_q.
\]
The sharp inequality of González-Riquelme–Oliveira e Silva is
\[
\sum_{X\in V}\sum_{t\in\mathbb F_q}|\mathcal E_q f(X,t)|^4
\le (1+q^{-1}-q^{-2})\left(q^{-2}\sum_{u\in V}|f(u)|^2\right)^2.
\]
**The additional classification here** is that equality for a nonzero complex function holds **if and only if**
\[
f(u)=\lambda\,\psi(\alpha u_1+\beta u_2+\gamma Q(u))
\quad\text{for all }u\in V,
\]
with \(\lambda\in\mathbb C\setminus\{0\}\) and \(\alpha,\beta,\gamma\in\mathbb F_q\). Thus there are exactly \(q^3\) extremizers modulo multiplication by nonzero complex scalars. The best constant and the constant-modulus necessity are established prior results; the all-phase classification in the anisotropic case is the subject of this finding.

## Assumptions and scope
The characteristic is odd, the field may be a proper extension of its prime subfield, and \(q\equiv3\pmod4\). Consequently \(-1\) is nonsquare and \(Q(u)=0\) implies \(u=0\). All sums use counting measure in the target and normalized counting measure on the paraboloid. The additive character \(\psi\) is fixed as above; replacing it with any nontrivial additive character only reparametrizes the coefficients. The zero function satisfies equality trivially but is excluded from the classification and projective count.

## Proof
**1. Recover the exact equality equation.** The proof of Theorem 1.1, case \(q\equiv3\pmod4\), in [1, §4.1, equations (4.3)–(4.6)] establishes the sharp inequality and shows every nonzero equality case has a constant nonzero modulus. For the noncritical pair-sum fibers, equality must also hold in each nonnegative Cauchy–Schwarz deficit. In a fiber indexed by \((u+v,Q(u)+Q(v))\), equality is therefore equivalent to constancy of the product \(f(u)f(v)\) as the ordered pair \((u,v)\) varies over that fiber. The critical fibers (equal coordinates) have one element because \(Q\) is anisotropic.

Choose \(x,a,b\in V\) with \(a\cdot b=0\). The unordered pairs \(\{x,x+a+b\}\) and \(\{x+a,x+b\}\) have the same sum and the same sum of squared norms, since
\[
Q(x)+Q(x+a+b)-Q(x+a)-Q(x+b)=2a\cdot b=0.
\]
If \(a,b\ne0\), then anisotropy forces \(a,b\) to be independent: a nonzero vector cannot be orthogonal to itself, and no nonzero multiple of it can be orthogonal to it. Thus the common fiber is noncritical and its Cauchy–Schwarz equality gives
\[
 f(x+a+b)f(x)=f(x+a)f(x+b)\qquad(a\cdot b=0). \tag{1}
\]
The same formula holds trivially if an increment is zero. Conversely, (1) identifies every pair-sum fiber: any two ordered pairs with equal sum and equal squared-norm sum differ by exchanging opposite corners of such an orthogonal parallelogram. This converse is not needed for necessity but ensures no extra equalities are omitted.

**2. All multiplicative second differences are constant.** Because \(f\) has nonzero constant modulus, write
\[
 D_a f(x)=\frac{f(x+a)}{f(x)},\qquad
 B_x(a,b)=\frac{f(x+a+b)f(x)}{f(x+a)f(x+b)}.
\]
By (1), for fixed \(a\ne0\), \(D_af(x)\) is unchanged under every translation by \(b\in a^\perp\). Hence \(D_af(x)\) depends only on the scalar \(x\cdot a\): the kernel of the surjective functional \(x\mapsto x\cdot a\) is precisely \(a^\perp\).

When \(a,b\) are linearly independent over \(\mathbb F_q\), \(B_x(a,b)=D_af(x+b)/D_af(x)\) depends only on \(x\cdot a\). By symmetry, the same quantity depends only on \(x\cdot b\). Because \(x\mapsto(x\cdot a,x\cdot b)\) is a bijection from \(V\) to \(\mathbb F_q^2\), \(B_x(a,b)\) must be independent of \(x\).

For collinear nonzero \(a,b\), choose \(c\notin\mathbb F_q a\). The multiplicative identity
\[
D_bf(x)=D_cf(x)D_{b-c}f(x+c)
\]
shows, after taking the \(a\)-difference, that \(B_x(a,b)\) is a product of two quantities independent of \(x\), as both \((a,c)\) and \((a,b-c)\) are independent. Zero increments give \(B_x=1\). Consequently \(B_x(a,b)=B(a,b)\) is independent of \(x\) for every pair of increments.

**3. Identify the bilinear phase.** The multiplicative finite-difference identities give
\[
B(a+a',b)=B(a,b)B(a',b),\qquad B(a,b+b')=B(a,b)B(a,b'),
\]
and \(B(a,b)=B(b,a)\). Thus \(B\) is a symmetric bicharacter of the additive group \(V\). Equation (1) says \(B(a,b)=1\) whenever \(a\cdot b=0\).

For fixed nonzero \(a\), the character \(b\mapsto B(a,b)\) is trivial on \(a^\perp\), so it factors as
\[
B(a,b)=\chi_a(a\cdot b)
\]
for an additive character \(\chi_a\) of \(\mathbb F_q\). If \(a,a'\) are independent, then additivity of \(B\) in its first argument yields
\[
\chi_{a+a'}(r+s)=\chi_a(r)\chi_{a'}(s)
\qquad\text{for all }r,s\in\mathbb F_q,
\]
since the two dot products with \(b\) vary independently. Setting first \(s=0\) and then \(r=0\) proves \(\chi_{a+a'}=\chi_a=\chi_{a'}\). A third noncollinear vector connects any collinear nonzero pair, so all \(\chi_a\) equal a single character \(\chi\). Every additive character of \(\mathbb F_q\) is of the form \(\chi(s)=\psi(\delta s)\) for a unique \(\delta\in\mathbb F_q\), by nondegeneracy of the field trace pairing. Hence
\[
B(a,b)=\psi(\delta\,a\cdot b).
\]
Define \(g(u)=\psi(\tfrac\delta2 Q(u))\). Polarization of \(Q\) shows that its multiplicative second difference is \(\psi(\delta\,a\cdot b)\), exactly \(B(a,b)\). Therefore \(h=f/g\) has \(B_h(a,b)=1\) for all \(a,b,x\). Taking \(x=0\) yields \(h(a+b)=h(a)h(b)/h(0)\). The quotient \(h/h(0)\) is an additive character of \(V\), so it equals \(u\mapsto\psi(\alpha u_1+\beta u_2)\) for unique \(\alpha,\beta\in\mathbb F_q\). This proves the asserted form, with \(\gamma=\delta/2\).

**4. Sufficiency and uniqueness.** For a function of the asserted form, \(\mathcal E_q f(X,t)=\lambda\mathcal E_q 1(X+(\alpha,\beta),t+\gamma)\). Translating the target variables preserves its fourth moment, and the constant signal is an equality case of [1, Theorem 1.1]. To count projective classes, suppose two parameter triples induce identical phases up to a scalar. Their ratio has constant multiplicative second differences, forcing \(\psi(2\Delta\gamma\,a\cdot b)=1\) for every \(a,b\). Nondegeneracy of \(\psi\) gives \(\Delta\gamma=0\); then evaluating the remaining linear character implies \(\Delta\alpha=\Delta\beta=0\). Thus exactly \(q^3\) classes occur.

## Verification
The standalone `verify.py` uses only the Python standard library. It constructs all noncritical pair-sum phase constraints for primes \(p=3,7,11\) and reduces the linearized relation matrix exactly over \(\mathbb F_p\); the computed ranks are \(5,45,117\), respectively, equal to \(p^2-4\). It separately checks five quadratic chirp coefficient systems and directly evaluates the normalized fourth moment for two chirps at each prime, agreeing with the sharp value to within \(3\times10^{-9}\). Run `python verify.py` from the package directory. These finite checks corroborate the unrestricted finite-field proof; they are not a proof for all prime powers.

## Relationship to prior work
González-Riquelme and Oliveira e Silva [1] prove the sharp constant and constant-modulus requirement for all odd finite fields. Their Theorem 1.2 fully classifies complex maximizers for the **opposite** congruence class \(q\equiv1\pmod4\), while §4.1 stops at the constant-modulus conclusion when \(q\equiv3\pmod4\). González-Riquelme and Ismoilov [2, §1.2] explicitly distinguish that unresolved complex-phase issue while investigating **cones**, not this paraboloid. Older finite-field paraboloid estimates [3] do not provide this equality classification. The additional conclusion here is the complete rigid quadratic-character form for every anisotropic field, including non-prime fields, plus the exact projective extremizer count.

## Limitations
The classification applies only to the two-dimensional quadratic paraboloid over odd fields with \(q\equiv3\pmod4\) and its normalized \(L^2\to L^4\) endpoint. No statement is made about the isotropic class, different surfaces, other exponents, or quantitative near-extremizer stability. Although the proof is unrestricted over the stated fields, priority cannot be established conclusively from a finite set of literature searches; an unindexed equivalent result may exist.

## References
[1] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (first posted 2024-05-26), Theorems 1.1–1.2 and §4.1. https://arxiv.org/abs/2405.16647

[2] C. González-Riquelme and T. Ismoilov, *Maximizers of the \(L^2\to L^4\) Fourier extension inequality for cones in finite fields*, arXiv:2509.05600 (2025), §1.2. https://arxiv.org/abs/2509.05600

[3] A. Iosevich and D. Koh, *Extension theorems for paraboloids in the finite field setting*, Math. Z. 266 (2010), 471–487. https://users.math.msu.edu/users/koh/papers/Mathz.pdf
