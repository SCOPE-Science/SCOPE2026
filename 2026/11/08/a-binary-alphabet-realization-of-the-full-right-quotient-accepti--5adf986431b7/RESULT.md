# A binary-alphabet realization of the full right-quotient accepting-state spectrum for permutation automata

## Finding

For every pair of nonnegative integers \(m,n\), consider pairs \(K,L\) of regular languages over the **same fixed binary alphabet** that are recognized by complete deterministic permutation automata and have accepting-state complexities \(m\) and \(n\), respectively. Write the right quotient as
\[
KL^{-1}=\{x:\text{there exists }y\in L\text{ with }xy\in K\}.
\]
The exact binary-alphabet spectrum is
\[
\left\{\operatorname{asc}(KL^{-1}):\operatorname{asc}(K)=m,\ \operatorname{asc}(L)=n\right\}
=\begin{cases}\{0\},&mn=0,\\\mathbb Z_{>0},&m,n\ge 1.\end{cases}
\]
Thus **two letters are necessary and sufficient** to obtain the entire positive spectrum simultaneously for every positive input pair: the unary spectrum is only \(\{1,\ldots,mn\}\). The main new content is an explicit binary witness for all \(m,n\ge1\) and output values \(\alpha\ge m\); smaller positive values are supplied by the known unary witnesses.

## Assumptions and scope

A permutation automaton is a complete DFA in which every letter acts bijectively on the finite state set. The accepting-state complexity \(\operatorname{asc}(K)\) is the number of accepting states in the minimal complete DFA of \(K\), equivalently its least possible number across deterministic recognizing automata. All automata in the construction share \(\Sigma=\{a,b\}\). We require no bounds on the number of their nonaccepting states.

Fix integers \(m,n\ge1\) and \(\alpha\ge m\). Put \(k=\alpha+1\ge2\), \(r=n+1\ge2\), and let \(\sigma=(1\,2\,\cdots\,k)\) and \(\tau=(1\,2)\) be permutations of \([k]=\{1,\ldots,k\}\). Permutations act on the right, in the order of the letters read. Define the following binary automata:

* \(A\) has state set \([k]\), initial state \(1\), final set \(F_A=\{1,\ldots,m\}\), and actions \(a=\sigma\), \(b=\tau\).
* \(B\) has state set \([k]\times\mathbb Z_r\), initial state \((k,0)\), final set \(F_B=\{(k,j):0\le j\le n-1\}\), and actions
\[
(p,j)\cdot a=(p\sigma,j+1),\qquad (p,j)\cdot b=(p\tau,j),
\]
where the second coordinate is reduced modulo \(r\).

The assertion for \(m=0\) or \(n=0\) follows because an input language then is empty; such input complexities are themselves realized over the binary alphabet by adding an identity letter to the corresponding unary automata.

## Proof

**1. A two-generator product lemma.** The transformations of \(B\) generate all of \(S_k\times\mathbb Z_r\), not merely a subdirect product. Indeed, let \(g=(\sigma,1)\) and \(h=(\tau,0)\). The permutation \(\sigma\tau\) has one fixed point and is a \((k-1)\)-cycle on the remaining points, including when \(k=2\), when this factor is the identity. Consequently,
\[
g^k=(\mathrm{id},k),\qquad (gh)^{k-1}=(\mathrm{id},k-1).
\]
Since \(\gcd(k,k-1)=1\), these two elements generate \((\mathrm{id},1)\). Therefore \(g(\mathrm{id},-1)=(\sigma,0)\) is generated as well, alongside \(h=(\tau,0)\). The classical generators \(\sigma,\tau\) generate \(S_k\), proving
\[
\langle(\sigma,1),(\tau,0)\rangle=S_k\times\mathbb Z_r.
\]
Because this group is finite, the monoid of positive words in \(a,b\) equals the generated group: inverses can be replaced by positive powers. In particular every prescribed pair \((\rho,j)\) is realized by some word, for every \(\rho\in S_k\) and \(j\in\mathbb Z_r\).

**2. Minimality of the two inputs.** The natural action of \(S_k\) is transitive, so all \(k\) states of \(A\) are reachable. For distinct states \(p,q\), some permutation takes \(p\) to a final state and \(q\) to the nonfinal state \(k\); that permutation is realized by a binary word, so the states are distinguishable. Thus \(A\) is minimal with exactly \(m\) accepting states.

For \(B\), full product generation makes every state \((p,j)\) reachable from \((k,0)\). Given different states \((p,i)\ne(q,j)\), if \(p\ne q\), choose a permutation taking \(p\) to \(k\) and \(q\) elsewhere and a counter increment placing the first state at an allowed residue; the resulting word accepts exactly the first. If \(p=q\) and \(i\ne j\), take a permutation moving their common first coordinate to \(k\), together with a counter increment moving exactly one of the two different residues to the unique excluded residue \(n\). Again the two states are distinguished. Hence \(B\) is minimal and has precisely \(n\) accepting states.

**3. Accepted-word permutation projection.** Let \(\rho_w\) be the permutation on \([k]\) induced by a word \(w\). If \(w\in L(B)\), its initial point \(k\) returns to \(k\); therefore \(\rho_w\in H:=\operatorname{Stab}_{S_k}(k)\). Conversely, for every \(\rho\in H\), Step 1 supplies a positive binary word inducing the group element \((\rho,0)\). This word returns \((k,0)\) to itself, which is accepting because \(0\ne n\). Thus
\[
\{\rho_w:w\in L(B)\}=H.
\]

**4. Exact quotient finals.** The standard right-quotient construction keeps all transitions of \(A\) and changes its final set to
\[
\widetilde F=\{p\in[k]:\exists w\in L(B),\ p\rho_w\in F_A\}
=\bigcup_{\rho\in H}\rho^{-1}(F_A).
\]
Since \(H\) fixes \(k\), this excludes \(k\). Since \(H\) acts transitively on \([k-1]\) and \(F_A\) is a nonempty subset of \([k-1]\), it includes all the other points. Thus \(\widetilde F=[k-1]\). The resulting \(k\)-state quotient automaton is minimal: its transition group is transitive, and two different states can be sent to \(1\) and \(k\) respectively, distinguishing them by acceptance. Its accepting-state complexity is exactly \(k-1=\alpha\).

**5. Complete spectrum and sharp alphabet threshold.** The construction covers every \(\alpha\ge m\). Rauch and Holzer's unary classification supplies every \(1\le\alpha\le mn\), and those witnesses remain valid over \(\{a,b\}\) by allowing \(b\) to act as the identity on both automata (erasing \(b\) preserves the minimal quotients and final-state counts). As \(mn\ge m\), these two ranges cover every positive integer. The positive quotient cannot be empty when both permutation-automaton input languages are nonempty, since any accepted suffix can be inverted in the first automaton and a reachable accepting state can be reached by some prefix. For a zero input the right quotient is empty. Finally, the unary spectrum is bounded by \(mn\) for fixed positive \(m,n\), so one letter cannot realize the entire positive spectrum. Exactly two letters suffice and are necessary.

## Verification

Run `python3 checker.py`. The standalone checker independently enumerates the transition group and computes accessible, distinguishable states using partition refinement for all \(2\le k\le6\), \(2\le r\le4\), and \(1\le m<k\). It verifies that the full generated group has order \(k!r\), that the accepted permutation projection equals the point stabilizer, that the quotient final set is exactly \([k-1]\), and that \(A\), \(B\), and their quotient are minimal. These are finite consistency checks, **not** a replacement for the all-parameter proof in the previous section.

## Relationship to prior work

Rauch and Holzer, *On the accepting state complexity of operations on permutation automata* (arXiv:2208.14731; 2022 preprint, 2023 publication), prove the exact **unary** right-quotient spectrum \([1,mn]\) for positive input counts. Their result supplies the bounded low-range witnesses used here.

German, *A Unary-to-Nonunary Transition in the Accepting-State Spectrum of Right Quotient for Permutation Automata* (arXiv:2605.10852, first public May 11, 2026), determines the **unrestricted-alphabet** spectrum and gives a **ternary** construction with a separate clock letter. Its full construction and supporting group arguments were compared directly. The present result preserves its point-stabilizer quotient mechanism but realizes the independent clock by two letters using the coprime orders of \(\sigma\) and \(\sigma\tau\), and proves that binary is the minimum sufficient alphabet size. The already-known unrestricted spectrum itself is not claimed as new.

## Limitations

This is a statement about deterministic **permutation** automata and accepting-state complexity, not the minimum total state count, nondeterministic automata, or arbitrary non-permutation DFAs. It makes no claim that the specific witnesses are minimal in *total* size across all possible constructions. The group factorization is proved for each finite \(k,r\), without optimizing word lengths. Although direct comparisons of the most relevant primary sources and scientific search records did not identify an earlier binary-spectrum result, an unindexed earlier alphabet-reduction argument remains possible. Independent mathematical audit has not been performed.

## References

1. S. German, *A Unary-to-Nonunary Transition in the Accepting-State Spectrum of Right Quotient for Permutation Automata*, arXiv:2605.10852 (first public May 11, 2026). https://arxiv.org/abs/2605.10852
2. C. Rauch and M. Holzer, *On the Accepting State Complexity of Operations on Permutation Automata*, arXiv:2208.14731 (first public August 2022; 2023 publication). https://arxiv.org/abs/2208.14731
