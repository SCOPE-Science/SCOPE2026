# Same-model review

## Correctness

**Assessment: PASS.**

The proof uses two source-paper inputs: registration of every Chair44 tiling on the cubic lattice with proper cubic frames, and the unique coherent hierarchy phase \(\alpha_n(T)\in\mathbb Z^3/2^n\mathbb Z^3\). A symmetry \(g(x)=Rx+t\) must preserve the unique level-\(n\) parent partition, so
\[
R\alpha_n+t\equiv\alpha_n\pmod{2^n}
\]
for every \(n\), giving \((I-R)\alpha=t\) in \(\mathbb Z_2^3\). This is the central identity; it was checked against the source's translation covariance of the hierarchy phase.

For a single nonidentity proper cubic rotation, \(I-R\) has rank two. The complete signed-permutation census gives Smith invariant factors \((1,1)\), \((1,2)\), or \((2,2)\). Because the phase coordinates lie in \(\mathbb Z_2\), the condition \(d x\in\mathbb Z\) with \(d=1\) or \(2\) forces \(x\in\mathbb Z\). Hence each compatible set is a unimodular image of \(\mathbb Z^2\times\mathbb Z_2\), proving density, Haar nullity, meagerness, and exact 2-adic Hausdorff dimension one.

For a noncyclic subgroup, the subgroup classification of the proper cubic group reduces to two Klein-four types and a dihedral group of order six; explicit generators in RESULT.md force all three phase coordinates to be ordinary integers. Larger noncyclic subgroup types contain one of these. The standalone finite census separately checks all 30 subgroups of the proper cubic group: every noncyclic subgroup has stacked \((I-R)\)-matrix of rank three with power-of-two third determinantal divisor, which gives the same integral-phase conclusion by Smith normal form.

The invariant-measure corollary is also exact. Translation covariance makes the pushforward phase measure invariant under the dense subgroup \(\mathbb Z^3\) of \(\mathbb Z_2^3\); continuity then promotes this to full translation invariance, hence Haar measure. No ergodicity or independence assumption is used.

Potential failure modes checked:
- orientation-reversing symmetries are excluded by the source's homochirality/registration structure;
- the affine translation part of a registered symmetry is integral;
- the phase relation is imposed at every hierarchy level, not merely at one finite scale;
- the ordinary integers \(\mathbb Z\) are distinguished from the 2-adic integers \(\mathbb Z_2\);
- noncyclic symmetry is only claimed to force integral phase, not to exist at every integral phase;
- the dense \(G_\delta\) statement is restricted to the primitive substitution hull, where minimality is standard.

## Originality

**Assessment: PASS, to the best of our knowledge.**

The motivating source, Tsiokos arXiv:2609.19214, was inspected at the theorem on the symmetry bound, the hierarchy-phase proposition, the registered substitution discussion, and the final questions. It proves the order-24 upper bound and constructs the coherent \(2^n\)-phase data, but no statement was found connecting an individual tiling's Euclidean point group to the 2-adic phase, no Haar-null or Hausdorff-dimension exceptional-set theorem, and no reduction of noncyclic or order-24 symmetry to the zero-phase fiber.

Targeted external searches covered:
- Chair44 with 2-adic phase, Haar measure, generic/asymptotic symmetry, and Hausdorff dimension;
- substitution tilings with p-adic/odometer factors and rotational stabilizers;
- generic or almost-everywhere trivial symmetry of aperiodic tilings;
- extended/reversing symmetries of multidimensional substitution shifts;
- Taylor--Socolar and classical chair tilings with adic/model-set descriptions.

The closest conceptual precedent located is Lee--Moody's Taylor--Socolar analysis, where an adic internal factor has a dense measure-zero singular set. Baake--Roberts--Yassawi and Bustos--Luz--Mañibo study global extended symmetry groups of shift systems, not the stabilizer of an individual Chair44 tiling or the arithmetic phase obstruction here. No prior statement of the phase-compatible subgroup \(P_a\), the exact \(\mathbb Z^2\times\mathbb Z_2\) exceptional sets, the noncyclic-implies-integral dichotomy, or the zero-phase reduction was found.

The current SCOPE archive was searched by Chair44, the arXiv identifier 2609.19214, aperiodic tilings, 2-adic phase, and synonymous symmetry terms; no overlapping record was found, and the recent repository changes inspected directly were unrelated.

No specific inaccessible paper was identified as a likely source of the exact claim. The main residual originality risk is recency: the Chair44 preprint was submitted only days ago, so parallel or not-yet-indexed follow-up work may exist.

## Value

**Assessment: PASS.**

The source paper leaves open which finite symmetry groups occur and whether the upper bound 24 is attained. The new result gives a deterministic arithmetic sieve on that question. Generic 2-adic phases prohibit all symmetry; nonintegral phases permit at most cyclic groups of orders 2, 3, or 4; and every larger or noncyclic symmetry is confined, up to translation, to one phase fiber. This converts a global symmetry search over the full tiling space into a zero-phase problem for all candidate groups of order greater than four.

The exact structure and dimension of the exceptional phase set also give a geometric measure-theoretic picture that is not contained in the finite order bound: symmetry-compatible phases are dense but occupy only a codimension-two 2-adic set, and every invariant random Chair44 tiling is almost surely asymmetric.

## Scientific limitations

The phase condition is only necessary. The zero-phase fiber may contain mostly asymmetric tilings, and this work does not classify its stabilizers or decide whether the order-24 bound is attained. The Hausdorff dimension refers to phase space rather than the tiling hull. Topological genericity is asserted only for the primitive substitution hull, not for the entire matching-rule space. The motivating source is exceptionally recent, so unindexed parallel work remains possible.

Same-model review: passed. Independent audit: not yet performed.
