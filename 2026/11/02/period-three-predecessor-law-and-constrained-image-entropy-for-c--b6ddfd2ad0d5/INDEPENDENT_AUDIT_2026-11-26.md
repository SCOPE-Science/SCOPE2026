# Independent mathematical audit

## correctness

PASS

The exactly-one neighborhoods yield the three-cycle 00→01→10→00 of 1-edges. Immediately before an isolated zero only 00 and 10 can both follow a 1 and start a 0-edge that permits the next 1. Following that 0-edge and the next a steps of the three-cycle gives the stated two-state partial permutations. Closed walks represent same-length indexed inputs, including n=1,2 with repeated neighbors. A projector forces at most one fixed start; a pure product of swaps fixes both states precisely at even gap count. All-ones has the three cyclic starts exactly when 3 divides n. The determinant of I-U has factors (1+z)(1-z-z^3)/(1-z^3); counting marked zeros gives n/m, even for words with smaller least period. At n=3k the duplicate contribution is Σ_{m≥2 even}(3k/m)binom(k-1,m-1)=3(2^(k-1)-1), confirming the subtraction and rational OGF independently of its log expression. The recurrence t_n is the sum of nth powers of the three roots of x^3-x^2-1 by Vieta; the conjugate pair has modulus λ^(-1/2), so the error bound and unit leading coefficient follow. All cyclic 00-avoiding words have count φ^n+(-φ^(-1))^n by the two-state adjacency trace, which gives the stated rate. No proof for unrestricted outputs is inferred.

## originality

PASS

Qualified to the same-length isolated-zero fiber law and exact distinct indexed image census, including its duplicate correction. Neither the Rule-22 de Bruijn graph, period-three behavior in previous preimage problems, the auxiliary recurrence, nor λ in isolation is credited as new.

## value

PASS

The shortest forbidden-word constraint on zeros is natural and isolates a structured high-density target class in a canonical rule. An exact same-ring existence test becomes a complete fiber size law; it distinguishes when counting paths overcounts targets, and the exact image census quantifies the loss of reachable configurations at every length. The value lies in this joint characterization and the distinct count, not in recomputing a spectral radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
