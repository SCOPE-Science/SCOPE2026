# Total and paired domination in generalized total graphs at prime ideals

## Finding

Let \(R\) be a finite commutative ring with identity, let \(P\) be a prime ideal, and write \(s=|P|\) and \(q=|R/P|\). For the generalized total graph \(GT_P(R)\), total domination exists if and only if paired domination exists if and only if \(s\ge2\). When \(s\ge2\), \[\gamma_t(GT_P(R))=\gamma_{\mathrm{pr}}(GT_P(R))=\begin{cases}2q,&2\in P,\\q+1,&2\notin P.\end{cases}\] Moreover every minimum total dominating set is paired. The number of minimum total dominating sets, equivalently minimum paired dominating sets, is \[\begin{cases}\binom{s}{2}^{q},&2\in P,\\\binom{s}{2}s^{q-1},&2\notin P.\end{cases}\] If \(s=1\), the component on \(P\) is an isolated vertex, so neither strengthened domination parameter exists.

Thus the strengthened domination theory of this prime-ideal family is controlled entirely by the two finite quotient data \(|P|\), \(|R/P|\), and the characteristic parity of \(R/P\). The result also enumerates every minimum witness.

## Assumptions and scope

Let \(R\) be a finite commutative ring with identity and let \(P\) be a prime ideal. Put
\[
s=|P|,
\qquad
q=|R/P|.
\]
Because \(R/P\) is a finite integral domain, it is a finite field. The generalized total graph \(GT_P(R)\) has vertex set \(R\), with distinct \(x,y\) adjacent exactly when
\[
x+y\in P.
\]

A total dominating set \(D\) requires every vertex, including every vertex of \(D\), to have a neighbor in \(D\). A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

Two vertices \(x,y\) are adjacent exactly when their quotient classes satisfy
\[
(y+P)=-(x+P).
\tag{1}
\]
The coset \(P\) itself induces a complete graph \(K_s\), and it has no edges to any other quotient class.

If \(2\in P\), then \(R/P\) has characteristic two, so every quotient class equals its own additive inverse. By (1), each of the \(q\) cosets of \(P\) induces a copy of \(K_s\), and there are no edges between distinct cosets. Hence
\[
GT_P(R)\cong qK_s.
\tag{2}
\]

If \(2\notin P\), then \(R/P\) has odd characteristic. The zero class gives the component \(K_s\). Every nonzero quotient class \(a+P\) is distinct from \(-a+P\), and (1) makes their union a complete bipartite component \(K_{s,s}\). The \(q-1\) nonzero classes therefore pair off, giving
\[
GT_P(R)
\cong
K_s\sqcup \frac{q-1}2K_{s,s}.
\tag{3}
\]

If \(s=1\), the component \(K_s=K_1\) is isolated. A graph with an isolated vertex has neither a total dominating set nor a paired dominating set.

Assume now that \(s\ge2\). Every connected component in (2) or (3) has total domination number two. In \(K_s\), a minimum total dominating set is exactly an arbitrary edge, so there are
\[
\binom{s}2
\]
choices. In \(K_{s,s}\), a minimum total dominating set consists of one vertex from each part, so there are
\[
s^2
\]
choices. Each such two-vertex set is itself an edge and therefore has a perfect matching.

Total domination is additive over a disjoint union whose components have no isolated vertices. Thus (2) gives
\[
\gamma_t(GT_P(R))=2q,
\]
while (3) gives
\[
\gamma_t(GT_P(R))
=
2+2\frac{q-1}2
=
q+1.
\]
Since every componentwise minimum total dominating set is an edge, their union has a perfect matching. Hence the same constructions are paired dominating, and paired domination cannot be smaller than total domination. Therefore
\[
\gamma_{\mathrm{pr}}(GT_P(R))
=
\gamma_t(GT_P(R)).
\]

Finally, choices in distinct components are independent. From (2), the number of minimum total dominating sets is
\[
\binom{s}2^q.
\]
From (3), it is
\[
\binom{s}2
\left(s^2\right)^{(q-1)/2}
=
\binom{s}2s^{q-1}.
\]
The same counts enumerate minimum paired dominating sets.

## Verification

The standalone `verify.py` builds \(GT_P(\mathbb Z/n\mathbb Z)\) directly from the rule \(x+y\in P\) for nine prime-ideal examples. It exhaustively determines both strengthened domination minima and counts all minimum witnesses. The examples cover characteristic-two and odd quotient fields, several nonzero ideal sizes, and the field obstruction \(P=0\).

It also replays the component formulas over forty-eight abstract \((s,q)\) profiles, including residue-field orders that are nonprime prime powers.

Exact output:

```text
VERIFY_OK
structural_profiles_checked=48
Zmod_case n=4 p=2 s=2 q=2 gamma_t=4 gamma_pr=4 count_t=1 count_pr=1
Zmod_case n=6 p=2 s=3 q=2 gamma_t=4 gamma_pr=4 count_t=9 count_pr=9
Zmod_case n=8 p=2 s=4 q=2 gamma_t=4 gamma_pr=4 count_t=36 count_pr=36
Zmod_case n=9 p=3 s=3 q=3 gamma_t=4 gamma_pr=4 count_t=27 count_pr=27
Zmod_case n=12 p=2 s=6 q=2 gamma_t=4 gamma_pr=4 count_t=225 count_pr=225
Zmod_case n=12 p=3 s=4 q=3 gamma_t=4 gamma_pr=4 count_t=96 count_pr=96
Zmod_case n=15 p=3 s=5 q=3 gamma_t=4 gamma_pr=4 count_t=250 count_pr=250
Zmod_case n=20 p=5 s=4 q=5 gamma_t=6 gamma_pr=6 count_t=1536 count_pr=1536
Zmod_case n=5 p=5 s=1 q=5 gamma_t=None gamma_pr=None count_t=0 count_pr=0
```

The finite checks are corroborative only. The arbitrary finite-ring theorem is proved by the quotient-class decomposition above.

## Relationship to prior work

Anderson and Badawi introduced the generalized total graph and, for a prime ideal \(P\), proved the exact decomposition of the non-\(P\) part into disjoint complete graphs when \(2\in P\) and disjoint complete bipartite graphs when \(2\notin P\). Together with their observation that the induced graph on \(P\) is a disjoint complete component, this supplies the structural input used here.

Patwari, Saikia, and Goswami later studied ordinary domination of the same generalized total graph. Their full text determines ordinary domination numbers and bondage numbers, but targeted full-text checks located neither total domination nor paired domination.

Two superficially close papers by Tamizh Chelvam and Balamurugan require care because text extraction can lose complement bars. Their domination calculations concern the complement of the generalized total graph. A page-level visual inspection of the finite-field paper confirms that its section on total domination is explicitly for \(\overline{GT(F)}\), not for \(GT(F)\). The companion commutative-ring paper likewise states in its title and abstract that its target is \(\overline{GT_P(R)}\). Those results therefore do not imply the theorem above.

The present claim uses the original graph, not its complement, and strengthens the ordinary-domination literature by giving the complete existence dichotomy, exact total and paired domination numbers, and exact minimum-witness counts.

## Limitations

The theorem assumes that the multiplicative-prime subset is a prime ideal. For a multiplicative-prime subset that is not an ideal, the quotient-coset decomposition used in the proof is unavailable.

The ring is finite. No cardinal-valued analogue is asserted for infinite rings.

The theorem determines strengthened domination and minimum-witness counts, not the full automorphism action on the family of minimum sets.

## References

1. D. F. Anderson and A. Badawi, “The Generalized Total Graph of a Commutative Ring,” *Journal of Algebra and Its Applications* 12 (2013), 1250212. DOI: 10.1142/S021949881250212X.
2. D. Patwari, H. K. Saikia, and J. Goswami, “Some Results on Domination in the Generalized Total Graph of a Commutative Ring,” *Journal of Algebra and Related Topics* 10 (2022), 119–128. DOI: 10.22124/JART.2021.19238.1265.
3. T. Tamizh Chelvam and M. Balamurugan, “Complement of the Generalized Total Graph of Commutative Rings,” *The Journal of Analysis* 27 (2019), 539–553. DOI: 10.1007/s41478-018-0093-6.
