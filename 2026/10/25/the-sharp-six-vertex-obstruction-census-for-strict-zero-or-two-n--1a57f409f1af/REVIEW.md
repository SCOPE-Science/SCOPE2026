# Scientific review

## Correctness
PASS. The definition of equilibrium agrees exactly with the finite bit-mask predicate in `verify.py`, which exhausts all labeled simple graphs through six vertices and all strategy assignments. The two candidate graphs also have self-contained parity/counting contradictions. Exhaustive orbit enumeration confirms that the 300 labeled failures are precisely 180 and 120 relabelings of the two witnesses. An independent edge-tally implementation checks 10,816 additional graph-state instances. All cardinalities and limits are explicit; no claims are made for larger orders.

## Originality
PASS with priority risk. The nine-edge 3-sun is **already known** to lack equilibrium (Klimm–Stahlberg, 2023, Lemma 5.3), and that fact is not presented as new. Gilboa's 2023 paper gives a larger nine-vertex obstruction and NP-hardness, but these do not classify smallest counterexamples. The new contribution tested is exact completeness at six vertices, the distinct and sparser eight-edge obstruction, and the 180/120 orbit counts. Primary papers, equivalent wording, published scholarly records and finite-graph catalog coverage were compared. A prior graph-specific classification under a different vocabulary remains possible.

## Value
PASS. For a response pattern whose equilibrium-existence decision is NP-complete, the smallest network supporting failure and the complete set of first-order obstructions are motivated finite structural invariants, not an arbitrary large numerical slice. The sparser eight-edge example improves the previously exhibited six-vertex nonexistence gadget, and the exact two-class boundary gives minimal model-validation test cases. This is a sharp finite classification, not a complexity breakthrough.

## Closest literature and risks
Gilboa–Nisan (2022) formalize the rule and initial open question; Gilboa (2023) establishes hardness and displays a nine-vertex obstruction; Klimm–Stahlberg (2023, Section 5.1) proves the 3-sun example. The latter is decisive partial prior coverage, expressly excluded from the novelty claim. The checked papers do not report the two-type first-order census. Residual publication-priority risk persists for uncatalogued or differently indexed enumerations. The use of exhaustive finite verification does not imply any infinite-network theorem.

Self-review: passed. Independent audit: not yet performed.
