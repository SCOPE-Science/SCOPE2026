# Scientific review

## Correctness — PASS
The proof works for every \(n\ge1\), including the case of a single domain point. If \(d=\min D\), order reversal and decrease give \(\max f(D)=f(d)\le d\). Thus either the image and domain are disjoint, forcing \(f^2=0\), or they meet exactly at \(d\), forcing \(f(d)=d\) and a nonzero rank-one idempotent square. This also establishes \(f^3=f^2\) for every element. Each antitone surjection on fixed domain/image sets is parametrized by \(\binom{w-1}{h-1}\) nonempty constant runs. The strict and touching endpoint alternatives correspond bijectively to subsets of sizes \(w+h\) and \(w+h-1\), respectively. A formal-power-series computation and a domain-shift bijection yield the Fibonacci totals. This proof does not extrapolate from examples. The independent-in-code exhaustive routine checked all maps through \(n=9\), including binomial strata and iterates; its `VERIFY_OK` confirms those finite cases.

## Originality — PASS with residual literature risk
The relevant primary article by Zubairu, Umar and Al-Kharousi, arXiv:2512.21134, Theorem 1.4, supplies the sum of the two stratum counts, but does not give the endpoint-defined square-zero/stabilized-square split, the cubic stabilization result or the two separate Fibonacci totals. The current formulas reproduce that established count exactly when added, and do not claim it as novel. Cornelius and collaborators' 2026 fixed-point refinements treat injective order-reversing decreasing partial maps; those can meet the \(h=w\) subcase, but do not imply the noninjective stratum formulas. The withdrawn Ayık et al. preprint concerns rank/cardinality properties; its complete original version was unavailable. An older thesis studies nilpotent subsemigroups for other order-decreasing classes, and its full text was not verified. Comparison of equivalent formulations, broader claims, indexed tables and implication structure did not reveal prior full coverage. Residual risk: an older inaccessible or unindexed source could contain the same endpoint partition.

## Mathematical value — PASS
The split is motivated by genuine semigroup dynamics: it identifies exactly which antitone decreasing transformations become zero after two compositions and which stabilize at a nonzero rank-one projection. Its full width-height distribution respects the two structural parameters used by the primary literature, gives the first admissible chain size for both behaviors, and produces strikingly distinct Fibonacci totals. These are natural invariants of a newly examined transformation-monoid sector, useful when studying powers, idempotents and nilpotent layers. The result is not asserted to resolve the broader power structure of all monotone decreasing maps.

## Closest sources and limitations
- Zubairu, Umar, Al-Kharousi (2025), arXiv:2512.21134, full text, Theorem 1.4: exactly the unsplit width-height census.
- Cornelius, Shalangwa, Ajiya, Ishaku (2026), DOI:10.62054/ijdm/0302.06, injective fixed-point/image-change refinements only.
- Ayık, Ayık, Dimitrova, Koppitz (2025), arXiv:2507.06047, withdrawn, original full text unavailable; rank/count claims in accessible abstract.
- Umar (1992), thesis on order-decreasing transformations, publicly accessible abstract only.

Unindexed literature and inaccessible complete manuscripts leave an unavoidable originality risk. Exhaustive computation through \(n=9\) is corroboration, not proof in general. The mathematics has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
