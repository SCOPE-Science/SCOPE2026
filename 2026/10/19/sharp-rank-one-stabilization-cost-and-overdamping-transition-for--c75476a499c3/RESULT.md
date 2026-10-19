# Sharp rank-one stabilization cost and overdamping transition for a planar rotating mode

## Finding

Fix real parameters \(a>0\), \(\delta\geq0\), and \(b\geq0\), and let \(\alpha=a+\delta\),
\[
A=aI_2+bJ,\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
The minimum Frobenius norm of a real correction \(\Delta\) whose perturbed matrix has all eigenvalues in \(\{z:\operatorname{Re}z\leq-\delta\}\) is \(\sqrt2\,\alpha\) without a rank restriction. For corrections of rank at most one, the exact minimum is
\[
d_1(\alpha,b)=\begin{cases}
+\infty,&b=0,\\
(\alpha^2+b^2)/b,&0<b<\alpha,\\
2\alpha,&b\geq\alpha.
\end{cases}
\]
For positive rotation below the threshold \(b=\alpha\), every minimum-norm rank-one correction is oblique (nonsymmetric), and the shifted closed-loop matrix is a nonzero nilpotent with a defective double zero eigenvalue. At and above that threshold the minimum-norm corrections are precisely the negative semidefinite symmetric rank-one matrices \(-2\alpha uu^{\mathsf T}\), with \(\|u\|_2=1\). At \(b>\alpha\) the shifted closed-loop matrix has imaginary eigenvalues \(\pm i\sqrt{b^2-\alpha^2}\). Hence the optimal geometry changes sharply at the rotation-to-growth ratio \(b/\alpha=1\).

If corrections are *required* to be negative semidefinite and symmetric of rank at most one, the admissible correction amplitudes are exactly
\[
\Delta=-tuu^{\mathsf T},\quad \|u\|_2=1,\quad
2\alpha\leq t\leq\frac{\alpha^2+b^2}{\alpha};
\]
this interval is nonempty precisely when \(b\geq\alpha\). Strict inequality \(\operatorname{Re}\sigma(A+\Delta)<-\delta\) is possible in this passive subclass precisely when \(b>\alpha\), with both inequalities on \(t\) strict. Above the upper amplitude endpoint, the determinant becomes negative and overdamping reintroduces instability.

For strictly shifted-Hurwitz matrices, the *infima* of correction norms in the unrestricted and arbitrary rank-one classes equal their respective closed-margin minima, but they are not attained. In the passive rank-one class the strict-stability infimum is \(2\alpha\) for \(b>\alpha\), and feasibility fails for \(b\leq\alpha\).

## Assumptions and scope

All matrices, correction factors and feedback directions are real. The matrix \(A\) is the two-dimensional rotation–dilation generator, \(a>0\), \(b\geq0\), \(\delta\geq0\). Corrections are additive, their costs use the Frobenius norm, and rank constraints mean *rank at most one*. The weak spectral margin permits eigenvalues on the line \(\operatorname{Re}z=-\delta\). Strict spectral margin does not. The passive subclass consists only of \(-tuu^{\mathsf T}\) with \(t\geq0\) and \(\|u\|_2=1\); arbitrary real rank-one corrections are not presumed symmetric. Neither the actuator nor the sensor is prescribed in the rank-one class.

The result is a complete classification for this specified two-by-two family, not a theorem for every normal matrix, a second-order gyroscopic pencil, or fixed-actuator feedback. Its numerical-optimization interpretation is a closed-form benchmark for low-rank matrix-nearness and regional eigenvalue assignment with variable rank-one directions.

## Proof

**Reduction to trace and determinant.** Shifting by the desired margin gives \(C=A+\Delta+\delta I_2=\alpha I_2+bJ+\Delta\). A real two-by-two matrix has spectrum in the closed left half-plane if and only if \(\operatorname{tr}C\leq0\) and \(\det C\geq0\). For the open left half-plane these two inequalities must both be strict (quadratic Routh–Hurwitz criterion). The first assertion follows by inspecting the real or complex-conjugate roots of the characteristic polynomial; conversely the inequalities force both real roots to be nonpositive, or force the real part of a conjugate pair to be nonpositive.

**Unrestricted minimum.** The trace condition implies \(\operatorname{tr}\Delta\leq-2\alpha\), and Frobenius Cauchy–Schwarz gives
\[
\|\Delta\|_F\geq\frac{|\operatorname{tr}\Delta|}{\sqrt2}\geq\sqrt2\,\alpha.
\]
The correction \(\Delta=-\alpha I_2\) attains equality and yields \(C=bJ\), whose spectrum is imaginary. Equality in Cauchy–Schwarz forces \(\Delta\) to be a scalar multiple of \(I_2\), so this is the unique unrestricted minimizer.

**Arbitrary rank-one corrections.** Write \(\Delta=uv^{\mathsf T}\), with \(u,v\in\mathbb R^2\), and introduce
\[
p=v^{\mathsf T}u,\qquad q=v^{\mathsf T}Ju,\qquad t=\|uv^{\mathsf T}\|_F.
\]
Since \(u\) and \(Ju\) are orthogonal and have equal norm, the planar Pythagorean identity gives \(p^2+q^2=t^2\). The rank-one determinant lemma, or direct expansion, gives
\[
\operatorname{tr}C=2\alpha+p,\qquad
\det C=\alpha^2+b^2+\alpha p-bq.
\]
Thus the trace condition forces \(p\leq-2\alpha\), and therefore \(t\geq2\alpha\). For \(b=0\), the matrix \(C=\alpha I_2+uv^{\mathsf T}\) has the positive eigenvalue \(\alpha\) (the one-dimensional kernel of \(v^{\mathsf T}\) is invariant); no rank-one stabilization exists.

Let \(b>0\). For a fixed \(t\geq2\alpha\), all feasible values of \(p\) are within \([-t,-2\alpha]\). The maximal determinant over corresponding \(q\), at a fixed \(p\), occurs at \(q=-\sqrt{t^2-p^2}\). Its value is
\[
F_t(p)=\alpha^2+b^2+\alpha p+b\sqrt{t^2-p^2}.
\]
For \(-t<p\leq-2\alpha\), its derivative is \(\alpha-bp/\sqrt{t^2-p^2}>0\), so its maximum over the entire permissible interval occurs at \(p=-2\alpha\). Consequently, feasibility at norm \(t\) is equivalent to
\[
b^2-\alpha^2+b\sqrt{t^2-4\alpha^2}\geq0.
\]
For \(b\geq\alpha\) this holds at \(t=2\alpha\), the smallest permitted norm. For \(0<b<\alpha\), it first holds when
\[
t^2=4\alpha^2+\frac{(\alpha^2-b^2)^2}{b^2}
=\frac{(\alpha^2+b^2)^2}{b^2}.
\]
This proves the stated formula globally, not merely as a stationary condition.

**Attainment, geometry and eigenvalues.** For \(0<b<\alpha\), put \(u=e_1\) and
\[
v=\begin{pmatrix}-2\alpha\\-(\alpha^2-b^2)/b\end{pmatrix}.
\]
Then \(\Delta=uv^{\mathsf T}\) has the claimed norm and
\[
C=\begin{pmatrix}-\alpha&-\alpha^2/b\\b&\alpha\end{pmatrix},
\quad \operatorname{tr}C=\det C=0,
\quad C\ne0.
\]
Cayley–Hamilton therefore gives \(C^2=0\), so \(C\) is a nonzero defective nilpotent. Every minimizer has \(p=-2\alpha\) and \(q=-(\alpha^2-b^2)/b\), because the determinant maximum must vanish at the optimal norm. Hence every minimizer is obtained by taking any unit vector \(u\) and choosing \(v=-2\alpha u-((\alpha^2-b^2)/b)Ju\); in particular it is nonsymmetric.

For \(b\geq\alpha\), equality at \(t=2\alpha\) forces \(p=-2\alpha\), \(q=0\), hence \(\Delta=-2\alpha uu^{\mathsf T}\) for some unit \(u\). With \(u=e_1\), its shifted matrix has trace zero and determinant \(b^2-\alpha^2\). At equality \(b=\alpha\) it is nonzero nilpotent, and when \(b>\alpha\) its eigenvalues are \(\pm i\sqrt{b^2-\alpha^2}\). Rotation of the unit vector preserves those spectral conclusions.

**Symmetric dissipative rank one and overdamping.** For \(\Delta=-tuu^{\mathsf T}\), the spectral invariants do not depend on \(u\):
\[
\operatorname{tr}C=2\alpha-t,
\qquad \det C=\alpha^2+b^2-\alpha t.
\]
Applying the two closed (respectively, strict) Routh–Hurwitz inequalities proves both the complete interval and the strict-stability classification. In particular, once \(t>(\alpha^2+b^2)/\alpha\), the determinant is negative: the shifted matrix has one positive and one negative real eigenvalue even though additional damping has been applied.

**Strict spectral margin.** For each \(b>0\) the closed-margin rank-one minimizer is approachable by strictly stable rank-one matrices. For \(0<b<\alpha\), let \(q_0=-(\alpha^2-b^2)/b\) and choose \(\Delta_\varepsilon=e_1(-2\alpha-\varepsilon,\;q_0-(\alpha/b+1)\varepsilon)\) with \(\varepsilon>0\). Its shifted trace equals \(-\varepsilon\) and determinant equals \(b\varepsilon>0\), while its Frobenius norm tends to the closed-margin optimum. For \(b\geq\alpha\), choose \(\Delta_\varepsilon=e_1(-2\alpha-\varepsilon,\;-(\alpha/b+1)\varepsilon)\); its shifted trace is \(-\varepsilon\) and determinant is \(b^2-\alpha^2+b\varepsilon>0\), with norm tending to \(2\alpha\). No strict-stability minimizer exists at the boundary cost, since the rank-one lower-bound argument forces trace zero (or determinant zero). Similarly \(- (\alpha+\varepsilon)I_2\) proves the strict-unrestricted infimum. The passive strictly stable interval was already determined.

## Verification

`VERIFY.py` is a standalone Python 3 standard-library checker of 39,823 exact-rational assertions. It checks the rank-one Pythagorean and determinant identities against direct matrix arithmetic on an integer lattice, the explicit optimal corrections on a rational parameter grid covering all branches, the defective and oscillatory boundary invariants, positive-trace/negative-determinant obstructions, strict-feasibility perturbations, overdamping beyond the upper endpoint, and the full-rank bound's equality example. The output is `CHECKS_PASSED 39823`. These finite tests independently guard against algebraic and sign errors; the proof above establishes the universal quantifiers. Reproduce with `python3 VERIFY.py` after extracting the files into one directory.

## Relationship to prior work

He and Liu (2024) address rank-one *regional eigenvalue assignment* for a second-order gyroscopic pencil with actuator constraints, an orthogonality-based assignment construction, and sensitivity optimization; they do not state a minimum-Frobenius-cost classification for the first-order real planar rotation–dilation family with free rank-one actuator and sensor. Their paper's primary MSC is 65F18. Guglielmi and Sicilia (2024) describe a low rank-adaptive differential-equation approach to computing small matrix-stabilizing perturbations and illustrate it on larger test matrices, rather than giving the exact scalar-parameter formula derived here. Guglielmi and Lubich (2017) introduce norm-nearest matrix stabilization with maximal-rank and other constraints; their published abstract covers the *general problem class* but supplies no matching closed-form planar rank-one profile. Its full text was not accessible for this assessment, so possible equivalent formulations remain an originality risk. The elementary two-by-two Routh–Hurwitz condition, matrix determinant lemma and Frobenius Cauchy–Schwarz inequality are standard tools, not claimed as new.

## Limitations

The formula is only for the specified real normal two-by-two rotation–dilation family and freely oriented real additive corrections. It does not handle fixed actuators, complex rank-one factors, arbitrary nonnormal systems, higher dimensions or eigenvalue-conditioning objectives. Most minimum-norm corrections lie on the spectral boundary and are not strictly Hurwitz; in the weak-rotation regime the minimizer is defective and can be highly sensitive. The method does not imply numerical robustness of its optimal perturbations or guarantee an achievable strict-margin minimum. Potential unlocated equivalent exact formulas in earlier structured-nearness or control literature cannot be excluded without independent full-text evaluation.

## References

1. B. He and H. Liu, “A robust regional eigenvalue assignment problem using rank-one control for undamped gyroscopic systems,” *AIMS Mathematics* **9** (2024), 19104–19124, DOI: 10.3934/math.2024931, published June 7, 2024. Full open text: https://www.aimspress.com/aimspress-data/math/2024/7/PDF/math-09-07-931.pdf .
2. N. Guglielmi and S. Sicilia, “Stabilization of a matrix via a low rank-adaptive ODE,” arXiv:2402.14657v1, first submitted February 22, 2024. Full text: https://arxiv.org/html/2402.14657v1 .
3. N. Guglielmi and C. Lubich, “Matrix Stabilization Using Differential Equations,” *SIAM Journal on Numerical Analysis* **55** (2017), 3097–3119, DOI: 10.1137/16M1105840. Abstract available: https://epubs.siam.org/doi/10.1137/16M1105840 .
