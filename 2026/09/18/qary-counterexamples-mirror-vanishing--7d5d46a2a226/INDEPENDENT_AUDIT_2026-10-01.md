# Independent audit — Nonbinary counterexamples to the literal mirror-vanishing extension

Audit date: 2026-10-01 (UTC) UTC

## Final claim assessed

The scientific claim in `RESULT.md` and `SLOGAN.txt` was assessed unchanged.

## Correctness — PASS

Multiples of the second generator have weight \(d\). If the all-ones coefficient is nonzero, the last \(d+1\) coordinates stay nonzero and a scalar ratio can cancel at most \(m=\lceil d/(q-1)\rceil\) balanced first-block coordinates, so the weight is at least \(d+t+1\). Nonzero multiples of the all-ones vector have full weight \(2d+1\), and \(k=2=n-2d+1\). An independent exact enumeration reproduced the distribution for prime fields \(q=3,5,7,11,13\) and \(2\le d\le14\); the proof uses only \(|\mathbb F_q^*|=q-1\) and covers every prime power.

## Originality — PASS

The contribution is the uniform all-nonbinary, all-distance family and linearly growing gap. The same-day small witness does not imply it; the stronger classification is later.

### Equivalent formulations
The all-\(d\) family was separated from the smallest-instance and later-classification formulations. Evidence: A same-day record gives the smallest \([5,2,2]_q\) witness; a 2026-09-20 record gives the later sharp dimension-two classification.

### Broader coverage
No earlier inspected result dominates the all-\(q>2\), all-\(d\ge2\) family. Evidence: He identifies the proof obstruction but gives no hypothesis-satisfying all-\(d\) family; the same-day record gives only the smallest witness; the sharp classification is later.

### Exact database or table
Catalogue equivalence would not itself supply the all-parameter implication. Evidence: Equivalent elementary codes may be catalogued, but no located table states the quantified mirror-vanishing counterexample theorem.

### Claim versus prior implication
The balanced-multiplicity construction is an additional quantified argument. Evidence: Neither the binary nonextension caveat nor the smallest witness mechanically implies the all-\(d\) family with unbounded gap.

### Source inspections
- **A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes** — https://arxiv.org/abs/2609.20344. Trigger: Primary theorem whose literal q-ary extension is refuted. Material read: Full relevant theorem and Section 3.4 discussion of larger alphabets. Assessment: The paper recognizes the nonbinary proof obstruction but does not provide an all-nonbinary hypothesis-satisfying counterexample family. Evidence: Its MDS discussion does not satisfy the local-gap premise.

Checked sources: https://arxiv.org/abs/2609.20344; https://doi.org/10.1109/18.705584; published archive record SCOPE-qary-long-gap-mirror-band--69c27f4f7824; published archive record SCOPE-qary-mirror-vanishing-counterexamples--5db1acf1b471

Residual risks: Originality is not claimed for the isolated smallest witness already present in a same-day record. Older code catalogues may contain equivalent constructions without this theorem.

## Scientific value — PASS

The family gives a clean, motivated boundary result for a new binary theorem: the literal statement fails over every nonbinary finite field, at equality in the dimension threshold, with an arbitrarily long initial gap for fixed \(q\).

## Reproducibility

An independent exact enumeration reproduced all tested prime-field instances \(q=3,5,7,11,13\) and \(2\le d\le14\); the general statement follows from the explicit proof.

## Disposition

**PASSED.** The unchanged final claim passes correctness, originality, and scientific value.
