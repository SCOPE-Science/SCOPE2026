# Finite Grothendieck quotients produce cotorsion completeness obstructions

Let \(k\) be a field and let \(\mathcal S\) be an essentially small Hom-finite semisimple
\(k\)-linear abelian category in which every object has finite length. Let
\[
\varphi:K_0(\mathcal S)\longrightarrow G
\]
be a nonzero homomorphism to a finite abelian group, and write
\(e=\exp(\operatorname{im}\varphi)\ge 2\). For a bounded complex \(X\) define its
Euler class
\[
\kappa(X)=\sum_n(-1)^n[H^n(X)]\in K_0(\mathcal S).
\]
Let
\[
\mathcal A_\varphi=
\left\{X\in \operatorname{Ch}^b(\mathcal S):\varphi(\kappa(X))=0\right\},
\]
equipped with the degreewise-split exact structure inherited from
\(\operatorname{Ch}^b(\mathcal S)\).

Define full subcategories
\[
\mathcal F=\{X\in\mathcal A_\varphi:H^n(X)=0\text{ for }n\ge1\},
\qquad
\mathcal C=\{X\in\mathcal A_\varphi:H^n(X)=0\text{ for }n\le1\},
\]
and ideals
\[
\mathcal I=\{f:H^n(f)=0\text{ for }n\ge1\},
\qquad
\mathcal J=\{g:H^n(g)=0\text{ for }n\le1\}.
\]

## Theorem

With the notation above:

1. \(\mathcal A_\varphi\) is an essentially small Hom-finite weakly idempotent
   complete Frobenius exact category. Its projective-injective objects are the
   contractible complexes.
2. \(\mathcal I=\langle\mathcal F\rangle\) and
   \(\mathcal J=\langle\mathcal C\rangle\) are object ideals, and
   \((\mathcal I,\mathcal J)\) is a complete ideal cotorsion pair.
3. The associated cotorsion pair of objects \((\mathcal F,\mathcal C)\) is neither
   special precovering nor special preenveloping.
4. \(\mathcal A_\varphi\) is not idempotent complete, while its idempotent
   completion is all of \(\operatorname{Ch}^b(\mathcal S)\).

Consequently, every nontrivial finite quotient of \(K_0(\mathcal S)\) yields a
congruence obstruction to completeness descent from object ideals to their
objects.

For \(\mathcal S=\operatorname{vect}_k^{\mathrm{fd}}\) and
\(\varphi:\mathbb Z\to\mathbb Z/m\mathbb Z\), this gives, for every \(m\ge2\),
\[
\mathcal A_m=
\{X:\chi(H^\ast X)\equiv0\pmod m\},
\]
where \(\chi(H^\ast X)=\sum_n(-1)^n\dim_kH^n(X)\).
When \(m=2\), the signs disappear modulo two, so this is exactly the
even-total-cohomology condition used by Ren--Wang. For \(m>2\), the correct
extension-stable replacement is the signed Euler congruence, not congruence of
the unsigned total cohomology dimension.

## Proof

### 1. Exact and Frobenius structure

The Euler class is additive on short exact sequences of complexes, hence
\(\mathcal A_\varphi\) is extension closed. Suppose a split monomorphism
\(X\to Y\) in \(\mathcal A_\varphi\) has ambient complement \(Z\), so
\(Y\cong X\oplus Z\). Then
\[
\varphi(\kappa(Z))
=\varphi(\kappa(Y)-\kappa(X))=0,
\]
so \(Z\in\mathcal A_\varphi\). The dual argument treats split epimorphisms.
Thus \(\mathcal A_\varphi\) is weakly idempotent complete.

The category of bounded complexes with the degreewise-split exact structure is
Frobenius, with contractible complexes as projective-injectives. Every
contractible complex has Euler class zero and therefore lies in
\(\mathcal A_\varphi\). For every \(X\in\mathcal A_\varphi\), standard cone
conflations provide
\[
0\to X[-1]\to P(X)\to X\to0,
\qquad
0\to X\to K(X)\to X[1]\to0,
\]
with \(P(X)\) and \(K(X)\) contractible. Since shifts negate the Euler class,
all terms lie in \(\mathcal A_\varphi\). Hence the inherited exact category has
enough projectives and injectives. If an object is projective or injective in
\(\mathcal A_\varphi\), one of these conflations splits, making it a retract of
a contractible complex; such a retract is contractible. This proves the
Frobenius assertion.

### 2. The two object ideals

Because \(\mathcal S\) is semisimple, every bounded complex splits as a direct
sum of its cohomology stalk complexes and a contractible complex. If
\(f:X\to Y\) belongs to \(\mathcal I\), write
\[
X\cong L\oplus U\oplus Q,
\]
where \(L\) has cohomology only in degrees \(\le0\), \(U\) only in degrees
\(\ge1\), and \(Q\) is contractible. Let \(f_0\) be the part of \(f\) obtained by
restricting to \(L\). Then \(f-f_0\) induces zero on every cohomology object and
is therefore null-homotopic, hence factors through a contractible object of
\(\mathcal F\).

The map \(f_0\) factors through \(L^{\oplus e}\). Since
\[
\varphi(\kappa(L^{\oplus e}))=e\,\varphi(\kappa(L))=0,
\]
the object \(L^{\oplus e}\) belongs to \(\mathcal A_\varphi\), and it lies in
\(\mathcal F\). Thus \(f\) factors through an object of \(\mathcal F\), proving
\(\mathcal I=\langle\mathcal F\rangle\). The reverse containment is immediate.
The dual argument gives
\(\mathcal J=\langle\mathcal C\rangle\).

### 3. Cotorsion orthogonality

Since \(\mathcal A_\varphi\) is extension closed, its first extension group is
the ambient one. Semisimplicity gives the natural decomposition
\[
\operatorname{Ext}^1_{\mathcal A_\varphi}(X,Y)
\cong
\operatorname{Hom}_{K^b(\mathcal S)}(X,Y[1])
\cong
\bigoplus_n
\operatorname{Hom}_{\mathcal S}(H^nX,H^{n+1}Y).
\tag{1}
\]
For \(f\in\mathcal I\) and \(g\in\mathcal J\), every component of the induced
map \(\operatorname{Ext}^1(f,g)\) vanishes: for \(n\ge1\) the \(f\)-factor
vanishes, and for \(n\le0\) the \(g\)-factor in degree \(n+1\le1\) vanishes.
Hence \(\mathcal I\subseteq{}^\perp\mathcal J\).

Conversely, if \(f\notin\mathcal I\), choose \(n\ge1\) with
\(H^n(f)\ne0\), and let \(B\) be the codomain of \(H^n(f)\). The stalk complex
\[
T=S^{n+1}(B^{\oplus e})
\]
belongs to \(\mathcal C\cap\mathcal A_\varphi\). Composing \(H^n(f)\) with the
inclusion of \(B\) into one summand of \(B^{\oplus e}\) gives a nonzero
component in (1), so
\(\operatorname{Ext}^1(f,1_T)\ne0\). Since \(1_T\in\mathcal J\), this proves
\({}^\perp\mathcal J\subseteq\mathcal I\). The dual argument, using a stalk in
degree \(m-1\) when \(H^m(g)\ne0\) for \(m\le1\), proves
\(\mathcal I^\perp=\mathcal J\). Thus
\((\mathcal I,\mathcal J)\) is an ideal cotorsion pair.

The same test-stalk argument at the object level shows
\[
{}^\perp\mathcal C=\mathcal F,
\qquad
\mathcal F^\perp=\mathcal C.
\tag{2}
\]

### 4. Explicit completeness of the ideal pair

Let \(A\in\mathcal A_\varphi\), and split
\[
A\cong L\oplus U\oplus Q
\]
as above. Choose a contractible \(P(U)\) in a conflation
\[
0\to U[-1]\to P(U)\xrightarrow{q_U}U\to0.
\]
Set
\[
E_A=L\oplus P(U)\oplus U[-1]^{\oplus(e-1)}\oplus Q,
\]
and let \(p_A:E_A\to A\) be the identity on \(L\) and \(Q\), the map \(q_U\) on
\(P(U)\), and zero on the extra copies of \(U[-1]\). Then
\[
\ker p_A\cong U[-1]^{\oplus e}\in\mathcal C.
\]
Moreover
\[
\varphi(\kappa(E_A))
=
\varphi(\kappa(L)-(e-1)\kappa(U))
=
-e\,\varphi(\kappa(U))=0,
\]
because \(\varphi(\kappa(L)+\kappa(U))=0\). Thus \(E_A\in\mathcal A_\varphi\),
and \(p_A\in\mathcal I\). The kernel inclusion lies in \(\mathcal J\), so
\(p_A\) is a special \(\mathcal I\)-precover.

Dually, split
\[
A\cong V\oplus W\oplus Q,
\]
where \(V\) has cohomology only in degrees \(\le1\) and \(W\) only in degrees
\(\ge2\). Choose a contractible \(K(V)\) in
\[
0\to V\xrightarrow{i_V}K(V)\to V[1]\to0.
\]
Set
\[
D_A=K(V)\oplus W\oplus V[1]^{\oplus(e-1)}\oplus Q.
\]
The natural inflation \(j_A:A\to D_A\), using \(i_V\), the identity on \(W,Q\),
and zero into the extra summands, has
\[
\operatorname{coker}j_A\cong V[1]^{\oplus e}\in\mathcal F,
\]
belongs to \(\mathcal J\), and has cokernel projection in \(\mathcal I\).
The same Euler-class calculation shows \(D_A\in\mathcal A_\varphi\).
Hence \(j_A\) is a special \(\mathcal J\)-preenvelope. Therefore
\((\mathcal I,\mathcal J)\) is complete.

### 5. Failure of object completeness

Choose \(R\in\mathcal S\) with \(\varphi([R])\ne0\). The complex
\[
M=S^0(R)\oplus S^1(R)
\]
lies in \(\mathcal A_\varphi\) because \(\kappa(M)=0\).
If \(M\) had a special \(\mathcal F\)-precover, there would be a conflation
\[
0\to C'\to F'\to M\to0
\]
with \(F'\in\mathcal F\) and \(C'\in\mathcal C\). The long exact cohomology
sequence and the support conditions force
\[
H^0(F')\cong R,\qquad H^n(F')=0\quad(n\ne0).
\]
Thus \(\kappa(F')=[R]\), contradicting
\(F'\in\mathcal A_\varphi\).

Likewise
\[
M^+=S^1(R)\oplus S^2(R)
\]
has Euler class zero. A special \(\mathcal C\)-preenvelope
\[
0\to M^+\to C''\to F''\to0
\]
would force \(H^2(C'')\cong R\) and all other cohomology of \(C''\) to vanish,
again contradicting \(\varphi(\kappa(C''))=\varphi([R])\ne0\).
Therefore the object cotorsion pair (2) is neither special precovering nor
special preenveloping.

### 6. Idempotent completion

For every ambient bounded complex \(X\),
\[
\varphi(\kappa(X^{\oplus e}))=e\,\varphi(\kappa(X))=0.
\]
Hence \(X^{\oplus e}\in\mathcal A_\varphi\), while \(X\) is a direct summand of
\(X^{\oplus e}\). Thus the idempotent completion of
\(\mathcal A_\varphi\) is all of \(\operatorname{Ch}^b(\mathcal S)\).

On the other hand, choose \(R\) as above and let \(d\ge2\) be the order of
\(\varphi([R])\). The stalk \(S^0(R^{\oplus d})\) belongs to
\(\mathcal A_\varphi\), but its idempotent projection onto one copy of \(R\)
cannot split inside \(\mathcal A_\varphi\), because \(S^0(R)\notin
\mathcal A_\varphi\). Hence \(\mathcal A_\varphi\) itself is not idempotent
complete. ∎

## Structural interpretation

The parity counterexample of Ren--Wang is therefore the smallest instance of a
finite Grothendieck-quotient mechanism. Modulo two, total cohomology dimension
and Euler characteristic have the same parity; this hides the signed
\(K_0\)-class that is actually additive under extensions. Passing from
\(\mathbb Z/2\) to a general finite quotient exposes the mechanism and permits
simultaneous congruence conditions when \(K_0(\mathcal S)\) has rank greater
than one.

Kernels of homomorphisms from Grothendieck groups are classical sources of
dense subcategories, going back to Thomason and, in exact-category form, work
of Matsui. No novelty is claimed for that dense-subcategory mechanism itself.
The contribution here is that every nonzero finite \(K_0\)-quotient in this
semisimple-complex setting supports the explicit complete ideal cotorsion pair
above while its object cotorsion pair fails completeness.

## Relation to prior literature

Ren--Wang construct the modulus-two vector-space case: bounded complexes whose
total cohomology dimension is even, with the same two cohomological object
ideals. Their example is Hom-finite, weakly idempotent complete and Frobenius,
and they prove that the ideal cotorsion pair is complete while the object pair
is neither special precovering nor special preenveloping.

Sun--Wang--Zhu prove positive completeness-descent results under additional
hypotheses, while Zhang--Zhou obtain a positive correspondence in
Krull--Schmidt exact categories. The construction here remains outside the
idempotent-complete/Krull--Schmidt regime and is compatible with those results.

Targeted searches for congruence-mod-\(m\), finite-Grothendieck-quotient, and
Grothendieck-group formulations of this cotorsion counterexample found the
Ren--Wang parity construction and the classical dense-subcategory literature,
but no matching general finite-quotient theorem. The originality claim is
therefore limited to the theorem above, to the best of our knowledge.

## Limitations

The motivating Ren--Wang source is a very recent v1 preprint, so a concurrent
revision or independent generalization is a realistic residual risk. The
literature on dense subcategories defined through \(K_0\) is classical and is
not claimed as new. The proof here is restricted to bounded complexes over
Hom-finite semisimple finite-length categories; extending the mechanism beyond
the semisimple setting would require replacing the cohomology splitting and
the explicit Ext formula. No independent validation is asserted.

## References

1. J. Ren, Y. Wang, *A parity obstruction to completeness of object cotorsion
   pairs*, arXiv:2609.18681v1 (2026).
   https://arxiv.org/abs/2609.18681
2. D. Sun, Q. Wang, H. Zhu, *Cotorsion pairs and Enochs Conjecture for object
   ideals*, arXiv:2412.05519 (2024).
   https://arxiv.org/abs/2412.05519
3. Y. Zhang, P. Zhou, *Ideal n-cotorsion pairs in Frobenius extriangulated
   categories*, arXiv:2606.29728 (2026).
   https://arxiv.org/abs/2606.29728
4. H. Matsui, *Classifying dense resolving and coresolving subcategories of
   exact categories via Grothendieck groups*, Algebr. Represent. Theory 21
   (2018), 551--563, DOI 10.1007/s10468-017-9726-8; arXiv:1608.00914.
   https://arxiv.org/abs/1608.00914
