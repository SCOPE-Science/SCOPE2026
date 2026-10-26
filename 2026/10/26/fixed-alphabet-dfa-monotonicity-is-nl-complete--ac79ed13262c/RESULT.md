# Fixed-alphabet DFA monotonicity is NL-complete

## Finding

For every fixed integer \(k\ge 1\), let \(\Gamma_k=\mathcal P(\{p_1,\ldots,p_k\})\), ordered by subset inclusion. For a language \(L\subseteq\Gamma_k^*\), call \(L\) monotone when, for all words \(u,v\) of the same length, \(u_i\subseteq v_i\) at every position and \(u\in L\) imply \(v\in L\). Given a DFA over the fixed alphabet \(\Gamma_k\), deciding whether its language is monotone is \(\mathrm{NL}\)-complete under logspace many-one reductions. In particular, one unary predicate already suffices. When \(k=0\), the alphabet has one letter and every language is monotone.

## Assumptions and scope

The input is a complete deterministic finite automaton with its transition table explicit. The integer \(k\) is fixed, not part of the input; the main lower bound already applies to \(k=1\), where the alphabet is \(\{\emptyset,\{p\}\}\) and \(\emptyset\subsetneq\{p\}\). The word order is positionwise and preserves length. This is not a claim about NFA input, positive definability, or the complexity of computing a minimal DFA.

## Proof

**Upper bound.**

Let \(\mathcal A=(Q,\Gamma_k,\delta,q_0,F)\) recognize \(L\). Construct an NFA \(\mathcal A^{\uparrow}\) on the same states by adding, for each transition \(q\xrightarrow{S}q'\) of \(\mathcal A\), a transition \(q\xrightarrow{T}q'\) for every \(T\supseteq S\). It recognizes the upward closure
\[
L^{\uparrow}=\{v:\exists u\in L,\ |u|=|v|,\ u_i\subseteq v_i\text{ for every }i\}.
\]
Thus \(L\) is monotone exactly when \(L^{\uparrow}\setminus L=\varnothing\). Complementing the DFA and taking its product with \(\mathcal A^{\uparrow}\) reduces non-monotonicity to NFA emptiness, which is in \(\mathrm{NL}\). Since \(\mathrm{NL}=\mathrm{coNL}\), monotonicity is in \(\mathrm{NL}\).

**Lower bound over a fixed binary alphabet.**

DFA emptiness remains \(\mathrm{NL}\)-complete when the initial state is nonaccepting, so the empty word is not accepted. Let \(\mathcal B=(Q,A,\delta,q_0,F)\) be such an instance, with \(A=\{a_1,\ldots,a_s\}\). Put \(m=\max(2,s)\). Over the one-predicate alphabet \(\{\emptyset,\{p_1\}\}\), encode \(a_i\) by the length-\(m\) block whose \(i\)-th letter is \(\{p_1\}\) and whose other letters are \(\emptyset\). Extend this fixed-length code homomorphically to words.

Construct a complete DFA \(\mathcal C\) that accepts exactly the coded words from \(L(\mathcal B)\): it parses blocks of length \(m\), requires exactly one \(\{p_1\}\) at a position \(i\le s\) in each block, remembers that position, and updates the simulated state of \(\mathcal B\) at the block boundary. Malformed blocks go to a rejecting sink; only block-boundary states corresponding to final states of \(\mathcal B\) are accepting. The construction has \(O(|Q|m^2)\) states and is computable in logarithmic space.

If \(L(\mathcal B)=\varnothing\), then \(L(\mathcal C)=\varnothing\), which is monotone. If \(L(\mathcal B)\ne\varnothing\), choose a nonempty accepted word \(w\) and let \(x\) be its code. Each block has at least one \(\emptyset\), because \(m\ge2\). Change one such letter to \(\{p_1\}\), obtaining \(y\) with \(x_i\subseteq y_i\) at every position. The altered block now contains two occurrences of \(\{p_1\}\), so it is malformed and \(y\notin L(\mathcal C)\), although \(x\in L(\mathcal C)\). Hence \(L(\mathcal C)\) is not monotone. We have \(L(\mathcal B)=\varnothing\) if and only if \(L(\mathcal C)\) is monotone, proving \(\mathrm{NL}\)-hardness for one predicate.

For any fixed \(k>1\), use the same construction and send every alphabet letter other than \(\emptyset\) and \(\{p_1\}\) to the rejecting sink. The same argument proves hardness for each fixed \(k\ge1\). Finally, if \(k=0\), then \(\Gamma_0=\{\emptyset\}\); two equal-length words are identical, so every language is monotone.

## Verification

The upper-bound reduction is an explicit product-automaton emptiness test. The lower-bound map is an explicit polynomial-size, logspace construction, and its two cases prove the required equivalence exactly. The proof is symbolic; finite tests are not used as evidence for the infinite family of input automata. The claim is restricted to DFA input over a fixed nontrivial powerset alphabet.

## Relationship to prior work

Kuperberg and Moreau prove that monotonicity testing for DFA-presented regular languages is \(\mathrm{NL}\)-complete when the alphabet is allowed to vary with the input. Their lower-bound construction adds a new top letter above the input alphabet. The fixed-binary statement here is a refinement: the one-hot block encoding removes the input-dependent alphabet while preserving the emptiness equivalence. The result does not claim a new classification for NFA input, for which prior work gives a different complexity bound.

## Limitations

The reduction establishes complexity under logspace many-one reductions and an explicit transition-table encoding. It does not settle complexity for succinct automata, does not characterize the positive-first-order definability problem, and does not establish priority against unindexed literature. The case \(k=0\) is trivial; the first nontrivial fixed vocabulary is \(k=1\).

## References

1. D. Kuperberg and Q. Moreau, “Positive and monotone fragments of FO and LTL,” arXiv:2406.17693, first posted 25 June 2024. See the definition of monotonicity, Proposition 4.5, and Appendix B.3. https://arxiv.org/abs/2406.17693
2. D. Kuperberg, “Positive First-order Logic on Words and Graphs,” *Logical Methods in Computer Science* 19(3), 2023. https://doi.org/10.46298/lmcs-19(3:7)2023
