---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A positive transition matrix permits the Kolmogorov criterion; the three-configuration cycle all-minus, one-plus and two-adjacent-plus gives forward/backward ratio ((1-p)/p)^2 for each N>=3, with a separate N=3 factorization. Hence p=1/2 is necessary. On that line write local transition as exp[b t_i(s_{i-1}+s_{i+1})]/(2 cosh[b(s_{i-1}+s_{i+1})]), b=atanh(2r-1)/2; multiplying the product kernel by W(s)=∏2cosh[b(s_{i-1}+s_{i+1})] makes a symmetric bilinear two-time exponent, proving detailed balance and uniqueness. Expanding W gives J=-log(4r(1-r))/4 coupled sites distance two. The graph splits into two disjoint length N/2 cycles for even N and one length N for odd N. The Ising transfer matrix eigenvalues 2cosh J,2sinh J yield C_k=(q^k+q^(m-k))/(1+q^m), susceptibility, strict even/odd independence and nearest-neighbor zero on even N. With N sqrt(1-r)->xi for odd sizes, q^N->exp(-4xi), giving sech(2xi). Finite N checks are corroboration, not universal proof; degeneracies r=1/2 and N=3 handled by the same algebra.

## originality

PASS

Best-of-knowledge originality PASS after searches and real statement-level primary comparisons; no source found to imply the exact final claim. Explicit historical/inaccessible-source risks remain: Older general reversible PCA classifications and finite-size Ising parity studies might imply components in another parameterization; complete 2019/2020 article not read.; Only N>=3 and interior p,r; deterministic boundaries and off-line invariant measures are outside scope.

## value

PASS

The original family was analytically solved only at small ring sizes; the exact one-parameter reversible subfamily has an all-size stationary law, all two-point correlations and a striking odd/even weak-noise crossover. Both necessity and observables are mathematically motivated and more than routine rephrasing of known Ising transfer matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
