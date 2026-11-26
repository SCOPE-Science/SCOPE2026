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

In a window of length divisible by four the odd positions alternate and contribute exactly one quarter of the total length as ones. The evens decimate to a contiguous shorter window. Iterating to length two gives K=N/2-1+p_J+p_(J+1), J=ceil(t/(N/2)). Successive odd-indexed symbols are complementary, so each odd-start pair of adjacency edges contributes exactly one transition. The N-1 edges contain (N-2)/2 complete such pairs and one lone edge, with the latter at the first or last position according to starting parity. Endpoint parity therefore fixes T to N/2 or N/2-1. At fixed N, K, the endpoints and T determine all four bigram counts, and those counts with K recover both endpoints using their sum and difference. For k>=4, the starts (J-1)N/2+d for J=1,3,11 and d=2,3,4,7 all use the designated J above. The leading offset is divisible by 16; checking residues modulo 4, 8 or 16 gives the four claimed endpoint pairs at every J. Direct evaluation confirms the twelve starts at N=8. A separate bounded generation of the word and literal bigram census found exactly twelve distinct full profiles for lengths 8 through 256 within the sampled starts and reproduced the N=8 witnesses. The general edge and witness arguments, not the finite prefix samples, establish the all-length theorem.

## originality

PASS

The three ordinary Abelian weight classes at dyadic lengths are prior work. The inspected consecutive-pair literature specializes to other automatic words, while the closest paperfolding records count weights, cyclic rotations or scattered two-letter subsequences. The supported distinct claim is the complete endpoint refinement of each weight layer for contiguous bigram equivalence, and hence the twelve classes.

## value

PASS

Powers of two match the word's even-position self-similarity and are a natural regime rather than sampled lengths. The pair-count level is the first refinement beyond the known Abelian weight count. The result gives the exact class count and a full weight/endpoint description with uniform witnesses, useful as an exact benchmark for 2-Abelian complexity of this standard automatic word.

The dated certificate retains the supplied scientific assessment, sources and limitations.
