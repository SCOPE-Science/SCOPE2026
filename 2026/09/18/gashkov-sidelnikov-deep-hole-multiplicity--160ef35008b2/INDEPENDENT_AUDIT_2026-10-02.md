# Fresh independent audit

Assessed at: 2026-10-02T17:01:01Z (UTC).
Disposition: repaired. Correctness / Originality / Value: PASS / PASS / PASS.

## Correctness

Read Shi--Li--Xia--Helleseth--Özbudak arXiv:2609.20402 complete relevant full text: signed columns biject with norm-one torus T; Theorem 1.3 uniquely decomposes every length-two remainder; Algorithms 1/2 and all four normalization branches specify admissible first coordinates and inverse coordinates. For a deep syndrome, every unordered minimum triple has three distinct, nonopposite summands, and each marked first summand determines the unique remaining pair, so |V(S)|=3M(S). In each of four branches, a nonexceptional first parameter satisfying the nonzero square/nonsquare conic condition has exactly two lifts to T, both yield distinct marked leaders; conversely an arbitrary marked leader's coordinate satisfies those same norm/discriminant conditions outside E={0}∪{AΔ=0}, |E|≤6, leaving at most 12 uncounted torus points. The branch complete character sum has main term q and three nonconstant sums with absolute bounds 1,3√q,3; removal of ≤6 nonnegative weighted terms of at most 4 yields q−3√q−28≤4A≤q+3√q+4. Therefore 2A≤|V|≤2A+12 gives (q−3√q−28)/6≤M≤(q+3√q+28)/6, exactly the stated symmetric discrepancy √q/2+14/3. Multiplication by a norm-one scalar bijects T-representations at syndromes with the same nonzero norm. The q=9 finite check is only illustration, not the infinite proof. Fresh independent finite corroboration constructs GF(q) and conics at q=9,27,81 and exhausts all syndrome/triple/marked-leader counts, two-lift conditions, every nonexceptional converse, exceptional bound and discrepancy; VERIFY_BRANCHES_OK actual exit0. Norm-class multiplicities are constant, with M=2 at q9, M=4 or6 at q27, M=12,14 or16 at q81. The four explicit branch quadratics, inverse coordinate logic and double-root contradiction are now included in the full RESULT; finite cases do not stand in for the infinite character-sum proof.

## Originality

1986 Gashkov--Sidel'nikov six-page original PDF was read at the conic-count step: it explicitly estimates a solution count N about q+1 with error ≤8√q to prove covering, so qualitative q/6+O(√q) is anticipated and appropriately disclaimed in this final record. The 2026 Shi et al. paper's Remark 4.7 gives a one-sided admissible-parameter lower bound (q−3√q−28)/4, not a two-sided all-minimum-leaders bound. The audited result adds the converse all-leader comparison and yields a sharper explicit leading constant 1/2 for M. 1987 FCT related paper located only bibliographically, residual risk stated; inaccessible plausible source alone does not fail best-of-knowledge O. Resultary API closest is the same assigned item plus a distinct torus-sampling item with a different decoder-efficiency claim.

## Value

Nearest-neighbor multiplicity is a natural decoding statistic distinct from merely finding one coset leader. A uniform explicit all-deep-coset bound with improved √q coefficient quantitatively controls ambiguity in maximum-likelihood decoding for two original natural code families; it is more than a cheap small-instance count.

## Primary-source comparison

- Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes: https://arxiv.org/html/2609.20402. Read: HTML abstract/introduction and theorem; Algorithms 1-2; relevant material in each of Sections 3.1,3.2,4.1,4.2 including the first-coordinate constraints, exceptional sets and character bounds; Remark 4.7; not an assertion that every line of unrelated text was read. Assessment: PROVIDES_INGREDIENTS_NOT_ALL_LEADER_BOUND. Lemma 3.1 lines 619-671; 3.4 lines 809-842; 4.1 lines 1023-1061; 4.4 lines 1206-1236; Remark 4.7 lines 1328-1334.
- Linear Ternary Quasi-perfect Codes Correcting Double Errors: https://www.mathnet.ru/php/getFT.phtml?jrnid=ppi&option_lang=eng&paperid=957&what=fullt. Read: All six original scanned PDF pages (PDF text lines 0-283): construction/quasi-perfectness, conic character-sum count, and later weight-distribution theorem; OCR imperfect but decisive formulas legible. Assessment: ANTICIPATES_QUALITATIVE_SCALE_NOT_EXACT_SHARP_BOUND. Original PDF page 2 displays character sum for N and |N−(3^s+1)|<8·3^(s/2), used to prove solvability; later pages concern weight spectrum, not an explicit all-deep-coset nearest-leader bound.
- Codes Connected with a Group of Linear-Fractional Transformations and Their Decoding: FCT 1987 LNCS 278, bibliographic references. Read: Bibliographic listings and citation metadata only; full theorem text not obtained. Assessment: INACCESSIBLE_PLAUSIBLE_SOURCE_RISK. Located title/venue but no theorem-level text; no claim of noncoverage from snippets.

## Explicit remaining risks

- The 1987 FCT full text was not accessible; it could sharpen an earlier multiplicity statement.
- The older scanned Russian PDF OCR is imperfect, though its decisive character-sum formula and bound are legible.
- No claim is made that q/6+O(√q) or torus norm invariance alone is original.

All source-tree, original-line and artifact evidence is preserved. The old assessment is inactive historical evidence, not this audit. This review is an independent scientific assessment to the best of our knowledge, not expert attestation or formal Lean verification; the latter two channel states remain exactly as in the frozen source. Publication is not performed by this isolated package.

