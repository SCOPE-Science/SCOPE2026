---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For S=Fq[[X,Y]], f order a>=2, any finite-length m quotient M satisfies m^m M=0. Hence S^n and (S/f)^n quotient kernels agree for m<=a. At m=a+1 every quotient where f acts nontrivially must have one-dimensional successive maximal-ideal layers, and is necessarily cyclic curvilinear Fq[t]/(t^(a+1)). Each tangent direction [u:v] in P1(Fq) has q^(a-1) such ideals; f annihilates iff initial homogeneous form f_a(u,v)=0. For each excluded ideal, surjective n-frames modulo unit-group yield q^(a(n-1))*(q^n-1)/(q-1) distinct kernels, so the exact deficit is (q+1-Nq(f_a))*q^(an-1)*[n]_q. For f=Y^a-X^b with a<b coprime, Nq=1 and the correction is q^(an)*[n]_q>0. Independently enumerated all commuting nilpotent 3x3 F2 pairs and generating one/two-frames: ambient counts (7,99), cusp (3,51), split node (5,75), anisotropic tangent (1,27), all matching formula. No schematic or motivic assertion.

## originality

PASS

Huang–Jiang–Oblomkov arXiv:2608.16086 provides motivic Quot series over torus-knot singularities mainly for the normalization module; the harder free R^n family is distinguished. Huang–Jiang arXiv:2312.12528 has arbitrary-rank results for multiplicity-two curves, special cases of the present formula, but not an arbitrary leading homogeneous f_a and a>=2 universal direction count. Smooth-ambient Hilbert/Quot coefficients are also prior. The all-leading-form first relation-sensitive point correction is distinct though an older curvilinear Hilbert-scheme lemma might imply it.

## value

PASS

Colength a+1 is an intrinsic first threshold where a curve equation of multiplicity a can affect punctual Quot counts. The sharp universal correction extracts the count of rational projective tangent-cone directions for arbitrary rank, degree and finite field; the torus-knot subfamily shows genuine strict onset. It offers an exact useful invariant of singular curve branches without pretending to determine the rest of the Quot series.

The dated certificate retains the supplied scientific assessment, sources and limitations.
