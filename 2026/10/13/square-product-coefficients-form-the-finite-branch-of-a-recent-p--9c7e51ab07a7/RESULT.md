# Square-product coefficients form the finite branch of a recent Pell reduction
## Finding
Let \(a,b,c,n\) be positive integers and suppose \(ab\) is a perfect square. Put \(S=\sqrt{ab}\). Then the integer solutions of
\[
a y^2=b(x^{2n}-c^{2n})
\]
are exactly those obtained from signed factor pairs \(r,s\in\mathbb Z\) with
\[
rs=c^{2n},\qquad r\equiv s\pmod 2,
\]
for which
\[
\frac{r+s}2=x^n
\]
for some \(x\in\mathbb Z\), and
\[
a\mid S\frac{s-r}2.
\]
For each such pair,
\[
y=\frac{S(s-r)}{2a}.
\]
Consequently the entire square-product coefficient regime is finite: before the parity, perfect-power, and divisibility filters there are exactly \(2\tau(c^{2n})\) signed factor-pair candidates.

In Section 3 of Zhuang--Mastorakis, arXiv:2610.00119v1, the square-free part \(t\) of \(ab\) is introduced and the reduction leads to their equation (18),
\[
w^2-tv^2=\frac{2gc^n}d,
\]
with \(g\mid t\). When \(ab\) is a square one has \(t=g=1\), so the auxiliary equation is a difference of two squares. The paper states that a solvable equation (18) has infinitely many integer solutions. That assertion is valid for the genuinely Pellian nonsquare branch \(t>1\), but it fails for \(t=1\), where every nonzero right-hand side has only finitely many solutions.

## Assumptions and scope
All variables \(a,b,c,n\) are positive integers and \(x,y\) are integers. The claim concerns only the even-exponent equation \(a y^2=b(x^{2n}-c^{2n})\) and the natural coefficient boundary \(ab\) square. It does not assess the paper's odd-exponent method or the nonsquare square-free-part branch \(t>1\).

The lead source was first public on 2026-09-09 and is categorized under Number Theory. The mathematical topic is quadratic Diophantine equations, MSC 11D09.

## Proof
Because \(S^2=ab\), every integer solution of the original equation satisfies
\[
\left(\frac{ay}S\right)^2=x^{2n}-c^{2n}\in\mathbb Z.
\]
A rational number whose square is an integer is itself an integer: if \(m/q\) is in lowest terms and \(q^2\mid m^2\), then \(q=1\). Hence
\[
z=\frac{ay}S\in\mathbb Z
\]
and
\[
z^2=x^{2n}-c^{2n}.
\]
Conversely, if \(x,z\in\mathbb Z\) satisfy this equation and \(a\mid Sz\), then \(y=Sz/a\) is integral and recovers a solution of the original equation. Thus this is an exact equivalence, not merely a necessary condition.

Now factor
\[
(x^n-z)(x^n+z)=c^{2n}.
\]
Set \(r=x^n-z\) and \(s=x^n+z\). Then \(rs=c^{2n}\), the two factors have the same parity, and
\[
x^n=\frac{r+s}2,\qquad z=\frac{s-r}2.
\]
The integrality condition \(a\mid Sz\) is exactly \(a\mid S(s-r)/2\). Conversely every signed factor pair satisfying these conditions reconstructs \(x,z,y\), proving the classification.

Since \(c^{2n}>0\), choosing the signed divisor \(r\) determines \(s=c^{2n}/r\). There are exactly \(2\tau(c^{2n})\) choices for signed \(r\), so the search is finite before any filters.

For the boundary in the source's equation (18), \(t=1\) forces \(g=1\), and the auxiliary equation has the form
\[
w^2-v^2=N,\qquad N=\frac{2c^n}d>0.
\]
It factors as \((w-v)(w+v)=N\), hence it is parameterized by finitely many divisor pairs of \(N\). For \(a=b=1,c=3,n=1,d=2\), one gets \(N=3\) and exactly
\[
(w,v)\in\{(2,1),(2,-1),(-2,1),(-2,-1)\}.
\]
The original equation has the corresponding nontrivial solution \((x,y)=(5,4)\), since \(4^2=5^2-3^2\).

## Verification
The standalone verifier exhaustively compares the signed-divisor parametrization of \(w^2-v^2=N\) with direct search for every \(1\le N\le500\). It also compares the full square-product classification above with direct substitution for 96 small coefficient/exponent cases, and checks the \(a=b=1,c=3,n=1\) witness. The proof itself is the exact factorization argument above; finite computation is only a replay check.

## Relationship to prior work
Zhuang--Mastorakis explicitly set \(ab=r^2t\) with \(t\) square-free, derive equation (18), and then state that a solvable equation (18) has infinitely many solutions. Their Section 2 separately gives a finite factorization method for \(z^2=x^{2n}-c^{2n}\). The present finding identifies the omitted interface between those two parts: when \(t=1\), Section 3 collapses exactly to the finite Section 2 problem, with the additional divisibility condition \(a\mid Sz\).

The fact that a generalized Pell equation with square discriminant is a finite factorization problem is classical. For example, OEIS A230263 records the general factorization criterion for \(x^2-d^2y^2=N\), and standard Pell literature isolates the nonsquare-discriminant case as the source of infinite unit orbits. Those older results cover the algebraic factorization but cannot state the source-specific \(t=1\) correction or its exact coefficient reduction, because the 2026 reduction is new.

## Limitations
The factorization argument does not improve the genuinely Pellian branch \(t>1\). It also does not claim that every admissible signed factor pair survives the perfect-power and divisibility filters. The \(2\tau(c^{2n})\) figure counts candidate signed factor pairs before those filters, not the number of solutions.

## References
1. X. Zhuang and N. E. Mastorakis, “Some Methods to Solve the Diophantine Equation \(a y^2=b(x^k-c^k)\),” arXiv:2610.00119v1, 2026.
2. OEIS A230263, “Number of nonnegative integer solutions to the equation \(x^2-4y^2=n\),” including the stated general square-discriminant factorization criterion.
3. R. A. Mollin, “Generalized Lagrange criteria for certain quadratic Diophantine equations,” New York Journal of Mathematics 11 (2005), 539–545.
