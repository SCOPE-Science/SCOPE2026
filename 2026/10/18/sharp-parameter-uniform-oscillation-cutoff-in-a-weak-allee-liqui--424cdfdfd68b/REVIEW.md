# Independent mathematical audit

## correctness

PASS

With D=1/(xy^2), the weighted components are (x/(x+M)-y)/y^2 and (r/x)(1/y-1/x). Their divergence is [Mx/(x+M)^2-r]/(xy^2). The numerator is bounded above by 1/4-r by the identity (x+M)^2-4Mx=(x-M)^2. At r=1/4 it is negative off one line; an interior periodic Jordan curve, whose enclosed region lies in the positive quadrant, would have zero flux and strictly negative integrated divergence. At M=1/2 the trace is 1/4-r and the critical determinant is 1/16; the real parts cross with slope -1/2. Independent exact replay `python3 /workspace/review-evidence/4.py` checks the critical linear part after u=x-1/2 and v=2(y-1/2)-u and gives cubic radial coefficient -1/32 in these real coordinates and original time. This corroborates the sign and is consistent with the different complex-amplitude and time normalization in the frozen formula. The smooth supercritical Hopf theorem gives a small attracting positive cycle for r just below 1/4, enough to rule out any smaller uniform cutoff. No conclusion is drawn about global convergence, the boundary, or existence of cycles for arbitrary r<1/4. Frozen SymPy checker inspected, not executed.

## originality

PASS

The supported distinct contribution is the global, equality-inclusive, all-M no-cycle boundary. The same-model Hopf result already gives the sharpness witness; neither that witness nor Bendixson–Dulac is claimed as new. Checked statements do not establish the global bound; a plausible broader 2017 theorem remains an explicit access risk.

## value

PASS

The equality-inclusive boundary rules out even remote cycles in the exact motivated subsystem, filling a question not resolved by the local phase portrait. Maximizing the local Hopf curve alone would not provide this result. Sharpness is uniform over M, not a claim of optimality for each M.

The dated certificate retains the supplied scientific assessment, sources and limitations.
