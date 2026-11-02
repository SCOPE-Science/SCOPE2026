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

# Exact verification and scope

The standalone `verify_hexagrammum.py` requires Python 3.9+ and no external packages. Run it with `python3 verify_hexagrammum.py`. Its complete observed output is in `verification_output.txt`, ending with `VERIFY_OK`.

The program enumerates all 720 permutations on six labels, builds the 60 unoriented Hamiltonian cycles and the 180 ordered pairs with disjoint edge sets, and checks that the incidence relation is regular of degree three on both sides. All eleven Frobenius cycle-type spectra are recomputed as actual orbits and compared to the displayed table. Fixed-point counts of powers and all 720 permutations provide separate consistency checks. The two rational-line-without-rational-incidence partitions are determined exactly.

An independent projective implementation constructs all Pascal lines and Kirkman points from six points on the conic \(XZ=Y^2\), with parameters \(0,1,3,9,25,64\). It confirms all 180 and only the expected incidence pairs, both over \(\mathbb Q\) and modulo \(10007\), and confirms all sixty lines and sixty points remain pairwise distinct there. All projective arithmetic is exact.

The theorem for all permitted incidence-generic sextuples follows from the functorial geometric construction and exhaustive finite permutation analysis; the two explicit projective examples establish a nonempty incidence-generic locus in characteristic zero and one permitted positive characteristic, not existence over every finite field or every Frobenius type. Characteristic \(p\ge7\) and the absence of additional Pascal–Kirkman incidences are part of the hypotheses. No independent scientific audit has been performed.
