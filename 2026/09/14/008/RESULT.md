# Groetzsch graph M4 edge ideal: Waldschmidt constant 29/19, stable Harbourne holds, resurgence 38/29

## Context

The containment problem asks for which pairs (m,r) the symbolic power
I^(m) is contained in the ordinary power I^r. Two asymptotic invariants
package this information: the Waldschmidt constant
hat-alpha(I) = lim alpha(I^(s))/s and the resurgence
rho(I) = sup{m/r : I^(m) not subset I^r}. For edge ideals of graphs both
are controlled by linear-programming duality (Bocci et al.): the
Waldschmidt constant is the fractional-vertex-cover optimum over the
minimal vertex covers, and resurgence is bounded through fractional
b-matching gaps. Computing both exactly for one natural extremal graph
is a recognized benchmark task: the admitted target asked for the exact
Waldschmidt constant, the stable Harbourne containment
I^(2r-1) subset I^r for all r >= 2, and the exact resurgence of the
Groetzsch (Mycielski M4) edge ideal.

## Definitions

Let G = M4 be the Mycielskian of C5: vertices v_0..v_4 (class V),
u_0..u_4 (class U), w; 11 vertices, 20 edges, triangle-free with
chromatic number 4. Order polynomial variables x_0..x_4 on V,
x_5..x_9 on U, x_10 on w. Let R = k[x_0..x_10] over any field and
I = I(G) = (x_i x_j : {i,j} in E(G)) its edge ideal. Symbolic powers
are over minimal primes = minimal vertex covers. For a monomial with
exponent vector a in N^11 write symb(a) = min_C sum_{v in C} a_v
(m in I^(s) iff symb(a) >= s) and nu(a) = max number of edges packable
under vertex capacities a (m in I^r iff nu(a) >= r). The fractional
relaxation nu_frac(a) is the capacitated fractional b-matching optimum.
The graph has exactly 16 minimal vertex covers (from 16 maximal
independent sets, alpha(G) = 5) in D5-orbits A(3,3,1)x5, B(3,5,0)x5,
C(4,2,1)x5, D(5,0,1)x1. All statements hold over any field.

## Result

Let G be the Groetzsch graph M4 and I = I(G) its edge ideal over any
field. Then:

1. The Waldschmidt constant is exactly hat-alpha(I) = 29/19.
2. The stable Harbourne containment I^(2r-1) subset I^r holds for every
   r >= 1, hence for every r >= 2; there is no failing r.
3. The resurgence is exactly rho(I) = 38/29.

## Proof and evidence

Waldschmidt constant. The fractional-cover LP min sum x_v subject to
cover sums >= 1 reduces by D5 symmetry to min 5p+5q+s. Exact rational
vertex enumeration gives optimum 29/19 at (p,q,s) = (3,2,4)/19, tight
on cover types A, B, D. A symmetric dual packing y on the 16 covers,
constant per orbit with weights 3/19 (A), 2/19 (B), 0 (C), 4/19 (D),
has every vertex load exactly 1 and value 29/19, so strong duality
certifies the fractional optimum is exactly 29/19. Hence
alpha(I^(s)) >= 29s/19 for all s. Conversely the symmetric monomials
k * a_sym with a_sym = (3^5, 2^5, 4) of degree 29k have cover sums 19k
on types A, B, D and 20k on C, so symb = 19k and
alpha(I^(19k)) <= 29k. The limit is therefore 29/19 (about 1.5263).
Computed initial values: alpha = 2,4,5,7,8,10,11,13 for s = 1..8.

Stable Harbourne. Saturated-cover lemma (any graph): let y be a maximum
b-matching for capacities a (nu = sum y_e) and T the set of saturated
vertices (including zero-capacity vertices). Then T is a vertex cover
(a non-covered edge could augment y) and sum_{v in T} a_v =
sum_{v in T} loads = at most 2 nu. A minimal C subset T gives
symb(a) <= 2 nu(a) for every exponent vector. If m in I^(2r-1) then
2 nu(a) >= symb(a) >= 2r-1 forces nu(a) >= r, i.e. m in I^r, for every
r >= 1. Exhaustive scan of about 29k canonical patterns to degree 12
plus simulated annealing found no witness for r <= 7, consistent with
the proof.

Resurgence lower bound. The monomial a_0 =
[1,1,1,1,1,0,1,1,1,1,2] (degree 11) has all 16 cover sums 7 or 8
(min 7) and nu(a_0) = 5 (solver-free dynamic program over 11 unit
copies, 85 states, plus an explicit size-5 matching), so
I^(7) not subset I^6 and rho >= 7/6. The symmetric multiples
k * a_sym have symb = 19k exactly and nu <= 29k/2 (fractional
edge-cover x = 1/2), giving genuine failures with ratios at least
38k/(29k+2) tending to 38/29; hence rho >= 38/29. Finite highlights:
k=1: 19/15; k=3: 57/44; k=5: 95/73; k=7: 133/102 (about 1.3039).

Resurgence upper bound. Lemma 1: 29 symb(a) <= 38 nu_frac(a) for all
real a >= 0. Since nu_frac(a) = min{a.x : x fractional edge-cover},
half-integrality of fractional edge-cover vertices reduces this to
checking min_{a in P} a.x >= 29/38 for every half-integral edge-cover
vertex x, where P is the cover polyhedron. There are 474 D5-canonical
such x (enumerated); each is certified by an exact rational z-packing
of value >= 29/38 (worst case x = 1/2 by hand with z = y*/2; the other
473 by machine certificates re-verified in pure-stdlib arithmetic).

Lemma 2: nu_frac(a) - nu(a) <= 1/2 (hence <= 1) for every integral a.
Fix integral a and a minimal-support optimal fractional packing y*.
(a-b) Every support component satisfies |E(K)| <= |V(K)|
(pseudoforest: otherwise a kernel perturbation improves or kills a
support edge), so no even cycle occurs and components are trees or
odd-unicyclic (M4 is triangle-free, so odd cycles have length >= 5);
tight-row counting gives |E(K)| <= |T_K|, so y*|_K solves a nonsingular
incidence subsystem with det +-1 on trees (totally unimodular) and
+-2 on odd-unicyclic components: half-integral. (c) At most one
half-edge component is nonbipartite, because the odd-cycle packing
number of M4 is 1 (exhaustive 2^11 subset enumeration, 594
nonbipartite induced subsets, independently re-verified). (d) Round
each half-edge component separately: bipartite components round with
zero loss by total unimodularity; the single odd-unicyclic component
J_0 loses at most 1/2 by deleting one cycle edge and rounding on the
spanning tree. Total integral value >= sum y* - 1/2.

For any failure pair (m, r) = (symb(a), nu(a)+1):
29m <= 38 nu_frac(a) <= 38 nu(a) + 38 = 38r, so m/r <= 38/29.
Combined with the lower family, rho(I) = 38/29 (about 1.3103).

## Limitations

All ILP optima (alpha table, matching numbers except the DP-certified
witness a_0) rely on the CBC solver; key values are cross-checked by
independent exact methods (solver-free DP for a_0, stdlib-only
re-verification of the 473 Lemma-1 rational certificates and of the
594-set odd-packing certificate). Lemma 2 is a complete self-contained
proof; gap numerics are consistency checks only, not used for the bound.

## Reproducibility

Run output/artifacts/m4_data.py, m4_setup.py, m4_dual.py,
m4_witness_verify.py and output/artifacts/probe/verify_certs.py
(stdlib-only) and probe/verify_odd_packing.py (stdlib-only).
Enumerated covers, certificates, and the odd-packing list are stored
under output/artifacts/probe/.

## References

- C. Bocci et al., The Waldschmidt constant for squarefree monomial
  ideals, J. Algebraic Combin. 44 (2016), 875-904 (arXiv:1508.00477):
  LP/duality method, fractional-chromatic formula, and graph families.
- Y. Gu, H. T. Ha, J. O'Rourke, J. Skelton, Symbolic powers of edge
  ideals of graphs (arXiv:1805.03428): unicyclic decomposition with
  Waldschmidt (2n+1)/(n+1) and resurgence (2n+2)/(2n+1); M4 with 20
  edges is not unicyclic so its theorems do not cover this claim.
- A. Alilooee, A. Banerjee, Symbolic powers of multipartite
  hypergraphs and Waldschmidt constant (arXiv:2103.06468): r-partite
  criterion and path-ideal formulas; not the M4 edge ideal.
