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
# Verification

The executable checker reconstructs the crown graph and the total Roman condition directly from definitions. It exhaustively enumerates every labeling of weight at most \(6\) for \(n=4,5\), confirms minimum weight \(6\), and compares the full optimizer set with the analytic classification. It then checks every edge-deletion set of size below \(n-1\) for those orders, verifies the explicit \(n-1\)-edge witness, checks the directed-count inequality through \(n=60\), and checks witness degrees through \(n=100\).

The finite calculations do not certify the infinite theorem by themselves. The universal lower bound is the analytic inequality \(|F|\ge |O||I|+n-|O|-|I|=n-1+(|O|-1)(|I|-1)\), after the survival characterization forces \(O\cap I=\varnothing\) and every arc from \(I\) to \(O\). The explicit witness supplies the universal upper bound.
