# A divisor-sum census of smooth Markov partitions for quadratic companion toral maps

## Finding
Let \(H\ge 2\) be an integer. For integers \(t,d\) with \(|t|\le H\) and \(|d|\le H\), define
\[
 A_{t,d}=\begin{pmatrix}0&-d\\1&t\end{pmatrix},\qquad
 f_{t,d}:\mathbb T^2\longrightarrow\mathbb T^2,\quad x\longmapsto A_{t,d}x\pmod{\mathbb Z^2}.
\]
Call \((t,d)\) *expanding* when both eigenvalues of \(A_{t,d}\) have modulus strictly greater than one, and *smooth-admissible* when, additionally, \(f_{t,d}\) admits a finite Markov partition whose boundary is piecewise \(C^1\) in the sense of Hughes and de Jong [HDJ]. Write \(E(H)\) for the number of expanding pairs in the box and \(N(H)\) for the number of smooth-admissible pairs. Put \(D(H)=\sum_{j=1}^H\lfloor H/j\rfloor\).

**Theorem (exact arithmetic prevalence).** For every integer \(H\ge2\),
\[
 \boxed{E(H)=2H^2-2},\qquad
 \boxed{N(H)=2D(H)-2H+2\left\lfloor\sqrt{H/2}\right\rfloor+2\left\lfloor\sqrt{H/3}\right\rfloor}.
\]
Consequently, with \(\gamma\) Euler's constant,
\[
 N(H)=2H\log H+(4\gamma-4)H+O(\sqrt H)
\]
and the proportion of expanding companion maps that admit a smooth Markov partition equals
\[
 \boxed{\frac{N(H)}{E(H)}=\frac{\log H+2\gamma-2}{H}+O(H^{-3/2})}.
\]
Every smooth Markov partition counted here can be taken piecewise linear by [HDJ]. The theorem counts distinct integer trace-determinant pairs in a canonical companion family, **not** all integer matrices ordered by the sizes of their individual entries.

## Assumptions and scope
The matrix \(A_{t,d}\) has characteristic polynomial \(z^2-tz+d\). Because \(A_{t,d}\) is a companion matrix, its minimal polynomial equals this characteristic polynomial. Thus a double eigenvalue yields a nontrivial Jordan block, whereas distinct eigenvalues are diagonalizable over \(\mathbb C\). We use the published theorem of Hughes and de Jong [HDJ, Theorem 1.2] that an expanding integral toral endomorphism admits a smooth Markov partition exactly when some positive matrix power is diagonalizable and has integer eigenvalues. Their proof and theorem are pre-existing inputs; the exact height enumeration and its density are the findings here.

The parameter \(H\) is integer; no statement is made about a bound on individual matrix entries or about dimension greater than two. Boundaries with a nonzero eigenvalue of modulus exactly one are excluded, as are all nonexpanding pairs. The box is symmetric in the two conjugacy invariants \(t=\operatorname{tr}A\) and \(d=\det A\), with \(H\) imposing the same arithmetic-height cutoff on each.

## Proof
**1. The expanding population.** Reciprocal eigenvalues of \(A_{t,d}\) are roots of \(z^2-(t/d)z+1/d\) when \(d\ne0\). The elementary quadratic Schur criterion (roots strictly inside the unit circle) reduces here to \(|d|>1\) and
\[
 d\ge2:\ |t|<d+1;\qquad d\le-2:\ |t|<-d-1.
\]
For integer \(t,d\), these become respectively \(|t|\le d\) and \(|t|\le |d|-2\). Both bounds are at most \(H\) inside the stated height box. Therefore
\[
 E(H)=\sum_{d=2}^H(2d+1)+\sum_{m=2}^H(2m-3)=2H^2-2.
\]
In particular, a zero determinant, a determinant of modulus one, and all unit-circle boundary cases contribute nothing.

**2. Exhaustion of spectral possibilities.** For an expanding companion matrix with distinct eigenvalues, the criterion [HDJ] is equivalent to the existence of \(n\ge1\) such that *both* eigenvalues raised to \(n\) are integers. If its characteristic polynomial splits over \(\mathbb Q\), the two eigenvalues are algebraic integers and rational, hence ordinary integers \(a,b\), and expansion means \(|a|,|b|\ge2\), with \(a\ne b\).

If the characteristic polynomial is irreducible over \(\mathbb Q\), its two roots \(\lambda,\lambda'\) are conjugate. If one has integer \(n\)-th power, Galois conjugation forces \(\lambda^n=(\lambda')^n\). Their ratio is a root of unity. If the roots are real and distinct, their ratio is \(-1\), so \(t=0\). If they are nonreal, then \(d>0\), \(\lambda=\sqrt d\,e^{i\theta}\), and \(\lambda/\lambda'=e^{2i\theta}\) is a root of unity. Because \(2\cos(2\theta)=t^2/d-2\) is both rational and an algebraic integer, it is an integer in \([-2,2]\). Thus \(t^2/d\) must be \(0,1,2,3,\) or \(4\). The last case is a double root and impossible for a smooth-admissible companion matrix. In the other cases either \(t=0\), or
\[
 t^2=d,\qquad t^2=2d,\qquad t^2=3d.
\]
Conversely, \(t=0\) gives \(\lambda^2=-d\in\mathbb Z\); \(t^2=d\) gives \(\lambda^6=d^3\in\mathbb Z\); \(t^2=2d\) gives \(\lambda^4=-d^2\in\mathbb Z\); and \(t^2=3d\) gives \(\lambda^6=-d^3\in\mathbb Z\). All these polynomial families have distinct roots if \(d\ne0\). Under expansion the necessary restrictions are \(|d|\ge2\). Therefore the above classes, together with the distinct integer-root class, are exhaustive and sufficient.

**3. Exact count, including overlaps.** Define \(h=\lfloor\sqrt H\rfloor\), \(u_2=\lfloor\sqrt{H/2}\rfloor\) and \(u_3=\lfloor\sqrt{H/3}\rfloor\). Set
\[
 Q(H)=\#\{(a,b)\in\mathbb Z_{\ge2}^2:ab\le H\}=D(H)-2H+1.
\]
Every pair \(|a|,|b|\ge2\) of integer eigenvalues with \(|ab|\le H\) also satisfies \(|a+b|\le|ab|\le H\). There are \(4Q(H)\) *ordered signed* pairs. Removing the \(2(h-1)\) equal-sign diagonal pairs \(a=b\), which would give non-diagonalizable companion matrices, and quotienting the remaining pairs by their free swap action yields \(2Q(H)-(h-1)\) smooth-admissible companion matrices with two distinct integer eigenvalues.

The line \(t=0\) contributes \(2(H-1)\) expanding pairs \((0,d)\), with \(2\le|d|\le H\). It overlaps the preceding class exactly when \(d=-a^2\), \(2\le a\le h\), so its new contribution is \(2(H-1)-(h-1)\).

For the three remaining nonreal families, \(t^2=d\) has exactly \(2(h-1)\) solutions (since \(d>1\)); \(t^2=2d\) has \(2u_2\) solutions, parametrized by \((t,d)=(\pm2j,2j^2)\); and \(t^2=3d\) has \(2u_3\) solutions, parametrized by \((\pm3j,3j^2)\). These families are mutually disjoint and disjoint from both the integer-eigenvalue and \(t=0\) classes. Their traces satisfy \(|t|\le H\) whenever \(|d|\le H\) and \(H\ge2\). Summation gives the exact cancellation
\[
 \begin{aligned}
 N(H)&=[2Q(H)-(h-1)]+[2(H-1)-(h-1)]\\
 &\quad+[2(h-1)+2u_2+2u_3]\\
 &=2D(H)-2H+2u_2+2u_3.
 \end{aligned}
\]
This calculation explicitly removes the repeated-eigenvalue obstruction and every class overlap; counting only integral eigenvalue powers without diagonalizability would be incorrect.

**4. Asymptotic.** The elementary Dirichlet hyperbola identity
\[
 D(H)=2\sum_{j\le\sqrt H}\lfloor H/j\rfloor-\lfloor\sqrt H\rfloor^2
\]
and \(\sum_{j\le m}j^{-1}=\log m+\gamma+O(m^{-1})\) give
\(D(H)=H\log H+(2\gamma-1)H+O(\sqrt H)\). Both floor square-root corrections in the exact formula are \(O(\sqrt H)\). Substitution and division by \(2H^2-2\) prove the two stated asymptotics. This completes the proof.

## Verification
The standalone Python 3 script `verify.py` uses only standard-library exact-integer arithmetic. Independently of the spectral classification proved above, it computes traces of matrix powers by the recurrence \(s_0=2\), \(s_1=t\), \(s_n=ts_{n-1}-ds_{n-2}\), and checks whether the discriminant \(s_n^2-4d^n\) is a nonnegative perfect square with the required parity for powers \(n\in\{1,2,3,4,6,12\}\). It separately excludes repeated-root companions and directly enumerates expansion for every trace-determinant box. All heights \(2\le H\le65\) agree with the exact formula and \(E(H)=2H^2-2\). These are finite diagnostics; the proof of the all-height theorem is in the preceding section and does not depend on extrapolation from tests.

## Relationship to prior work
Hughes and de Jong [HDJ] prove the geometric if-and-only-if criterion, linearity of all smooth Markov boundaries, and a finite set of possible exponents in dimension two (their Section 5.2). Those implications and the ordinary divisor summatory asymptotic are prior results. Their stated theorem does not count integer trace-determinant pairs in finite height boxes or give the exact density found here. Cawley's earlier [C] classification concerns hyperbolic toral **automorphisms** (unit determinant), whereas the expanding companions here have \(|d|\ge2\); it does not imply this enumeration. The passage from the geometric criterion to the spectral classification, overlap-aware height count, and exact arithmetic sparsity law is the new contribution. This is a best-knowledge literature comparison, not a claim of independently certified bibliographic priority.

## Limitations
The main input [HDJ] is a published/preprint theorem rather than re-proved here. The theorem counts characteristic-polynomial parameters of canonical companion matrices; it gives no density statement for the much larger space of integral matrices ordered by entry height, nor a uniform bound on the number of partition elements. It neither constructs individual partitions nor measures the fractal dimensions of nonsmooth boundaries. The \(O(\sqrt H)\) error is elementary and not claimed optimal. No independent scientific audit has been performed; an earlier equivalent arithmetic count could exist under different terminology.

## References
[HDJ] C. Hughes and H. de Jong, *Smoothness of Markov Partitions for Expanding Toral Endomorphisms*, arXiv:2604.00257, first public version 31 March 2026, revised version 12 October 2026, Theorems 1.2–1.3 and Section 5.2. Full open-access text: https://arxiv.org/html/2604.00257v2 .

[C] E. Cawley, *Smooth Markov partitions and toral automorphisms*, Ergodic Theory and Dynamical Systems 11 (1991), 633–651, https://doi.org/10.1017/S0143385700006404 .

[DH] The classical Dirichlet hyperbola identity and divisor-summatory estimate, as proved directly above from harmonic sums; no research priority is claimed for these elementary analytic-number-theory ingredients.
