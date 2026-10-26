# Frobenius orbit classification of bitangents on diagonal plane quartics

## Finding

For an odd prime power \(q\), consider the smooth genus-three plane curve
\[
C_{a,b,c}:\quad aX^4+bY^4+cZ^4=0,
\qquad a,b,c\in\mathbb F_q^\times.
\]
We count theta-contact bitangent **lines** over finite extensions, including hyperflex tangents whose intersection divisor is \(4P\). Let \(B_{a,b,c}\) be the 28-point finite étale scheme of odd theta characteristics, canonically identified with the bitangent lines of this smooth plane quartic (over a field of odd characteristic).

**Uniform quadratic-splitting case.** If \(q\equiv3\pmod4\), the permutation of the 28 geometric bitangents under arithmetic Frobenius is always
\[
\boxed{1^4\,2^{12}}.
\]
Thus there are exactly four \(\mathbb F_q\)-rational bitangent lines, regardless of \(a,b,c\); the other 24 form twelve quadratic pairs, and every bitangent is defined over \(\mathbb F_{q^2}\).

**All remaining cases.** Assume \(q\equiv1\pmod4\). Fix a generator \(g\) of \(\mathbb F_q^\times\), and let \(r,s\in\{0,1,2,3\}\) be determined by the fourth-power classes
\[
b/a\in g^r(\mathbb F_q^\times)^4,
\qquad c/a\in g^s(\mathbb F_q^\times)^4.
\]
Put \(\varepsilon=0\) for \(q\equiv1\pmod8\) and \(\varepsilon=2\) for \(q\equiv5\pmod8\), and define \(L(k)=4/\gcd(4,k)\), interpreting the argument modulo four. The multiset of Frobenius cycles is the disjoint union of
\[
\begin{aligned}
&\frac4{L(r+\varepsilon)}\text{ cycles of length }L(r+\varepsilon),\\
&\frac4{L(s+\varepsilon)}\text{ cycles of length }L(s+\varepsilon),\\
&\frac4{L(s-r+\varepsilon)}\text{ cycles of length }L(s-r+\varepsilon),\\
&\frac{16}{\operatorname{lcm}(L(r),L(s))}\text{ cycles of length }\operatorname{lcm}(L(r),L(s)).
\end{aligned}
\]
In particular, all bitangents split over \(\mathbb F_{q^4}\), and the exact possible rational-line counts and cycle profiles are:

| Congruence | Fourth-power class pair \((r,s)\) | Frobenius profile | Rational lines |
|---|---|---|---:|
| \(q\equiv1\pmod8\) | \((0,0)\) | \(1^{28}\) | 28 |
| \(q\equiv1\pmod8\) | \((0,2),(2,0),(2,2)\) | \(1^4 2^{12}\) | 4 |
| \(q\equiv1\pmod8\) | \((0,1),(0,3),(1,0),(1,1),(3,0),(3,3)\) | \(1^4 4^6\) | 4 |
| \(q\equiv1\pmod8\) | \((1,2),(1,3),(2,1),(2,3),(3,1),(3,2)\) | \(2^2 4^6\) | 0 |
| \(q\equiv5\pmod8\) | \((0,0)\) | \(1^{16}2^6\) | 16 |
| \(q\equiv5\pmod8\) | \((0,2),(2,0),(2,2)\) | \(1^8 2^{10}\) | 8 |
| \(q\equiv5\pmod8\) | \((1,2),(1,3),(2,1),(2,3),(3,1),(3,2)\) | \(1^4 4^6\) | 4 |
| \(q\equiv5\pmod8\) | \((0,1),(0,3),(1,0),(1,1),(3,0),(3,3)\) | \(2^2 4^6\) | 0 |

If the cycle profile is \(\prod_d d^{m_d}\), then for every positive integer \(n\),
\[
\#B_{a,b,c}(\mathbb F_{q^n})=\sum_{d\mid n}d\,m_d,
\qquad Z(B_{a,b,c}/\mathbb F_q,T)=\prod_d(1-T^d)^{-m_d}.
\]
These two formulas also specify every extension-field count and the full zeta function of the bitangent scheme, not the curve's Hasse–Weil zeta function.

## Assumptions and scope

The finite field has odd characteristic, including characteristic three; the coefficient product is nonzero. The curve is smooth, since its three partial derivatives have no common projective zero in odd characteristic. A theta-contact line means that the scheme-theoretic intersection divisor is \(2D\) for an effective divisor \(D\) of degree two, including \(D=2P\). The count is of geometric lines fixed by Frobenius, not of individual contact points. In characteristic three, some or all of these contact divisors are hyperflexes; this does not change the statement about the 28 lines.

The integers \(r,s\) depend on the choice of generator, but their induced cycle profile is invariant: replacing the generator multiplies both residue classes by the same odd residue modulo four and preserves the multiset of cycle lengths. Coefficient scaling likewise preserves the ratios.

## Proof

**1. Explicit complete geometric set.** For each cyclic choice of two coordinates, there are four lines of the form \(X=uY\) with \(u^4=-b/a\), and similarly \(X=vZ\) with \(v^4=-c/a\), and \(Y=wZ\) with \(w^4=-c/b\). Their intersection with \(C_{a,b,c}\) is the fourth power of the remaining coordinate, times a nonzero scalar; in particular they are theta-contact lines.

There are also sixteen lines \(X=uY+vZ\), where \(u^4=b/a\), \(v^4=c/a\). The identity
\[
a(uY+vZ)^4+bY^4+cZ^4
=2a\bigl(u^2Y^2+uvYZ+v^2Z^2\bigr)^2
\]
holds in every odd characteristic, including three. Thus these too are theta-contact. All 28 are pairwise distinct: the first 12 have a zero coefficient in the dual line, whereas the other 16 have three nonzero coefficients; within each class the fourth roots distinguish the lines.

A smooth genus-three plane quartic in characteristic not two has exactly 28 odd theta characteristics, each represented by a unique bitangent line (counting hyperflexes with multiplicity). Therefore the displayed 28 exhaust the geometric theta-contact lines. Since multiplication by two on the Jacobian is étale in odd characteristic, this 28-point theta-characteristic scheme is finite étale.

**2. Frobenius in the fourth-root cases.** Suppose \(q\equiv1\pmod4\), and let \(\zeta=g^{(q-1)/4}\). For any \(t\) with \(t^4=g^k\), one has \(t^q=\zeta^k t\). Accordingly Frobenius permutes its four fourth roots as the cyclic shift by \(k\bmod4\), giving \(4/L(k)\) cycles each of length \(L(k)\). The class of \(-1\) is \(\varepsilon\), because \(-1=g^{(q-1)/2}\). The three 4-line coordinate families are shifted respectively by \(r+\varepsilon,s+\varepsilon,s-r+\varepsilon\), while the 16 lines indexed by \((u,v)\) are translated on \((\mathbb Z/4)^2\) by \((r,s)\). A translation orbit on this 16-element set has length \(\operatorname{lcm}(L(r),L(s))\). The general profile follows. Checking the sixteen possible pairs gives the displayed tables; this is also implemented as an exact enumeration in the verifier.

**3. Quadratic-splitting case.** Suppose \(q\equiv3\pmod4\). Every fourth power in \(\mathbb F_q^\times\) is a square and every nonzero square is a fourth power. Also \(-1\) is a nonsquare. If all three coefficients have equal quadratic character, all three coordinate-pair families have zero rational members but each of the two fourth-root equations for \((u,v)\) has two rational solutions: precisely four rational noncoordinate bitangents. Otherwise one coefficient has the opposite quadratic character from the other two. Exactly two coordinate-pair families have square ratios after inserting the minus sign, each yielding two rational lines, and the noncoordinate family has none. Again exactly four rational bitangents.

Moreover every nonzero \(x\in\mathbb F_q\) has all four fourth roots in \(\mathbb F_{q^2}\), since \(q-1\mid(q^2-1)/4\) when \(q\equiv3\pmod4\). Thus all 28 lines split in that quadratic extension and a 28-point Frobenius set with four fixed points has cycle profile \(1^4 2^{12}\).

**4. Extension fields.** Each Frobenius orbit of length \(d\) has all its \(d\) points over \(\mathbb F_{q^n}\) precisely when \(d\mid n\). The finite-étale zeta product follows by its Euler product, or directly from \(\exp\bigl(\sum_n \#B(\mathbb F_{q^n})T^n/n\bigr)\).

## Verification

Run the self-contained file `verify_diagonal_bitangents.py` using Python 3. It independently enumerates projective lines over eleven prime fields of odd characteristic and over \(\mathbb F_9\); a line is counted only if substituting its defining linear equation into the quartic gives a scalar multiple of a square of a binary quadratic. This direct binary-square criterion is separate from the fourth-root count formula. The script tests all coefficient fourth-power-class representatives, reproduces the exact sixteen residue-pair cycle profiles, and prints `VERIFY_OK` and `GF9_VERIFY_OK` upon success. These finite checks support the proof but are not claimed as a proof for every finite field: that follows from the explicit line construction and Frobenius arguments above.

## Relationship to prior work

The explicit 28 Fermat-quartic bitangents and their decomposition into geometric symmetry orbits (12 and 16 lines) are classical, and **not** claimed as new. Plaumann–Sturmfels–Vinzant develop general bitangent algorithms and examples; Meagher–Top classify genus-three twists and arithmetic curve invariants; Bethea–Brazelton determine the geometric automorphism-set structure of the Fermat quartic; Betten–Kaplan–Karaoglu provide computational quartic data over some small finite fields. The narrower proposed contribution is the complete coefficientwise **arithmetic Frobenius-cycle classification of the finite-étale 28-bitangent scheme across every odd finite field**, especially its coefficient-independent quadratic splitting when \(q\equiv3\pmod4\).

## Limitations

The result does not classify bitangents on arbitrary nondiagonal quartics or in characteristic two. The extension-count and zeta formulas concern the 28-point bitangent scheme, not the genus-three curve or its Jacobian. These arithmetic profiles are computed from classical known geometric bitangent equations; an earlier source may already derive an equivalent finite-field Galois formulation or stronger theorem, and historical priority is not independently established. The formula does not claim uniqueness among all plane quartics for the observed congruence profiles.

## References

1. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic curves and their bitangents*, preprint arXiv:1008.4104 (first posted 2010-08-24); full text: https://math.berkeley.edu/~bernd/JSCquartics.pdf.
2. S. Meagher and J. Top, *Twists of genus three curves over finite fields* (2010), author-hosted full text: https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf.
3. D. Bethea and Z. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242 (2024), Sections 2 and 4.2: https://arxiv.org/html/2410.09242v1.
4. A. Betten, N. Kaplan and F. Karaoglu, *Classification of Quartic Curves Over Small Finite Fields* (online finite-field catalog, dated 2021-10-29): https://www.math.colostate.edu/~betten/mathdata/quartic_curves.html.
