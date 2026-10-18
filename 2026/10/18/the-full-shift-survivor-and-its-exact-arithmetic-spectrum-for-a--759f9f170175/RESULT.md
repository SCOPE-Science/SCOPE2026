# The full-shift survivor and its exact arithmetic spectrum for a prime-representing numerator map

## Finding

For every integer \(M\geq2\), the natural set of \(M\)-adic numerators whose denominators **never decrease** under the numerator dynamics of the prime-representing map is an exactly self-similar full shift on \(\varphi(M)\) symbols. Its Hausdorff, upper and lower box-counting, and Assouad dimensions in the canonical \(M\)-adic metric all equal

\[
 s_M=\frac{\log\varphi(M)}{\log M}.
\]

The Hausdorff measure at that dimension is exactly \(1\) with the metric normalization below, even for \(M=2\), when the survivor is a singleton. At level \(n\), the survivor occupies exactly \(\varphi(M)^n\) of the \(M^n\) residue classes, and therefore has Haar measure zero. Its dynamical entropy is \(\log\varphi(M)\). It has exactly \(\varphi(M)^n\) points fixed by the \(n\)-th iterate; hence the number of orbits of **least** period \(n\) is

\[
 \frac1n\sum_{d\mid n}\mu(d)\varphi(M)^{n/d}.
\]

Every periodic point is an explicitly computable rational number in the real interval \((M,2M)\), and every eventually periodic point also belongs to that interval. Consequently an integer numerator \(a\geq2M\) with no denominator decrease cannot have an eventually periodic symbolic itinerary. The result does **not** assert that every such integer numerator eventually loses denominator.

## Assumptions and scope

Fix an integer \(M\geq2\). Let

\[
 R_M=\varprojlim_{n\geq1}\mathbb Z/M^n\mathbb Z,
 \qquad d_M(x,y)=M^{-v_M(x-y)},
\]

where \(v_M(z)=\sup\{n\geq0:z\in M^nR_M\}\) for nonzero \(z\), and \(d_M(x,x)=0\). Multiplication by \(M\) is injective on \(R_M\). Set

\[
 U_M=\{r\in\{1,\ldots,M-1\}:\gcd(r,M)=1\},\qquad k=|U_M|=\varphi(M).
\]

For each unit \(x\in R_M^\times\), uniquely write \(x=r+Mq\) with \(r\in U_M\) and \(q\in R_M\), and define

\[
 D_M(x)=q(M+r).
\]

Its invariant survivor is

\[
 K_M=\{x\in R_M^\times:\ D_M^j(x)\in R_M^\times\text{ for every }j\geq0\}.
\]

The original real map is \(T(t)=\lfloor t\rfloor(1+\{t\})\). For an integer \(a=qM+r\geq2M\) with \(\gcd(a,M)=1\), Carvalho's numerator identity gives \(M T(a/M)=D_M(a)=q(M+r)\). The condition \(D_M(a)\in R_M^\times\) is exactly the condition that the next reduced denominator remains \(M\). Thus \(K_M\) is the canonical set of infinite **non-dropping** numerator residue itineraries. The dynamics on other denominators and the unproved possibility of nonterminating real rational orbits are outside the classification.

For this result, \(\mu\) in the periodic-orbit formula is the number-theoretic Möbius function; it is unrelated to the Bernoulli probability measure used below.

## Proof

**1. Inverse similarities and symbolic coding.** For every \(r\in U_M\), \(M+r\) is a unit of \(R_M\). Define

\[
 F_r(y)=r+\frac{My}{M+r},\qquad y\in R_M.
\]

For every unit \(y\), the output is a unit with residue \(r\), and \(D_M(F_r(y))=y\). Furthermore,

\[
 d_M(F_r(x),F_r(y))=M^{-1}d_M(x,y)
\]

for all \(x,y\in R_M\). This is equality, not just a Lipschitz bound: multiplication by \(M\) increases \(v_M\) by exactly one, and a unit factor preserves it. Different \(r\) give disjoint images modulo \(M\). The nested cylinders

\[
 F_{r_0}\circ F_{r_1}\circ\cdots\circ F_{r_{n-1}}(R_M),
 \qquad (r_0,\ldots,r_{n-1})\in U_M^n,
\]

have diameters at most \(M^{-n}\), so each infinite digit word defines one point. Taking the first residue digit of each successive iterate supplies its unique word. Thus the coding map from \(U_M^{\mathbb N_0}\) is a homeomorphism onto \(K_M\), and \(D_M\) becomes the left shift. The cylinders are precisely \(k^n\) distinct residue balls of radius \(M^{-n}\); each extension adds one of exactly \(k\) allowed unit digits. In particular \(K_M\) is compact and nonempty.

**2. Fractal geometry.** If \(k=1\) (equivalently \(M=2\)), there is one infinite word, hence one survivor and \(s_M=0\); its zero-dimensional Hausdorff measure is \(1\). For \(k>1\), assign mass \(k^{-n}\) to each allowed length-\(n\) cylinder. This defines a probability measure \(\nu\) on \(K_M\) with

\[
 \nu(B_{d_M}(x,M^{-n}))=k^{-n}=\bigl(M^{-n}\bigr)^{s_M}
 \quad(x\in K_M,\ n\geq0).
\]

Covering with the \(k^n\) cylinders gives \(\mathcal H^{s_M}(K_M)\leq1\). Conversely any nonempty subset of \(R_M\) with positive diameter \(M^{-n}\) lies in one such radius-\(M^{-n}\) ball, so its \(\nu\)-mass is at most \(k^{-n}\), equal to diameter raised to \(s_M\). Singleton sets have zero \(\nu\)-mass. Applying the mass-distribution inequality to every countable cover gives \(\mathcal H^{s_M}(K_M)\geq1\). Hence equality holds. For an arbitrary radius \(0<\rho\leq1\), the successive cylinder radii sandwich the mass by \(k^{-1}\rho^{s_M}\leq\nu(B(x,\rho))\leq k\rho^{s_M}\) (the constants cover open-versus-closed ball conventions). Thus the measure is \(s_M\)-Ahlfors regular, both box dimensions and Assouad dimension equal to \(s_M\). Uniform product probability on the digit sequences is mapped to \(\nu\). Each allowed residue ball has ambient normalized Haar mass \(M^{-n}\), so \(\operatorname{Haar}(K_M)\leq(k/M)^n\) for all \(n\), and this tends to zero because \(k<M\). Standard cylinder-block counts give shift topological entropy \(\log k\).

**3. Periodic spectrum and exact rational representatives.** A length-\(n\) word repeated forever specifies a unique fixed point of \(D_M^n\), and distinct words specify distinct points. Writing \(b_i=M+r_i\), composition of the inverse branches gives its rational value explicitly:

\[
 x_{(r_0,\ldots,r_{n-1})}
 =\frac{\displaystyle\sum_{j=0}^{n-1}r_jM^j\prod_{i=j}^{n-1}b_i}
 {\displaystyle\prod_{i=0}^{n-1}b_i-M^n}.
\]

The denominator is positive and is congruent to \(\prod_i r_i\pmod M\), hence is a unit. The formula therefore also defines a point in \(R_M\). Periodic-word counting yields \(k^n\) fixed points, and Möbius inversion yields the claimed least-period orbit count. In particular the Artin–Mazur zeta function of this compact subsystem is \((1-kz)^{-1}\).

For every \(r\in U_M\), direct calculation gives

\[
 F_r(M)=M+\frac{r^2}{M+r}>M,\qquad
 F_r(2M)=2M-\frac{r(M-r)}{M+r}<2M.
\]

As \(F_r\) is strictly increasing, \(F_r([M,2M])\subset(M,2M)\). Every rational periodic fixed point of a composition of these real contractions lies in that interval. Applying any finite prefix of the inverse branches preserves it, so every eventually periodic coding point lies in \((M,2M)\). No integer \(a\geq2M\) lies there. Equality in \(R_M\) between a rational with denominator coprime to \(M\) and an ordinary integer forces equality as rational numbers, since their difference embeds injectively in every \(p\)-adic factor for \(p\mid M\). This proves the final obstruction to eventual periodicity for an integer non-dropping numerator.

## Verification

The accompanying `check_survivor.py` uses only Python's exact integer and rational arithmetic. Run `python3 check_survivor.py`. It independently enumerates admissible numerator residue classes for \(2\leq M\leq12\), checks the predicted counts at multiple depths, checks every period word of length at most four, and verifies the closed rational formula and its digit itinerary. It also verifies the nonconstant period-two orbit \(50/11\mapsto52/11\mapsto50/11\) for \(M=3\). The executable successfully completed 15,740 checks. These finite tests are cross-checks; the proof of the claims for **all** moduli and all depths is the argument above.

## Relationship to prior work

Carvalho's *Rational dynamics of a prime-representing map* (arXiv:2605.21802v1, May 20, 2026) proves the numerator identity, finite-order residue-class recurrences, and density-one finite-order behavior for every fixed denominator. Those premises motivate the present non-dropping subsystem. The source does **not** state the compact full-shift conjugacy, its normalized Hausdorff measure or dimensions, or the complete rational periodic-point spectrum. The cylinder counts are compatible with the existing finite-order recurrences; the new conclusion is the dynamical and metric classification rather than a claim of novelty for the numerator identity.

Azevedo, Carvalho and Machiavelo's *Dynamics of a quasi-quadratic map* (arXiv:1210.0042v1, September 28, 2012), particularly Section 5, constructs a perfect Haar-null set of infinite-order points for a **different** ceiling-based map in a \(p\)-adic setting. This is important antecedent geometry, but does not imply the precise inverse branches, dimensions, Hausdorff measure, or periodic arithmetic spectrum for the map studied here.

## Limitations

A symbolic survivor in an \(M\)-adic completion need not contain an integer numerator \(a\geq2M\). Showing a nonempty Cantor set, or rational periodic points in the auxiliary numerator system, therefore does **not** provide a counterexample to the finite-order conjecture for the real map on rationals at least \(2\). In fact the rational periodic and eventually periodic auxiliary points lie below the eligible integer-numerator threshold. This result addresses persistent *fixed* denominators, not the full cascade through proper divisors; it gives neither a quantitative stopping-time estimate nor an existence result for genuinely nonterminating rational orbits.

## References

1. André Carvalho, *Rational dynamics of a prime-representing map*, arXiv:2605.21802v1 (first public May 20, 2026), Sections 1–4, particularly Lemmas 2.1–2.2, Theorem 3.1 and Theorem 4.4; https://arxiv.org/pdf/2605.21802.
2. Assis Azevedo, Maria Carvalho and António Machiavelo, *Dynamics of a quasi-quadratic map*, arXiv:1210.0042v1 (September 28, 2012), particularly Section 5; https://arxiv.org/pdf/1210.0042.
