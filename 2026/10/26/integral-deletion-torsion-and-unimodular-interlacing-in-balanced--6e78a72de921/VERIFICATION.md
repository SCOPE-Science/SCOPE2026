---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Let m=n-r+1 and rows M_{r−1}, columns M_r. For each row s the interlacing binary matrix R admits column t(s)=(s_1,...,s_{r−1},m−1); lexicographic ordering makes the selected square minor unit triangular, proving a Z-right inverse. For weighted deletion, represent each multiset by a monomial; E is D=sum_i partial/partial x_i on homogeneous degree r. The integer unimodular substitution y_0=x_0, y_i=x_i−x_0 turns D into partial/partial y_0 in every degree. Thus its integral diagonal coefficients are j with multiplicity binom(n−j−1,r−j), j=1..r when r<n. This proves the stated cokernel cyclic summands (not necessarily ordered Smith factors) and the characteristic-p rank formula sum_{p∤j}binom(n−j−1,r−j), full iff p>r. At r=n, E=[n],R=[1], including the degenerate single-symbol boundary. Independent direct multiset enumeration, modular ranks and Smith comparisons verified all 21 n,r pairs 1<=r<=n<=6, but only the integral argument proves the universal classification.

## originality

PASS

The directly relevant Higgins 2026 paper identifies the same deletion multiplicities, interlacing relation and balanced row/column sums but its inspected Sections 2–3 do not provide the integer cokernel, characteristic-p ranks or a unimodular maximal minor. Cai–Stanley's Young lattice DU Smith theorem concerns a different graded operator. Search also considered symmetric-power differentiation and subset-incidence Smith identities; a classical implicit polynomial-derivation computation may cover the new formula and remains a real risk, but no stronger examined statement forces it.

## value

PASS

Integral cokernels and all-characteristic ranks are natural invariants of the exact balanced multiset weighting. The sharp disagreement between weighted deletion and unimodular binary interlacing identifies a substantive arithmetic obstruction invisible from balanced margins and real singular values; the proof is an all-parameter structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
