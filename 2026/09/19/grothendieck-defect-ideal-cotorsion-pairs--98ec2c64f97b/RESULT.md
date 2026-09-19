# Finite Grothendieck quotients control object-cotorsion completeness

## Statement

Let \(k\) be a field and let \(\mathcal S\) be an essentially small Hom-finite semisimple
\(k\)-linear abelian category with finitely many isomorphism classes of simple objects.
Put
\[
K=K_0(\mathcal S),
\]
let \(H\le K\) be a finite-index subgroup, and write \(G=K/H\).
On
\(\mathcal D=\operatorname{Ch}^b(\mathcal S)\) use the degreewise split exact structure.
For a bounded complex \(X\), define its Euler class
\[
\chi_K(X)=\sum_n(-1)^n[H^n(X)]\in K,
\]
and let
\[
\mathcal A_H=\{X\in\mathcal D:\chi_K(X)\in H\}.
\]

Inside \(\mathcal A_H\), define
\[
\mathcal F_H=\{X:H^n(X)=0\text{ for }n\ge1\},\qquad
\mathcal C_H=\{X:H^n(X)=0\text{ for }n\le1\},
\]
and the ideals
\[
\mathcal I_H=\{f:H^n(f)=0\text{ for }n\ge1\},\qquad
\mathcal J_H=\{g:H^n(g)=0\text{ for }n\le1\}.
\]

Then:

1. \(\mathcal A_H\) is an essentially small Hom-finite weakly idempotent complete
   Frobenius exact category. Its projective-injective objects are precisely the
   contractible complexes. Its idempotent completion is \(\mathcal D\). If \(H\ne K\),
   then \(\mathcal A_H\) is not idempotent complete.

2. \[
   \mathcal I_H=\langle\mathcal F_H\rangle,\qquad
   \mathcal J_H=\langle\mathcal C_H\rangle,
   \]
   and \((\mathcal I_H,\mathcal J_H)\) is a complete ideal cotorsion pair.

3. The associated object cotorsion pair \((\mathcal F_H,\mathcal C_H)\) has exact
   obstruction classes
   \[
   \delta_-(A)=[\chi_K(H^{\le0}(A))]\in G,\qquad
   \delta_+(A)=[\chi_K(H^{\ge2}(A))]\in G.
   \]
   A special \(\mathcal F_H\)-precover of \(A\) exists if and only if
   \(\delta_-(A)=0\), and a special \(\mathcal C_H\)-preenvelope exists if and only if
   \(\delta_+(A)=0\).

4. Every pair of defect classes occurs:
   \[
   \{(\delta_-(A),\delta_+(A)):A\in\mathcal A_H\}=G\times G.
   \]
   Consequently
   \[
   (\mathcal F_H,\mathcal C_H)\text{ is complete}
   \iff G=0
   \iff H=K
   \iff \mathcal A_H\text{ is idempotent complete}.
   \]

5. Every finite abelian group occurs as such a defect group \(G\). Thus the parity
   obstruction of Ren--Wang is the first member, \(G\cong\mathbb Z/2\), of a family
   whose obstruction can have arbitrary finite abelian structure.

## Proof

Because \(\mathcal S\) is semisimple, every bounded complex is isomorphic to the
direct sum of its cohomology, with zero differential, and a contractible complex.
In particular,
\[
\chi_K(X)=\sum_n(-1)^n[X^n]
\]
in \(K_0(\mathcal S)\), so \(\chi_K\) is additive on conflations. Hence
\(\mathcal A_H\) is extension closed.

If a retraction \(X\twoheadrightarrow Y\) splits in \(\mathcal A_H\), then in
\(\mathcal D\) one has \(X\cong Y\oplus Z\). Additivity gives
\(\chi_K(Z)=\chi_K(X)-\chi_K(Y)\in H\), so \(Z\in\mathcal A_H\).
Thus \(\mathcal A_H\) is weakly idempotent complete.

Write \(K(X)=\operatorname{Cone}(1_X)\) and \(P(X)=K(X)[-1]\). The standard
degreewise split conflations
\[
0\to X[-1]\to P(X)\to X\to0,\qquad
0\to X\to K(X)\to X[1]\to0
\]
remain inside \(\mathcal A_H\), since shifts negate the Euler class and the middle
terms are contractible. They provide enough projectives and injectives.
Contractible complexes are projective-injective in the degreewise split exact
structure, and a projective or injective object is a direct summand of one of the
standard contractibles; such a summand is again contractible. Hence
\(\mathcal A_H\) is Frobenius with the stated projective-injectives.

For any \(X\in\mathcal D\), the class \(\chi_K(X)+H\) has finite order, say \(m\),
so \(X^{\oplus m}\in\mathcal A_H\). Thus every object of \(\mathcal D\) is a
direct summand of an object of \(\mathcal A_H\), proving that the idempotent
completion of \(\mathcal A_H\) is \(\mathcal D\). If \(H\ne K\), some simple
object \(S\) has \([S]\notin H\). If \(m\) is the order of \([S]+H\), then
\(S^0(S^{\oplus m})\in\mathcal A_H\), while the idempotent projecting onto one
copy has image \(S^0(S)\notin\mathcal A_H\). Hence \(\mathcal A_H\) is not
idempotent complete.

For \(X,Y\in\mathcal A_H\), extension closure and semisimplicity give
\[
\operatorname{Ext}^1_{\mathcal A_H}(X,Y)
 \cong \operatorname{Hom}_{K^b(\mathcal S)}(X,Y[1])
 \cong \bigoplus_n
 \operatorname{Hom}_{\mathcal S}(H^nX,H^{n+1}Y).
\]
Under this description, for \(f:X_0\to X_1\), \(g:Y_0\to Y_1\), the induced
action on the \(n\)-th summand is
\[
u\longmapsto H^{n+1}(g)\,u\,H^n(f).
\]
Therefore \(\operatorname{Ext}^1(f,g)=0\) whenever
\(f\in\mathcal I_H\) and \(g\in\mathcal J_H\).

Conversely, if \(H^n(f)\ne0\) for some \(n\ge1\), semisimplicity gives a simple
\(S\) and a map from the target cohomology to \(S\) that remains nonzero after
composition with \(H^n(f)\). Let \(m\) be the order of \([S]+H\) in \(G\).
Then \(T=S^{n+1}(S^{\oplus m})\) belongs to \(\mathcal C_H\), and the preceding
Ext formula produces
\(\operatorname{Ext}^1(f,1_T)\ne0\). Thus
\({}^{\perp}\mathcal J_H\subseteq\mathcal I_H\). The dual test, using
\(S^{n-1}(S^{\oplus m})\in\mathcal F_H\), gives
\(\mathcal I_H^{\perp}\subseteq\mathcal J_H\).
Hence \((\mathcal I_H,\mathcal J_H)\) is an ideal cotorsion pair.

It is also an object-ideal pair. For \(f\in\mathcal I_H\), decompose its source
as
\[
X\cong L\oplus U\oplus Q,\qquad
L=H^{\le0}(X),\quad U=H^{\ge1}(X),
\]
with \(Q\) contractible. Modulo a null-homotopic map, \(f\) factors through
\(L\). If \(m\) is the order of \(\chi_K(L)+H\), then
\(L^{\oplus m}\in\mathcal F_H\); the factorization through \(L\) can be routed
through the first copy of \(L^{\oplus m}\). The null-homotopic remainder factors
through a contractible complex. Hence
\(\mathcal I_H=\langle\mathcal F_H\rangle\). The argument for
\(\mathcal J_H=\langle\mathcal C_H\rangle\) is dual.

To prove ideal completeness, decompose
\[
A\cong L\oplus U\oplus Q,\qquad L=H^{\le0}(A),\quad U=H^{\ge1}(A),
\]
and let \(m\) be the order of \(\chi_K(U)+H\) in \(G\). The deflation
\(P(U)\twoheadrightarrow U\) extends to
\[
p:\;
E=L\oplus P(U)\oplus U[-1]^{\oplus(m-1)}\oplus Q
\longrightarrow A,
\]
where the extra summands map to zero. Its kernel is \(U[-1]^{\oplus m}\), which
lies in \(\mathcal C_H\), and
\[
\chi_K(E)=\chi_K(A)-m\chi_K(U)\in H.
\]
Moreover \(p\in\mathcal I_H\). The standard specialness criterion for an ideal
cotorsion pair therefore makes \(p\) a special \(\mathcal I_H\)-precover.
Dually, writing
\[
A\cong V\oplus W\oplus Q,\qquad V=H^{\le1}(A),\quad W=H^{\ge2}(A),
\]
and taking \(m\) to be the order of \(\chi_K(V)+H\), the inflation
\[
A\longrightarrow
K(V)\oplus W\oplus V[1]^{\oplus(m-1)}\oplus Q
\]
has cokernel \(V[1]^{\oplus m}\in\mathcal F_H\) and belongs to
\(\mathcal J_H\). It is a special \(\mathcal J_H\)-preenvelope.

Since both ideals are object ideals, their object classes form a cotorsion pair.
Now suppose
\[
0\to C\to F\to A\to0
\]
is a special object \(\mathcal F_H\)-precover. The long cohomology sequence,
using \(H^{\le1}(C)=0\) and \(H^{\ge1}(F)=0\), forces
\[
H^*(F)\cong H^{\le0}(A),
\]
so \(\chi_K(H^{\le0}(A))\in H\). This proves necessity of
\(\delta_-(A)=0\). Conversely, if this class lies in \(H\), then
\(\chi_K(U)\in H\) as well, and the construction above with \(m=1\) is a
special object precover. The dual argument proves the criterion for
\(\delta_+(A)\).

Finally, let \(g,h\in G\). Since \(G\) is finite and \(K\) is freely generated
by the simple classes, every element of \(G\) has a representative in the
nonnegative cone of \(K\): starting from an integral representative, add
sufficient multiples of the finite orders of the simple basis classes.
Choose objects \(L,M,W\in\mathcal S\) representing respectively
\(g,g+h,h\) in \(G\), and set
\[
A=S^0(L)\oplus S^1(M)\oplus S^2(W).
\]
Then
\[
\chi_K(A)\equiv g-(g+h)+h=0\pmod H,
\]
so \(A\in\mathcal A_H\), while
\[
(\delta_-(A),\delta_+(A))=(g,h).
\]
Thus the defect spectrum is all of \(G\times G\).

For any finite abelian group \(G\), choose a surjection
\(\mathbb Z^r\twoheadrightarrow G\), take a semisimple category with \(r\)
simple objects (for example finite-dimensional modules over \(k^r\)), and let
\(H\) be the kernel. This realizes \(G\) as the defect group.

## Relation to prior work

Ren and Wang, arXiv:2609.18681v1, construct the case
\(\mathcal S=\operatorname{vect}_k\), \(K\cong\mathbb Z\), \(H=2\mathbb Z\).
Their theorem proves completeness of the corresponding ideal cotorsion pair and
failure of both object-level special approximations by parity. The present result
does not claim that parity example, the Ext computation, or the underlying ideal
approximation criterion as new.

The use of Grothendieck-group subgroups to describe dense subcategories is also
prior art. Thomason classified dense triangulated subcategories by subgroups of
\(K_0\), and Matsui extended the viewpoint to dense resolving and coresolving
subcategories of exact categories. In particular, the density and idempotent-
completion aspect of \(\mathcal A_H\) should be viewed as an application of that
established \(K_0\) philosophy.

The new claim is the combination specific to ideal cotorsion theory: finite
Grothendieck quotients give complete object-ideal cotorsion pairs whose failure of
object completeness is measured exactly by two quotient-valued truncation
classes; the full defect spectrum is \(G\times G\); and every finite abelian group
is realizable as the defect group.

## Limitations

The theorem assumes \(\mathcal S\) is semisimple, Hom-finite, and has finitely
many simple isomorphism classes, and assumes \(H\) has finite index. The proof
uses semisimplicity both to split bounded complexes into cohomology plus a
contractible summand and to detect nonzero cohomology maps with simple test
objects. No claim is made for arbitrary exact or derived categories, for
infinite-index quotients, or for ordinary (non-special) precovers and
preenvelopes.

Originality is asserted only to the best of our knowledge. The 2013 paper
*Ideal approximation theory* of Fu, Guil Asensio, Herzog and Torrecillas is the
foundational source most plausibly capable of containing an abstract reformulation;
its abstract and the theorem/question statements quoted and used in later
literature were inspected, but its full text was not independently inspected here.
The directly relevant 2026 Ren--Wang paper and Matsui's Grothendieck-group
classification were inspected in full-text HTML. No source found in targeted
searches stated the quotient-valued obstruction theorem, its \(G\times G\)
realization, or arbitrary finite-abelian defect realization.

## References

1. J. Ren and Y. Wang, *A parity obstruction to completeness of object cotorsion
   pairs*, arXiv:2609.18681v1 (2026).
2. X. H. Fu, P. A. Guil Asensio, I. Herzog, and B. Torrecillas,
   *Ideal approximation theory*, Advances in Mathematics 244 (2013), 750--790,
   DOI: 10.1016/j.aim.2013.05.020.
3. R. W. Thomason, *The classification of triangulated subcategories*,
   Compositio Mathematica 105 (1997), 1--27.
4. H. Matsui, *Classifying dense (co)resolving subcategories of exact categories
   via Grothendieck groups*, arXiv:1608.00914.
5. D. Sun, Z. Tan, Q. Wang, and H. Zhu,
   *Ideal approximation theory in Frobenius categories*, arXiv:2502.11146.
