# Exact fourth-shift Hankel determinants of the \(q\)-golden ratio

## Finding

Let \(\Phi(q)=\sum_{h\geq 0}c_hq^h\in\mathbb Z[[q]]\) be the unique formal power series satisfying
\[
q\Phi(q)^2+(1-q-q^2)\Phi(q)=1,\qquad \Phi(0)=1.
\]
For every \(j\geq 1\), define its fourth-shift Hankel determinant
\[
\Delta_j^{(4)}=\det(c_{4+a+b})_{0\leq a,b<j},\qquad \Delta_0^{(4)}=1.
\]
Then, for **every integer** \(m\geq 0\),
\[
\boxed{\begin{aligned}
\Delta_{4m}^{(4)}&=(-1)^m(2m+1),\\
\Delta_{4m+1}^{(4)}&=(-1)^m(2m+2),\\
\Delta_{4m+2}^{(4)}&=0,\\
\Delta_{4m+3}^{(4)}&=(-1)^{m+1}(2m+2).
\end{aligned}}
\]
Equivalently, the complete generating function of these determinants is
\[
\boxed{\sum_{j\geq0}\Delta_j^{(4)}z^j=\frac{(1-z)(1+z)^3}{(1+z^4)^2}.}
\]
The sequence is an unbounded quasi-polynomial of **least** quasi-period \(8\). This verifies the first previously unresolved higher-shift instance, \(n=1,\ell=4\), of Conjecture C in Han--Pedon (2026). The first sixteen entries themselves were already displayed by Ovsienko--Pedon (2023); the claim here is the exact **all-index theorem** and its proof, not discovery of those entries.

## Assumptions and scope

Here \(q\) and \(z\) are formal indeterminates over \(\mathbb Q\); all Hankel determinants are ordinary integer determinants, and their size \(j\) is arbitrary. The defining quadratic equation specifies a unique series because its coefficient of \(\Phi\) has constant term \(1\). In the established terminology it is the \(q\)-golden ratio, the case \(n=1\) of the \(q\)-metallic numbers. No numerical convergence of the formal series is needed.

Define its shifted series
\[
F(q)=\frac{\Phi(q)-(1+q^2-q^3)}{q^4}=\sum_{h\geq0}c_{h+4}q^h.
\]
The initial coefficient is \(F(0)=2\), and substituting into the quadratic equation gives the exact polynomial relation \(A_0+B_0F+C_0F^2=0\), where
\[
\begin{aligned}
A_0&=-2+2q-2q^2+q^3,\\
B_0&=1+q-q^2+2q^3-2q^4,\\
C_0&=q^5.
\end{aligned}
\]

## Proof

**1. Exact algebraic continued-fraction step.** We use the Hankel continued fraction (\(H\)-fraction) transformation and its Hankel-determinant identity as established in Han--Pedon (2026, Section 2.1, Algorithm 2.3 and Theorem 2.2). For a triple \((A,B,C)\) with \(A+B\mathcal F+C\mathcal F^2=0\), \(B(0)=1\), \(C(0)=0\), write \(k=\operatorname{ord}_q(A)\), \(a=[q^k]A\), and
\[
D=\left[\frac{aq^kB}{A}-\frac{aq^kC}{B}\right]_{\leq k+1}.
\]
Its successor is
\[
\begin{aligned}
A^*&=\frac{-D^2A/a+BDq^k-Caq^{2k}}{q^{2k+2}},\\
B^*&=\frac{2AD}{aq^k}-B,\\
C^*&=-\frac{Aq^2}{a}.
\end{aligned}
\]
The truncation is in \(\mathbb Q[[q]]\). Every nonzero determinant is obtained from the parameters \(a,k\) of successive steps, as recalled in Step 3 below.

**2. Three parametric families, verified for all parameters.** For an arbitrary even integer \(t\geq2\), put \(\mathcal S_i(t)=(A_i(t),B_i(t),C_i(t))\), where
\[
\begin{aligned}
A_1(t)&=\frac{(t-1)q}{t},\\
B_1(t)&=1+q-q^2+\frac{2q^3}{t},\\
C_1(t)&=\frac{q^2(q^3-tq^2+tq-t(t-1))}{t(t-1)},\\[3pt]
A_2(t)&=-\frac{q^3+tq^2-tq-t(t+1)}{t^2},\\
B_2(t)&=1+q-q^2-\frac{2q^3}{t},\\
C_2(t)&=-q^3,\\[3pt]
A_3(t)&=\frac{t(q^3-(t+2)q^2+(t+2)q-(t+2)(t+1))}{(t+1)^3},\\
B_3(t)&=-\frac{2q^4-2q^3-((t+1)^2-2)q^2-(t+1)^2(q+1)}{(t+1)^2},\\
C_3(t)&=\frac{q^2(q^3+tq^2-tq-t(t+1))}{t(t+1)}.
\end{aligned}
\]
Direct substitution in the three successor formulas proves the following **polynomial identities in \(q\) and rational functions of the indeterminate \(t\)**:
\[
\begin{array}{rcl}
(A_0,B_0,C_0)&\xrightarrow{\ k=0,\ a=-2,\ D=1+2q\ }&\mathcal S_1(2),\\
\mathcal S_1(t)&\xrightarrow{\ k=1,\ a=(t-1)/t,\ D=1+q-q^2\ }&\mathcal S_2(t),\\
\mathcal S_2(t)&\xrightarrow{\ k=0,\ a=(t+1)/t,\ D=1+tq/(t+1)\ }&\mathcal S_3(t),\\
\mathcal S_3(t)&\xrightarrow{\ k=0,\ a=-t(t+2)/(t+1)^2,\ D=1+(t+2)q/(t+1)\ }&\mathcal S_1(t+2).
\end{array}
\]
The displayed \(a\) equals the leading nonzero \(q\)-coefficient of the corresponding \(A\); each displayed \(D\) has constant term \(1\), degree at most \(k+1\), and agrees with the required truncated series modulo \(q^{k+2}\). All output triples are polynomials with \(B(0)=1\), \(C(0)=0\), and nonzero \(A\), \(C\). Since \(t\geq2\), no parameter denominator vanishes. These identities therefore verify the **actual algorithmic transitions**, not just a formal resemblance among triples. The enclosed `verify.py` independently checks all four identities symbolically, including the truncation and normalization conditions, using \(t\) as an indeterminate. This establishes the infinite sequence of transforms by induction.

**3. Determinants from the infinite transform.** Index successive steps by \(i=1,2,\dots\), and denote the preceding \(k,a\) parameters by \(k_i,a_i\). The initial step is \((k_1,a_1)=(0,-2)\); for every \(m\geq1\), the next three steps are
\[
\begin{aligned}
(k_{3m-1},a_{3m-1})&=\left(1,\frac{2m-1}{2m}\right),\\
(k_{3m},a_{3m})&=\left(0,\frac{2m+1}{2m}\right),\\
(k_{3m+1},a_{3m+1})&=\left(0,-\frac{4m(m+1)}{(2m+1)^2}\right).
\end{aligned}
\]
Let \(s_0=0\), \(s_h=h+\sum_{i=1}^h k_i\), and \(P_h=\prod_{i=1}^h(-a_i)\). The cited \(H\)-fraction determinant theorem says that the Hankel determinants are zero outside the set of indices \(\{s_h:h\geq0\}\) and, for consecutive indices, obey
\[
\frac{\Delta_{s_{h+1}}^{(4)}}{\Delta_{s_h}^{(4)}}
=(-1)^{k_{h+1}(k_{h+1}+1)/2}P_{h+1}^{\,k_{h+1}+1}.
\]
The products telescope without any asymptotics:
\[
P_1=2,\qquad
P_{3m-1}=-1,\quad P_{3m}=\frac{2m+1}{2m},\quad P_{3m+1}=\frac{2m+2}{2m+1}\quad(m\geq1).
\]
Consequently \(s_1=1\), \(s_{3m-1}=4m-1\), \(s_{3m}=4m\), \(s_{3m+1}=4m+1\). Therefore the missing positive indices are precisely those congruent to \(2\) modulo \(4\). Starting from \(\Delta_0^{(4)}=1\), the displayed consecutive-ratio formula, with these telescoping products, gives exactly the four boxed formulas for every \(m\geq0\).

**4. Rational generating function and minimality.** Summing the four residue classes geometrically gives
\[
\sum_{j\geq0}\Delta_j^{(4)}z^j=\frac{(1-z)(1+z)^3}{(1+z^4)^2}.
\]
The denominator is the square of the eighth cyclotomic polynomial \(\Phi_8(z)=1+z^4\); it has no common factor with \((1-z)(1+z)^3\). Every quasi-polynomial of period \(p\) has generating-function poles only at \(p\)-th roots of unity. The primitive eighth-root poles here force \(8\mid p\), and the displayed residue formulas give period \(8\). Hence the least quasi-period is exactly \(8\).

## Verification

Run `python verify.py` with Python 3 and `sympy`. The checker derives the initial three polynomial coefficients from the shifted quadratic equation, verifies the four exact rational-polynomial transitions symbolically for an indeterminate parameter, and independently computes determinants of sizes \(0\) through \(22\) from \(50\) exact shifted Taylor coefficients by fraction-free determinant computation. Expected output:

```
SYMBOLIC_NEXTABC_OK initial_and_three_generic_transitions
INDEPENDENT_HANKEL_OK sizes=0..22 coefficients=50
```

The all-index proof is the parametric transition identity plus the general cited \(H\)-fraction theorem. Finite determinant evaluation alone would **not** prove the theorem, and the test does not claim otherwise.

## Relationship to prior work

Ovsienko--Pedon (2023/2024), Theorem 1.6, proves all-index results for shifts \(0,1,2,3\) of the \(q\)-golden ratio and explicitly lists the **first sixteen** entries of the fourth-shift sequence in formula (1.18); it does **not** give their full infinite formula. Han--Pedon (2025/2026) determines the shifts through \(n+1\). Han--Pedon (October 26, 2026), Theorem A/B, establishes the \((n+2)\)-shift and explicitly states in Conjecture C the quasi-polynomial property for all \(\ell\geq n+3\). Here \((n,\ell)=(1,4)\), which lies strictly beyond those proved ranges. The new theorem supplies its all-index formula, least quasi-period, and a nonperiodic rationally parameterized \(H\)-fraction certificate. The earlier printed initial terms and the proposed period \(8\) are acknowledged as prior evidence, not claimed as original results.

## Limitations

The theorem covers **only** the first higher shift of the \(q\)-golden ratio, not all metallic parameters or higher shifts in Conjecture C. Its symbolic proof uses the already published general \(H\)-fraction/Hankel identity, so it is not a self-contained reproving of that background theorem. Searches of relevant primary texts and indexed mathematical records have not located prior all-index coverage, but they cannot establish priority conclusively. No independent mathematical audit has been performed.

## References

- V. Ovsienko and E. Pedon, *Continued fractions for \(q\)-deformed real numbers, \(\{-1,0,1\}\)-Hankel determinants, and Somos--Gale--Robinson sequences*, arXiv:2312.17009, initial public version December 28, 2023; especially Theorem 1.6 and formula (1.18). https://arxiv.org/html/2312.17009v2
- G.-N. Han and E. Pedon, *Hankel continued fractions and Hankel determinants for \(q\)-deformed metallic numbers*, arXiv:2502.05993, initial public version February 9, 2025. https://arxiv.org/html/2502.05993v2
- G.-N. Han and E. Pedon, *Hankel determinants for the \((n+2)\)-shifted \(q\)-metallic numbers*, arXiv:2610.36132, initial public version October 26, 2026; especially Section 2.1, Algorithm 2.3, Theorem 2.2 and Conjecture C. https://arxiv.org/html/2610.36132v1
