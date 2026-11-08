# Independent mathematical audit

## correctness

PASS

Population-weighted rates cancel exactly to r and delta while individual prey rate differences remain e and g. The smooth transformation x=A/(A+B), P=A+B reduces dynamics to xdot=x(1-x)(e-gY), Pdot=P(r-P/K-delta Y), Ydot=beta Y(-1+delta P). The explicit Volterra Lyapunov function has derivative -(P-P*)^2/K, and compact positive sublevels plus LaSalle yield global ecological convergence. Eliminating P and Y from logarithmic derivatives gives a constant drift for logit(x)-(g/delta)log P-[g/(K beta delta^2)]log Y. Its integration yields exact odds and sign c=e-gY* governs global fixation; at zero a first integral selects one interior equilibrium on a normally attracting segment, with two transverse stable eigenvalues. The positive threshold follows from 0<g<delta and Krdelta>1. Inspected check.py independently shows the intended symbolic identities and numerical examples, but no need to regard numerical integration as proof.

## originality

PASS

Qualified best-of-knowledge PASS for exact neutral selection invariant and global memory foliation in a balanced payoff slice. The original 2026 Cruz-Neves abstract describes 2D ecological reduction and equilibrium stability, but did not make the exact initial-state odds formula evident. The primary complete paper could not be inspected in this run (arXiv PDF/HTML unavailable; authorized Oxford returned vpn_disconnected); this is a substantial priority caveat, not an automatic scientific rejection.

## value

PASS

Sharp global coexistence-selection and initial-condition memory in a natural nontrivially asymmetric payoff family, of direct use in deterministic eco-evolutionary analysis; the neutral foliation is a mathematically meaningful codimension-one phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
