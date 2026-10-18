# Scientific review: A sharp total-variation phase diagram for reinforced binary sampling

## Correctness (C): PASS

The urn count has an exact beta-binomial mass and a beta-mixture representation. A strictly increasing ratio of adjacent likelihood ratios makes the negative signed-mass set an interval. This structural lemma turns convergence of cumulative distribution functions into convergence of the **exact finite-lattice total-variation metric** in the critical scaling. Independent beta/binomial fluctuation components produce the Gaussian variance factor; a separate scale separation proves total variation tends to one when draws dominate initial concentration. In the concentration-dominated regime, a summed second-order Taylor expansion and an exact binomial-score identity yield the universal \(\varphi(1)\) coefficient. The complete quantifiers and estimates appear in `RESULT.md`. The standalone script checks 200 exact-rational parameter sets and 24 numerical asymptotic cases. Finite checks alone are not the proof.

## Originality (O): PASS on inspected primary evidence

The closest papers concern (i) Pólya convex ordering, Meleşteu–Pascu–Pascu (2022), arXiv:2201.05870; (ii) process Gaussian asymptotics covering precisely the same draw-to-initial-mass regimes, Borovkov (2019), arXiv:1912.09665; and (iii) binomial approximation to beta-binomial by Stein bounds or fixed-parameter corrections, Teerapabolarn (2008, 2014). Their precise inspected statements overlap essential ingredients, but do not imply the exact *discrete* total-variation phase profile and small-ratio coefficient without additional work. The supporting Gaussian fluctuation structure and fixed-parameter corrections are credited as existing facts. Searches also considered beta-binomial likelihood-ratio aliases and broader Bernoulli-mixture classes, with no stronger direct coverage identified. See `AUDIT.json` for source inspections, mathematical implication comparisons and residual priority risks. This finding has no independent validation.

## Value (V): PASS

The result supplies a natural sharp boundary for treating reinforced sampling as independent sampling: approximation error is of exact first order when the urn is much larger than the sample, remains bounded away from zero at comparable scales, and approaches one when sampling overwhelms initial mass. The Gaussian critical formula and the universal first-order coefficient give explicit benchmark values, beyond a generic convergence statement. The connected optimizing interval also has finite-sample meaning for the test distinguishing the two models.

## Limitations and status

Fixes the interior fraction \(\,p\in(0,1)\,\) while concentrations diverge; no uniformity near endpoints or critical convergence rate is claimed. Undiscovered equivalent earlier work cannot be ruled out, and known Gaussian limits are not presented as new. The attached checker is finite corroboration rather than a formal infinity certificate.

Self-review: passed. Independent audit: not yet performed.
