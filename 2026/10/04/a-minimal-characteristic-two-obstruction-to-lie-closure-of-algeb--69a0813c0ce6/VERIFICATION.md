---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The displayed matrices reconstruct exactly. In characteristic \(2\), for \(B=egin{pmatrix}1&1\0&1\end{pmatrix}\) and \(C=egin{pmatrix}1&0\1&0\end{pmatrix}\), direct multiplication gives \([B,C]=B\), so \(E=kB+kC\) is Lie closed. For \(v=(x,y)^{\mathsf T}\), the parameter-to-value matrix is \(egin{pmatrix}x+y&x\y&x\end{pmatrix}\) with determinant \(x^2\); hence only the direction \(x=0\) constrains the algebraic reflexive hull, yielding exactly \(\operatorname{Ref}_a(E)=\{egin{pmatrix}a&b\c&b\end{pmatrix}\}\). The two submitted hull elements have commutator \(egin{pmatrix}1&0\1&1\end{pmatrix}\), which violates that equation. Dimension \(1\) is impossible because its endomorphism algebra is commutative.

## originality

PASS

The closest primary theorem is explicitly proved in the finite-dimensional complex setting. Its key normalizer lemma uses matrix exponentials and differentiation, and it does not state a positive-characteristic extension. Fresh Resultary and literature searches for the characteristic-two hull equation, low-dimensional counterexamples and equivalent operator-space formulations found the submitted record itself and unrelated characteristic-two results, but no earlier statement that covers this example. This is therefore original on a best-of-knowledge basis, with older algebraic-reflexivity terminology retained as the main residual risk.

## value

PASS

This is a motivated sharp boundary to a newly stated structural theorem: characteristic-free Lie closure fails over every characteristic-two field and already in the smallest possible vector-space dimension. The exact hull computation exposes the mechanism rather than merely reporting a finite-field example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
