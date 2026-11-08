# Scientific review: first KC-monotonicity reversal

## Correctness (PASS)

For a uniformly random permutation, the first accepted vertex is uniform; conditioning on it leaves a uniform order on the graph after deleting its closed neighborhood. The exact rational identity in RESULT.md therefore follows by induction on the remaining vertex set. Direct substitution gives \(M(T)=73/15\) and \(M(U)=34/7\), and moving edge \(56\) to \(16\) across the bare path \(1-0-5\) satisfies the source definition of a proper KC-transform. Independent exhaustive enumeration of all \(9!\) vertex orders confirms both means and their entire cardinality histograms. The standard-library checker generates all Prüfer sequences for \(1\le n\le8\), retains exactly one representative per tree isomorphism type by complete rooted encodings, and examines every proper bare path, obtaining strictly positive increases in all 146 applicable cases. This makes the finite minimality claim exhaustive, not an extrapolation from samples.

## Originality (PASS, qualified)

The full accessible text of the source paper explicitly proposes KC-monotonicity in Section 9; its Section 8.1 defines proper transforms and proves monotonicity only for the distinct auxiliary quantity \(
u\) in Theorem 8.3. The source's Theorem 1.4, global path minimality, cannot imply monotonicity along each KC cover; the numerical counterexample does not refute the global theorem. The source's separate question concerning the first two greedy colouring classes changes the observable and does not imply the single-class KC reversal. Comparisons against related tree and greedy independent-set claims, exact-term searches, and general KC/Kelmans aliases did not reveal equivalent coverage. Search incompleteness and unindexed publications remain historical-priority risks.

## Value (PASS)

The theorem resolves a clearly articulated stronger proposed explanation for the established global path-minimum theorem, with a concrete minimal obstruction and complete finite cutoff. It separates monotonicity of the authors' provable auxiliary statistic from monotonicity of the natural actual random greedy output, guiding future arguments and computational tests of tree shifts. Both the exact shift and sharp nine-vertex boundary have structural meaning, rather than representing an arbitrary finite calculation.

## Closest literature and limitations

Krivelevich, Mészáros, Michaeli and Shikhelman, Greedy maximal independent sets via local limits, arXiv:1907.07216 (2019-07-16); Random Structures & Algorithms 64 (2024) 986–1015; DOI:10.1002/rsa.21200, Section 8.1 and Section 9. The underlying KC poset originates in Csikvári (2010), and Bollobás–Tyomkyn (2012) concern walk/path counts, not the greedy expectation. The complete witness and cutoff require uniform vertex order on simple unweighted trees; neither an infinite family of reversals nor a classification beyond order nine is claimed. No independent expert assessment or priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
