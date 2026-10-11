# Review

## Correctness
PASS. The source's arbitrary-initial theorem supplies the upper rate bound. Sharpness is reconstructed by two exact modes: fixed-diagonal perturbations satisfy an affine scalar error recurrence with multiplier \(1-c_0/c\), while a nontrivial normalized diagonal coordinate satisfies \(p_k=p_0^{(1-1/c)^k}\) and therefore has root rate \(|1-1/c|\). These two witnesses make the upper bound exact in the worst case. The scalar minimax problem is then solved by equioscillation, with edge cases \(c=1\), \(c=c_0\), and \(c_0=1\) treated explicitly.

## Originality
PASS. The focal primary source was inspected at its fixed-diagonal recurrence, arbitrary-initial diagonal formula, and convergence-rate theorem. It states the sharp convergence threshold for fixed diagonal and only a sufficient arbitrary-initial convergence result with an upper rate bound; searches within the inspected text did not locate an optimal, minimum, or worst-case tuning theorem. Semantic searches for exact worst-case rate, relaxation tuning, equioscillation, and the source identifier returned no same-object published finding. The immediately preceding upper-triangular Karcher-mean paper concerns existence, uniqueness, analyticity, and recursive mean formulas rather than projection-iteration tuning.

## Value
PASS. The parameter \(c\) is the algorithm's natural relaxation choice, and the source leaves an explicit two-mode rate bound without identifying the fastest globally robust value. Proving both modes sharp converts that estimate into an exact worst-case objective and yields a unique optimal parameter for every data set through \(c_0\). This is a structural algorithmic conclusion rather than a sampled special case or a routine restatement of the fixed-diagonal threshold.

## Closest literature and limitations
Huang's arXiv:2609.37018v1 is the closest source and supplies every nonstandard recurrence used in the proof. Huang--Lawson arXiv:2609.34267v1 is a broader mean-existence and computation paper for upper-triangular Lie groups. Targeted searches also surfaced unrelated minimax tuning results for Richardson, FRB/RFB, weighted Jacobi, and extragradient schemes; those algorithms do not imply the \(\operatorname{UT}_2\) projection-mean rate formula. The main residual risk is an equivalent generic relaxation observation under terminology not surfaced by the searches.

Same-model review: passed. Independent audit: not yet performed.
