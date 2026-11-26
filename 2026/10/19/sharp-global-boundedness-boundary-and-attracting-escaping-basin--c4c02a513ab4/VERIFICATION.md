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

I reconstructed the deterministic map proof. The uniform forcing bound is 3T, so the strict subcritical recursion absorbs in any square of radius greater than 3T/(1−|1−T|). At T=2, subtracting X from F²(X) cancels the bias exactly. If |X_j| is at least R=11+arctanh(9/10)/α, both arguments in the j-th tanh difference have magnitude above arctanh(9/10), with opposite signs. The diagonal contribution gives inward signed movement even against the worst cross-coordinate contribution. My rational recheck gives inward margin 53/25 and displacement at most 54/5<R, excluding sign overshoot in this region. A coordinate outside R+54/5 decreases until it enters, and one inside stays inside, independently of the other coordinate. For the resulting F²-invariant absorbing square B, B∪F(B) gives F-absorption including odd iterates. For q=T−1>1, the increments of (−q)^(−n)X_n are bounded by 3T q^(−n−1); summing the geometric tail gives the claimed error and the lower bound on the amplitude, hence the exact growth rate outside the stated radius. At (T,α)=(9/4,1/4), H has global Lipschitz factor 27/40 and the fixed point has norm at most 12/13. On the unit square the tanh derivative with respect to the coordinate lies in [15/64,1/4]. My row-sum recheck gives diagonal extrema −181/512 and −47/160 and cross bound 9/16, hence 469/512. This puts the entire claimed 1/13 square in the contraction region; the escape radius at the same parameters is 27.

## originality

PASS

Credit the original model, equilibrium equations and local stability to Buscarino, Famoso and Fortuna. Strict one-step comparisons are direct consequences of their bounded forcing, and local supercritical attraction plus the exterior estimate already suggests coexistence. The distinctive supported contribution is the global absorption mechanism at the formerly inconclusive neutral endpoint, which completes the exact threshold. The explicit invariant contraction square and the controlled escape-amplitude expansion quantify the two behaviors. The strongest matching catalogue record independently states endpoint attraction for the same map but is dated later, not an earlier or undated/same-day overlap.

## value

PASS

At the neutral affine multiplier the standard textbook recursion is silent. A uniform two-step inward mechanism resolves exactly where all-start boundedness fails in a published model. The explicit coexisting attraction and escape regions distinguish what a locally stable equilibrium or a finite-initial-condition bifurcation plot can say from global stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
