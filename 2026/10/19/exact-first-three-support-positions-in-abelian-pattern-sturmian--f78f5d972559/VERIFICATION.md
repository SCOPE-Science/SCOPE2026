---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scope

The proof in `RESULT.md` contracts two antidiagonals into paths and reduces the third antidiagonal to selected edges of a cyclic permutation on residue classes. It separately proves that every acyclic three-point support admits a forest-preserving infinite continuation.

Run `python3 check_three_sums.py` to reproduce `check_output.txt`. The checker enumerates all 14,190 triples with \(0\le a<b<c\le44\), independently calculates graph cyclomatic numbers using union-find, checks the algebraic formula, and tests 2,505 finite continuation stages. Finite tests support boundary confidence but cannot certify the unbounded theorem or independent novelty.

The existence corollary relies on the published 2026 characterization identifying Abelian pattern Sturmian words with characteristic functions of infinite forest-supported sets. The proof of the graph formula and the extension lemma are self-contained. The primary paper's full text was not accessible in this verification environment, so this is not a full-text priority certification. Independent scientific audit has not been performed.
