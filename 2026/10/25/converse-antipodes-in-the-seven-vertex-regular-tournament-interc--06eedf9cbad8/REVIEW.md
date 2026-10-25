# Scientific review

## Correctness — PASS

The claim is finite and complete: the first standalone proof program maps all \(2^{21}\) directed complete-graph choices bijectively to integer masks, selects those of score \((3,3,3,3,3,3,3)\), constructs all and only legal cyclic-triangle reversals, partitions all 2,640 regular states into all permutation orbits, and performs exhaustive breadth-first search on representatives. That establishes the complete graph's metric from a terminating exhaustive integer calculation, not a mere sample. The second program independently generates the regular states by recursive adjacency-row choices, builds moves directly, and checks distances from every state. Both computations passed on the actual standalone files and agree on every claimed class, shell, diameter, and converse antipode. The proof of class-constancy follows from permutation invariance. There is no extension asserted beyond order seven.

## Originality — PASS with recorded risks

The 1984 classical interchange framework and the 1998 article both cover the existence of directed-triangle reversal paths in a fixed tournament score class, so this established statement is explicitly excluded from the new contribution. The 1998 full text's Section 5 addresses general interchange-graph diameter bounds and asymptotic behavior, not the complete metric at score \((3,3,3,3,3,3,3)\). The open 2025 Coxeter interchange text introduces a broader transformation setting and recites the classical regular-degree/connectedness facts without an exact seven-regular three-orbit spectrum. The 2009 minimum-score hypercube statement concerns distinct score constraints, not our 14-regular graph. Searches for triangle-reversal distances, exact seven-tournament radii, and antipodes found no matching primary theorem or archived claim. This is a best-knowledge originality conclusion, not a proof that no equivalent work exists. The original Brualdi–Li chapter was not available in full; an unindexed small-order metric table there or elsewhere remains the main priority risk.

## Mathematical value — PASS

The unrestricted score-fiber connectivity theorem does not determine the *shortest* number of legal moves. The classical order-seven regular score fiber is the first natural finite case with three relabeling types; determining all exact distance shells, two distinct eccentricity regimes, and the converse-antipode criterion resolves a natural graph-metric invariant in that case. The sharp distinction (only one orbit has a unique antipode; the other orbits' converse distance is seven) is structural, not a routine restatement of the known vertex count or degree. The intrinsic four-vertex characterization enables identifying the antipodal class without solving a shortest-path problem. This is an exact finite theorem, with no claim of a general infinite-family consequence.

## Closest literature and limitations

Relevant sources include Brualdi–Li (1984), Guiduli–Gyárfás–Thomassé–Weidl (1998, full text inspected), Kannan–Tetali–Vempala (1999, bibliographic/abstract comparison), Chen–Chang–Wang (2009, abstract comparison), and Kolesnik–Mitchell–Przybyłowski (2025, available full text). A closely related 1984 source remained inaccessible in full, while other differently indexed theorems cannot be ruled out. The complete verification covers only seven vertices and uses exhaustive exact computation, not an asymptotic argument.

Self-review: passed. Independent audit: not yet performed.
