# Independent mathematical audit

## correctness

PASS

The finding is read as the displayed reduced-homology statement at RESULT.md line 18; its introductory sentence should say ‘reduced rational homology’ since ordinary H_0 never vanishes for these nonempty quotients. The established cycle homotopy types place reduced homology in d_n=floor((n−2)/3), rank two exactly when 3 divides n. In the augmented signed chain trace, a permutation orbit of length l contributes (−1)^l(−1)^(l−1)=−1 when selected. For rotations the quotient of permissible orbits is C_a for a=gcd(n,j)≥3, a single edge for a=2, and has no permissible orbit for a=1. Evaluating the path recurrence p_k=p_(k−1)−p_(k−2) and the cycle decomposition by omitting or selecting vertex zero gives the six-periodic cycle trace 2 cos(πa/3). For reflections folding the cycle gives a path of length (n−1)/2, n/2+1, or n/2−2; discard precisely the paired adjacent endpoints, including both pairs at n=4 for the edge axis. Direct residues in p_k=(1,0,−1,−1,0,1) periodically yield the four line characters. For rank two the generator trace ±1 forces determinant +1 (determinant −1 would force eigenvalues ±1 and zero trace), hence the primitive third or sixth roots. A reflection exchanges these eigenlines, giving trace zero. Equivariant subdivision and rational chain averaging give the quotient from invariant homology, nonzero only for the two trivial-line residues; averaging applies to reduced H_0 as well. Independent replay: python3 /workspace/review-evidence/reproduce.py 2, log /workspace/review-evidence/2.txt; 336 direct signed characters for n=3..18 and independent mod-two rank checks through n=13. These are corroboration, not the all-length proof. Supplied scripts were inspected, not run.

## originality

PASS

The supported distinct contribution is the complete combined character, in particular the two even-cycle reflection classes in the one-dimensional families. Credit prior odd-cycle reflections, full rotational quotient support, partial integral-module and quotient-homotopy coverage. The reduced full-quotient arithmetic criterion is a consequence rather than an independent novelty: combine odd-cycle reflection data with the vanishing or survival of rotation invariants. No verified primary or exact indexed statement settles the remaining even one-dimensional reflection sign for all lengths; two plausible matching-character record identifiers from the frozen evidence could not be resolved and remain a material access risk, not evidence of noncoverage.

## value

PASS

The surviving distinction is a natural axis-sensitive representation invariant for a standard complex. For example, in the even rank-one families it specifies which of two geometrically different reflection subgroups preserves the homology line, information invisible to ranks and to full-group vanishing. The uniform assignment matters independently of the quotient residue criterion, which is already accessible from combined results. No significance is claimed for an integral-lattice classification or unseen quotient topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
