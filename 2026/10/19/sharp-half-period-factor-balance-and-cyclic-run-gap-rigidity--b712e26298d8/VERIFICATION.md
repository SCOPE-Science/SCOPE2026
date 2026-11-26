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

For a nonempty pattern the relevant window has L-|v|+1 possible starts when L>=|v|, including overlaps. Complete periods contribute the same count; the residual arc of length r has range at most min(r,p-r,t,p-t) for t occurrence residues. Reaching k=floor(p/2) forces t and r into {k,p-k}; for every even or odd case a maximizing arc must be exactly the starts or a minimizing arc exactly their complement, and a block of either permitted size attains the bound. For k>=2 adjacent starts force a one-letter power, and its start block comes from a single cyclic run, with the second run too short to contribute. Conversely c^(R1-k+1) realizes a start block of size k when the run gap is at least k. The singleton-letter argument covers p=2,3. A two-run word is primitive by its single cyclic 0-to-1 transition. The proof covers all pattern lengths. In line 33 'exceeds' should read 'is at least'; even equal runs are covered by the displayed non-strict criterion, so this wording does not invalidate the theorem. Independent direct overlapping-window counts passed for 1508 primitive binary/ternary periods (replay: python /workspace/branches/independent_replay.py 2); these finite checks are not the proof. The frozen checker and output were inspected, not executed.

## originality

PASS

Pass for the sharp universal bound and full run-gap classification, not for qualitative periodic boundedness or the definition of factor balance. The closest actual claims concern sufficient boundedness criteria or different cyclic discrepancies. They do not supply the asserted optimal constant or its two-way rigidity statement.

## value

PASS

Uniform factor balance is an established invariant. The theorem makes least period a calibrated sharp benchmark across alphabets and gives a direct cyclic-run test for exactly when no smaller uniform constant works. The classification applies even though the definition ranges over all lengths and patterns; it is stronger than a routine proof that a periodic word is uniformly factor-balanced.

The dated certificate retains the supplied scientific assessment, sources and limitations.
