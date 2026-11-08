# Independent mathematical audit

## correctness

PASS

For r>=2 and n>=r+2, put X=sum_i x_i and Y=sum_i y_i in the labeled crown graph. The precise strict best-response equations are x_i=1_{Y-y_i in {0,r}} and y_i=1_{X-x_i in {0,r}}. Equal pair types require totals in {1,r+1}, while unequal types require totals in {0,r}; since these sets are disjoint for r>=2, equal and unequal types cannot coexist. All-equal-pair profiles have exactly t=1 or t=r+1 active pairs; all-unequal-pair profiles are polarized, or at the unique resonance n=2r split equally. Thus exactly E(n,r)=2+n+binom(n,r+1)+1_{n=2r}binom(2r,r), and matching action polynomial; K_{n,n} has only two polarized equilibria. The actual RESULT.md proof establishes all integer parameters, including n=r+2, not a sampled inference. Independent explicit open-neighborhood brute force found exactly the classified profiles for every n=4..7 and 2<=r<=n-2 (10 parameter pairs); examples E(6,3)=43 and E(7,3)=44.

## originality

PASS

Best-of-knowledge PASS for the complete labeled equilibrium count, polynomial and n=2r complementary resonance, not for basic best-response equations or generic complexity of picky public-goods games. The known NP-hardness of equilibrium existence on general graphs does not imply these fixed crown-graph counts.

## value

PASS

The dense crown is a natural one-perfect-matching deletion of K_{n,n}; this deletion changes a two-equilibrium system to an exact combinatorially large spectrum and creates a sharp resonance at n=2r. This is a motivated graph-family classification and quantitative structural sensitivity, beyond routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
