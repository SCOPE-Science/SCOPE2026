---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The checker constructs the sunlet graph directly from a cycle and one pendant leaf at each cycle vertex. For every labeling it tests the defining condition itself: each vertex labeled \(0\) or \(1\) must have closed-neighborhood weight in
\[
\{3,4\}.
\]

The full-label portion exhausts every labeling of \(S_3,S_4,S_5\), totaling
\[
4^6+4^8+4^{10}=1{,}118{,}208
\]
labelings. It obtains minima \(7,10,12\), exactly matching
\[
2n+\left\lceil\frac n3\right\rceil.
\]

A second check enumerates all cycle-label states for each \(3\le n\le10\) and independently chooses the minimum feasible pendant label from the local defining inequalities. This reduced-state optimization again matches the formula in every tested order. Finally, the explicit residue-class construction is checked directly for all \(3\le n\le50\).

Recorded output:

```text
VERIFY_OK
n=3: gamma_p_dI=7, minimum_functions=6
n=4: gamma_p_dI=10, minimum_functions=18
n=5: gamma_p_dI=12, minimum_functions=5
dp n=3: minimum=7, construction_weight=7
dp n=4: minimum=10, construction_weight=10
dp n=5: minimum=12, construction_weight=12
dp n=6: minimum=14, construction_weight=14
dp n=7: minimum=17, construction_weight=17
dp n=8: minimum=19, construction_weight=19
dp n=9: minimum=21, construction_weight=21
dp n=10: minimum=24, construction_weight=24
full_labelings_checked = 1118208
cycle_state_dp_range = 3..10
construction_checked_n = 3..50
all checks matched 2n+ceil(n/3)
```

The computations do not prove the arbitrary-order lower bound. That bound follows from the symbolic fact that the unique weight-two pair state is \((0,2)\) and no three consecutive positions can all be in that state.
