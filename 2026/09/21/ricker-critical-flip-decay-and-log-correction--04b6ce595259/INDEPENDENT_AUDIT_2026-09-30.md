# Independent Audit — Critical algebraic decay and logarithmic correction at the Ricker flip threshold

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `91ff3c3d62fdb6e6aeb4fbd6eaa8b745daf84bfa`  
**Audited current source tree:** `91ff3c3d62fdb6e6aeb4fbd6eaa8b745daf84bfa`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned snapshot tree. GitHub was used read-only. `INDEPENDENT_AUDIT_2026-09-30.md` and `.json` were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The global and local parts both check. At r=2 the map sends every positive orbit after one step into (0,e/2], and the submitted compact orbit-dependent interval is forward invariant. The equation f^2(x)=x reduces to x+f(x)=2; its derivative geometry leaves x=1 as the unique solution, so Coppel's criterion gives convergence to 1. Independently expanding u↦(1+u)e^{-2u}-1 gives F(u)=-u+(2/3)u^3-(2/3)u^4+(2/5)u^5+..., while the second iterate is u-(4/3)u^3+(8/15)u^5+(4/9)u^6+.... Consequently 1/G(u)^2-1/u^2=8/3+(64/15)u^2-(8/9)u^3+..., yielding the parity-subsequence logarithmic term (8/5)log m and, after the one-step alignment, the claimed (4/3)n+(8/5)log n+C asymptotic.

## Originality — PASS

PASS, with a disclosed historical-access residual. Global attraction of the Ricker equilibrium for the stable parameter range and the location of the flip threshold are prior art and receive no novelty credit. Fisher–Goh–Vincent (1979), read in full via authorized access after open retrieval failed, treats global-stability criteria and the Ricker model for the strict range 0<r<2; it does not give the critical algebraic or logarithmic relaxation law. Targeted searches did not locate the universal sqrt(n) coefficient or the 8/5 logarithmic correction. Goh (1977) remained behind a human-verification gate, so it is not represented as read and remains an explicit residual priority risk.

## Scientific value — PASS

PASS. The theorem supplies a quantitative critical-slowing law exactly at the first period-doubling threshold, globally across the positive basin except for the explicitly characterized finite-hit histories. The next-order logarithmic correction is stronger than merely identifying neutral stability and gives a benchmark for near-critical asymptotics. Generic parabolic-iteration machinery is not claimed as new.

## Independent checks

- Rechecked the invariant interval and the no-nontrivial-two-cycle argument at r=2.
- Symbolically recomputed F, F∘F, the reciprocal-square increment, and the one-step parity-matching increment; all submitted coefficients agree.
- Checked the conversion from the parity index m to the original n, including the 8/5 logarithmic coefficient.
- Read Fisher–Goh–Vincent (1979) in full through authorized institutional access after open full text was unavailable; its Ricker examples establish strict-range stability criteria but not the critical decay law.
- Open-access search for Goh (1977) failed; authorized retrieval reached a human-verification/access gate. No content from that inaccessible paper is claimed as read.
- Targeted searches for Ricker r=2 algebraic decay and logarithmic corrections found no covering source.
- Current main exactly matches the assigned source tree; the dated audit files are absent and VERIFICATION.md is unchanged.

## Limitations

- The result is for the deterministic scalar Ricker map exactly at r=2; it does not give a uniform r→2 crossover theorem.
- Goh (1977) could not be inspected because authorized access required human verification, leaving a disclosed historical-priority residual.
- No novelty is assigned to the flip threshold, endpoint/global stability as such, or generic parabolic iteration methods.

## Evidence and references

- https://doi.org/10.1139/f54-039
- https://doi.org/10.1016/0022-5193(75)90078-8
- https://doi.org/10.1017/S030500410002990X
- https://doi.org/10.1007/BF02462383
- https://doi.org/10.1016/0025-5564(77)90149-3
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/21/ricker-critical-flip-decay-and-log-correction--04b6ce595259

This guarded change set changes only the independent-audit channel of `VERIFICATION.md`; the Lean-verification and expert-attestation channels remain exactly as previously recorded.
