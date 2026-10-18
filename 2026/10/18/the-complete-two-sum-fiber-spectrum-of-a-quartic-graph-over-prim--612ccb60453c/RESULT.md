# The complete two-sum fiber spectrum of a quartic graph over prime-square rings

## Finding

Let \(p\ge5\) be prime, \(R=\mathbb Z/p^2\mathbb Z\), and \(C=\{(t,t^4):t\in R\}\). For \(s,y\in R\), put
\[
r(s,y)=\#\{(a,b)\in R^2:a+b=s,\ a^4+b^4=y\}.
\]
Write \(\chi\) for the Legendre character modulo \(p\), including \(\chi(0)=0\), and define
\[
b=\chi(-1),\quad c=\chi(-3),\quad e=\chi(-6),\quad
h=\gcd(4,p-1),\quad
L=\frac{p-2+b}{4},\quad
H=\frac{p-4-b-2c-2e}{8},\quad
u=1+c,\quad v=1+e.
\]
The integers \(L,H\) are nonnegative. The **entire** representation-multiplicity spectrum has the following exact, disjoint description; multiplicities with value zero are included.

For each of the \(p^2-p\) choices of \(s\) not divisible by \(p\), the counts of \(y\) by the value of \(r(s,y)\), **with coincident values added together**, are given by the multiset
\[
\underbrace{\{2,\ldots,2\}}_{pL},\
\underbrace{\{4,\ldots,4\}}_{pH},\
\{p+v\},\
\underbrace{\{v,\ldots,v\}}_{p-1},\
\{pu\},
\]
together with \(p^2-[pL+pH+p+1]\) additional zeros. The displayed notation is a multiset of **values of \(r\)**; when \(v=0\) or \(u=0\), the corresponding terms contribute additional zeros. This multiset has \(p^2\) entries. More precisely, let \(\lambda=8ys^{-4}\) in \(R\). The \(pL\) entries equal to \(2\), and the \(pH\) entries equal to \(4\), come from noncritical residue classes of \(\lambda\bmod p\). At \(\lambda\equiv1\pmod p\), there is one entry \(p+v\), at \(\lambda=1\) in \(R\), and \(p-1\) entries \(v\). At \(\lambda\equiv-8\pmod p\), there is one entry \(pu\), at \(\lambda=-8\) in \(R\), and \(p-1\) zeros.

For each of the remaining \(p\) choices of \(s\), the multiset is: one entry \(p\), exactly \(p(p-1)/h\) entries \(h\), and \(p^2-1-p(p-1)/h\) zeros.

These data determine all target fibers. In particular, the sumset size is exactly
\[
|C+C|=(p^2-p)\left[p(L+H)+1+\frac{(p-1)v}{2}+\frac u2\right]
+p\left[1+\frac{p(p-1)}h\right],
\]
and the ordered additive energy has the closed form
\[
\boxed{E(C):=\sum_{s,y}r(s,y)^2
=p^2\bigl(6p^2-8p+3+2(p-1)(p-2)\chi(-3)\bigr).}
\]
For a nontrivial additive character \(\psi:R\to\mathbb C\) and the normalized extension function
\[
\mathcal E1(X,Y)=p^{-2}\sum_{t\in R}\psi(Xt+Yt^4),
\]
orthogonality gives the exact constant-input fourth moment
\[
\sum_{X,Y\in R}|\mathcal E1(X,Y)|^4=E(C)/p^4.
\]

## Assumptions and scope

Every prime \(p\ge5\) is included. Pairs \((a,b)\) are ordered, and \(r(s,y)\) counts every pair, including diagonal pairs. All ring equations are modulo \(p^2\) unless a reduction modulo \(p\) is explicitly indicated. No unproved conjecture, limiting argument, or probabilistic computation is used in the theorem. The energy statement is a constant-input fourth moment, not a claimed sharp extension norm for arbitrary weights.

## Proof

**Reduction to one quartic.** Since \(2\) is invertible in \(R\), every ordered pair with sum \(s\) is uniquely \((a,b)=((s+d)/2,(s-d)/2)\) for \(d\in R\). Direct expansion gives
\[
8(a^4+b^4)=s^4+6s^2d^2+d^4.
\]
If \(s\) is a unit, setting \(z=d/s\), \(\lambda=8ys^{-4}\), and \(g(z)=z^4+6z^2+1\) reduces \(r(s,y)\) to the number of solutions of \(g(z)=\lambda\) in \(R\).

**Residue-field roots and their exceptional lifts.** Modulo \(p\),
\[
g'(z)=4z(z^2+3).
\]
The critical points are \(z=0\), with critical value \(g(0)=1\), and the \(u=1+\chi(-3)\) solutions to \(z^2=-3\), with critical value \(-8\). The values \(1\) and \(-8\) are distinct modulo \(p\) since \(p\ne3\). Each regular root modulo \(p\) lifts uniquely to a root for each fixed lift of the right-hand side, by the elementary first-order congruence
\[
g(z_0+pt)\equiv g(z_0)+pt\,g'(z_0)\pmod{p^2}.
\]
At the first critical point \(z=0\), all \(p\) lifts have exactly \(g(z)=1\) in \(R\). The other roots at this residue value are the \(v=1+\chi(-6)\) regular solutions of \(z^2=-6\); these contribute \(v\) to **every** lift of \(\lambda\equiv1\pmod p\). Thus \(r=p+v\) once and \(r=v\) at the other \(p-1\) lifts.

When \(u=2\), the two solutions to \(z^2=-3\bmod p\) each admit a unique Hensel lift \(z_*\in R\) satisfying \(z_*^2=-3\) in \(R\). For every \(t\in\mathbb F_p\), \(g(z_*+pt)=-8\) in \(R\). Hence \(\lambda=-8\) has \(2p=pu\) roots, whereas its other \(p-1\) lifts have no roots. When \(u=0\), every lift has zero roots and the same formula \(pu=0\) applies. All other residue roots are regular and are distributed in pairs \(\pm z\); away from the two critical values, the possibilities are \(0,2,4\) roots.

**Exact counts of two- and four-root residue classes.** For \(z,w\in\mathbb F_p\),
\[
g(z)-g(w)=(z^2-w^2)(z^2+w^2+6).
\]
The first factor vanishes at \(2p-1\) ordered pairs. The second vanishes at exactly \(p-\chi(-1)\) pairs (a standard nondegenerate quadratic-character sum). Their intersection has \(2u=2(1+\chi(-3))\) pairs, because \(z^2=w^2=-3\). Therefore
\[
\sum_{\lambda\in\mathbb F_p}\#g^{-1}(\lambda)^2
=3p-3-b-2c.
\]
Also \(\sum_\lambda\#g^{-1}(\lambda)=p\). The two critical values contribute \(1+v=2+e\) and \(u=1+c\) roots, respectively. If \(L\) and \(H\) denote the numbers of other residue values with respectively two and four roots, then
\[
2L+4H=p-(1+v)-u,\quad
4L+16H=3p-3-b-2c-(1+v)^2-u^2.
\]
Solving yields precisely \(L=(p-2+b)/4\) and \(H=(p-4-b-2c-2e)/8\); this also proves these are nonnegative integers. Each noncritical residue value has exactly \(p\) lifts in \(R\), all retaining its regular root count. These facts prove the unit-\(s\) distribution and locate every exceptional fiber.

**Nonunit first-coordinate sums.** If \(p\mid s\), both \(s^4\) and \(s^2d^2\) vanish in \(R\), so \(8y=d^4\). The derivative \(4d^3\) is invertible at every \(d\not\equiv0\pmod p\). Each nonzero fourth-power residue modulo \(p\), of which there are \((p-1)/h\), has \(h\) preimages modulo \(p\), and every one of the \(p\) lifts of its target has \(h\) lifted preimages. If \(p\mid d\), then \(d^4=0\) in \(R\); thus the single zero target has precisely \(p\) preimages. This proves the nonunit-\(s\) distribution. Counting the positive fibers gives the claimed exact sumset size.

**Energy and independent algebraic check.** Squaring and summing the displayed two per-\(s\) distributions gives
\[
E(C)=p^2\left(6p^2-8p+3+2(p-1)(p-2)c\right).
\]
An independent derivation is useful. With two difference variables \(d,e\), equality of quartic coordinates at a fixed common sum \(s\) is equivalent to
\[
(d^2-e^2)(d^2+e^2+6s^2)=0\pmod{p^2}.
\]
Modulo \(p\), the number of triples \((s,d,e)\) satisfying this is
\[
E_p=3p^2-3p+1-2(p-1)c.
\]
The singular reduction triples (zero gradient of the product) form exactly \(S=p+2(p-1)(1+c)\) points: the line \(d=e=0\) and the additional transverse intersections \(d^2=e^2=-3s^2\) with \(s\ne0\). Every regular reduction triple has \(p^2\) lifts among its \(p^3\) possible lifts, while every singular triple has all \(p^3\) lifts. The count is therefore
\[
p^2 E_p+(p^3-p^2)S
=p^2\left(6p^2-8p+3+2(p-1)(p-2)c\right),
\]
agreeing with the fiber-spectrum calculation.

Finally, expand \(\sum_{X,Y}|\mathcal E1(X,Y)|^4\), apply character orthogonality on \(R^2\), and use \(|R|=p^2\): the result is \(p^{-4}E(C)\). This completes the proof.

## Verification

Run `python3 artifacts/verify.py` from the extracted package directory. The script constructs every ordered pair \((a,b)\) for primes \(5,7,11,13,17,19\), independently builds the entire two-coordinate fiber table, and compares its distribution and additive energy against the formulas. It checks all \(p^4\) targets including those with zero representations. The expected output is included in `artifacts/verify_output.txt`. These finite calculations supplement the universal argument and are not substituted for it.

## Relationship to prior work

González-Riquelme and Oliveira e Silva develop sharp finite-field Fourier extension inequalities and their moment/convolution framework, including the parabola and related quadratic surfaces. The present object is instead a quartic graph over the nonreduced ring \(\mathbb Z/p^2\mathbb Z\), where critical-root lifting creates entire fibers of size proportional to \(p\).

The published note *Exact additive energy of the finite-field quartic graph* determines the quartic-graph energy **over finite fields**; it does not imply this prime-square ring spectrum, which includes exceptional lifts at \(\lambda=1,-8\) and the nonunit-sum stratum. A later note on the invariant quartic-graph extension quotient concerns complex coefficient weights on the field graph, not the ring representation counts. The prime-square cubic graph has also been studied separately; the polynomial degree changes the critical-lift mechanism, so its classification does not contain the quartic result.

## Limitations

This theorem treats prime-square rings with \(p\ge5\), not general composite moduli or higher prime powers. It determines the exact convolution fibers, sumset, additive energy and constant-input Fourier fourth moment, but not the sharp weighted \(L^2\)-to-\(L^4\) Fourier extension constant. An undiscovered treatment of these exact quartic ring fibers in the literature would affect originality. The arithmetic proof, rather than the finite enumerations, is the source of the unrestricted quantifiers.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (first public 2024-05-26).
2. *Exact additive energy of the finite-field quartic graph*, public mathematical research record (2026), finite-field formula.
3. *An arithmetic phase transition in the invariant quartic-curve Fourier norm*, public mathematical research record (2026), invariant-field extension quotient.
