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

# Verification

The proof uses an explicit basis of the symplectic Lie algebra: the matrices \(\left(\begin{smallmatrix}P&Q\\R&-P^{\mathsf T}\end{smallmatrix}\right)\) with symmetric \(Q,R\), whose evaluations at a nonzero vector span all of \(V\). This works even in characteristic two. The ordinary derivation identity is reduced directly to \(B^{\mathsf T}J+JB=\lambda J\); the local-derivation equality follows by constructing a matching derivation at every \(v+tz\).

The included `verify.py` uses only Python's standard library and independently constructs the complete derivation-equation nullspace and the local-equation nullspace. It enumerates all nonzero test vectors for the stated finite cases, then checks that the local nullspace consists of center-preserving endomorphisms and has the formula-predicted dimension. Replay command: `python verify.py`. Expected terminal line: `ALL_CHECKS_PASS`.

Tests checked \(\mathbb F_2\) at ranks \(1,2,3\), \(\mathbb F_3\) at ranks \(1,2\), and \(\mathbb F_5\) at rank \(1\). The finite tests do not verify an infinite family by themselves; the written proof does. Extension fields were not exhaustively tested. No independent audit has been conducted.
