---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The error ball was independently reconstructed by deleting one coordinate and then making zero or one substitutions in the surviving length-(n-1) word. Exact clique enumeration in the compatibility graphs independently found no 4-clique at n=7, exactly 12 5-cliques at n=8, and no 6-clique at n=8. All 12 n=8 optima contain both constant words. Independent orbit reduction under identity, complement, reversal, and reverse-complement gives exactly four classes of sizes 2,2,4,4 with the same representatives as classification.json. Thus both the maxima and complete finite classification are exhaustive.

## originality

PASS

Smagloy--Welter--Wachter-Zeh--Yaakobi define this exact deletion-plus-substitution channel and give non-asymptotic bounds/constructions, while later work improves asymptotic redundancy. The inspected sources do not contain exact binary n=7 or n=8 values or the 12-code symmetry classification, and targeted Resultary searches found no covering record.

## value

PASS

The result identifies a natural operational cutoff: blocklength eight is the first binary length that can support at least four messages under this error model. It also completely classifies every optimal code at that cutoff up to the natural reversal/complement symmetry, so it is substantially more informative than an isolated numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
