# Scientific review

## Correctness — PASS

The claim is for fixed convex Euclidean polygons and finite boundary sets hitting every open side. The polygon dissects exactly into the inscribed hull and disjoint corner triangles. Writing chord shortening as \(u_i\) and triangle area as \(v_i\), the exact local ratio satisfies \(v_i/u_i^2\ge\kappa_i\) because the normalized chord length is at least \(\sin(\theta_i/2)\). Weighted Cauchy then gives the claimed global optimum. The nonnegative slack decomposition is verified algebraically, and a common positive scale constructs genuine equality cases with all constraints satisfied. Finite independent hull computations passed 1,800 tests and three sharpness configurations; they are corroboration rather than infinite proof.

## Originality — PASS, subject to residual bibliographic uncertainty

Primary full-text comparisons covered Reitzner–Schütt–Werner (2019), Prochno–Schütt–Sonnleitner–Werner (2024), and Indrei (2015). The first two investigate boundary-random means or Hausdorff approximation; Indrei treats the isoperimetric deficit of one polygon and its regularity. None of their examined theorems implies the best possible nested loss comparison for every side-spanning inner hull with complete equality and stability. The elementary corner geometry is preexisting background; the claimed contribution is its sharp global angular optimization. Database queries for corner truncation, paired deficits, and nested-polygon Bonnesen inequalities did not identify coverage, which does not eliminate the possibility of unindexed equivalent results. The classical long boundary-random chapter was inspected selectively.

## Mathematical value — PASS

The precise invariant is the optimal ratio of removed area to squared removed perimeter for a prescribed outer polygon. It is motivated by deterministic and boundary-sampling convex approximation, nonzero, explicitly angular, and attained. The exact stability identity separates two genuinely geometric mechanisms of inefficiency and classifies all nontrivial equality configurations; these are structural and sharp properties beyond individual asymptotic marginal observations.

## Limitations

The theorem is restricted to side-spanning boundary-inscribed polygonal hulls; empty sides and arbitrary interior sampling fall outside the proof. No uniform positive constant over all possible angle patterns is claimed. Additional historical literature could contain the same optimization. Independent mathematical audit has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
