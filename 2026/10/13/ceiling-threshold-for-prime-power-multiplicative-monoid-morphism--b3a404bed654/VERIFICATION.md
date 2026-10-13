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
The general threshold is proved symbolically from the image of the source zero element. Because the non-\(q\) factors are units, the target class \([q]^{ev}\) vanishes modulo \(q^f\) exactly when \(ev\ge f\), equivalently \(v\ge\lceil f/e\rceil\).

The accompanying `verify.py` is an independent finite check for \(\mathbb Z/9\mathbb Z\to\mathbb Z/27\mathbb Z\). It uses \(2\) and \(3\) as multiplicative generators, enumerates every possible pair of target images, reconstructs the map on all nine source elements, and checks multiplicativity on all \(81\) ordered pairs. It obtains exactly \(19\) unital monoid homomorphisms.

The same program evaluates the source's printed stratum count as \(55\), the corrected stratum count as \(19\), and confirms that the forbidden \(v=1\) formula sends source zero to \(9\) rather than \(0\) modulo \(27\). Its captured output is in `verification.txt` and ends with `VERIFY_OK`.

No finite computation is used as proof of the general ceiling threshold. No claim is made here about unrelated assertions in the source or about revisions later than arXiv:2610.02393v1.
