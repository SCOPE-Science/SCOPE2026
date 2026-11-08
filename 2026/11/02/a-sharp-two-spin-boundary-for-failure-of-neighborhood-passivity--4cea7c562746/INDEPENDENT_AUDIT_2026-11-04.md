# Independent mathematical audit

## correctness

PASS

At a Gibbs start at beta0, a single beta1 Glauber step on energies (0,A,A,B) gives p1(--)-p1(+-)=H(B)/(2Z), H=(3g-1)(y+z)-f(1+y), with y=exp(-beta0 A), z=exp(-beta0 B), f=(1+exp(beta1 A))^-1, g=(1+exp(beta1(B-A)))^-1. Next-temperature local passivity is -tanh(beta2(B-A)/2)H/Z. H(A)>0, H(A+log(2)/beta1)<0 and H strictly decreases while 3g-1>0; afterwards H<0. Thus unique B* and the strictly nonempty ferromagnetic interval A<B<min(B*,2A), even for arbitrarily small positive cooling. Independent four-state rational calculation reproduced H(5)=293719/16000000, P(--)= -293719/163334085 and normalized populations for A=4, B=5, beta0=log(20/19), beta1=log(3/2), beta2=log2; one spin reaches beta1 Gibbs in one update. The analytic derivative, not the finite witness, proves the full parameter theorem.

## originality

PASS

A general failure of Luo et al. neighborhood passivity was already demonstrated on a 10-state Petersen graph by the trureturing formal refutation; that broad counterexample is NOT original. The surviving precise claim is the two-spin minimality, a ferromagnetic heat-bath example for every arbitrarily small cooling increment, and exact one-parameter threshold. The inspected prior refutation and Luo paper do not state the two-spin boundary; this is a best-of-knowledge original refinement, not an original general disproof.

## value

PASS

It identifies the smallest physically natural Ising spin count and a sharp nonasymptotic model-parameter region where an annealing activity bound’s sufficient local sign condition fails. It prevents incorrect interpretation of local passivity as universally preserved without claiming failure of the global activity bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
