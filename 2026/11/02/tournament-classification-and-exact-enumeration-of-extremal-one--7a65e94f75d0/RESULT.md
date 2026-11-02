# Tournament classification and exact enumeration of extremal one-bounded trifferent codes

## Finding
For every integer \(n\ge2\), a ternary trifferent code whose words each contain exactly one symbol \(2\) has at most \(2n\) codewords. This bound is attained. The full labeled family at equality is parametrized by tournaments on \(n\) labeled vertices modulo global reversal, so its cardinality is
\[
2^{\binom n2-1}.
\]
Moreover, under coordinate permutations and independent coordinatewise swaps of symbols \(0\) and \(1\) (fixing symbol \(2\)), the extremal-code equivalence relation is exactly tournament isomorphism, cut switching, and global reversal. The exact maximum \(2n\) alone is an elementary bound; the additional contribution claimed here is the all-length classification, exact multiplicity, and equivalence correspondence.

## Assumptions and scope
Let \(n\ge2\), with coordinates indexed by \(V=\{1,\ldots,n\}\) and alphabet \(\{0,1,2\}\). A code \(C\subseteq\{0,1,2\}^V\) is **trifferent** if each triple of distinct codewords has some coordinate at which all three symbols occur. It is **one-bounded** if each codeword has exactly one occurrence of symbol \(2\). A *labeled maximum* means a distinct set of ternary words with fixed coordinate labels and literal symbols (not a count modulo relabeling). An orientation of the complete graph is a tournament; its *converse* reverses every edge. Cut switching on a vertex set reverses all edges with exactly one endpoint in that set.

## Proof
**1. Fiber bound and complementary pairs.** For each \(i\in V\) partition \(C\) into the fiber \(C_i\) of words having \(2\) at coordinate \(i\). A triple in one fiber cannot be separated: at that coordinate all entries are \(2\), and elsewhere all entries lie in \(\{0,1\}\). Therefore \(|C_i|\le2\), proving \(|C|\le2n\). In an equality case every fiber has two elements. For any two distinct words in \(C_i\), and any other anchor \(j\ne i\), choose a word from \(C_j\). Their triple can only be separated at coordinate \(j\), because the unique \(2\) symbol appears there in its third member, so the first two words must have opposite binary entries at coordinate \(j\). Consequently the two words of each fiber are complementary on all coordinates other than their shared anchor.

**2. Triangle parity criterion.** Select either element of each pair as the first row. Write \(e_{ij}\in\mathbb F_2\) for its entry at coordinate \(j\ne i\); the other word in the same fiber has entry \(e_{ij}\oplus1\). Let \(\delta_{ij}=e_{ij}\oplus e_{ji}\), for unordered pairs, where \(\oplus\) is addition modulo two. Consider one word from each of three distinct fibers with anchors \(i,j,k\), and binary branch indicators \(a,b,c\). The triple fails to be separated precisely if the two binary entries agree at each of the three anchor coordinates (every other coordinate contains no \(2\)). These equalities are
\[
 e_{ji}\oplus b=e_{ki}\oplus c,\qquad
 e_{ij}\oplus a=e_{kj}\oplus c,\qquad
 e_{ik}\oplus a=e_{jk}\oplus b.
\]
Their XOR is equivalent to \(\delta_{ij}\oplus\delta_{ik}\oplus\delta_{jk}=0\). Conversely, if this parity vanishes, the three equations are consistent: after fixing any one of \(a,b,c\), solve two equations for the other two, and the third follows from parity. Therefore trifference of **every** such triple is equivalent to
\[
\delta_{ij}\oplus\delta_{ik}\oplus\delta_{jk}=1
\qquad\text{for all distinct }i,j,k.
\]
A triple with two words in one fiber and a third in a different fiber is automatically separated at the third anchor because of complementarity; a triple in one fiber cannot occur at equality.

**3. Tournament normalization.** Changing the selected first row in fiber \(i\) replaces \(e_{ij}\) by \(e_{ij}\oplus s_i\) for every \(j\ne i\), and therefore replaces \(\delta_{ij}\) by \(\delta_{ij}\oplus s_i\oplus s_j\). The triangle equations imply that there are choices of \(s_i\) making \(\delta_{ij}=1\) for all pairs: set \(s_1=0\) and \(s_j=\delta_{1j}\oplus1\), for \(j\ne1\). For \(i,j\ne1\), the odd triangle parity gives \(\delta_{ij}=1\oplus\delta_{1i}\oplus\delta_{1j}\), so normalization follows. At \(n=2\), the same formula normalizes the single pair without invoking a triangle. Thus the normalized array satisfies \(e_{ji}=1\oplus e_{ij}\), exactly the incidence choices of a tournament. Conversely, an arbitrary tournament incidence array produces a pair of complementary words in each fiber and has all triangle parities odd, hence is trifferent, attaining \(2n\).

**4. Labeled enumeration.** In a fixed labeled code the only freedom in the first-row choices is to interchange the two rows separately in each fiber. If two normalized matrices describe the same code, their row-choice differences \(s_i\) satisfy \(s_i\oplus s_j=0\) for every pair; therefore all \(s_i\) coincide. The two possibilities are the identity or complement of every off-diagonal entry, corresponding to a tournament or its global converse. The converse action is free for \(n\ge2\), and exactly \(2^{\binom n2-1}\) distinct labeled codes result.

**5. Equivalence.** Coordinate permutation relabels vertices. At coordinates in a subset \(S\subseteq V\), exchanging binary symbols \(0\) and \(1\) toggles column \(j\) by \(b_j=1_{j\in S}\). Restoring normalization by toggling row \(i\) by \(b_i\) changes \(e_{ij}\) to \(e_{ij}\oplus b_i\oplus b_j\). This reverses exactly tournament edges with one end in \(S\), i.e. cut switching. Finally the global row swap gives tournament converse, and all these operations are reversible. Hence the stated equivalence correspondence is exact.

## Verification
The standalone standard-library `verify.py` enumerates all complementary-pair fiber candidates for \(n=2,3,4,5\), directly checks all distinct-word triples for trifference, independently enumerates tournament constructions, and compares the actual labeled code sets. Counts obtained are \(1,4,32,512\), matching \(2^{\binom n2-1}\). The saved output in `VERIFIER_OUTPUT.txt` records the checks. The all-length conclusions follow from the argument above, not finite computations.

## Relationship to prior work
Han, Sun, and Ge (2026), arXiv:2607.26376v1, study general asymptotic trifferent codes by locally sparse hypergraphs. The inspected sections concern unrestricted code growth and do not state this one-symbol-fiber classification. Bhandari and Khetan (arXiv:2402.02390v1, Section 3, Lemma 3.1) prove the exact elementary optimum \(T_b(n,1)=2n\) and display a canonical construction corresponding to the transitive tournament; their inspected full article does not enumerate or classify every equality case. Neither the optimum nor their particular construction is claimed new here. Amarnani's 2026 thesis explicitly investigates \(r\)-bounded trifferent codes and is the closest potential priority source, but only its detailed abstract, emphasizing \(r\ge2\), was accessible: its entire PDF could not be assessed. Earlier generalized-trifference literature studies a different multiplicity of separating coordinates. The present statement distinguishes its exact tournament-parametrization claim from the known general optimization questions; absence in accessible material is not a proof of novelty.

## Limitations
This is a classification of a constrained layer, not a new exponential bound for unrestricted trifferent codes. The elementary maximum-size bound itself is not presented as an independent mathematical advance. Possible implicit prior coverage, notably in the complete Amarnani thesis or older unindexed tournament-coding notes, remains a genuine priority risk. No independent mathematical audit has been conducted.

## References
- X. Han, Y. Sun, G. Ge, *Polynomially Improved Lower Bounds for Trifferent Codes via Locally Sparse 3-Uniform Hypergraphs*, arXiv:2607.26376v1 (first publicly posted 2026-07-29).
- S. Bhandari, A. Khetan, *Improved Upper Bound for the Size of a Trifferent Code*, arXiv:2402.02390 (2024).
- N. N. Amarnani, *Bounds on Trifferent Codes: Linear trifferent codes, blocking sets and r-bounded trifferent codes*, TU Delft master's thesis (2026), repository record uuid:57a405cf-c3f2-4aa2-afd0-7c2840a9c8b6.
- A. Bishnoi and collaborators, *The generalized trifference problem*, arXiv:2505.07706 (2025).
