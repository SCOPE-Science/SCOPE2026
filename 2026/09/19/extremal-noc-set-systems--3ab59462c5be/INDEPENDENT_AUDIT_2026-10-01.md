# Independent mathematical audit — SCOPE-20260919-3ab59462c5be

Final disposition: **PASS**.

## Correctness
**PASS** — The equality proof reconstructs cleanly from the NOC definition and the source's levelwise bound. Total equality forces \(|\mathfrak C_k|=n-k+1\) at every size. Equality in the private-witness injection makes each level a full sunflower \(\{Y_k\cup\{x\}:x
otin Y_k\}\) with \(|Y_k|=k-1\). For a petal witness \(x\), the NOC condition makes every set containing \(x\) comparable with its level-\(k\) set; applying this to the next saturated level forces \(Y_k\subset Y_{k+1}\). Thus the cores form a strict chain and yield exactly the ordered construction. The converse witness check is immediate. The chain determines the first \(n-2\) labels and leaves only the final two interchangeable, giving \(n!/2\). The Hasse-cover count is \(2\sum_{k=1}^{n-1}(n-k)=n(n-1)\), and exactly the \(n-2\) nonterminal prefix vertices have indegree at least two.

## Originality
**PASS** — The complete Lindeberg-Hellmuth primary preprint was inspected in the portions containing the NOC definition, Lemma 5, and the network corollaries. Lemma 5 proves the sharp \(n(n+1)/2\) bound and gives the ordered family as one sharpness example, but it does not classify all equality cases or give the \(n!/2\) count. Resultary searches under NOC, inclusion visibility, strict compatibility, nested sunflower, and network terminology found the assigned result but no earlier theorem implying the nested-core equality classification. Older private-element set-system literature remains a best-of-knowledge risk.

### Equivalent formulations
Aliases and the network translation were checked; no equivalent equality-classification theorem was found.

### Broader coverage
The inspected broader structural results do not mechanically imply nested cores across all saturated levels.

### Exact database or table
Search absence is only supporting evidence; originality rests on the statement-level comparison with the full primary source.

### Claim versus prior implication
The final theorem is not a stated corollary of the source and requires a genuine equality analysis across levels.

## Value
**PASS** — A complete equality classification for a freshly sharp extremal bound is a natural structural problem. The theorem upgrades a bound-plus-example to rigidity, counts every labeled extremizer, and translates that rigidity into exact Hasse arc and reticulation counts for the canonical network classes. This is a motivated complete classification rather than an arbitrary finite slice.

## Source inspections
- **NOC NOC, who's there? Clustering systems of tree-child and normal networks** (https://arxiv.org/abs/2609.13336v1): full primary HTML through the NOC definition, Lemma 5 sharp bound/proof, and network corollaries. Assessment: NOT_COVERING_EQUALITY_CLASSIFICATION. Evidence: Lemma 5 proves the \(n(n+1)/2\) bound and displays one sharpness construction; the inspected text does not classify all maximizers or state the \(n!/2\) count.

## Residual risks
- Older extremal set-system literature using 'private element' or related terminology was not exhaustively searchable.
- Very recent parallel work may be unindexed; the originality judgment is best-of-knowledge.
