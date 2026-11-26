# Independent mathematical audit

## correctness

PASS

The ordered leftmost leaf always follows the left child; its kernel is exactly the equal mixture of J and m-J with mass 1/(j H_{m-1}) for J=j. For potential log H_{m-1}, the J-branch rth drop moment is a singular-endpoint Riemann sum for the rth exponential moment r!: the mesh is at most 1/H_{m-1}, the first cell is separately bounded, and the difference of upper and lower sums on the other cells telescopes under that mesh bound. On the m-J branch, J≤m/2 makes the drop O(1/H_{m-1}); J>m/2 has probability O(1/H_{m-1}) and drop at most the full potential. This establishes both the 1/2 drift and 3/4 variance, with a uniform fourth-moment bound. Above cutoff potential b=y^{1/3}, y=log H_{n-1}, the cumulative drift error is negligible in probability and in expectation because Eτ≤4y and the uniform error is exponentially small in b up to a polynomial. The stopped telescope gives τ/y→2 and the martingale bracket divided by y tends to 3/2; conditional Lindeberg follows from the fourth moments and Eτ=O(y), using a deterministic n-1 horizon with increments zero after stopping. Inversion of the drift gives variance parameter 6 for the CLT. The remaining mean time is O(1+b) by the fixed low-state drift bound and strict descent; it is negligible at the CLT scale, and the expected telescope gives E[T_n]=2y+O(1+b). This checks CLT normalization, not a separately asserted asymptotic for Var(T_n). An independent direct moment recurrence (`python3 /workspace/branches/eea45fe0-d889-41a7-8485-f669c546fef2/independent_boundary_recurrence.py`) checked normalization through 2000 and gave E[T_2000]≈4.94939, Var(T_2000)≈7.34794; the finite check is not the asymptotic proof.

## originality

PASS

Credit the CLT for the deterministic endpoint of the ordered interval model, not the first-order mean or a uniform-leaf CLT. The closest primary source poses the ordered-label distribution question explicitly, predicts 2 log log n in the discrete case, and reports the same first-order mean indirectly via a recursion for expected tree balance. The Gaussian fluctuation statement with its stated normalization is not supplied by these sources.

## value

PASS

The result answers the discrete fixed-endpoint instance of an explicit ordered-label distribution question. Its depth scale and Gaussian normalization identify behavior not captured by uniform tagging or maximum-height theorems, and the proof turns the heuristic harmonic jump picture into controlled fluctuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
