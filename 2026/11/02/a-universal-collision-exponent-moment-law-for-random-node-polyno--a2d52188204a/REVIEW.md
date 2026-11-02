# Self-review

## Correctness — PASS

For all fixed \(n\ge2\), \(\theta\ge0\), and \(q>0\), upper integrability follows after discarding bounded Vandermonde factors and integrating \(|u-v|^{\theta-q}\). Lower divergence uses a positive-volume two-node collision while every other separation stays bounded below. This proves both directions and includes the endpoint \(q=\theta+1\); a finite sampling experiment has not been substituted for either step. The two-node distribution is derived by the exact midpoint/gap Jacobian, and its moments follow by integrating its survival function. Fixed-point Gaussian-noise moments follow from the conditional Gaussian variance and a uniformly bounded Newton interpolant for \(f\in C^{n-1}\). The independent checker tests exact formulas and stochastic samples but is not itself the infinite-quantifier certificate.

## Originality — PASS, qualified

Relevant inspected primary sources include Belhadji–Bardenet–Chainais 2023 (arXiv:2310.09437, deterministic and DPP signal reconstruction estimates and \(L^2\) guarantees), Chkifa–Dolbeault 2023 (arXiv:2306.07435, different randomized sampling/interpolation scheme and robustness estimates), Belhadji–Bardenet–Chainais 2020 (arXiv:2002.09677, kernel interpolation and volume sampling), and Jantsch–Webster–Zhang 2016 (arXiv:1606.07093, deterministic Leja Lebesgue bounds). Established ingredients include the Lagrange interpolation formula and the Vandermonde density. Comparisons concern the *random operator-norm moment spectrum*, *all finite node counts*, *two-node exact distribution* and *unconditional fixed-point Gaussian-noise moments*, not similarity of paper titles. None of the inspected material or queried published mathematical records directly covers this combination. Broader specialized random-matrix inverse-moment or stochastic interpolation work may exist beyond the inspected set; independent priority verification remains necessary.

## Value — PASS

Mean-square stability of a noisy full interpolant is mathematically different from pointwise exactness or noiseless reconstruction. The sharp collision-exponent frontier separates infinite and finite unconditional quadratic amplification, placing iid nodes and polynomial projection DPP nodes on opposite sides and doing so independently of node count. The exact two-node tail provides a reproducible calibration distribution. The kernel-volume-sampling reference explicitly motivates further study of Lebesgue constants under repulsive sampling. These are natural sampling-design invariants rather than arbitrary numerical slices. Constant size in \(n\), floating-point stability and practical sampling cost are not addressed.

Self-review: passed. Independent audit: not yet performed.
