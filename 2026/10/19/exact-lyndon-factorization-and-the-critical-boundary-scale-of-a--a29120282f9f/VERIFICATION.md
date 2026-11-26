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

Substituting once at depth j gives W_{j+1}=W_j 0^{r q^j} W_j. The two copies start/end in 1, so the runs do not merge, and the new run is strictly longer than every earlier run. Thus in B_j each proper suffix either starts in 1 or has fewer leading zeros than B_j; W_0=1 handles j=0. The B_j are Lyndon and strictly decrease, so finite CFL uniqueness identifies the entire list, including k=0. The finite lists stabilize and give the infinite decomposition. In fact a Lyndon factor cannot cross a new record-run boundary from an earlier start: its suffix at the boundary is either a shorter all-zero prefix or has more leading zeros, and is smaller. An infinite Lyndon tail is also impossible because every suffix has a smaller later suffix starting at a longer run. Starts are |W_j|. Summing the linear recurrence gives n_j=2^j+r sum_{i=0}^{j-1}2^{j-1-i}q^i, with the empty sum at j=0, and generating function (1+(r-q)z)/((1-2z)(1-qz)). The two growth laws and q-uniform identity follow. The Duval checker is bounded corroboration by design and was inspected, not run.

## originality

PASS

The supported distinct claim is the full two-parameter canonical block decomposition with explicit boundaries and the critical nonuniform q=2 scale. The standard factorization theorems, uniform Cantor word family, and membership of individual Lyndon factors in the overlapping ternary subfamily are not credited as new.

## value

PASS

Gives the complete canonical decomposition, not just occurrence or lengths, for finite sparse morphic words and their infinite limit. Identifying exactly which boundaries obey the resonant j2^j law rather than the q^j law makes the count useful as a benchmark outside the uniform Cantor family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
