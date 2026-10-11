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
# Reproducibility of the finite computation

Unpack all nine attached files into one directory and invoke, in order, `python3 verify.py`, `python3 homology_check.py`, and `python3 steenrod_check.py`. No third-party Python package is needed; only an ordinary Python 3 standard library. The first checker generates the thirty-two cube edges from their bit coordinates, compares exact endpoint and breadth-first line-graph distances, reconstructs every scale-two simplex, and verifies the fixed critical matching by topological sorting the entire directed Hasse diagram. It asserts precisely \(13{,}896\) simplices, \(6{,}943\) matched pairs, \(10\) critical cells with dimensions \(0,3,5\), and \(66{,}304\) directed face incidences. The expected success marker is `VERIFY_OK`.

The independent simplicial boundary calculation checks mod-two homology concentrated in degrees \(0,3,5\), with dimensions \(1,1,8\), and prints `HOMOLOGY_OK`. The final cochain calculation solves the exact cocycle equations, chooses a nonzero mod-two degree-three class, evaluates the mod-two simplicial cup-one operation, checks the resulting degree-five cocycle, and reduces it against the degree-five coboundary space of rank \(2104\). It prints `STEENROD_OK Sq2_is_zero`. It thereby rules out the only possible nontrivial degree-five attachments to the degree-three sphere in the discrete-Morse model by classical Steenrod-square detection.

The programs certify exact statements about this fully enumerated finite simplicial complex; they do not prove a family-wide claim or an independent external audit. The homotopy argument invokes mathematical theorems described in `RESULT.md`, and was reviewed together with the computations. No other computational or external certificates are claimed.
