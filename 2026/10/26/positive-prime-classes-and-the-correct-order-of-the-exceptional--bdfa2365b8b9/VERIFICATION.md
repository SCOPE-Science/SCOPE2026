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

Under GRH for every Dirichlet L-function, the claimed envelope and count follow with the stated normalization. The product jump at p is Z(p)/p, so 1+sum_{p<=X} W(p)=Z(X). For p>X>=k every tail prime is coprime to k, and character orthogonality with weight 1/phi(k) cancels the principal character. The uniform nonprincipal bound in Thakur's equation (2) survives the average without a modulus-size multiplier. At X=k^(2+delta) the normalized error is O(log k/k^(delta/2)), and the subtracted product tends to 2+delta after division by e^gamma log k. The eligible prime r contributes at least 1/c-o(1) on the normalized scale: use Mertens with an arbitrary fixed relative tolerance and monotonicity of log u/u for large u, treat the finitely many small primes by their fixed positive weights, and use log phi(k)~log k. Taking delta to zero after the liminf yields 1/c-2. The primes represent different classes; PNT and omega(k)=O(log k)=o(phi(k)/log k) give the lower count, then c increases to 1/2. Thakur's nonnegative-class bound supplies the upper bound on strict positives.

## originality

PASS

The series, analytic tail estimate and upper bound are prior. The supported distinct result is the uniform positive lower envelope in small prime classes and its matching lower order for the exceptional sign count. The bounded searches did not find prior statement-level coverage of that lower result.

## value

PASS

The cited upper estimate says most signs are negative but leaves the scale of the exceptional positive set undetermined. The lower envelope identifies a uniform family of positive classes for composite as well as prime moduli and establishes that the positive exceptional set attains the scale of the upper bound. This answers a structural question about the signs without claiming a limiting count constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
