# Layer-by-layer symmetry loss makes the strictly \(n\)-finite Heyting witnesses rigid

## Finding

For every \(n\ge 0\), consider the Esakia space \(X_n\) introduced by Hyttinen and Quadrellaro. Put
\[
q=2^n+1,
\]
so each finite level \(L_n^i\) has \(q\) points, labelled \(x_i^0,\ldots,x_i^{q-1}\). For \(d\ge 0\), let
\[
T_{n,d}=\bigcup_{i=0}^d L_n^i
\]
with the order induced from \(X_n\). Then
\[
\operatorname{Aut}(T_{n,d})\cong
\begin{cases}
S_{q-d},&0\le d\le q-1,\\
1,&d\ge q-1.
\end{cases}
\]
In particular, after only \(q\) consecutive levels have been retained, all finite-level symmetry has disappeared.

The full Esakia space is therefore rigid:
\[
\operatorname{Aut}(X_n)=1.
\]
By Esakia duality, the infinite \((n+1)\)-generated Heyting algebra \(X_n^*\) used in the source construction is rigid as well:
\[
\boxed{\operatorname{Aut}(X_n^*)=1}.
\]
Thus the published strictly \(n\)-finite witnesses may simultaneously be taken to have no nontrivial algebra automorphisms.

## Assumptions and scope

The source defines \(X_n\) as the one-point compactification of countably many finite levels together with a partial order having minimum \(x_\infty\). For adjacent levels, its defining relation is
\[
x_i^l\le x_{i-1}^r
\quad\Longleftrightarrow\quad
r\ne l+1,
\]
where \(0\le l,r<q\); for level gaps of at least two, every lower point lies below every upper point. Hence the only missing comparabilities between adjacent levels form a matching of size \(q-1\): the lower point with label \(q-1\) and the upper point with label \(0\) are the unmatched vertices.

The finite objects \(T_{n,d}\) are used only to expose the symmetry mechanism. They are induced finite posets, not additional algebras asserted by the source. The rigidity conclusion for \(X_n^*\) uses only the source definition of \(X_n\) and ordinary Esakia duality.

## Proof

Every order automorphism of \(T_{n,d}\) preserves its levels. Indeed, \(L_n^0\) is exactly the set of maximal points; after deleting it, \(L_n^1\) is the set of maximal remaining points, and so on. Write the permutation induced on level \(i\) as
\[
p_i\in S_q.
\]

Consider the adjacent levels \(L_n^{i-1}\) and \(L_n^i\). Their missing comparabilities are exactly
\[
\bigl\{(x_i^l,x_{i-1}^{l+1}):0\le l<q-1}\bigr\}.
\]
This is a matching with a unique unmatched lower vertex \(x_i^{q-1}\) and a unique unmatched upper vertex \(x_{i-1}^0\). Therefore every automorphism must satisfy
\[
p_i(q-1)=q-1,\qquad p_{i-1}(0)=0,
\]
and preservation of each missing pair gives
\[
p_{i-1}(l+1)=p_i(l)+1\qquad(0\le l<q-1).
\]
Consequently \(p_i\) is uniquely determined by \(p_{i-1}\): if \(F\) denotes the shift operation
\[
F(p)(l)=p(l+1)-1\quad(0\le l<q-1),
\qquad
F(p)(q-1)=q-1,
\]
then \(p_i=F(p_{i-1})\). The map \(F(p)\) is a permutation exactly when \(p(0)=0\), and its value at zero is zero exactly when \(p(1)=1\).

Iterating this observation down \(d\) adjacent interfaces shows that a top-level permutation \(p_0\) extends to an automorphism of \(T_{n,d}\) if and only if
\[
p_0(j)=j\qquad(0\le j<\min(d,q-1)).
\]
When \(d\le q-1\), the remaining \(q-d\) labels may be permuted arbitrarily, and every such permutation has a unique extension. Hence
\[
\operatorname{Aut}(T_{n,d})\cong S_{q-d}.
\]
At \(d=q-1\), all labels on the top level are fixed, so the truncation is rigid; every deeper level is then fixed successively by the same adjacent-level recurrence. This proves the finite formula for all \(d\).

For the full \(X_n\), the point \(x_\infty\) is the unique minimum and is fixed by every order automorphism. The same maximal-layer argument preserves each \(L_n^i\). Restricting any automorphism to \(T_{n,q-1}\) makes it the identity there, and the recurrence forces the identity on all deeper levels. Thus every order automorphism of \(X_n\) is the identity. In particular every Esakia automorphism is the identity. Since Esakia duality sends Heyting-algebra automorphisms contravariantly to Esakia-space automorphisms, \(X_n^*\) is rigid.

## Verification

The standalone checker exhausts every possible top-level permutation for widths \(2\le q\le7\) and every truncation depth through two levels beyond the predicted rigidity threshold. For each candidate it constructs the forced lower-level permutations, then directly checks every pairwise order relation in the whole truncation. The exhaustive counts agree with
\[
(q-d)!\quad(0\le d\le q-1)
\]
and with one automorphism thereafter. It also checks the rigidity threshold for the source widths \(q=2^n+1\) through \(n=8\).

Replay output:

`VERIFY_OK 53567 exact assertions; exhaustive top-layer permutations for q<=7 and all truncation depths`

The computation checks finite instances of the exact recurrence; the all-\(n\) rigidity theorem is proved symbolically above and does not rely on extrapolation from the finite run.

## Relationship to prior work

Hyttinen and Quadrellaro introduced the spaces \(X_n\) to construct infinite \((n+1)\)-generated Heyting algebras whose \(n\)-generated subalgebras are uniformly finite. Their source gives the exact layered order used above and proves the resulting strict \(n\)-finiteness phenomenon. Direct full-text inspection found no occurrence of “automorphism”, “rigid”, or “symmetr”, and no symmetry analysis of the construction.

Targeted searches under the source title, the notation \(X_n\), rigid Heyting algebras, automorphism groups, and the layered “complete bipartite minus a matching” description did not locate the truncation formula or the rigidity conclusion. General facts about crown graphs and rigid ordered structures do not imply the statement, because the source's successive matchings are deliberately offset: each new layer fixes one additional top-level label, which is the mechanism quantified by the factorial descent above.

The source's existence theorem and all general facts about Esakia duality are prior work and are not part of the originality claim. The claimed addition is the exact automorphism profile of the source truncations and the resulting rigidity of these specific strictly \(n\)-finite witnesses.

## Limitations

The theorem concerns automorphisms, not arbitrary endomorphisms or p-morphisms of \(X_n\). It does not assert that every strictly \(n\)-finite variety has a rigid witness, only that the particular witness family constructed in the cited source is rigid. The proof is elementary once the layered order is isolated, so an equivalent observation may exist as unindexed folklore. No independent audit has been performed.

## References

1. T. Hyttinen and D. E. Quadrellaro, *Varieties of strictly n-generated Heyting algebras*, arXiv:2306.12250, first public 2023-06-21. The later journal version, with M. Martins and T. Moraschini, is *Strictly n-finite varieties of Heyting algebras*, *Journal of Symbolic Logic*, DOI:10.1017/jsl.2024.48.
2. Standard Esakia duality between Heyting algebras with homomorphisms and Esakia spaces with p-morphisms, as reviewed in the cited source.
