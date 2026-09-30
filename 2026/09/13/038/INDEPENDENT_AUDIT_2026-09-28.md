# Independent audit — SCOPE-20260913-038

Date: 2026-09-28 (UTC)  

## Disposition: PASSED

### Correctness
Independent reconstruction confirms the two one-sided potential-theory certificates. The lower trial measure has I(mu)=1.50716668339754, hence cap(E3)>=0.2215367734. Reconstructing all 384 rational probe subintervals for the upper trial measure gives a certified lower potential bound 1.47304969987, hence cap(E3)<=0.2292253497. The critical-point split of h(s)=s log|s|-(s+l)log|s+l| at {-l,-l/2,0} is sufficient and the weights have total mass one.

### Originality
Prior work gives rigorous general capacity methods and high-accuracy computations for the infinite Cantor set, but the audit found no published certified numerical enclosure for this exact eight-interval third prefractal E3. The contribution is a concrete certification/benchmark rather than a new general theorem.

### Scientific value
A rigorous two-sided benchmark for a natural finite Cantor prefractal is independently useful for validating capacity algorithms; the interval is nontrivial and the certificate is exact-rational apart from rigorously enclosed logarithms.

### Independent checks
The lower energy formula and all trial masses were recomputed independently. The upper certificate was reconstructed from the 96 cells and 40 base probes per Cantor interval; cell endpoints refine these to 384 subintervals. For each cell contribution, the only interior stationary point of `h(s)=s log|s|-(s+l)log|s+l|` is `s=-l/2`, with singular breakpoints at `-l` and `0`, so endpoint/critical evaluation gives a valid per-cell lower range bound. Summing per-cell minima is conservative and therefore valid for the total potential.

### Prior literature
Ransford–Rostand treat rigorous capacity computation and estimate the infinite middle-third Cantor set, not this finite E3 object. Dubinin–Karp give general multiple-interval inequalities. Liesen–Nasser–Sète provide numerical generalized-Cantor computations. None of the retrieved statements supplies this certified E3 interval.

### Limitations
- The ~0.2246 midpoint remains explicitly non-rigorous; only the outer bounds are audited.
- The record contains historical workspace-style artifact paths (output/artifacts/...) although the repository stores them under artifacts/; this is a packaging/documentation defect, not a defect in the scientific inequalities.
