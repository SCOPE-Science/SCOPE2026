# A binary-carry formula for the 2-adic degree of equidegree complete-intersection discriminants
## Finding
Let \(1\le c\le N\) and \(d\ge2\). Consider the discriminant \(\Delta_{N,c,d}\) for \(c\) homogeneous degree-\(d\) equations in \(\mathbb P^N\), with expected complete-intersection dimension
\[
n=N-c\ge0.
\]
Then its total degree satisfies
\[
\deg\Delta_{N,c,d}
=
c\binom{N+1}{c}d^{c-1}(d-1)^{n+1}.
\]
If \(\kappa_2(a,b)\) is the number of binary carries produced when adding the nonnegative integers \(a\) and \(b\), then the exact 2-adic valuation is
\[
\nu_2(\deg\Delta_{N,c,d})
=
\nu_2(N+1)
+
\kappa_2(c-1,n+1)
+
(c-1)\nu_2(d)
+
(n+1)\nu_2(d-1).
\]
In particular,
\[
\deg\Delta_{N,c,d}\ \text{is odd}
\quad\Longleftrightarrow\quad
c=1,\ N\equiv0\pmod2,\ d\equiv0\pmod2.
\]
For every genuine higher-codimension complete intersection, meaning \(2\le c\le N\), one has the stronger universal divisibility
\[
4\mid\deg\Delta_{N,c,d}.
\]
The factor \(4\) is sharp: for two quadrics in \(\mathbb P^2\),
\[
\deg\Delta_{2,2,2}=12.
\]

## Assumptions and scope
The discriminant is the reduced irreducible divisor in the parameter space of ordered \(c\)-tuples of degree-\(d\) equations whose common zero locus is not a smooth complete intersection of codimension \(c\). The field for the degree formula is of characteristic zero; the displayed degree is therefore the ordinary total degree of the characteristic-zero discriminant polynomial. The restriction \(c\le N\) keeps the expected complete-intersection dimension nonnegative and excludes the pure resultant case \(c=N+1\).

The result concerns only the 2-adic valuation of this total degree. It does not assert a factorization of the discriminant polynomial over characteristic zero or modulo \(2\).

## Proof
Benoist proves that when all defining degrees equal \(d\), every partial coefficient degree of the discriminant is
\[
\deg_i\Delta
=
\binom{N+1}{c}d^{c-1}(d-1)^{N-c+1}.
\]
He also records that total degree is the sum of the partial degrees. By symmetry,
\[
\deg\Delta_{N,c,d}
=
c\binom{N+1}{c}d^{c-1}(d-1)^{n+1}.
\]
Use the elementary identity
\[
c\binom{N+1}{c}=(N+1)\binom{N}{c-1},
\]
so
\[
\nu_2(\deg\Delta_{N,c,d})
=
\nu_2(N+1)
+
\nu_2\binom{N}{c-1}
+
(c-1)\nu_2(d)
+
(n+1)\nu_2(d-1).
\]
Since
\[
N=(c-1)+(n+1),
\]
Legendre's identity \(\nu_2(m!)=m-s_2(m)\), where \(s_2(m)\) is binary digit sum, gives
\[
\nu_2\binom{N}{c-1}
=
s_2(c-1)+s_2(n+1)-s_2(N).
\]
The right-hand side is exactly the number \(\kappa_2(c-1,n+1)\) of binary carries in the addition \((c-1)+(n+1)=N\). This proves the valuation formula.

For oddness, all four summands in the valuation formula must vanish. If \(d\) is odd, then \(\nu_2(d-1)\ge1\), while \(n+1\ge1\), so the degree is even. If \(d\) is even, then \(\nu_2(d)\ge1\), so vanishing forces \(c=1\). In that case the carry term vanishes and
\[
\nu_2(\deg\Delta_{N,1,d})=\nu_2(N+1),
\]
because \(d-1\) is odd. Hence the degree is odd exactly when \(N+1\) is odd, equivalently when \(N\) is even.

Now assume \(2\le c\le N\). If \(d\) is even and \(c\ge3\), the term \((c-1)\nu_2(d)\) is already at least \(2\). If \(d\) is even and \(c=2\), that term contributes at least \(1\), while
\[
\nu_2(N+1)+\kappa_2(1,N-1)=\nu_2(N+1)+\nu_2(N)\ge1,
\]
so the total valuation is at least \(2\).

If \(d\) is odd and \(n\ge1\), then \((n+1)\nu_2(d-1)\ge2\). Finally, if \(d\) is odd and \(n=0\), then \(c=N\) and the last term contributes at least \(1\), while
\[
\nu_2(N+1)+\kappa_2(N-1,1)
=
\nu_2(N+1)+\nu_2(N)
\ge1.
\]
Thus every case with \(2\le c\le N\) has valuation at least \(2\). The example \((N,c,d)=(2,2,2)\) has degree \(12\), so no larger universal power of \(2\) divides all such degrees.

## Verification
The bundled exact checker recomputes the Benoist total-degree specialization, the binary-carry valuation, the oddness classification, and the universal mod-\(4\) statement for every
\[
1\le N\le80,\qquad 1\le c\le N,\qquad 2\le d\le64.
\]
This is \(204120\) exact integer cases. It also checks the sharp example \(\deg\Delta_{2,2,2}=12\). The finite computation is regression evidence only; the proof above is uniform.

## Relationship to prior work
Benoist computes the partial homogeneity degrees of the singular-complete-intersection discriminant and, in the equidegree case, gives the closed formula used here. He separately proves a characteristic-\(2\) statement: the reduction of the integral discriminant is irreducible when the complete-intersection dimension is odd and is the square of an irreducible polynomial when that dimension is even.

The present claim concerns a different arithmetic invariant: the exact 2-adic valuation of the characteristic-zero total degree. The binary-carry term is not stated in the inspected paper, nor are the resulting odd-degree classification and the universal sharp divisibility by \(4\) in codimension at least two. Claim-specific searches for 2-adic valuations, parity, Kummer carries, and mod-\(4\) divisibility of complete-intersection discriminant degrees did not locate an equivalent statement.

This also does not overlap the finite-line, quadrisecant, dual-degree, or Chern-number results for complete intersections: those concern different associated schemes or topological invariants rather than the degree of the singular-member divisor in the equation parameter space.

## Limitations
The theorem treats the equidegree family only. Benoist's general unequal-degree formula is more complicated and may have different 2-adic behavior. The result excludes the resultant boundary case \(c=N+1\), where the expected common zero locus is empty. It also does not infer factorization or irreducibility properties from degree divisibility.

Literature searches cannot exclude an unindexed arithmetic observation in older discriminant literature. The novelty assessment is therefore statement-level rather than a claim of historical priority beyond the searched sources.

## References
Olivier Benoist, *Degrés d'homogénéité de l'ensemble des intersections complètes singulières*, Annales de l'Institut Fourier 62 (2012), no. 3, 1189--1214. DOI: 10.5802/aif.2720. First arXiv version: arXiv:1009.0704, 3 September 2010.
