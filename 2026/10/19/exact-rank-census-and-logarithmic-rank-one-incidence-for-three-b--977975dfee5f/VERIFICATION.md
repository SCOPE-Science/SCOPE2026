---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Dephase the unit-modulus minor to first row and column equal to one. In the remaining 2-by-2 with entries u,v,w,z, determinant vanishing means (u-1)(z-1)=(v-1)(w-1). If a factor equals zero, a factor from the other side is also zero; the four pairings give a normalized repeated row or column. Otherwise conjugate and divide by the common nonzero product to get uz=vw and then u+z=v+w. Equality of the two root multisets forces a repeated column or row. Fourier proportionality is exactly annihilation of all differences on the opposite index set, giving the stated max-plus-min valuation tests. Rank one instead requires annihilation of every difference pair, exactly t_R+t_C>=k. Fine column residue classes have size p^t, and coarse classes have size p^s. The rank-two union comprises triples within a coarse class but not a fine one, plus triples with a fine pair and third point outside that pair's coarse class. These two disjoint counts give B2; this remains valid when s=t. The E_t count chooses three different children of a residue class; I_{t,s} first chooses the unique close pair at valuation s, then the third point exactly valuation t away from either endpoint. This recovers the full row type partition, including p=2 where E_t=0. For a direct replay of the closed form, write Q_v=N(N^2p^{-2v}-3Np^{-v}+2)/6 and sum (Q_v-Q_{v+1})Q_{k-v}. After extracting N^2/36, the summand is N^2a+9Nb-3N^2a p^{-v}+2N^2a p^{-2v}-3Nb p^v-6Nb p^{-v}, with a=1-p^{-2}, b=1-p^{-1}. The three geometric sums yield precisely (N^2a+9Nb)k-(1+6/p)N^2+(-3+6/p)N+4. Dividing by the squared triple count gives the stated O_p(k/N) remainder at fixed p. For p=2,k=2, every row has (t,s)=(0,1), all B1 and B2 vanish, and all 16 minors are rank three. The included checker.py was inspected, not executed; it independently assesses determinant vanishing by cyclotomic coefficient fibers and rank one by congruences, but it does not separately test the simplified rank-one expression and asymptotic. The exact summation above checks those claims without extrapolating from the finite grid.

## originality

PASS

The phase-rigidity lemma and resulting local rank criterion are not original contributions, and the odd-prime-square census is earlier exact coverage. The supported distinct claim is the all-depth conditional rank census with the explicit global rank-one closed form and logarithmic incidence law. Later indexed results give materially overlapping or stronger global formulas, but are not evidence of antecedent coverage. No accessible earlier comparison examined establishes the odd-prime all-depth census or fixed-prime rank-one law.

## value

PASS

A full fixed-row conditional rank distribution for the cyclic prime-power Fourier transform measures loss of interpolation rank, not just whether some choice fails. The rank-one degeneration is rarer than ordinary singularity, and its exact fixed-prime asymptotic exhibits the extra factor of depth on the N^{-2} scale. This is a natural all-depth quantitative invariant beyond the already-known rigidity and prime-square slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
