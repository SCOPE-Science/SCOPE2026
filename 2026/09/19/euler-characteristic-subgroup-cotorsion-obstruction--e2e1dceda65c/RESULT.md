# Every proper Euler-characteristic subgroup obstructs object cotorsion completeness

## Statement

Let \(k\) be a field and
\[
\mathcal D=\operatorname{Ch}^{b}(\operatorname{vect}_k)
\]
with the degreewise split exact structure. For \(X\in\mathcal D\), write
\[
\chi(X)=\sum_n(-1)^n\dim_k H^n(X).
\]
Fix an additive subgroup \(B\le \mathbb Z\), and let
\[
\mathcal A_B=\{X\in\mathcal D:\chi(X)\in B\}.
\]
Inside \(\mathcal A_B\), define
\[
\mathcal F_B=\{X:H^n(X)=0\text{ for }n\ge1\},\qquad
\mathcal C_B=\{X:H^n(X)=0\text{ for }n\le1\},
\]
and ideals
\[
\mathcal I_B=\{f:H^n(f)=0\text{ for }n\ge1\},\qquad
\mathcal J_B=\{g:H^n(g)=0\text{ for }n\le1\}.
\]

Then:

1. \(\mathcal A_B\) is an essentially small, Hom-finite, weakly idempotent complete Frobenius exact category. Its projective-injective objects are exactly the contractible complexes.

2. The ideals are object ideals,
\[
\mathcal I_B=\langle\mathcal F_B\rangle,\qquad
\mathcal J_B=\langle\mathcal C_B\rangle,
\]
and
\[
{}^\perp\mathcal J_B=\mathcal I_B,\qquad
\mathcal I_B^\perp=\mathcal J_B.
\]
Moreover, \((\mathcal I_B,\mathcal J_B)\) is a complete ideal cotorsion pair.

3. For \(A\in\mathcal A_B\), an object-special sequence
\[
0\longrightarrow C\longrightarrow F\longrightarrow A\longrightarrow0,
\qquad C\in\mathcal C_B,\ F\in\mathcal F_B,
\]
exists if and only if
\[
\boxed{\chi(H^{\le0}(A))\in B.}
\]
Dually, a sequence
\[
0\longrightarrow A\longrightarrow C\longrightarrow F\longrightarrow0,
\qquad C\in\mathcal C_B,\ F\in\mathcal F_B,
\]
exists if and only if
\[
\boxed{\chi(H^{\ge2}(A))\in B.}
\]

4. Consequently, the associated object cotorsion pair \((\mathcal F_B,\mathcal C_B)\) is complete if and only if
\[
\boxed{B=\mathbb Z.}
\]
For every proper subgroup \(B<\mathbb Z\), it is neither special precovering nor special preenveloping, although the ideal cotorsion pair is complete.

5. If \(B<\mathbb Z\), then \(\mathcal A_B\) is not idempotent complete, but its idempotent completion is \(\mathcal D\).

The parity example of Ren--Wang, arXiv:2609.18681v1, is exactly the special case \(B=2\mathbb Z\): modulo \(2\), total cohomology dimension and Euler characteristic agree. Thus the obstruction is not intrinsically a parity phenomenon. Every proper subgroup of the Euler-characteristic group produces the same ideal/object completeness gap. Finite-index subgroups \(m\mathbb Z\) give congruence obstructions for every \(m\ge2\), while \(B=\{0\}\) gives an exact-zero Euler-characteristic obstruction.

## Proof

### 1. The Frobenius categories \(\mathcal A_B\)

Euler characteristic is additive on short exact sequences of bounded complexes. Hence \(\mathcal A_B\) is additive and extension closed in \(\mathcal D\). The induced exact structure is therefore well defined. Hom-finiteness and essential smallness are inherited from \(\mathcal D\).

If \(X\to Y\) is a split monomorphism in \(\mathcal A_B\), with ambient cokernel \(Z\), then
\[
\chi(Z)=\chi(Y)-\chi(X)\in B,
\]
so \(Z\in\mathcal A_B\). Thus \(\mathcal A_B\) is weakly idempotent complete.

Every contractible bounded complex has Euler characteristic \(0\), hence belongs to every \(\mathcal A_B\). The standard contractible cone sequences
\[
0\to X\to K(X)\to X[1]\to0,
\qquad
0\to X[-1]\to P(X)\to X\to0
\]
stay inside \(\mathcal A_B\), since \(B\) is closed under negation. Therefore \(\mathcal A_B\) has enough injectives and projectives. As in the ambient degreewise split exact category, the contractible complexes are projective and injective; conversely, a projective or injective object is a retract of one of these contractible cones and is itself contractible. Hence \(\mathcal A_B\) is Frobenius.

For a proper subgroup \(B\), one has \(1\notin B\). The object
\[
M=S^0(k)\oplus S^1(k)
\]
has Euler characteristic \(0\), so \(M\in\mathcal A_B\). Projection onto \(S^0(k)\) is an idempotent of \(M\), but its image has Euler characteristic \(1\notin B\), so this idempotent cannot split in \(\mathcal A_B\). Thus \(\mathcal A_B\) is not idempotent complete.

Conversely, every \(X\in\mathcal D\) is a direct summand of an object of Euler characteristic zero: choose a bounded zero-differential complex \(R\) with \(\chi(R)=-\chi(X)\), so \(X\oplus R\in\mathcal A_B\). Hence the Karoubi envelope of every proper \(\mathcal A_B\) is all of \(\mathcal D\).

### 2. Correction stalks

For \(r\in\mathbb Z\), define zero-differential complexes
\[
R_-(r)=
\begin{cases}
S^0(k^r),&r\ge0,\\
S^{-1}(k^{-r}),&r<0,
\end{cases}
\qquad
R_+(r)=
\begin{cases}
S^2(k^r),&r\ge0,\\
S^3(k^{-r}),&r<0.
\end{cases}
\]
Then
\[
\chi(R_-(r))=\chi(R_+(r))=r,
\]
while \(R_-(r)\) is supported in degrees \(\le0\) and \(R_+(r)\) in degrees \(\ge2\).

These correction stalks remove the dependence on the index of \(B\): any cohomological piece can be enlarged, without changing the relevant support condition, to an object of Euler characteristic \(0\), which belongs to every \(\mathcal A_B\).

### 3. The ideals are object ideals

Let \(f:X\to Y\) lie in \(\mathcal I_B\). Split \(X\) in the ambient complex category as
\[
X\cong L\oplus U\oplus Q,
\qquad
L=H^{\le0}(X),\quad U=H^{\ge1}(X),
\]
with \(Q\) contractible. Put \(f_0=f\iota_L\pi_L\). The maps \(f\) and \(f_0\) induce the same cohomology maps, so \(f-f_0\) is null-homotopic and factors through a contractible complex.

The map \(f_0\) factors through
\[
L\oplus R_-(-\chi(L)),
\]
which has Euler characteristic \(0\) and cohomology only in degrees \(\le0\). Therefore it lies in \(\mathcal F_B\). Adding the contractible factorization gives a factorization of \(f\) through an object of \(\mathcal F_B\). Thus
\[
\mathcal I_B=\langle\mathcal F_B\rangle.
\]
The same argument using \(H^{\ge2}\) and \(R_+\) gives
\[
\mathcal J_B=\langle\mathcal C_B\rangle.
\]

### 4. Ideal cotorsion

Because \(\mathcal A_B\) is full and extension closed in \(\mathcal D\), the standard degreewise-split extension calculation gives
\[
\operatorname{Ext}^1_{\mathcal A_B}(X,Y)
\cong
\bigoplus_n
\operatorname{Hom}_k(H^n(X),H^{n+1}(Y)).
\]
Under this identification, for \(f:X_0\to X_1\) and \(g:Y_0\to Y_1\), the induced map sends a family \((u_n)\) to
\[
\bigl(H^{n+1}(g)\,u_n\,H^n(f)\bigr)_n.
\]
It follows immediately that
\[
\operatorname{Ext}^1(\mathcal I_B,\mathcal J_B)=0.
\]

For the reverse inclusion, suppose \(f\notin\mathcal I_B\). Then \(H^n(f)\ne0\) for some \(n\ge1\). The test object
\[
T_n^+=S^{n+1}(k)\oplus S^{n+2}(k)
\]
has Euler characteristic \(0\), belongs to \(\mathcal C_B\), and has a nonzero \(H^{n+1}\). Choosing a linear functional nonzero on the image of \(H^n(f)\) yields an extension class on which
\[
\operatorname{Ext}^1(f,1_{T_n^+})
\]
is nonzero. Hence \(f\notin{}^\perp\mathcal J_B\).

Dually, if \(g\notin\mathcal J_B\), take \(m\le1\) with \(H^m(g)\ne0\) and use
\[
T_m^-=S^{m-1}(k)\oplus S^{m-2}(k)\in\mathcal F_B,
\]
again of Euler characteristic \(0\), to obtain
\[
\operatorname{Ext}^1(1_{T_m^-},g)\ne0.
\]
Therefore
\[
{}^\perp\mathcal J_B=\mathcal I_B,\qquad
\mathcal I_B^\perp=\mathcal J_B.
\]

### 5. Uniform special ideal approximations

Let \(A\in\mathcal A_B\) and write
\[
A\cong L\oplus U\oplus Q,
\qquad
L=H^{\le0}(A),\quad U=H^{\ge1}(A),
\]
with \(Q\) contractible. Put
\[
Z_U=R_+(\chi(U))
\]
and
\[
E_A=L\oplus P(U)\oplus Z_U\oplus Q.
\]
Define
\[
p_A:E_A\to A,\qquad
p_A(l,z,c,q)=(l,q_U(z),q),
\]
with \(Z_U\) sent to zero. Its kernel is
\[
C_A=U[-1]\oplus Z_U.
\]
Since \(\chi(U[-1])=-\chi(U)\),
\[
\chi(C_A)=0,
\]
and \(C_A\) is supported in degrees \(\ge2\), so \(C_A\in\mathcal C_B\). Also
\[
\chi(E_A)=\chi(A)\in B.
\]
The map \(p_A\) induces zero in every degree \(n\ge1\), hence \(p_A\in\mathcal I_B\). Therefore
\[
0\to C_A\to E_A\xrightarrow{p_A}A\to0
\]
is a special \(\mathcal I_B\)-precover sequence.

Dually, write
\[
A\cong V\oplus W\oplus Q,
\qquad
V=H^{\le1}(A),\quad W=H^{\ge2}(A),
\]
put
\[
Z_V=R_-(\chi(V)),
\qquad
D_A=K(V)\oplus W\oplus Z_V\oplus Q,
\]
and map
\[
j_A:A\to D_A,\qquad
j_A(v,w,q)=(\iota_V(v),w,0,q).
\]
Its cokernel is
\[
F_A=V[1]\oplus Z_V,
\]
which has Euler characteristic \(0\) and support in degrees \(\le0\), hence lies in \(\mathcal F_B\). Moreover \(j_A\in\mathcal J_B\). This is a special \(\mathcal J_B\)-preenvelope. Thus the ideal cotorsion pair is complete for every subgroup \(B\le\mathbb Z\).

### 6. Exact criterion for object completeness

Suppose
\[
0\to C\to F\to A\to0
\]
with \(C\in\mathcal C_B\) and \(F\in\mathcal F_B\). The long exact cohomology sequence gives
\[
H(F)\cong H^{\le0}(A).
\]
Since \(F\in\mathcal A_B\),
\[
\chi(H^{\le0}(A))=\chi(F)\in B.
\]
This proves necessity.

Conversely, if \(\chi(H^{\le0}(A))\in B\), write \(A\cong L\oplus U\oplus Q\) as above. Since \(\chi(A)\in B\), also \(\chi(U)\in B\). The ordinary cone sequence
\[
0\to U[-1]\to L\oplus P(U)\oplus Q\to A\to0
\]
then lies entirely in \(\mathcal A_B\), with kernel in \(\mathcal C_B\) and middle term in \(\mathcal F_B\). This proves the first criterion. The dual cone sequence proves the second criterion with \(H^{\ge2}(A)\).

If \(B<\mathbb Z\), then \(1\notin B\). The two objects
\[
M=S^0(k)\oplus S^1(k),\qquad
N=S^1(k)\oplus S^2(k)
\]
both have Euler characteristic \(0\), hence belong to \(\mathcal A_B\). But
\[
\chi(H^{\le0}(M))=1,\qquad
\chi(H^{\ge2}(N))=1.
\]
Therefore \(M\) has no special \(\mathcal F_B\)-object precover and \(N\) has no special \(\mathcal C_B\)-object preenvelope. If \(B=\mathbb Z\), the two criteria are automatic for every object, so the object cotorsion pair is complete. This proves the sharp dichotomy.

## Relation to recent literature

Ren and Wang construct the case of bounded complexes with even total cohomology dimension and show that the associated object cotorsion pair fails to be complete even though the ideal pair is complete. Their proof exploits parity and explicit doubled objects. Since
\[
\sum_n\dim H^n(X)\equiv \chi(X)\pmod2,
\]
their category is exactly \(\mathcal A_{2\mathbb Z}\).

The subgroup theorem above shows that the mechanism is more general. Parity is the first nontrivial subgroup of the Euler-characteristic group, not an isolated phenomenon. For \(m>2\), divisibility of the *total* cohomology dimension is not the right replacement, because total dimension is not exact-additive modulo \(m\); Euler characteristic is. The correction-stalk construction also treats the infinite-index subgroup \(B=\{0\}\), which is not obtained by merely replacing a double with a fixed finite multiple.

Wang, Wang and Zhu's earlier counterexample uses a half-space cut out by an exact-additive integer-valued function and is intrinsically not weakly idempotent complete. It does not give the subgroup family above or the Frobenius/weakly-idempotent-complete phenomenon.

## Originality and limitations

To the best of our knowledge, the exact subgroup-parametrized theorem, the criterion
\[
\chi(H^{\le0}(A))\in B,\qquad \chi(H^{\ge2}(A))\in B,
\]
for every \(B\le\mathbb Z\), and the dichotomy “object completeness iff \(B=\mathbb Z\)” have not previously been stated.

The recent Ren--Wang preprint was inspected in full in the portions defining the category, the object ideals, the special ideal approximations, and the parity obstruction. It states only the even/parity case. Targeted searches for Euler-characteristic congruence or subgroup versions of ideal/object cotorsion completeness did not locate an equivalent statement. General ideal-approximation and Frobenius-category theory is prior art and is not claimed as new.

The main residual originality risk is that this natural extension may be implicit in older exact-category literature under a more abstract \(K_0\)-theoretic formulation. No concrete theorem implying the result was located. No independent validation or formal verification is asserted.

## References

1. J. Ren and Y. Wang, *A parity obstruction to completeness of object cotorsion pairs*, arXiv:2609.18681v1 (2026). https://arxiv.org/abs/2609.18681v1
2. Q. Wang, Y. Wang and H. Zhu, *A Counterexample to the Open Question on Object Ideals*, arXiv:2609.14382v1 (2026). https://arxiv.org/abs/2609.14382v1
3. X. H. Fu, P. A. Guil Asensio, I. Herzog and B. Torrecillas, *Ideal approximation theory*, Advances in Mathematics 244 (2013), 750--790. https://doi.org/10.1016/j.aim.2013.05.020
