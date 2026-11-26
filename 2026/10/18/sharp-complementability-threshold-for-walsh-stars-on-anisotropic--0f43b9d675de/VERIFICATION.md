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

The weighted path norm is exactly the maximum of the coordinate-edge quotients. Averaging conjugates of a projection over the sign translations keeps its range and identity on that range, does not increase the norm, and gives the unique commuting projection by the distinct nonconstant Walsh eigenspaces modulo constants. For a light flip, only one output character changes, and the absolute output difference 2|f̂({0,j})| is at most the supremum input difference on those edges by averaging against that character. In the distinguished direction, odd symmetrization is contractive and produces x₀g with |g|≤w/2 and unit light-edge bound. A heavy-edge evaluation at all light signs positive equals (2/w) E[S_m g] after taking a supremum over translates and sign. For a level k<m/2, pair a uniformly chosen k-set of negative signs with a uniformly extended (m−k)-set. Its other marginal is uniform, and the pair differs in m−2k light edges. The difference of the two level means is at most min(w,m−2k), which directly bounds each contribution to E[S_m g]. The clipped function attains all these bounds simultaneously and is feasible. Thus the heavy quotient is exactly the stated expectation divided by w; the light bound and the projection lower bound 1 give the formula. At w=m the heavy bound is E[S_m²]/m=1; for m≥3 the nonzero level |S_m|=m−2 has a strictly greater contribution for every w<m, whereas all other contributions are nondecreasing as w decreases. The m=2 distribution gives no such level, and the two magnitudes 1,3 give the three branches for m=3. The dual norm follows by dual translation averaging and uniqueness of the matching spectral projection, with ||Q*||=||Q||. An incidental correspondence sentence at RESULT.md line 50 should not be read as saying every projection onto Y has adjoint range ran(Q*): its adjoint has kernel Y⊥, but its range may vary. The subsequent dual averaging proof establishes the asserted unrestricted minimum without that sentence. Replay: RESULT.md lines 20–50 with the level-pairing check above. The inspected LP script supplies optional finite floating-point corroboration; it was not executed and does not establish the universal formula. Scope is real scalars, one distinguished weight and equal remaining weights.

## originality

PASS

The credited overlap is substantial for particular slices: the unit-weight value and dual statement there follow from the general unweighted shadow formula; a distinct same-date weighted record also implies the plateau for w≤1. Neither gives the nontransitive star formula over varying w, in particular the genuine w>1 dependence and sharp norm-one threshold for m≥3. The unrestricted optimum and its dual for this regime depend on the new constrained heavy-edge optimization, not on a renamed supremum-norm projection. No priority follows from the record dates.

## value

PASS

The star is the first natural asymmetric degree-two spectrum separating a distinguished coordinate from interchangeable leaves. The exact optimum tests whether anisotropy can change a Lipschitz projection norm at all, unlike the large class of transitive spectra, and gives a sharp metric criterion for contractive complementability. The all-projections lower bound and explicit clipped extremizer are useful beyond the already known equal-weight value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
