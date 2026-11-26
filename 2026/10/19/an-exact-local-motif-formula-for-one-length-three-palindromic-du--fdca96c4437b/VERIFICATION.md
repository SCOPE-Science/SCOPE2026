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

Precisely one length-three reversal copy is appended to its source factor, with no complement or wraparound. Cancelling untouched prefix/suffix gives AB=BV^R even for overlapping factors. Gaps 1 and 2 force a constant span. At gap d≥3, B must be a prefix of A repeated; the tail condition requires the rotation of A by d modulo 3 to be palindromic. A nonconstant A has at most one such rotation. A gap d≥6 cannot join consecutive indices in an equality class because d−3 gives the same collision. The residual nonconstant gaps 3, 4, 5 give exactly abaaba, baaaaba, bbaabbab, and the unique possible residue prevents an intervening collision. Constant consecutive collisions are exactly the gap-one aaaa windows. Each equality class contributes size minus one consecutive edges; subtracting all edges therefore handles multiple collisions without overcounting. Window probabilities q^(−3) and (q−1)/q^(d+2) give the mean by linearity, including absent patterns at small n. The frozen verifier and metadata were inspected, not executed. A separately written bounded exact check tested direct descendants, consecutive collision edges and rational means on 23,452 words (q=2 through n=12, q=3 through n=8, q=4 through n=6; starting at n=3). Replay: /workspace/branches/bd9fa510-af55-420e-bcc8-8b4fda581296/reproduce_pal3.py. The all-length conclusion uses the proof, not that finite test.

## originality

PASS

The general palindromic-duplication collision criterion and a nonconstant gap-three example were already known. The supported contribution is the complete list of consecutive collision motifs for length three, the exact forward count and its uniform mean, not the collision criterion itself.

## value

PASS

Length three is the first case beyond the known exact short-length sphere calculations in which separated nonconstant collisions obstruct a run-only formula. The exact finite-motif census is an input-dependent quantity relevant to one-error sphere calculations, eliminates duplicate counting from long collision chains, and gives an exact average without needing a model for dependent overlapping windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
