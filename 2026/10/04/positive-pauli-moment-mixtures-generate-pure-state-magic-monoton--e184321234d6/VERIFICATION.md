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

The proof is analytic and uses no finite experiment as a substitute for an infinite statement.

The load-bearing imported result was checked in the full text of Leone--Bittel, arXiv:2404.11652 / Physical Review A 110, L040403: for every integer order \(m\ge2\), the stabilizer Rényi entropy is monotone under deterministic pure-state stabilizer protocols. Its definition gives \(\mathcal M_m=(1-m)^{-1}\log_2 P_m\), so the sign of \(1-m\) was explicitly checked when converting the theorem into \(P_m(\psi)\le P_m(\phi)\).

For the mixture step, the checks are: \(P_1=1\) by pure-state Pauli Parseval; \(0<P_m\le1\); nonnegative summable coefficients permit termwise summation; and the ratio logarithm gives the claimed monotonicity direction.

For faithfulness, equality forces \(P_r=1\) at some positively weighted \(r\ge2\). The pointwise inequality \(|x|^{2r}\le|x|^2\) then forces every Pauli expectation magnitude to lie in \(\{0,1\}\). Parseval fixes the number of unit-magnitude Paulis at \(2^n\), and their signed representatives form a maximal Abelian stabilizer group fixing the state.

The finite-temperature specialization was checked against arXiv:2608.14798. Expanding \(\cosh(\beta x)-1\) gives the coefficients \(\beta^{2m}/(2m)!\). The factors \(e^{-\beta}\) and \(2^n\) cancel between the state partition function and its pure-stabilizer reference, leaving exactly the displayed logarithmic mixture functional.

Limits: no strong/average monotonicity over arbitrary measurement branches, mixed-state extension, or \(\beta=0\) partition-function ratio is verified here.
