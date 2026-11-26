# Independent mathematical audit

## correctness

PASS

The frozen example incorrectly calls the optimum a two-character frame for every prime (e.g. it has three characters for p=3). The frozen running description also overstates the verifier: it filters at the predicted size rather than finding the minimum. Complete replacements in /workspace/repairs/1 fix the example, make positivity and nonemptiness explicit, and accurately document a replacement verifier. Rechecked the final theorem: Gram entries off the diagonal vanish precisely at the primitive orders specified by J. Reducing below degree p^(j+1), divisibility by 1+X^(p^j)+…+X^((p-1)p^j) is equivalent to constant coefficients across each digit fiber, since the quotient has degree <p^j. Nonempty branching forces >=p^r leaves, with equality precisely at p or 1 children as specified. The converses use equal numbers of leaves under forced siblings. Products of free choices give E. Above the last free level the tree fills complete residue classes, giving the subgroup p^s; the larger subgroup p^(s-1) would fill all children at the last free level, contradiction. Nested subgroups give equality and uniform orbit size, including the singleton and full-group cases. The repaired example has p characters and the stated counts. I ran the replacement /workspace/repairs/1/verify.py: exact cyclotomic long division and observed minimization over all subsets and profiles at N=2,4,8,16,3,9,5,7 reproduced all counts, stabilizers, orbit counts, and arities. This is a finite diagnostic supplement to the proof.

## originality

PASS

On re-audit, the repair distinguishes the known minimum, equivalent homogeneous-tree characterization and immediate product for the raw count from its surviving focus: the uniform frequency-translation stabilizer for all optimizers and its exact quotient census. The strongest inspected precedent provides the structural classification but no such subgroup or orbit theorem. Passing this bounded enumerative refinement does not award originality to the minimum or the classification.

## value

PASS

The repaired result tells a sampler how many genuinely distinct minimal unweighted designs there are after removing the natural equivalence of a common frequency shift. It also determines the exact subgroup of shifts fixing any design, even for redundant frames, rather than assuming a free action or simply dividing by the group order. The nonuniform degeneracy between profiles and uniform stabilizer within each profile are meaningful structural information; the value is modest and lies in the quotient invariant, not the routine product or known minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
