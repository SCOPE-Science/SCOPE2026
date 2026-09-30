# Independent Audit — 2026-09-29

**Record:** `2026/09/19/faithful-quasidiagonal-midpoints-exact-distance--299dad9e0920`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The norm-distance argument is internally exact once Moradi's equal-sector theorem and the construction identities are granted. For h=e^1-e^0, ||h||=1 and every quasidiagonal trace ν has ν(h)=0, whereas ω_{c,t}(h)=c(2t-1), yielding the lower bound. The proposed midpoint q_c is quasidiagonal and ω_{c,t}-q_c=c(t-1/2)(μ_1-μ_0); complementary sector support gives ||μ_1-μ_0||=2, so the lower bound is attained. The positive (1-c)γ coefficient gives faithfulness for c<1. Quasidiagonal traces are amenable, and faciality of amenable traces propagates amenability from the midpoint to the endpoints and hence the chord.

## Originality

**PASS** — Moradi's current public preprint abstract states the asymmetric non-face example and the theorem that every quasidiagonal trace gives equal weight to the two copies, but it does not advertise the symmetric faithful chord or an exact norm-distance profile. Targeted searches did not locate the formula dist(ω_{c,t},T_qd)=c|2t-1| or this construction-specific midpoint theorem. The separating-functional argument is elementary convex geometry, so the novelty is properly limited to its quantitative synthesis inside Moradi's new construction.

## Scientific value

**PASS** — The record turns qualitative non-faciality into a sharp metric statement and shows the phenomenon persists for faithful amenable traces at every prescribed distance c∈(0,1). The exact distance profile and unique quasidiagonal midpoint give substantially more geometric information about the counterexample.

## Evidence checked

- Mehdi Moradi, Quasidiagonal traces need not form a face: https://arxiv.org/abs/2609.18793 — Current public abstract confirms the RFD construction and the equal-weight theorem for all quasidiagonal traces.
- N. P. Brown, Invariant means and finite representation theory of C*-algebras: https://doi.org/10.1090/memo/0865 — Background source for amenable/quasidiagonal trace technology; no claim of novelty for the standard convex-analytic ingredients.

Repository evidence was read at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` / source-check commit `253a0fe5d0217455660a277f9adb940030e567ad`. A later repository-head comparison through `eff2c6312cec5b0dee5115e5f42211a853092dfb` found no changes under this record path, so the assigned source-tree SHA `2ff60d65e48899ffaba39c8d3b04ac600a59781b` is the tree audited. GitHub was used only as read-only evidence.

## Limitations

- The result is construction-specific and does not characterize the entire quasidiagonal trace set.
- The current public abstract of Moradi's preprint was accessible in this audit, but the full body was not independently re-opened through the available web interface; source-specific details beyond the abstract were therefore checked against the self-contained record derivation and its pinpointed theorem/lemma claims rather than represented as freshly re-read full text.
- An older abstract convex-geometric lemma could reduce novelty of the proof pattern without erasing the construction-specific quantitative family.

## Audit conclusion

This independent audit is scientifically complete on correctness, originality, and value. The record may remain at its source path without substantive research-file edits.
