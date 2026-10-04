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
# Verification

`verify.py` reconstructs the closure exactly from the defining recurrence through generation \(27\). The sumset step is exact because bit \(m\) of the union of shifts is present if and only if \(m=a+b\) for some \(a,b\in C_n\). Each attainable sum is then mapped by the exact least-prime-factor sieve to Conway's subprime value.

The replay checks all of the following:

- the cardinality sequence through \(n=27\) against the values published by Caragiu--Vicol--Zaki;
- \(Q_n=M_n\) for every \(1\le n\le26\);
- \(|C_{26}|=105412\) and \(M_{26}=162143\);
- \(|C_{27}|=170224\), \(R_{27}=262321\), \(Q_{27}=262313\), and \(M_{27}=262331\);
- membership of \(100188\) and \(162143\) in \(C_{26}\), giving the witness \(100188+162143=262331\);
- absence of every complementary pair \(a,262321-a\) from \(C_{26}\).

For the negative certificate, \(2M_{26}=324286<2\cdot262321\), so no composite attainable sum can map under the subprime function to \(262321\). Thus the exhaustive pair-sum exclusion is sufficient.

The run emitted `VERIFY_OK`; `verification_output.txt` records the replay summary and `stage_stats.csv` records the exact statistics for each stage. No floating-point computation is used. The verification establishes only the finite claim through generation \(27\).
