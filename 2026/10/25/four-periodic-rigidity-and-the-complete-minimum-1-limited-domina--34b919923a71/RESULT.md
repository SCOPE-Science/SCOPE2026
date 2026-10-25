# Four-periodic rigidity and the complete minimum 1-limited domination census of Möbius ladders

## Finding

For each integer \(n\ge3\), let \(M_{2n}\) be the finite simple cubic Möbius ladder with vertex set \(\{0,1,\ldots,2n-1\}\), cycle edges between consecutive residues modulo \(2n\), and antipodal edges \(\{i,i+n\}\) for \(0\le i<n\). A *1-limited dominating set* \(D\) dominates every vertex outside \(D\) and has at most one neighbor outside \(D\) at each vertex inside \(D\). Let \(\gamma_1^{\mathrm L}(M_{2n})\) be its minimum size and let \(N_n\) count distinct minimum sets on these fixed labelled vertices. Then

\[
\gamma_1^{\mathrm L}(M_{2n})=\begin{cases}n,&n\equiv0\pmod4,\\n+1,&n\not\equiv0\pmod4,\end{cases}\qquad
N_n=\begin{cases}4,&n\equiv0\pmod4,\\2n,&n\equiv2\pmod4,\\3n,&n\equiv1,3\pmod4.\end{cases}
\]

Every minimum set is described explicitly by the rung words below; there are no others. This resolves both the sharp domination number and the labelled minimum-set census for the complete family, rather than only providing example constructions.

## Assumptions and scope

Identify rung \(i\) (\(0\le i<n\)) with the pair \(\{i,i+n\}\), called its *top* and *bottom* vertices. Encode membership in \(D\) by a word \(s_0\ldots s_{n-1}\) over \(\{0,1,2,3\}\): \(0\) selects neither rung vertex, \(1\) selects top only, \(2\) selects bottom only, and \(3\) selects both. Neighboring rungs have same-row edges for indices \(i,i+1\) with \(i<n-1\); the seam between rungs \(n-1\) and \(0\) *switches* top and bottom. All shifts and words mentioned below refer to these fixed rung indices; the cyclic shift of a word with only symbols \(0,3\) is unambiguous because switching sides changes neither letter.

The complete classification is:

1. **\(n\equiv0\pmod4\)**: the four cyclic shifts of the length-\(n\) word \((0033)^{n/4}\), where the exponent denotes word repetition. These are all minimum sets, each of size \(n\).
2. **\(n\not\equiv0\pmod4\), first family**: for every integer \(0\le j<n\), the two words \(1^j3\,2^{n-j-1}\) and \(2^j3\,1^{n-j-1}\). These give exactly \(2n\) distinct minimum sets of size \(n+1\).
3. **\(n\equiv1\pmod4\), additional family**: for \(n=4r+1\) with \(r\ge1\), all \(n\) cyclic shifts of \(00\,333\,(00\,33)^{r-1}\).
4. **\(n\equiv3\pmod4\), additional family**: for \(n=4r+3\) with \(r\ge0\), all \(n\) cyclic shifts of \(0\,33\,(00\,33)^r\).

In items 3 and 4, the words have exactly \(n+1\) selected vertices. In particular, all counts regard actual subsets of the fixed, vertex-labelled graph: no rotation or reflection is identified as equivalent.

## Proof

**1. General lower bound.** Write \(S=V(M_{2n})\setminus D\). Every vertex of \(S\) has at least one neighbor in \(D\), while every vertex of \(D\) has at most one neighbor in \(S\). Counting crossing edges both ways gives \(2n-|D|\le |E(D,S)|\le |D|\), and hence \(|D|\ge n\). This standard general bound is recalled here to fix normalization; it is not claimed as new.

**2. Local restrictions.** Write \(x,y,z\) for the number of rungs with symbols \(0\), \(1\) or \(2\), and \(3\), respectively. Since \(x+y+z=n\), the exact size identity is
\[
|D|=y+2z=n+(z-x).
\]
Thus an optimum at or below \(n+1\) has \(z-x\le1\).

The cubic condition is equivalently that each selected vertex has at least two selected neighbors, and each unselected vertex has at least one selected neighbor. Direct inspection of its three neighbors gives these necessary local rules:

* A \(0\)-rung cannot be adjacent to a singleton rung \(1\) or \(2\). Indeed, that selected singleton already has an unselected rung-mate and would have another unselected horizontal neighbor.
* A run of \(0\)-rungs has length at most two, since either vertex in a middle zero rung with zero neighbors on both sides is undominated.
* A \(3\)-rung adjoining a \(0\)-rung must have a \(3\)-rung on its other side: otherwise the selected vertex on the side absent from a neighboring singleton (or either vertex of another zero rung) lacks two selected neighbors. Equivalently, every run of \(3\)-rungs incident with a zero run has length at least two.
* When two singleton rungs are adjacent across an ordinary, same-row edge, their letters must agree. At the twisted seam their letters must differ. In either case, a mismatched singleton would have neither its rung-mate nor that horizontal neighbor selected and could have at most one selected neighbor overall.

These rules are necessary for every feasible set, including sets much larger than the minimum; the argument below invokes them only for \(|D|\le n+1\).

**3. A zero rung and a singleton cannot coexist near the minimum.** If a feasible word contains both a zero and a singleton, split it at the singleton runs into disjoint maximal blocks of non-singleton symbols. Each block containing zeros begins and ends with at least two \(3\) symbols, and between consecutive zero runs it also has at least two \(3\) symbols. If that block contains \(r\ge1\) zero runs, their combined length is at most \(2r\), whereas its \(3\) count is at least \(2(r+1)\). Other blocks can only increase \(z-x\). Consequently \(z-x\ge2\), contradicting \(|D|\le n+1\). Thus a minimum-size candidate cannot contain both zero and singleton rungs.

**4. Singleton/three words.** If no rung is zero, the size condition becomes \(z\le1\). If \(z=0\), every rung is a singleton: the ordinary adjacency rule forces one constant letter along the whole path of rungs, but the seam requires the *opposite* letter. This is impossible. If \(z=1\), its position cuts the linear path of singleton rungs into two constant blocks. The twisted seam requires opposite singleton letters where both blocks are nonempty, and imposes no further restriction when either block is empty. Therefore the candidate words are precisely
\[
1^j3\,2^{n-j-1},\qquad 2^j3\,1^{n-j-1}\qquad(0\le j<n).
\]
Each satisfies the local 1-limited and domination conditions directly: every singleton vertex has its two requisite selected horizontal neighbors (one of which can lie in the full rung), while the full rung has its vertical neighbor plus an appropriately selected horizontal neighbor on each side of the seam. There are exactly \(2n\) distinct words and their size is \(n+1\).

**5. Zero/three words.** Suppose there are no singletons. An all-zero word fails domination, while an all-three word has size \(2n>n+1\). Otherwise there are \(r\ge1\) runs of zeros alternating cyclically with \(r\) runs of threes. Every zero run has length at most two and every three run has length at least two. Hence \(x\le2r\le z\).

If \(z-x=0\), equality holds throughout: every run has exactly two symbols, so the word is a cyclic shift of \((0033)^{n/4}\) and necessarily \(4\mid n\). There are four distinct shifts.

If \(z-x=1\), the nonnegative integer deficits \(2r-x\) and \(z-2r\) sum to one. Either exactly one zero run has length one while all other zero runs and all three runs have length two (giving \(n=4r-1\)), or exactly one three run has length three while all remaining runs have length two (giving \(n=4r+1\)). These are exactly the odd-order families specified above, with \(n\) distinct shifts because the exceptional run singles out a unique cyclic position. Every displayed zero/three word is feasible: each omitted rung vertex meets a neighboring fully selected rung, and each selected vertex in a full rung has a selected rung-mate plus a selected horizontal neighbor in its run.

**6. Optimality and enumeration.** The four-run pattern exists and reaches size \(n\) when \(4\mid n\). In every other congruence class the singleton/three constructions give size \(n+1\). The lower bound from step 1 excludes smaller sets, while steps 3–5 exclude a size-\(n\) set unless \(4\mid n\) and exhaust all minimizers of the attained size. Finally, the four shifts, \(2n\) singleton/three words, and (for odd \(n\)) \(n\) exceptional zero/three shifts are mutually distinct. This proves both displayed formulas and the complete structural classification for every \(n\ge3\).

## Verification

The accompanying independent Python program `verify.py` constructs the \(2n\)-vertex graph directly from cycle and antipodal edges, tests the local domination conditions vertex by vertex, and uses two separate checks:

* Exhaustive set enumeration for all seven cases \(3\le n\le9\), comparing the exact minimum sets against the closed-form candidate lists, including excluded lower-cardinality competitors.
* A separate four-state rung dynamic program with explicit twist conditions for all 58 cases \(3\le n\le60\), checking both minimum size and number of attaining words. It also explicitly checks every predicted minimum set in the same 58 cases.

Observed exact output: `VERIFY_OK exhaustive_n=3..9 dp_n=3..60 explicit_n=3..60`. These are finite cross-checks; the proof above establishes the unbounded theorem.

## Relationship to prior work

Radić and Tepeh's *On 1-limited and (1,2)-domination in cubic graphs* (arXiv:2610.01796, first posted October 1, 2026) motivates this family-level question and proves complexity results and exact values for Goldberg snarks, not the Möbius-ladder family treated here. Božović, Radić, Kovijanić-Vukićević, and Tepeh established the general half-order lower bound and characterization of equality through matching cut structure in *On k-limited domination in graphs* (arXiv:2606.22422; Corollary 11 in the open-access article). Those general statements are premises, not proposed new results. They do not themselves provide this family's four-periodic boundary or the complete labelled minimum-set census. Related (1,2)-domination work on cubic graphs and Cartesian products studies other graph classes. Möbius ladders are twisted cyclic ladders rather than the Cartesian prisms of the cited product paper; neither the product work nor the Goldberg-snark theorem states this optimizer census.

## Limitations

The classification uses the exact cubic \(1\)-limited rule and the standard simple Möbius ladder for integer \(n\ge3\). It does not yield results for arbitrary cubic graphs, different domination capacities, or near-minimum sets of size greater than the minimum. Independent mathematical assessment and a comprehensive historical-priority search have not been performed; pre-2026 work on matching cuts, cubic circulants, or (1,2)-domination may bear on priority. The finite program corroborates but does not replace the universal proof.

## References

1. G. Radić and A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796, initial public submission 2026-10-01. https://arxiv.org/abs/2610.01796
2. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, and A. Tepeh, *On k-limited domination in graphs*, arXiv:2606.22422, initial public submission 2026-06-21; open-access journal article https://doi.org/10.1007/s40314-026-03902-2
3. A. Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428, initial public submission 2026-06-21. https://arxiv.org/abs/2606.22428
4. M. Fakharan and coauthors, *On (1,2)-domination in cubic graphs*, Discrete Mathematics 344 (2021), article 112546. A full primary-text priority comparison with this older article remains unperformed.
