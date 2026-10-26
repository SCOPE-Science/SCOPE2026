# Self-review

## Correctness
PASS. The proof identifies the dual update with multiplication by \(W=X+Y\) in a finite group algebra. Because the long side is a power of two, the change of variables gives a free \(s\)-generator module over \(\mathbb F_2[W]/(W^L)\). The sensor matrix is invertible precisely when reductions of its site monomials hit every diagonal class. The counts use direct inclusion-exclusion, and the Poisson threshold follows from fixed-order factorial moments with a stated uniform error bound for \(L\ge s\). The verifier corroborates small cases only; no numerical test is mistaken for an all-size proof.

## Originality
PASS under the inspected literature, not a claim of independently established historical priority. The one-dimensional additive-CA orbit analyses in Tadaki (1993), general finite-field observability theory in Sundaram–Hadjicostis (2013), and affine-CA Kalman criterion in El Yacoubi et al. (2021) do not provide the explicit two-dimensional residue-class sensor rule or its complete exact sensor-set census in the inspected text. Similar sensor and reconstruction research exists: the full 2022 Plénet et al. article and 1997 Khan et al. matrix-algebra article were not inspected. Their possible specific overlaps remain residual risks. The general rank test itself is credited to prior work.

## Mathematical value
PASS. The all-zero eventual state of this linear automaton conceals every starting configuration; the result determines exactly when a fixed set of time traces nevertheless recovers the lost information. The answer is a transparent geometric characterization for every size and every placement, with a sharp minimal sensor count, an exact budget-dependent enumeration and a coupon-collector transition for random placements. The all-placement criterion rather than a narrow numerical example is the main structural contribution.

## Scope and open risks
The theorem covers only synchronous north-east XOR on dyadic rectangular periodic grids, noiseless static sensors and full pre-extinction time observations. No claim is made about other boundary conditions or update rules. The inaccessible plausible papers and unindexed literature must be examined before asserting independent historical priority.

Self-review: passed. Independent audit: not yet performed.
