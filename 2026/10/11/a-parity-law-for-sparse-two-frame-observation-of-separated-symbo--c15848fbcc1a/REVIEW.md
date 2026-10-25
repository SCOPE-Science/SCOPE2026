# Mathematical review — separated symbolic sensor observation

## Correctness — PASS
The threshold metric observes exactly coded frames 0 and 1. A full-shift discrepancy at coordinate k is detectable at a chosen time n exactly when k lies in n+{0,1,d,d+1}. Singleton discrepancies prove necessity of A+F_d=Z; arbitrary distinct sequences prove sufficiency. Uniform four-point incidence supplies the lower bound 1/4. The last d coordinates of any block of 2d+1 positions require at least ceil(d/2) observation times, because any three different offsets in F_d span at least d. This yields the odd-d obstruction (d+1)/(4d+2). Residue schedules modulo 2d (even) or 2d+1 (odd) attain the bounds. The duplicated offset for d=1 is handled explicitly and gives 1/3. These arguments work for every positive integer d; finite computations are supporting checks only.

## Originality — PASS, with primary-literature priority risk
The coding-to-covering reduction and the general observation-cost invariant are foundations from earlier work. Ferrari (DOI 10.3934/jdg.2026045) treats this general observation problem and gives the full-shift standard contiguous-window result; the d=1 and d=2 contiguous special cases are accordingly not independently new. Bollobás, Janson and Riordan (arXiv:0910.3815, Theorem 5.1) give a general finite-pattern covering algorithm and periodic-optimum existence, but their inspected statements do not evaluate the separated four-point family uniformly in d. Li, Offner and Ye (arXiv:2501.01571) analyze a different packing extremum. The surviving claimed contribution is the all-separation explicit parity law together with its sharp incidence proof and periodic constructions. Ferrari's full theorem sections were not accessible in the available open text, so an earlier hidden equivalent cannot be excluded; historical priority is not certified.

## Mathematical value — PASS
Two separated symbolic sensors observed at two neighboring frames form a motivated sampling pattern. The exact even/odd transition distinguishes tiling by four-point windows from a sharp local overlap obstruction. The odd penalty above 1/4 is 1/(8d+4). The uniform law is useful as a precise design benchmark and does not purport to govern all metrics or subshifts.

## Relevant literature
1. Luis Ferrari, *Observer–hider games for expansive dynamical systems*, Journal of Dynamics and Games (2026), DOI 10.3934/jdg.2026045.
2. Béla Bollobás, Svante Janson and Oliver Riordan, *On covering by translates of a set*, Random Structures & Algorithms 38 (2011), arXiv:0910.3815.
3. Cindy Li, David Offner and Iris Ye, *Minimum packing density for sets of four integers*, arXiv:2501.01571 (2025).

No formal proof assistant certificate or external expert attestation is asserted.
