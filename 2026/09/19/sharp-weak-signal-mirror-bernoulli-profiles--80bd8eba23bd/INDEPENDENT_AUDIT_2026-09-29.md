# Independent audit — Sharp weak-signal profiles for mirror Bernoulli products

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/sharp-weak-signal-mirror-bernoulli-profiles--80bd8eba23bd`  
**Audited tree:** `144f8fcc815625e51b8c0ea1852eb6fae2f3ddb5`

## Disposition

**PASSED.**

## Correctness

**PASS.** The mirror-product expansion is correct. Expanding the difference of the two product laws leaves exactly the odd Walsh levels; the linear level is the normalized Rademacher sum and the remaining odd levels have L2 mass O(q^{3/2}), while Delta is sqrt(q)(1+O(q)). This gives the stated O(q) normalized error. The triangular-array limit follows from separating macroscopic coefficients and applying Lindeberg to the diffuse tail, and the sharp scalar range [1/sqrt(2),1] is exactly the p=1 Khintchine range. The Bernoulli corollary correctly identifies the local midpoint contrasts and, under max a_i^2/V -> 0, gives the Gaussian constants sqrt(V/pi) and sqrt(2V/pi).

## Originality

**PASS.** Smirnov arXiv:2609.19222 proves universal constant-factor control and introduces the mirror-product states, but its inspected theorem only lower-bounds mirror distinguishability up to an absolute constant and does not state the weak-signal Rademacher-profile limit, the complete subsequential profile classification, or the diffuse sqrt(2/pi) constant. The earlier SCOPE rare-event Bernoulli record concerns vanishing total intensities and signed mass cancellation, a different regime and mechanism. Searches located no prior theorem matching this local mirror-profile classification.

## Scientific value

**PASS.** The result turns a constant-factor comparison into a sharp local asymptotic theory, identifies all possible weak-signal constants rather than a single bound, and yields an exact sqrt(2) gain for the doubled Bernoulli experiment in the diffuse regime. Those are meaningful quantitative refinements of the new Bernoulli-product TV framework.

## Independent checks

- Re-expanded R_a^+ - R_a^- and verified that only odd Walsh monomials survive, with the linear term sum_i a_i eps_i.
- Re-derived Delta^2=1-prod_i(1-a_i^2), hence q(1-q/2)<=Delta^2<=q for q<=1/2.
- Numerically enumerated all 2^m states for hundreds of random vectors with m<=6 and q<=1/2; every case satisfied the stated |tau/Delta-E|sum w_i eps_i|| <= 2q bound.
- Checked that coordinatewise convergence of sorted weights plus Lindeberg on the residual tail gives the claimed Rademacher-plus-Gaussian profile, and that the p=1 Khintchine extremizers give endpoints 1/sqrt(2) and 1.
- Inspected Smirnov's current arXiv HTML at Theorem 4.1 and the CNOT decomposition: it supplies only an absolute-constant mirror lower bound, not the record's local asymptotic constants.

## Evidence and literature

- https://arxiv.org/abs/2609.19222 — Smirnov, TV between Bernoulli products, up to constants; inspected current main theorem, CNOT decomposition, mirror states, and Theorem 4.1.
- https://arxiv.org/abs/2602.21828 — Avital–Kontorovich–Salafatinos, small-parameter Bernoulli-product TV; relevant neighboring asymptotic regime but not the mirror weak-signal profile theorem.
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/rare-bernoulli-tv-sign-cancellation--adcb7befe3ff — Earlier SCOPE rare-event sign-cancellation result; mathematically distinct small-total-intensity regime.

## Limitations

- The weak-signal theorem is local: q=sum a_i^2 must tend to zero; no global optimal comparison constant is established.
- The diffuse Bernoulli corollary needs both V->0 and max_i a_i^2/V->0.
- The underlying Smirnov paper is very recent, so contemporaneous unindexed follow-up work remains a residual originality risk.

## Repository identity

The assigned source-tree SHA `144f8fcc815625e51b8c0ea1852eb6fae2f3ddb5` exactly matched the current tree at the audited path on `main`; GitHub was read only during this audit.
