---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Concavity of lambda2 on mean-zero subspace and edge-orbit averaging reduce a global independent-weight optimum to two class rates. Core/leaf Laplacian decomposes into blocks with eigenvalues μ±(a η,b); μ-(a lambda,b) is gap and its target t condition is b>t,a lambda>=t(2b-t)/(b-t). Minimization of c(2+1/(u-1))+Qu for u=b/t>1 yields unique u=1+sqrt(c/Q), hence exact D and rates. For a cyclic core both cosine/sine Fiedler vectors saturate their Rayleigh quotients at any optimum; private-leaf equations force all b_i common, complex rim equation imaginary part forces all a_i common. Direct 52 finite weighted Laplacian cases corroborate, not replace, proof.

## originality

PASS

Sun–Boyd–Xiao–Diaconis solve general continuous-time fastest mixing through SDP but do not state the transitive corona closed price formula or cyclic uniqueness. Shakeri fixes internal layer weights and optimizes only coupling; Boyd et al 2007 treat discrete-time SLEM. Existing weighted corona spectra provide eigenvalues, not optimization or all-nonuniform rigidity.

## value

PASS

Closed all-core-class benchmark for spectral mixing under meaningful edge costs, with nontrivial global uniqueness for cycles and three distinct large-size scales. This answers design tradeoffs beyond routine substitution in spectral formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
