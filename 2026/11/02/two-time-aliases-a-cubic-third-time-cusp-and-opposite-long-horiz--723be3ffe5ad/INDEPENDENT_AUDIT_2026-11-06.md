# Independent mathematical audit

## correctness

PASS

The actual frozen RESULT.md defines the DIRECT step-size-parametrized map S_t=e^{at}(1+bt)e^{tL}, with h>0, known symmetric negative semidefinite L and two positive multipliers. Setting q=e^{ah}>0 and beta=bh gives m1=q(1+beta), m2=q²(1+2beta), so Delta=m1²-m2=q²beta². Positive m1,m2 impose beta>-1/2, hence exactly the two roots z=±sqrt(Delta)/m1 when 0<m2<m1² and unique beta=0 at equality. At s=t/h, M(s;z)=m1^s(1-z)^{s-1}(1+(s-1)z); the cubic m3 relation follows by expansion. An independent SymPy expansion gives branch separation 4 m1³z³=4Delta^{3/2} and exact witness m3+=2816/15625, m3-=-4096/15625. For an extra horizon the exponential-affine branch difference has at most three distinct real zeros, because its second derivative is exponential times a nonconstant affine function; 0,1,2 already are zeros. For 1/(1+z)<m1<1, q+<1<q- and beta-<0, establishing opposite direct long-horizon behavior along ker L. Strict observed contraction uses ||exp(tL)||<=1. Crucial scope: S_{nh} here is a direct long step and NOT the iterate S_h^n; the claim does not apply to higher-order ETDRK4 or a semigroup.

## originality

PASS

The exact two-horizon positive-branch classification, cubic third-horizon discriminant, and opposite DIRECT long-horizon behavior are narrower than general exponential-polynomial reconstruction. The first-order split exponential–Euler map is not the higher-order exponential integrator of the motivating NEXT work. Established confluent Prony algorithms are relevant but do not by the inspected passages expressly assert this exact positivity-constrained two-map/cusp/sign theorem. Novelty is best-of-knowledge and qualified by specialized identifiability literature.

## value

PASS

Observing two time maps and attributing growth to an exponential generator versus an explicit reaction is a natural inverse-model identifiability problem. This self-contained theorem supplies the exact alias locus, the third-observation resolution scale Delta^{3/2}, and a sharp counterexample to extrapolating directly evaluated long-horizon maps from short-time contraction. Although elementary algebra underlies it, the combined precise inverse and stability boundary is a motivated structural fact, not a generic algebra substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
