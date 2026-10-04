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

The proof is symbolic and uniform. Expand the \(r\)-th power, apply Parseval, and solve the two integer equations on the difference of multiplicity vectors. Coprimality of \(A\) and \(B\) gives the primitive relation \((-(B-A),B,-A)\); nonnegativity gives the sharp cutoff \(|t|B\le r\). Parameterizing the residual multiplicities proves the coefficient formula and leaves no finite search assumption.

The accompanying `verify_resonance.py` performs an independent exact-integer replay for every \(1\le r\le10\) and every coprime \(0<A<B\le25\). It constructs all multiplicity vectors directly, groups them by Fourier frequency, and checks the predicted collision keys and coefficients. It also checks that the first resonant coefficient equals \(\binom{B}{A}\). The finite range is corroborative only; it is not used as an exhaustive proof of the infinite theorem.

Scientific limits: coefficients are unimodular, the domain is the one-dimensional torus, and no closed minimizer classification is asserted for the higher-harmonic phase polynomial when \(r\ge2B\). The special \(\{0,1,N\}\) first-collision observation is prior literature and is not treated as new.
