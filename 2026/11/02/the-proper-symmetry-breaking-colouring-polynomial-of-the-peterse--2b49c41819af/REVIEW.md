# Review of the proper symmetry-breaking colouring polynomial of the Petersen graph

## Correctness — PASS

The domain is the fixed ten-vertex graph \(KG(5,2)\) with all palette colours named, and the count includes colourings using fewer colours than available. The group reduction \(\operatorname{Aut}(P)\cong S_5\) is justified by the five maximum independent stars. The least-unassigned-vertex independent-block recursion is exhaustive and duplicate-free; every completed partition is checked under all 120 automorphisms. The second verifier uses independent restricted-growth assignment and an unrestricted named-four-colour scan; it also reconstructs the classical chromatic polynomial. Both verifiers pass on the actual standalone code files. The coefficient table establishes the full polynomial for all nonnegative integer palettes; the high-palette asymptotic follows from exact polynomial subtraction. The proof does not extrapolate finite checks to a larger graph family.

## Originality — PASS, qualified

Collins–Trenk, Theorem 2.5 (2006), already proves the threshold \(\chi_D(P)=4\); the present theorem does not claim that threshold as new. Weigand–Jacobson (2008) and Lal–Bhattacharjya (2009) study generalized Petersen distinguishing parameters but the inspected available texts do not provide the full Petersen proper-distinguishing enumeration. Arvind–Cheng–Devanur (2008) develops a general method for counting symmetry-breaking vertex *labellings*, which does not furnish this concrete proper-colouring polynomial or its four-class stabilizer geometry. The classical Petersen chromatic polynomial is used only as a check. Earlier Petersen four-colour recolouring data may include unlabelled orbit sizes, but does not state the classwise stabilizer distribution across all palette sizes. Targeted searches did not locate the complete result. An equivalent unindexed historical computation cannot be ruled out.

## Value — PASS

For the canonical smallest highly symmetric non-bipartite cubic graph, a bare threshold \(\chi_D=4\) does not tell how often a proper assignment actually breaks symmetry. The exact polynomial answers that natural quantitative question uniformly in palette size. Its sharp \(8/27\) probability at four colours, two precise types of minimum-palette symmetry-breaking partitions, complete colour-class stabilizer census and \(10/q^3\) large-palette failure law are informative refinements. The leading coefficient has a direct group-theoretic interpretation through the ten base-symbol transpositions. This is a self-contained finite benchmark, not a claimed universal graph-family theorem.

## Closest literature and limitations

The decisive primary comparison is Collins and Trenk, *The Distinguishing Chromatic Number* (2006), Theorem 2.5, DOI 10.37236/1042. Other materially related sources are Weigand and Jacobson (2008), DOI 10.1080/09728600.2008.12088865; Lal and Bhattacharjya (2009), DOI 10.1137/080728640; and Arvind, Cheng and Devanur (2008), arXiv:math/0703927. The work concerns only \(KG(5,2)\), historical priority cannot be guaranteed, and independent scholarly validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
