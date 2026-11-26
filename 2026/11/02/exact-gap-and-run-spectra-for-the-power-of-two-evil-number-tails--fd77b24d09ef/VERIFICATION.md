---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The minimum generator m=2q+1 prevents any two-generator sum below 4q+2. In the conductor interval, with n=4q+t, odd digit parity of t gives a generator; even parity for t<2q gives two evil generators by partitioning its ones into two odd-sized sets. The endpoint t=2q+1 is represented using a=2^j and b=2q+1-a, with j=1 for even r and j=2 for odd r; both have odd parity and lie strictly between 0 and 2q. One complete residue interval modulo m is therefore present. Binary parity balances the upper gap band, giving genus 3q. In the upper band the Thue–Morse recurrences exclude triples; singletons correspond to 00 pairs at even sites and 11 pairs at odd sites in the halved prefix. The recurrence E_r=2^(r-1)-1-E_(r-1) counts these, and the last gap contributes an extra singleton exactly for even r. Pairing the remaining upper-band gaps gives R2 and the ratio tends to 1/9. A separate reachability replay agreed for r=2 through 10 (6,132 gaps and 4,106 candidate generators); the supplied verifier was inspected but not executed.

## originality

PASS

The supported contribution is the semigroup run spectrum, including the exact parity-dependent boundary effect. The evil-tail object, the Frobenius problem and general membership machinery are already established. Once F=4q is given for this subfamily, the gap set itself follows immediately from the minimum generator, so I do not treat it as independent novelty relative to that Frobenius specialization. Neither the inspected evil-tail literature nor the closest indexed gap-run result states or directly yields the exact run frequencies without separately analyzing adjacency and the terminal gap.

## value

PASS

The power-of-two threshold is natural for a binary-digit generator family. Its exact maximal-run spectrum separates the large initial block from the short holes, quantifies the persistent parity correction and gives the limiting isolated-gap fraction. This measures clustering, rather than simply recomputing the conductor or genus. The calculation is elementary but uses the structure of the interior and the endpoint, not a renaming of a bound on the largest gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
