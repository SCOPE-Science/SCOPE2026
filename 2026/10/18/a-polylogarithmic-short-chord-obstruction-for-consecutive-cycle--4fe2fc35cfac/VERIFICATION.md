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
# Reproduction and limits

Run `python3 verify.py` with Python 3. No external dependencies are required. The program builds every connected vertex-set sum from exhaustive subset enumeration for all chords of \(C_n\), \(4\le n\le12\), and independently builds the right-hand side of the two-gap identity. It verifies equality in \(210\) chord cases, checks the finite multiplication-table upper bound, and tests all standard intervals in the same range.

Expected output:
`VERIFY_OK exact_chord_instances=210 upper_bound_checks=210 n_range=4..12`

The exhaustive finite checks do not prove any infinite statement. The infinite proof is given in `RESULT.md` and uses Ford's published multiplication-table estimate (as stated by Konieczny and Ford); no numerical estimate for the unspecified implied constants is claimed. The asymptotic bound applies only to the labeled cycle with **one** new non-cycle edge. Independent external audit has not been performed.
