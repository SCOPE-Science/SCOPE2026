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

A parking word has t_i=#{letters<=i}>=i for all i. Group its unique weakly increasing runs as a run-by-letter multiplicity array, ordered by weakly increasing run minima. The transfer state (placed copies t, opened runs k, set S of earlier boundaries whose strict descent has been witnessed) encodes exactly these conditions. A new letter opens h nonempty runs and fulfills q old boundaries; stars-and-bars gives C(a+b,b+q+h) for k>=1, or C(a-1,h-1) when k=0. Newly opened boundaries remain unsatisfied until a later higher letter enters the preceding run. Each completed state corresponds bijectively to one flattened parking word; nonfinal runs have length>=2 so r<=ceil(n/2). Independent literal enumeration n=1..6 matched the claimed rows; infinite n follows from the bijection, not tests.

## originality

PASS

Best-of-knowledge originality: exact mathematical implication comparisons favor a non-covered surviving contribution; related special cases and premises are explicitly credited, with listed residual priority risks.

## value

PASS

The 2022/2023 paper explicitly asks for an unrestricted enumeration refined by weakly increasing run count and only gives data through n=8. This binomial-transfer algorithm resolves that natural stated problem for every n and every allowable r, with nonnegative explicit integer coefficients. It neither claims a small fixed-order scalar recurrence nor novelty of the original flattened notion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
