# Single commutators in C*-quotients of finite von Neumann algebras

## Statement

Let \(M\) be a finite complex von Neumann algebra with normalized center-valued trace
\[
T_M:M\longrightarrow Z(M),
\]
let \(J\triangleleft M\) be a norm-closed two-sided ideal, and let
\[
q:M\longrightarrow A:=M/J
\]
be the quotient map.

Jiaqi Wang proved in arXiv:2609.16932v1 that there is an absolute constant \(K\) such that every \(x\in M\) with \(T_M(x)=0\) can be written
\[
x=[b,c]:=bc-cb,\qquad \|b\|\,\|c\|\le K\|x\|.
\]
Combining this new uniform theorem with generalized Dixmier averaging yields the following quotient theorem.

**Theorem.** The center-valued trace descends to a contractive positive tracial idempotent
\[
\overline T:A\longrightarrow Z(A),
\qquad
\overline T(q(x))=q(T_M(x)),
\]
whose range is exactly
\[
Z(A)=q(Z(M)).
\]
Moreover,
\[
\boxed{\{[a,b]:a,b\in A\}=\ker\overline T.}
\]
Consequently, the set of single additive commutators in \(A\) is a norm-closed linear subspace, and for every \(a\in A\),
\[
\boxed{
\operatorname{dist}\!\left(a,\{[b,c]:b,c\in A\}\right)
=
\|\overline T(a)\|.
}
\]

Every bounded tracial linear functional \(\tau\) on \(A\) factors through \(\overline T\):
\[
\tau(a)=\tau(\overline T(a)).
\]
Thus the quotient has no additional bounded tracial obstruction to being a single commutator beyond its central component.

The descended map \(\overline T\) need not be faithful, so it is best viewed as the canonical descended central tracial projection rather than as a faithful center-valued trace on the quotient.

## Proof

### 1. The center-valued trace preserves every closed ideal

The generalized Dixmier averaging theorem says that for each \(x\in M\), \(T_M(x)\) is the norm limit of finite convex combinations of unitary conjugates \(uxu^*\).

If \(x\in J\), then every \(uxu^*\in J\). Since \(J\) is convex and norm closed,
\[
T_M(x)\in J.
\]
Hence
\[
T_M(J)\subseteq J.
\]
Therefore
\[
\overline T(q(x)):=q(T_M(x))
\]
is well defined. Positivity and contractivity follow from those of \(T_M\) and the quotient map, while
\[
\overline T(ab)=\overline T(ba),\qquad
\overline T^2=\overline T.
\]
Its range is initially contained in \(q(Z(M))\).

### 2. Every central quotient element lifts centrally modulo the ideal

Clearly
\[
q(Z(M))\subseteq Z(A).
\]
Conversely, suppose \(q(x)\in Z(A)\). For every unitary \(u\in M\),
\[
q(uxu^*)=q(x),
\]
so
\[
uxu^*-x\in J.
\]
The same holds for every finite convex combination \(y\) of unitary conjugates of \(x\):
\[
y-x\in J.
\]
Choose such convex combinations converging in norm to \(T_M(x)\). Since \(J\) is norm closed,
\[
T_M(x)-x\in J.
\]
Thus
\[
q(x)=q(T_M(x))\in q(Z(M)).
\]
Therefore
\[
\boxed{Z(A)=q(Z(M))=\operatorname{ran}\overline T.}
\]

This is a center-quotient consequence of generalized Dixmier averaging; center lifting itself is not claimed as a new general principle.

### 3. The zero-central-trace layer consists of single commutators

If \(a=[b,c]\in A\), choose lifts \(B,C\in M\). Then
\[
a=q([B,C]),
\]
and traciality of \(T_M\) gives
\[
T_M([B,C])=0.
\]
Hence
\[
\overline T(a)=0.
\]
So every single commutator lies in \(\ker\overline T\).

Conversely, let \(a=q(x)\in\ker\overline T\). Then
\[
q(T_M(x))=0,
\]
so \(T_M(x)\in J\). Put
\[
x_0=x-T_M(x).
\]
We have \(q(x_0)=a\) and \(T_M(x_0)=0\). Wang's theorem gives \(B,C\in M\) such that
\[
x_0=[B,C].
\]
Passing to the quotient,
\[
a=[q(B),q(C)].
\]
Therefore
\[
\boxed{\{[b,c]:b,c\in A\}=\ker\overline T.}
\]

Although the image of the commutator map need not be linear or closed in a general Banach algebra, here it is exactly the kernel of a bounded projection and hence is automatically a closed linear subspace.

### 4. Exact distance to the set of single commutators

Let
\[
\mathcal C_1(A)=\{[b,c]:b,c\in A\}=\ker\overline T.
\]
For \(k\in\mathcal C_1(A)\),
\[
\|\overline T(a)\|
=
\|\overline T(a-k)\|
\le \|a-k\|,
\]
so
\[
\|\overline T(a)\|\le \operatorname{dist}(a,\mathcal C_1(A)).
\]
On the other hand,
\[
a-\overline T(a)\in\ker\overline T=\mathcal C_1(A),
\]
hence
\[
\operatorname{dist}(a,\mathcal C_1(A))
\le \|\overline T(a)\|.
\]
Therefore
\[
\boxed{
\operatorname{dist}(a,\mathcal C_1(A))=\|\overline T(a)\|.
}
\]

### 5. Tracial functionals

If \(\tau:A\to\mathbb C\) is a bounded tracial linear functional, then \(\tau\) vanishes on all commutators. Since
\[
a-\overline T(a)\in\mathcal C_1(A),
\]
we get
\[
\tau(a)=\tau(\overline T(a)).
\]
Thus every bounded trace is determined by its restriction to \(Z(A)\).

## Quantitative commutator cost in arbitrary quotients

Define, for a single commutator \(a\in A\),
\[
\mu_A(a)=
\inf\{\|b\|\,\|c\|:a=[b,c]\}.
\]
For \(a\in\ker\overline T\),
\[
\boxed{\mu_A(a)\le 2K\|a\|.}
\]

Indeed, for \(\varepsilon>0\) choose a lift \(x\in M\) with
\[
\|x\|\le \|a\|+\varepsilon.
\]
Then \(T_M(x)\in J\), so \(x-T_M(x)\) is another lift of \(a\), has center-valued trace zero, and
\[
\|x-T_M(x)\|\le 2\|x\|.
\]
Applying Wang's theorem and then letting \(\varepsilon\downarrow0\) proves the claim.

The factor \(2\) here records the possible norm of \(I-T_M\); no claim of optimality is made.

## Reduced products: the original constant \(K\) is retained

There is a sharper statement for norm reduced products of finite-dimensional C*-algebras.

Let \(I\) be an index set, let \(\mathcal I\) be a proper ideal of subsets of \(I\), and let \(F_i\) be finite-dimensional complex C*-algebras. Define
\[
\mathcal J_{\mathcal I}
=
\left\{(x_i)\in\prod_{i\in I}F_i:
\forall\varepsilon>0,\ 
\{i:\|x_i\|\ge\varepsilon\}\in\mathcal I
\right\},
\]
and
\[
Q_{\mathcal I}
=
\prod_{i\in I}F_i\big/\mathcal J_{\mathcal I}.
\]
Let \(T_i:F_i\to Z(F_i)\) be the normalized center-valued traces. The coordinatewise map descends to
\[
\overline T_{\mathcal I}:Q_{\mathcal I}\to Z(Q_{\mathcal I}).
\]

The preceding theorem gives
\[
\mathcal C_1(Q_{\mathcal I})=\ker\overline T_{\mathcal I}.
\]
In addition,
\[
\boxed{
\mu_{Q_{\mathcal I}}(x)\le K\|x\|
\qquad(x\in\ker\overline T_{\mathcal I}).
}
\]

To see the sharper constant, start with any bounded representative \((x_i)\) of \(x\). Since \(\overline T_{\mathcal I}(x)=0\),
\[
y_i=x_i-T_i(x_i)
\]
represents the same quotient element and satisfies \(T_i(y_i)=0\) coordinatewise.

For this ideal quotient,
\[
\|[(y_i)]\|
=
\inf_{S\in\mathcal I}\sup_{i\notin S}\|y_i\|.
\]
Indeed, truncating on \(S\in\mathcal I\) gives one inequality; conversely, if \(z\in\mathcal J_{\mathcal I}\), then outside
\[
S_\delta=\{i:\|z_i\|\ge\delta\}\in\mathcal I
\]
one has \(\|y_i\|\le\|y-z\|+\delta\), which gives the reverse inequality.

Fix \(\varepsilon>0\) and choose \(S\in\mathcal I\) with
\[
\sup_{i\notin S}\|y_i\|\le \|x\|+\varepsilon.
\]
Set \(y_i'=0\) on \(S\) and \(y_i'=y_i\) elsewhere. Then \((y_i')\) still represents \(x\), is coordinatewise center-trace zero, and
\[
\sup_i\|y_i'\|\le\|x\|+\varepsilon.
\]
Wang's theorem gives
\[
y_i'=[B_i,C_i],
\qquad
\|B_i\|\,\|C_i\|\le K\|y_i'\|.
\]
For each nonzero coordinate rescale the two factors by reciprocal scalar factors so that
\[
\|B_i\|=\|C_i\|
=
\sqrt{\|B_i\|\,\|C_i\|}.
\]
Thus the sequences \(B=(B_i)\) and \(C=(C_i)\) are bounded and
\[
x=[B,C],
\qquad
\|B\|\,\|C\|
\le K(\|x\|+\varepsilon).
\]
Letting \(\varepsilon\downarrow0\) yields the claim.

## Matrix corona

For
\[
Q=\prod_{n\ge1}M_n(\mathbb C)\Big/\bigoplus_{n\ge1}M_n(\mathbb C),
\]
where the denominator is the \(c_0\)-direct sum,
\[
Z(Q)\cong\ell_\infty/c_0,
\]
and
\[
\overline T([(A_n)])
=
[(\operatorname{tr}_n(A_n)I_n)],
\]
where \(\operatorname{tr}_n\) is normalized matrix trace.

Hence
\[
\boxed{
[(A_n)]\text{ is a single commutator}
\iff
\operatorname{tr}_n(A_n)\longrightarrow0.
}
\]
Furthermore,
\[
\boxed{
\operatorname{dist}([(A_n)],\mathcal C_1(Q))
=
\limsup_{n\to\infty}|\operatorname{tr}_n(A_n)|.
}
\]

A striking consequence is that this C*-corona contains a nonzero positive projection that is a single additive commutator. Let \(p_n\in M_n\) be rank one and put
\[
p=[(p_n)]\in Q.
\]
Then \(\|p_n\|=1\), so \(p\neq0\), while
\[
\operatorname{tr}_n(p_n)=\frac1n\to0.
\]
Therefore
\[
\boxed{p=[b,c]\quad\text{for some }b,c\in Q.}
\]
The nonfaithfulness of \(\overline T\) is visible here: \(p\ge0\), \(p\neq0\), but \(\overline T(p)=0\).

## Context and originality boundary

Wang's arXiv:2609.16932v1 establishes the new uniform single-commutator theorem inside finite von Neumann algebras. Generalized Dixmier averaging and center-valued traces are classical, and center-lifting/center-quotient arguments using Dixmier averaging are known in related quotient constructions. Takesaki's 1971 paper studies quotient algebras associated with finite von Neumann algebras, and modern center-quotient-property literature treats center lifting in broad C*-algebraic settings.

The contribution here is the quotient consequence unlocked by Wang's theorem: for every norm-closed ideal of every finite von Neumann algebra, the full zero-central-trace layer of the C*-quotient is not merely in the closed linear span of commutators but consists of single commutators. This yields a closed-linear image theorem for the single-commutator map, an exact metric distance formula, a quantitative quotient estimate, and the sharper reduced-product/corona consequences above.

To the best of our knowledge, searches by the source identifier, finite-von-Neumann quotient terminology, center-valued trace, center quotient property, single commutator, matrix corona, reduced product, and equivalent formulations did not locate this combined theorem. Tuan Tran's independent arXiv:2609.20161 on dimension-free matrix commutator bounds records a passage to tracial matrix ultraproducts; that setting uses the tracial \(2\)-norm ideal and does not cover the operator-norm C*-quotients and arbitrary closed ideals treated here.

Residual bibliographic risk remains because older center-quotient/Dixmier-property literature could contain a nonquantitative quotient formulation, and abstract commutator literature could make some deductions routine once Wang's theorem is supplied. The classical center-lifting mechanism and the quotient-norm formula are therefore not claimed as new.

## Limitations

- Wang's universal constant \(K\) is inherited; no new numerical value or optimality claim is made.
- For a general quotient \(M/J\), the proof gives commutator cost at most \(2K\|a\|\); whether the factor \(2\) can always be removed is not resolved.
- The descended central tracial projection can be nonfaithful.
- Only finite von Neumann algebras are covered; no properly infinite analogue is asserted.
- The reduced-product sharp \(K\) statement is for norm reduced products of finite-dimensional C*-algebras as defined above.
- The result concerns additive commutators \(bc-cb\), not multiplicative group commutators.
- Cross-model review has not been performed.

## References

1. Jiaqi Wang, *A uniform commutator bound in finite von Neumann algebras*, arXiv:2609.16932v1 (2026). https://arxiv.org/abs/2609.16932
2. Generalized Dixmier averaging theorem, recalled for finite von Neumann algebras in *Elementary equivalence and disintegration of tracial von Neumann algebras*, Forum of Mathematics, Sigma (2025), Theorem 2.7. https://doi.org/10.1017/fms.2025.10066
3. Masamichi Takesaki, *The quotient algebra of a finite von Neumann algebra*, Pacific J. Math. 36 (1971), 827–831. https://doi.org/10.2140/pjm.1971.36.827
4. Tuan Tran, *Quantum expanders and dimension-free commutator bounds*, arXiv:2609.20161v1 (2026). https://arxiv.org/abs/2609.20161
