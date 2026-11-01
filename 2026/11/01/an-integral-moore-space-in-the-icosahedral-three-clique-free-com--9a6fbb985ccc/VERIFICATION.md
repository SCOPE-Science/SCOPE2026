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

# Reproducing the finite certificate

Run `python3 verify.py` with Python 3; no nonstandard packages or external input files are needed. It reconstructs the icosahedral graph and all twenty triangular cliques from a fixed twelve-vertex labeling, and checks an independent explicit triangle list.

The program enumerates all \(4{,}095\) nonempty vertex subsets, retaining precisely those avoiding every triangular clique. It checks that the complex has \(1{,}047\) nonempty faces, \(112\) six-vertex facets, and face vector \((12,66,200,345,312,112)\). It constructs \(522\) matching pairs via the published pivot order and checks the entire directed Hasse graph of \(4{,}344\) incidences for acyclicity. The three critical masks are `64`, `3124`, and `1926`.

Two algebraically distinct cancellation recurrences, one on the four-face rows and one on the five-face columns, calculate the integer Morse boundary coefficient \(-2\). Separate reductions of original simplicial boundary matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\) check the expected characteristic dependence. These field calculations alone would not determine the integral order-two torsion; that conclusion uses the signed integer calculation.

The certificate is finite and exact for this labeled complex. Its validity rests on the stated discrete-Morse and cellular attaching-map theorems, not on numerical extrapolation. Independent audit has not been performed.
