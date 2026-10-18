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
# Reproducibility and verification

`verify.py` is a self-contained Python 3 standard-library script. Execute `python3 verify.py` in a directory containing the extracted code. The saved exact output is `verification_output.txt`.

For each odd prime \(7\le P\le101\), the script generates the primes less than \(h=P-1\), constructs the exact CRT residue class modulo their product for every subset of \(U_h\), verifies the two endpoint gcds equal one, and directly computes all surviving interior positions using integer gcd. The set of positions \(i+1\) is tested against the selected subset; pairwise distinct residues are checked.

The script tested 4,042 subset patterns at 23 prime anchors. A second implementation explicitly enumerates every residue modulo \(Q_h\) for \(h=6,10,12,16,18\) and checks the lower binomial count for every supported value.

The universal assertions are established by the written proof, not these finite tests. The prime-number-theorem step supplies unbounded numbers of toggleable primes; positive singular-series weights and convergence of the defining cumulative constants supply strictness. No claim of independent external validation is made.
