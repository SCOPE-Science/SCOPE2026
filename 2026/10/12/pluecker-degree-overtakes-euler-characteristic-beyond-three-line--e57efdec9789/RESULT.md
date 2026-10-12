# Pluecker degree overtakes Euler characteristic beyond three line-Grassmannian exceptions
## Finding
Let
\[
X=\operatorname{Gr}(k,\mathbb C^n),
\qquad
2\le k\le n-2,
\]
with its Pluecker embedding. Put
\[
D_{k,n}=\deg X
\]
and
\[
E_{k,n}=\chi_{\mathrm{top}}(X).
\]

Then
\[
E_{k,n}=\binom nk,
\]
and there is never equality between \(D_{k,n}\) and \(E_{k,n}\).

More precisely,
\[
\boxed{
D_{k,n}<E_{k,n}
}
\]
exactly for
\[
\boxed{
(\min(k,n-k),n)=(2,4),(2,5),(2,6)
}.
\]
For every other non-projective complex Grassmannian,
\[
\boxed{
D_{k,n}>E_{k,n}.
}
\]

In the Schubert-cell interpretation, \(E_{k,n}\) is the number of elements in the rectangular Grassmannian Bruhat interval, while \(D_{k,n}\) is the number of saturated maximal chains from its minimum to its maximum. Thus, outside the three smallest line-Grassmannian cases, the number of maximal chains already exceeds the number of cells.

## Assumptions and scope
The base field is \(\mathbb C\). The degree is the projective degree in the standard Pluecker embedding.

By Grassmannian duality,
\[
\operatorname{Gr}(k,n)\cong\operatorname{Gr}(n-k,n),
\]
both invariants are unchanged when \(k\) is replaced by \(n-k\). Hence it is enough to write
\[
q=\min(k,n-k),
\qquad
c=n-q,
\qquad
2\le q\le c.
\]

The Schubert-cell decomposition has one affine cell for every partition fitting in a \(q\times c\) rectangle. Therefore its topological Euler characteristic is the number of such partitions,
\[
E(q,c)=\binom{q+c}{q}.
\]

The Pluecker degree is the number of standard Young tableaux of rectangular shape \(q\times c\):
\[
D(q,c)
=
\frac{(qc)!\,\prod_{i=1}^{q-1}i!}
{\prod_{j=c}^{c+q-1}j!}.
\]

## Proof
We split the proof into the two-row case and the case of at least three rows.

First let
\[
q=2.
\]
Then
\[
D(2,c)=\frac1{c+1}\binom{2c}{c}
\]
is the \(c\)-th Catalan number, while
\[
E(2,c)=\binom{c+2}{2}.
\]
For
\[
c=2,3,4,
\]
the pairs are respectively
\[
(D,E)=(2,6),(5,10),(14,15).
\]
At
\[
c=5
\]
one has
\[
(D,E)=(42,21).
\]

For \(c\ge5\),
\[
\frac{D(2,c+1)}{D(2,c)}
=
\frac{2(2c+1)}{c+2},
\]
whereas
\[
\frac{E(2,c+1)}{E(2,c)}
=
\frac{c+3}{c+1}.
\]
The difference after clearing positive denominators is
\[
2(2c+1)(c+1)-(c+3)(c+2)
=
3c^2+c-4>0.
\]
Thus, once \(D(2,c)\) exceeds \(E(2,c)\) at \(c=5\), it remains strictly larger for every larger \(c\).

Now assume
\[
q\ge3.
\]
We first compare the square case \(c=q\).

Every standard Young tableau of rectangular shape \(3\times q\) injects into one of shape \(q\times q\): keep the first three rows and fill the remaining \(q-3\) rows with the integers
\[
3q+1,\ldots,q^2
\]
in increasing row-major order. Hence
\[
D(q,q)\ge F_q,
\]
where
\[
F_q
=
\frac{2(3q)!}{q!(q+1)!(q+2)!}
\]
is the number of standard Young tableaux of shape \(3\times q\).

Let
\[
B_q=\binom{2q}{q}=E(q,q).
\]
At \(q=3\),
\[
F_3=42>20=B_3.
\]
Furthermore,
\[
\frac{F_{q+1}}{F_q}
=
\frac{(3q+1)(3q+2)(3q+3)}
{(q+1)(q+2)(q+3)}
\]
and
\[
\frac{B_{q+1}}{B_q}
=
\frac{2(2q+1)}{q+1}.
\]
After clearing positive denominators, the assertion that the first ratio is larger reduces to
\[
23q^3+32q^2-q-6>0,
\]
which holds for every \(q\ge1\). Thus
\[
F_q>B_q
\]
for every \(q\ge3\), and therefore
\[
D(q,q)>E(q,q).
\]

It remains to move away from the square while keeping \(q\ge3\) fixed. From the rectangular hook-length formula,
\[
\frac{D(q,c+1)}{D(q,c)}
=
\prod_{j=1}^{q}
\frac{qc+j}{c+j}.
\]
On the other hand,
\[
\frac{E(q,c+1)}{E(q,c)}
=
\frac{c+q+1}{c+1}.
\]
Already the first factor of the degree ratio satisfies
\[
\frac{qc+1}{c+1}
>
\frac{c+q+1}{c+1},
\]
because
\[
qc>c+q
\]
for \(q,c\ge3\). Every remaining factor in the degree ratio is greater than \(1\). Hence
\[
\frac{D(q,c+1)}{D(q,c)}
>
\frac{E(q,c+1)}{E(q,c)}
\]
for every \(c\ge q\ge3\).

Since the strict inequality \(D(q,q)>E(q,q)\) holds at the square endpoint, it persists for every \(c\ge q\). Together with the complete \(q=2\) analysis, this proves the classification and also proves that equality never occurs.

## Verification
The bundled checker evaluates both invariants exactly for every
\[
4\le n\le100
\]
and every
\[
2\le k\le n-2.
\]
It verifies the three exceptional pairs, the absence of equality, the rectangular degree formula, and the two ratio inequalities used in the proof.

The finite computation is regression evidence only. The theorem for all \(k,n\) follows from the symbolic argument above.

## Relationship to prior work
Eremenko and Gabrielov record the classical complex degree of the Pluecker Grassmannian and its interpretation as the number of standard Young tableaux of a rectangle. Their formula supplies the degree input.

The Euler characteristic follows independently from the Schubert-cell decomposition: every cell is an affine space of even real dimension, so the Euler characteristic is simply the number of cells, namely the number of partitions in the same rectangle.

The comparison made here asks when these two canonical counts attached to the same Bruhat interval cross: the number of its elements versus the number of its saturated maximal chains. Targeted literature searches for Grassmannian degree versus Euler characteristic, maximal chains versus cells, and the corresponding rectangular-tableau inequality did not locate this complete threshold classification.

## Limitations
Projective-space Grassmannians
\[
\operatorname{Gr}(1,n)\cong\mathbb P^{n-1}
\]
and their duals are excluded from the main statement; there the degree is \(1\) and the Euler characteristic is \(n\).

The result compares only two coarse invariants. It does not compare individual Betti numbers with refined degree data, nor does it extend automatically to other homogeneous varieties.

The originality search cannot rule out an unindexed combinatorial observation comparing the number of rectangular Young-lattice elements with the number of maximal chains.

## References
Alex Eremenko and Andrei Gabrielov, *Degrees of real Wronski maps*, arXiv:math/0108133, first submitted 20 August 2001; *Discrete & Computational Geometry* 28 (2002), 331--347, DOI 10.1007/S00454-002-0735-X.

Frank Sottile, *Enumerative Real Algebraic Geometry: Real Degree of Grassmann Varieties*, expository material on the Pluecker degree as the number of maximal Bruhat chains.
