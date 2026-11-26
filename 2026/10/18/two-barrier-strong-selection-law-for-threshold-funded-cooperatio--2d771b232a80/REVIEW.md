# Independent mathematical audit

## correctness

PASS

I independently checked the asymptotic by renewal at t on the embedded jump chain. Each visit to j costs θj/u_j in expected update expense when funded, with u_j=j(N−j)/N². Write ε=exp(−β(θ−d)), δ=exp(−βd), and m=N−1−t. A cycle from t ends at the next return to t or absorption. One-dimensional gambler's ruin on each side gives its exact escape probability [ε^t/(∑_{k=0}^{t−1}ε^k)+δ^m/(∑_{k=0}^{m}δ^k)]/(1+ε). The factor ε from the first downward jump at t is essential. The cycle's expected cost is θt/u_t times 1+O(ε): the right excursion pays nothing and the left excursion starts with probability O(ε) and has bounded expected length for fixed N, since a fixed block of up-steps has probability bounded below. Renewal therefore gives E_t=(θt/u_t)/(ε^t+δ^m) times 1+O(ε+δ), uniformly on the asserted compact sets. From any other mixed state the chance of absorbing before t is O(ε+δ) by the same ruin calculation; the expected pre-hit cost is bounded, hence also a relative O(ε+δ). This yields the claimed prefactor, minimum barrier exponent, half coefficient at equality, and logistic limit by setting β(A−B)=s. In the finite regimes the limiting embedded transient chain is still absorbing, so its inverse and occupations are continuous. Below d every step goes down; for full funding above d every step goes up. At equality the funded segment is unbiased, absorbing at zero and reflecting at t once the unrewarded t→t+1→t excursion is collapsed. Its visit Green function at funded j is 2min(i,j), by the discrete second-difference equation with reflecting condition at t (initial i>t first reaches t). Multiplying by θj/u_j gives all three finite formulas. The frozen scale-kernel normalization agrees with these independent checks.

## originality

PASS

The distinctive claim is the all-partial-cutoff, all-transient-start, compact-uniform sharp law including its discrete-update prefactor and logistic competition window. The same model, fundamental matrix, cutoff-one divergence, some finite regimes, and finite-beta cutoff-two cost formulas already exist and are not credited as new. The predecessor comparison should acknowledge its explicit cutoff-two cost formulas, not merely inverse-matrix entries.

## value

PASS

The result explains which absorbing exit limits expense and determines the scale and leading coefficient even at equality of the two barriers. A single uniform law captures the width and shape of the changeover; this cannot be read off from the qualitative divergence or from separately taking fixed-incentive limits. Its normalization is useful for the stated discrete institutional cost, and the discontinuous change from finite to exponential cost on omitting the final state is an informative contrast within the model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
