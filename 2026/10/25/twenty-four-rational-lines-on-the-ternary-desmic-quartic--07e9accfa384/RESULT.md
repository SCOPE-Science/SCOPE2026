# Twenty-four rational lines on the ternary desmic quartic

## Finding
Let \(k=\mathbb F_3\) and define the quartic surface
\[
X:\quad F(x_0,x_1,x_2,x_3)=\sum_{0\le i<j\le3}x_i^2x_j^2=0 \subset\mathbb P^3_k.
\]
In the standard desmic pencil (defined below), \(X\) is the sole \(k\)-rational member other than its three reducible tetrahedra. It has \(28\) \(k\)-points, consisting of \(12\) ordinary double points and \(16\) smooth points. Its entire set of \(k\)-defined projective lines has cardinality \(24\): the standard \(16\) Reye lines plus exactly \(8\) further lines disjoint from the singular set. Each of the \(12\) nodes is incident with four of these lines, while each of the \(16\) smooth \(k\)-points is incident with precisely three, including one Reye line and two of the extra lines.

## Assumptions and scope
All assertions about points and lines, unless explicitly called geometric, refer to objects rational over \(k=\mathbb F_3\). The claim does not count all lines over \(\overline{k}\). The three quadratic pair-partition quartics are
\[
A=(x_0^2+x_1^2)(x_2^2+x_3^2),\quad B=(x_0^2+x_3^2)(x_1^2+x_2^2),\quad C=(x_0^2+x_2^2)(x_1^2+x_3^2).
\]
The desmic pencil is \(aA+bB+cC=0\) subject to \(a+b+c=0\), with parameters \([a:b:c]\in\mathbb P^1(k)\).

## Proof
**The unique member.** The pencil has exactly four rational parameter values. Three have one coefficient zero, and their equations factor into pairs of differences of squares, hence are unions of four planes (tetrahedra). The remaining value is \([a:b:c]=[1:1:1]\); it is permitted because \(3=0\) in \(k\). Each cross term \(x_i^2x_j^2\) appears twice in \(A+B+C\), so \(A+B+C=2F\). The resulting surface has only finitely many singular points as calculated below and cannot be a reducible union of positive-degree surfaces, whose components intersect along a curve. Thus this is the sole irreducible rational member.

**Singular locus.** Set \(S=\sum_i x_i^2\). In characteristic three, \(F=\sum_i x_i^4-S^2\), so \(\partial F/\partial x_i=x_i(x_i^2-S)\). Over the algebraic closure a nonzero singular point has \(S\ne0\), and every nonzero coordinate has square \(S\). If \(r\) coordinates are nonzero, then \(S=rS\); hence \(r\equiv1\pmod3\). Thus \(r=1\) (four coordinate points) or \(r=4\) (eight sign points, projectively represented by \([1:\pm1:\pm1:\pm1]\)). They all lie on the quartic. At a coordinate point the local quadratic term in the other three coordinates is a nondegenerate diagonal form. At a sign point, in a chart fixing the first coordinate the Hessian of the dehomogenized equation has zero diagonal and pairwise off-diagonal entries the products of the corresponding signs; its determinant equals twice the product of its three off-diagonal entries, which is nonzero in \(k\). All twelve are geometrically ordinary double points.

**Point count.** For a rational point let \(r\) be the number of nonzero coordinates. As every nonzero square is \(1\), \(F=\binom r2\) in \(k\); thus \(r=1,3,4\). Their projective counts are respectively \(4,\binom43 2^2=16,2^3=8\). Hence \(\#X(k)=28\), of which the \(r=3\) points are smooth.

**The line families.** For every coordinate vector \(e_i\), adjoining a vector with zero \(i\)-th coordinate and all three others in \(\{\pm1\}\) defines a line on \(X\). There are four choices up to sign for each \(i\), giving sixteen distinct Reye lines. Indeed along such a line the quartic becomes \(3s^2t^2+3t^4=0\). Each contains exactly three nodes and one smooth rational point; every node lies on four such lines.

The eight additional lines have the reduced row-echelon spanning pairs
\[
(1,0,a,b),\qquad(0,1,c,d),\qquad a,b,c,d\in\{1,-1\},\quad ac+bd=0.
\]
For each of the four choices of \((a,b)\) there are exactly two orthogonal choices of \((c,d)\). Substitution \((s,t,as+ct,bs+dt)\) into the quartic yields zero identically: its coordinate-square sum is zero, and its sum of fourth powers vanishes because \(1+a^4+b^4=0\), \(1+c^4+d^4=0\), and \(ac+bd=0\), with the middle binomial coefficient divisible by three. Each such line consists of four smooth rational points.

**Exhaustiveness and incidence.** Every rational projective line corresponds uniquely to a \(2\times4\) rank-two reduced row-echelon matrix over \(k\). There are exactly \(\binom42_k=130\) such matrices. Expanding \(F(su+tv)\) into its five homogeneous coefficients and testing all 130 matrices gives exactly the 24 lines described above, with sixteen meeting the node set in three points and eight meeting it in none. The exhaustive, pure-Python certificate `verify.py` constructs every row-echelon basis, checks all five coefficients, checks all incidences, and repeats the inclusion test of the eight additional lines at a point with coordinates in \(\mathbb F_9\). It finds each node on four lines and each smooth rational point on three. In total, the smooth-point incidences are sixteen from the Reye family plus thirty-two from the extra family; the direct certificate establishes the per-point counts, not merely these totals.

## Verification
From the included package directory, run `python3 verify.py` with a standard Python 3 interpreter. The expected last line begins with `VERIFY_OK`. All finite-field operations are exact integers reduced modulo three. The independent \(\mathbb F_9\) check uses \(\alpha^2=2\). The exhaustive test is complete for \(k\)-rational lines; it is not a geometric search over all extensions.

## Relationship to prior work
The classical desmic configuration of twelve nodes and sixteen Reye lines is **not new**. Dolgachev–Kondō (arXiv:2505.01033, Proposition 3.1 and equation (1)) identify that configuration and the desmic pencil. Eklund (arXiv:1010.4058, first submitted 2010-10-19) studies Heisenberg-invariant quartics and line configurations in characteristic zero, but does not determine this characteristic-three rational-line incidence. The separate degree-six K3 surfaces of Degtyarev–Dolgachev–Kondō (arXiv:2505.16497) also possess a 24-line configuration, but are not this quartic in \(\mathbb P^3\). The additional eight rational lines, full rational line census, and 28-point incidence are the contribution claimed here.

## Limitations
No classification of geometric lines over extensions is asserted; the quartic may have additional nonrational lines. No Picard lattice, zeta function, or Artin invariant is claimed. An equivalent calculation might exist in specialized older finite-geometry literature that was not identified in the searches. Independent validation has not been performed.

## References
1. D. Eklund, *Curves on Heisenberg invariant quartic surfaces in projective 3-space*, arXiv:1010.4058 (submitted 2010-10-19), https://arxiv.org/abs/1010.4058.
2. I. Dolgachev and S. Kondō, *Desmic quartic surfaces in arbitrary characteristic*, arXiv:2505.01033 (submitted 2025-05-02), https://arxiv.org/abs/2505.01033.
3. A. Degtyarev, I. Dolgachev, and S. Kondō, *K3 surfaces of degree six arising from desmic tetrahedra*, arXiv:2505.16497 (submitted 2025-05-22), https://arxiv.org/abs/2505.16497.
