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

The proof was replayed from the standard compressed Fourier entry
\[
M_{\chi}(r,s)=\sum_{h\in H}\chi(h)\psi(shr).
\]
The critical structural facts are:

1. \(m\mid p+1\) implies \(\mathbb F_p^\times\subset H\).
2. \(H/\mathbb F_p^\times\) has order \((p+1)/m\), and an eligible \(\chi\) is a nontrivial character of this quotient.
3. The trace kernel in \(\mathbb F_{p^2}\) is a one-dimensional \(\mathbb F_p\)-space, hence exactly one projective line.
4. Summing the canonical additive character over the nonzero points of a projective line gives \(p-1\) on the trace-zero line and \(-1\) on every other line.
5. Quotient-character orthogonality converts those line sums into \(0\) off one \(H\)-orbit and \(p\chi(t_0)\) on that orbit.

The bundled `verify.py` uses exact modular arithmetic only. For several primes and every admissible divisor \(m\ge4\) of \(p+1\), it builds \(\mathbb F_{p^2}\), a primitive multiplicative generator, \(H\), the embedded prime-field subgroup, the projective-line quotient, and every nonzero \(H\)-orbit. It checks that exactly one orbit contains the trace-zero line and that the resulting product-orbit support is a permutation pattern. It also checks the eligible-character count.

The checker prints `VERIFY_OK`.

The computation is finite and is not used as an infinite proof. It does not test characters outside the theorem's hypothesis.
