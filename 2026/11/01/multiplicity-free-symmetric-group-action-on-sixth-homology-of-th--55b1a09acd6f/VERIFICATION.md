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
# Reproduction and mathematical dependencies

Execute `python3 verify.py` (Python 3 standard library only). The verifier prints `VERIFY_OK` after checking the 35 triple-vertices, all 15 conjugacy classes of \(\mathfrak S_7\), all 720 stabilizer orientation cases, exact orbit-conflict independence-polynomial evaluations at \(-1\), the Murnaghan–Nakayama character table and orthogonality, and the three degree-six constituent multiplicities. It checks \(\chi_6(1)=29\) and \(\chi_9(1)=7\).

The mathematical proof identifies invariant simplices with independent sets in the orbit-conflict graph and their orientation signs with orbit parity; the reduced Lefschetz trace is therefore \(-I(D_g;-1)\). The ninth character is the induced sign representation on six-subset cross-polytopal classes. The verifier checks this orientation representation but treats the independence and homology-rank statements of Feng–Wang and Feng as published mathematical inputs. It does not independently compute an integral chain model, the full nonequivariant homology, a sixth-degree cycle basis, or an integral homotopy equivalence.

The resulting self-review is passed; no independent mathematical audit is claimed.
