# Independent audit — 2026-09-26

Record: `2026/09/09/044`. Verdict: **correctness PASS; originality PASS (finite tables); scientific value PASS (bounded).** Disposition: retain accepted.

## Correctness
I independently implemented Murnaghan–Nakayama character recursion by enumerating subpartitions and accepting a removed skew shape exactly when it is connected and contains no 2×2 square. For each cycle partition, I computed class sizes, squared cycle type, then evaluated both inner products and their half-sum/half-difference. All 22+45+88 entries are integral and nonnegative and the degree sums give d² and d(d+1)/2. The unique |s−a| maxima are n=6: 3 at ((3,2,1),(4,2)); n=7: 4 at ((4,2,1),(5,2)); n=8: 5 at ((4,3,1),(4,2,2)), with (s,a,g,m)=(6,1,7,5). For (3,2,1), all 11 irreducibles occur in both the total and symmetric square. These checks use a separate recursion from the package's compute.py and verify.py, and directly confirm the 201600 power-map numerator.

## Prior work and originality
Bessenrodt–Bowman, arXiv:2202.03066v3, gives general small-depth constituents, full [n−3,3] decompositions, two-row families and a refined Saxl conjecture. It expressly says the [n−3,2,1] formula appears more involved. Thus the reported numerical n≤8 census can be useful as finite data, but the general character formula, power-map splitting identity, and refined-Saxl conjecture are prior work. The n=6 staircase check is a test case of that existing conjecture, not a new conjecture or proof for all staircases.

## Scientific value and limits
The machine-readable 155-row table supplies reproducible low-degree test data for future splitting formulas. The maximum gap is over the nine specified source shapes only; it does not bound all S8 Kronecker squares or establish a parametric pattern.

Sources: RESULT.md and artifacts/compute.py, verify.py, splitting_tables.json; https://arxiv.org/html/2202.03066v3; https://arxiv.org/abs/1909.07489.
