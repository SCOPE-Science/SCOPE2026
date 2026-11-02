# Independent mathematical audit

## correctness

PASS

Independent perimeter endpoints select same, opposite, adjacent side-pairs with probabilities p, p, 1-2p, p=(a²+b²)/(2(a+b)²). Same side gives T=1; normalizing to the square and integrating the diamond density on opposite sides gives A(t)=t(3-t)/(1+t); integrating the adjacent segment-line hit condition UV/(U+V)>=1-t gives B(t)=t-(1-t)² log((1+t)/(1-t))/2. Thus F=pA+(1-2p)B, atom p, no others. The difference h=2B-A has h‴=-8(5-t)/((1-t)(1+t)^4)<0, h(0)=0, h(1-)=1, and h′(0+)=-3<h′(1-)=2, proving exactly one interior zero. Strict monotonicity of p with aspect ratio and quadratic inversion establish the inverse and CDF crossing. Independent SymPy derivative and 4 high-precision conditional quadrature checks match exactly; t*=0.560487923302786118 and common CDF=0.438105619826313741.

## originality

PASS

The probability experiment is not a motion-invariant line, a central-angle chord, or fourth endpoint-distance moment. The exact distribution of minimum gauge along independent perimeter-endpoint chords, including the atom, aspect-ratio recovery and universal one-crossing property was not found in checked records. Indexed-source coverage remains nonexhaustive.

## value

PASS

A complete geometric-probability distribution for a natural random-chord construction, with identifiable shape parameter and a unique universal crossing, is a meaningful exact invariant. The CDF crossing refutes stochastic ordering by aspect ratio and goes beyond elementary endpoint-length moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
