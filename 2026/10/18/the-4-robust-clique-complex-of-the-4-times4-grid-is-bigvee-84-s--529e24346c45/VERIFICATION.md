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

# Reproducibility and bounds

The verifier `verify_morse.py` fixes the graph \(P_4\square P_4\) on vertex bits \(0\) through \(15\), enumerates all \(65536\) vertex subsets, and compares the independence-number recursion to membership determined from exactly \(405\) independent four-subsets. It enumerates the face vector \((16,120,560,1415,1788,912)\), the empty face, \(2364\) distinct staged matching pairs and \(84\) unmatched five-faces. It explicitly orients all \(22008\) Hasse incidences and topologically sorts the entire \(4812\)-vertex directed graph. Every assertion must complete for `VERIFY_OK` to appear.

`verify_mod2.py` independently enumerates faces by forbidden four-subsets and reduces each boundary matrix over \(\mathbb F_2\), giving ranks \((0,15,105,455,960,828,0)\) in dimensions \(0\) through \(6\), reduced Betti vector \((0,0,0,0,0,84)\), and Euler characteristic \(-83\).

Both checks require only Python 3's standard library; run `python3 verify_morse.py` and `python3 verify_mod2.py` from the extracted package. The discrete-Morse acyclicity check, together with Forman's theorem, proves the integral homotopy type. The mod-two computation is independent corroboration. The result is restricted to this specified finite graph; no induction over graph dimensions is certified.
