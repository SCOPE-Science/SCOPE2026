# Self-review

## Correctness
PASS. For the source's nonconstant formula, \([p]^e\) represents zero and its image is \([q]^{ev}\) times a unit. It is zero modulo \(q^f\) exactly when \(ev\ge f\), so the integer threshold is the ceiling. The explicit \(p=q=3\), \(e=2\), \(f=3\) bottom stratum fails because zero maps to \(9\) modulo \(27\). The exhaustive verifier independently finds \(19\) homomorphisms and agrees with the corrected parameter count.

## Originality
PASS, subject to the stated revision risk. The inspected v1 source prints the floor lower limit in Proposition 3.1, Definition-Lemma 3.3, and Theorem 3.4. The earlier same-author paper covers same-modulus automorphisms, not this cross-exponent threshold. Checked published-result records and targeted literature searches did not locate the ceiling correction or the exact \(19\)-map witness.

## Value
PASS. This is a structural correction to a complete parametrization: for every \(f>e\) with \(e\nmid f\), it deletes a whole invalid stratum. The first odd-prime witness changes the predicted hom-set size from \(55\) to \(19\), so the consequence is quantitatively substantial and directly testable.

## Closest literature and limitations
The closest source is J. Atalaye, L. Baker, and S. Marques, “Prime-Power Multiplicative Modular Monoid Morphisms,” arXiv:2610.02393v1. Their earlier arXiv:2408.06278v2 treats automorphisms of one prime-power residue monoid and does not cover unequal source-target exponents. The claim is about v1; a later revision may contain the same repair. The exact count \(19\) is claimed only for the explicit \(9\)-to-\(27\) witness.

Self-review: passed. Independent audit: not yet performed.
