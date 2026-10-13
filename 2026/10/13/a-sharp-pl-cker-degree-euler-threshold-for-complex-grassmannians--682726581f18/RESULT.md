# A sharp Plücker degree–Euler threshold for complex Grassmannians
## Finding
Let
\[
\operatorname{Gr}(k,n)
\]
be the complex Grassmannian of \(k\)-dimensional subspaces of \(\mathbb C^n\), where
\[
n\ge2,
\qquad
1\le k\le n-1,
\]
in its Plücker embedding.

Its projective degree is
\[
\boxed{
D_{k,n}
=
\deg\operatorname{Gr}(k,n)
=
\frac{(k(n-k))!\prod_{i=1}^{k-1}i!}
{\prod_{j=0}^{k-1}(n-k+j)!}
}
\]
and its ordinary topological Euler characteristic is
\[
\boxed{
E_{k,n}
=
\chi_{\mathrm{top}}(\operatorname{Gr}(k,n))
=
\binom nk.
}
\]

There is no equality
\[
D_{k,n}=E_{k,n}.
\]

Writing
\[
s=\min(k,n-k),
\]
the complete ordering is
\[
\boxed{
D_{k,n}<E_{k,n}
\iff
s=1
\quad\text{or}\quad
(s=2\ \text{and}\ n\le6).
}
\]

In every remaining case,
\[
\boxed{
D_{k,n}>E_{k,n}.
}
\]

Thus, apart from projective spaces, the only degree-below-Euler Grassmannians are
\[
\operatorname{Gr}(2,4),\quad
\operatorname{Gr}(2,5),\quad
\operatorname{Gr}(2,6),
\]
together with their dual presentations.

The transition on the two-plane edge is sharp:
\[
(D_{2,6},E_{2,6})=(14,15),
\]
while
\[
(D_{2,7},E_{2,7})=(42,21).
\]
At the first genuinely interior point,
\[
(D_{3,6},E_{3,6})=(42,20).
\]

## Assumptions and scope
The base field is \(\mathbb C\).

The degree is the ordinary projective degree for the Plücker embedding
\[
\operatorname{Gr}(k,n)
\hookrightarrow
\mathbb P(\Lambda^k\mathbb C^n).
\]

The Euler characteristic is the ordinary topological Euler characteristic of the complex projective manifold.

Grassmannian duality identifies
\[
\operatorname{Gr}(k,n)
\cong
\operatorname{Gr}(n-k,n),
\]
and preserves both invariants. Consequently it is enough in the proof to assume
\[
k\le\frac n2.
\]

## Proof
The classical Plücker degree formula is
\[
D_{k,n}
=
\frac{(k(n-k))!\prod_{i=1}^{k-1}i!}
{\prod_{j=0}^{k-1}(n-k+j)!}.
\]
Equivalently, this is the number of standard Young tableaux of rectangular shape
\[
(n-k)^k.
\]

The Schubert cell decomposition of
\[
\operatorname{Gr}(k,n)
\]
has one affine cell for each \(k\)-subset of an \(n\)-element set, equivalently one cell for each Young diagram contained in the rectangle
\[
(n-k)^k.
\]
Every cell has even real dimension. Therefore
\[
E_{k,n}
=
\chi_{\mathrm{top}}(\operatorname{Gr}(k,n))
=
\binom nk.
\]

By duality assume
\[
1\le k\le\left\lfloor\frac n2\right\rfloor.
\]

For
\[
k=1,
\]
the Grassmannian is projective space:
\[
D_{1,n}=1,
\qquad
E_{1,n}=n,
\]
so degree is strictly smaller.

Now take
\[
k=2.
\]
The degree formula becomes the Catalan number
\[
D_{2,n}
=
\frac1{n-1}\binom{2n-4}{n-2}.
\]
Define
\[
R_n=\frac{D_{2,n}}{\binom n2}.
\]
A direct quotient calculation gives
\[
\frac{R_{n+1}}{R_n}
=
\frac{2(2n-3)(n-1)}{n(n+1)}.
\]
For every
\[
n\ge4,
\]
this is greater than \(1\), since
\[
2(2n-3)(n-1)-n(n+1)
=
3n^2-11n+6>0.
\]
Hence \(R_n\) is strictly increasing. The consecutive values
\[
R_6=\frac{14}{15}<1,
\qquad
R_7=\frac{42}{21}=2>1
\]
show that
\[
D_{2,n}<E_{2,n}
\]
exactly for
\[
n=4,5,6,
\]
and
\[
D_{2,n}>E_{2,n}
\]
for every
\[
n\ge7.
\]
In particular equality never occurs on the two-plane edge.

It remains to treat
\[
k\ge3.
\]
First observe that, for fixed \(n\), Plücker degree increases as one moves from the edge toward the center. Put
\[
r=n-k,
\qquad
M=kr.
\]
If
\[
r\ge k+2
\]
and
\[
q=r-k-1,
\]
the degree product gives
\[
\frac{D_{k+1,n}}{D_{k,n}}
=
\frac{(M+q)!}{M!}\frac{k!}{(r-1)!}
=
\prod_{s=1}^{q}\frac{M+s}{k+s}>1.
\]
If
\[
r=k+1,
\]
the next Grassmannian is the dual presentation and the ratio is \(1\). Thus for
\[
3\le k\le\frac n2,
\]
\[
D_{k,n}\ge D_{3,n}.
\]

Write
\[
r=n-3.
\]
Then
\[
D_{3,n}
=
\frac{2(3r)!}{r!(r+1)!(r+2)!}.
\]
Let
\[
B_n=\binom n{\lfloor n/2\rfloor}
\]
be the largest binomial coefficient in row \(n\). At
\[
n=6,
\]
\[
D_{3,6}=42>20=B_6.
\]

Moreover
\[
\frac{D_{3,n+1}}{D_{3,n}}
=
\frac{(3r+1)(3r+2)(3r+3)}
{(r+1)(r+2)(r+3)}
>2
\qquad(r\ge3),
\]
whereas
\[
\frac{B_{n+1}}{B_n}\le2.
\]
Induction therefore gives
\[
D_{3,n}>B_n
\qquad(n\ge6).
\]
Since
\[
\binom nk\le B_n,
\]
we obtain
\[
D_{k,n}
\ge
D_{3,n}
>
B_n
\ge
\binom nk
=
E_{k,n}
\]
for every
\[
3\le k\le\frac n2.
\]

Combining this with duality and the \(k=1,2\) cases proves the full classification and excludes equality.

## Verification
The bundled checker evaluates the Plücker degree product with exact integer arithmetic for every
\[
2\le n\le100,
\qquad
1\le k\le n-1.
\]

It verifies the complete degree-versus-Euler classification, the Catalan specialization on the \(k=2\) edge, the adjacent normalized-ratio identity there, the fixed-\(n\) degree ratio toward the center, and the comparison
\[
D_{3,n}>\binom n{\lfloor n/2\rfloor}
\]
through the finite test range.

These computations are regression evidence only. The theorem for all parameters follows from the exact product formulas and the symbolic inequalities in the proof.

## Relationship to prior work
The Plücker degree of a Grassmannian is classical. Eremenko and Gabrielov state the full factorial formula and its interpretation as the number of rectangular standard Young tableaux, in the course of studying Wronski projections of Grassmannians. The Euler characteristic is independently the number of Schubert cells, namely \(\binom nk\).

The comparison here places those two classical counts against one another over the entire Grassmannian family. Targeted searches for Plücker degree versus Euler characteristic, rectangular-tableau count versus the Schubert-cell count, equality, and threshold language did not locate the complete ordering above.

Nearby work studies real or complex Wronski degrees, Plücker-degree curvature, polar degrees, and Euler characteristics of Grassmannian complements, rather than the exact ordering of projective degree and the Euler characteristic of the Grassmannian itself.

## Limitations
The projective degree depends on the Plücker polarization. Other embeddings of the same Grassmannian have different degrees.

The result compares two coarse numerical invariants and does not assert a direct geometric correspondence between a generic Plücker linear section and the Schubert-cell decomposition.

Both input formulas are classical and the final inequalities are elementary. An older exercise or unindexed note may therefore contain the same threshold without presenting it as a uniform degree-versus-Euler classification.

## References
Alex Eremenko and Andrei Gabrielov, *Degrees of real Wronski maps*, arXiv:math/0108133, first submitted 20 August 2001; *Discrete & Computational Geometry* 28 (2002), 331--347.

Frank Sottile, *Enumerative Real Algebraic Geometry*, arXiv:math/0107179, first submitted 24 July 2001.
