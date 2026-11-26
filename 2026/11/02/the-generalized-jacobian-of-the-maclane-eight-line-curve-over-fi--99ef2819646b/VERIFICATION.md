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

Write the three line families as X=ω^aY (a=1,2), Y=ω^bZ, Z=ω^cX (b,c=0,1,2). Mixed triples with one per family concur exactly for a+b+c=0 modulo 3, giving six points. The two three-line pencils give the other two triples. In a triple with two lines of the same family and one of another, the determinant is a unit times a difference of distinct cube roots; the nonzero one-per-family determinants are also such differences. Their norm is 3, so the list is stable in every allowed characteristic, including 2. The remaining four intersections are double; the normalization graph has 20 vertices and 32 edges. Ordinary triple points have a single extra first-jet discrepancy after identifying constants: restricting linear forms to the three distinct tangent directions has rank 2, and quadratic forms have rank 3 on their three branch jets, so all higher jets can be realized independently. Normalization units therefore give one vector-group line per triple point, with linear descent on those lines; double points contribute only constants. This gives U(k)=(k,+)^8. The character lattice of the gluing torus is the kernel of the oriented incidence boundary, since gluing constants are taken modulo line and singular-point constants. An independent integral verification does not need the frozen determinant: in the nonsplit graph the fixed part consists of the path 234–L_2–25–L_5–567 and the isolated point 01. Contract this fixed forest equivariantly. Two fixed vertices and seven free orbits of vertices remain, with 14 free edge orbits. In the connected orbit graph choose a spanning forest rooted at the two fixed vertices (each other vertex has one edge toward its root); its lift is a forest, since each child has a unique lifted parent edge. Contract it. The two surviving fixed vertices have seven free edge pairs, at least one joining them. With compatible orientations the boundary on the remaining Z[C_2]^7 is augmentation on each crossing summand and zero on loop summands. Subtract a chosen crossing summand from the others by an integral equivariant basis change; the kernel is the augmentation ideal Z_- plus six regular summands. This proves the actual integral torus and not merely its isogeny type. Split Frobenius fixes all 13 cycles. Lang vanishing makes the rational-point extension exact and the p-primary and prime-to-p factors split as finite abelian groups. For nonsplit Frobenius the fixed component/point/branch counts are (2,4,4), giving two-cycle counts (3,4,14); in the split case they are (8,12,32). Subtracting normalized branches and adding singular points gives both point counts and zeta functions. The genus is 21 by the plane degree formula (also 8·3+4−8+1). The frozen certificate and output were inspected, not executed; the integral result was checked by the independent contraction argument.

## originality

PASS

The arrangement and the general Picard and normalization mechanisms are established; the supported distinction is the explicit integral Frobenius module and exact rational Picard group of the original reduced plane divisor, including its additive part. The evaluated zeta function is a straightforward companion from known incidence, not by itself the basis for the pass. The inspected strongest matches do not give the full calculation. This does not certify priority.

## value

PASS

The MacLane curve is a distinguished nonrealizable-over-R line arrangement whose finite-field forms naturally vary with the cube roots of unity. The result distinguishes actual torus types and finite abelian groups, not just dimensions or zeta-determined orders. It also isolates the additive effect of the triple crossings, which a nodal replacement loses. These are useful exact arithmetic invariants of the original curve; the routine zeta calculation serves as a companion rather than the sole value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
