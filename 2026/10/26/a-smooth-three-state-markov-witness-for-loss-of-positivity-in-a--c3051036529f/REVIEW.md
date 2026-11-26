# Independent mathematical audit

## correctness

PASS

The frozen proof fails as written: its displayed product (RESULT.md lines 78–80) reverses the printed chronologies x6 then y_(n+1) in (3.19), and its A3 sample is not the one displayed in the accessible preprint. In fact the frozen displayed product gives y₂=(e^(−s)−e^(−2αs))/C and y₃=[C−(C+1)e^(−s)+e^(−(C+1)s)]/C>0 for s>0, with leading term (C+1)s²/2. Its checker evaluates only the desired closed form, so cannot detect the error. The repair uses the actual printed sequence and defines A on the whole real line, identically zero for t≤0, resolving the negative A3 evaluation. Supports are disjoint: (b_++δ)/100 is below the first positive node d₀ and 100(b_−−δ)>1; the remaining same-scale sample distances exceed δ. This also works with the upper in-interval half-step Gauss node. Local finiteness and O(t^(4−k)) derivative bounds for k≤3 yield bounded C³ regularity across zero; the triangular integral formulas give nonnegativity, and column sums preserve mass. With U=e^(−βs), V=e^(−αs), the actual first stage gives (U, β(U−V)/C) in coordinates 1 and 2; the second produces (UV,U(U−V)/C). Then UV=e^(−s), U²=e^(cs), and the stated y₃ follows by mass. Its negative numerator has opposite sign to the strictly increasing e^(cs)+ce^(−s)−(1+c), whose leading term is cCs²/2. This retains the arbitrary shrinking sequence and the exact h_n^10 law. All corrected scientific files are in repairs/1. Replay `python3 /workspace/repairs/1/verify.py`: five stage-propagation and reversal comparisons passed; n=1 gives −1.933754005405e−12 ordered and +2.693361511695e−11 reversed. The sign proof is analytic, not an extrapolation from those runs.

## originality

PASS

The repaired claim is the fixed-generator, three-state, arbitrarily-small-step counterexample with exact third coordinate for the chronological method (3.19) in the accessible primary preprint. It is not the known warning about signed stage combinations, a local generator sign test, or a positivity interval for another integrator. The compared indexed and primary statements do not cover this claim; residual access and indexing limits remain.

## value

PASS

Exact positivity is a necessary probability invariant. With one smooth generator, rather than a different generator for every step, this witness shows that taking sufficiently small steps is not a universal remedy for the named method on bounded C³ generators. It quantifies the defect and distinguishes it from an order or stability failure; its h_n^10 scale limits practical impact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
