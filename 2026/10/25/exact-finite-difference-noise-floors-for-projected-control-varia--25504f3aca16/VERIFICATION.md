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

# Reproducibility and scope

Run `python check.py` with Python 3 and the `numpy` and `sympy` packages. The program obtains exact expectations of multivariate Gaussian polynomial monomials by parity and double-factorial moments and verifies all four one-step recurrences for \((d,k)=(2,1),(3,2),(3,1)\) with rational \(\alpha,\tau\) and nonzero starting vectors. It checks the exact algebraic stationary floor identity and strict full/restricted separation for all tested integer \(2\le d\le17\), \(1\le k<d\), at \(\alpha=1/(q+3)\), \(\tau=0.1\).

For the independent Monte Carlo diagnostic with \(d=5\), \(k=3\), \(\alpha=0.19\), \(\tau=0.13\), 20,000 trajectories and 180 steps, the exact formula gives full/restricted mean-square floors \(0.1910805382284798\) / \(0.031074193548387107\); the seeded run yielded \(0.18746766455619285\) / \(0.03082333402493489\). The Monte Carlo tolerance is 12 percent for each component. This diagnostic does not establish infinite-horizon stability or algebraic identities.

The proof in `RESULT.md` establishes the claims for all admissible integers, projectors, initial vectors and step sizes; the code is a finite test only. The claimed reference gradient is exact; code never simulates a noisy or adaptive projection oracle. No independent audit or external mathematical certification has been conducted.
