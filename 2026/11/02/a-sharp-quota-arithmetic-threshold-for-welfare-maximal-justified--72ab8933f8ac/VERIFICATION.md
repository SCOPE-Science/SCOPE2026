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

# Reproducible verification

Run `python3 verify_sparse_jr.py` from the directory containing this document. The script uses only Python 3 standard-library modules. It enumerates anonymous approval profiles exactly over the following bounded domains:

- Three seats; ballots of size one or two; four candidates and one through twelve voters.
- Three seats; ballots of size one or two; five candidates and one through six voters.
- Two seats; ballots of size one or two; four candidates through nine voters and five candidates through six voters.
- Three seats; singleton ballots; five candidates through ten voters.

It additionally verifies the four-candidate counterexample construction for every population \(1\le n\le100\), and confirms it is incompatible exactly when \(2n\ge5\lceil n/3\rceil+3\).

A successful complete run prints `VERIFY_OK anonymous_profiles 850550 witness_range 100`. At the first noncompatible size \(n=9\), the exhaustive four-candidate test found four anonymous profiles with no welfare-optimal JR committee. For \(n=10\) and \(n=11\), it found none; at \(n=12\), it found 24.

The analytical argument in `RESULT.md` establishes the universally quantified result; the finite code alone does not prove untested sizes or unrestricted candidate counts. No external or independent scientific audit is claimed.
