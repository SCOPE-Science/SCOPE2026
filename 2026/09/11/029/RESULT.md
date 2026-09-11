# Intact-row modulus growth and a first Ahlfors-regular conformal-dimension lower bound for the asymmetric p=7 L-block carpet

## Context

Ahlfors-regular conformal dimension attainment versus non-attainment is a
recognized open boundary in quasisymmetric uniformization (Bonk–Kleiner
Cannon reformulation, Keith–Laakso modulus program, Carrasco-Piaggio
critical-exponent theorem). The standard carpet's attainment is famously open
(Bonk–Kleiner Problem 6.2); few concrete witnesses exist. The admitted target
(non-attainment witness for a named asymmetric carpet) and the preset fallback
(certified width-≤0.1 interval with U≤1.9) are both documented BLOCKED
(see Limitations). The result below is the complete lower-bound theorem
salvaged from the target's modulus route, submitted as an emergent finding on
the same object with the same admitted method.

## Definitions

Let S ⊂ [0,1]² be the self-similar carpet obtained by subdividing [0,1]² into
7×7 congruent squares and deleting, at every iteration, the asymmetric
L-shaped block with lower-left indices {(2,3),(3,3),(3,4)}, retaining the other
46 first-level squares, with the Euclidean metric.
Let G_k be the level-k kept-cell graph (4-adjacency) and M_k(p) its
left-to-right vertex p-modulus.
Let Q_LR := inf{p : lim_k M_k(p) = 0} be the side-to-side critical exponent,
Q_full the corresponding capacity (full-family) exponent, and dim_AR(S) the
Ahlfors-regular conformal dimension.

## Result

1. (Exact Menger widths, k ≤ 3.) G_k has left–right Menger width exactly 5^k
   for k = 1, 2, 3 (certified by node-split Dinic max-flow/min-cut; achieved
   flows 5, 25, 125), realized by the 5^k fully-kept horizontal rows whose
   base-7 y-digits lie in {0,1,2,5,6}; every such row-crossing has exact length
   7^k. The row construction is valid for general k by induction on the IFS.
2. (Modulus growth.) For every p > 1 and every k,
   M_k(p) ≥ 5^k · (7^k)^{1-p} = g(p)^k with g(p) = 5·7^{1-p},
   by the disjoint-path Hölder certificate. Hence
   Q_LR ≥ 1 + log 5 / log 7 ≥ 1.82708,
   via the exact integer witness 5^100000 ≥ 7^82708
   (sharp at five digits: 5^100000 < 7^82709).
3. (Conformal-dimension lower bound.) The side-to-side family is a subfamily of
   the capacity family defining dim_AR, so Q_full ≥ Q_LR by family inclusion,
   and dim_AR(S) = Q_full (Carrasco-Piaggio / Keith–Laakso, as cited in the
   admitted topic). Hence
   dim_AR(S) ≥ 1 + log 5 / log 7 ≥ 1.82708.
   With the Hausdorff upper bound dim_AR(S) ≤ dim_H(S) = log 46 / log 7
   ≤ 1.96754 (certified integer witness 46^100000 ≤ 7^196754),
   dim_AR(S) ∈ [1.82708, 1.96754],
   the first localization for this carpet. Longer decimals 1.827087… /
   1.96753… are double-precision evaluations only.

## Proof / evidence

*Rows.* The omitted block meets only square-rows y = 3 (cells x = 2,3) and
y = 4 (cell x = 3); rows {0,1,2,5,6} are fully kept. A level-k row is fully
kept iff all its base-7 y-digits avoid {3,4}, giving 5^k intact rows,
pairwise vertex-disjoint, each an x-crossing of length 7^k. Maximality is
certified by max-flow/min-cut on the node-split network (source→A capacity 1,
B→sink capacity 1, v_in→v_out capacity 1, undirected edges as paired
infinite-capacity arcs; flows 5, 25, 125 at levels 1, 2, 3).
*Modulus.* For disjoint paths of lengths L_i,
Mod_p ≥ Σ_i L_i^{1-p} (test-mass averaging / Hölder dual). With L_i ≡ 7^k:
M_k(p) ≥ 5^k 7^{k(1-p)} = g(p)^k. g(p) > 1 iff p < 1 + log 5 / log 7; below
this edge M_k(p) → ∞, so Q_LR ≥ 1 + log 5 / log 7. The integer witness
5^100000 ≥ 7^82708 gives the five-digit edge Q_LR ≥ 1.82708.
*Transfer.* Family inclusion reverses the vanishing implication, giving
Q_full ≥ Q_LR; the Carrasco-Piaggio identification dim_AR = Q_full yields
the bound.

## Limitations

- Proves only the lower edge Q_LR ≥ 1.82708 for the side-to-side family and
  its transfer to dim_AR; does not compute Q_LR exactly, does not bound
  dim_AR from above beyond dim_H, and does not decide attainment.
- Maximality is machine-certified for k ≤ 3; the general-k row construction is
  proved, and maximality beyond level 3 is not needed for the growth bound.
- Target (non-attainment witness) is BLOCKED: singleton peripheral-shape
  spectrum and no decaying minimizing sequence at any Q ≤ 1.9 across six
  weight families. Preset fallback ([L,U] width ≤ 0.1, U ≤ 1.9 with
  full-modulus decay) was ATTEMPTED_AND_BLOCKED (400-cut dual LB 0.94292;
  multi-start primal floor 1.07689; level-3 UB 1.22813; decay only at Q∼1.9–2.0
  in the wrong subfamily).
- The exploratory level-1 LP-duality enclosure M_1(1.9) ∈ [0.95405, 0.95769]
  is an uncertified baseline only and is not part of the verified headline.

## Reproducibility

`python3 output/artifacts/verify_emergent.py` (stdlib + numpy) prints
`ALL CERTIFICATES OK`: intact-row counts, max-flow/min-cut Menger widths
5, 25, 125, growth factors, and certified integer edge witnesses
(5^100000 ≥ 7^82708; 46^100000 ≤ 7^196754). Independently rerun by the
auditor on 2026-09-11.

## References

- Kwapisz (2020), Conformal dimension via p-resistance: Sierpinski carpet
  (symmetric Sp family; method scaffold).
- Anttila, Eriksson-Bique (2026), Cartesian products of Sierpinski carpets do
  not attain their conformal dimension (S^k, k ≥ 2; single carpet open).
- Kajino, Murugan (2023), On the conformal walk dimension (standard-carpet
  attainment open, Bonk–Kleiner Problem 6.2).
- Esmayli, Schardine, Shanmugalingam (2025), On Carrasco Piaggio's theorem
  (general modulus–dimension criterion).
- Keith, Laakso (2004), Conformal Assouad dimension and modulus (general
  criterion; dim_C < dim_H for Sierpinski n-carpets).
