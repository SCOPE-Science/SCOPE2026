# Binary witnesses for every strict level of adversarial synchronization

## Finding
For every integer \(n\geq3\), define the complete deterministic automaton \(B_n\) with state set \(Q_n=\{0,1,\ldots,n-1\}\), binary alphabet \(\{b,c\}\), and transformations
\[
 i\mathbin{\cdot}b=i+1\pmod n,\qquad
 i\mathbin{\cdot}c=\begin{cases}0,&i=0,\\1,&i\ne0.\end{cases}
\]
In the adversarial \(k\)-synchronization game, Alice selects one letter on each turn and Bob may respond with any word of length strictly less than \(k\), including the empty word. Alice wins if the combined word maps all states to one state. Denote the class of automata on which Alice can force this by \(\mathcal A_k\).

**Theorem.** For every \(n\geq3\) and integer \(k\geq1\),
\[
 B_n\in\mathcal A_k\quad\Longleftrightarrow\quad k\leq n-2.
\]
Whenever \(k\leq n-2\), Alice can force synchronization in at most three of her moves, and Bob can prevent her from winning in fewer than three. The ordinary shortest reset-word length of \(B_n\) is exactly three.

**Consequences.** Every inclusion \(\mathcal A_k\supsetneq\mathcal A_{k+1}\) remains strict among binary-alphabet complete deterministic automata, as witnessed by \(B_{k+2}\). For unary automata all the levels coincide with ordinary synchronizability. Thus two is the smallest alphabet size admitting a strict hierarchy at every positive level.

## Assumptions and scope
The integer \(n\) is at least three. Words act from left to right on sets of states; \(S\mathbin{\cdot}w\) denotes the image of \(S\) under the word \(w\). The initial set is \(Q_n\). Alice moves first; after each Alice letter Bob chooses a word of length \(0\) through \(k-1\), and synchronization is permanent. The winning condition is eventual synchronization against every legal Bob strategy, with perfect information. A winner is determined even if the play lasts arbitrarily long. The theorem concerns this particular binary family and the alphabet-size consequence, not minimum state counts among all witnesses.

## Proof
**1. Elementary two-state property.** Applying \(c\) to any state set containing at least two states produces a subset of \(\{0,1\}\). On a two-element set, \(c\) collapses the pair precisely when the set does *not* contain state \(0\): when it contains \(0\), it maps to \(\{0,1\}\); when neither state is zero, both are sent to \(1\). The letter \(b\) acts as a permutation.

**2. Alice wins when \(k\leq n-2\).** Fix any Bob strategy; every Bob response has length at most \(n-3\). Alice first plays \(c\), reducing the initial position to \(\{0,1\}\). Consider Bob's response \(w\). If it ever contains a \(c\) after a positive run of \(b\)'s while the two tracked states are distinct, then this \(c\) collapses them: starting from \(\{0,1\}\), a positive run of at most \(n-3\) letters \(b\) sends the pair to \(\{t,t+1\}\) with \(1\leq t\leq n-3\), which excludes zero. Likewise any such \(c\) following an earlier nontrivial \(b\)-run already gives synchronization. If Bob has not synchronized the automaton, its position after \(w\) is either \(\{0,1\}\) or a two-element subset excluding zero. (To see this directly, prior to a collapsing \(c\) the only non-collapsing \(c\) acts on \(\{0,1\}\) and leaves it there; after the final non-collapsing \(c\) there can be at most \(n-3\) consecutive \(b\)'s.)

If the position excludes zero, Alice wins immediately on her second move by choosing \(c\). Otherwise it is \(\{0,1\}\); Alice's second move is \(b\), yielding \(\{1,2\}\). Bob has at most \(n-3\) letters. As long as this pair remains distinct, reaching state zero from either initial state \(1\) or \(2\) by \(b\)'s requires at least \(n-2\) such steps, and applying \(c\) while the pair excludes zero collapses it. Hence Bob either synchronizes the pair himself or leaves a pair excluding zero. In the latter case Alice's third move \(c\) synchronizes. This argument includes the boundary \(n=3\), for which Bob may play only the empty word when \(k=1\).

**3. Bob wins when \(k\geq n-1\).** Bob tracks two surviving tokens occupying a set \(\{0,j\}\), with \(1\leq j\leq n-1\), immediately after each of his turns. Such tokens exist initially. Suppose the invariant holds at Alice's turn. If Alice plays \(c\), the tracked set becomes \(\{0,1\}\); Bob responds with the empty word. If Alice plays \(b\) and \(j=n-1\), their image is \(\{1,0\}\); Bob again responds with the empty word. If Alice plays \(b\) and \(1\leq j\leq n-2\), the tracked states become \(\{1,j+1\}\), both distinct and nonzero. Bob responds with \(b^{n-1-j}\), which sends \(j+1\) to zero and \(1\) to \(n-j\). The response length lies between one and \(n-2\), so is legal because \(k\geq n-1\). The invariant is restored with two distinct tracked states. No Alice letter can merge these tracked states before Bob's reply; thus this strategy prevents synchronization forever.

**4. Exactly three Alice moves are necessary.** Bob can always respond with the empty word. No single letter resets \(B_n\): \(b\) permutes all states and \(c\) leaves \(\{0,1\}\). No two-letter word resets: words containing no \(c\) are permutations; \(bc\) and \(cb\) have rank two; and \(cc\) fixes the image \(\{0,1\}\). Conversely \(cbc\) is a reset word because \(Q_n\mathbin{\cdot}c=\{0,1\}\), then \(\{0,1\}\mathbin{\cdot}b=\{1,2\}\), then \(\{1,2\}\mathbin{\cdot}c=\{1\}\). This proves both the exact reset threshold and the worst-case three-turn lower bound.

**5. Alphabet-size minimality.** In a unary DFA with single letter \(a\), synchronizability is equivalent to the existence of a constant power \(a^L\). If such a power exists, Alice can choose \(a\) on every turn; the cumulative word remains a power of \(a\) and reaches length at least \(L\) after finitely many Alice turns regardless of Bob's intervening powers. Thus Alice wins for every response-length bound, including unbounded finite responses. If no power resets, she loses already when Bob always chooses the empty word. Unary game levels consequently coincide. Together with the binary family, this proves the final consequence. \(\square\)

## Verification
The standalone Python program `verify.py` builds the complete powerset synchronization game, includes every Bob response word of length less than \(k\), computes the monotone winning attractor and the minimum worst-case number of Alice turns, and tests \(3\leq n\leq10\) and \(1\leq k\leq n+1\). Its 60 parameter outcomes agree with the formula and report three moves for the winning cases. Separate checks reconstruct the proposed three-turn strategy, Bob's tracked-pair invariant, and the exact ordinary reset threshold. Run `python3 verify.py` from the artifact directory; expected output is provided in `verification_output.txt`. The finite tests are independent corroboration; steps 1–5 prove the infinite statement.

## Relationship to prior work
Lipin and Volkov introduced and studied these adversarial synchronization games. Their Lemma 2.1 constructs a **three-letter** witness \(E_n\) at level \(n-1\), using letters \(b,c,d\), and their Corollary 2.2 proves strictness without a fixed alphabet restriction. The present automaton retains only the first two transformations of that construction. Removing \(d\) changes the exact winning cutoff from \(n-1\) to \(n-2\), but preserves the existence of witnesses at every hierarchy level while reducing the alphabet from three to two. The new conclusion does not follow by simply restricting Alice's strategies, since Bob's permissible responses are also restricted; the two-sided strategies above determine the altered game exactly. The related study of uniform synchronization strategies by Fernau, Haase, Hoffmann, and Volkov concerns different game restrictions and does not itself supply this family-specific cutoff.

## Limitations
The theorem neither minimizes the number of states needed for each hierarchy separation nor classifies all binary witnesses. It does not provide a quantitative winning bound for arbitrary binary automata. Its originality assessment is limited to the inspected relevant literature and mathematical databases; an older equivalent under another formulation cannot be categorically excluded. No independent mathematical audit is claimed.

## References
- A. E. Lipin and M. V. Volkov, *Adversarial Synchronization*, arXiv:2601.18362v1, first publicly posted January 26, 2026, especially §2.2, Lemma 2.1 and Corollary 2.2. https://arxiv.org/abs/2601.18362
- H. Fernau, C. Haase, S. Hoffmann and M. V. Volkov, *Uniform winning strategies for the synchronization games on subclasses of finite automata*, arXiv:2512.11007, first publicly posted December 11, 2025. https://arxiv.org/abs/2512.11007
