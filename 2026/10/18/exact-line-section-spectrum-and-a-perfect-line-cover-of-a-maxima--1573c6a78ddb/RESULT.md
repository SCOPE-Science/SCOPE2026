# Exact line-section spectrum and a perfect line cover of a maximal plane quartic

## Finding

Let \(k=\mathbb F_5[u]/(u^2-2)\), let \(c=1+2u\in k\), and let \(C\subset\mathbb P^2_k\) be the quartic
\[
X^4+Y^4+Z^4+c(X^2Y^2+Y^2Z^2+Z^2X^2)=0.
\]
For \(j\in\{0,1,2,3,4\}\), let \(n_j\) be the number of \(k\)-rational projective lines containing exactly \(j\) distinct points of \(C(k)\). Then \(C\) is a smooth genus-three curve with \(56\) points, and
\[
(n_0,n_1,n_2,n_3,n_4)=(63,168,196,0,224).
\]
Every point of \(C(k)\) is incident to exactly three rational unisecants, seven bisecants, and sixteen four-secants. In particular, the four-secants admit a matching of size \(14\) whose members partition the \(56\) points. Hence the exact rational line-cover number is
\[
\operatorname{cov}_k(C)=14=|C(k)|/4.
\]
Here \(\operatorname{cov}_k(C)\) is the smallest number of \(k\)-rational projective lines whose union contains \(C(k)\). The curve is a characteristic-five Klein quartic Ciani model; its point count attains the Hasse–Weil bound for genus three over \(k\).

## Assumptions and scope

All curves, points, and lines in the theorem are over the explicitly presented field \(k\) of order \(25\); geometric smoothness is asserted over an algebraic closure. Write an element uniquely as \(a+bu\), with \(0\leq a,b\leq4\), and encode it by the integer \(a+5b\in\{0,\ldots,24\}\). An encoded line triple \((A,B,D)\) denotes the equation \(AX+BY+DZ=0\), with each coefficient decoded in this convention. The same convention encodes affine point coordinates \((1,Y,Z)\). This encoding is not ordinary arithmetic modulo \(25\).

The following fourteen encoded coefficient triples constitute a completely explicit covering certificate:

```text
(1, 0, 11)    (1, 1, 13)    (1, 2, 1)    (1, 2, 3)
(1, 5, 8)     (1, 8, 5)     (1, 10, 21)  (1, 11, 8)
(1, 13, 19)   (1, 15, 15)   (1, 16, 6)   (1, 19, 0)
(1, 19, 13)   (1, 23, 3)
```

The accompanying `verify.py` contains, independently of its projective-plane enumeration, the four encoded rational point coordinates for each of these lines. Thus the lower-bound and upper-bound arguments do not depend on optimization software or a nonexhaustive numerical search.

## Proof

**Smoothness.** The partial derivative with respect to \(X\) is \(2X(2X^2+c(Y^2+Z^2))\), with cyclic analogues. If all three coordinates of a singular point were nonzero, the vector \((X^2,Y^2,Z^2)\) would lie in the kernel of the matrix with diagonal entries \(2\) and off-diagonal entries \(c\). Its eigenvalues are \(2-c\), twice, and \(2+2c\), once. All are nonzero because \(c\notin\mathbb F_5\). If exactly one coordinate vanished, the remaining two squares would lie in the kernel of a two-by-two matrix with diagonal \(2\) and off-diagonal \(c\), whose determinant \(4-c^2\) is nonzero. If two coordinates vanished, the quartic equation would force the third to vanish. Hence \(C\) is geometrically smooth. A smooth plane quartic has genus \(3\) and is geometrically irreducible.

**Explicit saturated line cover.** In `verify.py`, `WITNESS` lists the fourteen line triples above, and `WITNESS_AFFINE` lists four points on each line. Using the field multiplication law
\[
(a+bu)(d+eu)=(ad+2be)+(ae+bd)u,
\]
straight substitution checks that each of the fifty-six listed points satisfies both the quartic and its assigned line equation; no two listed points coincide. This is a finite exact certificate, with no numerical approximations. Hasse–Weil bounds the total number of rational points of any smooth genus-three curve over \(\mathbb F_{25}\) by
\[
25+1+2\cdot3\cdot5=56.
\]
Thus the fifty-six certified points exhaust \(C(k)\), the curve is maximal, and the fourteen lines cover it without overlap. By Bézout, any line has at most four distinct intersections with \(C\), so any line cover contains at least \(\lceil56/4\rceil=14\) lines. Equality proves the covering-number statement.

**Complete rational line spectrum.** Every rational projective point, and dually every rational projective line, has a unique normalized triple either \((1,a,b)\), \((0,1,b)\), or \((0,0,1)\) with \(a,b\in k\). There are \(25^2+25+1=651\) triples. The exact independent enumeration in `verify.py` evaluates the quartic on all such point representatives, and each of the \(651\) line equations on the resulting \(56\) curve points. Its histogram is precisely the asserted \((63,168,196,0,224)\), and its point-by-point tallies yield the asserted incidences. As structural crosschecks, the histogram satisfies
\[
168+2\cdot196+4\cdot224=56\cdot26,
\qquad
196+6\cdot224={56\choose2},
\]
counting point–line and unordered point-pair–line incidences in two ways.

## Verification

Run `python3 verify.py` with the Python standard library; no external dependency, solver, random seed, network access, or precomputed table is required. It constructs \(\mathbb F_{25}\) by its displayed irreducible polynomial, checks the fixed independent fifty-six-point witness and fourteen line equations, enumerates all \(651\) projective points and lines, verifies the complete spectrum and the per-point incidences, and checks the two counting identities. It terminates with three `PASS` messages or raises an assertion. The algebraic smoothness argument and Bézout/Hasse–Weil inequalities above supply the noncomputational parts of the proof.

## Relationship to prior work

Asgarli, Dassarma, Ghioca, MacLean and Stokdyk explicitly ask for the exact covering number of rational plane-curve points by rational lines and obtain an asymptotic upper bound for reflexive curves over sufficiently large fields. Their general asymptotic statement does not determine a perfect cover or an exact incidence spectrum at field order \(25\). Tafazolian's recent classification identifies the maximal genus-three Klein quartic as the exceptional transitive maximal case in odd characteristic. Dolgachev and Martin describe the Klein quartic in the Ciani pencil with parameter \(\frac32(-1\pm\sqrt{-7})\); the chosen \(c\) satisfies its characteristic-five parameter polynomial \(c^2+3c+18=0\). These geometric and classification results do not supply the fourteen-line partition or the enumerated line-section spectrum in the portions available for comparison. Prior work on completely split line sections and on Klein-quartic twists addresses counts, monodromy, or arithmetic twists rather than the exact global covering asserted here. Literature on complete projective k-arcs in the plane of order 25 concerns point sets with no three collinear and does not give the four-secant partition of this quartic.

## Limitations

The cover and spectrum concern the explicit characteristic-five canonical plane model, not an arbitrary plane quartic, arbitrary embedding, or a uniform family of finite fields. The spectrum is established by exhaustive exact finite enumeration, not by a closed character-theoretic formula. The original full text of one closely related recent classification could not be inspected; an unindexed equivalent finite-geometry description remains a literature risk. This is a mathematical proof and reproducible finite certificate, not a claim of independent audit or external certification.

## References

1. S. Asgarli, S. Dassarma, D. Ghioca, S. MacLean, E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1 (first submitted 2026-10-09), in particular Question 1.1 and Theorem 1.2.
2. S. Tafazolian, *Transitive automorphism groups of maximal curves*, arXiv:2609.17611v1 (first submitted 2026-09-14), abstract and classification statement.
3. I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, arXiv:2303.16170v2 (2023), Section 4.2, especially the Ciani Klein model.
4. K. Coolsaet and H. Sticker, *A full classification of the complete k-arcs of PG(2,23) and PG(2,25)*, Journal of Combinatorial Designs 17 (2009), 459–477, DOI 10.1002/jcd.20211 (distinct notion of arc).
5. F. Fité, E. Lorenzo García and A. V. Sutherland, *Sato–Tate distributions of twists of the Fermat and the Klein quartics*, Research in the Mathematical Sciences 5 (2018), 41, DOI 10.1007/s40687-018-0162-0.
