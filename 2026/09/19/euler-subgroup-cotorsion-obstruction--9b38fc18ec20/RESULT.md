# Euler-subgroup obstructions to object cotorsion completeness

Let \(k\) be a field and let
\[
\mathcal D=\operatorname{Ch}^b(\operatorname{vect}_k)
\]
with the degreewise split exact structure. For a bounded complex \(X\), write
\[
\chi(X)=\sum_n(-1)^n\dim_k H^n(X).
\]
For an additive subgroup \(B\leq \mathbb Z\), define the full subcategory
\[
\mathcal A_B=\{X\in\mathcal D:\chi(X)\in B\}.
\]
Since every subgroup of \(\mathbb Z\) is \(d\mathbb Z\) for a unique \(d\geq 0\), with \(0\mathbb Z=\{0\}\), this gives an Euler-congruence family that includes the zero-Euler subcategory.

Define
\[
\mathcal F_B=\{X\in\mathcal A_B:H^n(X)=0\text{ for }n\geq1\},
\qquad
\mathcal C_B=\{X\in\mathcal A_B:H^n(X)=0\text{ for }n\leq1\},
\]
and ideals
\[
\mathcal I_B=\{f:H^n(f)=0\text{ for }n\geq1\},\qquad
\mathcal J_B=\{g:H^n(g)=0\text{ for }n\leq1\}.
\]

## Main theorem

For every additive subgroup \(B\leq\mathbb Z\):

1. \(\mathcal A_B\) is a Hom-finite, weakly idempotent complete Frobenius exact category. Its projective-injective objects are exactly the contractible complexes.
2. \(\mathcal I_B=\langle\mathcal F_B\rangle\) and \(\mathcal J_B=\langle\mathcal C_B\rangle\).
3. \((\mathcal I_B,\mathcal J_B)\) is a complete ideal cotorsion pair, and \((\mathcal F_B,\mathcal C_B)\) is the associated cotorsion pair of objects.
4. For \(A\in\mathcal A_B\), a special \(\mathcal F_B\)-object precover exists if and only if
\[
\chi\!\left(H^{\leq0}(A)\right)\in B,
\]
and a special \(\mathcal C_B\)-object preenvelope exists if and only if
\[
\chi\!\left(H^{\geq2}(A)\right)\in B.
\]
Consequently,
\[
\boxed{\;(\mathcal F_B,\mathcal C_B)\text{ is complete }\Longleftrightarrow B=\mathbb Z.\;}
\]
If \(B\neq\mathbb Z\), neither half is special: the failure occurs already for
\[
M=S^0(k)\oplus S^1(k),\qquad
N=S^1(k)\oplus S^2(k),
\]
both of which have Euler characteristic \(0\).
5. If \(B\neq\mathbb Z\), the idempotent completion of \(\mathcal A_B\) is \(\mathcal D\).

Thus the obstruction is not specifically parity. It is exactly the failure of the allowed Euler-characteristic subgroup to contain \(1\). The parity example is the case \(B=2\mathbb Z\), while \(B=\{0\}\) gives a zero-Euler counterexample.

## Proof

### 1. The exact and Frobenius structure

Euler characteristic is additive on degreewise split short exact sequences. Hence \(\mathcal A_B\) is extension closed in \(\mathcal D\), and inherits an exact structure. If \(X\to Y\) is a split monomorphism in \(\mathcal A_B\), then its ambient complement \(Z\) satisfies
\[
\chi(Z)=\chi(Y)-\chi(X)\in B,
\]
so \(Z\in\mathcal A_B\); therefore \(\mathcal A_B\) is weakly idempotent complete.

Shifts preserve membership because \(\chi(X[1])=-\chi(X)\). The standard contractible cone sequences
\[
0\to X\to K(X)\to X[1]\to0,\qquad
0\to X[-1]\to P(X)\to X\to0
\]
therefore lie in \(\mathcal A_B\). As in the ambient degreewise split exact category, bounded contractible complexes are projective and injective; these cone sequences give enough of both. Conversely, a projective or injective object is a retract of a contractible complex and is therefore contractible.

The usual cohomology splitting
\[
X\cong H(X)\oplus Q_X,\qquad Q_X\text{ contractible},
\]
also stays inside \(\mathcal A_B\), because \(\chi(H(X))=\chi(X)\in B\).

### 2. Extensions and the two object ideals

For \(X,Y\in\mathcal A_B\), extension closure gives the same degreewise-split extension calculation as in \(\mathcal D\):
\[
\operatorname{Ext}^1_{\mathcal A_B}(X,Y)
\cong
\bigoplus_n\operatorname{Hom}_k(H^n(X),H^{n+1}(Y)).
\]
If \(f:X_0\to X_1\) and \(g:Y_0\to Y_1\), the induced map sends a family \((u_n)\) to
\[
\bigl(H^{n+1}(g)\,u_n\,H^n(f)\bigr)_n.
\]
It follows immediately that
\[
\operatorname{Ext}^1(\mathcal I_B,\mathcal J_B)=0.
\]

The reverse orthogonality can be tested by stalks. If \(B=d\mathbb Z\) with \(d\geq1\), use \(S^r(k^d)\), whose Euler characteristic lies in \(B\). If \(B=\{0\}\), use
\[
S^r(k)\oplus S^{r+1}(k),
\]
whose Euler characteristic is zero. These test objects detect every nonzero cohomology map in the same degree-by-degree Ext formula. Hence
\[
{}^\perp\mathcal J_B=\mathcal I_B,\qquad
\mathcal I_B^\perp=\mathcal J_B.
\]

It remains to see that these are object ideals. Suppose \(f\in\mathcal I_B\). Write
\[
X\cong L\oplus U\oplus Q_X,\qquad
L=H^{\leq0}(X),\quad U=H^{\geq1}(X),
\]
and separate \(f\) into the part supported on \(L\) plus a null-homotopic map. The null-homotopic part factors through a contractible object of \(\mathcal F_B\).

For the \(L\)-part, if \(B=d\mathbb Z\) with \(d\geq1\), factor through \(L^{\oplus d}\in\mathcal F_B\). If \(B=\{0\}\), factor through
\[
L\oplus L[1]\in\mathcal F_B,
\]
whose Euler characteristic is zero. Thus \(\mathcal I_B=\langle\mathcal F_B\rangle\). The dual argument, using \(W^{\oplus d}\) or \(W\oplus W[-1]\) for \(W=H^{\geq2}\), gives
\[
\mathcal J_B=\langle\mathcal C_B\rangle.
\]
Therefore \((\mathcal F_B,\mathcal C_B)\) is a cotorsion pair of objects.

### 3. Completeness of the ideal pair

Let
\[
A\cong L\oplus U\oplus Q,\qquad
L=H^{\leq0}(A),\quad U=H^{\geq1}(A),
\]
with \(Q\) contractible.

If \(B=d\mathbb Z\) with \(d\geq1\), set
\[
C_A=U[-1]^{\oplus d},
\]
\[
E_A=L\oplus P(U)\oplus U[-1]^{\oplus(d-1)}\oplus Q.
\]
Using the standard deflation \(P(U)\to U\), there is a conflation
\[
0\to C_A\to E_A\xrightarrow{p_A}A\to0.
\]
Here \(C_A\in\mathcal C_B\), \(p_A\in\mathcal I_B\), and
\[
\chi(E_A)
=\chi(L)-(d-1)\chi(U)
=\chi(A)-d\chi(U)\in d\mathbb Z.
\]
Hence this is a special \(\mathcal I_B\)-precover.

For \(B=\{0\}\), use instead
\[
C_A=U[-1]\oplus U[-2],\qquad
E_A=L\oplus P(U)\oplus U[-2]\oplus Q.
\]
Then \(\chi(C_A)=0\) and \(\chi(E_A)=\chi(A)=0\), while the same map \(p_A\) lies in \(\mathcal I_B\) and has kernel in \(\mathcal C_B\).

Dually, write
\[
A\cong V\oplus W\oplus Q,\qquad
V=H^{\leq1}(A),\quad W=H^{\geq2}(A).
\]
For \(B=d\mathbb Z\), \(d\geq1\), set
\[
D_A=K(V)\oplus W\oplus V[1]^{\oplus(d-1)}\oplus Q.
\]
The standard inflation \(V\to K(V)\) gives
\[
0\to A\xrightarrow{j_A}D_A\to V[1]^{\oplus d}\to0,
\]
with \(j_A\in\mathcal J_B\) and cokernel in \(\mathcal F_B\). For \(B=\{0\}\), replace these by
\[
D_A=K(V)\oplus W\oplus V[2]\oplus Q,\qquad
\operatorname{coker}(j_A)=V[1]\oplus V[2].
\]
Again both middle term and cokernel have Euler characteristic zero. Thus every object has special ideal approximations on both sides, so \((\mathcal I_B,\mathcal J_B)\) is complete.

### 4. Exact criterion for object approximations

Suppose
\[
0\to C\to F\to A\to0,
\qquad
C\in\mathcal C_B,\quad F\in\mathcal F_B.
\]
The long exact cohomology sequence gives
\[
H(F)\cong H^{\leq0}(A).
\]
Therefore such a conflation can exist only if
\[
\chi(H^{\leq0}(A))\in B.
\]

Conversely, if this Euler characteristic lies in \(B\), then
\[
\chi(H^{\geq1}(A))
=
\chi(A)-\chi(H^{\leq0}(A))
\in B.
\]
The undoubled cone sequence
\[
0\to H^{\geq1}(A)[-1]\to
H^{\leq0}(A)\oplus P(H^{\geq1}(A))\oplus Q
\to A\to0
\]
is then a special \(\mathcal F_B\)-object precover.

The dual argument gives the exact preenvelope criterion
\[
\chi(H^{\geq2}(A))\in B.
\]

If \(B=\mathbb Z\), both criteria always hold. If \(B\neq\mathbb Z\), then \(1\notin B\). The complexes
\[
M=S^0(k)\oplus S^1(k),\qquad
N=S^1(k)\oplus S^2(k)
\]
belong to \(\mathcal A_B\) because both have Euler characteristic zero, but
\[
\chi(H^{\leq0}(M))=1,\qquad
\chi(H^{\geq2}(N))=1.
\]
Hence the object pair is neither special precovering nor special preenveloping.

### 5. Idempotent completion

For \(B=d\mathbb Z\), \(d\geq2\), every \(X\in\mathcal D\) is a direct summand of
\[
X^{\oplus d}\in\mathcal A_B.
\]
For \(B=\{0\}\), every \(X\) is a direct summand of
\[
X\oplus X[1]\in\mathcal A_B.
\]
Thus the idempotent completion of every proper \(\mathcal A_B\) is \(\mathcal D\). This also explains why the object-level obstruction disappears after idempotent completion.

## Relation to the literature

Ren and Wang, *A parity obstruction to completeness of object cotorsion pairs*, arXiv:2609.18681v1 (16 September 2026), construct the case \(B=2\mathbb Z\). Their category is stated using even total cohomology dimension; parity makes this equivalent to even Euler characteristic. Their exact object-specialness criterion is correspondingly a parity criterion, and they show that idempotent completion removes the obstruction.

The present result identifies the underlying mechanism as the additive subgroup of the Euler-characteristic group and gives a sharp classification over all \(B\leq\mathbb Z\). For moduli \(d>2\), divisibility of total cohomology dimension is not extension-additive, so Euler characteristic is the essential replacement. The case \(B=\{0\}\) is qualitatively distinct from a congruence modulo a positive integer and is covered by the same theorem.

The original completeness-descent question is due to Fu, Guil Asensio, Herzog and Torrecillas, *Ideal approximation theory*, Adv. Math. 244 (2013), 750–790, DOI: 10.1016/j.aim.2013.05.020. Wang, Wang and Zhu, arXiv:2609.14382v1, give a different counterexample in a category that is not weakly idempotent complete.

## Limitations

Originality is asserted only to the best of our knowledge. The \(B=2\mathbb Z\) specialization, the degreewise-split Ext computation, and the underlying ideal-approximation criterion are prior work from arXiv:2609.18681v1 and the earlier ideal approximation literature. The new claim is the Euler-subgroup family, the exact object-completeness boundary \(B=\mathbb Z\), the zero-Euler case, and the uniform specialness criteria above.

The construction is specific to bounded complexes of finite-dimensional vector spaces with the degreewise split exact structure. No claim is made that every failure of completeness descent in a Frobenius exact category arises from an Euler or Grothendieck-group obstruction.
