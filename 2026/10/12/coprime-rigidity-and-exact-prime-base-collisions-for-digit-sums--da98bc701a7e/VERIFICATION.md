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

The infinite theorem is established by the symbolic proof in `RESULT.md`. The critical checks are:

1. For \(q>1\), \(A=s(b^\ell-1)/q\) is an integer with \(1\le A\le b^\ell-2\), so its fixed-length base-\(b\) block has digit sum at most \(\ell(b-1)-1\).
2. The exact identity \[s(b^{K\ell}-1)/q=A(1+b^\ell+\cdots+b^{(K-1)\ell})\] creates \(K\) identical blocks without carries.
3. Subtracting a fixed integer from a word made of positive identical base-\(b^\ell\) blocks changes only boundedly many low blocks; it cannot erase a deficit growing linearly in \(K\).
4. Symmetry converts the one-sided divisibility conclusion into \(a=c\).
5. In prime base, removing powers of the base prime preserves digit sums exactly and leaves coprime cores, giving the if-and-only-if classification.

`verify.py` was run from the packaged artifact directory. It returned `VERIFY_OK`. Its finite checks are regression tests, not substitutes for the proof. They cover coprime multiplier pairs in bases \(2\) through \(12\), bounded prime-base classifications for \(p\in\{2,3,5,7,11\}\), and exact repeated-block identities over a deterministic grid.

Limits: no exhaustive computation can certify the universal theorem; the proof does. No classification is asserted for arbitrary composite-base multipliers sharing factors with the base.
