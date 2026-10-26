# Seven-periodic total domination of squared cycles and a frozen-to-cyclic exchange transition

## Finding

Let \(G_n=C_n^2\) for integers \(n\ge7\), with vertices \(\mathbb Z_n\) and edges between vertices of cyclic distance one or two. A total dominating set \(S\) requires that **every** vertex, including every selected vertex, have a distinct adjacent selected vertex. Write \(n=7k+r\), \(0\le r\le6\). Its minimum cardinality is
\[
\gamma_t(G_n)=2k+\begin{cases}0&r=0,\\1&r\in\{1,2\},\\2&r\in\{3,4,5,6\}.\end{cases}
\]

Define \(\mathcal T_n\) to have one vertex for every total dominating set of cardinality \(\gamma_t(G_n)\), with an edge for each single-vertex replacement preserving minimum total domination. Then for every integer \(k\ge1\),
\[
\mathcal T_{7k}\cong\begin{cases}C_7&k=1,\\7K_1&k\ge2,\end{cases}\qquad\mathcal T_{7k+2}\cong C_{7k+2}.
\]
The \(7\) minimum sets in \(G_{7k}\) are the translations of the cyclic gap word \((2,5)^k\); this multiplicity is already contained in Premala--Sekar's 2014 Theorem 3.2(vi) and is **not** claimed as new. The \(7k+2\) minimum sets in \(G_{7k+2}\) are precisely the \(7k+2\) cyclic translates of the set with successive gap word \((2,5)^k,2\); exchanges link a translate numbered \(a\) to precisely those numbered \(a+7\) and \(a-7\) modulo \(7k+2\).

In particular \(\gamma_t(G_{17})=6\), while Lemma 2.1 in Premala--Sekar (2014) would give \(\lceil17/5\rceil+1=5\). The exhibited gap argument proves the correction independently of that paper's polynomial recurrences.

## Assumptions and scope

Cycles have \(n\) distinct vertices, \(n\ge7\), and the graph is the ordinary simple second power of the cycle. The total-domination requirement uses open neighborhoods, not closed neighborhoods. The exchange operation removes one element of a minimum set and inserts one formerly unselected vertex; simultaneous multiple changes are excluded. The formula is valid for every integer \(n\ge7\); the two reconfiguration classifications apply to the explicitly stated residue classes and no classification is claimed here for the other five classes.

## Proof

**Cyclic-gap criterion.** List a nonempty selected set in cyclic order as \(s_1,\ldots,s_t\), and let \(d_i\) be the positive clockwise distance from \(s_i\) to \(s_{i+1}\), indices modulo \(t\); hence \(\sum_i d_i=n\). For any vertex strictly between consecutive selected vertices, the closest selected vertex on either side is at most two edges along the original cycle exactly when the intervening gap is at most five. If a gap is at least six, its middle contains an unselected vertex of cyclic distance at least three from every selected vertex. Every selected vertex \(s_i\) itself has a selected neighbor in \(G_n\) exactly when \(d_{i-1}\le2\) or \(d_i\le2\). Thus \(S\) totally dominates if and only if \(1\le d_i\le5\) for every \(i\) and no two consecutive gaps belong to \(\{3,4,5\}\). The criterion also handles the cyclic junction.

**Sharp cardinality bound.** Call a gap long if its length is at least three. There are at most \(\lfloor t/2\rfloor\) long gaps; all others have length at most two. Consequently
\[
n\le 5\lfloor t/2\rfloor+2\lceil t/2\rceil
=2t+3\lfloor t/2\rfloor.
\]
For \(n=7k\), the bound excludes \(t\le 2k-1\). For \(n=7k+1\) or \(7k+2\), it excludes \(t\le2k\). For \(n=7k+r\) with \(3\le r\le6\), it excludes \(t\le2k+1\). Equality with each asserted minimum is witnessed by the cyclic gap words
\[
\begin{array}{c|c}r&\text{gap word}\\\hline
0&(2,5)^k\\
1&(2,5)^k,1\\
2&(2,5)^k,2\\
3&(2,5)^k,1,2\\
4&(2,5)^k,2,2\\
5&(2,5)^k,2,3\\
6&(2,5)^k,2,4
\end{array}
\]
(all taken cyclically). Every word satisfies the gap criterion, proving the formula.

**Equality when \(n=7k\).** Here \(t=2k\) and the gap bound is attained. It forces precisely \(k\) long gaps of length five and \(k\) short gaps of length two, alternating. The cyclic pattern has period seven in vertex positions, so its translations produce exactly seven distinct minimum sets. If \(k\ge2\), deleting any selected vertex merges a consecutive pair of gaps into a gap of length seven. To stay in the equality class, the newly inserted vertex must split this length-seven interval into gaps two and five, reversing their order; the unreversed split restores the old vertex. Reversing them instead makes two adjacent length-five gaps in the surrounding alternating word, violating the cyclic-gap criterion. Thus no nontrivial one-exchange is possible, giving \(7K_1\). If \(k=1\), there are only two selected vertices, every optimum is a pair at clockwise separation two, and each pair shares one vertex with precisely two other optimum pairs; the exchange graph is \(C_7\).

**Equality when \(n=7k+2\).** Here \(t=2k+1\) and the gap bound is attained. Exactly \(k\) gaps have length five and \(k+1\) have length two; the long gaps are never adjacent, and there is exactly one pair of consecutive short gaps. Hence the cyclic gap word is, up to rotation, \((2,5)^k,2\), with a unique distinguished pair of consecutive twos. Choosing the location of that pair gives precisely \(n\) distinct translates. Any nontrivial one-vertex replacement must split the merged adjacent old gaps into new lengths two and five; removal at the unique pair of twos instead gives a merged interval of length four, whose only \((2,2)\) split restores the removed vertex. All other removals merge a \((2,5)\) or \((5,2)\) pair to seven. Splitting seven with the reversed order creates adjacent long gaps except at the two boundaries of the unique short-short pair. These two legal reversals transform the configuration to its vertex translations by plus or minus seven, respectively, and no other exchanges exist. The resulting exchange graph has edges \(a\sim a\pm7\) modulo \(n\). Since \(\gcd(7,7k+2)=1\), this is a single cycle of length \(n\).

## Verification

The included standalone `verify.py` independently constructs open neighborhoods of every squared-cycle vertex, tests all candidate subsets of cardinality below or equal to the stated minimum for every \(7\le n\le23\), and compares the neighborhood-based result against an independent cyclic-gap implementation. It also constructs the complete optimal exchange graphs and checks all asserted frozen and cyclic cases, including the exact \(\pm7\) exchange rule. This finite check corroborates, but does not replace, the proof for arbitrary \(n\).

## Relationship to prior work

The 2014 paper of Premala and Sekar investigates exactly the same squared-cycle total-domination polynomial. Its Theorem 3.2(vi) explicitly states that there are seven minimum sets of size \(2k\) at order \(7k\), a result acknowledged here. Its Lemma 2.1, by contrast, states a five-periodic minimum formula that predicts five at order seventeen. The cyclic-gap lower bound excludes every five-vertex total dominator at order seventeen, and an explicit six-vertex construction exists. The present exact minimum formula therefore cannot be deduced from that lemma. Wongsriya and Trakultraipruk (2017) introduce and classify the identical one-token-exchange notion for **ordinary** paths and cycles, but not their second powers. Their work makes the exchange question natural, without implying the frozen-to-cyclic dichotomy in the powered graphs. Henning and Yeo (2011) provide foundational total-domination context rather than a classification of these minimum configurations.

## Limitations

The novelty comparison cannot exclude an earlier equivalent statement under different terminology or in unavailable work. No exchange classification is asserted for orders outside the two specified congruence classes. The minimum counts at multiples of seven are prior work, not independent novelty. The finite verifier is not an exhaustive proof for all orders. No independent external audit has been conducted.

## References

1. M. A. Henning and A. Yeo, *Girth and Total Domination in Graphs*, Graphs and Combinatorics 28 (2012), 199–214; first online February 25, 2011. https://doi.org/10.1007/s00373-011-1033-2
2. T. Premala and C. Sekar, *Total Dominating Sets and Total Domination Polynomials of Square of Cycles*, IOSR Journal of Mathematics 10(4), Version V (July–August 2014), 78–85. https://iosrjournals.org/iosr-jm/papers/Vol10-issue4/Version-5/M010457885.pdf
3. A. Wongsriya and N. Trakultraipruk, *γ-total dominating graphs of paths and cycles*, ScienceAsia 43 (2017), 326–333. https://doi.org/10.2306/scienceasia1513-1874.2017.43.326
