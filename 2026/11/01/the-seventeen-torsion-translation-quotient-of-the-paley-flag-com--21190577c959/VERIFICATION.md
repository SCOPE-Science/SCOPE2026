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

# Verification scope

The packaged standalone standard-library program `verify_quotient.py` has been run against the packaged bytes. It checks all cliques, the absence of 4-cliques, all translation orbits in simplex dimensions zero to two, the four oriented triangle attaching words, the integral boundary determinant 17, and the final attaching exponent 17. Its stdout is `verify_quotient_output.txt` and ends with `VERIFY_OK`.

The auxiliary `verify_paley17.py` and `verification_output.txt` check the acyclic simplicial matching and modular simplicial homology. They are independent finite sanity checks only. They do not substitute for the proof of the quotient homotopy or the integral deck module, which follows from CW cancellations and universal covering cellular chains.

One may reproduce the quotient calculation using `python3 verify_quotient.py` from the directory containing the embedded code. Standard Python 3 library suffices. All computations concern the finite graph on 17 explicitly labeled vertices. No external validation or independent audit has been performed.
