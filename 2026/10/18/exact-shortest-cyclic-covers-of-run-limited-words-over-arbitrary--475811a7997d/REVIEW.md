# Independent mathematical audit

## correctness

PASS

PASS: For q,r≥2 and n≥r let vertices be legal length n−1 words and edges legal length n factors avoiding linear a^r. The overlap graph is strongly connected via a non-a letter. Its imbalance is indicator(initial a^{r−1}) minus indicator(final a^{r−1}); sources are terminal-but-not-initial, sinks initial-but-not-terminal. The integer potential φ=leftmost start of a^{r−1}, or sentinel if absent, drops by ≤1 on each legal edge, so balancing extra edges needs at least Σ_sources φ. The explicit path s=P Q→Q reverse(P) from first a^{r−1} to a sink is legal, length φ, and the inverse based on last a^{r−1} proves a source–sink bijection, so the augmentation attains the lower bound and is Eulerian. The generating function for weighted prefix and remaining suffix multiplies to (q−1)Σ_{i=1}^{r−1} i z^i / [D_{r−1}(z)D_r(z)]. Independent Python enumerated graph imbalances, actual path legality, source–sink bijection, potential costs and generating coefficients for several q=2,3,4,r=2,3 parameter cases, matching binary r=3 excess 0,1,4,9,21,45,93,188. The general theorem relies on combinatorial proof, not finite checks.

## originality

PASS

PASS best of knowledge: Sawada–Gabrić 2025 construct universal cycles for the cyclically restricted per-window language (all cyclic rotations avoid the forbidden run), whereas here the required length-n windows are only LINEARLY a^r-free and the containing cycle must avoid a^r cyclically. The larger linearly legal edge set can be non-Eulerian and requires repeated edges. General shortest Eulerization algorithms (Bernardini et al.) yield methods but not this exact all-q,r symbolic excess rational GF and explicit optimal bijective augmentation. Earlier binary r=2 Fibonacci specialization is already known and not claimed new.

## value

PASS

PASS: exact shortest single-cycle cover of an entire natural constrained language across every alphabet and forbidden-run size is a substantive combinatorial optimization invariant. Explicit optimal path routing, matching integer dual potential and rational multivariate-parameter series go substantially beyond a routine transfer-matrix count of admissible words or generic Eulerization existence; meaningful for sequence-cover algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
