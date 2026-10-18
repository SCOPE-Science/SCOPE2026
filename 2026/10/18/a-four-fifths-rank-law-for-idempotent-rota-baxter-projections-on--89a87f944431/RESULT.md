# A four-fifths rank law for idempotent Rota–Baxter projections on finite Heisenberg Lie algebras

## Finding
Let \(q\) be any prime power, \(m\ge2\), and let \(\mathfrak h_m(q)\) be the Heisenberg Lie algebra of dimension \(2m+1\). Every idempotent weight-\(-1\) Lie Rota–Baxter operator has an explicitly counted rank, and the count is symmetric about half the Lie-algebra dimension.

Define
\[
I_{m,q}(b)=\prod_{j=0}^{b-1}\frac{q^{2m-j}-q^j}{q^b-q^j},\qquad
F_{m,q}(b)=I_{m,q}(b)q^{b(2m-b+1)}\quad(0\le b\le m).
\]
The empty product is one. If \(N_{m,q}(r)\) counts these operators of rank \(r\), then
\[
N_{m,q}(b)=N_{m,q}(2m+1-b)=F_{m,q}(b)\quad(0\le b\le m),
\]
and the total number is \(2\sum_{b=0}^{m}F_{m,q}(b)\). Equivalently, the exact rank enumerator is
\[
\sum_{r=0}^{2m+1}N_{m,q}(r)t^r
=\sum_{b=0}^{m}F_{m,q}(b)(t^b+t^{2m+1-b}).
\]

If \(P\) is chosen uniformly among these operators and \(K_m=\min(\operatorname{rank}P,2m+1-\operatorname{rank}P)\), then for fixed \(q\),
\[
K_m=\tfrac45m+O_{\mathbb P,q}(1),\qquad
\frac{\operatorname{rank}P}{2m+1}\ \Longrightarrow\ \tfrac12\delta_{2/5}+\tfrac12\delta_{3/5}.
\]
The concentration is stronger than a law of large numbers: fluctuations of \(K_m\) remain of bounded order and have discrete-Gaussian tails.

## Assumptions and scope
The coefficient field is \(\mathbb F_q\), including arbitrary prime powers and characteristic two. Let \(V\) be a \(2m\)-dimensional vector space with a nondegenerate alternating bilinear form \(\omega\), and define
\[
\mathfrak h_m(q)=V\oplus\mathbb F_q z,\qquad [u+az,v+bz]=\omega(u,v)z.
\]
An operator is an \(\mathbb F_q\)-linear map \(P\) satisfying both
\[
P^2=P,\qquad [Px,Py]=P([Px,y]+[x,Py]-[x,y])\quad\text{for all }x,y.
\]
The enumeration counts distinct actual linear operators, not equivalence classes under automorphisms. The limiting statement holds as \(m\to\infty\) for each fixed \(q\); it is not claimed to be uniform when \(q\) varies with \(m\).

## Proof
**1. Projection/factorization lemma.** If \(P^2=P\), put \(U=\operatorname{im}P\) and \(W=\ker P\); then \(\mathfrak h_m(q)=U\oplus W\). Substituting vectors of \(U\) or \(W\) separately into the displayed Rota–Baxter identity shows \([U,U]\subseteq U\) and \([W,W]\subseteq W\). Conversely, for \(x=u+w\) and \(y=u'+w'\), the expression within \(P\) is \([u,u']-[w,w']\); its image is \([u,u']\), exactly \([Px,Py]\). Thus the operators are in bijection with *ordered complementary Lie subalgebra pairs* \((U,W)\), a classical general principle. This direct argument remains valid in every characteristic.

**2. Classification of Lie subalgebras.** Write \(\pi:\mathfrak h_m(q)\to V\) for the projection. A subalgebra \(U\) containing \(z\) is exactly \(\pi^{-1}(A)\) for some vector subspace \(A\le V\), and conversely every such inverse image is a subalgebra. A subalgebra \(W\) not containing \(z\) projects injectively onto a subspace \(B\le V\), and must be the graph \(\{b+\ell(b)z:b\in B\}\) of a unique linear functional \(\ell:B\to\mathbb F_q\). Closure under the bracket forces \(\omega|_{B\times B}=0\), so \(B\) is totally isotropic and \(\dim B\le m\); conversely these conditions suffice.

**3. Exactly one central summand.** In any complementary subalgebra pair \(U\oplus W=\mathfrak h_m(q)\), at most one contains \(z\). If neither did, both dimensions would be at most \(m\), contradicting their sum \(2m+1\). Hence exactly one contains \(z\). Suppose the noncentral factor has dimension \(b\le m\), projected isotropic subspace \(B\), and graph functional \(\ell\). The central factor has the form \(\pi^{-1}(A)\). Complementarity holds exactly when \(V=A\oplus B\), so \(\dim A=2m-b\). For each fixed \(B\), the number of such vector-space complements is \(q^{b(2m-b)}\), by expressing every complement as the graph of a linear map from one fixed complement into \(B\). There are independently \(q^b\) functionals \(\ell\).

**4. Count isotropic subspaces.** Build an ordered independent isotropic \(b\)-frame one vector at a time. After selecting \(j\) vectors spanning an isotropic \(j\)-space, its perpendicular contains \(q^{2m-j}\) vectors and its span contains \(q^j\); thus the next vector has \(q^{2m-j}-q^j\) choices. Dividing by the number \(\prod_{j=0}^{b-1}(q^b-q^j)\) of ordered bases of a fixed \(b\)-space proves that the number of isotropic \(b\)-subspaces is \(I_{m,q}(b)\). Multiplication by the complement and graph choices gives \(F_{m,q}(b)\) pairs with the noncentral summand of dimension \(b\). The two choices of which ordered summand is noncentral yield ranks \(b\) and \(2m+1-b\), with identical counts. The ranges do not overlap, since \(b\le m\). This proves the exact rank polynomial.

**5. Rank concentration.** Factor the product to obtain the exact expression
\[
F_{m,q}(b)=q^{4mb-\frac52b^2+\frac32b}
\frac{\displaystyle\prod_{k=m-b+1}^{m}(1-q^{-2k})}
{\displaystyle\prod_{k=1}^{b}(1-q^{-k})}.
\]
For each fixed \(q\), both numerator and denominator products lie between the positive convergent infinite products \(\prod_{k\ge1}(1-q^{-2k})\) and \(\prod_{k\ge1}(1-q^{-k})\), respectively, and one. Thus the product quotient stays between constants depending only on \(q\), for all \(0\le b\le m\). The exponent completes the square:
\[
4mb-\tfrac52b^2+\tfrac32b
=\tfrac52\bigl(\tfrac{8m+3}{10}\bigr)^2
-\tfrac52\bigl(b-\tfrac{8m+3}{10}\bigr)^2.
\]
Put \(b_0=(8m+3)/10\). For sufficiently large \(m\), the range \([0,m]\) contains an integer within \(1/2\) of \(b_0\). Comparing every term with that term bounds the probability of \(|K_m-b_0|\ge t\) by \(C_q q^{-5t^2/4}\) for all \(t\ge1\), after summing the rapidly decreasing discrete-Gaussian series. Therefore \(K_m=b_0+O_{\mathbb P,q}(1)=4m/5+O_{\mathbb P,q}(1)\). Finally, \(P\mapsto\operatorname{id}-P\) exchanges ranks \(b\) and \(2m+1-b\), so the two branches have equal probability, giving the stated equal-mixture limit.

## Verification
The included self-contained `verify.py` checks the full rank vector by two independent finite routes. It enumerates all linear subspaces in row-reduced echelon form and tests Lie-subalgebra pairs for \((m,q)=(1,2),(1,3),(2,2)\). It also exhaustively enumerates all \(3\times3\) coefficient matrices and evaluates both polynomial operator identities for \(q=2,3\). All checks returned `VERIFY_OK`. In particular, at \((m,q)=(2,2)\) the rank counts in increasing rank order are \((1,240,960,960,240,1)\). These are finite verifications of the exact theorem, not a proof of the asymptotic. Reproduce with `python3 verify.py` (standard library only).

## Relationship to prior work
The correspondence between idempotent weight-\(-1\) Lie Rota–Baxter maps and ordered complementary Lie subalgebras is classical and is explicitly recalled by Han, Khudoyberdiyev, Xie and Zhang [1]. Earlier three-dimensional Heisenberg operator classifications by Ji and Hua [2] and Rathee [3] concern the \(m=1\) case, including non-idempotent or different-weight settings. The higher-rank finite-field count here does not claim that correspondence or the three-dimensional case as new. Cairns and Nikolayevsky [4] consider *respectful* Lie decompositions satisfying an additional cross-bracket inclusion, which is not imposed here. The new assertions are the uniform higher-rank count and its four-fifths law.

## Limitations
An equivalent counting identity may exist in unindexed finite-geometric or Rota–Baxter literature. Related three-dimensional classification papers and abstract-level sources do not settle whether such an identity was stated elsewhere. The theorem treats only idempotent weight-\(-1\) *linear* operators on the specified Heisenberg Lie algebras; it does not classify arbitrary Rota–Baxter operators, arbitrary nilpotent Lie algebras, or group-valued operators. The finite checker covers prime fields of orders two and three only. No independent mathematical audit has been performed.

## References
[1] JiaJia Han, Abror Khudoyberdiyev, Yunzhou Xie, Yi Zhang, *Rota-Baxter operators and factorization of Lie affgebras*, arXiv:2610.14838 (first publicly submitted 2026-10-10), https://arxiv.org/abs/2610.14838.

[2] Guangzhi Ji and Xiuying Hua, *Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra*, Korean Journal of Mathematics 26 (2018), 53–60, DOI:10.11568/kjm.2018.26.1.53.

[3] Nishant Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428 (2024), https://arxiv.org/html/2402.15428v3.

[4] Grant Cairns and Yuri Nikolayevsky, *Respectful decompositions of Lie algebras*, arXiv:2207.03068 (2022), https://arxiv.org/html/2207.03068v1.
