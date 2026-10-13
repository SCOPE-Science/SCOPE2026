# A sharp degree–Euler crossover for generic Grassmannian torus orbits
## Finding
Let
\[
X_{k,n}\subset\operatorname{Gr}(k,n)
\]
be the closure of a generic orbit of the maximal diagonal torus in the Plücker embedding, where
\[
n\ge2,
\qquad
1\le k\le n-1.
\]
Kapranov identifies its moment polytope with the hypersimplex
\[
\Delta(k,n)
=
\operatorname{conv}
\left\{
e_{i_1}+\cdots+e_{i_k}
:
1\le i_1<\cdots<i_k\le n
\right\}.
\]

Write
\[
A(m,j)
\]
for the Eulerian number counting permutations of \(m\) letters with exactly \(j\) descents. Then
\[
\boxed{
\deg X_{k,n}=A(n-1,k-1)
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}(X_{k,n})=\binom nk.
}
\]

These two canonical invariants have a sharp global crossover:
\[
\boxed{
\deg X_{k,n}<\chi_{\mathrm{top}}(X_{k,n})
\iff
n\le4
\ \text{or}\
k\in\{1,n-1\},
}
\]
whereas
\[
\boxed{
\deg X_{k,n}>\chi_{\mathrm{top}}(X_{k,n})
\iff
n\ge5
\ \text{and}\
2\le k\le n-2.
}
\]

There is no equality case.

Since
\[
\dim X_{k,n}=n-1,
\]
dimension four is the first dimension in which every non-simplex hypersimplex orbit closure has degree strictly larger than Euler characteristic.

## Assumptions and scope
The base field is \(\mathbb C\). The variety \(X_{k,n}\) is the projective closure of an orbit through a generic point of \(\operatorname{Gr}(k,n)\), so every Plücker coordinate is nonzero.

The acting maximal torus is taken modulo its scalar diagonal subgroup. The resulting effective torus has dimension \(n-1\).

The degree is the ordinary projective degree in the Plücker embedding. The Euler characteristic is the ordinary topological Euler characteristic of the complex projective variety.

The endpoint cases
\[
k=1
\quad\text{and}\quad
k=n-1
\]
are included. Their hypersimplices are simplices and their orbit closures are projective spaces.

## Proof
Kapranov proves that the closure of a torus orbit through a point \(L\in\operatorname{Gr}(k,n)\) is a projective normal toric variety whose polytope is the matroid polytope of \(L\). For a generic point every \(k\)-subset is a basis, so this polytope is exactly
\[
\Delta(k,n).
\]

For a projective toric variety, the degree in the monomial embedding is the normalized lattice volume of its defining polytope. The classical hypersimplex volume formula gives
\[
\operatorname{Vol}_{\mathbb Z}\Delta(k,n)
=
A(n-1,k-1).
\]
Therefore
\[
\deg X_{k,n}=A(n-1,k-1).
\]

The toric orbit decomposition has one orbit for every face of the hypersimplex. An orbit of positive complex dimension is a complex torus
\[
(\mathbb C^*)^q
\]
and has Euler characteristic zero. Thus only the zero-dimensional orbits contribute. They correspond to vertices of the hypersimplex. Since those vertices are indexed by \(k\)-subsets of an \(n\)-element set,
\[
\chi_{\mathrm{top}}(X_{k,n})
=
\binom nk.
\]

It remains to compare the two closed formulas.

First, the endpoint Eulerian numbers satisfy
\[
A(n-1,0)=A(n-1,n-2)=1.
\]
Hence at
\[
k=1
\quad\text{or}\quad
k=n-1
\]
one has
\[
\deg X_{k,n}=1<n=\chi_{\mathrm{top}}(X_{k,n}).
\]

Now assume
\[
2\le k\le n-2.
\]
For \(m\ge4\), the smallest Eulerian number away from the two endpoints is
\[
A(m,1)=A(m,m-2)=2^m-m-1.
\]
For completeness, this can be proved directly from the Eulerian recurrence
\[
A(m,j)
=
(m-j)A(m-1,j-1)+(j+1)A(m-1,j).
\]
The case \(m=4\) is immediate. Inductively, for
\[
2\le j\le m-3,
\]
both Eulerian terms on the right are at least \(A(m-1,1)\), so
\[
A(m,j)
\ge
(m+1)A(m-1,1)
>
A(m,1)
\]
for \(m\ge5\). Symmetry handles the opposite edge.

Thus, for every interior \(k\),
\[
A(n-1,k-1)\ge 2^{n-1}-n.
\]

For
\[
n\ge5,
\]
one also has
\[
2^{n-1}-n
>
\binom n{\lfloor n/2\rfloor}.
\]
For \(n=5\), this is
\[
11>10.
\]
For \(n\ge6\), use
\[
\sum_{\substack{0\le j\le n\\ j\equiv b\pmod2}}\binom nj=2^{n-1},
\qquad
b=\left\lfloor\frac n2\right\rfloor.
\]
If \(b\) is odd, the noncentral terms in that parity class include \(\binom n1=n\) and another positive term. If \(b\) is even, then necessarily \(n\ge8\), and the noncentral terms include
\[
\binom n0+\binom n2>n.
\]
So the central binomial coefficient is strictly smaller than \(2^{n-1}-n\).

Since
\[
\binom nk
\le
\binom n{\lfloor n/2\rfloor},
\]
we obtain, for every
\[
n\ge5,\qquad 2\le k\le n-2,
\]
the strict chain
\[
\deg X_{k,n}
=
A(n-1,k-1)
\ge
2^{n-1}-n
>
\binom n{\lfloor n/2\rfloor}
\ge
\binom nk
=
\chi_{\mathrm{top}}(X_{k,n}).
\]

Finally, the only remaining interior case with
\[
n\le4
\]
is
\[
(n,k)=(4,2),
\]
where
\[
\deg X_{2,4}=A(3,1)=4<6=\binom42.
\]
This proves the complete classification and shows that equality never occurs.

## Verification
The bundled checker constructs Eulerian rows from their recurrence and evaluates
\[
A(n-1,k-1)
\]
and
\[
\binom nk
\]
for every
\[
2\le n\le120,
\qquad
1\le k\le n-1.
\]
It verifies the claimed below/above classification and confirms that no equality occurs in the finite test range.

The checker also verifies the two symbolic numerical bounds used in the proof:
\[
A(n-1,k-1)\ge 2^{n-1}-n
\]
for every tested interior \(k\), and
\[
2^{n-1}-n
>
\binom n{\lfloor n/2\rfloor}
\]
for every tested \(n\ge5\).

These computations are regression evidence only. The theorem for all parameters is proved by toric degree and orbit-stratification formulas together with the recurrence and parity-class inequalities above.

## Relationship to prior work
Kapranov's treatment of Chow quotients identifies generic maximal-torus orbit closures in Grassmannians as projective normal toric varieties with hypersimplex moment polytope. His paper also identifies the hypersimplex vertices and the correspondence between torus orbits and faces.

The normalized volume of a hypersimplex is classically an Eulerian number. Li's work on Ehrhart \(h^*\)-vectors records this formula and reviews the unimodular-triangulation interpretation.

The comparison here juxtaposes the normalized-volume degree with the fixed-point Euler count and proves a sharp all-parameter phase boundary. Targeted searches using hypersimplex, generic Grassmannian torus orbit, Eulerian degree, binomial Euler characteristic, and equality language did not locate the complete crossover statement.

## Limitations
The result concerns generic torus orbit closures, equivalently the full hypersimplex matroid polytope. Nongeneric matroid orbit closures have different polytopes and are not classified here.

The projective degree is tied to the Plücker polarization.

Both closed formulas are classical. The new content is their complete comparison, so a purely combinatorial source comparing the same Eulerian and binomial numbers without toric language remains a residual novelty risk.

## References
M. M. Kapranov, *Chow quotients of Grassmannian I*, arXiv:alg-geom/9210002, first submitted 7 October 1992; in *I. M. Gel'fand Seminar*, Advances in Soviet Mathematics 16, Part 2, American Mathematical Society.

Nan Li, *Ehrhart \(h^*\)-vectors of hypersimplices*, arXiv:1104.5292, first submitted 28 April 2011; DMTCS Proceedings, FPSAC 2013.
