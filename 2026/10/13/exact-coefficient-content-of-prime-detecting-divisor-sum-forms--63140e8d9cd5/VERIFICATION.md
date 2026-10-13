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

# Verification record

The coefficient identity is reproduced in `RESULT.md` for all integer \(1\le k<\ell\) and \(n\ge2\). Exact symbolic checks are the evaluation
\[
c_{k,\ell}(p^2)=(p^k-p^\ell)(1-p^{k+\ell})
\]
and the two congruence-preserving manipulations of divisor sums under multiplication by powers of \(p\). The critical reverse implication uses Möbius inversion on the divisor poset of \(p\)-coprime inputs. The prime-power fixed-divisor exponents are checked against Carmichael group exponents, including \(\lambda(2)=1\), \(\lambda(4)=2\), and \(\lambda(2^j)=2^{j-2}\) for \(j\ge3\).

Run `python3 verify.py`. It uses only standard Python and calculates the coefficients independently by direct divisor enumeration and multiplicative factorization. It checks every exponent pair \(1\le k\le8\), \(k<\ell\le12\) for indices \(2\le n\le180\), verifies observed gcds against the theorem, and checks prime-square identities for selected primes. The actual output is `verification_output.txt`.

The finite program is not an exhaustive certificate for the infinite parameter theorem; the fully quantified argument is in `RESULT.md`. It does not check the excluded constant term or imply scientific validation by a separate auditor.
