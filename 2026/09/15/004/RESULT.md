# Disproof of the exact 1/8 container-counting target for dense K4-free graphs

## Context

The admitted target concerned K4-free graphs on vertex set [n] with sublinear
independence number alpha(G) <= m(n), where m(n) = o(n) lies in the
Fox-Loh-Zhao / Csaba tight window, and with edge density near 1/8. For fixed
small epsilon > 0, let F(n,m,epsilon) be the family of such graphs with
e(G) >= (1/8 - epsilon) n^2. The target asserted a joint hypergraph-container
lemma plus counting exponent: a container family C(n) with |C(n)| = 2^{o(n^2)}
covering every G in F, each container with e(C) <= (1/8 + o(1)) n^2, from which
log_2 |F(n,m,epsilon)| = (1/8 + o(1)) n^2 was to follow.

## Definitions

- F(n,m,epsilon) = {G on [n] : K4 not subset of G, alpha(G) <= m(n),
  e(G) >= (1/8 - epsilon) n^2}.
- (A) Sparse-edge containers: |C(n)| = 2^{o(n^2)}, every G in F is a spanning
  subgraph of some C in C(n) with e(C) <= U_n := (1/8 + o(1)) n^2.
- (B) Counting exponent: log_2 |F(n,m,epsilon)| = (1/8 + o(1)) n^2.
- L_n := (1/8 - epsilon) n^2; H(x) = -x log_2 x - (1-x) log_2 (1-x).

## Result

For every fixed epsilon in (0, 1/16): if a family C(n) satisfying (A) existed,
then necessarily log_2 |F(n,m,epsilon)| <= (H(8 epsilon)/8 + o(1)) n^2. Since
H(8 epsilon) < 1 for 8 epsilon < 1 (e.g. H(0.08)/8 approx 0.0503 at
epsilon = 0.01, a gap of approx 0.0747 below 1/8), this contradicts (B).
Therefore (A) and (B) cannot both hold. The asserted deduction of (B) from (A)
is invalid, and the target conjunction is false.

## Proof / evidence

Assume (A). Every G in F is a spanning subgraph of some C with N_C := e(C)
<= U_n and e(G) >= L_n, so |F| <= sum_C N_dense(C) with
N_dense(C) = #{G subset of C : e(G) >= L_n}. If N_C < L_n the term is zero;
otherwise with t_C = N_C - L_n, N_dense(C) <= sum_{j=0}^{t_C} C(N_C, j).
The deletion ratio q_C = t_C/N_C = 1 - L_n/N_C satisfies
q_C <= 1 - L_n/U_n = (epsilon + o(1))/(1/8 + o(1)) -> 8 epsilon, uniformly over
C. For epsilon < 1/16, q_max < 1/2 for large n, so the entropy tail bound
sum_{j <= qN} C(N,j) <= 2^{N H(q)} applies uniformly, up to a negligible
log_2(t_C+1) = O(log n) term. Writing a_n = L_n/n^2 and u = N/n^2,
g(u) = u H(1 - a_n/u) has g'(u) = -log_2 q = log_2(u/(u - a_n)) > 0, hence is
strictly increasing; the maximum over N in [L_n, U_n] is attained at U_n.
By continuity of H, max_C N_C H(t_C/N_C) = (H(8 epsilon)/8 + o(1)) n^2.
With |C(n)| = 2^{o(n^2)}, log_2 |F| <= (H(8 epsilon)/8 + o(1)) n^2, bounded
away from 1/8 by delta(epsilon) = (1 - H(8 epsilon))/8 > 0. The numeric gap
was reproduced by artifacts/entropy_gap.py. The argument uses only container
parameters, not K4 structure; the crude bound 2^{e(C)} would give only 1/8
and no contradiction, while the dense-subgraph tail is sharp.

## Limitations

Disproof is specific to fixed epsilon in (0, 1/16); at epsilon = 1/16 the gap
closes since H(1/2)/8 = 1/8. It does not rule out variants with
epsilon(n) -> 0, containers with larger edge counts, or different density
thresholds, and it gives only an upper-bound obstruction without determining
the true value of log_2 |F|.

## Reproducibility

Run `python3 artifacts/entropy_gap.py`; it prints H(8 eps)/8 and the gap to
1/8 for eps in {0.005, 0.01, 0.02, 0.03, 0.05, 0.0625} and asserts the
eps = 0.01 instance (approx 0.0503, gap > 0.07).

## References

- D. Saxton, A. Thomason, Hypergraph containers, Invent. Math. (2015),
  doi:10.1007/s00222-014-0562-8 (nearest prior general container theory;
  contains no such F(n,m,eps) 1/8 result).
- J. Balogh, R. Morris, W. Samotij, Independent sets in hypergraphs
  (container line surveyed in literature search).
- DRAFT.md proof (Sections 2-4); research_report.json (TARGET disproof).
