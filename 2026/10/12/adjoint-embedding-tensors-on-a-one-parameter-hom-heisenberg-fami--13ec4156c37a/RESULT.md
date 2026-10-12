# Adjoint embedding tensors on a one-parameter Hom-Heisenberg family

## Finding

Let \(K\) be a field. Start with the three-dimensional Heisenberg Lie algebra with basis
\[
\{e,f,c\},
\qquad
[e,f]=c,
\]
and define the Lie endomorphism
\[
\alpha_\lambda(e)=e,\qquad
\alpha_\lambda(f)=\lambda f,\qquad
\alpha_\lambda(c)=\lambda c
\]
for \(\lambda\in K\).

The Yau twist
\[
H_{\lambda,K}
=
(H_K,[\, ,\,]_\lambda,\alpha_\lambda),
\qquad
[x,y]_\lambda=\alpha_\lambda([x,y]),
\]
has sole nonzero basic bracket
\[
[e,f]_\lambda=\lambda c.
\]

For the adjoint representation, an embedding tensor is a linear map
\[
T:H_{\lambda,K}\to H_{\lambda,K}
\]
satisfying
\[
T\alpha_\lambda=\alpha_\lambda T
\]
and
\[
[T(x),T(y)]_\lambda
=
T([T(x),y]_\lambda)
\qquad(x,y\in H_{\lambda,K}).
\]

The complete classification has three sharply different fibers.

If
\[
\lambda=0,
\]
then
\[
\boxed{
T=
\begin{pmatrix}
a&0&0\\
0&p&s\\
0&r&t
\end{pmatrix}
}
\]
with arbitrary
\[
a,p,r,s,t\in K.
\]

If
\[
\lambda\notin\{0,1\},
\]
then
\[
\boxed{
T=
\begin{pmatrix}
a&0&0\\
0&p&0\\
0&r&t
\end{pmatrix},
\qquad
a(p-t)=0,
\qquad
p(t-a)=0.
}
\]
Equivalently, this generic fiber is the disjoint union of
\[
\boxed{
t=0,\qquad ap=0,\qquad r\in K,
}
\]
\[
\boxed{
t\ne0,\qquad a=p=0,\qquad r\in K,
}
\]
and
\[
\boxed{
t\ne0,\qquad a=p=t,\qquad r\in K.
}
\]

If
\[
\lambda=1,
\]
then
\[
\boxed{
T=
\begin{pmatrix}
a&b&0\\
d&e&0\\
g&h&i
\end{pmatrix},
}
\]
where
\[
\boxed{
bi=0,\qquad
di=0,\qquad
i(a-e)=0,\qquad
bd=a(e-i).
}
\]
Equivalently:

- if \(i=0\), the upper-left matrix
  \[
  A=
  \begin{pmatrix}
  a&b\\
  d&e
  \end{pmatrix}
  \]
  is arbitrary singular and \(g,h\) are arbitrary;

- if \(i\ne0\), then \(g,h\) are arbitrary and either
  \[
  A=0
  \]
  or
  \[
  A=iI_2.
  \]

For every prime power \(q\), the three fiber sizes are
\[
\boxed{
|\operatorname{ET}_{\mathrm{ad}}(H_{0,\mathbf F_q})|
=
q^5,
}
\]
\[
\boxed{
|\operatorname{ET}_{\mathrm{ad}}(H_{1,\mathbf F_q})|
=
q^5+q^4+q^3-2q^2,
}
\]
and, for every fixed
\[
\lambda\in\mathbf F_q\setminus\{0,1\},
\]
\[
\boxed{
|\operatorname{ET}_{\mathrm{ad}}(H_{\lambda,\mathbf F_q})|
=
4q^2-3q.
}
\]

The exact rank distributions in ranks \(0,1,2,3\) are respectively
\[
\boxed{
\left(
1,\,
(q-1)(q^2+2q+2),\,
(q-1)^2(q+1)(2q+1),\,
q(q-1)^3(q+1)
\right),
}
\]
\[
\boxed{
\left(
1,\,
q^4+2q^3-q^2-q-1,\,
q(q-1)^2(q+1)^2,\,
q^2(q-1)
\right),
}
\]
and
\[
\boxed{
\left(
1,\,
2(q^2-1),\,
(q-1)^2,\,
q(q-1)
\right).
}
\]

Thus both
\[
\lambda=0
\]
and
\[
\lambda=1
\]
are exceptional large fibers. The generic fiber has order only quadratic in \(q\), while the two exceptional fibers have order \(q^5\).

Summing over all parameters,
\[
\boxed{
\#\{(\lambda,T):
\lambda\in\mathbf F_q,\,
T\in\operatorname{ET}_{\mathrm{ad}}(H_{\lambda,\mathbf F_q})
\}
=
2q^5+q^4+5q^3-13q^2+6q.
}
\]

For a fixed parameter, the extension-field point counts give the zeta functions
\[
\boxed{
Z_{\lambda=0}(T)=\frac{1}{1-q^5T},
}
\]
\[
\boxed{
Z_{\lambda=1}(T)
=
\frac{(1-q^2T)^2}
{(1-q^5T)(1-q^4T)(1-q^3T)},
}
\]
and
\[
\boxed{
Z_{\lambda\notin\{0,1\}}(T)
=
\frac{(1-qT)^3}{(1-q^2T)^4}.
}
\]

## Assumptions and scope

Das and Makhlouf introduce embedding tensors on multiplicative Hom-Lie algebras. Their definition requires
\[
\alpha T=T\beta
\]
and
\[
[T(u),T(v)]
=
T(\rho(T(u))v).
\]
For the adjoint representation one has
\[
V=\mathfrak g,\qquad
\beta=\alpha,\qquad
\rho(x)y=[x,y].
\]

Their paper assumes characteristic \(0\). The classification here is independently reconstructed from the same polynomial identities and is valid over an arbitrary field.

The Hom-Lie family is obtained from the standard Yau-twist construction: \(\alpha_\lambda\) is a Lie endomorphism of the Heisenberg algebra and
\[
[x,y]_\lambda=\alpha_\lambda([x,y]).
\]

No quotient by Hom-Lie automorphisms is taken.

## Proof

Write a general linear map in column convention as
\[
T=
\begin{pmatrix}
a&b&u\\
d&e&v\\
g&h&i
\end{pmatrix}.
\]

The commutation equation
\[
T\alpha_\lambda=\alpha_\lambda T
\]
gives
\[
(\lambda-1)b=0,
\qquad
(\lambda-1)u=0,
\qquad
(\lambda-1)d=0,
\qquad
(\lambda-1)g=0.
\]

The Hom-Heisenberg bracket is
\[
[x,y]_\lambda
=
\lambda(x_e y_f-x_f y_e)c.
\]

### The fiber \(\lambda=0\)

The bracket vanishes identically. Hence the embedding-tensor quadratic identity is automatic.

The commutation equation with
\[
\alpha_0=\operatorname{diag}(1,0,0)
\]
forces exactly
\[
b=u=d=g=0,
\]
leaving
\[
T=
\begin{pmatrix}
a&0&0\\
0&p&s\\
0&r&t
\end{pmatrix}.
\]

Thus the fiber is
\[
K\times M_2(K).
\]

Over \(\mathbf F_q\) its cardinality is \(q^5\). Its rank is
\[
\mathbf 1_{a\ne0}+\operatorname{rank}B
\]
for
\[
B=
\begin{pmatrix}
p&s\\
r&t
\end{pmatrix}.
\]
Using the standard \(2\times2\) matrix rank counts gives the first displayed rank profile.

### The generic fiber \(\lambda\notin\{0,1\}\)

Commutation forces
\[
b=u=d=g=0.
\]
So
\[
T=
\begin{pmatrix}
a&0&0\\
0&p&v\\
0&r&t
\end{pmatrix}.
\]

Substitution into the embedding-tensor identity on the ordered basis pairs yields
\[
v^2=0,
\qquad
a(p-t)=0,
\qquad
p(t-a)=0.
\]
Because \(K\) is a field,
\[
v=0.
\]

If \(t=0\), the two remaining equations reduce to
\[
ap=0.
\]

If \(t\ne0\), then either
\[
a=p=0
\]
or both are nonzero, in which case the two equations force
\[
a=p=t.
\]

This proves the three generic strata.

Their cardinalities over \(\mathbf F_q\) are
\[
q(2q-1),
\qquad
q(q-1),
\qquad
q(q-1),
\]
respectively, for a total
\[
4q^2-3q.
\]

For ranks:

- in the \(t=0\) stratum, the zero map occurs once, rank \(1\) occurs
  \[
  (q-1)(q+2)
  \]
  times, and rank \(2\) occurs
  \[
  (q-1)^2
  \]
  times;

- in the \(a=p=0,\ t\ne0\) stratum, all
  \[
  q(q-1)
  \]
  maps have rank \(1\);

- in the \(a=p=t\ne0\) stratum, all
  \[
  q(q-1)
  \]
  maps are invertible.

This gives the generic rank profile.

### The fiber \(\lambda=1\)

Now
\[
\alpha_1=I
\]
and
\[
[e,f]_1=c,
\]
so there is no linear commutation restriction.

Expanding the embedding-tensor identity on the ordered basis pairs gives
\[
u^2=0,
\qquad
v^2=0,
\]
hence
\[
u=v=0.
\]

The remaining equations are equivalent to
\[
bi=0,
\qquad
di=0,
\qquad
i(a-e)=0,
\qquad
bd=a(e-i).
\]

If
\[
i=0,
\]
this becomes
\[
bd=ae.
\]
Thus the upper-left \(2\times2\) matrix
\[
A=
\begin{pmatrix}
a&b\\
d&e
\end{pmatrix}
\]
is singular, while \(g,h\) are free.

The number of singular \(2\times2\) matrices is
\[
q^4-|\operatorname{GL}_2(\mathbf F_q)|
=
q^3+q^2-q.
\]
Thus this branch has
\[
q^2(q^3+q^2-q)
=
q^5+q^4-q^3
\]
points.

If
\[
i\ne0,
\]
then
\[
b=d=0
\]
and
\[
a=e.
\]
The final equation becomes
\[
a(a-i)=0.
\]
Hence
\[
A=0
\]
or
\[
A=iI_2.
\]
Each choice has \(q^2\) free values of \(g,h\), so this branch contributes
\[
2q^2(q-1)
\]
points.

Adding gives
\[
q^5+q^4+q^3-2q^2.
\]

For the rank distribution, let
\[
N_1=(q-1)(q+1)^2
\]
be the number of rank-one \(2\times2\) matrices.

When \(i=0\):

- \(A=0\) gives one rank-zero map and \(q^2-1\) rank-one maps;
- for a fixed rank-one \(A\), the bottom row \((g,h)\) lies in the row space of \(A\) in exactly \(q\) cases, giving rank \(1\), and lies outside it in \(q^2-q\) cases, giving rank \(2\).

When \(i\ne0\):

- \(A=0\) always gives rank \(1\);
- \(A=iI_2\) always gives rank \(3\).

This yields
\[
1,
\quad
q^4+2q^3-q^2-q-1,
\quad
q(q-1)^2(q+1)^2,
\quad
q^2(q-1).
\]

Finally, summing the three fiber counts over
\[
\lambda\in\mathbf F_q
\]
gives
\[
q^5+
\left(q^5+q^4+q^3-2q^2\right)
+
(q-2)(4q^2-3q),
\]
which simplifies to
\[
2q^5+q^4+5q^3-13q^2+6q.
\]

The zeta functions follow by replacing \(q\) with \(q^m\) in each fixed-fiber count.

## Verification

The included program `artifacts/verify.py` reconstructs the Yau-twisted bracket and both embedding-tensor conditions symbolically.

It verifies the full matrix equation
\[
T\alpha_\lambda=\alpha_\lambda T
\]
and reconstructs all basis-pair embedding-tensor defects.

It then exhaustively tests every \(3\times3\) matrix for every parameter over
\[
\mathbf F_2
\]
and
\[
\mathbf F_3.
\]

The fiber counts are:

- over \(\mathbf F_2\):
  \[
  32,\quad48
  \]
  for \(\lambda=0,1\);

- over \(\mathbf F_3\):
  \[
  243,\quad333,\quad27
  \]
  for \(\lambda=0,1,2\).

The exact rank profiles match the displayed formulas in every tested fiber.

The program also checks the closed rank formulas algebraically for
\[
q=2,3,5,7.
\]

It returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary-field classification follows from the symbolic case split above.

## Relationship to prior work

Das and Makhlouf introduce embedding tensors on Hom-Lie algebras, prove the graph characterization, define their cohomology, and give general examples such as the identity map, square-zero derivations, direct-sum projections, and equivariant maps. Their full text contains no Heisenberg example and no finite-field calculation.

The same paper recalls the Yau-twist construction from a Lie algebra endomorphism. The family here applies that construction to the smallest nonabelian nilpotent Lie algebra and then solves the entire adjoint embedding-tensor problem across the twist parameter.

Ben Jmaa, Makhlouf, and Saadaoui study current Hom-Lie algebras and explicitly discuss current Heisenberg Hom-Lie algebras, their representations, derivations, cohomology, and extensions. Their article does not study embedding tensors or averaging operators.

Later work on averaging operators for Hom-Lie algebras classifies homogeneous operators on \(q\)-deformed Witt-type Hom-algebras, not this finite-dimensional Hom-Heisenberg family.

Focused searches for Hom-Heisenberg embedding tensors, adjoint embedding tensors, averaging operators, exact finite-field counts, and the polynomial
\[
4q^2-3q
\]
did not locate a covering result.

## Limitations

The theorem treats the one-parameter Yau-twist family
\[
\alpha_\lambda=\operatorname{diag}(1,\lambda,\lambda)
\]
on the three-dimensional Heisenberg algebra.

No quotient by the Hom-Lie automorphism group is computed.

The primary source assumes characteristic \(0\); the arbitrary-field extension here is independently justified by direct verification of the Hom-Lie and embedding-tensor polynomial identities.

A specialized or differently indexed finite-dimensional Hom-Lie averaging classification may contain equivalent formulas. Failed searches do not prove novelty.

## References

1. A. Das and A. Makhlouf, “Embedding tensors on Hom-Lie algebras,” arXiv:2304.04178v1, first public 9 April 2023.
2. T. Ben Jmaa, A. Makhlouf, and N. Saadaoui, “Current Hom-Lie algebras,” *Acta et Commentationes Universitatis Tartuensis de Mathematica* 26 (2022), DOI `10.12697/ACUTM.2022.26.08`.
3. “Averaging operators on \(q\)-deformed Witt and \(q\)-deformed \(W(2,2)\) algebras,” *Communications in Algebra* 53 (2025), DOI `10.1080/00927872.2025.2460101`.
