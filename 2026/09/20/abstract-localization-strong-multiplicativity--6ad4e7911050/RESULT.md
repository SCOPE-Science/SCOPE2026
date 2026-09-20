# Abstract localization rings do not characterize strong multiplicativity

## Statement

Kim and Koç define a multiplicative set \(S\) of a commutative ring \(R\) to be **strongly multiplicative** when every family \((s_i)\) in \(S\) has an element of \(S\) lying in \(\bigcap_i s_iR\). Their Theorem 2.6 in arXiv:2609.16741v1 lists, among equivalent conditions,

\[
\text{there exists }e=e^2\in R\text{ such that }R_S\cong Re\text{ as rings}.
\]

Taken literally as a bare abstract-ring isomorphism, this condition is too weak.

### Theorem
For every field \(k\), there is a commutative ring \(R\) with two multiplicative sets \(S,T\subseteq R\) such that

1. \(T\) is strongly multiplicative;
2. \(S\) is not strongly multiplicative;
3. \(R_S\cong R_T\) as unital rings; and
4. both localization rings are abstractly isomorphic to an idempotent summand \(Re\) of \(R\).

Consequently, strong multiplicativity is not determined by the abstract isomorphism type of the localization ring. The idempotent-localization clause becomes correct when the isomorphism is required to respect the canonical \(R\)-algebra structure, equivalently the localization map.

## Construction and proof

Let
\[
A=k[x],\qquad B=k[x,x^{-1}],\qquad C=\prod_{n\ge 1}B,
\]
and set
\[
R=A\times C.
\]
Let
\[
e=(0,1_C),\qquad s=(x,1_C),
\]
and define
\[
T=\{1_R,e\},\qquad S=\{s^n:n\ge0\}.
\]
Both are multiplicative sets and neither contains zero.

### 1. \(T\) is strongly multiplicative

Since \(e^2=e\), the finite multiplicative set \(T\) has \(e\) as a common multiple of all its elements. Hence \(T\) is strongly multiplicative. Localizing at \(e\) kills the complementary factor \((1-e)R=A\times0\), so
\[
R_T=R_e\cong Re\cong C.
\]

### 2. \(S\) is not strongly multiplicative

For every \(n\ge0\),
\[
s^nR=x^nA\times C.
\]
Therefore
\[
\bigcap_{n\ge0}s^nR
=
\left(\bigcap_{n\ge0}x^n k[x]\right)\times C
=0\times C.
\]
But each element of \(S\) has first coordinate \(x^m\neq0\). Thus
\[
S\cap\bigcap_{n\ge0}s^nR=\varnothing,
\]
so \(S\) is not strongly multiplicative.

### 3. Nevertheless \(R_S\cong Re\) as abstract rings

Localization of a finite product at \(s=(x,1_C)\) gives
\[
R_S\cong A_x\times C\cong B\times C.
\]
Because \(C\) is a countable product of copies of \(B\), it absorbs one extra copy:
\[
B\times C\longrightarrow C,
\qquad
(b,(c_1,c_2,\ldots))\longmapsto(b,c_1,c_2,\ldots)
\]
is a unital ring isomorphism. Hence
\[
R_S\cong B\times C\cong C\cong Re
\]
as abstract rings, even though \(S\) is not strongly multiplicative.

The same ring therefore has a strongly multiplicative set \(T\) and a non-strongly-multiplicative set \(S\) whose localization rings are abstractly isomorphic.

## Spectral separation

The defect is visible inside \(\operatorname{Spec}(R)\). Since \(R=A\times C\),
\[
\operatorname{Spec}(R)=\operatorname{Spec}(A)\sqcup\operatorname{Spec}(C).
\]
For \(S\),
\[
D(S)=D(s)=D_A(x)\sqcup\operatorname{Spec}(C).
\]
The subset \(D_A(x)\subseteq\operatorname{Spec}(k[x])\) is nonempty and proper and is not clopen, because \(k[x]\) has no nontrivial idempotents. Thus \(D(S)\) is not clopen.

By contrast,
\[
D(e)=\operatorname{Spec}(C),
\]
which is clopen. An abstract isomorphism \(R_S\cong Re\) only produces an abstract homeomorphism of their spectra; it does not identify the two spectra with the same subset of \(\operatorname{Spec}(R)\).

## Corrected idempotent-localization criterion

The problematic clause can be replaced by the following marked version:

> There exists an idempotent \(e\in R\) and an \(R\)-algebra isomorphism
> \[
> \Phi:R_S\xrightarrow{\sim}Re,
> \]
> where \(Re\) is regarded as an \(R\)-algebra via \(r\mapsto re\), such that
> \[
> \Phi(r/1)=re\qquad(r\in R).
> \]

Equivalently, the localization map \(R\to R_S\) is isomorphic, as a ring map under \(R\), to the idempotent localization \(R\to R_e\cong Re\).

With this replacement, the equivalence with strong multiplicativity is valid.

Indeed, if \(S\) is strongly multiplicative, Proposition 2.3 supplies a least element \(t\in S\), and Lemma 2.5 writes \(t=ue\) with \(u\) a unit and \(e\) idempotent. The universal property gives canonical \(R\)-algebra isomorphisms
\[
R_S\cong R_t\cong R_e\cong Re.
\]
Conversely, an \(R\)-algebra isomorphism \(R_S\cong Re\) identifies ideal extension \(IR_S\) with \(Ie\). Since multiplication by an idempotent commutes with arbitrary intersections,
\[
\left(\bigcap_\lambda I_\lambda\right)e
=
\bigcap_\lambda(I_\lambda e),
\]
localization at \(S\) commutes with arbitrary intersections of ideals. Theorem 2.6's implication from that intersection property back to strong multiplicativity then applies.

This also explains the two points where a bare abstract isomorphism is insufficient in the published proof of Theorem 2.6: identifying \(IR_S\) with \(Ie\) requires compatibility with the map from \(R\), and an abstract homeomorphism \(\operatorname{Spec}(R_S)\cong\operatorname{Spec}(Re)\) does not by itself imply equality \(D(S)=D(e)\) as subsets of \(\operatorname{Spec}(R)\).

## Scope and limitations

This result does **not** contradict the forward statement that a strongly multiplicative set yields a canonical idempotent localization. Nor does it challenge the least-element characterization or the arbitrary-intersection characterization. It isolates a distinction in the literal wording of the abstract-ring condition: the localization must be remembered together with its map from \(R\).

The counterexample uses an infinite direct product in order to exploit the absorption \(B\times B^{\mathbb N}\cong B^{\mathbb N}\). No claim is made here that such a counterexample exists under Noetherian or finite-product hypotheses.

Originality is claimed only to the best of our knowledge. The map-compatible formulation is standard localization language; the new contribution claimed here is the explicit separation showing that the bare abstract-ring wording in arXiv:2609.16741v1 is genuinely false, not merely imprecise.

## References

1. H. Kim and S. Koç, *Strongly multiplicative sets, idempotent localizations, and S-prime phenomena*, arXiv:2609.16741v1 (2026).
2. S. Koç, *On strongly multiplicative sets*, arXiv:2512.23935 (superseded by the joint preprint above).
3. H. Hamed and A. Malek, *S-prime ideals of a commutative ring*, Beitr. Algebra Geom. 61 (2020), DOI: 10.1007/s13366-019-00476-5.
