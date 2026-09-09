# Exhaustive joint merit–flatness census of skew-symmetric Littlewood polynomials at length 33

## Context
Two recognized programs motivate this result: Littlewood flatness (sup-norm of
±1-coefficient polynomials on the unit circle; Littlewood 1966; Balister et
al. 2019 existential theorem) and the Golay merit-factor / LABS program
(Jedwab–Katz–Schmidt asymptotics; Brest–Bošković and Bošković–Herzog–Brest
heuristic best-known tables at lengths ≥121). Prior work is existential,
asymptotic, or heuristic in disjoint long-length windows; no source publishes
an exhaustive joint (merit, flatness) table at length 33 in the
skew-symmetric subspace (Golay's conjecture class).

## Definitions
Let N=33, m=16. Let S be the 2^16 skew-symmetric sign sequences
a ∈ {±1}^33 with a_0=+1 (global sign fixed, lossless for both metrics) and
a_{16+j} = (−1)^j a_{16−j}, j=1..16.
For a ∈ S: aperiodic autocorrelations C_k(a) = Σ_{j=0}^{32−k} a_j a_{j+k};
energy E(a) = Σ_{k=1}^{32} C_k²; merit factor F(a) = N²/(2E(a)) = 1089/(2E);
P_a(z) = Σ_{k=0}^{32} a_k z^k; flatness M(a) = max_{|z|=1} |P_a(z)|/√33.
Pareto comparison is certified: p dominates q if E_p ≤ E_q and
g_p·f_up ≤ g_q (grid analogue, see below).

## Result
(i) Exact merit optimum. Over S, min E = 88, i.e. max F = 1089/176 = 99/16
= 6.1875, attained by exactly 4 sequences: half-indices {10112, 15366, 26963,
29397}, forming two reversal pairs (10112↔29397, 15366↔26963). All 65536
energies are multiples of 8 (281 distinct values, 88..5456, exact mean 496,
exact sum 32505856), and every member has all odd-lag autocorrelations
identically 0.
(ii) Frozen-rectangle exclusion. No a ∈ S satisfies F(a) ≥ 6 AND M(a) ≤ 1.25.
The only members with F ≥ 6 are the four E=88 sequences, whose flatness is
lower-bounded by direct grid evaluation at 1.3076486 (pair 10112/29397) and
1.4166389 (pair 15366/26963), both strictly above 1.25.
(iii) Certified joint Pareto frontier. Under certified comparison the exact
Pareto set is 6 sequences in 3 reversal pairs: E=88 pair (10112/29397,
M ∈ [1.3076486, 1.3076548]); E=120 pair (8777/30492, M ∈ [1.3004729,
1.3004790]); E=128 pair (46407/57362, M ∈ [1.2480442, 1.2480501], the
flattest skew sequences at this length). The set is a certified antichain and
every one of the other 65530 members is certified-dominated by a frontier
member, with minimum strict grid ratio 1.0106, over 2000× the enclosure slack.

## Proof / evidence
Exhaustion: all 65536 halves enumerated once; full sequences built by the
skew rule; autocorrelations/energies in exact integer arithmetic.
Flatness enclosure: for degree n=32, max|P| ≤ g/cos(nΔ/2) where g is the max
over a grid of spacing Δ (Bernstein estimate, valid as nΔ/2<π/2). With
G=32768, Δ=2π/G, nΔ/2=π/1024, f=1/cos(π/1024)=1.0000047062…. The committed
bound uses f_up=1/(1−x²/2)+10⁻¹² with x=3.14159266/1024 ≥ π/1024 (since
cos x ≥ 1−x²/2), so M(a) ≤ g(a)·f_up/√33 rigorously and M(a) ≥ g(a)/√33
(grid values are attained). Interval widths ≤ 6.2×10⁻⁶.
Merit step is bit-exact: F ≥ 6 ⟺ E ≤ 90.75, and every E is a multiple of 8,
so only E=88 qualifies.
Verification: output/artifacts/verify.py (stdlib only, ~1 min) re-enumerates
everything, recomputes all C_k/E, recomputes grid maxima by direct DFT
(agreement ≤10⁻⁶ with the FFT table), recomputes f_up from above, and
rechecks exclusion and full 65530-member domination. Prints VERIFY_OK.
Independent audit replay confirmed VERIFY_OK plus 20 random grid-max entries
(diffs ≤5×10⁻¹⁰) and hand-checked merit fractions.

Explicit witnesses: E=88 C_k for 10112/29397:
[0,5,0,−3,0,−3,0,1,0,1,0,−3,0,1,0,1,0,−3,0,1,0,−3,0,−3,0,1,0,1,0,1,0,1];
for 15366/26963:
[0,−3,0,−3,0,1,0,−3,0,1,0,−3,0,1,0,1,0,1,0,1,0,1,0,1,0,−3,0,5,0,−3,0,1].
Full ±1 string (half-index 10112):
[1,1,1,1,1,1,1,1,−1,−1,−1,−1,1,1,−1,1,1,−1,−1,−1,1,1,−1,1,−1,−1,1,−1,1,−1,1,−1,1];
its reversal is member 29397. Flattest pair 46407/57362 (E=128,
F=1089/256≈4.2539), C_k:
[0,5,0,5,0,1,0,−3,0,1,0,−3,0,1,0,5,0,−3,0,1,0,−3,0,1,0,1,0,1,0,−3,0,1],
M ∈ [1.2480442, 1.2480501]. Middle pair 8777/30492 (E=120, F=363/80=4.5375),
C_k: [0,−7,0,1,0,5,0,−3,0,1,0,−3,0,−3,0,−3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
M ∈ [1.3004729, 1.3004790]. Full sequences and grid maxima in
output/artifacts/frontier.json.

## Limitations
Skew subspace only (2^16 sequences with a_0=+1); no claim about unrestricted
length-33 LABS. Frozen rectangle (6, 1.25) is a stipulated certificate line
(near the skew optimum F*=6.1875 and an aspirational flatness line), not a
published record; the structural content is the exact optimum + full energy
census + certified frontier, which imply the exclusion. Sup-norm upper
bounds rest on the rigorous Bernstein grid estimate, not exact algebraic
maximization; lower bounds are attained grid values. First-data claim scoped
to the N=33 skew joint table.

## Reproducibility
Run `python3 output/artifacts/verify.py` (stdlib only) → VERIFY_OK.
Artifacts: Ehist.json (energy histogram + census checks), frontier.json
(rectangle, f_up, 6 Pareto members with halves, full sequences, C_k, E,
exact F, gmax, M intervals), gmax_all.json (all-65536 grid-max table at 9 dp
+ E vector).

## References
- P. Balister et al., Flat Littlewood Polynomials Exist, arXiv:1907.09464 (2019).
- J. Jedwab, D. J. Katz, K.-U. Schmidt, Advances in the merit factor problem
  for binary sequences, arXiv:1205.0626 (2012).
- J. Brest, B. Bošković, Computational Searching of Long Skew-symmetric
  Binary Sequences with High Merit Factors, arXiv:2011.00068 (2020).
- B. Bošković, J. Herzog, J. Brest, Parallel Self-Avoiding Walks for a
  Low-Autocorrelation Binary Sequences Problem, arXiv:2210.15962 (2022).
