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
The proof was reconstructed from the definition before acceptance. The critical lower-bound identity is
\[
r_i+c_j-2x_{ij}=n-2
\]
for every off-diagonal pair \(i\ne j\) in a hypothetical two-colouring. Row and column summation forces \(r_i=c_i\), and for \(n\ne4\) forces all row sums, hence all edge labels, to coincide, which is impossible for \(n\ge3\).

The bundled `verify.py` independently checks the explicit \(n=3,4,5\) witnesses, exhaustively tests all two-colourings for \(n=3,4,5\), and checks the balanced one-factor construction through \(n=60\). These computations are corroborative. They do not certify all orders and are not used as a substitute for the symbolic proof.

Published comparison was also implication-checked: the minimum-degree-three-colour theorem covers the upper bound for \(n\ge6\), but not the two-colour lower bound or the small-degree exact cases.
