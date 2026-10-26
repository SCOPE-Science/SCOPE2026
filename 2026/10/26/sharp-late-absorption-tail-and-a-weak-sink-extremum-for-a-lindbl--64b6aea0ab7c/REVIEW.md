# Scientific review: Lindblad half-line late absorption

## Correctness — PASS
The exact half-line Green function is expanded at both square-root band edges, with the physical branch and decay poles separated. Its two \(t^{-3/2}\) amplitude contributions give a positive mean \(t^{-3}\) absorption flux; cross-band oscillations integrate one order lower. The resulting \(t^{-2}\) defective tail gives precisely the conditional moment boundary at order two and the \(2C_m\) truncated-second-moment logarithmic coefficient. Differentiating the explicit coefficient yields a strictly decreasing polynomial in squared loss, proving a unique maximizer; differentiation of the independent total-absorption integral shows the opposite response at unit coupling. These computations apply to each fixed positive parameter value. The standalone SciPy/NumPy checker reports 66 successful finite/identity checks but is not a substitute for the band-edge argument.

## Originality — PASS, best-knowledge
Riberi (arXiv:2605.08056) proves the Green function, exact propagators and full eventual absorption, but the inspected mathematical statements and appendices do not give the present integrated late-time coefficient, sharp conditional moment cutoff, logarithmic second-moment constant, or optimization of the rare-late coefficient. Friedman–Kessler–Barkai (arXiv:1611.05676) obtain oscillatory cubic detection laws under repeated **projective measurements** on the full lattice; the Lindblad sink and precise coefficient do not follow from that renewal-measurement formula. Didi–Barkai (arXiv:2108.13047) instead study measurement-induced motion and a different asymptotic exponent. The cubic exponent by itself is established in other models and is not claimed as novel. Closely related published-result searches and the available prior mathematical findings did not identify equivalent implication coverage. Priority outside inspected literature remains uncertain.

## Value — PASS
The total absorption probability and the late-event tail answer different physical design questions. The theorem quantitatively separates them at unit coupling, computes exactly which surviving absorption-time moments exist, and gives the uniquely extremal rare-late coefficient for each start site. The coefficient's finite-site dependence and \(\eta_m^{\mathrm{tail}}<1\) provide a structurally meaningful contrast with overall absorption optimization; maximizing late events is not itself a recommended design goal.

## Scope and risks
Only fixed-parameter half-line nearest-neighbor Lindblad absorption is covered. The instantaneous \(t^3\) flux oscillates; only the integrated tail has a scalar asymptotic. A more general unlocated band-edge asymptotic theorem might encompass the statement, and no literature-wide or independent priority determination is asserted.

Self-review: passed. Independent audit: not yet performed.
