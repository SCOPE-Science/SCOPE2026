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

Projecting to the cycle of antipodal rungs excludes selecting two lifts of one rung or selecting adjacent rungs. At a quotient gap of two (unique two-edge arc for m≥5), a graph path of length ≤2 would have to follow that arc with no rung step. The other lift thus has distance exactly three, via that arc and a rung. No other pair constrains the lifts, since a length≤2 path would project to an arc of length≤2. A gap surplus L=m−2t>0 gives r>0 broken constraint links; each chain has two lifts even when traversing the twist. The positive compositions of L and the choice of their positions contribute binom(L−1,r−1)binom(t,r), and marking/unmarking multiplies by m/t. At L=0 the alternating rungs have two possible origins and the t lift reversals must compensate for the single twist; that gives four configurations exactly for odd t. The empty packing and t=1 work separately or by the stated formula. Evaluating the first nonzero top coefficient gives 2m for odd m, 4 for m≡2 mod 4, and 2m+m(m−4)=m(m−2) for m≡0 mod 4. Every top configuration has a length-two gap: the surplus is strictly less than the number of gaps in all three regimes. Rotation preserves the resulting distance-three pair, uses valid direct edges and visits every vertex; the timewise packing bound proves optimality even for strong tours. The separate bounded check (python3 /workspace/review_checks.py, tours) enumerated from BFS distances for m=5..10 and confirmed that every maximum had minimum separation exactly three; it does not prove the unbounded result. The supplied verification files were inspected, not executed.

## originality

PASS

Pass for the twisted-family polynomial including its different saturated branch, and for the exact separation and capacity conclusion. Do not credit the general gap-counting method, or the shared unsaturated sum in isolation, as new. An indexed same-day result for untwisted circular ladders has that same sum, but the boundary switches parity; the dates establish no relative priority. Older enumeration and packing-number sources were not fully accessible, so historical priority remains qualified.

## value

PASS

The labelled coefficient sequence is a useful exact invariant of this standard cubic family, while the contrast with the prism isolates an effect of the twist at density saturation. The exact-three tour construction explains why this static optimum remains achievable under the stronger traversing constraint; it is not merely a generic upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
