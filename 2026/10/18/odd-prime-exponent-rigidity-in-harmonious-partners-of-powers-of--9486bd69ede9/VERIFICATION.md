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

# Verification and limits

The exact theorem is in `RESULT.md`; a proof checklist is in `REVIEW.md`. Run `python3 verify.py` using Python 3 standard library only. The checker evaluates the original harmonious-pair identity by independently computing divisor-sum factors for every \(1\leq k,r\leq16\), \(1\leq s\leq6\), and each odd prime \(p\leq997\). There are 256,512 exact cases and four true instances. A second, independently structured check computes the divisor sum by enumerating divisors directly for 576 smaller parameter profiles. Successful output begins `VERIFY_OK`.

The infinite assertion rests on the deductive proof, not on a finite test. Required noncomputational checks: (i) strict lower bound when \(k=1\); (ii) denominator coprimalities that imply \(2^k-1\mid p^s\); (iii) exclusion of \(2^k-1\) as a proper perfect power via residues modulo 8 and an odd cofactor; (iv) the exact integer relation \(2p+1=t(p^{s-1}+2\sum_{i=0}^{s-2}p^i)\), including the empty-sum convention at \(s=1\); and (v) reverse substitution. The code provides supporting finite evidence only, and neither exhaustively searches literature nor proves infinite statements.

The full primary paper and a related preprint were read for claim comparisons. The closest indexed prior exact theorem covers only the prime-odd-part subcase; its summary was inspected, but not a complete manuscript. Independent audit has not been performed.
