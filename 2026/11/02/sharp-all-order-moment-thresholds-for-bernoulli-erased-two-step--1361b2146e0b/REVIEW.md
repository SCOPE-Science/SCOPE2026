# Scientific review: sharp all-order erasure-moment thresholds

## Correctness — PASS

The theorem is quantified for every real \(p>0\), every \(0<q<1\), every real two-dimensional pair \(D,N\) with \(D^2=N^2=0\), \(N\ne0\), and \(\operatorname{tr}(ND)\ne0\), and every nonzero deterministic initial state. The key algebra \(NA^kN=k\gamma N\), where \(A=I+D\), follows from \(A^k=I+kD\). The exact series defining \(V_p\) converges uniformly on bounded sets for the uniquely determined rate \(\lambda_p>q\). The nondegenerate rows \(\ell^{\mathsf T}\) and \(\ell^{\mathsf T}D\) establish positive definiteness in the homogeneous sense, giving two-sided equivalence to \(\|x\|^p\), including fractional powers. The one-step identity \(qV_p(Ax)+(1-q)V_p(Nx)=\lambda_pV_p(x)\) then yields exact expectations and two-sided moment-rate bounds with constants uniform in both time and initial direction. The geometric erasure count proves the unique threshold, and adjacent-success pairs imply finite-time absorption almost surely. The canonical matrix computation correctly gives the first- and second-moment thresholds \(1/2\) and \(1/3\), plus an exactly conserved quadratic form at the latter boundary.

The standalone verifier was executed from the actual new package sources. It returned `VERIFY_OK checks= 1165`, covering exact rational critical-moment conservation, matrix identities, noninteger-moment eigenfunction tests, finite mode trees and nonunit coupling. The finite checks corroborate, but do not establish, the infinite-time claim; the constructive proof above supplies that step.

## Originality — PASS, qualified

The closest primary works address networked control under random delays and packet drops, second-moment small-gain criteria, or first-/second-order moment recurrences. In the inspected relevant mathematical material of Su–Li–Lu (arXiv:2108.12795v1), Lu–Li–Su (arXiv:2204.13083), Sykora et al. (DOI:10.1002/rnc.5218), and Li–Lu–Su (arXiv:2402.04074), no direct all-real-moment identity for this nilpotent/unipotent two-mode family or the explicit first-versus-second-moment erasure window was located. The generic second-moment results may imply a criterion for this particular example after substantial specialization; that general concept is not claimed as new. The main distinguishing fact is one constructive homogeneous eigen-energy for each arbitrary positive real moment order, with the exact root and sharp phase diagram. Search records for Bernoulli sparsification, randomized Gauss–Seidel and mean-square stability concern different state updates and do not dominate this claim.

**Residual risk:** The full technical text of Xu–Zhang–Gu–Tang, DOI:10.1137/22M1496062, was unavailable from lawful access routes; publisher and author-repository abstracts were reviewed. An unrecognized prior specialization or a general random-matrix result could reduce the novelty. A search without a match does not establish publication priority, and no independent audit has occurred.

## Value — PASS

The exact thresholds determine whether networked deadbeat control can have exploding expected error while trajectories physically reach zero in finite time almost surely. Unlike a numerical example, the result covers a similarity-invariant two-mode class and **every positive real moment order**, including orders not governed by polynomial covariance recurrences. The explicit \(1/3<q<1/2\) interval separates decaying mean error from growing mean-square error, a testable boundary for channel reliability and risk-sensitive control design. The exact homogeneous eigen-energy also provides a mathematical diagnostic that is stronger than checking a finite collection of simulations or moments. This motivated classification is not a routine normalization of a familiar zero/one stability test.

## Limits of this review

The result assumes independent Bernoulli dropouts, zero applied control on erasure, no exogenous noise, two-dimensional state and nilpotent successful update. It does not claim optimal control synthesis, universal networking robustness, or a general higher-dimensional classification. Source coverage is not exhaustive and third-party full technical access was limited for one relevant article. Numerical checks establish only their stated finite cases; the proof is an analytic argument. No independent scientific validation or external certification is claimed.

Self-review: passed. Independent audit: not yet performed.
