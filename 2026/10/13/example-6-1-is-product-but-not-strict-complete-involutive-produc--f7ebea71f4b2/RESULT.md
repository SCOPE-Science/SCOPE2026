# Example 6.1 is product but not strict: complete involutive product census

## Finding

Let \(K\) be a field of characteristic \(0\). Consider the five-dimensional \(4\)-Hom-Lie color algebra from Example 3.1 of Abdaoui, Gharbi, Mabrouk, and Makhlouf. Its grading is
\[
L_{00}=\langle e_1,e_2\rangle,\qquad
L_{01}=\langle e_3\rangle,\qquad
L_{10}=\langle e_4\rangle,\qquad
L_{11}=\langle e_5\rangle,
\]
its twist satisfies
\[
\alpha(e_1)=e_2,\qquad
\alpha(e_2)=e_1,\qquad
\alpha(e_i)=e_i\quad(3\le i\le5),
\]
and the nonzero twisted brackets are
\[
[e_2,e_3,e_4,e_5]_\alpha=e_2,
\]
\[
[e_1,e_3,e_4,e_5]_\alpha=e_1,
\]
\[
[e_1,e_2,e_4,e_5]_\alpha=e_3.
\]

A product structure in the source is a degree-zero map \(P\ne\pm I\) satisfying
\[
P^2=I,\qquad P\alpha=\alpha P,
\]
and the Nijenhuis identity. A strict product structure is a product structure that also lies in the centroid.

There are exactly
\[
\boxed{32}
\]
degree-zero involutions commuting with \(\alpha\). They are of two types. For signs
\[
\varepsilon,\sigma_3,\sigma_4,\sigma_5\in\{\pm1\},
\]
put
\[
D(\varepsilon;\sigma_3,\sigma_4,\sigma_5)
=
\operatorname{diag}(\varepsilon,\varepsilon,\sigma_3,\sigma_4,\sigma_5),
\]
and let \(S(\varepsilon;\sigma_3,\sigma_4,\sigma_5)\) be defined by
\[
S(e_1)=\varepsilon e_2,\qquad
S(e_2)=\varepsilon e_1,\qquad
S(e_i)=\sigma_i e_i\quad(3\le i\le5).
\]

Every \(S\)-type involution is Nijenhuis. A \(D\)-type involution fails the product condition exactly when
\[
\boxed{
\sigma_3=-\varepsilon,\qquad
\sigma_4=\sigma_5=\varepsilon.
}
\]
Thus precisely two of the \(32\) commuting involutions fail, so there are \(30\) Nijenhuis involutions. Since the source definition excludes \(\pm I\),
\[
\boxed{\text{there are exactly }28\text{ product structures}.}
\]

The strict locus is empty. More precisely,
\[
\boxed{
\operatorname{Cent}(L)\cap\{T:T\alpha=\alpha T,\ \deg T=0\}=K I.
}
\]
Hence the only involutive centroid maps are \(\pm I\), and both are excluded by the product-structure definition:
\[
\boxed{\text{there are no strict product structures}.}
\]

In particular, the map printed in the source's Example 6.1,
\[
P_0=\operatorname{diag}(1,1,-1,-1,-1),
\]
is indeed a product structure, but it is not strict. A one-bracket witness is
\[
P_0[e_2,e_3,e_4,e_5]_\alpha=e_2,
\]
whereas strict centroid compatibility in the second slot would require
\[
[e_2,P_0e_3,e_4,e_5]_\alpha
=
[e_2,-e_3,e_4,e_5]_\alpha
=
-e_2.
\]
These are unequal in characteristic \(0\).

## Assumptions and scope

The source preprint first appeared publicly on 17 May 2022 and lists \(17D30\) first among its Mathematics Subject Classification codes. Example 3.1 defines the algebra above. Section 6 defines Nijenhuis operators, product structures, and strict product structures; Example 6.1 asserts that \(P_0\) is strict.

The result concerns exactly this source example. It does not claim a classification of product structures on arbitrary \(n\)-Hom-Lie color algebras.

The source works over characteristic \(0\), which is retained here.

## Proof

A degree-zero endomorphism preserving the grading has the form
\[
P|_{\langle e_1,e_2\rangle}
=
\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
P(e_i)=\sigma_i e_i
\quad(3\le i\le5).
\]
Commutation with \(\alpha\) forces
\[
c=b,\qquad d=a.
\]
Thus the \(2\times2\) block is
\[
\begin{pmatrix}a&b\\b&a\end{pmatrix}.
\]
The involution condition gives
\[
a^2+b^2=1,\qquad 2ab=0.
\]
Since \(\operatorname{char}K=0\), either \(b=0,\ a=\pm1\), or \(a=0,\ b=\pm1\). The one-dimensional graded pieces also have signs \(\sigma_i=\pm1\). This proves the \(16+16=32\) list.

The source proves that a product structure is equivalent to both eigenspaces
\[
L_+=\ker(P-I),\qquad L_-=\ker(P+I)
\]
being graded subalgebras.

For \(D\)-type maps, the only possible failure comes from
\[
[e_1,e_2,e_4,e_5]_\alpha=e_3.
\]
The four inputs all lie in the same eigenspace exactly when
\[
\sigma_4=\sigma_5=\varepsilon.
\]
Closure then fails exactly when \(e_3\) has the opposite sign,
\[
\sigma_3=-\varepsilon.
\]
The other two nonzero brackets have output in the same \(\langle e_1,e_2\rangle\) eigenspace as their unique \(e_1\) or \(e_2\) input, so they create no further obstruction.

For \(S\)-type maps, each eigenspace contains only a one-dimensional line in \(\langle e_1,e_2\rangle\). Hence the bracket involving both \(e_1\) and \(e_2\) cannot receive all four inputs from one eigenspace. If one eigenspace contains a vector
\[
u=e_1+\delta e_2
\]
together with \(e_3,e_4,e_5\), multilinearity gives
\[
[u,e_3,e_4,e_5]_\alpha=u.
\]
Thus both eigenspaces are closed and every \(S\)-type involution is a product structure unless it equals \(\pm I\), which an \(S\)-type map never does.

For strictness, let \(T\) be degree zero and commute with \(\alpha\). Write
\[
T(e_1)=a e_1+b e_2,\qquad
T(e_2)=b e_1+a e_2,
\]
and
\[
T(e_3)=c e_3,\qquad
T(e_4)=d e_4,\qquad
T(e_5)=f e_5.
\]
Centroid compatibility applied to
\[
[e_2,e_3,e_4,e_5]_\alpha=e_2
\]
and insertion of \(T\) in the \(e_3\)-slot gives
\[
b e_1+a e_2=c e_2,
\]
so
\[
b=0,\qquad a=c.
\]
Inserting \(T\) in the \(e_4\)- and \(e_5\)-slots gives
\[
a=d=f.
\]
Therefore \(T=aI\), proving the centroid claim and the absence of strict product structures.

## Verification

The bundled checker `artifacts/verify.py` reconstructs the \(\mathbb Z_2^2\)-color skew-symmetry, the twist, and the three independent nonzero brackets.

It enumerates all \(32\) degree-zero involutions commuting with \(\alpha\). For each one it checks the source Nijenhuis identity on every ordered basis quadruple.

It independently checks the centroid identity in every slot. The output is
\[
32\text{ commuting involutions},
\quad
30\text{ Nijenhuis involutions},
\quad
28\text{ product structures},
\quad
0\text{ strict product structures}.
\]

It also verifies directly that the printed \(P_0\) is Nijenhuis but is not in the centroid. The checker returns `VERIFY_OK`.

Enumeration is not the proof of completeness; the symbolic block argument above proves the \(32\)-map exhaustion and the eigenspace/centroid arguments prove the classification.

## Relationship to prior work

The primary source defines the algebra in Example 3.1 and states in Example 6.1 that
\[
P_0=\operatorname{diag}(1,1,-1,-1,-1)
\]
is a strict product structure.

The same paper proves that product structures are characterized by closure of the \(\pm1\) eigenspaces and that strict product structures are precisely product structures in the centroid. Applying those criteria to the source's own multiplication shows that \(P_0\) is product but not strict and yields the complete \(28\)-element product census above.

The published journal record reproduces the same work. Targeted searches using the exact example number, the exact diagonal map, strict-product terminology, centroid terminology, and the full \(28\)-versus-\(0\) classification did not locate a correction or an equivalent classification.

## Limitations

The classification is for degree-zero involutions commuting with the source twist, exactly as required by the source definition of product structure.

The result concerns only Example 3.1/6.1.

It does not classify arbitrary Nijenhuis operators without the involution condition.

Failed searches do not prove absolute historical novelty.

## References

1. K. Abdaoui, R. Gharbi, S. Mabrouk, and A. Makhlouf, “Cohomology and formal deformations of \(n\)-Hom-Lie color algebras,” arXiv:2205.08341v1, first public 17 May 2022; *Ukrainian Mathematical Journal* 75 (2023), DOI `10.3842/umzh.v75i9.7238`.
