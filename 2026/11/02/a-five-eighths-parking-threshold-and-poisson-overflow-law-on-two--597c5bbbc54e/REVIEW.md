# Scientific review

## Correctness — PASS

The result follows by a rooted-tree mass-conservation recursion that is separately compared with exhaustive sequential parking for all \(50{,}549\) small preference sequences. Under independent Poisson arrivals, two doubly preferred leaves under one intermediate parent occur with probability asymptotic to \(t^4/(8b)\); the number of such parents is asymptotically Poisson with mean \(t^4/8\). A union bound shows that all competing routes to overflow have probability \(O_t(b^{-1/4})\); each exceptional parent contributes one car to the root, which absorbs one, leaving \((Z-1)_+\). Monotone coupling with concentrated Poisson car totals proves the fixed-count limit and the two threshold directions. Finite checks validate the recursion, not the infinite limit.

## Originality — PASS, with historical-priority limitations

Prior results cover generic parking functions on rooted trees, extremal trees, and random Cayley or Galton–Watson tree parking transitions. The closest model sources are Bruner–Panholzer (2015), Contat–Curien (2021), Aldous–Contat–Curien–Hénard (2022), and Contat (2023). Their stated theorems concern general characterizations, different tree ensembles, or fixed branching degree. The explicit deterministic height-two high-degree scale \(m\asymp b^{5/4}\) and the shifted-Poisson law for the **number** exiting are not direct special cases of their conclusions. The known local flux recursion and the Poisson rare-event theorem are credited. Historical priority beyond the inspected sources has not been independently certified.

## Value — PASS

The result identifies an actual first-failure threshold in a canonical bounded-depth hierarchy where car density tends to zero. It explains the nontrivial \(5/8\) load exponent via a two-level collision cascade and gives the full escape-count distribution, not merely a mean or one probability. It is a benchmark for parking bottlenecks in high-degree hierarchical networks and illustrates a sharp mechanism distinct from positive-density transitions on random trees.

## Scope and limitations

Only deterministic balanced height-two trees, uniform independent preferences and one-space upward parking are treated. A fixed-count rate of convergence is not claimed. A broader historical-priority search and independent mathematical review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
