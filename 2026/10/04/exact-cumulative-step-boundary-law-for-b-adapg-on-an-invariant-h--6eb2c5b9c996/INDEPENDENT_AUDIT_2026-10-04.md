# Independent mathematical audit

## correctness

PASS

On the collinear ray, the Bregman optimality condition gives the exact dual recurrence \(h(t_{k+1})=h(t_k)+\gamma_{k+1}(c-t_k)\), with \(h(t)=t/\sqrt{1-t^2}\). Positive generated steps make \(t_k\) strictly increase. The source's objective-infimum result then forces the only possible limit to be the boundary minimizer \(t=1\). Since \(h(t_k)\to\infty\) while every increment is at most \((c+1)\gamma_k\), bounded cumulative step mass is impossible. Weighted Cesaro convergence gives \(h(t_k)/S_k\to c-1\), and inversion of \(h\) yields both stated \(S_k^{-2}\) asymptotics. An independent scalar replay on a divergent positive step schedule matched the leading constants; it was used only as a transcription check.

## originality

PASS

The source paper supplies B-adaPG, the same Hellinger-ball kernel, failure of its Bregman-zone assumption, and the objective-infimum theorem, but not the invariant-ray full-sequence theorem or exact cumulative-step constants. Earlier Hellinger BPM theory explains the general boundary-rate phenomenon under its own step conditions. The recent broad convergence paper was only abstract-accessible here and remains a residual risk, not evidence of noncoverage.

## value

PASS

The source explicitly highlights boundary-active least squares with this Hellinger kernel outside its Bregman-zone assumption. The audited invariant ray is a natural exactly solvable benchmark: it proves full-sequence boundary convergence, rules out finite cumulative step mass, and determines sharp leading behavior in the method's endogenous clock.

The dated certificate retains the supplied scientific assessment, sources and limitations.
