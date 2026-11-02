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

# Reproduction and checks

Run `python3 verify.py` in a directory containing the included file. The program needs only the Python 3 standard library. A successful run prints `DEBRUIJN_MCS_CENSUS_VERIFY_OK` after checking all five exact histogram tables.

The code enumerates all Eulerian circuits of the binary order-\(m\) de Bruijn graph, rooted at the unique all-zero edge, for each \(1\leq m\leq5\). It verifies every cyclic length-\(m\) factor, the canonical length, and uniqueness. It checks *every closed-substring interval* and its immediate extensions, then computes the same set of endpoint pairs by a separate longest-common-prefix/next-occurrence method. Their agreement is asserted for every canonical word, not just sample inputs. The order-five enumeration list checksum, with ASCII linearizations separated by newline in depth-first zero-before-one order, is `b47b0bf70bc81346dc18f851456e7c19754b65a4a8294a61312f3b02a099ceb1`.

The order-five frequency counts sum to 2048 and the checker provides explicit minimum and maximum witnesses. This is a complete finite proof through order five, provided the elementary exhaustive algorithms are interpreted as written. It does not certify any higher-order recurrence, independent publication priority, or external validation.
