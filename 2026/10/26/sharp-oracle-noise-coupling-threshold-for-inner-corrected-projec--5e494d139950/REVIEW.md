# Scientific review

## Correctness — PASS

The finding has one exact object: the two-microstep, four-stage IPFE scheme of Koellermeier and Samaey, with a specified additive four-stage noise covariance and macrostep \(ah=1\). Substituting the inner stages gives the exact uncorrected multiplier \(\lambda(1-\lambda)\); the final-stage difference produces the amplified error \(\xi[-(1+\lambda)\eta_2+\eta_3]/(2\lambda)\). The proof retains the positive correlation-deficit term and proves both directions of the bounded-variance threshold. It also proves the full finite-time second-moment identity, the constant-correlation divergence coefficient, the finite critical limit and the necessary/sufficient independent batch growth. Normalizations \(h\), \(a\), \(\sigma^2\), \(\rho\) and all quantifiers are explicit. An exact rational verifier independently checks the derived algebra on 1,680 instances; it is not used as an infinite proof.

## Originality — PASS (qualified best-knowledge assessment)

The method and deterministic order/stability claims are prior work, not claimed new: Koellermeier--Samaey, arXiv:2210.08302v2, Section 5.2 eq. (114). The target new statement is an exact stochastic-oracle covariance and stationary-risk theorem for its four-stage implementation. Xiu--Kevrekidis analyzes stochastic equation-free projective computation using a different coarse-observable construction, and the accessible Papavasiliou--Kevrekidis abstract discusses general variance reduction, without providing an inspected exact IPFE theorem. Four focused published-finding corpus queries covering IPFE, noise amplification, aliases, coupling and exact covariance returned no covering statement. Nearby records concern different stochastic iterations or standard correlated-noise algebra, not this tableau and risk threshold. Residual risk: an uninspected older finite-difference/coupling paper could imply the specialized result; Papavasiliou--Kevrekidis full text was unavailable. No inference of uniqueness is drawn from search failure.

## Value — PASS

IPFE uses a short-interval derivative difference to preserve desirable deterministic fast-mode stability and order. The theorem identifies a sharp hidden stochastic cost: \(\lambda^{-2}\) uncorrelated sampling variance even when the original PFE variance stays bounded. The exact correlation-deficit threshold, leading error-floor constants and necessary independent batch growth explain when the correction is viable and when it imposes a resource penalty. This is a motivated structural boundary and reproducible solver-design benchmark, not an arbitrary parameter slice or generic restatement of deterministic stability.

## Closest literature and limitations

See RESULT.md References 1--3. The full open source text of the originating IPFE paper was read in relevant sections; related Xiu--Kevrekidis material was read. Only the abstract of the Papavasiliou--Kevrekidis variance-reduction article could be inspected, so exact noncoverage by its full text is not claimed. The theorem is not about physical SDE forcing or nonlinear dynamics and relies on independent refresh across macrosteps. Independent scientific assessment and publication-priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
