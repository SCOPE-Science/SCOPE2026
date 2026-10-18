---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For every real t with 0<t≤1 the oriented edge relation p1+p2+p3+t p4=0 identifies dual ball K_t=[−1,1]^3 intersect |u1+u2+u3|≤t. Extreme dual vertices are permutations of (1,−1,±t), with t=1 degeneracy handled. The eight signed edge molecules are exactly primal vertices because each edge is shorter than its alternative path. The algebraic identity (t,1,−1)=(1,t,−1)−(1−t)[(1,−1,t)+(1,−1,−t)]/2, with symmetries, bounds every nonnorming extreme dual evaluation by (2−t)v(T), norming ones by v(T), and p4 is always normed. Therefore ||T||≤(2−t)v(T). The rank-one map T=φ⊗z, φ(p_i)=(1,−1/2,−1/2), z=((1−t)/(1+t))p1+(2/(1+t))p2 has ||φ||=1, ||z||=2−t, v(T)=1 by vertex enumeration. The identities and witness arithmetic were checked symbolically and against the declared finite exact parameter verifier, but the proof treats the continuous interval, not only sampled rational t. Endpoint t=1 yields index 1; t→0 limit 1/2 is not a claimed degenerate four-point metric.

## originality

PASS

Prior full weighted-cycle rigidity theorems imply n=1 at t=1 and n<1 for 0<t<1, but explicitly do not give exact subunit values. Cobollo et al determine numerical index for three-point spaces; its t→0 limit may be checked against equilateral triangle but does not cover four points. Finite-dimensional general algorithms and unit-cycle parity have no stated continuous 1/(2−t) family. This natural sharp continuous interpolation is best-of-knowledge new with residual possible hidden polyhedral formula.

## value

PASS

The simplest nontrivial one-edge perturbation of a square has a natural full one-dimensional parameter t. The formula 1/(2−t) quantifies the entire transition between square index 1 and equilateral triangle limit 1/2, including exact rate and a uniform rank-one extremizer, information not derivable from existing index-one thresholds. This is a natural complete classification of an exact Banach invariant for a geometrically motivated family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
