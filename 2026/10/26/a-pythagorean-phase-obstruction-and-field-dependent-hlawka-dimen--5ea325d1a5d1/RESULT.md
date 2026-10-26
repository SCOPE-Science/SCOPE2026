# A Pythagorean phase obstruction and field-dependent Hlawka dimensions

## Finding

Write \(\mathbb K\in\{\mathbb R,\mathbb C\}\) and let \(\ell_p^n(\mathbb K)\) carry the usual coordinate norm. A normed space has the **Hornich–Hlawka property** when
\[
\|x\|+\|y\|+\|z\|+\|x+y+z\|\geq\|x+y\|+\|y+z\|+\|z+x\|
\]
for every triple. Let \(q\in(3,4)\) be the unique real solution of
\[
3\,2^{1/q}+(3^q+4^q)^{1/q}=8
\]
(\(q=3.572346330821\ldots\)). For **each** \(p\in(q,\infty]\) and positive integer \(n\), the exact minimum coordinate dimension of failure is different over the two scalar fields:
\[
\ell_p^n(\mathbb C)\text{ has the Hornich–Hlawka property}\iff n=1,
\qquad
\ell_p^n(\mathbb R)\text{ has the property}\iff n\leq2.
\]
The complex two-coordinate obstruction is witnessed by
\[
x=(1,1),\qquad y=(1,-1),\qquad z=(-1,4i/3).
\]
For finite \(p\), its signed Hornich–Hlawka gap (left minus right) is exactly
\[
\frac23\left(3\,2^{1/p}+(3^p+4^p)^{1/p}-8\right).
\]
It is strictly negative exactly for \(p>q\), zero for this witness at \(p=q\), and tends to \(-2/3\) as \(p\to\infty\). **The threshold \(q\) is sharp for this explicitly specified Pythagorean witness, not asserted to be the first exponent at which the complex space fails.**

There is also a phase-rigidity statement: with the first two vectors fixed and \(z=(-1,t e^{i\theta})\), for each fixed \(t>0\) and every \(p\), the Hornich–Hlawka gap is minimized precisely when \(e^{i\theta}=\pm i\). Thus the imaginary phase in the witness is an exact optimizer within its fixed-amplitude family, not a fortuitous numerical choice.

## Assumptions and scope

All exponents \(p\in(q,\infty)\) are real, and \(p=\infty\) uses the coordinate maximum norm. The statements apply to every finite integer \(n\geq1\) and the indicated real or complex scalar field. A complex space is considered with its usual norm; the inequality itself depends only on the underlying real normed space. No assertion is made for complex exponents \(p\leq q\), nor is \(q\) claimed to be globally optimal across all triples. The cited contemporary \(\ell_p\) results explicitly concern the **real** field; the new phase obstruction concerns **complex** coordinates.

## Proof

**1. Existence and exact meaning of \(q\).** Define, for finite \(p>0\),
\[
A(p)=3\,2^{1/p}+(3^p+4^p)^{1/p}.
\]
Both terms are strictly decreasing in \(p\): they are ordinary \(\ell_p\) norms of fixed vectors having two positive entries (the first term is \(3\|(1,1)\|_p\)). In particular, \(A\) is continuous and strictly decreasing. At \(p=3\),
\[
A(3)=3\sqrt[3]2+\sqrt[3]{91}>3\cdot\frac54+\frac{17}4=8,
\]
because \(2>(5/4)^3\) and \(91>(17/4)^3\). At \(p=4\),
\[
A(4)=3\sqrt[4]2+\sqrt[4]{337}<3\cdot\frac65+\frac{22}5=8,
\]
because \(2<(6/5)^4\) and \(337<(22/5)^4\). Therefore a unique \(q\in(3,4)\) satisfies \(A(q)=8\). Moreover \(A(\infty)=3+4=7\).

**2. Exact complex obstruction.** With the displayed \(x,y,z\), the sums are
\[
x+y=(2,0),\quad x+z=(0,1+4i/3),\quad y+z=(0,-1+4i/3),\quad x+y+z=(1,4i/3).
\]
The two singleton norms \(\|x\|_p,\|y\|_p\) equal \(2^{1/p}\); the other two norms \(\|z\|_p,\|x+y+z\|_p\) equal \((3^p+4^p)^{1/p}/3\). The three pair norms are \(2,5/3,5/3\), using the Pythagorean identity \(|3\pm4i|=5\). Subtracting the right side from the left side gives precisely \(2(A(p)-8)/3\), which is negative for \(p>q\). The limiting computation gives \(-2/3\) for \(p=\infty\). Appending zero coordinates preserves all seven norms, so the violation occurs in each complex dimension \(n\ge2\).

**3. Phase optimality.** Keep \(x,y\) fixed and let \(z=(-1,t e^{i\theta})\) for a prescribed \(t>0\). The four norms on the left and \(\|x+y\|=2\) are independent of \(\theta\). For the remaining pair norms, write \(a=|1+t e^{i\theta}|\) and \(b=|-1+t e^{i\theta}|\). As \(a^2+b^2=2(1+t^2)\), Cauchy–Schwarz gives \(a+b\leq2\sqrt{1+t^2}\), with equality exactly when \(a=b\), or \(\cos\theta=0\). Those and only those two phases minimize the signed gap. This argument is independent of \(p\).

**4. The dimensions which retain the property.** The one-coordinate complex space is the real two-dimensional Euclidean plane, so its norm satisfies Hornich–Hlawka (as does a one-coordinate real space). Every real normed plane has the property: every centrally symmetric planar convex body is a zonoid, so a real planar norm is a limit of sums of absolute real linear functionals; the scalar Hornich–Hlawka inequality passes through sums and uniform limits. In particular \(\ell_p^2(\mathbb R)\) has the property for every \(p\).

For \(n\ge3\), take the real triple
\[
u=(-1,1,1),\qquad v=(1,-1,1),\qquad w=(1,1,-1).
\]
It has signed gap \(4\,3^{1/p}-6\), negative for \(p>p_0=\log3/\log(3/2)\). We have \(p_0<3<q\), since \((3/2)^3>3\). Zero padding gives a violation in every real dimension \(n\ge3\). The same conclusion at \(p=\infty\) follows by taking the limit. This completes both exact coordinate-dimension classifications.

## Verification

The equalities in the seven norm expressions are symbolic and apply for every permitted exponent. The inequalities \(A(3)>8>A(4)\) have elementary rational-power certificates in Step 1; continuity and strict monotonicity establish the unique threshold without reliance on approximate root finding. The auxiliary standalone file `CHECK.py` independently computes the seven norms for representative exponents, checks the equivalent gap formula, brackets \(q\), and tests the endpoint \(p=\infty\). Those finite tests are **not** a substitute for the universal proof.

## Relationship to prior work

Seokbin Lee, *Constructions and reductions on the Hornich–Hlawka inequality and its generalizations* (arXiv:2610.23785v1, first posted 2026-10-16), explicitly defines the investigated \(\ell_p(N)\) spaces over \(\mathbb R\) and records the classical real-plane positive result and the negative three-real-coordinate witness beyond \(p_0\). Those facts are used and credited here, not presented as new. The new contribution is the explicit **two-complex-coordinate** obstruction with its phase optimization and resulting sharp coordinate-dimension contrast over a nontrivial entire exponent interval.

The earlier study *A New Look at the Hornich–Hlawka Inequality* (Results in Mathematics, 2025) likewise discusses the real \(\ell_p(3)\) witness; it does not establish this complex two-coordinate phase obstruction. Research on dimensional Hlawka constants for complex diagonal Schatten operators, including E. Esa's 2026 work, gives bounds and sharp constants in different dimension/exponent regimes, but the inspected main results do not state this two-complex-coordinate onset. A result in older work under the equivalent term *quadrilateral inequality*, or a stronger general theorem not identified here, remains a possible historical-priority issue.

## Limitations

The precise global critical exponent for failure of Hornich–Hlawka on \(\ell_p^2(\mathbb C)\) is **not determined**. The number \(q\) optimizes the exponent for the named Pythagorean triple only; the imaginary phase is optimal among all phases at each **fixed** amplitude, but the amplitude \(4/3\) is not proved globally optimal. The proof shows exact minimum failure dimensions only for \(p>q\). No claim is made of independent verification or exhaustive historical priority.

## References

1. S. Lee, *Constructions and reductions on the Hornich–Hlawka inequality and its generalizations*, arXiv:2610.23785v1 (2026-10-16). https://arxiv.org/html/2610.23785v1
2. D.-Ş. Marinescu and C. P. Niculescu, *A New Look at the Hornich–Hlawka Inequality*, Results in Mathematics (2025). https://doi.org/10.1007/s00025-025-02464-9
3. E. Esa, *Dimension-independent Hlawka constants for Schatten norms*, 2026, public research repository. https://github.com/savarin/hlawka-schatten
