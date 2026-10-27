# A perfect fourteen-line partition of the maximal Klein quartic over twenty-five elements

## Finding

Let \(k=\mathbb F_5[u]/(u^2-3)\cong\mathbb F_{25}\), set \(t=1+4u\), and let \(C\subset\mathbb P^2_k\) be the plane quartic

\[
X^4+Y^4+Z^4+t(X^2Y^2+Y^2Z^2+Z^2X^2)=0.
\]

For an \(k\)-rational projective line \(L\), define \(r(L)=\#(L(k)\cap C(k))\). Then \(C\) is smooth of genus three with \(\#C(k)=56\). Among the \(651\) distinct \(k\)-lines the complete intersection-size spectrum is

\[
\bigl(\#\{L:r(L)=0\},\ldots,\#\{L:r(L)=4\}\bigr)
=(63,168,196,0,224).
\]

Furthermore \(C(k)\) admits a partition into exactly fourteen disjoint four-point line sections. If \(\tau(C)\) is the minimum number of \(k\)-lines whose union contains \(C(k)\), then

\[
\boxed{\tau(C)=14=\frac{\#C(k)}{\deg C}.}
\]

The point count meets the genus-three Hasse--Weil bound; hence this curve realizes the exceptional \(\mathbb F_{25}\)-maximal genus-three Klein quartic discussed in the recent classification of transitive maximal curves.

## Assumptions and scope

The ground field has exactly \(25\) elements and characteristic five. Its displayed quadratic presentation is a field because \(3\) is not a square in \(\mathbb F_5\). The equation and all the lines are defined over this field. By a line section we mean its *distinct rational points*, not a divisor with multiplicity. Each point and each line is counted only once, up to multiplication of homogeneous coordinates by an element of \(k^\times\).

The covering number is for the canonical plane embedding of this smooth genus-three curve; no claim is made about coverings by higher-degree curves, planes over extensions, or other embeddings. The general question of covering rational points of plane curves by rational lines appears in Asgarli--Dassarma--Ghioca--MacLean--Stokdyk (2026).

## Proof

**Smoothness.** The gradient of the homogeneous quartic is

\[
\frac{\partial F}{\partial X}=2X\bigl(2X^2+t(Y^2+Z^2)\bigr),
\]

with cyclic analogues. Because \(t\notin\mathbb F_5\), we have \(t^2\ne4\), \(t\ne2\), and \(t\ne-1\). At a point having one nonzero coordinate the corresponding derivative is nonzero. At a point having exactly two nonzero coordinates, simultaneous vanishing of those two derivatives forces the determinant \(4-t^2\) to vanish, a contradiction. When all three coordinates are nonzero, the three derivatives give a homogeneous linear system in \(X^2,Y^2,Z^2\), with coefficient matrix having diagonal \(2\) and off-diagonal \(t\). Its determinant is \((2-t)^2(2+2t)\ne0\); therefore no such projective singular point exists. Thus \(C\) is geometrically smooth. A smooth projective plane curve of degree four is geometrically integral, of genus \((4-1)(4-2)/2=3\).

**Exhaustive finite-field count.** Encode the field element \(a+bu\) as the integer \(a+5b\), for \(0\le a,b<5\). Addition and multiplication in this representation are given exactly by

\[
(a+bu)(c+du)=(ac+3bd)+(ad+bc)u,
\]

with coefficients reduced modulo five. Every projective point has precisely one representative in the disjoint sets

\[
(1:y:z)\ (y,z\in k),\quad (0:1:z)\ (z\in k),\quad (0:0:1).
\]

There are \(25^2+25+1=651\) such triples. The same normalization enumerates every dual point representing a rational line. The standalone, dependency-free `CHECK.py` implements precisely these finite loops, tests the polynomial at every representative, and counts the rational curve points on every line by the exact equation \(\ell_X X+\ell_Y Y+\ell_Z Z=0\). Exhaustive enumeration yields precisely \(56\) curve points and the spectrum \((63,168,196,0,224)\). The independent incidence identities

\[
\sum_{j=0}^4 jN_j=56(25+1)=1456,
\qquad
\sum_{j=0}^4\binom j2N_j=\binom{56}{2}=1540
\]

also hold. These are *finite exhaustive computations*, not estimates of an unbounded problem.

**Fourteen-line upper certificate.** In the above integer encoding, the following fourteen coefficient triples \((\ell_X,\ell_Y,\ell_Z)\) represent distinct \(k\)-lines \(\ell_XX+\ell_YY+\ell_ZZ=0\):

```text
(1, 0,16)  (1, 0,18)  (1, 2,18)  (1, 3, 3)
(1, 4,15)  (1, 7, 9)  (1,12,13)  (1,17, 9)
(1,17,11)  (1,18,18)  (1,20,16)  (1,23, 1)
(1,23,22)  (1,24, 3)
```

Their respective four-element sets of indices in the canonical ordered list of the \(56\) rational points are

```text
[ 2, 8,46,54]  [16,21,39,42]  [10,14,22,52]  [20,23,28,31]
[ 5, 9,38,51]  [12,40,44,49]  [ 6,33,41,47]  [ 7,15,24,29]
[11,35,37,48]  [ 1,19,25,30]  [17,34,36,50]  [ 3,18,26,45]
[13,27,53,55]  [ 0, 4,32,43]
```

These sets are pairwise disjoint and their union is the full index set \(\{0,\ldots,55\}\). Each entry can be independently reconstructed using the enumerator in `CHECK.py`, which checks all fourteen lines directly. Hence fourteen lines cover all \(56\) rational curve points.

**Sharp lower bound.** Since \(C\) is smooth and geometrically irreducible of degree four, it has no line component. Bézout's theorem bounds the number of distinct intersection points on any line by four. Thus any line cover needs at least \(\lceil56/4\rceil=14\) lines. Together with the explicit partition this proves \(\tau(C)=14\). Because \(56=25+1+2\cdot3\cdot5\), the curve meets the Hasse--Weil maximal bound for genus three over \(\mathbb F_{25}\).

## Verification

Run `python3 CHECK.py` from the directory containing this document and the checker. The program performs all finite field operations by elementary integer arithmetic; it uses neither random sampling nor a numerical solver. It independently enumerates every rational projective point and dual line, verifies the four possible line intersection sizes, checks both incidence counts, and checks the displayed fourteen-line partition. The expected terminal line is `optimal_line_cover=14, each line meets curve in 4 distinct rational points`. The proof of smoothness and the Bézout lower bound are mathematical arguments separate from enumeration.

## Relationship to prior work

Tafazolian (arXiv:2609.17611v1, Theorem 1.1) classifies maximal curves whose automorphism groups act transitively on rational points and identifies the exceptional \(\mathbb F_{25}\)-maximal genus-three Klein quartic with \(56\) points. That classification does not state its precise rational-line intersection spectrum or exhibit an optimal disjoint line cover. Asgarli et al. (arXiv:2610.13042v1) develop asymptotically sharp line-cover bounds for plane curves over sufficiently large finite fields, but do not imply this exact small-field cover. Makhul--Schicho--Gallet (arXiv:1711.06021v3) establish limiting distributions of line intersection types over field extensions, rather than the present exact base-field spectrum or line partition. The finite exact result here is a specialization to a distinguished geometric object, not an improvement claimed for general plane curves.

## Limitations

The result supplies one minimal cover, not the number or orbit structure of *all* minimal covers. No statement is made for arbitrary maximal genus-three models over different finite fields, or for larger base fields. The exact finite-field counts are justified by exhaustive certificate code and a transparent enumeration domain; they are not replaced by a symbolic closed-form count. The comparison with prior literature supports priority only at the level of inspected material and targeted searches; implicit coverage in broader finite-geometry or algebraic-geometric-code tables remains a residual risk. Independent mathematical audit has not been performed.

## References

1. Saeed Tafazolian, *Transitive automorphism groups of maximal curves*, arXiv:2609.17611v1 (first public version: 2026-09-14). https://arxiv.org/abs/2609.17611
2. Shamil Asgarli, Sarthak Dassarma, Dragos Ghioca, Simon MacLean, Evan Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1 (first public version: 2026-10-09). https://arxiv.org/abs/2610.13042
3. Mehdi Makhul, Josef Schicho, Matteo Gallet, *Probabilities of incidence between lines and a plane curve over finite fields*, arXiv:1711.06021v3 (2021 revision; earlier first public version 2017). https://arxiv.org/abs/1711.06021
