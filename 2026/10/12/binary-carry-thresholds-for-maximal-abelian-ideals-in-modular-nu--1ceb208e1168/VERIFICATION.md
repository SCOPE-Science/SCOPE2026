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

The executable `artifacts/verify.py` reconstructs the integral binomial product defining the canonical null-filiform Zinbiel algebra. It evaluates the Zinbiel coefficient identity on all triples of indices from \(1\) through \(25\), and independently checks the mod-two bit-overlap criterion for all pairs through \(256\).

The program reconstructs the least total degree of a nonzero product in each tail by searching both product orientations through indices \(1024\), and checks the theorem's \(j+t(j)\) formula for \(1\le j\le512\). It independently checks the closed \(\beta\) formula for \(2\le n\le512\).

For each \(2\le n\le6\), it explicitly constructs **every** vector subspace of \(\mathbf F_2^n\), tests both left and right ideal conditions against the full basis, and confirms that the only ideals are the \(n+1\) tails and that exactly one largest abelian ideal exists. The numbers of all subspaces are \(5,16,67,374,2825\), respectively. It also checks the unbounded-gap instances \(2\le r\le9\).

The checker output is embedded as `artifacts/verify_output.txt` and ends in `VERIFY_OK`.

These finite computations do not prove the infinite claims; the arbitrary-dimension proof is given in `RESULT.md`.
