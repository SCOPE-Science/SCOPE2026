# Scientific review of the Bayesian last-success posterior threshold

## Correctness — PASS

The claim concerns the conditional Beta-posterior decision after a success, with arbitrary real positive shapes and a deterministic integer number of future observations. A predictive-probability ratio converts every deterministic future stopping rule to a finite sum of rising-factorial ratios with strictly monotone shape dependence. This proves a unique continuous acceptance threshold and its monotonic increase with the failure-shape parameter. A simultaneous induction establishes both immediate acceptance and first-future-success optimality throughout the high-failure region. An explicit profitable deviation after the first future success proves sharp failure below the quadratic transition. Independent policy enumeration and exact-rational Bellman calculations (1181 passing assertions) stress-test the identities. Finite checks do not prove the universal theorem; the preceding finite induction and finite-policy proof do.

## Originality — PASS, with qualification

The closest full-text source is Katsunori Ano's 2026 *Monotone Multiple Stopping and Last-Success Problems* (arXiv:2610.10237v1), especially its Bayesian section, which supplies finite backward recursions but does not state the all-horizon quadratic posterior-shape phase boundary, strict converse, unique general threshold, or the complete two-future-trial formula. Bruss' known-odds theorem does not address posterior learning. Paindaveine's 2026 unknown-odds paper studies frequentist oracle performance rather than Beta-posterior statewise structural phases; Gnedin–Derbazi use random observation times and another model. Targeted search of relevant mathematical finding records and the open literature did not show a theorem implying this combination. This is a best-knowledge originality assessment, not a uniqueness certificate. Residual risk: classical Bayesian secretary literature, an antecedent Japanese preprint mentioned by Ano, or a general monotone-likelihood-ratio stopping theorem might imply part of the new structural result in different language.

## Mathematical value — PASS

This exact posterior-state phase diagram addresses a substantive ambiguity in Bayesian last-success selection: updating can invalidate pathwise monotone stopping, but the theorem determines precisely when the intuitive one-step odds rule regains global optimality and when adaptation strictly improves it. The universal critical curve \(B=k(k-1)+1\), strict converse, and explicit two-trial boundary provide a usable structural and computational answer for every finite horizon rather than an arbitrary parameter slice or a numerical approximation. Its value is limited to one selection right and Beta mixing; it is not claimed to solve the broader multiple-selection problem.

Self-review: passed. Independent audit: not yet performed.
