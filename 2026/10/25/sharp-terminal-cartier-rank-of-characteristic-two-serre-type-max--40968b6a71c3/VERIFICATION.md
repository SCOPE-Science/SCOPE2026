---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For odd n=2k+3>=3, m=(2^n+1)/3, the pole semigroup <4,m> gives differential basis x^i y^j dx with j=0,1,2, 4i+jm<=3m-5. Reading RESULT.md and the actual Cartier verifier establishes transition rules (j=0 odd -> ((i-1)/2,0), j=1 odd -> ((i-1)/2,2), j=1 even -> ((i+m-1)/2,0), j=2 odd -> ((i-1)/2,1), others zero). For C^(n-1), the j=1 alternating route followed by exit to j=0 requires s≡I_{k-r} mod 4^(k-r+1) in a bounded range, uniquely yielding initial indices indexed r=0..k and terminal exponents (2*4^r-2)/3. Initial j=0 and j=2 paths fail the necessary index bounds. Terminal exponents are even, hence C^n=0, while rank(C^(n-1))=k+1=(n-1)/2>0. Semilinear nonzero images over an algebraically closed perfect field have these dimensions. Independently implemented basis transition and enumerated n=3,5,7,9,11,13,15,17 (basis sizes 3,15,63,255,1023,4095,16383,65535): all exact terminal images/ranks and subsequent vanishing checked. Finite checks corroborate only; infinite proof is the congruence and exclusion argument.

## originality

PASS

The invariant refines the known a-number of the identical Serre-type family: the rank of the last nonzero Cartier power and maximal length-n chain count are not supplied by the inspected original statement. Related all-power Cartier theorem for van der Geer–van der Vlugt curves assumes odd characteristic and different curve equations, so it does not mathematically imply this characteristic-two answer. Best-of-knowledge PASS with notable priority uncertainty because likely relevant full text was not accessible.

## value

PASS

The rank of the penultimate Cartier iterate counts maximum-length nilpotent Cartier chains and is a natural arithmetic-geometric invariant of these Jacobians, beyond their a-number. Exact uniform answer for every odd n>=3 is independently useful even though shorter blocks and full Ekedahl–Oort types are unclassified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
