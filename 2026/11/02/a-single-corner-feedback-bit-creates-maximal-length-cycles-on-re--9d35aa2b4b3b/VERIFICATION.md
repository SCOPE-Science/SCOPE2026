---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Derive path continuants f_{2k+1}=zf_k² and f_{2k}=f_k²+f_{k−1}² in characteristic two. Since T_3 and T_{2^b−1} are nilpotent, the Kronecker-sum grid A is nilpotent. Return moments from the corner resolvent and binomial mod2 reduce to t=0 and t=2^j−2 (j=3..b). Applying determinant lemma to B=A+eeT yields det(zI−B)=z^{2n}p_b(z); p_b(0)=1 and p_b′(z)=z^{n−1}, so p_b is squarefree. Fitting splitting gives q^n recurrent points and q^{deg gcd(p_b,z^t−1)} fixed under B^t. For b=3,5 exact irreducibility checks, plus primality of 2^7−1 and 2^31−1, imply one nonzero primitive binary cycle. Independently reconstructed binary polynomials p_3=0xc1,p_4=0xc101,p_5=0xc1010001 and verified GF(2) irreducibility for degrees7 and31; inspected all three independent source verifiers and logged outcomes. This does not claim maximal cycles for all b.

## originality

PASS

Known additive-CA algebra, homogeneous multidimensional rules and hybrid 2D reversibility give background techniques, not an identified all-b characteristic polynomial and its exact one-corner recurrent census for 3×(2^b−1). The maximal b=3,5 cycle fact is more specific than generic reversibility.

## value

PASS

An unusually small local modification changes a nilpotent global cellular-automaton map into one with q^n recurrent states; 93 binary cells support a primitive cycle of length 2^31−1. The general all-b exact periodic census is a structural finite-field invariant, with clear boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
