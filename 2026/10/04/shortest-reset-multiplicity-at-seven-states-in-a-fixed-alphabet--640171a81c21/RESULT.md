# Shortest-reset multiplicity at seven states in a fixed-alphabet construction
## Finding
For the seven-state de Bondt--Don--Zantema Theorem 3 construction, the three-letter restriction \(A^{-cd}\) on \(\{a,b,e\}\) has exactly \(1{,}327{,}104\) shortest synchronizing words, all of length \(32\); exactly \(663{,}552\) reset to state \(3\) and \(663{,}552\) to state \(4\). Its two-letter restriction \(A^{-bcd}\) on \(\{a,e\}\) has exactly \(331{,}776\) shortest synchronizing words, all of length \(32\) and all resetting to state \(4\). Thus adding \(b\) preserves the reset threshold and multiplies the number of shortest reset words by exactly \(4\).

## Assumptions and scope
Let \(Q=\{1,2,3,4,5,6,7\}\). We use the seven-state specialization of the construction in Theorem 3 of de Bondt--Don--Zantema. Its relevant letters act by
\[
a=(2,3,4,5,6,7,1),\qquad
b=(1,3,3,4,5,6,7),\qquad
e=(3,4,4,5,6,7,1),
\]
where each tuple lists the images of states \(1,\ldots,7\). The automaton \(A^{-cd}\) retains \(a,b,e\), while \(A^{-bcd}\) retains only \(a,e\). A synchronizing word maps all of \(Q\) to a singleton. The claim is finite and only concerns these two seven-state automata; it asserts no formula for other state counts.

## Proof
For either alphabet, consider the deterministic power automaton whose vertices are nonempty subsets of \(Q\) and whose letter action is direct image. Breadth-first search from \(Q\) explores subset states in nondecreasing word length. Assign the start subset count \(1\). Whenever a transition from a subset at distance \(d\) reaches a subset first seen at distance \(d+1\), copy the path count; whenever it reaches a subset already known at distance \(d+1\), add the path count. By induction on \(d\), the stored count at each subset is exactly the number of words of length \(d\) taking \(Q\) to that subset. Consequently, the first singleton layer gives the exact reset threshold, and the singleton counts in that layer give the exact number of shortest reset words, separated by target state.

The exhaustive computation gives first singleton distance \(32\) for both alphabets. For \(\{a,e\}\), the only singleton on that layer is \(\{4\}\), with path count \(331{,}776\). For \(\{a,b,e\}\), the singleton counts are \(663{,}552\) at \(\{3\}\) and \(663{,}552\) at \(\{4\}\), totaling \(1{,}327{,}104\). The ratio is therefore exactly \(4\).

This finite exhaustive proof is consistent with the published threshold theorem: at \(n=7\), the source formula \(n^2-3n+4\) equals \(32\), and the published witness \((ea^{n-2})^{n-2}ae\) specializes to a synchronizing word of length \(32\).

## Verification
Run `python3 artifacts/verify.py`. The verifier constructs the transition maps from the displayed seven-state table, performs the complete subset-state breadth-first recurrences for both alphabets, checks the exact first-singleton layer and target-resolved counts, replays the published witness, and prints `VERIFY_OK`. Its recorded output is in `artifacts/verification_output.json`.

The verifier reaches \(121\) subsets for the two-letter automaton and \(122\) subsets for the three-letter automaton. Because the underlying power sets are finite and every outgoing letter transition from every dequeued pre-threshold subset is processed, this is an exhaustive finite argument rather than sampling.

## Relationship to prior work
De Bondt, Don, and Zantema define this family and prove that \(A^{-cd}\) has shortest synchronizing-word length \(n^2-3n+4\); they also note that the two-letter restriction \(A^{-bcd}\) has the same threshold. Their paper studies how alphabet size can change synchronizing behavior, and its exhaustive global DFA census covers state counts only through \(n=6\). The source gives the threshold and explicit witnesses, but it does not give the number of shortest reset words for the seven-state members above.

The present result therefore refines the same-threshold comparison at the first state count beyond that census: adding \(b\) leaves the optimum length unchanged while increasing the multiplicity of optimal reset words by the exact factor \(4\), and it creates shortest resets to an additional target state.

## Limitations
The result is only an exact finite statement at \(n=7\). It does not establish a multiplicity formula for the infinite family, does not classify shortest words syntactically, and does not claim that no other publication outside the searched and inspected literature has independently enumerated these words. The computation uses exact integer path counts; no probabilistic or floating-point step is involved.

## References
1. M. de Bondt, H. Don, H. Zantema, “Slowly synchronizing automata with fixed alphabet size,” arXiv:1609.06853, first submitted 2016-09-22. Theorem 3 gives the construction and the \(n^2-3n+4\) threshold.
2. H. Don, H. Zantema, M. de Bondt, “Slowly synchronizing automata with fixed alphabet size,” *Information and Computation* 279 (2021), 104614, DOI 10.1016/j.ic.2020.104614.
