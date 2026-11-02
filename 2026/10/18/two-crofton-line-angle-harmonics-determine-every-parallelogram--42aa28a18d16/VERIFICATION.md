---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Using the actual seven-file source package at commit 3592338, the exact conditional direction density is W(theta)/(2(a+b)) with W=a|sin(theta)|+b|sin(theta-phi)|, because the offset interval has length W and integral W=2(a+b). The Fourier integral of absolute sine equals -2/(4k^2-1), so m_k=-(a+b exp(2ik phi))/((a+b)(4k^2-1)). For two independent hit-conditioned lines, T_k=|m_k|^2=(1-4p(1-p)sin^2(k phi))/(4k^2-1)^2, giving an absolutely convergent Fourier expansion. With q=4p(1-p)sin^2 phi and s=sin^2 phi, q∈(0,s], s∈(0,1], A=1-q, B=1-4q(1-s); B-(2A-1)^2=4q(s-q)≥0 and B≤1. Conversely the sharp region with A<1 yields unique s=1-(1-B)/(4(1-A)), p=(1+sqrt(1-(1-A)/s))/2, phi=arcsin sqrt(s), including the square (A,B)=(0,1), rectangle upper boundary and rhombus lower boundary. A rectangle (2,1,pi/2) and rhombus (1,1,arcsin(2sqrt2/3)) both have T1=1/81 but distinct T2=1/225 and 49/18225, proving minimality. Independent symbolic elimination (3 identities), exact rational counterexample, and midpoint integrations across 40 seeded shapes/80 quadratures agree with the claim, max numerical error 5.01e-8; these are only corroboration of the general proof. No sampling error/stability result is claimed.

## originality

PASS

Best-of-knowledge the precise minimal two-Crofton-angle-harmonic parallelogram inverse and sharp feasible parabola are not stated in inspected primary literature; HOWEVER the same general line-pair Fourier forward law is expressly prior work of Cufi--Gallego--Reventos (2019), confirmed by Hug--Schneider (2020). Novelty credit is limited to the finite two-observable inverse, its image/equality geometry, and exact one-observable impossibility; those are close algebraic consequences of known harmonic methods, so originality is qualified. No unconditional priority/certification claim.

## value

PASS

The input is a natural motion-invariant stereological experiment, and the output gives a sharp identification/minimality result for the two-dimensional similarity-moduli space of nondegenerate parallelograms using only unlabeled relative line angles. The exact parabolic image is a realizability criterion, with geometric boundary classes rectangles and rhombi, not merely a recomputation of a table. A researcher analyzing random line incidence can need the two lowest normalized angular moments rather than full directional distributions. Mathematical depth is modest because the general forward pair-line Fourier formula was known in 2019 and the inverse is a two-variable elimination; the specific exact inverse is nonetheless a motivated, self-contained natural classification. No broad polygon identification or statistical stability theorem is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
