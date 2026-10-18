---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Use the 2026 Araya–Harada four [28,2,21]_4 projective-column seed vectors and Proposition 4.13 correspondence for [5s+3,2,4s+1]_4, s>=6. Adding a full PG(1,4) normalized projective line contributes J conjugate(J)^T=0 to the Hermitian Gram, so repeating the five-point block s-5 times preserves LCD. The four multiplicity lists have length 5s+3, minimum codeword weight 4s+1, no zero columns (dual distance>=2), and yield the four displayed weight enumerators by three scalar multiples per projective message direction. Monomial automorphisms are 3*prod_i(m_i!)*Stab_PGL(2,4)(m); PGL(2,4) acts as A5, and the multiplicity patterns have color-class partitions 2-1-2, 1-2-1-1, 3-1-1, 2-2-1 with even stabilizer orders 2,1,3,2 respectively. Thus factorial formulas A 6(s-1)!²(s+1)!(s+2)!², B 3(s-1)!s!(s+1)!²(s+2)!, C 9(s-2)!(s+1)!³(s+2)!, D 6(s-3)!(s+1)!²(s+2)!² follow. Independent GF4 implementation checked full GL(2,4) of order 180 and PGL of order 60, every color stabilizer and zero Hermitian Gram, while the inspected packaged certificate and verifier enumerate sample s=6,7,10. Exhaustiveness of the four code classes is explicitly imported from Araya–Harada, not independently proved by finite checks.

## originality

PASS

Araya–Harada 2026 Proposition 4.13 already classifies exactly four quaternary Hermitian LCD equivalence classes and prints their seed multiplicity vectors; it also uses automorphism-group orders in mass formulas and computes them via graph automorphism tools. Its inspected full article does not tabulate the four closed all-s automorphism orders. The source-specific group/order formulas need the multiplicity-preserving PGL(2,4) color stabilizers and repeated-coordinate kernels. Earlier 2020/2022 dimension-two papers provide framework but no identified closed all-s quartet. Best-of-knowledge only.

## value

PASS

Monomial automorphism-group orders are intrinsic coding invariants and appear explicitly in the mass formulas that substantiate the existing classification. The four full factorial forms for every s>=6 turn an automorphism calculation previously delegated to finite colored-graph computations into uniform, parameter-explicit symmetry data, distinguishing stable projective stabilizers 2/1/3/2. This is a natural complete four-class invariant even without a new code-construction theorem; not a free recomputation of a published numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
