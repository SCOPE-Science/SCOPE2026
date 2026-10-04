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

The verification replays the claim on direct finite products of local rings rather than on an abstract graph template.

For a factor \(\mathbb Z/p^e\mathbb Z\), the checker constructs all ring elements, recognizes units coordinatewise, forms the nonzero zero-divisors, and adds an edge exactly when the coordinatewise product is zero. It then exhaustively searches for minimum total and paired dominating sets up to the claimed size.

Separately, it constructs the proof witnesses: in a nonfield factor it uses the socle element \(p^{e-1}\), while in a field factor it uses \(1\). It confirms that the coordinate-supported witnesses form a total-dominating clique and that the odd-factor augmentation has a perfect matching.

Exact output:

```text
VERIFY_OK
factors=((2, 2), (2, 1)) vertices=5 gamma_t=2 gamma_pr=2 witness=2
factors=((2, 2), (3, 1)) vertices=7 gamma_t=2 gamma_pr=2 witness=2
factors=((2, 3), (3, 1)) vertices=15 gamma_t=2 gamma_pr=2 witness=2
factors=((2, 2), (2, 1), (2, 1)) vertices=13 gamma_t=3 gamma_pr=4 witness=4
factors=((2, 2), (3, 1), (2, 1)) vertices=19 gamma_t=3 gamma_pr=4 witness=4
factors=((2, 3), (2, 1), (3, 1)) vertices=39 gamma_t=3 gamma_pr=4 witness=4
factors=((2, 2), (2, 1), (2, 1), (2, 1)) vertices=29 gamma_t=4 gamma_pr=4 witness=4
```

The examples include two-, three-, and four-factor nonreduced rings. These checks are corroborative only; the general theorem follows from the Artinian local decomposition, the socle-annihilation argument, and the published domination lower bound.
