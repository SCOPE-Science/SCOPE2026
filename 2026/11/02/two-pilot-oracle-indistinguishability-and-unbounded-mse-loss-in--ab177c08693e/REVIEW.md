# Independent mathematical audit

## correctness

PASS

In both spectra the first L eigenvalues equal delta, the positive tail energy is delta^2, and the remaining eigenvalues are strictly below delta; the concentrated larger tail exceeds its smaller tail since epsilon^2<1/p. Thus the exact squared pilots are (9k+1)delta^2 and delta^2, at identical n and cost. Commuting exact spectral truncations make the preconditioned log diagonal with leading zeros; independent Gaussian squares give MSE twice the squared log tail divided by the probe count. The diffuse ratio is exactly N(p-h)/p>1 and diverges. For the concentrated member at each k, the one-probe risk tends to zero and the mixed risk has a positive limit. Hence selecting mixed on any such pilot tuple produces unbounded loss as epsilon tends to zero, while selecting one on every tuple produces unbounded loss across the diffuse k sequence. This reasoning also covers independent randomization as described in the record. Both preconditioned matrices use at most three eigenspaces, so Lanczos is exact in at most three exact-arithmetic steps once the oracle projection is provided. The Section 4.3 switching inequality, verified as arXiv eq. (4.4), has left/right ratio (9k+1)/(3k+1)>1; the Wiley equation numbering was not independently confirmed. Equality of costs is nominal and does not include acquiring the best-rank oracle. VERIFICATION.md records 5575 finite checks; verification.py was inspected, not rerun. The conclusion is not about the actual Nyström pilot distributions.

## originality

PASS

The supported distinct claim is the two-spectrum indistinguishability theorem for arbitrary rules using only the exact pilot data. The single diffuse witness and its exact loss ratio also occur as a specialization in the separately dated 2026-11-22 record; they are not a point of distinction from that record. Neither that material overlap nor the earlier optimality rule with full spectral information supplies the identical-pilot pair or the lower bound for every pilot-only selector.

## value

PASS

The information obstruction distinguishes a failing switching heuristic from an intrinsically insufficient summary: no retuning of any function of just those two exact residuals can obtain a finite competitive guarantee in this model. Positivity, mild conditioning, and exact finite-step Lanczos isolate the failure from other numerical pathologies. This is a substantive boundary of a motivated budget-allocation model without implying failure of the end-to-end randomized algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
