---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The nonzero states split into \(k\) phase classes, and every transition that avoids the sink advances phase by one. Thus a word of rank at most \(k-r\) must kill at least \(r+1\) phases. For a killed phase representative, entering the sink forces a full occurrence of \(u\); distinct killed phases force distinct starting residues modulo \(k\). Since \(u\) is unbordered, selected occurrences cannot overlap, and distinct residues exclude a start gap exactly divisible by \(k\), so consecutive starts are at least \(k+1\) apart. This gives the lower bound \(k+r(k+1)\). The first copy of \(u\) merges each surviving two-state phase to at most one image, while the \(r+1\) displayed copies in \(u(au)^r\) start in distinct residue classes and kill that many phases, giving the matching rank. A fresh independent power-automaton replay for all binary unbordered words through \(k=5\) reproduced the threshold sequence, and the frozen verifier extends exact BFS checks to binary \(k\le7\) and ternary \(k\le5\); these finite checks are corroborative only.

## originality

PASS

Pribavkina's full primary paper constructs the exact completed semi-flower automaton, proves the incompletable-word/reset-word equivalence, and proves only the rank-one endpoint threshold \(k^2+k-1\). The fresh Resultary search did not locate an intermediate-rank profile for this family. The audited phase argument therefore supplies a genuine all-intermediate-ranks refinement of the source endpoint.

## value

PASS

Transformation-rank profiles are a natural refinement of reset thresholds. This theorem determines the entire high-deficiency profile of a canonical slowly synchronizing family and explains the endpoint threshold through a uniform phase/nonoverlap mechanism rather than adding an arbitrary finite statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
