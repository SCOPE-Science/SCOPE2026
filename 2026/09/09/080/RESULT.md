# S0 chain-type stem of order 5^5: full H^2 Aut-orbit census and class-2 centre-25 obstruction

## Context
Classification of groups of prime-power order by coclass (Leedham–Green–Newman),
isoclinism families (Hall; James for order p^6), and constructive p-group
generation (O'Brien) treats each closed isoclinism-cell orbit census or sharp
extension obstruction as the standard progress unit. The target was the James
Phi_7 coclass-2 subcell at order 5^6 (class 2, centre of order 25) via a logged
Lazard Lie-ring plus H^2 automorphism-orbit table. Pursuing that census on the
fixed chain-type stem quotient revealed that this stem admits no such
extension; the census plus the obstruction localizing the failure to one named
cocycle line is the reported headline result.

## Definitions
- p = 5. Q = 5-dimensional class-2 Lie algebra over F5 with basis
  e0,e1,e2,f0,f1 and presentation S0: [e0,e1] = f0, [e0,e2] = f1 (all other
  basis brackets zero). Verified stem: Z(Q) = Q' = span{f0,f1}, dim 2.
  Class 2 < 5, so Lazard covers the exponent-5 stratum of the corresponding
  group stem quotient of order 5^5.
- Coefficients: trivial module F5 (central kernel C of order 5).
- Pairs ordered (i,j), i<j, encoded as 10-vectors; H^2 = H^2_Lie(Q, F5).
- Extension: for cocycle w, L = Q + span{c} with [x,y]_L = [x,y]_Q + w(x,y)c.
- W = {w : w(Z(Q), Q) = 0}, the class-preservation subspace.
- Aut(Q) in column convention; A-part = induced 3x3 action on Q/Z(Q);
  T-part = 2x3 central translations.

## Result (headline claim)
Let Q be the S0 algebra above. Then:
1. dim H^2_Lie(Q, F5) = 6, with explicit normalized 10-vector basis logged in
   committed_log.json (key H2basis10).
2. |Aut(Q)| = 750,000,000 = 48,000 x 5^6, via 12 committed 5x5 generators
   (6 H-lifts generating the full plane-stabilizer A-part of order 48,000;
   6 elementary T-translations generating the full 5^6 kernel). Aut(Q)
   partitions all 5^6 = 15,625 H^2 classes into exactly 8 orbits:

   | orbit | size | stabilizer order | min rep (coords) |
   |---|---|---|---|
   | 0 | 1 | 750000000 | (0,0,0,0,0,0) |
   | 4 | 4 | 187500000 | (0,0,1,0,0,0) |
   | 5 | 24 | 31250000 | (0,1,0,0,0,0) |
   | 7 | 96 | 7812500 | (0,1,1,0,0,0) |
   | 1 | 600 | 1250000 | (0,0,0,0,0,1) |
   | 6 | 2400 | 312500 | (0,1,0,1,0,0) |
   | 3 | 5000 | 150000 | (0,0,0,1,0,2) |
   | 2 | 7500 | 100000 | (0,0,0,0,1,0) |

   Sizes sum to 15,625 with orbit-stabilizer exact per orbit. Full 10-vector
   representatives in committed_log.json (linear_orbits[].rep10).
3. Class-preservation lemma: a 1-dim central extension stays class <= 2 iff
   its class lies in W. dim W = 1; W is Aut-stable with orbits {0} and one
   orbit of the 4 nonzero classes.
4. Obstruction theorem: both class-<=2 one-step extensions (split Q x F5 and
   the nonzero-W extension) have centre dimension 3. Hence Q admits NO
   6-dimensional class-2 extension with centre of order 25 (no exponent-5
   Phi_7 group of order 5^6 from this stem quotient).

## Proof / evidence
Finite exact computation over F5, stdlib only:
- Jacobi on all 625 quadruples; centre dim 2, derived dim 2.
- Jacobi-constraint matrix on ten alternating pair-variables has rank 2
  (dim Z^2 = 8); coboundary image spanned by pairs (e0,e1),(e0,e2) (rank 2);
  normalized quotient {z01 = z02 = 0} gives dim H^2 = 6.
- Aut completeness: A in GL(3,5) lifts iff it preserves plane span{e1,e2}
  (equivalently wedge images of (0,1),(0,2) span the centre plane and image
  of (1,2) vanishes, with nonzero determinant); exhaustive enumeration of
  all 5^9 matrices confirms liftable set = plane-stabilizer = 48,000
  elements, and the 6 logged H-gens BFS-close to exactly 48,000; the 6
  elementary T-blocks each preserve brackets (central shifts) and generate
  all 5^6 translations; centre characteristic forces the block form.
- Action (g.w)(x,y) = w(g^{-1}x, g^{-1}y) + normalization; 12 recomputed 6x6
  matrices byte-match the log; BFS over all 15,625 classes yields the
  8-orbit partition.
- Lemma: in L, [[ea,eb],ec] = w([ea,eb]_Q, ec)c since Q is class 2; with
  [Q,Q] = Z(Q) this vanishes for all triples iff w|_{ZxQ} = 0; coboundaries
  df(x,y) = f([x,y]) vanish on ZxQ so the condition descends to H^2.
- W computed as coordinate nullspace (dim 1), Aut-stability checked on all
  generators, W-orbit BFS gives {0} + 4-class orbit; extension centre dims
  recomputed as 3 and 3.
- Replay: `python3 output/artifacts/verify.py` prints VERIFY_OK (10 checks).
  Builders: `s0_h2_aut_orbits.py`, `w_orbits.py`.

## Limitations
- Full Phi_7 cell closure (James-count match, SmallGroups cross-IDs) is NOT
  achieved; a Phi_7 group of order 5^6 must come from a different stem
  quotient or a non-Lie exponent-25 lift.
- Group reading restricted to the exponent-5 Lazard stratum (class 2 < 5).
- Preset fallback constants (3 orbits; stabilizers 2400/480/120; dim H^2<=4)
  are refuted for this S0 and not claimed.
- Sibling S1 corroboration cited in DRAFT references a log absent from the
  artifact set and is not part of the certified headline.

## Reproducibility
- `python3 output/artifacts/s0_h2_aut_orbits.py` rebuilds S0, H^2, Aut gens,
  action, full partition; writes committed_log.json.
- `python3 output/artifacts/w_orbits.py` class-preservation analysis.
- `python3 output/artifacts/verify.py` independent reimplementation; expect
  VERIFY_OK. Stdlib only; seconds to minutes.

## References
- O. Garaialde Ocana, J. Gonzalez-Sanchez, Transporting cohomology in Lazard
  correspondence, arXiv:1405.4654 (general H^i transport; no cell orbit table).
- M. L. Lewis, J. Maglione, Enumerating isoclinism classes of semi-extraspecial
  groups, arXiv:1806.10511 (different family/method).
- M. F. Newman, E. A. O'Brien, M. R. Vaughan-Lee, Presentations for the groups
  of order p^6 for prime p>=7, arXiv:2302.02677 (p>=7 only; no H^2 orbit log).
- P. K. Rai, M. K. Yadav, On Sh-rigidity of groups of order p^6,
  arXiv:1412.0884 (|Out_c| census, not H^2 orbit partition).
