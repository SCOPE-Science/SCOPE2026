---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For a binary order-n universal partial word with one joker at position k=1 or k=2, the k windows using it delete 2k distinct labeled edges from the binary de Bruijn graph B_{n−1}; the rest must form an Euler trail. Degree balance forces a constant postjoker block when k=1 and a two-periodic alternating block when k=2 (with n=2,3 exceptional). The random bit transition has P^{n−1}=uniform, giving each root arborescence T_n=2^{2^{n−1}−n}. For k=1 deletion of loop and root-exit edge preserves T_n per complementary prefix, so U_{n,1}=2T_n. For k=2, the remaining 3-edge Laplacian perturbation has Green-function overlap determinant α/2 with α=(1−(−1/2)^{n−2})/3, giving U_{n,2}=T_n α for n≥4 and ratio→1/6; proof handles both small endpoints separately. Independently exhaustively enumerated all partial strings for n=2,3,4 obtaining (U_{n,1},U_{n,2})=(2,0),(4,2),(32,4), consistent with theorem.

## originality

PASS

Chen–Kitaev–Mütze–Sun, On universal partial words (2016/2017) Theorems 9 and 10 show existence with joker first and second, and examples, but their inspected full primary paper does not tabulate all indexed boundary-joker words. The all-order second-position closed formula requires a rank-three tree update and parity correction; de Bruijn arborescence counts for first position are simpler and prior routine ingredients. Goeckner et al. nonbinary and Fillmore et al. cyclic results address different enumerative models. No identified prior theorem covers exact U_{n,2}; residual unindexed literature risk.

## value

PASS

Enumeration by joker placement is a natural and explicitly motivated strengthening of universal partial-word existence. The all-order second-position formula detects a parity-dependent 1/6 asymptotic penalty from shifting a single wildcard by one position. This natural infinite enumerative family is substantive despite leaving interior placements open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
