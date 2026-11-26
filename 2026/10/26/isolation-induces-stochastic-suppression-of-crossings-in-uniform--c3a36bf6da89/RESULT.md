# Stochastic suppression of crossings under isolated-chord size bias

## Finding

In a uniform perfect matching of \(2n\) cyclically ordered labeled endpoints, let \(C_n\) count crossing pairs and \(I_n\) count chords crossing no other chord. For \(n\ge2\), the crossing count under \(I_n\)-size bias is stochastically smaller than the ordinary crossing count:
\[
\frac{\mathbb E[I_ng(C_n)]}{\mathbb E I_n}\le \mathbb E[g(C_n)]
\]
for every nondecreasing real function \(g\) on \(\{0,\ldots,\binom n2\}\). The inequality is strict for strictly increasing \(g\). More precisely, if an endpoint pair separates arcs with \(2k\) and \(2(n-1-k)\) other endpoints, the crossing count conditional on that pair being an isolated chord is stochastically bounded above by \(C_{n-1}\), which is in turn stochastically bounded above by \(C_n\).

## Assumptions and scope

All perfect matchings are equally likely. A crossing means that the endpoints of the two chords alternate in the cyclic order. A chord need not join consecutive endpoints to be isolated. Size bias here means weighting each diagram by its number of isolated chords, not conditioning on the presence of one or more isolated chords. No stochastic comparison under the latter conditioning or general negative association is asserted.

## Proof

**Coupling.** To generate a uniform diagram with \(m\) chords, give each of \(m\) indexed chords two independent uniform points on a circle. Label the ranks of the resulting \(2m\) points starting from a fixed origin. The rank permutation is uniform; every unlabeled pairing of the ranks has the same number \(2^m m!\) of indexed and oriented representations. Within any two disjoint groups of chords the crossing counts are independent, since each is a function of its group's own independent coordinates. Deleting endpoints of the other group does not change whether endpoints alternate. Therefore the sum of the crossing counts from groups of sizes \(a,b\) is bounded pointwise by the crossing count of the entire diagram of size \(a+b\). In particular \(C_a^{(1)}+C_b^{(2)}\le_{\rm st} C_{a+b}\), where the summands are independent and \(C_0=0\). Taking a group of size one shows \(C_{n-1}\le_{\rm st}C_n\); the counts differ in this coupling with positive probability when \(n\ge2\), since the extra chord crosses the first chord with probability \(1/3\).

**Conditioning on a designated chord.** Let \(A_c\) be the event that a given endpoint pair \(c\) occurs and is isolated. A chord with one endpoint in each open arc of \(c\) would cross it. Thus on \(A_c\) there must be even numbers of remaining endpoints on both arcs. With arc sizes \(2k\) and \(2\ell\), where \(k+\ell=n-1\), each pair of within-arc matchings specifies exactly one full completion. Uniformity gives independent uniform within-arc matchings. The conditional count is consequently distributed as \(C_k^{(1)}+C_\ell^{(2)}\), and the coupling bounds it by \(C_{n-1}\) in stochastic order.

**Isolated-chord weighting.** Write \(I_n=\sum_c\mathbf 1_{A_c}\). The expectation on the left of the theorem is the weighted average of \(\mathbb E[g(C_n)\mid A_c]\), with weights \(\Pr(A_c)/\mathbb EI_n\) over events of positive probability. These weights exist since an adjacent pair occurs and is isolated with positive probability. Each average term is at most \(\mathbb E[g(C_{n-1})]\). The final comparison to \(\mathbb E[g(C_n)]\) is strict when \(g\) is strictly increasing by the positive-probability strict inequality in the coupling.

## Verification

`python verify.py` exhaustively checks the conditional split laws for every designated endpoint pair of positive isolation probability, the comparisons of the corresponding upper tails with those of \(C_{n-1}\) and \(C_n\), and the \(I_n\)-weighted tail comparisons for \(2\le n\le6\). These finite exact checks supplement the coupling proof.

## Relationship to prior work

Acan and Pittel, *Formation of a giant component in the intersection graph of a random chord diagram* ([arXiv:1406.2867](https://arxiv.org/abs/1406.2867)), give a component decomposition into arcs and, in §4, equation (4.9), an enumerative formula for conditional component counts. Its one-chord, zero-crossing specialization, together with the marginal crossing distribution, determines the isolated-chord-weighted crossing probabilities. The [October 12, 2026 isolated-chord covariance result](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-isolated-chords-impose-an-exact-crossing-count-penalty-with-a-no--0f60fb4dde2a/RESULT.md) gives the independent arc decomposition, the exact mixed covariance and its sign. The [October 13, 2026 marked simple-chord result](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-a-marked-simple-chord-gives-an-exact-crossing-palm-law--6cd88475e150/RESULT.md) proves stochastic suppression when weighting by the count of consecutive-endpoint chords; the biased law there is exactly \(C_{n-1}\). That simple-chord comparison alone does not address positive chord counts on both arcs. The contribution here is the order for all isolated chords, via the bound on independent crossing counts at each arc split, not the exact covariance or the enumeration of the biased law.
