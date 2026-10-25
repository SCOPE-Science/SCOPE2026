---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For unsigned incidence N, NN^T=Q(G), N^TN=A(LG)+2I. G is connected nonbipartite (contains an odd cycle), so N has full row rank; m-n=t-1 gives exactly t-1 additional eigenvalues -2. For adjoining a length (2h+1) cycle at one cut vertex, the 2h fresh vertices form even path matrix B with inertia (h,0,h), determinant (-1)^h and b^TB^-1b=2(-1)^(h-1). Its Schur complement in M=Q-2I is M if li≡3 mod4, or M+4ee^T if li≡1 mod4. The inverse terminal diagonal g remains -1/2 until first 1(mod4) block then g=1/(4q-2), giving nonzero Schur multipliers and at most one sign flip. The consequent inertias and determinant telescoping yield the two exact formulas independent of attachment position. Independently built 10 odd-cycle chains of lengths 3,5,7 with up to four blocks and varied attachments; exact SymPy integer determinants matched and independently evaluated real symmetric eigenvalue signs matched with no near-zero eigenvalues. Finite examples corroborate but do not prove the unbounded induction.

## originality

PASS

Paone–Paone 2026 gives full line-graph inertia for roses and generalized theta graphs and a general one-sided bridgeless-cactus bound with leaf elimination, but the inspected Section 10 does not provide the complete odd-cycle block-PATH inertia/determinant two-case law for t>=3 with distinct cut vertices. Francis–Uptain 2026 concerns bridge-connected gadgets and unbounded positive signature, not vertex-glued blocks. New exact boundary-resolvent telescoping extends this known method to a naturally different infinite topology; t<=2 cases are credited.

## value

PASS

A complete signless-Laplacian/line-graph inertia and determinant classification across unbounded cycle lengths, residue classes, attachments and block number is a natural spectral graph invariant result. Explicit branching counterexample (four pentagons) demonstrates the path hypothesis and helps delimit its mathematical utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
