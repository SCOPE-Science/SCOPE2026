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

The theorem is valid over every field of characteristic \(3\), while the exact determinant can be computed over the prime field. The seven-dimensional quotient has a basis of six matrix units and one diagonal class. Each of the \(245\) Hom–Jacobi coefficient rows is derived from three matrix commutators; fixing one diagonal scalar coefficient leaves a \(245\times48\) matrix. The selected \(48\times48\) minor in `RESULT.md` is a unit: determinant \(1\) modulo \(3\).

The program `verify.py` rebuilds that coefficient matrix, the selected minor, its determinant, the independent scalar map, and the eight-dimensional original Lie algebra's full \(448\times64\) Hom–Jacobi matrix. It reports ranks \(48\) for the quotient's fixed-scalar matrix and \(55\) for the original algebra's Hom–Jacobi matrix; these are sufficient and consistent with the symbolic descent proof. The separately implemented `crosscheck.py` uses alternate basis and rank logic and gets dimensions \(1\) and \(9\). The two programs use only Python's standard library and perform exact arithmetic modulo \(3\).

The included `verify_output.txt` and `crosscheck_output.txt` contain actual results of executing the correspondingly named programs. Both terminate with `VERIFY_OK`. The proof does not rely on an infinite search, randomized testing, or extrapolation beyond sampled fields. The composition algebra, radical, unit criterion, and idempotent criterion are established by symbolic block multiplication; the last two counts are for finite \(k=\mathbb F_{3^a}\).

Limitations: no computations classify Hom–Lie structures for other types or primes, and no independent external mathematical assessment has been performed.
