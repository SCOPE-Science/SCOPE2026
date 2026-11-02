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

# Verification of the two-partner online Prop1 theorem

Run `python verify.py` with Python 3 and its standard library. The file independently rebuilds shares and assigned loads after every arrival and checks exact inequalities after multiplying the proportional shares by two. The checks were executed successfully on the complete unmodified checker source:

- \(55{,}987\) exhaustive sequences of length zero through six on a three-agent path, using sizes \(1,2,5\);
- \(271{,}453\) exhaustive sequences of length zero through five on a four-agent cycle, using sizes \(1,2,3\);
- \(10{,}000\) reproducible random cases, up to 75 arrivals on a six-agent cycle with singleton jobs and magnitudes \(1,2,5,11,23\);
- \(128\) possible seven-step recipient histories in the degree-three adaptive tournament.

The theoretical proof is independent of the finite tests: the pairwise signed-discrepancy induction and two-neighbor accounting identity cover all positive real weights and every finite horizon. The adversarial lower-bound construction is specific to deterministic online decisions, and does not prove any randomized lower bound against oblivious inputs. The checks are not independent mathematical certification; independent audit has not been performed.
