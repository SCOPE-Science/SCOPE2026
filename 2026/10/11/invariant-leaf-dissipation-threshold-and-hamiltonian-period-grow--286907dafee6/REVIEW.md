# Independent mathematical audit

## correctness

PASS

Reconstructed the exact vector field dx=y, dy=-x+yz, dz=-y-a*x*y-b*x*z. Differentiation gives d[x+z+a*x^2/2]/dt=-b*x*z; for b=0 every level reduces to dy=-x+(C-x-a*x^2/2)y. In y>-1 the proper nonnegative H=x^2/2+y-log(1+y) has dH=(C-a*x^2/2)y^2/(1+y), yielding compact forward trapping under a>=0,C<=0 and LaSalle convergence to (0,0) unless (a,C)=(0,0). The invariance check is essential: on y=0, dy=-x, and on x=0, dx=y, so no other trajectory remains in the zero set. At the center a=C=0, v=log(1+y) makes xdot=e^v-1, vdot=-x with convex coercive W=e^v-v-1; small energies give period 2*pi. Quadrature T=sqrt(2)*integral dv/sqrt(h-W(v)), negative turning point v_-=-h-1+o(1), and positive interval negligible at scale sqrt(h) give T/sqrt(h)->2*sqrt(2). For y<-1 at C=0, H_-=x^2/2+y-log(-1-y) is conserved and y~-x^2/2; dt=dx/y is integrable towards both spatial ends. For a=0,C!=0, H is strictly monotone between crossings, y<-1 drifts x strictly left, y=-1 has dy=-C, preventing recurrence. Compact invariant measures are mixtures of equilibrium and periodic-orbit laws by Poincare recurrence/ergodic decomposition. Checked finite-symbolic identities from inspected verify.py without treating optional quadratures as proof.

## originality

PASS

Best-of-knowledge original boundary classification for the exact LE2 field, rather than claims about the known chaotic parameter examples. The 2013 LE2 primary paper/2015 correction identify the equations, but their numerical phase portraits do not supply this b=0 global foliation, Hamiltonian h->infinity period asymptotic or invariant-measure classification. Nearby Sprott J / 2022 line-equilibrium results concern different vector fields. An equivalent treatment of the exp-potential oscillator could exist under another name; this risk remains explicit.

## value

PASS

The b=0 coupling-removal parameter is a natural boundary of a named quadratic flow. A polynomial integral splits the full system into invariant leaves and leads to a sharp damping versus conservative threshold, an exact large-energy period-growth constant, and an invariant-measure/finite-time-blowup division across y=-1. These independently useful global properties go well beyond a routine coordinate substitution, numerical trajectory plot or trivial equilibrium check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
