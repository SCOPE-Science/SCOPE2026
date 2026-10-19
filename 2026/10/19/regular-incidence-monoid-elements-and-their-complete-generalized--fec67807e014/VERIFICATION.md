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

# Computational verification and limits

Extract `CHECK.py` beside the other files and execute `python3 CHECK.py` using Python 3 and its standard library only. It constructs finite-field convolution multiplication directly, including a polynomial quotient representation of \(\mathbb F_4\). For every enumerated ordered pair it checks the inner-inverse equation, reflexivity, the invertibility criterion, and uniqueness of the commuting reflexive inverse. It compares counts separately for every nonzero-diagonal support as well as in total. Verified examples include the four-vertex star and fence over \(\mathbb F_2\), a three-vertex chain over \(\mathbb F_2\) and \(\mathbb F_3\), a fork over \(\mathbb F_2\), a two-vertex chain over \(\mathbb F_4\), and a two-vertex antichain over \(\mathbb F_5\). The successful terminal marker is `ALL_INCIDENCE_INVERSE_SPECTRA_PASSED`.

The proof covers all finite posets and prime-power fields, whereas the checker exhausts only the stated finite cases. Neither computational success nor limited literature searching certifies historical priority. Independent audit has not been performed.
