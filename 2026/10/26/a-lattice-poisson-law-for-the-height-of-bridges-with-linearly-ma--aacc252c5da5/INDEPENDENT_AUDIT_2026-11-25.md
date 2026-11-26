# Independent mathematical audit

## correctness

PASS

Return count includes the terminal return and height is absolute; under the conditioning bridges with exactly k excursions are equiprobable. Each signed primitive excursion is a reflected or positive primitive Dyck path; removing the initial and terminal steps gives the factors 2zC and 2zC_{h−2} for all excursions and height <h respectively. The common sign/length factors cancel in the probability, and Lagrange inversion for C=1+zC² gives the stated coefficient including n=k. For the tilt, writing q=√(1−4z), λ=(1−q)/(1+q), the restricted Catalan continued fraction has cross-ratio multiplier λ and initial cross-ratio λ² at C_0=1. Thus E−E_{<h}=2qλ^h/(1−λ^h). With ρ_n=k_n/n, the matching tilt has q=ρ_n/(2−ρ_n), λ=1−ρ_n, mean (1+q)/(2q)=n/k_n, and variance z/q³=(1−ρ_n)(2−ρ_n)/ρ_n³. Hence k_n p_n converges to ρτ/(1−ρ). The PGF is the independent tilted PGF (1−(1−s)p_n)^k times a ratio of conditioning probabilities. Weighting tall excursions by s∈[0,1] changes the per-length mean and variance by O(hλ^h), O(h²λ^h) from differentiation of the exact tail on a compact interior tilt range. Both reweighted and full laws have bounded exponential moments and probabilities uniformly bounded below at lengths 1 and 2 when h≥3. In Fourier inversion the latter bounds imply |φ(t)|²≤1−c(1−cos t) on [−π,π]; the uniform third moments give the Gaussian expansion at t=O(k^(−1/2)). The mean shift o(√k) makes both local probabilities asymptotic to 1/√(2πkσ_ρ²). In the window, k hλ^h=O(log k) even for much larger h; hence the ratio tends to 1 and the Poisson PGF, including s=0, follows. For the logarithmic lower bound, h=(1−δ)log k/(−log λ)+O(1) with 0<δ<1/2 still gives mean shift O(k^δ log k)=o(√k), but k p_n diverges; the upper bound uses 1+δ and k p_n→0. Rounding preserves these bounds. This establishes the interior-density claim and τ=0 as well, without a continuous Gumbel limit. Independent replay at /workspace/reproductions/1/independent_check.py corroborates the exact counts and tilt with 326 exact checks (exhaustive bridges through semilength 8, plus rational tail/tilt checks), not the limit. The furnished VERIFICATION.md and verify.py were inspected, not executed.

## originality

PASS

Finite Catalan enumeration and standard conditioning tools are ingredients, not the claimed novelty. The closest bridge comparison has endpoint conditioning only; composition and pinning results inspected concerning largest part or interreturn gap do not transfer to heights without the internal path mark. The bounded prior comparison did not establish coverage of the conditional lattice Poisson law or its prefactor.

## value

PASS

A fixed positive density of returns changes the simple-bridge maximum scale from √n to log n. The height-specific Poisson count, lattice-window prefactor and explicit height constant distinguish this conditional ensemble more sharply than a bound on the longest excursion time. The result gives an exact boundary for a natural conditioned model and does not overstate the interior-density range or claim a continuous Gumbel law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
