# The exact birational range for involutive-cone incidences
## Finding
Let \(V\) be a complex symplectic vector space of dimension \(2n\), let \(n\ge2\), and let
\[
\widetilde\rho_m:\mathbf P(\widetilde F_d^m)\longrightarrow B_d^m
\]
be the incidence map for degree-\(d\) hypersurfaces in \(\mathbf P(V)\) containing a hyperplane-supported involutive cone of degree \(m\), with
\[
d\ge m\ge2.
\]
Then \(\widetilde\rho_m\) is birational onto its image for every pair
\[
(m,d)\ne(2,2).
\]
For
\[
(m,d)=(2,2),
\]
the generic degree is exactly
\[
2n.
\]

The cases \(n=2\) and \(n=3\), as well as the exceptional quadratic-diagonal degree in arbitrary dimension, are proved in the initiating paper. The new part is the complete range for \(n\ge4\), including the previously untreated cubic hypersurfaces containing involutive quadric cones.

## Assumptions and scope
The notation is that of Guedes, *Hypersurfaces containing involutive cones in projective symplectic spaces*. For a hyperplane \(H\subset\mathbf P(V)\), write \(p=\sigma(H)\) for its symplectic polar point. A degree-\(m\) involutive hypersurface supported on \(H\) is a cone whose vertex contains \(p\).

For fixed cone \(C\), write \(L_C\) for the projective linear system of degree-\(d\) hypersurfaces containing \(C\). The parameter space of degree-\(m\) involutive cones has dimension
\[
D_n(m)=\binom{m+2n-3}{m}+2n-2.
\]
The initiating paper proves a sufficient birationality criterion. Put
\[
G_n(d,m)=
\binom{d+2n-3}{2n-2}
-
\binom{d-m+2n-3}{2n-2}.
\]
If
\[
G_n(d,m)>D_n(m),
\]
then the incidence map is birational onto its image.

The proof below uses this criterion wherever it is strict and treats the unique remaining higher-dimensional case
\[
(m,d)=(2,3)
\]
directly.

## Proof
Assume first that \(n\ge4\).

For \(m\ge3\) and \(d=m\), birationality is Proposition 8.3 of the initiating paper. For \(d\ge m+1\), the function \(G_n(d,m)\) is strictly increasing in \(d\). At the first value \(d=m+1\),
\[
G_n(m+1,m)-D_n(m)
=
\binom{m+2n-3}{m-1}-(2n-1).
\]
Since \(m\ge3\),
\[
\binom{m+2n-3}{m-1}
\ge
\binom{2n}{2},
\]
and hence
\[
G_n(m+1,m)-D_n(m)
\ge
(n-1)(2n-1)>0.
\]
Thus the published criterion proves birationality for every
\[
m\ge3,\qquad d\ge m+1.
\]

Now set \(m=2\). For \(d\ge4\), monotonicity reduces the criterion to \(d=4\), where
\[
G_n(4,2)-D_n(2)
=
\frac{2(n-1)(n+1)(2n-3)}{3}>0.
\]
Therefore all pairs
\[
m=2,\qquad d\ge4
\]
are birational. The paper proves that the quadratic-diagonal case
\[
(m,d)=(2,2)
\]
has generic degree \(2n\). It remains only to prove birationality for
\[
(m,d)=(2,3).
\]

Fix a general involutive quadric cone
\[
C=(H,[q]).
\]
Let \(p=\sigma(H)\). The form \(q\) is a general nondegenerate quadratic form on the \((2n-2)\)-dimensional quotient \(H/p\), and in particular \(q\) is irreducible.

A general cubic hypersurface containing \(C\) has, after restricting to \(H\), an equation
\[
F|_H=qB,
\]
where \(B\) is a general linear form. Choose \(B\) with
\[
B(p)\ne0.
\]
No second involutive quadric cone supported on the same hyperplane \(H\) can occur. Indeed, any second quadratic equation \(q'\) must divide \(qB\). If \(q'\) is irreducible then \(q'=q\); if \(q'\) is reducible, one of its linear factors would have to divide \(B\), but both factors of a reducible cone equation vanish at \(p\), contradicting \(B(p)\ne0\).

Consider now a second supporting hyperplane \(H'\ne H\), and put
\[
K=H\cap H'.
\]
Let \(q'\) be the second cone equation and let \(s\) be the degree of the greatest common divisor of
\[
q|_K
\quad\text{and}\quad
q'|_K.
\]

For \(n\ge4\), the quadratic form \(q|_K\) is always irreducible. If \(p\notin K\), projection from \(p\) identifies \(K\) with the quotient \(H/p\), so \(q|_K\) has rank \(2n-2\). If \(p\in K\), then \(K/p\) is a hyperplane in \(H/p\); restricting a nondegenerate quadratic form to a hyperplane lowers its rank by at most \(2\), so
\[
\operatorname{rank}(q|_K)\ge2n-4\ge4.
\]
Thus only
\[
s=0
\quad\text{or}\quad
s=2
\]
can occur.

The two-cone Hilbert-function computation of the initiating paper gives, for \(m=2\) and \(d=3\),
\[
H_0=\binom{2n}{3}-4n+4,
\qquad
H_2=\binom{2n}{3}-2n+2.
\]
Also
\[
A_n(3,2)=\binom{2n+1}{3}-(2n-1)
\]
and
\[
D_n(2)=(n-1)(2n+1).
\]
For a fixed second cone \(C'\), the codimension inside \(L_C\) of cubics containing both cones is
\[
A_n(3,2)-H_s.
\]
Hence
\[
A_n(3,2)-H_0
=
D_n(2)+2n-2,
\]
while
\[
A_n(3,2)-H_2
=
D_n(2).
\]

For the stratum \(s=0\), the entire second-cone parameter space has dimension \(D_n(2)\), strictly smaller than the imposed codimension
\[
D_n(2)+2n-2.
\]
Its union therefore cannot fill \(L_C\).

It remains to control the stratum \(s=2\). First suppose that \(p'=\sigma(H')\notin K\). Restriction from the quadratic cone forms on \(H'\) to quadrics on \(K\) is an isomorphism, because projection from \(p'\) identifies \(K\) with \(H'/p'\). Thus, for fixed \(H'\), the condition
\[
q'|_K\in\mathbf C\,q|_K
\]
determines \(q'\) uniquely up to scalar. This stratum has dimension at most
\[
2n-1<D_n(2).
\]

Now suppose \(p'\in K\). The possible \(H'\) form a family of dimension \(2n-2\). The kernel of the restriction map from cone quadrics on \(H'\) to quadrics on \(K\) has vector-space dimension \(2n-2\). Consequently, for fixed \(H'\), the projectivized inverse image of the line
\[
\mathbf C\,q|_K
\]
has dimension at most \(2n-2\). Hence this part of the \(s=2\) stratum has dimension at most
\[
4n-4.
\]
For \(n\ge4\),
\[
4n-4<D_n(2)=(n-1)(2n+1).
\]
Since the fixed-\(C'\) codimension in the \(s=2\) case is exactly \(D_n(2)\), neither part of the \(s=2\) stratum can fill \(L_C\).

Thus a general cubic in \(L_C\) contains no second involutive quadric cone. The incidence is generically one-to-one for
\[
(m,d)=(2,3)
\]
when \(n\ge4\), and therefore is birational onto its image.

Combining this with the published exact results in \(\mathbf P^3\) and \(\mathbf P^5\), Proposition 8.3, the sufficient criterion, and the published generic degree \(2n\) on the quadratic diagonal proves the stated complete range for every \(n\ge2\).

## Verification
The accompanying `verify.py` checks the exact binomial identities and all strict inequalities used to reduce the higher-dimensional range to the single pair
\[
(m,d)=(2,3).
\]
It checks the formulas for \(G_n(4,2)-D_n(2)\), the \(m\ge3\) boundary value, the two cubic Hilbert-function codimensions, and the two dimension inequalities for the \(s=2\) strata over a broad finite range.

These computations are consistency checks only. The proof for all \(n\), \(m\), and \(d\) is symbolic and is given above; the finite verification does not substitute for the irreducibility, restriction-map, or incidence-dimension arguments.

The stored replay output ends in `VERIFY_OK`.

## Relationship to prior work
The initiating paper proves the exact birational range in \(\mathbf P^3\) and \(\mathbf P^5\), proves that the quadratic-diagonal incidence has generic degree \(2n\) in every odd projective dimension, proves the boundary case \(d=m\) for \(m\ge3\), and supplies the sufficient higher-dimensional binomial criterion used above.

Its concluding remarks explicitly state that the exact birational range in
\[
\mathbf P^{2n-1},
\qquad n\ge4,
\]
is not known. The sufficient criterion leaves a small low-degree region untreated; after the elementary monotonicity reductions above, the only genuinely unresolved pair is
\[
(m,d)=(2,3).
\]
The direct two-cone incidence analysis above settles that pair uniformly.

Targeted searches for the exact range, the pair \((2,3)\) in higher dimension, cubic hypersurfaces containing involutive quadric cones, and equivalent generic-degree formulations located no covering statement. No later revision of the initiating preprint was located during the comparison.

## Limitations
The theorem determines only the generic degree of the incidence projection and hence its birationality onto the image. It does not compute the degree of the image \(B_d^m\), describe singularities of that image, or classify special hypersurfaces containing more than one involutive cone.

The proof of the cubic-quadric case is dimension-theoretic. It shows that the locus with a second cone is proper; it does not determine the number, dimensions, or scheme structures of all exceptional multiple-cone strata.

A 2014 thesis cited by the initiating paper contains earlier enumerative work on involutive cones. Only its public metadata and abstract were available in the comparison, so an unindexed formulation in that thesis remains a residual originality risk. This risk is mitigated by the initiating 2026 paper itself explicitly stating that the exact higher-dimensional birational range is unknown.

## References
1. G. A. Guedes, *Hypersurfaces containing involutive cones in projective symplectic spaces*, arXiv:2609.19427v1, 2026.
2. G. A. Guedes, *Um estudo enumerativo em variedades simpléticas projetivas*, doctoral thesis, Universidade Federal de Minas Gerais, 2014.
