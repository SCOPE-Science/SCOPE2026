# The characteristic-two dual-Hesse jump of the Fermat cubic inflection-tangent divisor

## Finding

Put
\[
F=X^3+Y^3+Z^3,\qquad
D=V\!\left(F(X^3+Y^3)(Y^3+Z^3)(Z^3+X^3)\right)\subset\mathbb P^2_{\mathbb Z}.
\]
For each prime \(p\ne3\), the geometric reduction \(D_p\) consists of a smooth cubic together with its nine indicated inflection-tangent lines. The geometric support of the singular locus has the following complete distribution:

| Characteristic | Line-line ordinary doubles | Line-line ordinary triples | Distinct cubic-line triple-contact points | Total geometric singular points |
| --- | ---: | ---: | ---: | ---: |
| \(p\ge5\) | 27 | 3 | 9 | 39 |
| \(p=2\) | 0 | 12 | 9 | 21 |

In characteristic two the nine-line arrangement is the dual-Hesse configuration: every pair of lines belongs to exactly one of twelve triple crossings, and every line contains four such crossings. More precisely, the three pencil centers persist and the 27 double intersections in other characteristics coalesce three at a time into nine further triples. This asserts the special identification of the fixed integral cubic-and-tangents model, not originality of the abstract dual-Hesse configuration.

The number of **rational geometric singular points** is
\[
\#\operatorname{Sing}(D_p)(\mathbb F_p)
=\begin{cases}
7,&p=2,\\
39,&p\equiv1\pmod3,\\
9,&p>2,\ p\equiv2\pmod3.
\end{cases}
\]
These are counts of geometric point supports and do not assert equality of singular schemes or numerical Tjurina invariants.

## Assumptions and scope

The base prime \(p\) is any rational prime except \(3\); intersections are taken over an algebraic closure of \(\mathbb F_p\) before rational points are counted. Let \(\zeta\) be a primitive cube root of unity in that closure. The nine tangent lines are
\[
L_{XY,a}:X+\zeta^aY=0,\quad
L_{YZ,b}:Y+\zeta^bZ=0,\quad
L_{ZX,c}:Z+\zeta^cX=0,
\]
where \(a,b,c\in\{0,1,2\}\). A cubic-line *triple-contact point* means a meeting of two smooth, distinct branches with intersection multiplicity exactly three; the terminology does not presume a characteristic-zero analytic normal form in characteristic two. Geometric singular points of this reduced union arise at and only at intersections of distinct smooth components.

## Proof

**Components and cubic contact.** Because \(p\ne3\), the three factors \(X^3+Y^3\), etc., have distinct linear factors. The Fermat cubic is smooth: its partial derivatives \(3X^2,3Y^2,3Z^2\) have no common projective zero. For example, restricting \(F\) to \(L_{XY,a}\) using \(X=-\zeta^aY\) gives \(F|_{L_{XY,a}}=Z^3\). Thus this line meets the cubic only at
\[
P_{XY,a}=[-\zeta^a:1:0],
\]
with intersection multiplicity three. The cyclic permutations give the other six contacts. The nine points are distinct, smooth on the cubic, and lie on no other indicated line. Each tangent line is therefore a flex tangent (triple contact), including in characteristic two. Every singular point involving the cubic is one of these nine points.

**Line intersections.** Within each of the three pencils, the three lines meet respectively at \([0:0:1]\), \([1:0:0]\), and \([0:1:0]\). The nine line equations remain pairwise distinct for \(p\ne3\). Two lines from different pencils meet at a point with all three coordinates nonzero. The cross-pairing \(L_{XY,a}\cap L_{YZ,b}\) is represented by
\[
[\zeta^{a+b}:-\zeta^b:1].
\]
The corresponding three-family line-coefficient determinant is
\[
\det\begin{pmatrix}1&\zeta^a&0\\0&1&\zeta^b\\\zeta^c&0&1\end{pmatrix}
=1+\zeta^{a+b+c}.
\]
This determinant vanishes exactly if \(p=2\) and \(a+b+c\equiv0\pmod3\). Indeed, in odd characteristic the equation \(\zeta^j=-1\) is impossible, since cubing yields \(1=-1\). In characteristic two the equation becomes \(\zeta^j=1\). A triple with two lines from one pencil and a line from another cannot occur: its determinant is a nonzero multiple of \(\zeta^a-\zeta^{a'}\), which remains nonzero for \(p\ne3\). Nor can four distinct lines concur, because a point lies on at most one line from each pencil except at a pencil center, which belongs to no other pencil's line.

For odd \(p\ne3\), the 27 pairs of lines from distinct pencils therefore produce 27 distinct ordinary double points, besides the three pencil-center triples. In characteristic two, precisely nine triples indexed by \(a+b+c\equiv0\) occur, and each consumes three of those 27 pair intersections. There are therefore twelve triple points and no double points. Since \(\binom92=36=12\binom32\), this is the dual-Hesse incidence pattern. Each line contains one pencil center and three of the nine cross-family triple points, hence four triple points in all.

At any cross-family meeting, all coordinates are nonzero and their cubes have values \((t,-t,t)\) after normalization, for a nonzero \(t\); the Fermat equation is therefore \(t\ne0\). The pencil centers also lie off the cubic. Hence these line-line singular points do not collide with the nine cubic-line contact points, in any allowed characteristic.

**Prime-field rationality.** If \(p\equiv1\pmod3\), all roots of unity \(\zeta\) lie in \(\mathbb F_p\), so all 30 line-line crossings and all nine cubic-line contacts are rational: total 39. If \(p\equiv2\pmod3\), Frobenius exchanges \(\zeta\) and \(\zeta^2\). Exactly three of the nine contacts (those indexed by zero) are rational. For odd \(p\), the only rational cross-family double point in each of the three pair-of-pencil families is the intersection of its two individually rational lines, giving three rational double points; the three pencil centers are rational, so the total is \(3+3+3=9\). In characteristic two, the twelve line-line triples comprise three rational pencil centers and nine cross-family triples indexed by \(a+b+c=0\); only the triple with \(a=b=c=0\) is Frobenius-fixed, hence the line-line contribution is four, and with three rational contacts the total is seven.

## Verification

The standalone `verify.py` uses exact arithmetic in prime fields and their quadratic extensions. It enumerates all 36 unordered pairs of the nine lines, canonicalizes their cross products, checks the line-multiplicity distributions, tests disjointness from the nine triple-contact points and evaluates their rationality. Its representative-prime run includes \(p=2,5,7,11,13,17,19,23,31,37,41,43\) and completes with `VERIFY_OK`. The universal all-prime conclusion is established by the determinant and contact identities above, not by that finite list.

## Relationship to prior work

Talar's 2023 cubic-line arrangement study records the characteristic-zero incidence numbers for the Fermat cubic and its nine inflection lines: 27 nodes, three ordinary line triples, and nine cubic-line contacts. Dimca–Ilardi–Pokora–Sticlaru explicitly study this degree-twelve divisor and its characteristic-zero freeness properties. The dual-Hesse line incidence type itself is classical, and Kühne–Szemberg–Tutaj-Gasińska discuss its realizability over various characteristics; none of those facts is claimed as newly discovered here. The contribution isolated here is the exact specialization of the fixed integral **cubic-and-nine-tangent divisor** in characteristic two, and the complete rational-geometric singular-support spectrum for all prime reductions where the divisor remains reduced. Literature comparisons are not proofs of novelty, and possible earlier implicit arithmetic deductions remain a residual risk.

## Limitations

Characteristic three is excluded because the displayed integral equation becomes nonreduced there. This result counts reduced geometric singular-point supports only, and makes no assertion about embedded singular schemes, total Tjurina numbers, freeness after reduction, or alternative models. In characteristic two, no characteristic-zero ADE label is attached to the triple-contact singularities.

## References

1. Przemysław Talar, *On cubic-line arrangements with simple singularities*, arXiv:2305.01530v2 (first posted 2023-05-02), Sections 1 and 3. https://arxiv.org/html/2305.01530v2
2. Alexandru Dimca, Giovanna Ilardi, Piotr Pokora, Gabriel Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117v4 (first posted 2023-01-03), Theorem 1.7 and the Fermat cubic example. https://arxiv.org/html/2301.01117v4
3. Lukas Kühne, Tomasz Szemberg, Halszka Tutaj-Gasińska, *Line arrangements with many triple points*, Rend. Circ. Mat. Palermo (2024), §2.2, DOI:10.1007/s12215-024-01047-x. https://link.springer.com/article/10.1007/s12215-024-01047-x
4. Magdalena Lampa-Baczyńska, Daniel Wójcik, *On the dual Hesse arrangement* (2019), DOI:10.18778/8142-814-9.12, bibliographic/abstract comparison only.
