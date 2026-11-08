---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For cyclic indexed binary rings, labeled two-bit de Bruijn transitions of rule126 (output 0 exactly for uniform triples) give d_n(y)=tr(prod B_y). The labeled-one matrix splits into complement-even E=[[0,1],[1,1]] and complement-odd O=[[0,1],[-1,-1]], with Fibonacci and period-three traces. Each cyclic zero gap contributes simultaneous eigenvalues F_(a-1) and tau_a, proving the exact product formula for all outputs other than all-one (including adjacent zeros via F_-1=1). The all-one trace is Lucas L_n plus 2 if 3|n, else -1. Multi-zero output fibers are bounded by F_(n-3)+1, strictly below F_(n-2)+tau_(n-1) for n>=7; all-one exceeds that runner-up. Independently enumerated all indexed initial states and all outputs for n=1,...,12 and verified exact products, top, and one-zero equality for n>=7. All-length inequalities prove the unbounded statement.

## originality

PASS

Erica Jen 1989 already gives Rule 126 Fibonacci preimages and maximization of all-one **finite linear blocks**, and the de Bruijn/transfer-matrix technique is established. However periodic indexed-ring closure adds a second period-three mode; the exact all-output gap factorization and unique one-zero runner-up for every n>=7 are not a direct corollary of the inspected linear-block ranking. Rule126 image-set/reachability literature does not itself rank the positive fibers.

## value

PASS

The two leading preimage multiplicities and equality classes quantify worst-case ambiguity of a canonical elementary cellular automaton on finite periodic systems. The exact factorization gives a reusable structural classification, while the runner-up gap is a natural extremal question independent of sampling or trivial rule renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
