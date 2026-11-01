---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

In basis 1,z^n/sqrt(n), positive-index Dirichlet matrix entries are sqrt(i/j)b_epsilon(i+j), while the zero row and column are o(1) after multiplying by epsilon in Hilbert-Schmidt norm. Beta/gamma bounds yield finite Hilbert-Schmidt sums for epsilon>0. Embed the positive indices in L²(0,infty) with intervals [epsilon log i, epsilon log(i+1)) to obtain step kernels epsilon sqrt(i/j)b_epsilon(i+j)/sqrt(ell_i ell_j). For a.e. x>y>0 they converge to e^(-x); for x<y to zero. The common C exp(-max(x,y)) square-integrable envelope proves HS convergence, hence norm/singular convergence, to Tf(x)=e^(-x)int_0^x f(y)dy. T*T kernel is e^(-2max(y,z))/2; differentiating its eigen-equation yields lambda(f_double_prime+2f_prime)+e^(-2y)f=0 and f_prime(0)=0, whose square-integrable solution e^(-y)J_1(e^(-y)/sqrt(lambda)) requires J_0(1/sqrt(lambda))=0. HS trace integral int_0^infty xe^(-2x)dx=1/4. At epsilon=0, input 1 produces divergent sum_i i/(i+1)^2. The packaged check.py was examined but its 54 recorded finite checks are not proof of this operator limit.

## originality

PASS

Best-of-knowledge comparison of exact statements and implications: Searched under weighted Hardy/Volterra/Bessel and Hankel/Dirichlet names; existing Volterra Bessel spectral formulas could already give s_k(T), but do not alone provide the nontrivial HS convergence of epsilon H_epsilon to T. Criteria for boundedness of an individual moment operator or compactness do not determine every fixed scaled singular-value limit of the approach to Lebesgue measure. A beta measure with any epsilon>0 may satisfy compactness criteria, but those alone give no 1/epsilon coefficient or fixed-k Bessel indexing; hence no demonstrated prior-result implication. The singular spectrum of the limiting Volterra operator is not itself new and is separated from the contribution.

## value

PASS

The endpoint is a real blowup in a canonical Dirichlet-space Hankel family; the result resolves the entire fixed-index singular sequence and exact Hilbert–Schmidt asymptotic, not only a norm bound. Bessel-zero constants and the limiting Volterra operator give a useful quantitative spectral model for a critical analytic Hilbert operator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
