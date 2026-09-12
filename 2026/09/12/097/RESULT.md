# Exact triangle-family SA1 gap classification for binary pairwise MAP

## Context
Binary pairwise MAP inference (energy minimization) on a graph G=(V,E) with labels
x in {0,1}^V is a canonical NP-hard optimization problem with applications in
Markov random fields, computer vision, and valued constraint satisfaction. The
Sherali-Adams level-1 (SA1) relaxation, also called the local-polytope or basic
LP relaxation, keeps singleton distributions b_i and pairwise distributions
b_ij agreeing on singleton marginals and minimizes the expected cost. Its
one-sided integrality gap OPT_MAP/OPT_SA1 measures the worst-case looseness.
The admitted target asked whether the worst-case gap over series-parallel
(treewidth at most 2) instances with restricted cost alphabets is at most 4/3
with a named triangle extremal. The full series-parallel bound remains open.
This record settles the extremal triangle subfamily completely and isolates a
general obstruction to the natural inductive proof.

## Definitions
- Graph: the 3-node triangle K3 (3 vertices, 3 edges); K3 is K4-minor-free,
  hence series-parallel (treewidth 2).
- Costs (minimization): unary u_i in {0,1,2}^2 per node; pairwise th_ij in
  {1,2}^{2x2} per edge. All costs are positive in the pairwise part, so every
  feasible LP value is strictly positive and the ratio is well defined.
- Integer optimum: OPT_MAP = min_{x in {0,1}^3} sum_i u_i(x_i)
  + sum_{ij} th_ij(x_i,x_j), by exhaustive enumeration over 8 labelings.
- SA1 optimum: OPT_SA1 = min over b_i, b_ij >= 0 with b_ij marginalizing to
  b_i, b_j of sum_i <u_i,b_i> + sum_ij <th_ij,b_ij>.
- Gap: OPT_MAP / OPT_SA1 (>= 1 since the relaxation lower-bounds the integer
  optimum).
- Half-integral reduction: the binary pairwise local polytope admits a
  half-integral optimal solution (roof duality; Hammer-Hansen-Simeone 1984;
  Rother et al. 2007, QPBO). With singleton marginals p_i = b_i(1), each edge
  decouples into a one-dimensional LP over t = b_ij(0,0), linear in t with
  slope th00+th11-th01-th10. Hence the LP optimum equals the minimum over
  p in {0,1/2,1}^3 of the unary part plus closed-form per-edge min-couplings
  (27 profiles, exact rational arithmetic).

## Result
(a) For EVERY triangle instance with unary costs in {0,1,2} and pairwise costs
in {1,2} (16^3 pairwise triples times 9^3 unary triples = 2,985,984
instances), OPT_MAP / OPT_SA1 <= 4/3, and the maximum 4/3 is attained.
(b) Tightness: the zero-unary antiferromagnetic triangle with th((0,0)) =
th((1,1)) = 2 and th((0,1)) = th((1,0)) = 1 on all three edges has verified
integer optimum 4 and verified SA1 optimum 3, hence gap exactly 4/3.
(c) Obstruction: the scalar degree-2 (ear) induction step that a global
LP-value proof would need is FALSE in general. Over all 9 x 16 x 16 x 27 x 4
= 248,832 local single-gadget rational configurations, minbit(boundary) /
eff(LP mass) attains 2 (4484 configurations violate the 4/3 step). Extremal
gadget: u_v = (0,0), tha = thb = ((1,2),(1,2)), pv = pa = pb = 0, boundary
(a,b) = (1,1): eff = 0+1+1 = 2, minbit = 0+2+2 = 4, ratio 2. Any proof of a
series-parallel 4/3 bound must therefore use boundary-conditioned
(terminal-state) induction, not scalar LP-value induction.

## Proof and evidence
Witness integer optimum 4: the two constant labelings cost 3x2 = 6; each of
the six 2-1 labelings has exactly one equal edge (cost 2) and two cut edges
(cost 1+1), total 4. Exhaustive check over all 8 labelings confirms 4.
Witness SA1 optimum 3: upper bound from the explicit feasible point b_i =
(1/2,1/2) for all i and b_ij = 1/2 on (0,1),(1,0) per edge, whose singleton
marginals agree and whose per-edge cost is (1+1)/2 = 1, total 3
(machine-checked feasibility and value in exact rational arithmetic);
lower bound because every pairwise entry is at least 1 and unaries are 0, so
every feasible LP point has value at least 3. Hence OPT_SA1 = 3 exactly and
the ratio is 4/3 exactly. Re-verified in Fractions: integer 4 at (0,0,1);
LP 3 at p = (1/2,1/2,1/2), t = (0,0,0), feasible, primal value 3.
Census: for each of the 2,985,984 instances both optima were computed exactly
(brute-force integer optimum; half-integral LP enumeration with closed-form
edge minima). All values are multiples of 0.5 at magnitude below 100, exactly
representable in binary floating point; cross-validation showed 2000/2000
agreement between float and independent Fraction evaluators and 300/300
agreement between the half-grid and eighth-grid LP enumerations, confirming
half-integrality on this class. Outcome: worst ratio exactly 4/3, zero
instances above 4/3. An independent auditor vectorized re-enumeration of the
full family reproduced worst 4/3 with zero violations, plus 200/200
float-vs-exact spot-checks.
Ear-step refutation: exhaustive exact-rational check of the inequality
minbit(a,b) <= (4/3) eff(v) over all 248,832 configurations gives worst ratio
2 with 4484 violations, as above; a second extremal form with pa = pb = 1 is
recorded in the logs.

## Limitations
This classifies the TRIANGLE subfamily completely, not the full
series-parallel class. The unrestricted target (4/3 upper bound for all
series-parallel graphs, or an explicit counterexample) remains open. Random
search on larger series-parallel graphs (8000 trials, n = 3..8, 2-trees /
partial 2-trees / odd cycles; worst observed 1.20; zero violations) is
supporting context only, not part of the proved claim. Half-integrality is
invoked as a classical theorem with the cited references and the additional
eighth-grid validation above.

## Reproducibility
Scripts: evaluate.py (exact Fraction and float evaluators, primal
builder/checker), search.py and fastsearch.py (float evaluators, random
series-parallel generators, exhaustive driver). Logs:
triangle_exhaustive.log, triangle_random_seed1.log,
random_afbiased_seed11.log, ear_step_refutation.log. To reproduce: (i) run
the exhaustive triangle loop over all 2,985,984 instances comparing brute-force
integer optima with half-integral LP values; (ii) re-certify the witness with
the Fraction construction above; (iii) re-run the 248,832-configuration
ear-step enumeration.

## References
- Hammer, Hansen, Simeone (1984), roof duality and half-integrality of binary
  pairwise relaxations.
- Rother, Kolmogorov, Lempitsky, Szummer (2007), QPBO.
- Bienstock and Ozbay, tree-width and the Sherali-Adams operator.
- Thapper and Zivny (2015), Sherali-Adams relaxations for valued CSPs.
- Cooper and Zivny (2012), Tractable triangles and cross-free convexity,
  JAIR 44:455-490.
- Gupta, Talwar, Witmer (2013), sparsest cut on bounded treewidth graphs.
