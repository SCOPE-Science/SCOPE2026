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

Let R(z)=1−z+z²/2−z³/6+z⁴/24 and φ(z)=(1−R(z))/z, with φ(0)=1. The scalar R is strictly positive by the sum of squares in RESULT.md lines 63–67, so the symmetric matrix has positive diagonal. For a nonedge, solving I=E_0+E_r+E_s and L=αE_r+βE_s gives E_r=−β/[v(β−α)] and E_s=α/[v(β−α)] at that entry. The entry of T(h) is then αβh[φ(αh)−φ(βh)]/[v(β−α)]>0 for h>0, because φ'<0 by its strictly negative discriminant. For an edge, the projectors give the stated u and −w. The complement degree bound gives β≤v and u≥0, with equality exactly for disconnected complement. Such a complement is a union of equally sized cliques: nonadjacent pairs in different components have no common neighbors, so the constant nonadjacent intersection number is zero and each component is a clique. Write U=uα≥0 and V=wβ=1+U. Then the edge entry is h C_G(h)=h[Vφ(βh)−Uφ(αh)]. In addition to the frozen derivative proof, λφ'(λh) strictly decreases in λ>0 since φ'(z)+zφ''(z)=−1/2+2z/3−3z²/8<0. Thus C_G'<0 and its negative leading term forces one positive cutoff. At h=1/k the expansion in powers of A/k in lines 103–107 gives strictly positive edge entries. The positive scalar R is ≤1 precisely on [0,ρ], giving spectral contractivity exactly up to ρ/β. There the edge entry is u[R(αρ/β)−1], negative if u>0 and zero otherwise. For the triangular family α=n, β=2n−2 and M_2=3(n−2); the recurrence M_{j+2}=(α+β)M_{j+1}−αβM_j yields the displayed coefficients. At h=1/(n−2) the numerator is −41, −48, −39, −8, 51 at n=5,…,9 and increases thereafter. Rescaling h=x/[2(n−2)] gives the claimed limiting polynomial; convergence of its unique roots follows by bracketing the sign-changing positive root. For finite replay, construct the adjacency on 2-subsets by intersection, then evaluate the actual matrix polynomial at h=1/(n−2) in rationals. At n=5 the 30 edge/15 nonedge pairs match and P_5=−41/27; at n=9 the 252 edge/378 nonedge pairs match and P_9=51/343. verify_srg_rk4.py was inspected, not executed; finite checks do not establish the universal claims.

## originality

PASS

The strongest verified overlap is exact: a separate index entry under 2026/11/8 gives the same general positivity cutoff, nonedge sign and Euler improvement, and another from that directory date gives the triangular cubic, asymptotic gain in equivalent units, and triangular spectral gap. These entries are later-dated in the index than the frozen 2026/10/26 record, not independent evidence of earlier priority. Earlier indexed results actually cover the complete-multipartite equality branch and individual cases. The full prior classification of strict positivity loss before the spectral endpoint on every primitive strongly regular graph was not found in those statements or in the general published methods inspected. The universal endpoint classification, including the comparison with positivity, is supported on the evidence available; no independent priority is claimed for already covered cases or on the basis of an index date alone.

## value

PASS

For diffusive data such as concentrations, spectral contractivity is not enough if one step can generate negative entries. Classical RK4 and strongly regular graphs are natural numerical and structural families, respectively. The theorem identifies the single usable interval from graph parameters, and characterizes exactly when entrywise failure starts before spectral instability. The triangular example quantifies the possible gain over Euler in a natural infinite family; it is illustrative rather than the sole contribution. The value is for completed linear steps, not for nonlinear SSP or stagewise guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
