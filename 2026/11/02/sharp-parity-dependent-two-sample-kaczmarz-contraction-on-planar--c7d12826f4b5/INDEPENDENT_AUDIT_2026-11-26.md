# Independent mathematical audit

## correctness

PASS

For phi=pi/m, projecting on the selected unit row removes squared error ||e||^2 max(r_i,r_j), where r_j=cos^2(theta-j phi). All unordered pairs have equal weight, and sum r_j=m/2. Thus normalized progress is 1/2+D/[m(m-1)], where D=sum_{i<j}|r_i-r_j|. By the difference-of-cosines identity and counting ordered cyclic displacements d, D=(1/2) sum_{d=1}^{m-1} sin(d phi) sum_{i=0}^{m-1}|sin(2 theta-(2i+d)phi)|. For odd m, 2i+d ranges over every residue modulo m, so at theta=0 the inner sum and the outer weight sum both equal cot(phi/2); translating theta by phi/2 preserves the value. For even m, the even and odd displacement weight sums are respectively cot(phi) and csc(phi); at theta=0 the respective inner sums are twice these, and at theta=phi/2 they are exchanged. Thus the candidate D values are cot^2(phi)+csc^2(phi) and 2 cot(phi)csc(phi), with difference tan^2(phi/2)>0. Every possible crossing is on the half-step grid. Between these points D''=-4D<0 because a set of m>=3 distinct projected polygon vertices cannot all have one identical projection. Strict concavity and row-rotation symmetry exhaust minimizers, including m=3. Ties do not change the squared decrement. The one-row mean is exactly 1/2; conditional expectation iterates the optimal one-step inequality without claiming a sharp long-run rate. Small-angle expansions give both the stated limit and the even gap asymptotic. The numerical script was inspected, not executed; the angular proof supplies the uniform guarantee.

## originality

PASS

The supported increment is the exact worst-direction two-sample constant for the full family of regular planar frames, including the parity-resolved equality directions and the finite even-row gap. The selection algorithm, the state-dependent residual identity, and the regular three-row case are not distinct contributions. Neither the fixed-three-row comparisons nor the general state-dependent bounds evaluate the remaining angular optimization over all row counts.

## value

PASS

The formula quantifies the benefit of one extra sampled residual in a natural tight frame and gives a sharp benchmark for geometry-agnostic contraction bounds. The exact minimizers change with row-count parity even though the limiting constant is the same; the small quartic gap measures a genuine geometric difference rather than numerical error. This is a state-uniform one-step benchmark, not a claim about fastest implementation or an optimal long-run residual budget.

The dated certificate retains the supplied scientific assessment, sources and limitations.
