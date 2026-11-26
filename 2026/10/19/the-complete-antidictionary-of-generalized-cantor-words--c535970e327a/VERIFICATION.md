---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The substitution recursion W_(j+1)=W_j 0^(L_j) W_j gives ruler gap lengths L_(v2(i)) inductively. Every word with ones is tested by exact congruences on the internal gap offsets and lower-bound congruences for the boundary runs; the powers-of-two moduli are nested, so a failure has an incompatible pair. This also handles the initial occurrence, since any finite compatible pattern can be copied at arbitrarily large indices. An illegal internal gap can occur in a minimal absence only when that two-one word is the entire candidate. Otherwise deleting each end must eliminate each incompatible pair, so only the two affected conditions can conflict (if the same single exact condition is affected at both ends, an allowed two-one gap already occurs). Two left/right boundary thresholds must coincide at j+1 with the distance an odd multiple of 2^j; the two deletions force incompatible valuations on an interior index if the multiple exceeds one. For two exact endpoints the relaxed compatibilities force equal exponent j and again distance exactly 2^j by the intermediate-index argument. A mixed pair could conflict minimally only with exact exponent k-1, threshold k, and distance divisible by 2^k; the offset 2^(k-1) then has different forced valuations under the two deletions. Thus only the stated pure-type exceptions survive. At distance 2^j both pure-type exceptions lack the full occurrence but realize both deletions by swapping a valuation j and one at least j+1; remaining internal gaps are those of W_j. All-zero words occur, both letters occur, and disjointness and lengths give the count, generating series and asymptotic. The two exceptional length sequences overlap exactly as stated for q=3; for q>=4 the ratio is strictly between 1 and q, so no equality between their powers is possible. An independent digit-position reproduction (/workspace/review_evidence/check_4.py) exhaustively checks every length through 82,65,80,100,125,130 respectively for q=3,4,5,6,7,8. These prefixes capture the exact factor languages in those ranges: a length at most q^k meets at most two substitution blocks and W_2 contains all allowed bigrams, so W_(k+2) contains all factors of those lengths. The frozen verifier was inspected, not executed; the general proof, not these finite ranges, covers all q and all lengths.

## originality

PASS

The general infinite-word classification across every integer q>=3 is the distinct finding supported by the comparison, not a claim that the ternary formulas have no antecedent. The exact finite ternary classification determines the infinite ternary specialization by stabilization, and another finite result contains its two scale words at the maximal level. Neither states the all-q theorem or solves the different zero-run threshold/length arithmetic for q>=4. General algorithms and ordinary factor counts do not themselves give labelled missing extensions. The closest factor-complexity paper remained inaccessible in full; the possible implications of its right-special results are a real residual risk, not evidence for or against coverage.

## value

PASS

An explicit antidictionary gives exact finite certificates of nonoccurrence in a natural infinite substitution language. Beyond the covered ternary slice it classifies every possible labelled minimal failure over a nontrivial parameter family, rules out mixed endpoint obstructions uniformly, and explains the distinct lacunary count spectrum for nonternary q. This is stronger than supplying a complexity count or applying a sequence algorithm to one finite prefix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
