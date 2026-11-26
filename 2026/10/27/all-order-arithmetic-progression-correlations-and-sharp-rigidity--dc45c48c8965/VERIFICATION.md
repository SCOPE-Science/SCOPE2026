---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The parity identities s_(2n)=1 and s_(2n+1)=-s_n give the stated binary substitution starting with +1. For fixed m and h, outside at most m residue classes modulo 2^L all valuations in the product are known from the residue, so the Cesaro and Haar averages differ from the same finite-cylinder average by at most 2m/2^L in the limit. Odd-unit scaling removes the odd part of h; for a=v2(h), outside 2^a Z_2 all the valuations equal that of x, and inside it a factor (-1)^(am) appears. This gives the even and odd formulas with the subgroup weight 2^-a and mean 1/3. Splitting the unit-step integral by parity yields exactly the stated block-length recursion. Strong induction gives the bound and reduces even sharp lengths by halving. For odd m>=5 both lower indices must be sharp; the ordered sharp candidates are 1,2,3,4,6,8,12,16,..., with gaps at least two after 4. Thus only m=5 or 7 could be sharp in this range, and both terms vanish there. The signs propagate from 1 and 3. For even h the lower bound is sharp only at a=1 and c_m=-1/3, namely the stated powers of two greater than one. The two parity ranges meet at the threshold; no strict uniform separation is asserted.

## originality

PASS

Motivated by known all-factor frequencies, higher-point integrals, and exact pair and triple laws, the distinct contribution is the explicit reduced progression recurrence together with the uniform sharp order classification and spacing threshold. Exact moments as unevaluated finite sums and the low-order specializations are not independently new. None of the inspected stronger formulas gives the reduced order law or mechanically classifies its extremizers as a uniform consequence.

## value

PASS

The reduction to order and 2-adic step valuation gives a short exact evaluator usable without constructing the much longer words spanned by the progression. The sharp extremizers and boundary parity law turn fixed low-order data or general integral representations into an interpretable all-order dependence result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
