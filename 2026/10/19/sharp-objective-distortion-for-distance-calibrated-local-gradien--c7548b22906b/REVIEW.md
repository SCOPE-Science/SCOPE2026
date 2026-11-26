# Independent mathematical audit

## correctness

PASS

For the replacement files, normalize λ_min=||x||=1 and let m_j be the jth eigenvalue moment under squared-coordinate masses. Direct quadratic expansion gives 1−2θ√m₂/m₁+θ²m₃/(m₁m₂). Since m₁≥1 and m₃≤κm₂, this is bounded by 1+4κ²/(κ+1)²<5 for every finite κ, with κ=1 giving zero. For the repaired spiked family, dp converges in law to a χ²₁ variable by normalized independent Gaussians. Tightness and the absence of an atom at zero give κp→0 and κ²p→∞ in probability because κ≪d≪κ². Thus m₁→1, m₂→∞, m₃/(κm₂)→1, and θ²m₂≤4/κ+4κp→0. The ratio tends to 5 in probability, which gives instances arbitrarily close to 5 at finite κ and proves nonattainment. The exact κ=8 spot check follows from f(T)=22−100s+274s² with s=2√74/45. The prior squared-distance theorem applies to precisely the same step. For the frozen claim, the endpoint chord of z^{3/2} separately confirms its correct sign threshold: the maximum m₃/m₂^{3/2} occurs at upper-eigenvalue mass (2κ+1)/[(κ+1)(κ²+κ+1)] and the crossing is the unique root above one at about 7.3066744332. The cutoff was removed as a contribution for originality, not for incorrectness. If κ is read as an upper spectral bound with fixed calibration, the same cutoff holds; the repaired statement defines κ unambiguously as the actual condition number. No simulation is needed.

## originality

PASS

This PASS is for the re-audited replacement in repairs/2, not the frozen claim as submitted. The frozen universal descent threshold and endpoint witness are covered by the distinct Resultary core-LARS frontier 70b4a7c981f6. The repaired finding removes that contribution, cites its coverage, and retains only the sharp global magnitude of objective amplification and its near-attainment in probability under a specified spiked spectrum. The relevant compared results do not supply that magnitude and typicality law.

## value

PASS

The repaired result quantifies how far verified distance decrease can diverge from objective decrease: a one-step increase can approach a factor of five. Demonstrating typical near-attainment under a natural uniform-sphere start with one high-curvature direction is stronger than a single counterexample. It identifies the separated scales κ≪d≪κ² at which the spike is negligible for the initial objective but dominates the squared gradient. The covered cutoff is not credited as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
