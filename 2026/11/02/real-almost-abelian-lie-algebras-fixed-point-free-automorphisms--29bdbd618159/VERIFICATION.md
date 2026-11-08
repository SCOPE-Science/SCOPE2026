---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For invertible real A, V=[g(A),g(A)] is characteristic; every automorphism is v↦av+w, x↦Bx with BA=aAB and invertible a,B. Invertible A has finite nonzero eigenvalue multiset, so similarity of A and aA forces |a|=1; absence of any fixed vector requires a=-1 and 1 not in spec(B). The existence criterion is A similar over R to -A, with a generic scalar multiple of an anticommuter avoiding eigenvalue 1. Pair matched nonimaginary real-primary eigenspaces with B²=-I; on iω Jordan blocks K(z)=D conjugate(z) anticommutes with iω+N, and an even multiplicity pairs blocks by B(x,y)=(-Ky,Kx), yielding order exactly four. Necessity uses each primitive Jordan quotient ker N^j/(ker N^(j-1)+N ker N^(j+1)) of complex dimension m_{ω,j}. The induced finite-order antilinear map C=conjugate∘B has no real eigenvalue one, so its real determinant must be positive; for an invertible antilinear H conjugate its determinant has sign (-1)^m, forcing m even. A lone rotation block admits B=2 diag(1,-1), infinite order but never a finite-order fixed-free map. Exact symbolic representative matrix checks support these algebraic arguments, not an all-size enumeration.

## originality

PASS

Burde–Dekimpe arXiv:2604.27916, especially Theorems 5.4 and 5.7, studies complex solvable/almost-abelian Lie algebras and general fixed-free automorphism results, not the real imaginary-Jordan parity obstruction. Reversible-equivariant real linear operator theory of Lamb–Roberts 1999 is a highly plausible broader framework under compact reversing symmetry; its full text could not be examined because OA was unavailable and authorized Oxford returned vpn_disconnected. That creates a real unresolved historical-priority risk but is not evidence that the complete real Lie automorphism finite-order iff condition was previously stated. The result is assessed original at best knowledge with explicit risk.

## value

PASS

Fixed-point-free automorphisms of finite-dimensional real solvable Lie algebras are a natural structure problem, and finite-order versus general fixed-free existence are distinct meaningful classifications. The parity obstruction gives a complete intrinsic criterion across all invertible real Jordan structures and the minimum three-dimensional real counterexample; its order-four construction makes the distinction sharp. This is not a trivial field-substitution from complex classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
