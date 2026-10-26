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
# Verification details

The accompanying \(\texttt{check\_stern9.py}\) was executed with Python 3 and SymPy from the packaged file. It returned PASS after constructing the \(72\)-state transition matrix over primitive residue pairs modulo \(9\), exactly factoring its integer characteristic polynomial, proving the sextic \(q\) irreducible modulo \(17\), computing \((R(E)C)_0=116619264\), and checking exact rational Rouché disk inequalities for every one of the twelve sextic roots. It also directly counted consecutive Stern residues on the first twelve dyadic blocks.

A calculation of finite counts alone would not prove the limiting exponent. The proof's core is the exact polynomial factorization, one-root-per-disk certification, and the nonzero scalar recurrence projection, from which standard rational-generating-function theory proves the infinite limsup. The verified source date \(2017\text{-}04\text{-}18\) is the arXiv posting of the earlier Stern statistical study; the more directly relevant Deshouillers–Schinzel article is dated 2019 in its publisher's record, without a confirmed precise public day. No publication date was guessed from that year. The earlier dated paper motivates the literature period rather than claiming the modulus-nine theorem.

No independent audit has been performed. No general interval rate or publication priority is claimed.
