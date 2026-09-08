# Line non-Lefschetz locus of the symmetric ACI Q[x,y,z]/(x^3,y^3,z^3,xyz) is the whole P^2

## Context

For a graded Artinian algebra A over a field of characteristic zero, a linear
form l is a Lefschetz element if every multiplication map
x l : [A]_i -> [A]_{i+1} has maximal rank. The Lefschetz elements form a
Zariski-open set; its complement in P([A]_1) is the non-Lefschetz locus N(A).
Boij-Migliore-Miro-Roig-Nagel completely describe N for monomial complete
intersections and prove expected codimension for general complete
intersections. Cook-Nagel classify type-two WLP via combinatorial
determinants. Booth-Vraciu give a fixed-general-L determinant criterion for
level monomial almost complete intersections but publish no varying-[a:b:c]
locus equations, codimension, or degree. No prior source records the line
locus of the symmetric 4-generator cubic ACI below.

## Definitions

Let A0 = Q[x,y,z]/(x^3,y^3,z^3,xyz).
A monomial x^a y^b z^c lies in the ideal iff some exponent is >= 3 or all
three are >= 1. Let L = a*x + b*y + c*z with [a:b:c] in P^2 and let
M_i(a,b,c) be the parameterized Macaulay matrix of x L : [A0]_i -> [A0]_{i+1}
in monomial bases. Let F_i be the Fitting ideal of maximal minors of M_i.

## Result

1. A0 is Artinian with Hilbert function (1,3,6,6,3) (total dimension 19,
   socle degree 4), level of type 3 (socle equals all of [A0]_4).
2. For every [a:b:c] in P^2, x L : [A0]_2 -> [A0]_3 (6 -> 6) has rank <= 5,
   hence never maximal. Every linear form fails WLP at degree 2 -> 3.
   The line non-Lefschetz locus is N(A0) = P^2 (codimension 0).
3. At L = x+y+z the graded ranks in degrees 0..3 are 1,3,5,3; WLP FAILS with
   kernel witness f = x^2 - x*y + y^2 - x*z - y*z + z^2 in [A0]_2, xL(f) = 0.
4. The Jordan partition of x(x+y+z) on the 19-dimensional A0 is
   [5,4,4,2,2,1,1] (7 blocks, largest 5), from exact ker L^k dimensions
   7,12,15,18,19 (k=1..5), L^5 = 0 != L^4.

## Proof / evidence

Bases: survivors are exponent triples in {0,1,2}^3 with a zero coordinate;
counting gives graded dimensions 1,3,6,6,3. Each of x^2y^2, x^2z^2, y^2z^2
times x,y,z is a cube or an xyz-multiple, so all of [A0]_4 is socle; every
monomial of degree <= 3 has a surviving multiple, so no socle below 4.

Order the degree-2 basis (x^2,x*y,y^2,x*z,y*z,z^2) and degree-3 basis
(x^2y,x*y^2,x^2z,y^2z,x*z^2,y*z^2). Then

M_2(a,b,c) = [[b,a,0,0,0,0],[0,b,a,0,0,0],[c,0,0,a,0,0],
              [0,0,c,0,b,0],[0,0,0,c,0,a],[0,0,0,0,c,b]].

Row supports: r0 in {c0,c1}, r1 in {c1,c2}, r2 in {c0,c3}, r3 in {c2,c4},
r4 in {c3,c5}, r5 in {c4,c5}. A permutation contributing to det must pick
distinct columns: if sigma(0)=0 then sigma(2)=3, sigma(4)=5, sigma(5)=4,
sigma(3)=2, sigma(1)=1, giving sigma=(0,1,3,2,5,4) of sign + (2 inversions)
and product b*b*a*c*a*c = a^2b^2c^2; if sigma(0)=1 then sigma(1)=2,
sigma(3)=4, sigma(5)=5, sigma(4)=3, sigma(2)=0, giving tau=(1,2,0,4,3,5) of
sign - (3 inversions) and product a*a*c*b*c*b = a^2b^2c^2. No other choice
exists, so det M_2 = a^2b^2c^2 - a^2b^2c^2 = 0 identically (exhaustion over
all 720 permutations confirms exactly these two nonzero terms). Hence
rank M_2(a,b,c) <= 5 < 6 at every [a:b:c]: N(A0) contains V(Fitting_2) = P^2,
so N(A0) = P^2.

Fitting scheme remark: F_2 = (det M_2) = (0); the degree-2 degeneracy locus
alone is the whole plane. F_1 contains a^3,b^3,c^3 (3x3 minors on the stated
row triples of M_1), so V(F_1) is empty. All 36 five-by-five minors of M_2
are nonzero monomials (machine-checked, each a single permutation term), so
generic rank is exactly 5.

Single-L certificate: at (1,1,1) exact rational elimination gives ranks
1,3,5,3; M_2(1,1,1)*(1,-1,1,-1,-1,1)^T = 0.

Jordan form: exact 19x19 rational nullities dim ker L^k = 7,12,15,18,19;
block sizes from successive differences give [5,4,4,2,2,1,1].

What is proof vs computation: bases/Hilbert/socle counts, the M_2 matrix,
the two-permutation determinant cancellation, the single-L kernel vector,
and the M_1 minors a^3,b^3,c^3 are hand-checkable. The 720-permutation scan,
all-36-minors check, 19x19 Jordan nullities, and rank table are exact
rational machine computations replayable stdlib-only. No conjecture remains.

## Limitations

No claim beyond this single ideal A0. Sub-loci where rank drops below 5
(coordinate lines/points) are not classified; they are not needed since
det == 0 already forces failure everywhere. The Jordan partition is
machine-certified exact rational linear algebra, not hand-computed.

## Reproducibility

Run `python3 artifacts/verify_A0.py` (stdlib only: fractions, itertools).
It replays monomial bases, Hilbert function, socle, det M_2 == 0 via
permutation expansion, all 36 nonzero 5x5 minors, single-L ranks and kernel
witness, and Jordan nullities/partition. Expected output ends with
ALL CHECKS PASSED. Independently: rebuild M_i in any CAS from the monomial
bases, recompute the maximal minors, and verify the two inclusions
(det == 0 gives N = P^2; one evaluated point per component plus rank checks).

## References

- M. Boij, J. Migliore, R. M. Miro-Roig, U. Nagel, The non-Lefschetz locus,
  arXiv:1609.00952.
- D. Cook II, U. Nagel, The weak Lefschetz property for monomial ideals of
  small type, arXiv:1507.03853.
- M. D. Booth, A. Vraciu, The generators of a colon ideal with an
  application to the weak Lefschetz property for monomial almost complete
  intersections in three variables, arXiv:2603.11491.
- E. Marangone, The non-Lefschetz locus of conics, arXiv:2404.16238.
