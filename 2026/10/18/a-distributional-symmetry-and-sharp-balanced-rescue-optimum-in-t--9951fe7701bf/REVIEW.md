# Independent mathematical audit

## correctness

PASS

Rebuilt three-state transient Q=[[-a-b,b,a],[c,-a-c,0],[d,0,-b-d]], absorption r=[0,a,b]. Symbolically inverted (sI-Q) and recovered L(s)=ab(2s+K)/(s^3+[2(a+b)+C]s^2+[a^2+3ab+b^2+(a+b)C+cd]s+abK), K=a+b+C. All coefficients and denominator positive for s>=0. Differentiate holding C fixed: dL/dz=-ab(2s+K)s/D^2<0 for s>0. AM-GM z<=C^2/4 proves unique balance if C>0. Derived E[T]=(a^2+ab+b^2+(a+b)C+z)/(abK) and Var[T]=A^2/(abK)^2-2[2(a+b)+C]/(abK)-4/K^2 with A=a^2+3ab+b^2+(a+b)C+z, so both increase in z. Symbolic exact independent reproduction and rational a=4,b=1,C=2 endpoints were checked.

## originality

PASS

General finite absorbing Markov-chain resolvents and conservation-colonization optimization are standard; the exact direction-swap law with heterogeneous local extinction rates and one-parameter balanced allocation optimum was not found in identified papers.

## value

PASS

An unexpected complete-law exchange symmetry despite unequal local extinction rates, plus an exact simultaneous optimum for two practically distinct extinction-time moments at a fixed physically explicit successful rescue budget, gives a useful finite-state ecological mechanism and boundary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
