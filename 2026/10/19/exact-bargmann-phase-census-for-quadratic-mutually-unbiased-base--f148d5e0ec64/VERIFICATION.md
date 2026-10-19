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
# Reproducibility checks and limits

Run `python verify_mub.py` and `python verify_extensions.py` under a standard Python 3 installation. The first constructs the exact defining exponents in the quadratic MUB vectors and checks the resulting complex numerical inner products with an absolute error threshold below \(5\cdot10^{-8}\). It exhausts \(648\), \(15{,}000\), and \(115{,}248\) ordered distinct-base vector triples for prime dimensions \(3\), \(5\), and \(7\). It also checks the dimension-three zero Gram determinant count \(216\) and the unordered count \(36\).

The second implements field addition, multiplication, inverses, quadratic character, and absolute trace directly in the quotient \(\mathbb F_3[u]/(u^2+1)\), uses independent full vector inner products, and exhausts \(524{,}880\) ordered triples across the complete \(q+1=10\) quadratic bases in dimension \(9\). Its six multiplicity counts, in the order \((s,t)\), are \((-1,0):29160\), \((-1,1):116640\), \((-1,2):116640\), \((1,0):145800\), \((1,1):58320\), \((1,2):58320\). It checks the exact quadratic-character trace-sum vector \((2,-1,-1)\). Both standalone programs terminated with `VERIFY_OK` in the packaged source. The numeric tolerance is a finite consistency check only; exact proof for all prime powers uses Gauss identities and counting in RESULT.md. No independent external mathematical audit was performed.
