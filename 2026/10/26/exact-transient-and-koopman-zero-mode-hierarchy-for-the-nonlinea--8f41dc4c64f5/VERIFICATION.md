---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The local update f(a,b,c)=a+c+bc is left-permutive. Distinct inputs with identical cyclic output must travel exclusively in the off-diagonal paired-state graph; its two recurrent SCCs are the claimed even-cycle components, yielding odd-N injectivity and restricting collisions at even N to the alternating-parity support sector U. Direct equations for zero-output parity show F^{-1}(U)=U and F preserves U. Thus the complement is an invariant finite permutation sector of size 2^(2m)-2^(m+1)+1. Inside U successive maps are shifts times (I+S)^t on m-dimensional F_2 cyclic modules; m=q*u with u odd yields (x+1)^q as the only nilpotent factor of x^m-1 and rank m-min(t,q). Intersecting parity-sector images only in zero gives the image formula; nilpotent primary vectors produce exact entrance counts. Koopman rank K^t equals |image F^t|, so first and second rank differences give zero multiplicity and Jordan block frequencies. Independently enumerated every state of ring sizes 3..14 and image ranks; the original package code and off-diagonal graph table were separately inspected. The all-N statement rests on the finite 12-vertex collision graph proof and polynomial factorization, not the bounded experiment.

## originality

PASS

Qualified PASS: Zhu–Richard 2026 gives the Koopman framework, odd-N unitarity of rule 154 and plots/numerical near-unitarity for even N=22,24, but the accessible full paper's §§4.2–4.3 do not give all even-N transient ranks, time-to-cycle counts or the zero-Jordan hierarchy. Nobe–Yura 2007 analyzes an odd-ring linearization, a different regime. Generic Koopman fact that zero modes are transients becomes a numeric formula only after identifying the exceptional alternating support and its nilpotent primary factor. No Resultary exact rule-154 table was found. Equivalent finite-ring preimage-tree work remains a possible historical risk.

## value

PASS

Rule 154 is a canonical nonlinear elementary cellular automaton, with a striking even/odd reversibility contrast. An exact global transient census, sharp settling cutoff and full Koopman nilpotent Jordan structure for every even ring length give a substantive algebraic explanation of previously observed near-unitarity, rather than a finite simulation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
