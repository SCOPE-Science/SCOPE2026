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

For odd m, root-one block is k[Q8], other inversion/Frobenius blocks are full 2x2 matrices over unramified local length-four chain rings. In the Q8 block x^2=0 forces all reduced coefficients zero and x lies in central square-zero ideal (1+z)k[Q8], giving H_q=1+(q-1)z+(q^3-q)z^2+q^3(q-1)z^4. Matrix valuation strata give P_Q coefficients; orthogonal blocks add regular-image ranks, so product rank polynomial, total q^4 product(3Q^8-2Q^6), and maximum 4m follow. Independently enumerated all 65,536 matrices over F2[t]/(t^4), testing X^2=0 and F2-linear image rank by fresh elimination: lengths 0..4 counts 1,9,78,168,384 (total 640). This finite check is not the proof of arbitrary q,m; the crossed-product norm splitting and local valuation arguments supply that generality.

## originality

PASS

The complete characteristic-two square-zero left-regular rank polynomial on the odd-index dicyclic family and the quaternionic four-dimensional linear square-zero locus were not established by the inspected earlier cohomology/ghost-number papers. Dicyclic and dihedral cases must not be conflated: their principal eight-dimensional blocks differ. A 1970 general modular group algebra classification is closely relevant but could not be read fully; best-of-knowledge PASS retains explicit indirect-priority risk.

## value

PASS

Square-zero elements of modular group algebras naturally define regular-module differentials; the complete rank distribution and acyclic maximum-rank count are meaningful homological invariants. The specific quaternionic central-ideal collapse is a structural fact not a renamed general matrix enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
