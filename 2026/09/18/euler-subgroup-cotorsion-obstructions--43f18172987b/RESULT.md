# Euler-subgroup cuts separate ideal and object cotorsion completeness

## Result

Let \(k\) be a field and let
\[
\mathcal D=\operatorname{Ch}^{b}(\operatorname{vect}_k)
\]
carry the degreewise split exact structure. For a bounded complex \(X\), write
\[
\chi(X)=\sum_n(-1)^n\dim_k H^n(X).
\]
Fix an additive subgroup \(H\leq \mathbb Z\), and define the full subcategory
\[
\mathcal A_H=\{X\in\mathcal D:\chi(X)\in H\}.
\]
Inside \(\mathcal A_H\), put
\[
\mathcal F_H=\{X:H^n(X)=0\text{ for }n\geq1\},\qquad
\mathcal C_H=\{X:H^n(X)=0\text{ for }n\leq1\},
\]
and define ideals
\[
\mathcal I_H=\{f:H^n(f)=0\text{ for }n\geq1\},\qquad
\mathcal J_H=\{g:H^n(g)=0\text{ for }n\leq1\}.
\]

**Theorem 1 (Euler-subgroup family).** For every subgroup \(H\leq\mathbb Z\):

1. \(\mathcal A_H\) is a Hom-finite, weakly idempotent complete Frobenius exact category. Its projective-injective objects are exactly the contractible complexes.
2. The two ideals are object ideals:
   \[
   \mathcal I_H=\langle\mathcal F_H\rangle,\qquad
   \mathcal J_H=\langle\mathcal C_H\rangle.
   \]
3. They form a complete ideal cotorsion pair:
   \[
   {}^\perp\mathcal J_H=\mathcal I_H,\qquad
   \mathcal I_H^\perp=\mathcal J_H.
   \]
4. For \(A\in\mathcal A_H\), define two obstruction classes
   \[
   o_-(A)=\chi(H^{\leq0}(A))+H,\qquad
   o_+(A)=\chi(H^{\geq2}(A))+H
   \]
   in \(\mathbb Z/H\). Then \(A\) admits a special \(\mathcal F_H\)-precover if and only if \(o_-(A)=0\), and a special \(\mathcal C_H\)-preenvelope if and only if \(o_+(A)=0\).
5. Consequently, the associated object cotorsion pair \((\mathcal F_H,\mathcal C_H)\) is complete if and only if \(H=\mathbb Z\). For every proper subgroup \(H<\mathbb Z\), the single object
   \[
   W=S^0(k)\oplus S^1(k^2)\oplus S^2(k)
   \]
   belongs to \(\mathcal A_H\) and has neither a special \(\mathcal F_H\)-precover nor a special \(\mathcal C_H\)-preenvelope.
6. If \(H<\mathbb Z\), then \(\mathcal A_H\) is not idempotent complete, but its idempotent completion is \(\mathcal D\).

For \(H=m\mathbb Z\) with \(m\geq2\), the two obstruction coordinates are independent: every
\[
(a,b)\in(\mathbb Z/m\mathbb Z)^2
\]
occurs as \((o_-(A),o_+(A))\). Indeed, for representatives \(0\leq a,b<m\),
\[
A_{a,b}=S^0(k^a)\oplus S^1(k^{a+b})\oplus S^2(k^b)
\]
has \(\chi(A_{a,b})=0\), \(o_-(A_{a,b})=a\), and \(o_+(A_{a,b})=b\).

The parity example of Ren and Wang is exactly the case \(H=2\mathbb Z\). Thus the ideal/object completeness gap is not intrinsically a parity phenomenon: it persists for every proper subgroup of the Euler-characteristic group.

There is, however, a genuinely parity-specific feature in the original formulation. Let
\[
\beta(X)=\sum_n\dim_k H^n(X)
\]
be the total Betti number and, for a positive integer \(m\), let
\[
\mathcal B_m=\{X\in\mathcal D:\beta(X)\in m\mathbb Z\}.
\]

**Theorem 2 (sharp total-Betti threshold).**
\[
\boxed{\mathcal B_m\text{ is extension closed if and only if }m\in\{1,2\}.}
\]
Hence replacing “even total cohomology dimension” by “total cohomology dimension divisible by \(m\)” does not yield the same exact-category mechanism for any \(m>2\). The correct all-modulus extension is the Euler-subgroup condition \(\chi(X)\in H\).

## Proof

### 1. The exact and Frobenius structure

Euler characteristic is additive on degreewise split conflations. Therefore \(\mathcal A_H\) is extension closed in \(\mathcal D\) and inherits an exact structure.

Weak idempotent completeness follows from the subgroup condition. If a split epimorphism \(X\to Y\) occurs between objects of \(\mathcal A_H\), its kernel \(K\) in \(\mathcal D\) satisfies
\[
\chi(K)=\chi(X)-\chi(Y)\in H;
\]
dually, the cokernel of a split monomorphism again has Euler characteristic in \(H\).

For any complex \(U\), use the standard contractible complexes \(K(U)\) and \(P(U)=K(U[-1])\) in degreewise split conflations
\[
0\to U\to K(U)\to U[1]\to0,\qquad
0\to U[-1]\to P(U)\to U\to0.
\]
Contractible complexes have Euler characteristic \(0\), and shifts negate Euler characteristic. Hence these conflations remain inside \(\mathcal A_H\) whenever \(U\in\mathcal A_H\), giving enough injectives and projectives. As in the ambient degreewise split exact category, the projective-injective objects are exactly the contractible complexes. Thus \(\mathcal A_H\) is Frobenius.

### 2. Stable extensions and ideal orthogonality

Every bounded complex of finite-dimensional vector spaces decomposes as
\[
X\cong H(X)\oplus Q_X,
\]
with \(Q_X\) contractible. Consequently
\[
\operatorname{Ext}^1_{\mathcal A_H}(X,Y)
\cong
\bigoplus_{n\in\mathbb Z}
\operatorname{Hom}_k(H^nX,H^{n+1}Y).
\]
For morphisms \(f:X_0\to X_1\) and \(g:Y_0\to Y_1\), the induced map on an extension family \((u_n)\) is
\[
(u_n)\longmapsto
\bigl(H^{n+1}(g)\,u_n\,H^n(f)\bigr)_n.
\]
Thus \(\operatorname{Ext}^1(\mathcal I_H,\mathcal J_H)=0\).

For the converse, suppose \(f\notin\mathcal I_H\). Choose \(n\geq1\) with \(H^n(f)\neq0\). The test object
\[
T=S^{n+1}(k)\oplus S^{n+2}(k)
\]
has Euler characteristic \(0\), belongs to \(\mathcal C_H\) for every \(H\), and hence \(1_T\in\mathcal J_H\). A linear functional detecting a nonzero vector in the image of \(H^n(f)\) gives an extension class on which
\(\operatorname{Ext}^1(f,1_T)\) is nonzero. Therefore
\({}^\perp\mathcal J_H\subseteq\mathcal I_H\).

Dually, if \(g\notin\mathcal J_H\), choose \(r\leq1\) with \(H^r(g)\neq0\) and use
\[
T'=S^{r-1}(k)\oplus S^{r-2}(k)\in\mathcal F_H.
\]
Then \(\operatorname{Ext}^1(1_{T'},g)\neq0\). Hence
\[
{}^\perp\mathcal J_H=\mathcal I_H,\qquad
\mathcal I_H^\perp=\mathcal J_H.
\]

### 3. The ideals are object ideals

If \(f\in\mathcal I_H\), split the cohomology of its domain into the part \(L=H^{\leq0}\) and the complementary positive-degree part, plus a contractible summand. The component of \(f\) detected on cohomology factors through \(L\). Choose a zero-differential complex \(R\), supported in degrees \(\leq0\), with
\[
\chi(R)=-\chi(L).
\]
Then \(L\oplus R\in\mathcal F_H\) because its Euler characteristic is \(0\). The difference between \(f\) and the cohomological component is null-homotopic and therefore factors through a contractible complex, which also lies in \(\mathcal F_H\). Thus \(f\) factors through an object of \(\mathcal F_H\).

This proves \(\mathcal I_H=\langle\mathcal F_H\rangle\). The dual argument, stabilizing the cohomology in degrees \(\geq2\) by a zero-differential complex of opposite Euler characteristic supported in degrees \(\geq2\), gives
\[
\mathcal J_H=\langle\mathcal C_H\rangle.
\]

### 4. Uniform special ideal approximations

For an integer \(a\), choose zero-differential complexes
\[
R_-(a)\quad\text{supported in degrees }\leq0,\qquad
R_+(a)\quad\text{supported in degrees }\geq2,
\]
with Euler characteristic \(a\). One explicit choice is
\[
R_-(a)=
\begin{cases}
S^0(k^a),&a\geq0,\\
S^{-1}(k^{-a}),&a<0,
\end{cases}
\qquad
R_+(a)=
\begin{cases}
S^2(k^a),&a\geq0,\\
S^3(k^{-a}),&a<0.
\end{cases}
\]

Let
\[
A\cong L\oplus U\oplus Q,
\]
where \(L=H^{\leq0}(A)\), \(U=H^{\geq1}(A)\), and \(Q\) is contractible. Put
\[
C_A=U[-1]\oplus R_+(\chi(U))
\]
and
\[
E_A=L\oplus P(U)\oplus R_+(\chi(U))\oplus Q.
\]
Using \(P(U)\twoheadrightarrow U\), the identity on \(L\oplus Q\), and zero on the correction summand gives a degreewise split conflation
\[
0\to C_A\to E_A\xrightarrow{p_A}A\to0.
\]
Because
\[
\chi(C_A)=-\chi(U)+\chi(U)=0,\qquad
\chi(E_A)=\chi(A),
\]
all three objects belong to \(\mathcal A_H\), and \(C_A\in\mathcal C_H\). The map \(p_A\) is in \(\mathcal I_H\). It factors through
\[
F_A^\sharp=
L\oplus R_-(-\chi(L))\oplus P(U)\oplus Q\in\mathcal F_H.
\]
Thus \(p_A\) is an object-special \(\mathcal I_H\)-precover.

Dually, write
\[
A\cong V\oplus W\oplus Q,
\]
where \(V=H^{\leq1}(A)\) and \(W=H^{\geq2}(A)\). Put
\[
F_A=V[1]\oplus R_-(\chi(V))
\]
and
\[
D_A=K(V)\oplus W\oplus R_-(\chi(V))\oplus Q.
\]
The standard injection \(V\hookrightarrow K(V)\), the identity on \(W\oplus Q\), and zero into the correction term define a conflation
\[
0\to A\xrightarrow{j_A}D_A\to F_A\to0.
\]
Again \(\chi(F_A)=0\), \(\chi(D_A)=\chi(A)\), and \(F_A\in\mathcal F_H\). Moreover \(j_A\in\mathcal J_H\), and it factors through
\[
C_A^\sharp=
K(V)\oplus W\oplus R_+(-\chi(W))\oplus Q\in\mathcal C_H.
\]
Hence \(j_A\) is an object-special \(\mathcal J_H\)-preenvelope. The ideal cotorsion pair is complete.

### 5. Exact obstruction to object completeness

Suppose a conflation
\[
0\to C\to F\to A\to0
\]
exists with \(F\in\mathcal F_H\) and \(C\in\mathcal C_H\). The long exact cohomology sequence forces
\[
H^{\leq0}(F)\cong H^{\leq0}(A)
\]
and \(F\) has no positive cohomology. Hence
\[
\chi(H^{\leq0}(A))=\chi(F)\in H.
\]
This proves necessity of \(o_-(A)=0\).

Conversely, if \(\chi(L)\in H\) for \(L=H^{\leq0}(A)\), then
\[
\chi(U)=\chi(A)-\chi(L)\in H
\]
for \(U=H^{\geq1}(A)\). The unstabilized cone sequence
\[
0\to U[-1]\to L\oplus P(U)\oplus Q\to A\to0
\]
lies entirely in \(\mathcal A_H\), its middle term belongs to \(\mathcal F_H\), and its kernel belongs to \(\mathcal C_H\). Thus it is a special \(\mathcal F_H\)-precover. This proves the first obstruction criterion. The second follows dually from the truncation \(H^{\geq2}(A)\).

If \(H<\mathbb Z\), then \(1\notin H\). For
\[
W=S^0(k)\oplus S^1(k^2)\oplus S^2(k),
\]
we have \(\chi(W)=0\), while
\[
\chi(H^{\leq0}(W))=1,\qquad
\chi(H^{\geq2}(W))=1.
\]
Hence both object approximations fail on the same object.

The same subgroup argument also identifies the idempotent-completion boundary. If \(H<\mathbb Z\), the object \(W\in\mathcal A_H\) has the direct summand \(S^0(k)\notin\mathcal A_H\), so \(\mathcal A_H\) is not idempotent complete. Conversely, every \(X\in\mathcal D\) is a direct summand of an object of \(\mathcal A_H\): choose a stalk complex \(R\) with
\[
\chi(R)=-\chi(X),
\]
so \(X\oplus R\) has Euler characteristic \(0\in H\). Therefore the idempotent completion of \(\mathcal A_H\) is \(\mathcal D\).

### 6. Why total-Betti congruences stop at parity

For a degreewise split conflation
\[
0\to X\to Y\to Z\to0
\]
with connecting maps
\[
\delta_n:H^n(Z)\to H^{n+1}(X),
\]
exactness gives
\[
\beta(Y)=\beta(X)+\beta(Z)-2\sum_n\operatorname{rank}\delta_n.
\]
Thus \(\mathcal B_1=\mathcal D\), and \(\mathcal B_2\) is extension closed.

Now let \(m>2\). Take
\[
X=S^1(k^m),\qquad Z=S^0(k^m).
\]
Both have total Betti number \(m\). Choose an extension class whose only connecting map
\[
\delta_0:k^m\to k^m
\]
has rank \(1\). Such a class exists because
\[
\operatorname{Ext}^1_{\mathcal D}(Z,X)
\cong\operatorname{Hom}_k(k^m,k^m).
\]
For its middle term \(Y\),
\[
\beta(Y)=2m-2,
\]
which is not divisible by \(m\). Hence \(\mathcal B_m\) is not extension closed for any \(m>2\).

## Relation to prior work

Ren and Wang construct the case in which the ambient category consists of bounded complexes with **even total cohomology dimension**. Since
\[
\beta(X)\equiv\chi(X)\pmod2,
\]
their category is precisely \(\mathcal A_{2\mathbb Z}\). They prove that it is Hom-finite, weakly idempotent complete and Frobenius, construct the complete ideal cotorsion pair, and identify parity conditions for special object approximations. Those parity results are prior work.

The present result claims novelty only for the subgroup-level extension: the family \(\mathcal A_H\) for every \(H\leq\mathbb Z\), the uniform Euler-zero stabilization of the ideal approximations, the \(\mathbb Z/H\)-valued pair of exact object-approximation obstructions, completeness exactly at \(H=\mathbb Z\), simultaneous failure on a single universal three-degree object for every proper \(H\), realization of every residue pair for \(H=m\mathbb Z\), and the sharp statement that total-Betti divisibility itself is extension closed only for moduli \(1\) and \(2\).

Fu, Guil Asensio, Herzog and Torrecillas introduced ideal approximation theory and the completeness question for object ideals. Subsequent work established positive results under additional hypotheses, while Wang, Wang and Zhu produced a negative example in a more general exact-category setting. These are treated as prior work.

Targeted searches for arbitrary Euler-characteristic subgroups, congruence-valued truncation obstructions, and higher-modulus total-Betti versions did not locate the statements above. Originality is therefore asserted only to the best of our knowledge.

## Limitations

The construction uses bounded complexes of finite-dimensional vector spaces and the degreewise split exact structure. It does not assert an analogous subgroup classification for arbitrary Frobenius exact categories or for a general additive \(K_0\)-valued invariant.

The source of the parity construction is a recent first version and may be revised. General ideal-approximation literature was checked for the directly relevant completeness statements, but not every theorem in the older literature was inspected under every possible reformulation. Because the extension from parity to an arbitrary subgroup is elementary once Euler additivity is isolated, an equivalent observation may exist in terminology not captured by the searches.

Theorem 2 concerns extension closure of the full subcategory cut out by total Betti divisibility; it does not say that other higher-modulus constructions are impossible.

## References

1. J. Ren and Y. Wang, *A parity obstruction to completeness of object cotorsion pairs*, arXiv:2609.18681v1 (2026). https://arxiv.org/abs/2609.18681
2. X. H. Fu, P. A. Guil Asensio, I. Herzog and B. Torrecillas, *Ideal approximation theory*, Advances in Mathematics **244** (2013), 750–790. https://doi.org/10.1016/j.aim.2013.05.020
3. D. Sun, Z. Tan, Q. Wang and H. Zhu, *Ideal approximation theory in Frobenius categories*, arXiv:2502.11146 (2025). https://arxiv.org/abs/2502.11146
4. Q. Wang, Y. Wang and H. Zhu, *A counterexample to the open question on object ideals*, arXiv:2609.14382 (2026). https://arxiv.org/abs/2609.14382
