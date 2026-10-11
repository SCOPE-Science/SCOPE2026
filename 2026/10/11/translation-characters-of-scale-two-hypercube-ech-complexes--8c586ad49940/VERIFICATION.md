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
# Reproduction and limits

Run `python3 verify_cech.py` using Python 3.8 or later with no nonstandard dependencies. The script constructs the closed-neighborhood Čech faces in each dimension, checks the full signed Lefschetz sum for every translation in dimensions \(2\) through \(7\), and verifies multiplicities by direct discrete Fourier inversion. For dimensions \(2\) through \(5\), it computes the complete simplicial boundary ranks over \(\mathbb F_2\) and confirms only degree-two reduced homology occurs. It also verifies the multiplicity dimension sum for dimensions \(2\) through \(13\).

The output `verification_output.txt` is the actual saved stdout of a separate successful invocation on the bundled script. Exact reference cases: the second Betti number of \(K_3\) is \(7\). Dimension \(4\) has second Betti number \(31\). This is **not** an exhaustive all-dimensional computation. The theorem's infinite range instead follows from the published wedge-homotopy theorem plus the complete fixed-simplex classification and character orthogonality proved in `RESULT.md`.

There was no independent audit and no claim of external formal verification.
