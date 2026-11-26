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

The two parity layers are involutions, so F² fixes a string exactly when the two layer orders agree on it. At each site the order test compares the zero-neighbor predicate before and after the opposite parity updates; its independent 32-case evaluation gives the six stated forbidden windows. Cyclic overlap edges are in bijection with allowed labeled words and enforce the repeated boundary bit at L=4. A fixed point of F cannot have any toggle since each bit is updated only once; consequently the two parity words independently avoid cyclic 00, giving the Lucas square. Subtracting and dividing by two counts temporal orbits rather than configurations or rotations. The independent polynomial calculation gives descending nonzero-part coefficient list [1,−1,0,−1,−2,−1,0,−1,1] followed by eight zeros, and exact powers give primitive counts 2,6,26,100,350,1204,4050,13470 at L=4,6,...,18. Direct enumeration checked every configuration for even L=4 through 16. In the sextic substitute t=z+1/z to get t³−t²−4t+2, whose sign changes isolate three roots in (−2,−1), (0,1), (2,3). The last gives ρ and its inverse; it exceeds √5 because the cubic is increasing for t≥2 and has value √5−3 at √5. Therefore ρ>φ, while all eigenvalues besides ρ have modulus at most one. The trace asymptotic and Lucas subtraction follow without assumptions on zero-eigenvalue Jordan blocks. Frozen support was inspected, not executed; bounded reproduction: /tmp/opencode/record4_independent.py. Enumeration corroborates the local rule and trace, while the involution and overlap argument proves validity for all specified L.

## originality

PASS

The same local rule, parity protocol and invariant sectors are established. The distinct result is the unrestricted labeled-ring census of primitive temporal two-cycles of the fixed staggered permutation, including the forbidden-window characterization and spectral growth. The checked asynchronous orbit groups and quantum subsystem calculations do not specialize directly to this count.

## value

PASS

Primitive period two is the first nontrivial temporal recurrence sector of this natural staggered permutation. The result replaces simulation with a uniform language characterization and exact finite-size census, distinguishes its growth exponent from that of stationary configurations, and works without a nearest-neighbor exclusion. It does not claim control of higher periods or quantum transport.

The dated certificate retains the supplied scientific assessment, sources and limitations.
