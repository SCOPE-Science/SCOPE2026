# Independent mathematical audit

## correctness

PASS

An independent killed-tree derivation checks the renewal calculation. Orient edges toward the absorbing root. The equation −Lh=1 for the mean implies that its difference across any edge is the number of vertices on the upstream side, by summing that equation there. Thus the backbone differences are m_i. For v=E[T²]−h² the killed-generator equation is −Lv(x)=Σ_{y~x}(h(x)−h(y))². By symmetry the occupation-time vector from b_0 solves the unit Dirichlet point-source equation: its value at b_i and all vertices on its tooth is N−i, with zero at the target. Weighting each squared edge difference by the sum of its endpoint occupations gives (2(N−i)−1)m_i² on backbone edge i and 2(N−i)Σ_{j=1}^{ℓ_i}j²=(N−i)q(ℓ_i) on tooth i. The uniform lower-degree remainder is O_N(M²), and weighted Hölder minimizes the cubic uniquely on the real simplex; sum-preserving bounded rounding and compactness give the optimal leading coefficient and convergence for every integer minimizer. The mean is linear with strict minimum tooth coefficient at i=N−1. For N=2 the forward difference is strictly increasing in x≥0 and odd on integer inputs, with Δ(M−1)=4M²+6M+1>0 for M≥1; its crossing gives the claimed feasible ceiling and onset at M=3 (M=0 is trivial). At M=3 the placement (1,2) indeed changes (mean,variance) from (6,56) to (7,51). A fresh rational generator calculation checks 120 geometries with N=2,3,4 and budget at most four, and an exact enumeration checks two-tooth optima at M=0…8. Replay: /workspace/branches/4caa2ae5-e382-4d43-9d05-dd2fd53c4a37/ctmc_check.py. Frozen verify.py was inspected, not executed. The finite checks do not certify the asymptotic theorem or any joint limit in N and M.

## originality

PASS

Credit is limited to the deterministic fixed-total-budget variance design, including the asymptotic optimal profile and sharp finite-budget two-site transition. Finite-tree moment methods, branch-time renewal identities and the cubic one-dimensional moment are not claimed as new. The inspected literature and close indexed findings do not imply this design classification; the conclusion is bounded by the source access recorded below.

## value

PASS

Under a natural fixed trap-volume budget the standard mean and variance objectives give quantitatively different designs. The increasing weight with distance makes the unique large-budget distribution nonuniform, while every site remains occupied; moving all volume toward the exit incurs the explicit limiting loss factor S_N². The exact first departure at M=3 on the smallest nontrivial backbone is a finite, interpretable boundary for that conflict. This value is in the allocation result, not a new general first-passage method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
