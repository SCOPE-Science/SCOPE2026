---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On four consecutive sites the weighted row Gram entries are moments of orders −3 through 3. The normalized moments are δ_{t0}; rank forces at least four distinct nodes. For 4≤m≤6, apply this quadrature to z^(−3) z^(6−m)∏(z−z_j): the expression vanishes on the support but its constant Laurent coefficient is −e_3. Thus e_3=0, and evaluating the prime-power cyclotomic divisibility of its sum mask at one gives p dividing 4, 10 or 20, respectively. This rules out precisely the smaller sizes needed in the p=3 and p≥7 branches and rules out four for p=5. Uniform subgroup rules attain four and five, and the uniform average of the six real sine/cosine coordinates is zero; Carathéodory reduces it to at most seven nodes with positive weights after discarding zeros. For m=4 the square Parseval matrix is unitary, giving w=1/4 and ratios among the fourth roots. For the five-node branch e_3/∏z_j is the inverse-pair-product sum. Divisibility by Φ_(5^k) gives equal mask coefficients in the five lifts of each residue mod H=5^(k−1), since the quotient has degree <H. Pair-sum class populations are therefore multiples of five, with at most two occupied classes. Three different site residues would produce three distinct sums. Two residues, each repeated, give three sums since H is odd, while a 1+4 split gives counts 4 and 6. All five sites must be the same mod H, a full coset by distinctness. Fourier inversion then gives equal weights (orders ±1,±2,±3 cover the nontrivial order-five characters). The argument includes H=1 and the smallest allowed cycles. It does not classify all seven-node rules. Independent replay `python /workspace/review_checks/frozen_probes.py` used monic polynomial long division on 53,529 masks; the only zero masks in these tested families were the five order-25 cosets. This checks the obstruction on the enumerated families only; the proof supplies the uniform claims.

## originality

PASS

The four-site weighted 4/5/7 law and prime-five coset rigidity are distinct from the best inspected mathematics. The two low-prime cardinalities also follow in part from known ingredients (e.g. the rank lower bound and unweighted subgroup construction at p=2); no independent novelty is attributed to those ingredients. One later eleven-cycle result overlaps exactly at N=11 and strengthens the support classification there; it does not cover the uniform theorem.

## value

PASS

The exact minimum counts physical Fourier measurements needed to obtain a perfectly conditioned four-site frame when gains can vary. This is a natural fixed moment problem, and the prime-five rigidity and gap between weighted and equal-weight minima distinguish arithmetic effects that are not given by the generic rank and Carathéodory bounds. The complete prime-power law is useful even without classifying all seven-node supports.

The dated certificate retains the supplied scientific assessment, sources and limitations.
