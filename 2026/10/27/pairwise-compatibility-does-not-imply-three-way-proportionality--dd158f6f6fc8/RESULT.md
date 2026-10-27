# Pairwise compatibility does not imply three-way proportionality in ranking compression

## Finding

There is an input profile of six strict rankings of five candidates for which every pair among **positional proportionality**, **pairwise proportionality**, and **proportionality for solid coalitions** (PSC) can be attained by three output rankings, but no three-output multiset attains all three simultaneously. Output rankings may be arbitrary permutations, may repeat, and need not appear among the inputs.

Moreover, the same incompatibility, with pairwise compatibility retained, occurs for **every** number of input voters of the form \(n=6r\), \(r\in\mathbb{Z}_{\ge1}\), every number of candidates \(m\ge5\), and target output size \(k=3\). These are explicit instances, not assertions that every profile at these parameters is incompatible.

For the base instance, among the \(\binom{122}{3}=295240\) unordered multisets of three output permutations, exactly \(5\) satisfy positional and pairwise proportionality, exactly \(44\) satisfy positional proportionality and PSC, and exactly \(6\) satisfy pairwise proportionality and PSC. None satisfies the conjunction of all three.

## Assumptions and scope

Write \(a\succ_{\pi} b\) when ranking \(\pi\) places \(a\) before \(b\), and \(\operatorname{Top}_{\ell}(\pi)\) for the unordered set of its first \(\ell\) candidates. A profile consists of \(n\) strict total orders over the same \(m\) candidates; the output is a multiset of \(k\) strict total orders, with \(1\le k\le n\).

For an event \(E\) about a ranking, let \(s(E)\) be its number of occurrences in the input and \(h(E)\) its number of occurrences in the output. The three axioms require \(h(E)\ge\lfloor ks(E)/n\rfloor\) for every event of the appropriate kind:

- **Positional:** candidate \(a\) lies in its ranking's top \(\ell\) positions, for each candidate and \(1\le\ell\le m\).
- **Pairwise:** \(a\succ b\), for every ordered pair of distinct candidates.
- **PSC:** \(\operatorname{Top}_{|S|}(\pi)=S\), for each nonempty candidate subset \(S\).

These formulas are equivalent to the integer-threshold definitions requiring at least \(t\) outputs whenever at least \(tn/k\) inputs satisfy the event.

For the base instance, use candidate labels \(1,2,3,4,5\), with input rankings

\[
\begin{array}{lll}
(2,5,1,4,3),&(5,3,1,2,4),&(2,4,1,5,3),\\
(2,3,1,5,4),&(2,5,3,4,1),&(3,2,4,5,1).
\end{array}
\]

## Proof

**Pairwise compatibility.** The following three outputs, read as multisets of rankings, are explicit witnesses. Directly counting every top-position, ordered-pair, and exact-prefix-set event verifies the indicated two axioms:

| Axioms attained | Three output rankings |
|---|---|
| Positional + pairwise | \((2,1,4,5,3)\), \((2,3,5,4,1)\), \((5,3,1,2,4)\) |
| Positional + PSC | \((1,2,3,5,4)\), \((2,3,4,5,1)\), \((2,5,1,4,3)\) |
| Pairwise + PSC | \((2,1,4,5,3)\), \((2,5,3,1,4)\), \((3,2,5,4,1)\) |

**Three-way obstruction.** The definitions applied to the six input rankings yield the following eleven necessary requirements. An input support of \(2\), \(4\), or \(6\) induces the respective output lower quota \(1\), \(2\), or \(3\), because \(k/n=1/2\).

| Event | Input support | Required output support |
|---|---:|---:|
| Top-two set is \(\{2,5\}\) (PSC) | 2 | 1 |
| Top-two set is \(\{2,3\}\) (PSC) | 2 | 1 |
| \(5\) is in the top four (positional) | 6 | 3 |
| \(1\) is in the top three (positional) | 4 | 2 |
| \(3\) is in the top three (positional) | 4 | 2 |
| \(2\succ4\) (pairwise) | 6 | 3 |
| \(5\succ3\) (pairwise) | 4 | 2 |
| \(3\succ1\) (pairwise) | 4 | 2 |
| \(5\succ1\) (pairwise) | 4 | 2 |
| \(4\succ5\) (pairwise) | 2 | 1 |
| \(1\succ5\) (pairwise) | 2 | 1 |

Suppose three output rankings satisfy all eleven requirements. Name the ranking whose top-two set is \(\{2,5\}\) by \(A\), and the ranking whose top-two set is \(\{2,3\}\) by \(B\). They are different. Name the third \(C\). Since \(A\) has \(5\succ3\) and \(B\) has \(3\succ5\), the quota for \(5\succ3\) forces \(C\) to have \(5\succ3\). Also, all three must place \(2\) before \(4\), and none may place \(5\) last.

We first show that the third candidate of \(A\) is \(1\). Otherwise \(A\) has \(1\) outside its top three, so the two-occurrence top-three quota for \(1\) forces both \(B\) and \(C\) to put \(1\) in their top three. Because \(B\) begins with \(2,3\) in some order, its third candidate must then be \(1\). Since \(5\) cannot be last, its remaining candidates are \(5\) fourth and \(4\) fifth. Thus \(B\) has \(1\succ5\) and \(5\succ4\). In \(A\), both \(5\succ1\) and \(5\succ4\) hold. The quotas for \(5\succ1\) and \(4\succ5\) consequently force \(C\) to satisfy \(5\succ1\) and \(4\succ5\), respectively. Along with \(2\succ4\), this gives \(2\succ4\succ5\succ1\) in \(C\), contradicting the required top-three placement of \(1\) in \(C\). Hence \(A\)'s third candidate is indeed \(1\).

Now \(A\)'s top three contain \(2,5,1\), so \(3\) lies outside them. Because \(B\) has \(3\) in its top two, the two-occurrence top-three quota for \(3\) forces \(C\) to put \(3\) in its top three. If \(B\)'s third candidate were \(1\), the top-four condition on \(5\) would again give \(B\)'s final two candidates as \(5,4\). If \(B\)'s third candidate were \(5\), it would also have \(5\succ4\). Either way both \(A\) and \(B\) would have \(5\succ4\), requiring \(C\) to have \(4\succ5\). But then \(C\) would have \(2\succ4\succ5\succ3\), placing \(3\) no higher than fourth, a contradiction. Therefore \(B\)'s third candidate is \(4\), followed by \(5\) fourth and \(1\) fifth.

The top-three quota for \(1\) now forces \(C\) to place \(1\) in its top three (\(A\) does, but \(B\) does not). Because \(A\) has \(1\succ3\) and \(B\) has \(3\succ1\), the quota for \(3\succ1\) forces \(C\) to have \(3\succ1\). Coupled with its already-forced \(5\succ3\), this gives \(5\succ3\succ1\). Therefore the first three positions of \(C\) must be \((5,3,1)\), and \(2\succ4\) forces \(C=(5,3,1,2,4)\).

But now \(5\succ1\) holds in all three outputs: in \(A\) because \(5\) is top-two and \(1\) third, in \(B\) because \(5\) is fourth and \(1\) fifth, and in \(C\) because \(5\) is first and \(1\) third. The final requirement demands at least one output with \(1\succ5\), a contradiction. Thus the three axioms are not jointly satisfiable.

**Infinite extensions.** For any integer \(r\ge1\), repeat each of the six input rankings exactly \(r\) times. The ratio \(ks(E)/n\) remains unchanged for every event, so the same three-output witnesses satisfy each pair, and the same eleven-condition contradiction prohibits all three. To increase the number of candidates to any \(m\ge5\), append the same additional candidates in a fixed common order below candidate \(1\)–\(5\) in every input ranking and each pairwise witness. This preserves each pair of axioms: original-candidate comparisons and top-prefix events remain as before, while all new nonzero prefix or comparison quotas involving appended candidates are unanimous in the extended witnesses. If a jointly satisfying output existed for the enlarged candidate set, deleting all appended candidates from each output ranking would preserve all eleven original necessary conditions (deletion can only improve original top-position membership and preserves original pairwise comparisons and the demanded exact top-two sets), contradicting the base obstruction.

**Exact pairwise counts.** There are \(5!=120\) possible strict output rankings. Every multiset of three is represented exactly once by a nondecreasing triple of their indices. Computing the three axiom predicates for each of the \(\binom{122}{3}=295240\) multisets yields the pairwise counts \(5\), \(44\), and \(6\) stated above and joint count zero. The supplied standalone program implements and verifies this exhaustive finite count.

## Verification

Run `python3 check_rankings.py` from the same directory as this document. The program uses only the Python standard library. It independently checks every displayed witness against the original quantified axiom definitions; derives all event quotas; traverses all \(295240\) unordered output multisets without symmetry exclusions beyond ordering the three chosen permutations; verifies the eleven input support counts; and tests several replicated and padded instances. Expected pairwise counts, in the order positional+pairwise, positional+PSC, pairwise+PSC, are \(5,44,6\). The mathematical impossibility and infinite-extension arguments above do not rely on finite sampling.

## Relationship to prior work

Halpern, Liu, Micha, Ng, and Suksompong (2026) introduced these precise ranking-compression axioms. They prove that positional proportionality and PSC each always admit an output, show that pairwise proportionality can fail by itself on sufficiently large candidate sets, and obtain simultaneous guarantees for structured single-peaked input profiles. They do not state the present **pairwise-feasible but triple-infeasible** profile or its replicated/padded family. Their pairwise-impossibility instances do not imply the new separation: this profile permits pairwise proportionality, and indeed permits each of the three *pairs* of axioms. Their output-from-input counterexamples also impose a restriction absent here.

Lederer (2025) studies proportionality for a **single** aggregated output ranking under a different fairness formulation. Those guarantees do not determine the integer three-ranking compatibility problem considered here. Related committee voting work on PSC selects alternatives rather than a multiset of complete rankings.

## Limitations

This theorem is an explicit compatibility obstruction, not a complete classification of compatible profiles or a claim that five candidates or six voters are globally minimal. The exact counts refer only to the displayed base profile. The extension fixes the number of output rankings at three. No distributional or algorithmic hardness conclusion follows. Priority with respect to unpublished or unindexed work has not been independently established.

## References

1. Daniel Halpern, Xinyu Liu, Evi Micha, Yu Peng Ng, and Warut Suksompong, *Proportionality in Ranking Compression*, arXiv:2610.23193, first submitted 2026-10-16. https://arxiv.org/html/2610.23193v1
2. Patrick Lederer, *Proportional Representation in Rank Aggregation*, arXiv:2508.16177, first submitted 2025-08-22. https://arxiv.org/abs/2508.16177
3. Haris Aziz, Patrick Lederer, Dominik Peters, Jannik Peters, and Angus Ritossa, *Committee Monotonicity and Proportional Representation for Ranked Preferences*, arXiv:2406.19689, 2024. https://arxiv.org/abs/2406.19689
