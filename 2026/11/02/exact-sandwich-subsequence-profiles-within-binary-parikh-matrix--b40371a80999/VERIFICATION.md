---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS: The unique gap vector w=b^g0 a b^g1 ... a b^gA gives C=Σ_{i=1}^A i*g_i and I=Σ_{i=1}^{A-1}g_i. Fixing I=s and terminal gap j=g_A leaves a complete homogeneous polynomial h_s(z,...,z^{A-1})=z^s [s+A-2 choose A-2]_z and a factor Σ_{j=0}^{B-s} z^{Aj}, establishing the entire bivariate polynomial and exact conditional fractions. The sharp support proof separately treats A=2 (C=s+2j, parity), A>=3 with s=0 or s=1, and 2<=s<=M where intervals [Aj+s, Aj+(A-1)s] touch because (A-2)s>=A-1. For A>=3 this gives 0 or 1 plus [2,M] depending on A|C. Scattered ab^t a iff I>=t is exact for first/last a, so corollaries follow including B=0. Fresh independent direct word-and-inversion counts for 35 pairs A=2..6,B=0..6 reproduced every joint coefficient and complete conditional support. Not an inference from bounded experiments.

## originality

PASS

PASS (qualified, partial prior coverage explicitly credited): A same-model October 2026 primary paper by Fazekas, Huang and Mercaş was read in full for relevant results. Its Lemma 3.1 ALREADY yields the existential threshold t<=min(B,C,AB-C) for pattern ab^t a by substitution, and its Lemma 4.3 ALREADY gives aba avoidability iff A divides C. These two consequences are covered and cannot be counted as novel. The surviving central claim is the full two-variable exact Gaussian-binomial distribution of the number of b letters between first and last a and its all-s support, including A=2 parity and A>=3 interval-plus-hole; the inspected prior theorem does not establish that distribution, and bounded searches of q-Parikh/partition literature did not identify an implication. O PASS refers only to this genuinely finer complete profile, not to the two known existence/universal corollaries.

## value

PASS

PASS: Conditional structure within binary Parikh-matrix equivalence classes is a natural word-combinatorial question. The exact full internal-gap histogram and its sharp support provide more information than marginal Gaussian counts or yes/no sandwich-pattern tests; for every t they give exact containment probabilities. This is a useful explicit natural refinement for all A,B,C, not mere reparameterization of a known existence criterion. Value is assigned to the new distribution and fine support, not covered threshold corollaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
