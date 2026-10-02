# Independent audit — 2026-10-01

## Final claim

For SPD spectra in \([\mu,L]\), the optimal two individually Euclidean-nonexpansive Richardson stages have the stated exact phase transition at \(\kappa=1+\sqrt2\), and requiring every first-order factor to be nonexpansive forces \(\Theta(\kappa\log(1/\varepsilon))\) rather than Chebyshev-order acceleration.

## Correctness — PASS

Normalization reduces the two-stage problem to minimizing \(\sup_{x\in[a,1]}|(1-ux)(1-vx)|\) over \(u,v\in[0,2]\). The shifted degree-two Chebyshev roots are feasible exactly when \(a\ge\sqrt2-1\), equivalently \(\kappa\le1+\sqrt2\). In the complementary branch the endpoint lower bound is attained uniquely by \(u=2\) and \(v=2/(1+2a)\), and its interior extremum stays below the endpoint level precisely on that branch. The general \(m\)-stage lower bound follows already at \(\lambda=\mu\). An independent dense-grid replay at six representative condition numbers reproduced both closed-form branches and the transition; the finite replay corroborates the exact minimax proof.

Checked sources:
- Assigned package RESULT.md and deterministic verifier at the assigned Git snapshot.
- G. H. Golub, R. S. Varga, Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods, Parts I and II, Numerische Mathematik 3 (1961); both primary papers inspected in full from the author archive.
- O. Axelsson, Milestones in the Development of Iterative Solution Methods (2010), historical discussion of factorized Chebyshev stages.
- T. A. Manteuffel, Optimal Parameters for Linear Second-Degree Stationary Iterative Methods (1982).
- Published-record semantic search for stagewise nonexpansive Richardson/Chebyshev frontiers.

Residual risks:
- None.

## Originality — PASS

Best-of-knowledge originality passes. The full Golub--Varga Parts I and II develop unrestricted Chebyshev semi-iteration, cyclic variants, and spectral-norm comparisons, but do not impose or solve the interval-uniform constraint that every first-order Richardson factor itself be a Euclidean nonexpansion. The published-record search returned no earlier exact \(1+\sqrt2\) transition, unique boundary pair, or all-stage \(\Theta(\kappa)\) barrier under this constraint.

### Equivalent formulations

Searches:
- Published-record semantic query: stagewise safe Richardson Chebyshev nonexpansive factors condition number transition
- Full inspection of Golub--Varga Parts I and II

Evidence:
- No earlier published record with the exact constrained minimax frontier was located.
- The classical papers optimize Chebyshev/semi-iterative methods and compare spectral norms, but the factorwise \(0\le\tau_i\le2/L\) constraint is absent.

Reasoning: Equivalent formulations include constrained root-location minimax, per-factor nonexpansive gradient/Richardson schedules, and a no-square-root-acceleration theorem under factorwise safety.

### Broader coverage

Searches:
- Golub--Varga Parts I and II
- Manteuffel 1982
- Axelsson 2010

Evidence:
- The classical work is broader on Chebyshev acceleration but does not solve the imposed safety-constrained minimax problem.
- Stationary second-degree recurrence optimization and implementation-stability discussions use different admissible classes.

Reasoning: No inspected stronger theorem mechanically implies the exact two-stage frontier or unique optimizer.

### Exact database or table

Searches:
- Exact threshold and optimizer searches
- Assigned deterministic verifier

Evidence:
- No independent prior parameter table or formula containing \(\kappa_\star=1+\sqrt2\) with the safe pair was located.
- The package's numerical samples agree with the theorem but are not used as novelty evidence.

Reasoning: The claim is an analytic minimax theorem, not a finite-table inference.

### Claim versus prior implication

Searches:
- Classical Chebyshev minimax polynomial versus the safe constraint

Evidence:
- The classical degree-two minimax polynomial supplies the unconstrained branch only.
- The constrained branch requires a new endpoint lower bound and equality analysis; the general \(m\)-stage barrier uses the smallest spectral point under the factorwise constraint.

Reasoning: The final claim is not a corollary of unrestricted Chebyshev optimality because feasibility changes sharply at the stated threshold.

### Source inspections

- **Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods, Part I** — Covers unrestricted Chebyshev semi-iteration but not the factorwise nonexpansive minimax frontier. Material read: Complete primary paper. Method: Primary full-text inspection. Evidence: The paper derives Chebyshev semi-iterative polynomials and spectral convergence without the per-factor safety box.
- **Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods, Part II** — Does not contain the assigned interval-uniform per-stage nonexpansiveness problem or threshold. Material read: Complete 12-page primary paper. Method: Primary rendered-page inspection. Evidence: It treats cyclic Chebyshev methods, spectral-norm comparisons, applications, and numerical experiments.

Checked sources:
- Assigned package RESULT.md and deterministic verifier at the assigned Git snapshot.
- G. H. Golub, R. S. Varga, Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods, Parts I and II, Numerische Mathematik 3 (1961); both primary papers inspected in full from the author archive.
- O. Axelsson, Milestones in the Development of Iterative Solution Methods (2010), historical discussion of factorized Chebyshev stages.
- T. A. Manteuffel, Optimal Parameters for Linear Second-Degree Stationary Iterative Methods (1982).
- Published-record semantic search for stagewise nonexpansive Richardson/Chebyshev frontiers.

Residual risks:
- The theorem uses a deliberately strong factorwise Euclidean nonexpansiveness notion; it is not a floating-point stability theorem or a statement about stable three-term Chebyshev recurrences.

## Scientific value — PASS

The theorem gives a sharp, interpretable tradeoff between a natural factorwise safety requirement and acceleration: it identifies the exact two-step phase transition, the unique constrained optimizer beyond it, and proves that enforcing the same local safety at every stage destroys Chebyshev-order acceleration. This is a motivated structural boundary, not a routine restatement of classical Chebyshev theory.

Checked sources:
- Assigned package RESULT.md and deterministic verifier at the assigned Git snapshot.
- G. H. Golub, R. S. Varga, Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods, Parts I and II, Numerische Mathematik 3 (1961); both primary papers inspected in full from the author archive.
- O. Axelsson, Milestones in the Development of Iterative Solution Methods (2010), historical discussion of factorized Chebyshev stages.
- T. A. Manteuffel, Optimal Parameters for Linear Second-Degree Stationary Iterative Methods (1982).
- Published-record semantic search for stagewise nonexpansive Richardson/Chebyshev frontiers.

Residual risks:
- The theorem uses a deliberately strong factorwise Euclidean nonexpansiveness notion; it is not a floating-point stability theorem or a statement about stable three-term Chebyshev recurrences.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
