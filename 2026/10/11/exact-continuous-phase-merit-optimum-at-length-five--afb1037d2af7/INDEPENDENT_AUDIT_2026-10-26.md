# Independent mathematical audit

## correctness

PASS

For all c_j of unit modulus, Parseval gives ||P||_4^4=25+2 sum_{k=1}^4|C_k|²; |C4|²=1. Scalar/modulation normalization gives c=(1,1,p,pq,pqr) with p,q,r on T. Direct expansion of C1,C2,C3 and minimization over p yields K−2|L|. Let q=e^{iβ}, r=e^{iγ}, x=cosβ, y=cosγ, z=cos(β−γ): K=9+4x+4y+2z and |L|²=7+6x+6y+2z+4xy. K≥2 follows as a sum of phase-averaged squared moduli. The inequality K−2|L|≥1 reduces to D=(K−1)²/4−|L|²=4Q(A,B), with A=cos((β+γ)/2), B=cos((β−γ)/2), Q=(4B²−1)A²+B(4B²+3)A+B⁴+B²+2. Symmetry takes B≥0. On B≤1/2, concavity in A makes A=−1 the minimizer; on B≥1/2 the convex vertex is at/beyond −1 by positive factor 1+(1−B)(1+4B(1−B)). The endpoint Q(−1,B)=(1−B)[(1−B)²+B²(2−B)]≥0 with equality only B=1,A=−1 up to simultaneous sign reversal. Consequently q=r=−1, then remaining objective 1+|p−1|² forces p=1. Undo normalization gives precisely c_j=λ η^j times (1,1,1,−1,1), E=2, ||P||4^4=29 and merit 25/4. Independently re-expanded K, D→4Q, factor and vertex identities by exact SymPy; exact Barker autocorrelations are (0,1,0,1). Finite checker stress tests do not prove universal claim.

## originality

PASS

No inspected prior source proves the all-complex-phase length-five global inequality with complete equality orbit. Borwein–Ferguson (2005) tabulate E=2.000 as a stochastic lowest found, but provide statistical rather than analytic global certification. Binary Barker literature knows the same value for +/-1 coefficients, a strictly smaller feasible set. Neuwirth phase-extremal and even-moment analyses do not dominate the five-term continuous-phase minimization. Related published SCOPE results treat length six or nonconsecutive/different Fourier supports. This is best-of-knowledge, not a priority guarantee.

## value

PASS

The aperiodic base energy/merit factor is a canonical intrinsic quality measure for unimodular/polyphase sequences. Length five is a natural minimal nontrivial Barker boundary case, and the literature previously provided E=2 as a numerical/polyphase search candidate and a binary sequence. Proving its exact global optimality over the entire continuous complex phase torus, and showing the only optimizers form one scalar/modulation orbit, is a useful non-tabular rigidity classification with an analytic sharp inequality. It provides a precise benchmark for continuous-phase autocorrelation design and distinguishes numerically located minima from rigorously exhaustive ones. The result is explicitly only length five and fourth moment; no larger-length theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
