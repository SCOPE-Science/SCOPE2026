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

Direct propagation gives \(p_2=(c^2/2,s^2,c^2/2)\) and \(p_3=(c^4/2,(1-c^4)/2,(1-c^4)/2,c^4/2)\). Shannon entropy on three or four accessible sites is maximized exactly by uniformity, yielding the stated unique angles on \([0,\pi/2]\). Fresh independent state propagation reproduced exact numerical uniformity at both angles and the Hadamard deficits. At one step the two position probabilities are one half for every angle, establishing earliest strict failure at step two. The frozen verifier was read and independently propagates the same walk.

## originality

PASS

The original paper says the Hadamard coin has maximum measurement entropy and supports the discussion with much larger-step plots. The erratum does not alter that conclusion. Ide-Konno-Machida later state that numerical results suggest entropy increases to \(\pi/4\) and decreases after it for any \(n\). The audited exact two- and three-step formulas directly contradict that universal finite-time suggestion, while targeted searches found no prior exact optimizer angles or earliest-counterexample statement.

## value

PASS

This is the earliest boundary test of a published universal finite-time entropy statement, and the corrected angles attain the absolute information-theoretic maximum by uniformizing every accessible position. The correction is mathematically motivated and directly relevant to finite-time quantum-walk spreading.

The dated certificate retains the supplied scientific assessment, sources and limitations.
