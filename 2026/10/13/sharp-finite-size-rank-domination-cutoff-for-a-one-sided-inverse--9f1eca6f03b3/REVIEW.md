# Scientific review

## Correctness — PASS

The matrix rank inequality at any finite size bound is equivalent to vanishing on the inverse-pair zero locus: outside that locus the constant equal to the tested dimension bound suffices. Rational canonical form identifies the exact common annihilator of all invertible matrices with the product of primary irreducible powers; companion matrices prove that every exponent is necessary. The Laurent quotient and unbounded-degree argument yield the unlimited-rank class. The lower word-degree bound is the Laurent support interval \([-L,L]\), and the shifted annihilator attains it with nonzero coefficient at the negative endpoint. The direct rank equality of \(XY-I\) and \(YX-I\) justifies the global implication. All steps hold for every prime power and size, not merely the tested cases.

The standalone exact verifier independently reconstructs examples at \((q,N)=(2,1),(2,2),(3,1),(3,2)\), checks the upper-bound rank condition over 6839 full matrix pairs, checks four next-size witnesses, and returns `VERIFY_OK`. Enumeration is not used as an infinite proof.

## Originality — PASS, with residual risk

The nearest inspected source is Yan–Yang, arXiv:2610.01804v1, Proposition 3.1. It proves equality of the two inverse-relation ranks over algebraically closed characteristic zero, not the exact finite-field bounded-size domination ideal, its primary-power exponents, or its sharp degree threshold. Shamovich–Volčič, arXiv:2505.07469v1, Theorem 3.4 treats equality of ranks and stable association; Klep–Vinnikov–Volčič, arXiv:1504.08004v2, concerns other finite-dimensional rational-identity size bounds. Draisma–Kahle–Wiersig, DOI:10.1112/blms.12819, minimizes term count for vanishing on generic rank varieties. None of the inspected results directly gives the full claim, and the database searches yielded no equivalent statement. The rational canonical form and irreducible counts are standard ingredients and are not claimed as new. Older equivalent finite-matrix-polynomial-identity formulations remain a residual originality risk.

## Value — PASS

The exact classification answers a natural question left by the nonhomogeneous rank-domination obstruction: which candidate polynomials can falsely pass every matrix test through dimension \(N\), and what is the smallest degree where such failure can occur? It establishes a sharp all-\(q\), all-\(N\) cutoff, useful for designing and interpreting finite computational rank tests, with an explicit smallest nontrivial binary example. The result is neither a generic known membership restatement nor a finite-table gain.

## Limitations

Only the generator \(xy-1\) and finite coefficient fields are classified. Neither the full general nonhomogeneous problem nor a universal degree-free finite testing rule follows. Exact finite enumeration supports examples; the theorem's full quantifiers rely on the proof. An undiscovered historical equivalent is possible.

Self-review: passed. Independent audit: not yet performed.
