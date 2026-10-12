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

Use Python 3.8 or newer. From this directory run:

`python3 verify.py`

The program uses only the standard library and prints a `VERIFY_OK` line after completing all checks. It constructs the binary-carry local-transition tables directly from pattern counts, enumerates all 64 start phases with every admissible odd-part residue, and checks the exact rational run-start densities, the initial 145 symbols, and independently generated sequence prefixes through length \(2^{17}\). The decisive finite enumeration is exhaustive *after* the symbolic proof has reduced the infinite problem to these finitely many carry configurations. The direct long-prefix tests alone do not prove any unbounded claim.

For completeness, the only boundary cases not described by the common-prefix identity are odd parts \(1\) and \(3\), whose jump behavior becomes constant once the \(2\)-adic valuation reaches \(6\). The checker includes their exceptional jump bits among the possible local windows; they contribute zero to the limiting densities. The rational table verifies \(\sum_{\ell}\ell\delta_w(\ell)=1\) for each pattern. The proof requires ordinary binary expansions with no leading zeros and overlapping occurrences. No independently conducted audit or validation is reported.
