# Review of the random power-domination crossover on rook graphs

## Correctness — PASS

The deterministic reduction is exact: following the closed-neighborhood step the only unobserved cells form the product of the unoccupied rows and columns. A one-row or one-column residue can be forced; a residue with at least two rows and two columns is permanently stuck because no observed vertex has exactly one unobserved neighbor. This proves the criterion for every board with both dimensions at least two.

The finite generating polynomial follows by union counting and two-dimensional inclusion-exclusion. For every pair of nonnegative integers \(r,s\), the Bernoulli joint falling-factorial moment is exactly \((m)_r(n)_s(1-p)^{nr+ms-rs}\); replacing avoidance probability by \(\binom{mn-nr-ms+rs}{t}/\binom{mn}{t}\) gives the fixed-budget version. Standard factorial-moment convergence proves asymptotic independence for finite crossover parameter. For an infinite parameter, divergence and binomial concentration handle Bernoulli rows, while negative correlation and Chebyshev's inequality handle fixed-budget rows. The Poisson column marginal completes both cases. The argument covers all quantified sequences and boundary regimes, and never uses finite experiments as an infinite proof.

Standalone exhaustive propagation checks on eight board sizes agree with every finite criterion and coefficient, and independently verified exact mixed moments agree in the rectangular test case. The script's expected final line is `ALL_VERIFY_OK`.

## Originality — PASS with specified uncertainty

Closest direct known work: Soh and Koh, *A Note on Power Domination Problem in Diameter Two Graphs* (2014), states the minimum cardinality for Cartesian products of complete graphs. It does not follow from that scalar number alone that the **random** independent-sensor and uniform-fixed-size threshold has a two-Poisson crossover at \((m-n)\log n/n\), nor that the entire finite sensor-set enumerator has the given inclusion-exclusion expression. Its full original text was inaccessible, so any broader statements therein remain a concrete risk.

Dorbec et al., *Power Domination in Product Graphs* (2008), studies other graph products; its accessible abstract does not announce stochastic reliability on rook graphs, and the publisher full text was not accessed. Benson et al., arXiv:1510.02421 (2015), treats product-graph zero forcing and lower bounds; its accessible full text does not cover the stated occupancy-limit theorem. Brimkov et al., arXiv:1805.10984 (2018), introduces the general power-domination polynomial and examines other specific families; that general definition by itself does not imply the rook-graph closed form or the critical crossover. The ordinary coupon-collector Poisson law supplies a proof ingredient, but its use does not by itself specify the two-channel union or the near-square geometry; the exact row/column reduction is necessary.

Related studies of power domination under sensor failure concern other graph classes or conditioned sensor models; those do not directly imply this random all-cells law. The searches and accessible comparisons found no dominating published theorem, exact lookup table, or equivalent formulation. This is evidence of originality under accessible literature, **not** a proof that an unindexed earlier result does not exist. See the limitations in `RESULT.md`.

## Value — PASS

The problem asks for full observation under random PMU placement in a basic diameter-two graph family. Optimal deterministic placement uses only \(\min(m,n)-1\) sensors, whereas independent or uniformly random placement requires a budget at scale \(n\log n\) for nondegenerate success probability. More importantly, the shape of the board determines whether *both* row and column coverage mechanisms survive in the limit. The row-excess scale \(n/\log n\) yields a sharp, continuous two-channel-to-one-channel transition, with exact finite reliability accessible from one polynomial. This is a motivated sensitivity question with a parameter-dependent answer, rather than a relabeling of the scalar optimization result.

## Limitations and provenance

Primary literature was compared by mathematical content rather than title matches, but a relevant 2014 article could not be read in its entirety. Earlier unindexed random-observation formulations may exist. Computational checks are finite; the proof makes no claim about random edge failures, adversarial placement, or independent external certification.

Self-review: passed. Independent audit: not yet performed.
