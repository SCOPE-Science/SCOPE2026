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

# Exact verification

Run `python3 verify_majority.py` to exhaust every connected labeled graph on two through five vertices and every possible single missing edge, and to solve monotone exact rational probability/time recurrences. Its complete logged outputs are: connected labeled counts 1,4,38,728; qualifying edge-marked insertions 0,0,0,90; two marked classes occurring 30 and 60 times; first class pre/post polarization 0 and 7/48 with times 105/16 and 355/64; second class pre/post polarization 0 and 31/192 with times 713/96 and 545/96.

Run `python3 independent_markov.py` to construct separate 32-state absorbing Markov systems and solve rational linear systems without use of the potential-recursion implementation. The result matches all eight finite network quantities and identifies two unanimous versus four absorbing states.

Run `python3 star_family.py` for independent rational evaluation of the star-family finite-sum recurrence (\(m=4\) gives \(7/48\)), checks through m=8 and asymptotic spot checks through m=256. The computer does not prove the infinite limit; that follows from the explicitly bounded hub-flip event in RESULT.md. Neither random sampling nor partial enumeration has been passed off as exhaustive.

The six scientific files and the three scripts are complete standalone inputs, requiring only a Python 3 interpreter. No external independent audit is claimed.
