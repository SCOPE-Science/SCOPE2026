# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The recurrence is the source paper's angle-bisector recurrence with the fixed base-ray cosine 7/8 replaced by a general parameter c. The selected-edge condition is explicit: when t<c, PA is the only obtuse dihedral, because its cosine has the sign of t-c, while the PB cosine has numerator 1-ct>1-c^2>0 and the other four dihedrals are acute or right.

On the degenerate boundary b=0, the fixed-point equation reduces exactly to 2c tau^3-3 tau^2+1=0. For c>1/sqrt(2), this polynomial is strictly decreasing on (0,c), is positive at 1/sqrt(2), and negative at c, giving a unique tau in (1/sqrt(2),c). Direct differentiation plus the fixed-point identity gives the exact multiplier f_c'(tau)=-1/2. A standard forward-invariant contraction rectangle then gives a local basin, summability of t_n-tau, and convergence of the product b_n/tau^n to a positive constant.

The second-order law was stress-tested separately. Taylor expansion in delta=t-tau and u=b^2 gives delta^+=-(1/2)delta+g u+o(|delta|+u), while u^+/u tends to tau^2. Since tau^2>1/2, delta/u converges to g/(tau^2+1/2), yielding the stated K. Exact symbolic checks verify both the fixed-point polynomial reduction and the angle-doubling identity. High-precision recurrence calculations verify the constants and scaled asymptotics for the source seed and additional parameter choices.

The inradius formula follows from r=3V/S using the four face areas. The diameter formula is valid in the stated small-b regime, where PB is the longest edge; for the source rectangle this is already established in the primary paper.

## Originality

The primary source arXiv:2609.18788 was inspected at theorem and recurrence level. It fixes c=7/8, proves the invariant rectangle, unique selected edge, explicit recurrence, exponential upper/lower bounds for b_n, a (5/4)^n lower bound for h/r, and qualitative degeneration. It does not state an asymptotic fixed point, exact exponential rate, a second-order approach law, a general c-family, a continuum of rates, or the limiting angle-doubling relation.

Searches included the source identifier and title; the exact polynomial 7t^3-12t^2+4; the numerical constants 0.783553... and 1.276237...; and synonymous combinations of largest-dihedral-angle bisection, tetrahedral degeneration, asymptotic rate, fixed point, attractor, and recurrence. No inspected source contained the present formulas. Related work by Michaud--Korotov and by Adiprasito--Kalmanovich--Solomon studies dynamical behavior for longest-edge bisection, a different refinement rule, and does not imply this LAB boundary-attractor calculation.

The source is extremely recent, so simultaneous or not-yet-indexed follow-up work is the main residual originality risk. The claim is only to the best of our knowledge.

## Value

The result changes the source counterexample from a single trapped orbit with coarse geometric bounds into an explicitly parameterized asymptotic dynamical mechanism. It identifies the exact growth base of the mesh-conditioning ratio, shows that the approach to the degenerate shape has a universal transverse multiplier -1/2, gives a continuum of realizable degeneration rates, and explains the limiting geometry through an exact angle-doubling equilibrium. These sharpen both the quantitative severity and the structural interpretation of LAB degeneration.

The contribution is not a classification of all tetrahedral LAB dynamics and does not establish a full-dimensional open basin in unrestricted tetrahedral shape space.
