---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS: Differentiating f=x0 u^2+2 x1 u v+x2 v^2 (char k !=2) yields J=(u^2,uv,v^2,x0u+x1v,x1u+x2v). Let A=k[x0,x1,x2], M=(u,v)/J; the graded A-presentation A(-2)^2 -> A(-1)^2 -> M has 2x2 determinant Delta=x0x2-x1^2, nonzero in A, proving injection, Hilbert series 2t/(1-t)^2 and S/J=A⊕M, giving (1+2t-2t^2)/(1-t)^3. Explicit map u->x1, v->-x0 shows M is the ideal (x0,x1) in B=A/(Delta), sheaf O_C(-p)=O_{P1}(-1); it is torsion-free rank one on smooth C and square-zero as nilpotents. Hence associated primes are (u,v) and its embedded (u,v,Delta), the ideal is saturated and J=(u,v)∩(J+(Delta)), and depth equals min(3,2)=2. The projective chart f/unit=U^2+T v^2 proves Whitney umbrella on C, transverse normal crossings off C. Independently verified derivative/determinant identities symbolically and exact modular 101 quotient dimensions d=1,..,6 equal 5,10,16,23,31,40. Infinite claims are algebraic, not inferred from those six degrees.

## originality

PASS

PASS best of knowledge: Gondim–Russo already identify the reduced singular plane and distinguished conic for this Perazzo cubic. Gharahi–Ottaviani study the conic in another geometric framework; Fiorindo–Mezzetti–Miró-Roig compute the different apolar Artinian algebra. None of the materially inspected papers explicitly supplies the Jacobian-scheme embedded prime, nilpotent theta line or its all-degree Hilbert series. The classical reduced geometry and the Perazzo model are credited, not claimed new.

## value

PASS

PASS: Reconstructing an embedded scheme structure, its sheaf as a theta-characteristic line, depth defect and precise local pinch-versus-normal-crossing transition on a classical singular cubic is a natural geometric sharpening. Its invariant is the genuine gradient scheme, not an arbitrary finite computation or trivial renaming of the known reduced conic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
