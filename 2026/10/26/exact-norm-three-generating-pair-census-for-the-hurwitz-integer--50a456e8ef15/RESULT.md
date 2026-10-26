# Exact norm-three generating-pair census for the Hurwitz integer order

## Finding

Let \(\mathcal H=\mathbb Z\langle1,i,j,h\rangle\), where \(h=(1+i+j+k)/2\), \(i^2=j^2=k^2=ijk=-1\), be the classical Hurwitz **integer** order in the rational Hamilton quaternion division algebra of discriminant \(2\). Write \(S=\{x\in\mathcal H:\operatorname{nrd}(x)=3\}\). Exactly \(960\) ordered pairs \((x,y)\in S\times S\) generate \(\mathcal H\) as a unital \(\mathbb Z\)-algebra, out of \(|S|^2=96^2\) possible ordered pairs.

For any fixed \(x\in S\), the number \(g(x)=\#\{y\in S:\mathbb Z[x,y]=\mathcal H\}\) depends only on its absolute reduced trace:

\[
\begin{array}{c|rrrr}
|\operatorname{trd}(x)|&3&2&1&0\\\hline
\#\{x\in S\}&16&24&48&8\\
 g(x)&36&8&4&0
\end{array}
\]

Thus every generating pair has at least one member of absolute trace \(3\). Under simultaneous conjugation by the \(24\)-element unit group \(\mathcal H^\times\), the generating pairs form exactly \(80\) orbits, of respective numbers \(48,16,16\) for first-generator absolute trace \(3,2,1\). For example \(x=(3+i+j+k)/2\) and \(y=(3+i+j-k)/2\) generate the entire order.

## Assumptions and scope

All rings and subalgebras are unital. The reduced norm is \(\operatorname{nrd}(a+bi+cj+dk)=a^2+b^2+c^2+d^2\); the reduced trace is \(\operatorname{trd}(a+bi+cj+dk)=2a\). An element belongs to \(\mathcal H\) exactly when its four standard coordinates are all integers or are all half-integers with odd doubled coordinates. The result is an exact finite classification at norm \(3\), the smallest positive \(3\)-power norm; it does not assert analogous counts for higher norms or other quaternion orders. The unrelated Hurwitz quaternion order over a cubic real field is not the object considered here.

## Proof

**Algebra reduction.** For any \(x,y\in\mathcal H\), Cayley–Hamilton gives \(x^2=\operatorname{trd}(x)x-\operatorname{nrd}(x)\) and the analogous equation for \(y\). Direct quaternion multiplication gives
\[
yx=\operatorname{trd}(x)y+\operatorname{trd}(y)x-\operatorname{trd}(x\bar y)-xy.
\]
All coefficients are integers because the reduced traces and polarizations of the integral reduced norm are integers on \(\mathcal H\). It follows by multiplication on the left by \(x\) and \(y\) that \(M=\mathbb Z\langle1,x,y,xy\rangle\) is stable under both multiplications. Indeed \(x(xy)=x^2y\in M\), while \(y(xy)=(yx)y\in M\) after using the displayed identity and the quadratic identity for \(y\). Therefore \(M=\mathbb Z[x,y]\).

Write \(x=(u_0+u_1i+u_2j+u_3k)/2\), \(y=(v_0+v_1i+v_2j+v_3k)/2\), where \(u,v\in\mathbb Z^4\) satisfy \(\sum u_r^2=\sum v_r^2=12\), with the four entries of each tuple congruent modulo \(2\). Put \(U=(u_1,u_2,u_3)\), \(V=(v_1,v_2,v_3)\) and
\[
Q(U,V)=\sum_{1\le a<b\le3}(u_av_b-u_bv_a)^2=\|U\times V\|^2.
\]
In the standard real quaternion coordinates, the absolute determinant of \((1,x,y,xy)\) is \(\|(U/2)\times(V/2)\|^2=Q(U,V)/16\); the lattice covolume of \(\mathcal H\) is \(1/2\). Thus the index of \(M\) in \(\mathcal H\), when finite, is \(Q(U,V)/8\); when \(Q=0\), \(M\) has rank less than four. In all cases, \(\mathbb Z[x,y]=\mathcal H\) **if and only if** \(Q(U,V)=8\). Equivalently, \(\operatorname{nrd}([x,y])=2\), the minimal commutator-norm condition in discriminant \(2\).

**Trace rigidity.** The possible values of \(|u_0|\) are \(3,2,1,0\), with respective numbers of first coordinates \(16,24,48,8\) in \(S\). The corresponding squared imaginary lengths are \(3,8,11,12\). Since \(Q(U,V)=|U|^2|V|^2-(U\cdot V)^2\), the equation \(Q=8\) requires that the product of the two squared lengths minus \(8\) be a perfect square. From the four possibilities \(3,8,11,12\), the only possible unordered pairs are \((3,3)\), \((3,8)\), \((3,11)\), for which \(|U\cdot V|\) must be respectively \(1,4,5\). Thus at least one of \(|\operatorname{trd}(x)|\), \(|\operatorname{trd}(y)|\) equals \(3\), and the other is nonzero.

**Exact partner counts.** Signed coordinate permutations of \(U\) permit representatives \((1,1,1)\), \((2,2,0)\), \((3,1,1)\), \((2,2,2)\) for the four absolute traces. For \(U=(1,1,1)\), the cases \(|v_0|=3,2,1\) each contribute exactly \(12\) vectors \(v\): respectively \(6\) imaginary sign patterns for each sign of \(v_0\), \(3\) positions times \(2\) aligned patterns for each sign, and \(3\) positions times \(2\) aligned patterns for each sign. For \(U=(2,2,0)\), only \(|v_0|=3\) contributes, with \(8\) vectors. For \(U=(3,1,1)\), only \(|v_0|=3\) contributes, with \(4\) vectors. For \(U=(2,2,2)\), none contributes. The total is therefore
\[
16\cdot36+24\cdot8+48\cdot4+8\cdot0=960.
\]

**Conjugacy orbits.** The norm-one unit group \(\mathcal H^\times\) has \(24\) elements (eight integral Lipschitz units and sixteen half-integral units). If a unit fixes a generating ordered pair under simultaneous conjugation, it centralizes \(x\) and \(y\), hence all of \(\mathcal H\), so lies in its center \(\mathbb Z\). The only central units are \(\pm1\). Every orbit thus has cardinality \(24/2=12\). Dividing the trace-stratified counts by \(12\) yields \(48,16,16\) orbits and \(80\) in total.

## Verification

The self-contained Python standard-library script `verify.py` enumerates all integer quadruples with squared length \(12\) and common parity, checks \(|S|=96\), independently computes the index of \(\mathbb Z\langle1,x,y,xy\rangle\) by a determinant in the \((1,i,j,h)\) lattice basis for all \(9216\) ordered pairs, compares that determinant to the \(Q/8\) criterion, and checks the exact per-trace counts \((36,8,4,0)\), total \(960\), and orbit sizes. It prints `VERIFY_OK` if all assertions hold. The symbolic proof of the index criterion and the finite case split above are essential; the script is an exhaustive finite check, not evidence about other norms.

## Relationship to prior work

Eisenträger, Goren, Iezzi, Kir, Kırımlı, Love, Mahaney, Park and Sabitova, *Generating sets for maximal orders in rational quaternion algebras*, arXiv:2610.10139v1 (first posted October 7, 2026), prove general existence/bounds for generators of prime-power norms (Theorems 1.1, 1.2 and 8.2). Their Remark 8.3 relates two-generator rings to commutator norm, and their Section 7 includes the classical theta count of norm-\(3\) elements for the discriminant-\(2\) maximal order. Neither statement counts the generating ordered pairs at the first norm \(3\), identifies their exact trace obstruction, or classifies their conjugation orbits. The present count uses the classical commutator criterion but adds its exact small-norm incidence profile. Goren and Love, *On elements of prescribed norm in maximal orders of a quaternion algebra* (arXiv:2307.16828; Canadian Journal of Mathematics, 2025), concern norm-restricted spanning sets, lattice minima, and determination by theta functions rather than the incidence of two-element generating pairs.

## Limitations

This is an exact local finite case for a unique classical maximal order, not a uniform theorem for arbitrary discriminants, primes, or exponents. General commutator criteria and the number of norm-\(3\) elements are known: novelty is restricted to the sharp trace-stratified two-generator census and its unit-conjugation orbit count. Unindexed computational tables or earlier explicit enumerations may contain the same numbers; no claim of exhaustively excluding all such sources is made. Independent audit has not been performed.

## References

1. K. Eisenträger et al., *Generating sets for maximal orders in rational quaternion algebras*, arXiv:2610.10139v1 (October 7, 2026), https://arxiv.org/abs/2610.10139 ; lawful author manuscript https://jonathanlove.info/egikklmps.pdf . Especially Sections 7–9 and Remark 8.3.
2. E. Z. Goren and J. R. Love, *On elements of prescribed norm in maximal orders of a quaternion algebra*, arXiv:2307.16828 (2023); *Canadian Journal of Mathematics* 77 (2025), 1938–1965, https://doi.org/10.4153/S0008414X24000592 . Especially Sections 2–3.
3. J. Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (2021), for the classical Hurwitz integer order and quaternion order theory.
