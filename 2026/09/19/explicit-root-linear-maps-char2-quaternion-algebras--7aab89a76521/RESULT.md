# Explicit root-linear maps for characteristic-two quaternion division algebras

## Statement

Let `F` be a field of characteristic `2` with finite 2-rank

\[
[F:F^2]=2^r<\infty,
\]

and let

\[
Q=[a,b)_F
\]

be a quaternion **division** algebra with its standard involution. Put
\(K=F(i)\), where \(i^2+i=a\), and write

\[
Q=K\oplus Kj,\qquad j^2=b,\qquad jc=\sigma(c)j\quad(c\in K),
\]

where \(\sigma\) is the nontrivial `F`-automorphism of `K/F`. The standard involution is

\[
\overline{c+dj}=\sigma(c)+dj.
\]

Let

\[
H=\{x\in Q:\bar x=x\},\qquad A=\{\bar x-x:x\in Q\}.
\]

A map \(\alpha:H\to Q\) is called **root-linear** when it is additive and

\[
\alpha(xh\bar x)=x\alpha(h)\qquad(x\in Q,\ h\in H).
\]

Then the following hold.

1. \(H=F\oplus Kj\) and \(A=F\).
2. Since `Q` is division, \(b\notin F^2\). Choose \(c_2,\dots,c_r\in F\) so that
   \(\{b,c_2,\dots,c_r\}\) is a 2-basis of `F`, i.e. the monomials
   \(b^{\varepsilon_1}c_2^{\varepsilon_2}\cdots c_r^{\varepsilon_r}\), with each \(\varepsilon_i\in\{0,1\}\), form an \(F^2\)-basis of `F`.
3. For \(S\subseteq\{2,\dots,r\}\), write \(m_S=\prod_{s\in S}c_s\), with \(m_\varnothing=1\). Then

   \[
   \boxed{\{[m_Sj]:S\subseteq\{2,\dots,r\}\}}
   \]

   is a left-`Q` basis of the quotient `H/A` for the scalar action

   \[
   x.[h]=[xh\bar x].
   \]

   In particular,

   \[
   \boxed{\dim_Q(H/A)=2^{r-1}.}
   \]
4. Every \(z\in K\) has a unique expansion

   \[
   z=\sum_{S\subseteq\{2,\dots,r\}}(u_S^2+bv_S^2)m_S,
   \qquad u_S,v_S\in K.
   \]

   Define

   \[
   \boxed{\alpha_S(f+zj)=u_S+v_Sj\qquad(f\in F).}
   \]

   Each \(\alpha_S\) is root-linear, and the family \((\alpha_S)_S\) is a right-`Q` basis of the space of all root-linear maps `H -> Q`. Thus every root-linear map has a unique form

   \[
   \alpha=\sum_S \alpha_S q_S,
   \qquad q_S\in Q.
   \]

This replaces the abstract choice-of-basis existence argument for this finite-2-rank quaternion case by finite coordinates.

## Proof

### 1. Hermitian and alternate elements

For \(c,d\in K\),

\[
\overline{c+dj}=\sigma(c)+dj.
\]

Hence \(c+dj\) is Hermitian exactly when \(c\in F\), giving

\[
H=F\oplus Kj.
\]

Also

\[
\overline{c+dj}-(c+dj)=\sigma(c)+c=\operatorname{Tr}_{K/F}(c).
\]

The Artin--Schreier generator satisfies \(\operatorname{Tr}_{K/F}(i)=1\), so the trace map is onto `F`. Therefore \(A=F\).

### 2. The quotient action in coordinates

Identify \(H/A\) additively with `K` through

\[
[f+zj]\longmapsto z.
\]

For \(\lambda=c+dj\in Q\), direct multiplication gives

\[
\lambda(zj)\bar\lambda
=
 b\bigl(cz\sigma(d)+d\sigma(z)\sigma(c)\bigr)
 +\bigl(c^2z+bd^2\sigma(z)\bigr)j.
\]

The first term lies in `F`: if \(T=cz\sigma(d)\), then the expression in parentheses is \(T+\sigma(T)\). It therefore vanishes in `H/A`. Consequently the induced left-`Q` action on `K` is

\[
\boxed{(c+dj)\cdot z=c^2z+bd^2\sigma(z).}\tag{1}
\]

A useful subtlety is that a central scalar \(t\in F\) acts on this quotient as multiplication by \(t^2\), not by the ordinary `F`-scalar action. Thus the left-`Q` dimension of `H/A` is not constrained by its ordinary `F`-dimension in the naive way.

### 3. A finite 2-basis gives a `Q`-basis

First, \(b\notin F^2\). Otherwise \(b=s^2\) for some \(s\in F^\times\), and \(u=s^{-1}j\) would satisfy \(u^2=1\). Since \(u\ne1\), the nonzero element \(u+1\) would have square zero, impossible in a division ring.

Hence `b` can be extended to a finite 2-basis \(\{b,c_2,\dots,c_r\}\) of `F`.

Let \(K^2=\{x^2:x\in K\}\). Since `K/F` is separable quadratic while `F/F^2` is purely inseparable, `F` and `K^2` are linearly disjoint over `F^2`. Moreover \(i=i^2+a\), so \(FK^2=K\). It follows that any \(F^2\)-basis of `F` is also a \(K^2\)-basis of `K`. Therefore

\[
\{m_S,\ bm_S:S\subseteq\{2,\dots,r\}\}
\]

is a \(K^2\)-basis of `K`.

For \(m_S\in F\), formula (1) simplifies to

\[
(c+dj)\cdot m_S=(c^2+bd^2)m_S.
\]

As `c` and `d` range over `K`, their squares range over `K^2`. Hence the `Q`-span of \(m_S\) is exactly

\[
K^2m_S\oplus bK^2m_S.
\]

The displayed \(K^2\)-basis decomposes `K` as the direct sum of these subspaces. Therefore the classes \([m_Sj]\) form a left-`Q` basis of `H/A`, proving the dimension formula.

### 4. Coordinate projections are exactly the root-linear maps

The preceding basis decomposition gives every \(z\in K\) uniquely as

\[
z=\sum_S(x_S+by_S)m_S,
\qquad x_S,y_S\in K^2.
\]

Frobenius \(K\to K^2\), \(u\mapsto u^2\), is an additive field isomorphism onto `K^2`; hence uniquely \(x_S=u_S^2\) and \(y_S=v_S^2\). The left-`Q` coordinate of \([f+zj]\) on the basis vector \([m_Sj]\) is precisely \(u_S+v_Sj\). Thus \(\alpha_S\) is the composition

\[
H\longrightarrow H/A\longrightarrow Q
\]

with a left-`Q` coordinate projection. It is additive and satisfies

\[
\alpha_S(xh\bar x)=x\alpha_S(h),
\]

so it is root-linear. Conversely, every root-linear map vanishes on `A` and therefore induces a left-`Q` linear map `H/A -> Q`; its values on the displayed basis determine it uniquely. This proves the right-`Q` basis assertion.

## Explicit imperfection-degree-one case

When \([F:F^2]=2\), the division hypothesis forces \(F=F^2\oplus bF^2\), and the above theorem reduces to a single explicit map. Every \(z\in K\) has a unique decomposition

\[
z=u^2+bv^2,
\]

and

\[
\boxed{\alpha(f+zj)=u+vj}
\]

is a nonzero root-linear map. Every root-linear map `H -> Q` is uniquely \(\alpha q\) for some \(q\in Q\).

A concrete example is

\[
F=\mathbb F_2((t)),\qquad K=\mathbb F_4((t)),\qquad Q=[1,t)_F.
\]

Here `K/F` is the unramified quadratic extension, and the cyclic quaternion algebra with parameter `t` is division because norms from `K` have even `t`-adic valuation whereas `t` has odd valuation. Also

\[
F=F^2\oplus tF^2.
\]

Thus every Laurent series \(z\in K\) splits uniquely into its even and odd powers as

\[
z=u^2+tv^2,
\]

and \(\alpha(f+zj)=u+vj\) is completely explicit.

## Consequence for range-compatible Hermitian-matrix homomorphisms

The source classification proves that, in characteristic `2` with a first-kind involution, every range-compatible group homomorphism

\[
\Phi:\operatorname{Herm}_n(Q)\to Q^n,\qquad n\ge2,
\]

has a unique decomposition

\[
\Phi(M)=MX+\Delta(M)^\alpha,
\]

where \(X\in Q^n\) and \(\alpha:H\to Q\) is root-linear. Combining that theorem with the explicit basis above gives the finite-coordinate normal form

\[
\boxed{
\Phi(M)=MX+\sum_{S\subseteq\{2,\dots,r\}}\Delta(M)^{\alpha_S}q_S,
}
\]

with uniquely determined \(X\in Q^n\) and \(q_S\in Q\). Thus, for finite 2-rank quaternion centers, the nonlocal part of every such range-compatible homomorphism is explicit.

## Relation to prior literature

The recent paper that introduces the noncommutative root-linear formulation proves that, in characteristic `2`, root-linear maps on `H` correspond to left-`D` linear maps `H/A -> D`. For quaternion division rings with the standard involution it identifies `A=F` and `H` with the reduced-trace kernel, and explicitly leaves the construction of a nonzero root-linear map nonconstructive. The theorem above computes the quotient module and its dual in coordinates when the center has finite 2-rank.

The characteristic-2 quaternion presentation, standard involution, and cyclic-algebra description used here are classical. They are not originality claims.

## Limitations

The finite-dimensional coordinate theorem assumes \([F:F^2]<\infty\). If an explicit possibly infinite 2-basis of `F` containing `b` is already given, the same argument yields a `Q`-basis indexed by finite subsets of the remaining 2-basis elements; obtaining such a basis for a completely arbitrary field may itself require choice. No claim is made that the displayed basis is canonical: it depends on the chosen quaternion presentation and 2-basis.

Originality is asserted only to the best of our knowledge. Older literature on quaternion algebras, involutions, `p`-bases, or Hermitian forms could contain the underlying semilinear module decomposition in different terminology. The specific root-linear coordinate basis and its use to make the recent range-compatible classification constructive were not located in the sources checked.

## References

1. C. de Seguins Pazzis, *Range-compatible homomorphisms on Hermitian matrices*, arXiv:2609.20363v1 (2026): https://arxiv.org/abs/2609.20363v1
2. J. Voight, *Quaternion Algebras*, Chapter 6, “Characteristic 2”, Graduate Texts in Mathematics 288, Springer (open access): https://link.springer.com/chapter/10.1007/978-3-030-56694-4_6
