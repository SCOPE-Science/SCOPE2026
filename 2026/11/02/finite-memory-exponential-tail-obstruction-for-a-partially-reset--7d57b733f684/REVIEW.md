# Scientific evaluation

## Correctness

PASS. The generator applied to \(x^2+gq^2\) is the explicit negative-definite quadratic drift plus four, establishing positive recurrence and a finite stationary second moment. The reset-free probe starting at \((0,q)\) has exact mean \(g(1-e^{-(1+1/g)a})q/(g+1)\) and variance \(2a/(g+1)+g^2(1-e^{-2(1+1/g)a})/(g+1)^2\). Independent Poisson reset ages and the pre-reset bath marginal yield an exact stationary conditioning identity. Jensen proves exponential-moment divergence; a compact-mass restriction and one-dimensional Gaussian asymptotics prove the quantified far-tail bound. The quasistatic comparison is expressly to a defined mixture, not to a claimed rigorous parameter limit. Algebraic checks are reproducible in the companion script.

## Originality

PASS, with residual risk. Santra and Das, arXiv:2603.17027v1, full-text sections II–III and Appendix, establish the model, variance, and quasistatic Gaussian approximation but do not establish the stated finite-\(g\) far-tail obstruction or the exponential-moment divergence threshold. Falcao and Evans, arXiv:1610.03503v1, analyze collision-triggered joint resetting of two particles, not a bath degree of freedom preserved at exogenous reset epochs. Targeted published-results comparisons found no matching stronger finite-\(g\) claim; general age-mixture arguments are established techniques and an unidentified stronger general partial-resetting theorem remains a priority risk.

## Value

PASS. The exact rare-event boundary is motivated by the source paper's central conclusion that strong viscoelastic memory gives Gaussian stationary tails. It identifies a nonuniform asymptotic effect: even very long but finite bath relaxation allows rare reset-free intervals with unbounded diffusive center-of-mass spread. A quantitative exponential-moment obstruction and spatial log-tail bound distinguish this effect from low-order moments or a minor coefficient refinement, and delimit when the quasistatic tail law can be used.

## Scope and residual limitations

The main lower bound is not a matching tail asymptotic. The moment-generating function may diverge at smaller nonzero arguments. The strong-memory Gaussian mixture is used as an explicit mathematical comparator; convergence of finite-memory stationary laws to this comparator is not newly proved. The calculation is for one linear bath coordinate with position-only Poisson resetting and finite positive bath friction.

Self-review: passed. Independent audit: not yet performed.
