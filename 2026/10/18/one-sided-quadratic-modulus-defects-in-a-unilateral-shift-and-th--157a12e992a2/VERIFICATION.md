---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For bounded A=A*>=aI and B=B*, the norm Fréchet derivative of (A²+i t[A,B]+t²B²)^{1/2} solves AL+LA=i[A,B] via Sylvester inverse ∫e^{-uA}De^{-uA}du. Lipschitzness of self-adjoint positive-part norm gives d_±(t)=t||(±L)_+||+O(t²). In finite dimensions nonzero traceless L has both signs. For unilateral shift S, A=2I+(S+S*)/2>=I, X=I-(S-S*)/(2i), B=AX+XA, exact commutator i[A,X]=-P0/2 gives d_+(t)=O(t²), d_-(t)=t/2+O(t²). Approximate constant unit vectors v_N at the top spectral endpoint give ||A+i t B||>=3sqrt(1+4t²) and d_+(t)>=3(sqrt(1+4t²)-1), hence exact quadratic order. For nilpotent finite S_n, L_n=(P_last-P0)/2 has both one-sided slopes 1/2 for n>=2. Independent NumPy matrices for n=2,3,6,20 verified this commutator and Sylvester equation to machine precision; finite tests are not proof of infinite rank.

## originality

PASS

Fong–Tsui exact zero-defect results and quantitative ε bounds concern ||Im T|| vs modulus defect for classes of real parts; earlier published flat-modulus A and normal T results do not imply perturbative one-sided defect *slopes*, especially for noncommuting spectral-interval A or the finite/infinite shift dichotomy. General square-root Fréchet differentiation is acknowledged as standard.

## value

PASS

The trace obstruction to one-sided first-order modulus defects in finite dimensions fails at a natural unilateral shift boundary, producing a striking rigorous Θ(t²) versus Θ(t) asymmetry, while every finite truncation restores slopes 1/2. This is a motivated structural counterexample in nonnormal operator theory, with a clear finite/infinite limitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
