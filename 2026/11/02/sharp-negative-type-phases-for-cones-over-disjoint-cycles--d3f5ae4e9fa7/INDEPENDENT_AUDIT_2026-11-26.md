# Independent mathematical audit

## correctness

PASS

The hub-anchored matrix is [qI+(q−1)A+(2−q)J]/2, with A the rim adjacency and J all ones. On the overall constants and between-rim mean-zero constants it has eigenvalues [2(n−1)−(n−3)q]/2 and (3q−2)/2 respectively. All remaining modes have eigenvalues [q+2(q−1)cos(2πj/ell)]/2. An even cycle first contributes one zero at q=2; otherwise the least eigenvalues are attained exactly on the longest odd rims and yield the stated local root. Positive cross-multiplication gives the comparison at n=cot²(π/(2L)); a tie would give the rational algebraic integer 2cos(π/L)=2(n−1)/(n+1), strictly between 1 and 2. Each first zero crosses with negative slope. The kernel and dimensions follow by the group and Fourier multiplicities and Gram rank, including unbounded even nullities by taking a fixed number h of equal sufficiently long odd rims, since cot²(π/(2L))/L→∞. The frozen notes report a bounded run (499 checks); its referenced script is not among the attached support. The independent `python /workspace/branches/independent_reproduction.py 2` passed 11 shortest-path/Gram cases, including mixed rims, multiple critical modes, and both sides of the seven-cycle/triangle switch. The analytic argument covers all permitted parameters, not the finite run.

## originality

PASS

The general diameter-two test and wheel spectral methods are prior, as is the isolated C5 threshold. The distinct supported claim is the full mixed-rim phase and endpoint-nullity classification, including the impossibility of resonance and arbitrary positive even nullity in the local phase. The closest inspected indexed result uses shared-vertex bouquets, not universally joined hubs on disjoint rims. No exact coverage of the mixed-rim claim was established in the inspected evidence.

## value

PASS

The local-versus-global decision answers where critical equality loads live, not merely what the exponent is. It gives a concrete transition from adding triangle rims without changing the longest local cycle, proves no critical-mode collision, and realizes arbitrarily large even embedding-rank drops. These conclusions are useful beyond a one-off wheel calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
