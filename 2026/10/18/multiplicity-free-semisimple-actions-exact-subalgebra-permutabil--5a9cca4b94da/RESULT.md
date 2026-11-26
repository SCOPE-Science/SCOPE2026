# Exact mixed and total subalgebra-permutability counts for multiplicity-free semisimple actions

## Finding

Let \(q\) be a prime power and let \(f_1,\dots,f_r\) be distinct monic irreducibles over \(\mathbb F_q\), with \(r\ge2\) and \(d_i=\deg f_i\ge2\). Set \(V_i=\mathbb F_q[t]/(f_i)\), \(V=\bigoplus_i V_i\), and \(d=\dim V\). In \(L=\mathbb F_q h\ltimes V\), the ideal \(V\) is abelian and \([h,v]=Av\), where \(A\) is multiplication by \(t\). Two subalgebras permute if their vector sum is a subalgebra. Pairs are ordered, and all \(\mathbb F_q\)-linear subalgebras, including zero and \(L\), are counted. Write \(d_S=\sum_{i\in S}d_i\) and
\[
G_a(q)=\sum_{k=0}^a{a\brack k}_q,\qquad H_q(a,b)=\sum_{k=0}^a{a\brack k}_q q^{b(a-k)}.
\]
The ordered permutable-pair count with exactly one subalgebra contained in \(V\) is
\[
P_{\rm mix}=2\sum_{S\subseteq[r]}q^{d-d_S}\sum_{T\subseteq[r]\setminus S}H_q(d_S,d_T).
\]
The total subalgebra count \(N\) and total ordered permutable-pair count \(P\) are consequently
\[
N=G_d(q)+\prod_i(1+q^{d_i}),\qquad
P=G_d(q)^2+P_{\rm mix}+\prod_i(1+3q^{d_i}).
\]
The exterior subalgebra count and the all-exterior pair term are already given by the squarefree census of Lie retractions [2], via the correspondence below. The additional enumeration is the mixed term, yielding the full probability \(\operatorname{sd}(L)=P/N^2\) and its dimension threshold. For fixed factor degrees, as \(q\) grows through fields admitting the specified distinct irreducibles, \(\operatorname{sd}(L)\to1/4\) when \(d=4\), and \(\operatorname{sd}(L)\to1\) when \(d\ge5\).

## Proof

**Subalgebras.** The distinct factors and the Chinese remainder projections imply that the \(A\)-invariant subspaces are precisely \(V_S=\bigoplus_{i\in S}V_i\): an invariant subspace splits by the polynomial projections and has either zero or the full intersection with each simple factor. All subspaces of \(V\) are subalgebras. A subalgebra not contained in \(V\) has intersection \(V_S\) with \(V\), since bracketing with any of its elements \(h+u\) acts on the intersection by \(A\). It thus has the unique form \(X_{S,u}=V_S\oplus\mathbb F_q(h+u)\) with \(u\) specified modulo \(V_S\); conversely all these spaces are subalgebras. This gives \(N\). Any two subalgebras contained in \(V\) permute, giving \(G_d(q)^2\).

**Mixed pairs.** For \(U\le V\) and \(X_{S,u}\), closure of \(U+X_{S,u}\) under brackets is equivalent to \(A(U+V_S)\subseteq U+V_S\). This says that its image in \(V/V_S\) is \(V_T\) for some unique \(T\subseteq[r]\setminus S\), using the complementary summands to identify the quotient. For this image and each \(k\)-dimensional \(K=U\cap V_S\), the quotient \(U/K\) is the graph of an arbitrary map \(V_T\to V_S/K\). There are \({d_S\brack k}_q\) choices of \(K\) and \(q^{d_T(d_S-k)}\) such maps per choice. Multiply by \(q^{d-d_S}\) choices of \(u\) and sum over \(k,S,T\), doubling for order. This proves the mixed count.

**Exterior pairs and the earlier retraction census.** For \(X_{S,u}\) and \(X_{T,v}\) put \(W=V_{S\cup T}\). Their sum has intersection \(W+\mathbb F_q(v-u)\) with \(V\), and the brackets with \(W\) stay in \(W\). Closure therefore requires the image of \(v-u\) in \(V/W\) to be zero or span an invariant line. The second option is impossible for a nonzero image since every simple factor has degree at least two. Thus they permute exactly when \(u-v\in W\).

Choose \(u\) in the complement of \(V_S\), and let \(p_S\) be projection onto \(V_S\). Associate to \(X_{S,u}\) the idempotent Lie endomorphism \(R_{S,u}\) whose restriction to \(V\) is \(p_S\) and with \(R_{S,u}(h)=h+u\). It is a Lie endomorphism since \(p_S\) commutes with \(A\), and it is idempotent since \(p_Su=0\). Its image is \(X_{S,u}\). Conversely \([L,L]=V\) (as \(A\) is invertible), so an idempotent Lie endomorphism preserves \(V\) and induces coefficient zero or one on \(L/V\). Coefficient zero forces its restriction to \(V\) to vanish by bracket preservation and invertibility; idempotence then forces the endomorphism itself to be zero. With coefficient one its restriction is an idempotent commuting with \(A\), necessarily one of the \(p_S\), and its translation is killed by \(p_S\). This proves the bijection with nonzero retractions. Two retractions commute on \(V\), and commute on \(h\) exactly when \((1-p_T)u=(1-p_S)v\), or \(u-v\in V_{S\cup T}\). Consequently the squarefree corollary of [2], with the pairs involving the zero retraction removed, gives the exterior-pair product in \(P\). Equivalently, in each block there is one choice if it belongs to both \(S,T\), and \(q^{d_i}\) choices for each of the other three membership patterns: a free translation in the one missing block, or a common translation when both are missing.

**Limit and smallest case.** The leading degree of \(G_d(q)\) is \(\lfloor d^2/4\rfloor\), since \({d\brack k}_q\) is monic of degree \(k(d-k)\). For \(d\ge5\) this exceeds \(d\), so exterior subalgebras are a vanishing proportion and the proportion of pairs with both inside \(V\) tends to one. If \(d=4\), the degrees are \((2,2)\). Here \(G_4=q^4+3q^3+4q^2+3q+5\), and the mixed count is \(8q^4+4q^2(q^4+q^3+q^2+q+4)+2G_4\). Thus
\[
N=2q^4+3q^3+6q^2+3q+6,
\]
\[
P=q^8+6q^7+21q^6+34q^5+67q^4+64q^3+79q^2+36q+36.
\]
The leading ratio is \(1/4\). For two distinct irreducible quadratics over \(\mathbb F_3\), for example, \(N=312\), \(P=51264\), and \(\operatorname{sd}(L)=89/169\).

## Verification and scope

The argument holds in every characteristic. The companion `verify.py` tests the formula on finite examples by enumerating subspaces of \(V\), generating exterior subalgebras by the classification, and checking pairwise bracket closure. For the two multiple-factor examples, degrees \((2,2)\) over \(\mathbb F_3\) and \((2,3)\) over \(\mathbb F_2\), the resulting \((N,P)\) are \((312,51264)\) and \((419,144477)\). The formulas depend on the degrees, not the polynomial coefficients. Repeated factors are excluded because their invariant subspaces need not be coordinate sums; linear factors are excluded because an exterior sum can then have an invariant residual line.

## References

1. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, [arXiv:2609.19086v1](https://arxiv.org/abs/2609.19086v1). Gives the invariant and counts for other families, including the three-dimensional Heisenberg algebra and \(\mathfrak{sl}_2(\mathbb F_q)\).
2. *Commuting Lie retractions: a rational-canonical joint-rank census*, [2026-10-12 record](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-commuting-lie-retractions-a-rational-canonical-joint-rank-census--0e69fccd676e/RESULT.md), squarefree corollary and commutation condition in the proof. Its prior counts apply to the exterior terms; it does not count mixed pairs involving arbitrary subspaces of the abelian ideal.
