---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the three-generated CI gluing, write U=<b,c> and S=aU+dN_0. Since d is in U and gcd(a,d)=1, the least element in each residue class modulo d is a times the corresponding least representative from U, with residue permuted by a. This gives F=a(bc-b-c)+(a-1)d. If m=d, use a>=m/b and bc-b-c>=b^2-b-1 to get m[b+(m-1)/b-2]>=2m sqrt(m-1)-2m. If m=ab, then d>=m and the bound is m(a+b-2)-a>=2m sqrt(m)-(5/2)m, since b>=2. For the upper bound take b=floor(sqrt(m)), c=b+1. For m>=4, m exceeds the two-generator Frobenius number and both minimal generators, so it is a nonminimal positive element of U. A coprime a>m/b yields a valid minimal gluing with multiplicity m. Inclusion–exclusion over squarefree divisors loses at most 2^omega(m), whereas (4^omega(m)+1) phi(m)/m exceeds that loss. The factorial lower bound on the product of distinct prime divisors gives 4^omega(m)=m^{o(1)}, hence the witness has a,b~sqrt(m) along all m and the Frobenius ratio tends to 2. The lower bound matches and symmetry gives g=(F+1)/2 pointwise and for the minima. At m=4 the claimed class is nonempty (for instance <4,6,9> is the gluing with a=3,b=2,c=3,d=4).

## originality

PASS

Classical gluing and individual Frobenius expressions are known, and an indexed result gives a stronger exact optimum on the square-multiplicity subfamily. The supported distinct claim is a limit through every integer multiplicity, with explicit two-sided estimates and a uniform coprimality-window construction, not an exact optimum or a claim of priority for the square slice.

## value

PASS

The complete-intersection restriction changes the admissible class materially, and the fixed-multiplicity question is independently motivated. The theorem supplies the optimal leading constants through all multiplicities, including arbitrary prime factorizations not controlled by the square optima, plus explicit witnesses and a uniform lower bound. The value is the sharp extremal law over the whole class, not the known gluing formula or the affine genus conversion alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
