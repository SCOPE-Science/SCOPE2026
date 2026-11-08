# Self-review

## Correctness — PASS

For the precisely normalized common-switch process with finite integer \(d\ge2\) and \(\alpha>0\), the two-state stationary generator gives the previously established radial transform. A positive heat-kernel mixture of exponentials yields the unique isotropic Lévy density. The polar class-\(L\) test is monotonicity of \(r^d\ell(r)\), and the modified-Bessel derivative identity reduces the sign test to the ratio \(2H_\beta(br)/H_\beta(ar)\), strictly below two and tending to two at the origin when \(\beta=d/2-1\ge0\). This proves the necessity and sufficiency \(\alpha\ge2\) including its equality case, without relying on finite sampling. The radial derivative has a nonnegative integrable negative at exactly these rates, yielding the explicit Poisson jump density of total mass \(\alpha\); direct OU Lévy integration reconstructs the stationary law. The known scalar threshold is checked separately and does not establish the vector threshold. The standalone checker passed 393 finite diagnostic assertions, including high-precision logarithmic asymptotics and dimensional jump-integral checks; finite diagnostics are not the proof.

## Originality — PASS, qualified by residual priority risk

Frydel (arXiv:2407.12213, sections II–V and equation (20)) already derived the stationary transform, dimensional extension and the effective-stiffness distribution's crossover at \(\alpha=2\). Those are not claimed as new. Existing one-dimensional switching-trap work already includes the scalar self-decomposability threshold, including unequal-rate extensions; it does not imply self-decomposability of a joint distribution in \(\mathbb R^d\). Sato's classical polar criterion and subordination inheritance are also credited. The published variance-gamma/Gaussian compound-Poisson example is a different distribution; Buchmann–Lu–Madan's Thorin-subordinator sufficient theory does not entail the converse for a non-Thorin subordinator. The exact joint-vector cutoff, its proof, the positive vector OU jump bath and strict projection-versus-joint interval were not found in the inspected accessible material. Older Markov-modulated OU papers and unindexed special-function classifications remain an explicit priority risk; literature search is not a uniqueness certificate.

## Mathematical value — PASS

The difference between a scalar marginal's ability to admit independent-increment OU forcing and the full joint model's ability is physically consequential: the same trap switch is shared by all coordinates. The interval \(2(\sqrt2-1)\le\alpha<2\) is an exact, natural and nonempty model-identifiability boundary. The constructive above-threshold Lévy bath and the below-threshold obstruction give a complete stationary-marginal decision rule for every finite \(d\ge2\). It is not merely a generic special-function identity or a numerical slice.

## Limitations and literature risk

The result does not address independent coordinate switches, unequal switching rates, arbitrary anisotropy, arbitrary matrix-drift OU baths, temporal covariance or path-law equivalence. The explicit vector threshold coincides numerically with the source's known effective-stiffness crossover; this coincidence is not misrepresented as a newly discovered value in the original physical model. The relevant earlier Markov-modulated OU manuscript (Ratanov, arXiv:2102.13308; 2022 journal continuation) was accessible in abstract only, so a stronger covered equivalent in that full text cannot be categorically excluded; a later Frydel semi-Markovian source also received abstract-level comparison only.

Self-review: passed. Independent audit: not yet performed.
