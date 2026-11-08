# Independent mathematical audit

## correctness

PASS

For every real mu, write F_mu(x,y)=(mu+y,-max(x,0)), q_mu(t)=mu-max(t,0); direct two-step recurrence x_{n+2}=q_mu(x_n) gives F_mu^4=(q_mu²(x),q_mu²(mu+y)-mu). Piecewise evaluation shows q_mu² constant mu for mu<=0 and clipping onto [0,mu] for mu>0, exactly the orthogonal projection onto singleton or [0,mu]×[-mu,0]. On the square F rotates by 90 degrees; every noncenter point has least period four, fixed center unique, and all invariant probabilities are four-rotation-invariant. Every initial point has empirical limit the cycle-uniform measure of its projected point; only corner projection fibers contain positive planar area, yielding unique four-corner physical measure for mu>0, and whole-plane fixed Dirac for mu<=0. Explicit states require four steps, confirming sharpness. Independently checked 2500 rational grid cases across negative, zero and positive mu including boundaries; analytic scalar proof covers all real inputs.

## originality

PASS

PASS best-of-knowledge. The exact same normal form was published by Simpson; his accessible 2024 full paper addresses parameter-space dynamics and the delta_R=1 centre boundary but not the all-plane fourth-iterate projector or full ambient-Lebesgue physical measure theorem. The 2026 first-return result requires delta_R>1. Priority risk from older polygon paper is explicit.

## value

PASS

The zero-determinant/neutral-quarter-turn resonance is a natural boundary of a classical piecewise-linear bifurcation family. A global finite-time metric projection followed by exact order-four rotation gives a complete invariant/ergodic and physical-measure classification, sharply separating invariant area probability from the unique physical corner cycle and its basin; this is a motivated structural fact despite its elementary recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
