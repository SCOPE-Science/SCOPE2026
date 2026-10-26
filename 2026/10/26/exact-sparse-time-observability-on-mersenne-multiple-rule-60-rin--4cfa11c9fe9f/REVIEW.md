# Scientific review: sparse-time Rule 60 observability

## Correctness — PASS
The theorem's domain is \(r\ge2\), \(a\ge0\), \(q\ge1\), with a binary cyclic Rule 60 update and one stationary observed coordinate. Observation rows identify with powers of \(H=(1+X)^q\) in the cyclic group algebra; their rank is the degree of the minimal polynomial because the cyclic vector is the unit. Over \(\mathbb F_{2^r}\), the ring factorization has \(2^r-1\) roots, each with multiplicity \(2^a\). The root \(1\) yields nilpotence index \(\lceil2^a/q\rceil\); all other roots have nilpotence index \(2^{\max(a-v_2(q),0)}\), with eigenvalue collisions counted by the odd-part gcd. The least-common-multiple calculation produces the claimed formula and proves the first-observation independence. A separate exhaustive/rand-seeded Boolean rank checker agreed on 744 parameter cases. Finite tests are corroborative and not the basis of the all-parameter proof.

## Originality — PASS under inspected evidence
The classical additive-automaton paper of Martin–Odlyzko–Wolfram develops the polynomial treatment of dynamics but not the evaluated one-site, stride-\(q\) observation rank. El Yacoubi et al. (2021) supply a general affine observability-rank criterion, not this closed gcd-and-Jordan classification. Elser (2021) has the distinct problem of recovering unknown rules from full-state snapshots. The finite-volume affine clock-factor and two-frame shift-sensor research records concern different observation objects and do not imply this formula. A 2022 article on bounded CA observation and a 2022 paper on RNG reconstruction were available at abstract level only, so earlier equivalent treatment in their full texts is a residual priority risk. The searches have not established worldwide uniqueness.

## Mathematical value — PASS
Sparse observation of a known linear dynamical system asks an identifiable and natural question: how many initial-state bits can a single fixed instrument recover at an imposed clock rate? The theorem solves this exactly over infinitely many growing ring sizes and sampling intervals, exposes a prime-to-two spectral collision law, separates the singular zero mode, and proves the sharp even-ring impossibility for any omitted time step. The infinite-family closed result is nontrivial beyond running the standard Kalman matrix-rank test for individual instances, and it determines information loss exactly. Scope does not include noisy recovery or arbitrary ring lengths.

## Limits
The mathematical result is proved for a specific infinite family, not every ring length. Some relevant 2022 full texts remained unavailable, and no independent historical-priority validation has occurred.

Self-review: passed. Independent audit: not yet performed.
