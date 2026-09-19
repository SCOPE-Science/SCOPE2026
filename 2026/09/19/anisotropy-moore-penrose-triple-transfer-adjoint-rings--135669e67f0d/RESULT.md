# Anisotropy controls Moore–Penrose triple transfer in adjoint matrix rings

## Result

Let \(D\) be a division ring with involution, let \(V\) be a finite-dimensional right
\(D\)-vector space, and let \(h\) be a nondegenerate Hermitian or skew-Hermitian form
whose adjoint involution on
\[
R=\operatorname{End}_D(V)
\]
is denoted by \(*\). Write \(R^\dagger\) for the Moore–Penrose invertible elements.

Consider the two conditions
\[
\tag{Z}
abc=0\quad\Longrightarrow\quad acb\in R^\dagger
\]
and
\[
\tag{MP}
abc\in R^\dagger\quad\Longrightarrow\quad acb\in R^\dagger
\]
for all \(a,b,c\in R\).

Then
\[
\boxed{
\text{\rm (Z)}
\iff
\text{\rm (MP)}
\iff
h\text{ is anisotropic}
\iff
R\text{ is }*\text{-regular}.
}
\]

Thus Question 4.3 of Chen--Wang--Zou, arXiv:2609.20084v1, has an affirmative
answer throughout this natural class of simple Artinian \(*\)-rings: in an adjoint
endomorphism ring, their Condition (3) implies Condition (4), and both conditions
hold exactly on the anisotropic side.

For the ordinary transpose involution on \(M_n(F)\), this specializes to
\[
\boxed{
\text{\rm (Z)}\iff\text{\rm (MP)}
\iff
x_1^2+\cdots+x_n^2
\text{ is anisotropic over }F.
}
\]

Consequently, for a finite field \(\mathbb F_q\),
\[
\boxed{
M_n(\mathbb F_q)\text{ satisfies (Z) and (MP)}
\iff
n=1,\ \text{or }n=2\text{ and }q\equiv3\pmod4.
}
\]
In every other case with \(n\ge2\), both conditions fail.

## Context

Chen, Wang and Zou introduce four transposed-triple conditions for \(*\)-rings.
Their Condition (3) is (Z), and their Condition (4) is (MP). They prove
\[
(1)\Longrightarrow(4)\Longrightarrow(3)
\]
and ask explicitly whether Condition (3) implies Condition (4)
(Question 4.3). Their Example 4.2 notes that \(M_2(\mathbb C)\) with conjugate
transpose satisfies both conditions because it is \(*\)-regular, even though it is
not symmetric.

The result above identifies the precise mechanism behind that example for all
finite-dimensional adjoint endomorphism rings: anisotropy of the underlying form.

## Proof

### 1. Anisotropy makes every endomorphism Moore–Penrose invertible

Assume that \(h\) is anisotropic. Every subspace \(W\le V\) is then nondegenerate:
if \(0\ne w\in W\cap W^\perp\), then \(h(w,w)=0\), contradicting anisotropy.
Hence
\[
V=W\oplus W^\perp
\]
for every \(W\).

Let \(T\in R\). Put \(K=\ker T\) and \(I=\operatorname{im}T\). Both are
nondegenerate, so
\[
V=K\oplus K^\perp=I\oplus I^\perp.
\]
The restriction
\[
T|_{K^\perp}:K^\perp\longrightarrow I
\]
is an isomorphism. Define \(S\in R\) to be its inverse on \(I\) and zero on
\(I^\perp\). Then \(TS\) is the orthogonal projection onto \(I\), while \(ST\)
is the orthogonal projection onto \(K^\perp\). Therefore
\[
TST=T,\qquad STS=S,\qquad (TS)^*=TS,\qquad(ST)^*=ST.
\]
Thus \(S=T^\dagger\). Hence \(R^\dagger=R\), so (MP), and therefore (Z), hold
trivially.

This also gives directly the familiar fact that the adjoint involution is proper
and \(R\) is \(*\)-regular. Indeed, if \(T^*T=0\), then
\[
h(Tv,Tv)=h(v,T^*Tv)=0
\]
for every \(v\), so anisotropy gives \(T=0\).

### 2. An isotropic vector produces a rank-one obstruction to Condition (Z)

Assume now that \(h\) is isotropic. Choose \(0\ne u\in V\) with \(h(u,u)=0\).
Nondegeneracy forces \(\dim_DV\ge2\).

For \(p,q\in V\), write
\[
\theta_{p,q}(v)=p\,h(q,v).
\]
Choose nonzero \(r,x,y,z,w\in V\) such that
\[
h(r,x)=0,\qquad h(r,z)=1,\qquad h(w,x)=1.
\]
Such vectors exist by nondegeneracy: take \(0\ne x\in r^\perp\), then choose
\(z,w\) realizing the two nonzero pairings. Define
\[
A=\theta_{u,r},\qquad B=\theta_{x,y},\qquad C=\theta_{z,w}.
\]
Rank-one composition satisfies
\[
\theta_{p,q}\theta_{r,s}
=
\theta_{p\,h(q,r),\,s}.
\]
Therefore
\[
ABC=0,\qquad
ACB=\theta_{u,y}\ne0.
\]

The operator \(T=\theta_{u,y}\) is not Moore–Penrose invertible. If it had a
Moore–Penrose inverse, then
\[
P=TT^\dagger
\]
would be a self-adjoint idempotent with
\[
\operatorname{im}P=\operatorname{im}T=uD.
\]
The image of a self-adjoint idempotent is a nondegenerate subspace, since its
kernel is its orthogonal complement. But \(uD\) is totally isotropic:
\[
h(ua,ub)=\bar a\,h(u,u)b=0
\]
for all \(a,b\in D\). This contradiction shows \(T\notin R^\dagger\).

Hence (Z) fails whenever \(h\) is isotropic. Since \(0\in R^\dagger\),
(MP) always implies (Z), so (MP) fails as well. This proves all equivalences.

### 3. Transpose involution and finite fields

For \(R=M_n(F)\) with transpose, \(h\) is the standard symmetric form
\[
h(x,y)=x^Ty,
\]
so anisotropy is exactly the absence of a nonzero solution to
\[
x_1^2+\cdots+x_n^2=0.
\]

Over \(\mathbb F_q\):

- \(n=1\): the form is anisotropic.
- \(n=2\), \(q\) odd: \(x^2+y^2=0\) has a nonzero solution exactly when
  \(-1\) is a square, i.e. exactly when \(q\equiv1\pmod4\).
- \(n=2\), \(q\) even: \((1,1)\) is isotropic.
- \(n\ge3\): every quadratic form of degree \(2<n\) over a finite field has a
  nontrivial zero (for example by Chevalley--Warning); hence the standard form
  is isotropic.

This gives the stated finite-field classification.

A concrete failure in \(M_2(\mathbb F_5)\) is
\[
A=\begin{pmatrix}1&0\\2&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
C=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
Then
\[
ABC=0,\qquad ACB=A.
\]
The image of \(A\) is the isotropic line spanned by \((1,2)^T\), since
\(1^2+2^2=0\) in \(\mathbb F_5\), so \(A\) is not Moore–Penrose invertible.

## Relation to prior work

The notions of proper involution and \(*\)-regular ring, and the fact that every
element of a \(*\)-regular ring has a Moore–Penrose inverse, are classical and are
not claimed here. Generalized inverses of matrices over arbitrary fields were
studied by M. H. Pearl (1968), and Moore–Penrose inverses for matrices over
semisimple Artinian rings with involution were studied by Huylebrouck, Puystjens
and Van Geel (1988).

The claimed contribution is the exact equivalence between the two transposed
triple-product conditions of arXiv:2609.20084v1 and anisotropy in adjoint
endomorphism rings, together with the explicit isotropic rank-one obstruction and
the resulting finite-field classification.

## Limitations

This does not resolve Question 4.3 for arbitrary \(*\)-rings. It proves the
implication for endomorphism rings carrying an adjoint involution from a
nondegenerate Hermitian or skew-Hermitian form.

Originality is asserted only to the best of our knowledge. The full text of
Huylebrouck--Puystjens--Van Geel (1988) was not inspected, and the full text of
Pearl (1968) was not independently inspected. Those sources are the principal
residual prior-art risk for equivalent matrix-level formulations. No independent
validation is asserted.

## References

1. H. Chen, L. Wang, H. Zou, *Transposed Triple Products and Pro-Symmetric
   Rings in \(\ast\)-Rings*, arXiv:2609.20084v1 (2026).
   https://arxiv.org/abs/2609.20084v1
2. M. H. Pearl, *Generalized inverses of matrices with entries taken from an
   arbitrary field*, Linear Algebra and its Applications 1 (1968), 571--587.
   https://doi.org/10.1016/0024-3795(68)90028-1
3. D. Huylebrouck, R. Puystjens, J. Van Geel, *The Moore-Penrose inverse of a
   matrix over a semi-simple artinian ring with respect to an involution*,
   Linear and Multilinear Algebra 23 (1988), 269--276.
   https://doi.org/10.1080/03081088808817878
4. A. Vosough, G. H. dos Santos, R. E. Hartwig et al., *Reverse order law for
   outer inverses and Moore-Penrose inverse in the context of star order*,
   F1000Research 11 (2022), Article 843.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC10130701/
