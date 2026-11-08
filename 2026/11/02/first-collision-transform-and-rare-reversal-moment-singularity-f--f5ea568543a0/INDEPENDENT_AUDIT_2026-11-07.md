# Independent mathematical audit

## correctness

PASS

The folded distance has three mobile-state types C,O,S and generator rates C/O -> S of 2alpha, S -> C/O each alpha. Eliminating F_S from the backward equations gives U=s(s+4alpha)U/(4v^2), with incoming contact F_C(0)=1 and antipodal folding F_O(H)=F_C(H). This yields the quoted hyperbolic quotient for x in (0,H] and s>=0, all alpha,v,H>0. Its fixed-alpha s expansion gives the mean. The chance of a preballistic reversal is exactly 1-exp(-alpha*x/v); conditioned on this event the first stalled holding time is Exp(rate 2alpha), and a further reversal before contact has probability O(alpha), proving alpha*T|E => Exp(rate 2). The scaled transform at s=alpha*z expands uniformly holomorphically on |z|<1 as 1-alpha*x*z*(z+4)/(2v*(z+2))+O(alpha^2), so Cauchy coefficient extraction proves every fixed moment coefficient, not merely weak convergence. Independent SymPy verification recalculated mean and coefficients m=2,...,16; source program generator identities and incoming boundaries inspected.

## originality

PASS

Best-of-knowledge original for the precise quantified final claim after comparing same-object and broader primary literature; the prior components/techniques are explicitly credited and residual historical-priority risk is retained.

## value

PASS

First entry to a jammed encounter is a natural kinetic observable, distinct from stationary jamming occupation or mixing. The exact spectral transform and sharp rare-tumble hierarchy reveal genuine nonuniform integrability: typical collision tends to ballistic while mean doubles and all higher moments diverge. The effect and conditional Exp(2) mechanism are useful beyond a numerical or textbook observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
