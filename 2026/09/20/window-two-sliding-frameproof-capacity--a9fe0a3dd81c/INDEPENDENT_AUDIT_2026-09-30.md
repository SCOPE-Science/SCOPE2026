# Independent Audit — Exact capacity of window-two sliding-window dynamic frameproof codes

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `8de41746f8c9a04d593f6d5cfdaa675d6c9afbe8`  
**Audited current source tree:** `8de41746f8c9a04d593f6d5cfdaa675d6c9afbe8`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned source tree. GitHub was used read-only, and the dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The protection lemma is valid under Paterson's unrestricted-coalition definition: if a user lies in a nonunique pirate class at time j and receives a nonunique mark at j+1, the fixed coalition U\{u} can realize that two-segment pirate prefix, so every member of the current pirate class must receive a globally unique mark next. If the class has size s, this consumes s symbols; the remaining n-s users occupy at most q-s symbols, so some next nonunique class has size at least ceil((n-s)/(q-s)). When n>max_s s(q-s+1), this size is strictly larger than s, producing an impossible infinite strictly increasing sequence bounded by q-1. The matching construction protects exactly the previous nonunique class and therefore prevents any user from matching two consecutive pirate marks. Maximizing a(q-a+1) gives floor((q+1)^2/4), including the vacuous a=1/q-user case.

## Originality — PASS

PASS. Paterson's 2007 full text proves the same alpha(q-alpha+1) value for window length two only within schemes having a fixed number alpha of unique protected users per segment. The paper explicitly states in its 'Further Possibilities' section that complete generality requires alpha to vary with each segment and leaves open whether such general schemes support more users. The submitted upper bound removes that fixed-alpha restriction specifically at window length two and proves that optimizing the old construction is already unrestrictedly optimal. Later surfaced frameproof work concerns different static/wide-sense models and does not close this feedback-dependent open case.

## Scientific value — PASS

PASS. The theorem exactly resolves the first nontrivial window length of an explicit open problem from the foundational source, replacing an asymptotic unrestricted upper bound by the sharp capacity floor((q+1)^2/4). The proof is short and structural and shows why variable protection cannot improve the fixed-alpha construction when the window has length two.

## Independent checks

- Reconstructed the protection lemma using one fixed unrestricted coalition U\{u}; nonuniqueness guarantees an available traitor mark at every step.
- Checked the pigeonhole recurrence s_next>=ceil((n-s)/(q-s)) and the strict-growth contradiction under n>max_s s(q-s+1).
- Checked the matching construction for a>=2 and the a=1 boundary where all marks are unique and no valid pirate broadcast exists.
- Read the openly available Paterson 2007 full text hosted by the author/ResearchGate. Theorem 4.8 is fixed-alpha, while Section 4.2.1 explicitly says complete generality requires varying alpha and states the open problem.
- Targeted searches for a later unrestricted window-two exact capacity found no covering result.
- GitHub current main has exactly the assigned directory tree SHA; the dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The theorem is specific to window length two and Paterson's unrestricted-coalition frameproof definition.
- The upper-bound coalition can be as large as U\{u}; it does not prove the same capacity for a fixed small c-frameproof variant.
- The result closes the variable-protection question only for l=2, not for longer sliding windows.

## Evidence and references

- https://doi.org/10.1007/s10623-006-9030-9
- https://doi.org/10.1007/s10623-006-9037-2
- https://doi.org/10.1007/s10623-020-00797-w
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/window-two-sliding-frameproof-capacity--a9fe0a3dd81c

This guarded change set changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
