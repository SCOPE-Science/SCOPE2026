# Independent mathematical audit

## correctness

PASS

At any state with x clique and y independent unmatched vertices of K_x∨bar(K_y), eligible clique edges number x(x−1)/2 and cross edges xy; the next uniformly sampled edge is therefore internal with probability (x−1)/(x−1+2y) and crossing with probability 2y/(x−1+2y). Conditioning gives the stated finite rational distribution recursion and exact endpoints. Independent small-state rational recursion reproduced representative terminal laws and matching-size parity. For a_n/n→α>0,b_n/n→β>0, exponential edge clocks of rate 1/n yield fluid drift dx/dt=−x²−xy,dy/dt=−xy. The first integral x/y−log(y/β)=α/β leads to terminal survivor y*=βe^(−α/β). Uniform drift/martingale estimates justify endpoint convergence; stopping when x<=εn controls late survivors. The finite-parameter invariant H_n=x/y−log(y/β_n)−r_n has jumps O(1/n) and conditional drift O(1/n²) per accepted match; its centered martingale bracket converges to [4−e^(−r)(r+2)²]/y*. A stopping argument keeps the late part O(ε²), allowing martingale CLT and delta method Y centered at z_n=b_n exp(−a_n/b_n) with variance v=βe^(−r)[4−e^(−r)(r+2)²]. This v>0 for r>0. Matching size differs from (a+b−Y)/2 by at most 1/2, preserving the CLT. The maximum matching size is min(a,floor((a+b)/2)); differentiating the two branches of the asymptotic efficiency ratio gives a unique minimum at r=1 of 1−1/(2e). The finite exact solver check.py was read; full-edge-order enumeration and simulations corroborate only finite cases, not the stopped martingale limit.

## originality

PASS

The exact recursion and dense complete-split fluid/CLT constants, especially unique 1−1/(2e) efficiency minimum, are not contained in the inspected Arnosti random BIPARTITE graph results or the accessible descriptions of Dyer–Frieze general greedy matching. Those classical papers are acknowledged as contextual foundations for random-edge greedy algorithms and sparse random graph limits. The highly relevant 1991 Dyer–Frieze full text could not be reached by lawful arXiv/open access or authorized institutional access; its possible special dense-split calculations remain an explicit originality risk, not an automatic failure.

## value

PASS

Uniform random-EDGE maximal matching is a canonical greedy algorithm, and complete split graphs are a simple structured dense obstruction to optimality. The exact finite law, Gaussian survivor fluctuations, and sharp worst balance ratio quantify both algorithmic performance and variability rather than a tiny graph example. In particular a split graph with a perfect matching can lose a nonzero 1/(2e) fraction asymptotically under uniform greedy edge ordering; the variance is a reproducible natural statistic for randomized-algorithm benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
