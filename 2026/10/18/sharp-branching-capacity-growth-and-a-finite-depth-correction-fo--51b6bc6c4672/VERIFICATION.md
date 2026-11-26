---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The repaired theorem keeps the all-p counting-measure limit. The level j output p-norm is bounded by Minkowski on the ancestor extensions (multiplicity b^(j-i) at level j) and by Hölder on the level masses. For S_j=sum_(i<=j) b^(-i/(p-1)), this bounds the p-th power of the norm above by sum b^j S_j^(p-1). The common radial input g(v)=b^(-|v|/(p-1)) gives the lower bound (sum b^j S_j^p)/S_N. With k=N-j, the normalized weights are b^(-k-1); bounded convergence for this summable sequence gives the same limit S_infinity^(p-1)/(b-1) from both sides, with b and p fixed. The demonstrated b=4,p=3,N=2 bounds are exact. The dropped Hilbert claims are not mathematically false: the inverse grounded branch matrix is strictly positive, giving a simple radial least eigenvalue, hence exact multiplicity b by direct sum. For large N the Rayleigh bound and the roots of the radial equation give t=1-r_+=O_b(q) for q=b^(-N-1), with t((1-t)^(2N+1)+bq)=(b-1)q and lambda=(b-1)t-t^2+O_b(t^3). Expanding gives the stated relative coefficient 2N(b-1)-2 and error O_b(N^2 q^2), and the reciprocal square root gives the claimed norm correction. The frozen line 73 contains a stray character before the large parenthesis, not a substantive mathematical error. Independent branch matrices for b=2,3 at N=5 agree with the secular values, and finite p-bound checks are consistent with the repaired theorem.

## originality

PASS

Best of current evidence for the narrowed claim: the sharp fixed-p counting-measure norm equivalent survives. Do not count the original Hilbert subclaim as a distinct contribution: the exact binary grounded block and leading correction scale are prior, and the all-b Hilbert correction is a routine expansion of an exact specialization of an earlier tridiagonal spectral theorem. The absolute correction constant is not explicitly stated in the binary bounds alone.

## value

PASS

The repaired result identifies the exact branching growth factor for an unweighted discrete Hardy norm over all fixed interior exponents. It links the geometric mass of the last levels to a single radial input that asymptotically saturates all the dominant levels, which goes beyond a nonsharp norm bound or a Hilbert spectral computation. It gives a sharp reference constant in a natural family without counting already-covered spectral deductions as a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
