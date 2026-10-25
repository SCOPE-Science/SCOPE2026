# A two-frequency obstruction to relaxation-free energy correction for SSPRK(3,3)

## Finding

For the fixed-coefficient correction family RF-SSPRK(3,3) with stage-weight perturbation vector \((2,-1,-1)\), the existence of an energy-conserving real scalar correction is **not inherited under orthogonal direct sums**: two harmonic oscillator modes, each of which separately admits an energy-conserving correction, may have no correction when excited together. This phenomenon already occurs in four real dimensions. Here is a complete phase classification of one explicit example.

Let \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), \(K=\operatorname{diag}(J,\sqrt7J)\), and solve \(u'(t)=Ku(t)\) with step length \(h=1\). Write \(u=(u^{(1)},u^{(2)})\), assume \(\|u\|_2=1\), and set \(w=\|u^{(1)}\|_2^2\in[0,1]\). Define

\[
w_-=\frac{2415-7\sqrt{7409}}{3072},\qquad
w_+=\frac{2415+7\sqrt{7409}}{3072}.
\]

Exactly when \(w\in[0,w_-]\cup[w_+,1]\), there is at least one real coefficient perturbation \(\varepsilon\) preserving the original squared Euclidean energy at this step. At the two boundary fractions the real coefficient is unique (a double root); in the open interval \((w_-,w_+)\), **every real coefficient strictly increases squared energy**, so the energy-preserving correction does not exist. Numerically, \(w_-\approx0.5900\) and \(w_+\approx0.9823\).

Both pure modes \(w=0\) and \(w=1\) separately admit real corrections. In particular, at the rational mixture \(w=2/3\), the exact squared-energy change is

\[
\|u_+\|_2^2-\|u\|_2^2
=\frac{727}{16}\varepsilon^2-\frac{211}{12}\varepsilon+\frac{16}{9}
\ge\frac{223}{2908}>0
\quad\text{for every }\varepsilon\in\mathbb R.
\]

The minimum occurs at \(\varepsilon=422/2181\). All claims hold for *every* choice of phases of the two modes having the stated energies, not just aligned coordinates.

## Assumptions and scope

Consider the standard explicit three-stage SSPRK(3,3) method in its Runge--Kutta form, with stage values
\[
Y_1=u,\quad F_1=KY_1,\quad
Y_2=u+F_1,\quad F_2=KY_2,\quad
Y_3=u+\tfrac14(F_1+F_2),\quad F_3=KY_3.
\]
Its original endpoint weights are \(b=(1/6,1/6,2/3)\). We vary **only** the endpoint weights, keeping the stages, step size, and real operator fixed:
\[
u_+(\varepsilon)=u+\left(\tfrac16+2\varepsilon\right)F_1
+\left(\tfrac16-\varepsilon\right)F_2
+\left(\tfrac23-\varepsilon\right)F_3,
\quad\varepsilon\in\mathbb R.
\]
The perturbation vector \((2,-1,-1)\) is the one used for RF-SSPRK(3,3) by Najafian and Vermeire [1]. We impose no nonnegativity condition on the perturbed weights; permitting *all* real \(\varepsilon\) makes the impossibility assertion stronger. The initial vector is any nonzero state; normalizing its squared norm to one merely removes a positive common scale factor. The exact system conserves \(\|u(t)\|_2^2\) because \(K\) is skew-symmetric.

This is a single-step feasibility theorem. It does not concern separate correction parameters per mode, changes to the step size, unrelated projection directions, or arbitrary Runge--Kutta families.

## Proof

**1. Endpoint multiplier.** For a linear equation \(u'=Ku\), the stated stages are
\[
Y_1=u,\qquad Y_2=(I+K)u,\qquad
Y_3=(I+\tfrac12K+\tfrac14K^2)u.
\]
Substitution into the variable endpoint weights yields \(u_+(\varepsilon)=R_\varepsilon(K)u\), where the *exact* stability polynomial is
\[
R_\varepsilon(z)=1+z+
\left(\tfrac12-\tfrac32\varepsilon\right)z^2+
\left(\tfrac16-\tfrac14\varepsilon\right)z^3.
\]

**2. One oscillator's exact defect.** For a real planar skew rotation with squared frequency \(r>0\), complexification (or the identity \(J^2=-I\)) gives
\[
R_\varepsilon(i\sqrt r)
=1-\left(\tfrac12-\tfrac32\varepsilon\right)r
+i\sqrt r\left[1-\left(\tfrac16-\tfrac14\varepsilon\right)r\right].
\]
Consequently \(\|R_\varepsilon(\sqrt rJ)v\|_2^2-\|v\|_2^2
=\|v\|_2^2Q_r(\varepsilon)\), with
\[
Q_r(\varepsilon)=
\left(\tfrac94r^2+\tfrac1{16}r^3\right)\varepsilon^2
+\left(3r-r^2-\tfrac1{12}r^3\right)\varepsilon
-\tfrac1{12}r^2+\tfrac1{36}r^3.
\]
This expansion is an identity for every positive \(r\) and every real \(\varepsilon\).

**3. Separate feasibility, mixture obstruction.** At \(r=1\) and \(r=7\), respectively,
\[
Q_1(\varepsilon)=\tfrac{37}{16}\varepsilon^2+\tfrac{23}{12}\varepsilon-\tfrac1{18},
\qquad
Q_7(\varepsilon)=\tfrac{2107}{16}\varepsilon^2-\tfrac{679}{12}\varepsilon+\tfrac{49}{9}.
\]
Their discriminants, with the conventional definition \(\Delta=B^2-4AC\), are \(67/16>0\) and \(5341/16>0\). Thus each single-mode quadratic has real zeros.

Because the blocks are orthogonal and the endpoint multiplier is a polynomial in their block-diagonal generator, the total energy defect is exactly the convex combination
\[
Q_w(\varepsilon)=wQ_1(\varepsilon)+(1-w)Q_7(\varepsilon)
=\frac{2107-2070w}{16}\varepsilon^2
+\frac{702w-679}{12}\varepsilon
+\frac{98-99w}{18}.
\]
Its leading coefficient is strictly positive throughout \(0\le w\le1\), and its exact discriminant is
\[
\Delta(w)=\frac{9216w^2-14490w+5341}{16}.
\]
Solving the quadratic equation \(\Delta(w)=0\) gives precisely \(w_-,w_+\) stated above. The inequalities \(0<w_-<w_+<1\) follow, for example, by squaring the rational bounds on \(\sqrt{7409}\). Since the discriminant is positive outside the open interval and negative inside it, a real root of \(Q_w\) exists if and only if \(w\in[0,w_-]\cup[w_+,1]\). When the discriminant is negative, the positive quadratic has positive minimum \(-\Delta(w)/(4A(w))\), giving strict energy increase for all \(\varepsilon\). At the endpoints the discriminant vanishes and there is one repeated real root.

**4. Rational strict certificate.** Substituting \(w=2/3\) gives \(Q_{2/3}(\varepsilon)=727\varepsilon^2/16-211\varepsilon/12+16/9\), whose discriminant is \(-223/16\). Completing the square proves
\[
Q_{2/3}(\varepsilon)=
\frac{727}{16}\left(\varepsilon-\frac{422}{2181}\right)^2+
\frac{223}{2908}.
\]
All arguments are algebraic and apply to the continuum of real correction parameters and mode phases. In particular a finite experiment is not used to infer the universal claim.

## Verification

Run `python3 verify.py` with Python 3 standard library. It performs exact rational-arithmetic reconstruction of the SSPRK(3,3) polynomial, both single-mode defect polynomials and discriminants, the entire mixed discriminant polynomial (identified by three evaluations because its degree is at most two), and the strict rational certificate at \(w=2/3\). It also cross-checks the energy formula against 54 direct four-dimensional stage calculations with floating-point oscillator coefficients. The expected terminal marker is `VERIFY_OK exact stage polynomial, two mode certificates, quadratic frontier identity, 54 direct 4D runs`. The direct numerical checks are corroborative only; the algebra above proves the statements for all parameters in their stated domain.

## Relationship to prior work

Najafian and Vermeire [1, §§2.3, 3--4] introduce the relaxation-free endpoint-weight correction, specify the perturbation vector \((2,-1,-1)\) for SSPRK(3,3), derive a general quadratic feasibility discriminant, and prove existence for sufficiently small time steps. They also report that correction failure can arise at larger time steps. Those established contributions are not claimed here. What is established here is a complete *two-mode energy-fraction phase diagram* for the exact specified RF-SSPRK(3,3) family, showing the distinct noninheritance phenomenon: two individually correctable, different-frequency oscillators can become uncorrectable as an orthogonal direct sum.

The same authors' quasi-orthogonal projection method [2] employs a different correction direction and is not constrained to the fixed one-dimensional perturbation \((2,-1,-1)\). Bencomo and Chan's analysis [3] treats relaxation of the effective step size and discrete adjoints rather than this fixed-step endpoint-weight family. Earlier results for another SSPRK order or for ordinary fixed-weight stability polynomials do not imply the sign classification of \(\Delta(w)\) here without a separate calculation. No global novelty guarantee is asserted; an equivalent statement could appear under another formulation.

## Limitations

The example uses exactly two planar frequencies \(1\) and \(\sqrt7\), step size one, exact stage evaluations, and the particular fixed perturbation vector \((2,-1,-1)\). The claim is not a failure of all possible energy-preserving integrators, does not contradict the small-step existence statement in [1], and does not establish instability or long-time dynamics after a step for which the correction is infeasible. The numeric threshold is an exact statement about this example, not a universal critical energy ratio. Novelty is subject to independent priority verification.

## References

[1] M. R. Najafian and B. C. Vermeire, *Energy Conservative Relaxation-Free Runge-Kutta Schemes*, arXiv:2401.14508v1 (first public version 2024-01-25), §§2.3, 3--4. https://arxiv.org/abs/2401.14508

[2] M. R. Najafian and B. C. Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods*, arXiv:2409.18328v1 (2024-09-26), §§1--2. https://arxiv.org/abs/2409.18328

[3] M. J. Bencomo and J. Chan, *Discrete adjoint computations for relaxation Runge-Kutta methods*, arXiv:2107.11408v1 (2021-07-23), §§1--2. https://arxiv.org/abs/2107.11408
