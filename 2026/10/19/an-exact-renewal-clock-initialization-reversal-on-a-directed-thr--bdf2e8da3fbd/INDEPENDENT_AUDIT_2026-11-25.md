# Independent mathematical audit

## correctness

PASS

For the independent-clock process used in the proof, immediately after A activates the opinion pair (u,v) represents (u,u,v). Conditional Poisson evolution over length t gives expectations u+(v−u)te^(−t) at B and u+(v−u)e^(−t) at C. Averaging gives the stated 2-by-2 stochastic matrix and invariant row ((1−φ)/K,m/K). For each indicator opinion, that row gives a bounded martingale. At every later renewal the conditional chance that C activates before B and before the next renewal is (1−E[e^(−2T)])/2>0; this ensures almost-sure absorption and justifies using the martingale to read fixation probabilities. The first interval U gives coefficients p_B=(1−φ)E[e^(−U)]/K and p_C=((1−φ)E[Ue^(−U)]+mE[e^(−U)])/K. For the equilibrium residual the two transforms are 1−φ and 1−φ−m (differentiate (1−E[e^(−sT)])/s at 1); substituting establishes equality of p_B and p_C. Erlang-2 gives K=23/27 and checks the two vectors and strict inequalities 25/69>23/69>19/69. This argument needs independence of A's renewals and the Poisson clocks, as used in the frozen renewal/memorylessness argument; marginal clock laws alone do not suffice. The frozen VERIFICATION.md and Erlang-stage checker were inspected; the checker was not executed.

## originality

PASS

The supported distinct claim is the closed pair of fixation laws for the directed triad, especially the equilibrium equality and reversal for an unchanged interarrival law. Heterogeneous renewal copying, equilibrium initialization, and the residual-life transform are not new. None of the inspected prior formulas gives the joint comparison by substitution alone.

## value

PASS

This is a complete fixation calculation on the first directed cycle where one update need not produce consensus. The equilibrium equality is structural and holds for arbitrary positive mean-one laws, while the explicitly reversed bias shows why the renewal interval law and node rates do not by themselves characterize a prediction absent the initialization protocol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
