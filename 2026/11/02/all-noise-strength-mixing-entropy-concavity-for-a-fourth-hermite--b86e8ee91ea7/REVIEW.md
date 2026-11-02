# Scientific review

## Correctness — PASS

The claim is for the explicitly defined fourth-Hermite density, all \(0<a\le1/100\), \(0<q\le1\), \(0<t<1\). Gaussian convolution gives an exact eighth-Hermite output density, and each factor's nonnegativity ensures a uniform denominator bound. The relative-entropy derivative identities are differentiated legitimately under the Gaussian integral. Eight independent Gaussian polynomial moments, four absolute-moment estimates, and both rational certificates are reconstructed by `verify.py`. The analytic first- and second-derivative bounds then imply the advertised global negative curvature. No finite experiment is treated as an infinite proof.

## Originality — PASS (qualified best-knowledge)

The complete relevant Section 8 of arXiv:2610.22386v1 was inspected. Its theorem for \(0<a\le1/100\), \(q\le5/8\) covers all effective amplitudes \(\epsilon=aq^2\le1/256\). Because the output depends only on \(\epsilon\), its conclusion ALSO implies unsmoothed concavity at \(a\le1/256\). The evaluated theorem instead extends the actual effective-amplitude domain to \(1/256<\epsilon\le1/100\), including genuinely uncovered unsmoothed inputs. A general entropy-concavity theorem for Gaussian-scale mixtures does not subsume this case because the input's fourth and eighth Gaussian-Hermite coefficients are incompatible with a nondegenerate variance mixture. Searches of related entropy-concavity and Hermite literature and mathematical-record matches found no claimed stronger implication. General entropy-concavity remains contested; relevant broader literature might contain an implicit perturbation argument, so priority is not independently certified.

## Value — PASS

The exact family is used in a recent statistical-mechanics study to model OU noise restoring mixing-entropy concavity. Extending the certified effective-amplitude range beyond \(1/256\) to \(1/100\) validates the full amplitude family at **all** bath times, including *zero added noise* for amplitudes previously uncovered by reparametrization. It provides a uniform, numerically explicit all-time curvature certificate in a regime where generic symmetric classes can exhibit failures, rather than merely changing a numerical constant or checking isolated parameter values.

## Closest literature and limits

Abu-Ajamieh (arXiv:2610.22386v1), Section 8, is the closest explicit same-family result. Ball–Nayar–Tkocz's broader conjecture and Luo's related work concern more general entropy inequalities; Eskenazis–Gavalakis establish a different Gaussian-mixture class. Conservative perturbation amplitude and curvature constants are not asserted optimal, and no statement extends to arbitrary positive distributions. No independent priority or proof audit has been performed.

Self-review: passed. Independent audit: not yet performed.
