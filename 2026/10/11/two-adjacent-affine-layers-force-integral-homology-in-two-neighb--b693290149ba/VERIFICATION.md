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

# Reproduction and scope

Run `python3 verify.py` with Python 3.8 or newer; the program uses only the standard library. It constructs the actual simplicial complexes from their defining face rule for every \(2\le n\le4\) and \(2\le q\le5\), checks two distinct completions and connectedness of the top-facet incidence graph, and computes all reduced boundary ranks and Betti numbers over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_5\). Successful completion prints `VERIFY_OK 12 exact complexes`.

The executable confirms finite instances but does not serve as an exhaustive test of the infinite family. The all-parameter argument is the proof from the connected incidence graph and the relative exact sequence. Its claim of no integral torsion uses dimension invariance across every characteristic together with the universal coefficient theorem; the sample primes are not a substitute for that argument.
