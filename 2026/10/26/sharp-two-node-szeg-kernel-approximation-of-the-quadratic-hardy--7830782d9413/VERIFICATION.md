---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For the confluent or distinct two-node Szegő span, the finite Blaschke product B(z)=(z²-sz+p)/(1-conj(s)z+conj(p)z²) has model space V=H²⊖B H², so the orthogonal error of z² equals the sum of the squared moduli of its first three Taylor coefficients. Those are c0=p, c1=t=-s+p conj(s), c2=1-|p|²+conj(s)t. Setting x=|p|, y=|t| and A=1-x², Schwarz–Pick supplies 0<=y<=A. Inverting t to solve s=-(t+p conj(t))/A and bounding c2 gives error² >= x²+(1-x)u+(A-u)² with u=y²/(1-x). Completing squares gives 9/16+((2x-1)²(4x+3))/16+[u-(1-x)(x+1/2)]², valid for every pair including repeated nodes. Equality forces x=1/2,u=1/2, |t|=1/2 and phase alignment; after a common rotation the zeros are exactly (1±i)/2. That pair has c0=1/2,c1=-1/2,c2=1/4 and error²=9/16, giving captured energy 7/16. Independently verified the polynomial sum-of-squares identity exactly in SymPy and the 2×2 complex kernel Gram projection numerically to high precision. These finite calculations are checks, not the global proof.

## originality

PASS

PASS, qualified: existing Hardy n-best rational/kernel approximation sources establish model-space decompositions, existence, and lower bounds for different rational classes, but the inspected main statements do not fix the exact 9/16 optimum and all node configurations for z² in the type-(1,2) two-kernel class. A classical finite-Blaschke coefficient inequality could conceal the same special case.

## value

PASS

Two-point nonlinear Hardy kernel approximation is the first nontrivial free-node benchmark beyond one kernel. Exact optimal error and the unique right-angle equal-radius node geometry are natural, reproducible invariants needed for concrete adaptive rational approximation benchmarks. This is a self-contained exact extremal result with meaningful geometry; its value does not depend on generalizing to every degree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
