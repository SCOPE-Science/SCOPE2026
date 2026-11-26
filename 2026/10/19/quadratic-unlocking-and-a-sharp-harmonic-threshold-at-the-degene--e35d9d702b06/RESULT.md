# Exact locking at the critical harmonic ratios of a degenerate half-turn

## Finding

Fix \(a>0\) and \(b\in\{-4a,4a\}\). For sufficiently small real \(\mu\) of either sign, the increasing circle lift
\[
F_{\mu,b}(x)=x+\tfrac12+\mu[a(1+\cos(4\pi x))+b\sin(2\pi x)]
\]
has real translation number \(1/2\). Thus exact locking holds at the critical ratios, where the quadratic bottleneck form of the two-step return is degenerate. In the case \(b=4a\) the bottleneck at \(x=3/4\) is detected by the exact signed displacement
\[
F_{\mu,4a}^2(3/4)-1-3/4=-2a\mu[1-\cos(8\pi a\mu)]^2.
\]
For small nonzero \(\mu\) this has sign opposite to \(\mu\); the first nonzero term at this point is of order \(\mu^5\), not \(\mu^3\).

## Assumptions and scope

The parameter \(a\) is held fixed while \(\mu\to0\). The lift is orientation preserving because its derivative is uniformly positive for sufficiently small \(|\mu|\). The real translation number is \(\lim_{k\to\infty}(F_{\mu,b}^k(x)-x)/k\), with no reduction modulo one. Only the two critical ratios are claimed here.

## Proof

Write \(f(x)=a(1+\cos(4\pi x))+4a\sin(2\pi x)\) for \(b=4a\) and let
\[
D(x)=F_{\mu,4a}^2(x)-1-x=\mu[f(x)+f(x+1/2+\mu f(x))].
\]
At \(x=3/4\), \(f(x)=-4a\) and the second argument is \(5/4-4a\mu\). For \(c=\cos(8\pi a\mu)\) one has \(f(5/4-4a\mu)=2a(1-c^2)+4ac\). Thus \(D(3/4)/\mu=-4a+2a(1-c^2)+4ac=-2a(1-c)^2\). This ratio is strictly negative for sufficiently small nonzero \(\mu\), and expansion of cosine gives \(D(3/4)=-2048\pi^4a^5\mu^5+O(\mu^7)\). At \(x=0\), \(D(0)/\mu\to f(0)+f(1/2)=4a>0\). Hence \(D\) has a zero for both signs of \(\mu\). At such a point \(x_*\), \(F^2(x_*)=x_*+1\), so lift periodicity gives \(F^{2k}(x_*)=x_*+k\) and translation number \(1/2\). At \(\mu=0\) the conclusion is immediate. Conjugation by \(x\mapsto x+1/2\) changes \(b\) to \(-b\) without changing the translation number, proving the other endpoint.

## Comparison and limits

Glendinning's strict-transversality theorem does not apply at the equality of the constant and second-harmonic amplitudes: the first-order return vanishes at its minima. [A second-order rotation-number cusp at a degenerate half-resonance tongue edge](https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-a-second-order-rotation-number-cusp-at-a-degenerate-half-resonan--e144d81f7af4/RESULT.md) analyzes the same lift, with quadratic drift for \(0<|b|<4a\) and locking for \(b=0\) or \(|b|>4a\), but explicitly excludes \(|b|=4a\). Its local quadratic minimum vanishes at these ratios, so it does not decide their locking. The exact trigonometric cancellation above decides the missing boundary without requiring a uniform expansion in \(b\) or a claim about generic tongue pinching.

## Reference

P. Glendinning, *Scaling of the rotation number for perturbations of rational rotations*, arXiv:2506.19508, Theorem 1.3 and §6, Eqs. (6.34)–(6.36).
