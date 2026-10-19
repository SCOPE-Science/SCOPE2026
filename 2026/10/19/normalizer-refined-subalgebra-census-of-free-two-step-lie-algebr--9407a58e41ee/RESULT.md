# Normalizer-refined subalgebra census of free two-step Lie algebras over finite fields

## Finding

For every finite field \(\mathbb F_q\), consider the free class-two nilpotent Lie algebra on \(d\ge2\) generators, \(L_d=V\oplus\Lambda^2V\), with \(V=\mathbb F_q^d\) and bracket \([v+z,w+z']=v\wedge w\). Put \(c=\binom d2\) and \(k=d-1\). For a subalgebra \(H\), write \(N(H)=\{x\in L_d:[x,H]\subseteq H\}\).

**Rank-one normalizer theorem.** For integers \(0\le b\le c\) and \(0\le t\le k\), the exact number of subalgebras satisfying
\[
\dim\pi_V(H)=1,\qquad \dim(H\cap\Lambda^2V)=b,\qquad
\operatorname{codim}_{L_d}N(H)=k-t
\]
is
\[
M_{d,q}(b,t)=\binom d1_q\binom kt_q\binom{c-k}{b-t}_q
q^{(k-t)(b-t)+c-b},
\]
provided \(0\le b-t\le c-k\) and \(0\le t\le\min(b,k)\); outside these inequalities the count is zero. Here \(\binom nr_q\) is the Gaussian binomial coefficient counting \(r\)-dimensional subspaces of \(\mathbb F_q^n\). In particular, the rank-one ideal stratum is precisely \(t=k\). Summing over \(t\) gives \(\binom d1_q\binom cb_q q^{c-b}\).

**Complete six-dimensional normalizer census.** In the first case beyond the three-dimensional Heisenberg algebra, \(d=3\), put \(g=q^2+q+1\). Define the polynomial
\[
\mathcal Z_{3,q}(X,Y)=\sum_{H\le L_3}X^{\dim H}Y^{\operatorname{codim}_{L_3}N(H)},
\]
where the sum runs over **all** Lie subalgebras, including central subalgebras and the whole algebra. Then
\[
\begin{aligned}
\mathcal Z_{3,q}(X,Y)={}&1+gX+gX^2+(1+qg)X^3+gX^4+gX^5+X^6\\
&+gq^2(q+1)(X^2+X^4)Y\\
&+g\bigl(q^2(q+1)+q^4\bigr)X^3Y\\
&+gq^3XY^2+gq^4X^2Y^2.
\end{aligned}
\]
Thus \(Y=0\) counts the ideals by dimension, while \(Y=1\) counts all subalgebras by dimension; the positive \(Y\)-degrees resolve two distinct nonnormalizer-index strata. At \(q=2\) there are exactly \(577\) subalgebras in total, and at \(q=3\) exactly \(3955\). The theorem holds in all characteristics, including characteristic two.

## Assumptions and scope

A subalgebra here means an \(\mathbb F_q\)-linear subspace closed under the given alternating Lie bracket. A normalizer is a vector subspace; its codimension is taken over \(\mathbb F_q\). The generating space \(V\) is a fixed complementary copy of \(L_d/[L_d,L_d]\), and \(Z=\Lambda^2V\) is central, of dimension \(c\). The zero-dimensional and full subalgebras are included. Gaussian coefficients are defined to be zero for invalid lower indices; the displayed rank-one power of \(q\) is used only in the admissible index range. The formula does not count subalgebras up to automorphism, integral sublattices, or arbitrary class-two Lie algebras.

## Proof

**1. Parameterizing arbitrary subalgebras.** Set \(U=\pi_V(H)\le V\), \(W=H\cap Z\le Z\), \(a=\dim U\), \(b=\dim W\). Since brackets only depend on \(V\)-components, the condition for closure is precisely
\[
\Lambda^2 U\subseteq W.
\]
Once \(U,W\) satisfying this are chosen, \(H\) is the graph of a unique linear map \(U\to Z/W\) together with \(W\). Therefore exactly \(q^{a(c-b)}\) subalgebras have these fixed \(U,W\). The graph maps affect neither closure nor the normalizer: every commutator lies in \(Z\), and \(H\cap Z=W\).

**2. Rank-one normalizers.** When \(a=1\), select \(U=\mathbb F_q u\). The injective map \(V/U\to Z\), \(v+U\mapsto v\wedge u\), has image \(K_U=u\wedge V\) of dimension \(k=d-1\). A vector \(v+z\in L_d\) normalizes \(H\) precisely when \(v\wedge u\in W\). Define \(t=\dim(W\cap K_U)\). The normalizer's \(V\)-projection is the inverse image of \(W\cap K_U\), hence has dimension \(1+t\); all \(c\) central dimensions normalize. Therefore
\[
\dim N(H)=c+1+t,\qquad \operatorname{codim}_{L_d}N(H)=k-t.
\]
For fixed \(U\), the number of \(b\)-subspaces \(W\) with intersection dimension \(t\) with \(K_U\) is the Gaussian intersection count
\[
\binom kt_q\binom{c-k}{b-t}_q q^{(k-t)(b-t)}.
\]
To see this without an external counting lemma: first choose \(W\cap K_U\) and the image of \(W\) in a fixed complement of \(K_U\); each resulting \(W\) is the graph of one of \(q^{(k-t)(b-t)}\) linear maps between the quotient spaces. There are \(\binom d1_q\) choices of \(U\), and \(q^{c-b}\) independent graph lifts \(U\to Z/W\). Multiplying proves \(M_{d,q}(b,t)\). The condition \(N(H)=L_d\) is exactly \(t=k\); it is equivalent to \(H\) being an ideal. Summing over all \(t\) recovers the total \(\binom cb_q\) choices for \(W\), establishing the first specialization.

**3. Complete enumeration when \(d=3\).** Now \(\dim V=\dim Z=3\), so \(L_3\) has dimension six. Let \(a=\dim U\) and classify all four possibilities.

For \(a=0\), \(H=W\subseteq Z\) is central. Its normalizer is \(L_3\), giving the terms \(1+gX+gX^2+X^3\).

For \(a=1\), insert \(c=3\), \(k=2\) into the proved rank-one theorem. Explicitly, the nonzero strata \((\dim H,\operatorname{codim}N(H))\) and their counts are
\[
\begin{array}{c|c}
(1,2):gq^3 & (2,2):gq^4\\
(2,1):gq^2(q+1)&(3,1):gq^2(q+1)\\
(3,0):gq&(4,0):g.
\end{array}
\]

For \(a=2\), \(U\) is a plane and \(\Lambda^2U\) is a line. Thus \(W\) must have dimension \(b\in\{1,2,3\}\); for each \(U\), there are respectively \(1\), \(q+1\), and \(1\) choices for \(W\). Their lift multiplicities are respectively \(q^4\), \(q^2\), and \(1\). If \(b\le2\), every \(v\notin U\) satisfies \(\dim(v\wedge U)=2\) and \((v\wedge U)\cap\Lambda^2U=0\), so \(v\wedge U\) cannot be contained in such a \(W\); the normalizer's projection is exactly \(U\), of codimension one in \(V\). For \(b=3\), \(W=Z\) and the normalizer is all of \(L_3\). There are \(g=\binom32_q\) planes \(U\). These cases contribute \(gq^4X^3Y+gq^2(q+1)X^4Y+gX^5\).

For \(a=3\), closure forces \(W\supseteq\Lambda^2V=Z\); the only possibility is \(H=L_3\), contributing \(X^6\). Adding the four disjoint cases gives the displayed polynomial. Every argument uses linear algebra over an arbitrary field, including characteristic two.

## Verification

A standalone Python 3 checker, `check_normalizer.py`, independently lists all subspaces by reduced row-echelon representatives and performs direct Lie-bracket and normalizer tests. It exhausts the six-dimensional ambient-space subspaces over \(\mathbb F_2\) and \(\mathbb F_3\), checks all rank-one normalizer strata over both fields (and three-dimensional Heisenberg tests over three prime fields), and tests the Gaussian-intersection counts for six-dimensional centers over \(\mathbb F_2\). Running `python3 check_normalizer.py` terminates with `ALL_NORMALIZER_STRATA_VERIFIED`. These finite experiments are checks, not the proof for arbitrary \(q\) or \(d\).

## Relationship to prior work

Seungjai Lee, *Zeta functions of \(\mathbb F_p\)-Lie algebras and finite \(p\)-groups*, arXiv:2010.02268, Theorem 5.1 and Example 5.2, gives the ideal-zeta enumeration for free class-two nilpotent Lie algebras. The present \(Y=0\) specialization is an alternative expression of an already known ideal count, **not** a novel ideal-census theorem. The general Gaussian-intersection identity used in the proof is also standard. The claim made here is only the full normalizer-index refinement, including non-ideal subalgebras, the rank-one joint strata, and the complete six-dimensional bivariate profile. Lee and Voll, *Zeta functions of integral nilpotent quiver representations*, arXiv:2006.12346, studies quiver subrepresentation and related ideal enumerators rather than this normalizer-refined invariant. Noncommuting-graph invariants and endomorphism-orbit counts concern different data and do not imply this joint distribution.

## Limitations

This theorem does not classify individual subalgebra automorphism orbits. Only the rank-one normalizer strata are enumerated in arbitrary generator rank; the full bivariate polynomial is given for exactly three generators. A prior equivalence in older or poorly indexed normalizer-enumeration literature cannot be excluded by searches alone. Independence and external mathematical certification are not claimed.

## References

1. Seungjai Lee, *Zeta functions of \(\mathbb F_p\)-Lie algebras and finite \(p\)-groups*, arXiv:2010.02268, first public posting 2020-10-05; Theorem 5.1 and Example 5.2. https://arxiv.org/abs/2010.02268
2. Seungjai Lee and Christopher Voll, *Zeta functions of integral nilpotent quiver representations*, arXiv:2006.12346, first public posting 2020-06-22. https://arxiv.org/abs/2006.12346
