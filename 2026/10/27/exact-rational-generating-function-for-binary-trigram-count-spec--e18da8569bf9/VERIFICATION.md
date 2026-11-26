---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The linear binary word spells an Euler trail on the four bigram vertices; conversely any trail spells a word with exactly those trigram multiplicities. Directed Euler existence needs weak connectivity on the nonisolated support and the zero or one-start/one-end imbalance pattern. The only possible disconnected nonempty nonloop supports would each have two disjoint single-direction edges (AB with CD or AC with BD), giving four imbalanced vertices and thus excluded. Isolated loop vertices are handled separately: each loop is allowed only when its vertex is visited by the nonloop core, except in the two loop-only profiles. The empty vector contributes once. The three linear flow equations, nonnegative bounds and nonloop mass in RESULT.md follow by substitution. For an independent exact rational verification, set e=E+i, d=D_0+j and sum f from max(0,j−i+D_0−E−α−β); split into j≥i and j<i to obtain geometric rays. Forbid the A loop at i=0 when α=0 and the D loop at j=0 when δ=0, using inclusion-exclusion. The resulting thirteen-stratum sum including the loop-only correction cross-multiplies exactly to the stated numerator (replay: python3 /workspace/branches/review3-rational.py, SymPy). At z=1 the leading pole is (13/12)(1−z)^−5 and the other poles have lower order, giving 13n^4/288. Independent direct word counts through n=16 and connected multigraph counts through n=22 match the coefficients; the all-length identity is established by the geometric sums, not these finite runs. Reproduction files for the finite checks are trigram_recount.py and trigram_flow_independent.py under /workspace/branches/a7b4a96f-9d6c-4cc1-815b-f837c0503501. The uploaded verify.py was read, not executed. The noiseless code cardinality follows by choosing one representative per profile.

## originality

PASS

The object, leading asymptotic, imbalance-sector decomposition and several exact coefficients are prior in the October 18 Resultary record. The surviving distinct claim is the exact all-length rational function including the twelve open sectors and their connectivity restrictions. Three November 2 records state equivalent exact functions and are cataloged later; this neither establishes an earlier matching result nor certifies independent provenance. The closest finer published enumeration has a different equivalence relation; its exact counts can be used only after an additional balanced-support correction.

## value

PASS

The profile was motivated as a noiseless multiset-read invariant and already studied asymptotically. Exact finite-blocklength cardinality is the maximum number of distinguishable codewords for this observation; the known leading term and exact cyclic/finer counts do not give that finite answer. The result counts the twelve open endpoint sectors and loop/connectivity contributions rather than merely reproducing finite tabulations or the leading term. No error-correction capability or higher-window theorem is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
