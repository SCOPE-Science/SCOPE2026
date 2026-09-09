# Certified two-leg obstruction closing level-1 theta–Haemers certificates for C7

## Context

Shannon capacity of the 7-cycle C7 is the first open odd-cycle case after
Lovasz's Theta(C5)=sqrt(5). The recognized gap is lower ~3.2588
(Lean-verified Buys–Polak–Zuiddam 2026; Itty et al. 2026) versus upper
theta(C7)~3.3177 (Lovasz 1979). The admitted level-1 family for this lane
consists of: Lovasz theta SDP-dual weights, Schrijver theta'
(entrywise-nonnegative) SDP weights, integer Haemers fitting matrices over
finite fields, and fractional (n,d)-representations (Bukh–Cox/Blasiak H_f),
combined by product/Kronecker and covering arithmetic.

## Definitions

- C7 vertices Z7, edges i~i+/-1. Strong power C7^{boxtimes n} joins distinct
  words when every coordinate is equal or adjacent.
- Theta(C7)=lim_n alpha(C7^{boxtimes n})^{1/n}.
- theta(C7): Lovasz theta SDP value; theta'(C7): Schrijver
  entrywise-nonnegative variant (primal maximum: any feasible B lower-bounds it).
- H_f(C7;F)=inf{n/d : C7 has an (n,d)-representation over F} with pairs
  (A_v,B_v), A_v^T B_v=I_d and A_u^T B_v=A_v^T B_u=0 for nonedges; column
  spaces X_v=col(A_v).

## Result (headline claim, self-contained)

No certificate of the admitted level-1 form can prove Theta(C7)<=3.30 or
alpha(C7^{boxtimes 4})<=114. Concretely, with exact rational/integer
arithmetic and no floating-point premises:

- (B) theta(C7) in [3.3176,3.3177] by exact Chebyshev-root enclosure
  (T7+1=(x+1)(8x^3-4x^2-4x+1)^2 by coefficient expansion; three certified
  disjoint sign-change intervals with strict monotonicity isolate all roots;
  largest is cos(pi/7); f(x)=7x/(1+x) increasing gives the enclosure).
- (H) H_f(C7;F)=7/2 over every field F: every (n,d)-representation satisfies
  n/d>=7/2 (self-contained Prop.11 iteration: edge 0~1 with I={3,5} gives
  t=dim(X0 cap X1)>=4d-n; reflection gives t'>=4d-n; nonedge (1,6) gives
  X1 cap X6={0}, so d>=t+t'>=2(4d-n), i.e. 2n>=7d), and weight 1/2 on each of
  the 7 C7-edges is an exact fractional coloring of bar(C7) of value 7/2
  (each vertex covered twice), giving H_f<=7/2 via cited H_f<=chi_f(bar).
- (T) theta'(C7)>=82827/25000=3.31308 via explicit rational circulant witness
  B with first row [1/7,0,2857/25000,2547/50000,2547/50000,2857/25000,0]:
  trace 1, zeros exactly on C7 edges, entrywise >=0, objective
  <J,B>=1+14(a2+a3)=82827/25000>33/10, strictly PSD by exact no-pivot LDL
  with 7 positive rational pivots (smallest ~4.97e-4). Hence
  theta'(C7) in [3.31308,3.3177].
- (S) Sharpness: symmetric rank-4 Haemers fitting matrices of C7 over GF(2)
  (edge-values [0,1,0,1,0,0,1]) and GF(3) (edge-values [0,2,0,1,0,0,2]),
  diagonal 1, zeros on all 28 nonedges, rank exactly 4 with pivot columns
  [0,1,3,5]; so the rank<=3 impossibility is best possible. The rank<=3
  impossibility is conditional on the cited lower-bound premise
  Theta(C7)>=3.2578 (Theta<=rank would give 3.2578<=3); unconditional weak
  form rank<=2 impossible from alpha(C7)=3.
- (K) Kill corollaries: theta'(C7^{boxtimes 4})>=theta'(C7)^4
  =(82827/25000)^4=47063879763179701041/390625000000000000~=120.48>114 by
  exact integer comparison 82827^4>114*25000^4 (Kronecker-squaring preserves
  trace/PSD/nonneg/edge-zero); H_f(C7^{boxtimes 4};F)=H_f(C7;F)^4
  =(7/2)^4=2401/16~=150.06>114 exactly (2401>114*16; any rank certificate
  sits above H_f). Sanity: 114^{1/4}~=3.2676 lies below the theta' floor
  3.31308. Lovasz product gives theta(C7)^4~=121.15 (floor 121) for context.

## Proof / evidence

- `theta_baseline.py` -> VERIFY_OK: factorization, root isolation, enclosure.
- `verify.py` -> VERIFY_OK: theta'-point objective, 7 LDL pivots, edge/cover checks.
- `obstruction_window.py` (exit 0): window enumeration, n/d>=7/2 replay,
  367^{1/5}>3.257 integer check, 7/2 cover, theta' floor restatement.
- `haemers_rank4.py` -> VERIFY_OK: GF(2)/GF(3) fitting + rank-4 logs.
- `fallback_route_kill.py` -> VERIFY_OK: both-legs exact kill of 114.
All scripts stdlib-only, replay in seconds. Independent audit recomputed the
LDL pivots, eigenvalue positivity, factorization, intervals, ranks, and kill
integers. Cited-not-reproved: Lovasz odd-cycle theta formula; Bukh–Cox
framework (Prop.11, Thm 8 H_f<=chi_f, Cor.10, Thm 20/21 collapse, H_f
multiplicativity); theta multiplicativity; lower-bound premises
alpha(C7^5)>=367 and Lean-verified Theta>=3.2588 (labelled premises for the
conditional rank<=3 corollary only). Fractional-theta variants collapse per
cited Bukh–Cox Sec.5; min/hybrid combinations sit above min(3.31308,3.5)>3.30.

## Limitations

Level-1-specific only. Not ruled out: Lasserre/SDP levels >=2, non-circulant
theta' witnesses above 3.31308 (bounded by 3.3177), ad-hoc strong-power
arguments. The bare value H_f(C7)=7/2 is prior (Bukh–Cox Prop.4, disclosed);
novel auditable content is the exact rational LDL theta'-floor log, the sharp
rank-4 witness logs, and the assembled machine-checked two-leg obstruction
with exact residuals. No upper-bound improvement is claimed. One legacy
script (`capacity_baseline.py`, not filed in output) contains a superseded
float64 margin section printing FAIL; the headline does not depend on it.

## Reproducibility

Run `python3 output/artifacts/<script>.py` for each script above; expect
VERIFY_OK (or exit 0 for obstruction_window.py). Exact integer/Fraction
arithmetic only for all headline inequalities; zero floats used.

## References

- Lovasz 1979 (theta, odd-cycle formula). https://doi.org/10.1109/TIT.1979.1055985
- Bukh–Cox 2018, arXiv:1802.00476 (fractional Haemers theory, Prop.11/Thm 8/Cor.10/Thm 20-21/Prop.4).
- Blasiak thesis (fractional Haemers origin).
- Polak–Schrijver 2018, arXiv:1808.07438 (alpha(C7^5)>=367).
- Buys–Polak–Zuiddam 2026, arXiv:2607.29681 (Lean-verified lower bound).
- Itty et al. 2026, arXiv:2607.21517 (lower bound 3.258020).
- Zuiddam 2019; de Boer–Buys–Zuiddam 2024 (duality context).
