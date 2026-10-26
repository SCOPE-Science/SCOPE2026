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

# Reproducible mathematical checks

Run `python3 verify.py` with standard Python 3. No external libraries, data files or randomized simulation are required. A deterministic seed selects 220 finite rational parameter configurations. For each, the program exhausts all correctness vectors and independently computes the two pivotal background probabilities by exact convolution. It also checks 216 homogeneous binomial identities, the exact three-voter and five-voter example, direct enumeration for the two-state witness through eleven voters, and 20 successive positive/negative sign predictions.

Expected key fractions: `-1/375` at three voters and `2/625` at five voters. A passing program is supportive finite evidence only; the all-size proof is the two pivotal-event partition followed by a monotone exponential-ratio argument.

Only a single fixed delegation edge is modeled. The code does not validate that any algorithm will select this edge, any empirical distribution of signals, or any scientific assertion about real human behavior. The common-signal model is stipulated, and signal-conditional competence vectors are mathematical inputs.
