# Independent mathematical audit

## correctness

PASS

Frozen RESULT.md ab65a012bd799f35194631e3bda52a43917bae17 and verify.py 348742fccd5372f023ec58fda4d1aac5b1aa3581 inspected. For left matrix trace tau, determinant D>0 and intercept a>0, solve u"-tau u'+D u=0 with u(0)=0,u'(0)=1 and W(t)=integral_0^t u. The half-flight x(t)=r u(t)-aW(t) closes iff r=aW/u; on the first positive lobe u>0 and log u is strictly concave for either focus, real-node or repeated-root regimes, proving t->r increasing and no premature crossing. The balanced right zone is the reflected, kappa-scaled left flow; return y=r and flight time t/kappa, so P=(1+1/kappa)t and residence ratio kappa. Independent high-precision evaluations tested five endpoint regimes tau=-3,-2,-1,2,3 at D=a=1,kappa=3/2. Predicted stable-node log asymptotic residual 5.4e-5 at t=30; stable double-node log+loglog residual 0.23 at t=25 with logarithmically slow convergence; focus normalized ceiling gap tends 1 (0.9999995); unstable double-node P(R-r)/(C a /D)=1; unstable distinct-node log residual -3.6e-4. All follow analytically by asymptotic expansion of explicit exponentials: stable node log divergence, stable repeated loglog, focus finite ceiling, unstable repeated inverse gap, unstable distinct log divergence. Small-speed inverse gives P=C(2r/a+2tau r²/(3a²)+O(r³)). Numerics only check formula; proof uses exact flows and asymptotics. Hypotheses a,D,kappa>0 and all real tau, boundaries tau=+/-2sqrt D handled.

## originality

PASS

PASS with material risk. Carmona-Fernández-Sánchez-Novaes 2023 fully characterizes crossing-annulus existence and domains of half-maps, but does not state these five physical-time endpoint expansions and one-sided residence-time ratio in the material read. Liu-Liu-Wang 2026 directly studies crossing-annulus critical periods and is an important possible stronger source; lawful OA/preprint search found no full copy, and authorized retrieval stopped at VPN-disconnected, so no whole-document noncoverage is claimed. Other Resultary hits concern unrelated harmonic annuli or different PWL oscillator geometry. Best-of-knowledge distinct quantified time-asymptotic classification.

## value

PASS

PASS. The five natural trace/discriminant boundaries of the same crossing center have sharply different physical-period behavior, including loglog and inverse-gap resonances and exact residence-time splitting. These are geometric and dynamical invariants relevant to approach to the annulus boundary, not trivial type checks or arbitrary sampled parameters. The exact formulas are self-contained and analytically justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
