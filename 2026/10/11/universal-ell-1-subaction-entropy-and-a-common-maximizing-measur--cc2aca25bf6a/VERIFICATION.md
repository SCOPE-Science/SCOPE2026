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

# Verification and proof boundaries

The research claim is an analytical theorem with three explicit proof checkpoints: (i) the restriction of an occurring rectangle to any monotone staircase is bijective by reversible unit-square corner flips; (ii) the translated concatenated path of an integer direction has exactly \(s d^{N(|a|+|b|)}\) distinct patterns, each of canonical measure \(1/(s d^{N(|a|+|b|)})\); (iii) every joined finite cylinder partition is dominated by a rectangle with side lengths growing at most \(|a|N+O(1)\) and \(|b|N+O(1)\). These together prove equality of topological and measure entropy in all integer directions, including coordinate-axis and negative-coordinate cases. The origin is the entropy-zero identity map.

The premise of exact regular rectangle counts and uniform cylinder measures was checked against Bondarenko--Grigorchuk--Vdovina, arXiv:2602.22356v1, Section 3. The premise that adjacent-corner completion is unique in the extendable regular matrix presentation was checked against Proposition 6. No assumption of strong mixing is used.

`python verify_staircase_entropy.py` passed 325 exact finite combinatorial checks: path-to-rectangle restriction in additive-square examples over \(\mathbb F_2\) and \(\mathbb F_3\), plus finite checks separating diagonal line projection from a full diagonal action. The code uses finite enumeration only. It does not verify all regular tile systems, all integer directions, or infinite limiting operations; those follow solely from the supplied proof.

The geometric \(\ell^1\) expression is a formula on lattice vectors, **not** an assertion about irrational-direction entropy. The result is not claimed to be independently audited.
