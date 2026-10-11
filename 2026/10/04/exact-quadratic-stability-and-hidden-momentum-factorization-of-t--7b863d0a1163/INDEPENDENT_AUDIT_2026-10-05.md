# Independent mathematical audit

## correctness

PASS

The 2018 paper's actual recurrence uses one momentum state and an exponentially averaged gradient-difference state. Restricting an SPD quadratic to one eigenmode yields a four-state linear recurrence. A fresh independent symbolic determinant gives exactly the submitted factorization into a zero root, the passive \(\beta\) root, and a quadratic with product \(q_\lambda\). The second-order Jury conditions reduce to \(q_\lambda<1\) and \(0<\eta\lambda<2(1+q_\lambda)\). Over a spectral interval the endpoint \(L\) is decisive. The quadratic's smallest possible spectral radius is \(\sqrt{q_\lambda}\), attained throughout the complex-root interval; since \(q_\lambda\) increases with derivative gain, the stability/rate tradeoff follows.

## originality

PASS

The complete 2018 primary paper was read after open full-text retrieval failed: it introduces the exact recurrence, discusses overshoot, Laplace heuristics and experiments, but gives no SPD-quadratic Schur boundary or exact modal rate. The 2020 follow-up/rethinking paper is centered on suppressing derivative-term noise and stabilizing training; its accessible primary abstract likewise does not state this exact factorization or stability theorem. Targeted Resultary searches found related optimization stability records but no same-algorithm quadratic classification.

## value

PASS

The derivative state is the defining departure from momentum in the source optimizer. The exact factorization separates passive memory from the active quadratic mode and quantifies a non-obvious design tradeoff: larger derivative gain widens stable steps while raising the best modal contraction floor. This is a motivated structural analysis of a published optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
