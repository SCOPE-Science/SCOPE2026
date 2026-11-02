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

The claim concerns the integral elementary-symmetric intersection V(e1,e2,e3), not naive reduction of power sums (which would make the quadratic redundant in char2). Exact independent GF(4) symbolic multiplication verifies that the parametrization [s^3:(s+t)^3:(s+ωt)^3:(s+ω²t)^3:t^3] satisfies e1=e2=e3=0. On H=e1=0 the polar form of e2 is nondegenerate, so e2 defines a smooth quadric; e3 is not identically zero there, giving a degree-six pure complete intersection. Two distinct conjugate degree-three rational curves exhaust that degree. Five explicit F2 common points and bidegrees (1,2)/(2,1) on the quadric force intersection multiplicity exactly five and ordinary transverse nodes; arithmetic genus 4 follows via the dual graph. Frobenius interchanges components, forcing counts #B(F_{2^n})=5 for odd n and 2^{n+1}-3 for even n. Zeta exp of counts is (1+T)^4/((1-T)(1-4T²)); independent projective enumeration over F2,F4,F8,F16 yields 5,5,5,29.

## originality

PASS

Qualified: primary work on Bring’s complex analytic equations and geometry does not supply the characteristic-two elementary-symmetric special fiber; the 2023 full paper explicitly excludes positive characteristic. The model choice is essential since raw power sums change scheme in characteristic 2.

## value

PASS

Determines a natural arithmetic-geometric degeneration of a canonical genus-four curve at the delicate characteristic-two prime, including exact geometric components, five nodes, arithmetic genus, stability and all extension-field counts/zeta. The distinction between valid flat elementary-symmetric model and naive power-sum reduction is mathematically essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
