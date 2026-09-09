# First relative H-conjugacy-class multiplication tables for two-block Young-subgroup algebras (S4/S5/S6), with Hurwitz counting-form check and stabilization read-across

## Context

Neretin (arXiv:2509.07148, 8 Sep 2025) defines the relative class algebras
C[S_N // Y({m_j})] — functions on S_N constant on conjugacy classes under a
Young subgroup Y = S_{m_1} x ... — and proves a colored Hurwitz-type formula
for their structure constants (Theorem 5), but publishes no explicit tables,
class lists, or stabilization data. The Ivanov–Kerov / Farahat–Higman
stabilization question in this relative setting is open. The chain
(2+2, 2+3, 3+3) is the minimal two-block family with both blocks nontrivial
and growing, where relative stabilization can first be probed.

## Definitions

- Blocks: S4: B1={0,1}, B2={2,3}, H=S2xS2 (|H|=4); S5: B1={0,1},
  B2={2,3,4}, H=S2xS3 (|H|=12); S6: B1={0,1,2}, B2={3,4,5}, H=S3xS3
  (|H|=36). Colors: B1=color 0, B2=color 1.
- Product convention (fixed throughout): `a*b = apply b then a`,
  i.e. (a∘b)(i) = a[b[i]] in one-line/tuple notation.
- H-conjugacy class of g: {h g h^{-1} : h in H}. Class-sum basis:
  gamma(C) = sum_{p in C} p, gamma_mu * gamma_lam = sum_nu c^nu_{mu,lam} gamma_nu.
- Neck mess (Neretin Obs.1): each disjoint cycle of a representative becomes a
  necklace carrying its points' colors; the multiset of necklaces is the
  H-class invariant. Reduced neck mess drops monochrome length-1 necklaces.
- Structure constants, two equal counting forms:
  c[i][j][k] = #{(a,b) in Ci x Cj : a*b = rep(Ck)}
             = #{(a,b) in Ci x Cj : a*b in Ck} / |Ck|.

## Result (headline claim)

Complete relative H-class multiplication tables by direct enumeration:

| case | H-classes | class sizes | nonzero c | triples checked |
|---|---|---|---|---|
| S4 / 2+2 | 10 | 1,1,1,1,2,2,4,4,4,4 (sum 24) | 168 | 1000 |
| S5 / 2+3 | 18 | 1,1,2,2,3,3,6(x6),12(x6) (sum 120) | 1032 | 5832 |
| S6 / 3+3 | 38 | 1,2,2,3,3,4,6(x3),9(x5),12,18(x11),36(x12) (sum 720) | 9173 | 54872 |

- size x #Aut = N! for every class (24 / 120 / 720).
- Both counting paths agree entry-wise on all triples; row sums
  sum_k tot[i][j][k] = |Ci||Cj| everywhere; C0={identity} is a two-sided unit.
- Hurwitz check: every entry verified in the counting form
  c = #{labeled triples}/|Cnu| underlying Neretin Theorem 5 (Obs.4, eqs.1–2)
  plus the #Gamma = N!/#Aut instance per class.
- Stabilization read-across by reduced neck mess (all 10 S4 labels persist in
  S5; all 18 S5 labels persist in S6): shared-slot coincidence 932/1000
  (S4→S5) and 5415/5832 (S5→S6). Examples: [(0,0)]x[(0,1)]→[(0,0,1)] = 1/1/1
  (stable); [(0,1)]x[(0,1)]→[] = 4/6/9 (drift) with siblings →[(0,1,1)],
  →[(0,0,1)], →[(0,1),(0,1)] at 1/1/1, 1/1/1, 2/2/2; [(0,0)]x[(0,0)]→[] = 1/1
  then splits in S6 as []:3 + [(0,0,0)]:3; [(0,0),(1,1)]^2→e = 1/3/9.
  No uniform stabilization at these sizes — first explicit boundary record of
  which slots are stable, drifting, or splitting.

S4 class list (rep one-line, size, reduced mess): C0 `0123` 1 `[]`;
C1 `0132` 1 `[(1,1)]`; C2 `0213` 4 `[(0,1)]`; C3 `0231` 4 `[(0,1,1)]`;
C4 `1023` 1 `[(0,0)]`; C5 `1032` 1 `[(0,0),(1,1)]`; C6 `1203` 4 `[(0,0,1)]`;
C7 `1230` 4 `[(0,0,1,1)]`; C8 `2301` 2 `[(0,1),(0,1)]`;
C9 `2310` 2 `[(0,1,0,1)]`. (S5/S6 listings in artifacts, same format.)

## Proof / evidence

Direct H-orbit enumeration (|G|x|H| ≤ ~26k ops) and triple-product counting
(|G|^2 = 518k products for S6; seconds, stdlib only), independently recomputed
by the auditor from the committed blocks: partitions, size multisets, and
nonzero counts match exactly; S4 (100/100) and S5 (324/324) (i,j) pairs
verified on all k-slots in both counting forms; S6 150-pair random sample
(5700 slots) zero mismatches; identity unit, rowsums, and an S6 associativity
spot ((C3*C10)*C35 = C3*(C10*C35)) pass. Stabilization figures and all named
witness slots replayed exactly. Prior full-text check confirms the gap:
Neretin Sep-2025 gives the formula with zero tables; nearest priors (double-
coset algebra, diagonal-pair stabilization, full-center results; GAP full-
center calls only) are different objects with no H-relative tables.

## Limitations

- Hurwitz verification covers the counting identity c = N(triples)/|Cnu| and
  size*aut = N!, not a re-enumeration of unlabeled checker surfaces /
  Aut-weights; the geometric re-summation is Neretin's proof.
- Stabilization is an exact finite read-across (threshold not reached), not a
  general stability theorem.
- Product convention a*b = apply-b-then-a must be respected on replay;
  tensor files store c[mu][lam][nu] with product v*u in Neretin's w = vu notation.
- Auditor exhaustively re-looped S4/S5 tensors but sampled S6 (150/1444 pairs);
  full S6 byte-agreement is claimed by dual in-artifact paths.

## Reproducibility

Artifacts: per-case class file (representatives, neck/reduced messes, sizes,
#Aut, sparse constants) + dense tensor c[i][j][k]. Deterministic ordering
(lexicographic enumeration, lexicographically minimal representatives).
Rebuild: construct H from blocks, H-orbits of S_n, elem→class map, then
c[i][j][k] = #{(a,b): a*b = rep_k}; cross-check with total/|Ck| and
sum_k tot = |Ci||Cj|.

## References

- Y. A. Neretin, On algebras of conjugacy classes of symmetric groups with
  respect to Young subgroups, arXiv:2509.07148 (8 Sep 2025). Formula source;
  no tables. https://arxiv.org/abs/2509.07148
- Y. A. Neretin, On algebras of double cosets of symmetric groups with respect
  to Young subgroups, arXiv:2304.11690. Neighboring bi-invariant algebra.
  https://arxiv.org/abs/2304.11690
- Y. A. Neretin, Algebras of conjugacy classes in symmetric groups,
  arXiv:1604.05755. G⊃K stabilization theory; example S_n×S_n/diagonal.
  https://arxiv.org/abs/1604.05755
