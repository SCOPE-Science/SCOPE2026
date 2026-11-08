# Independent mathematical audit

## correctness

PASS

For dx/dt=-x+u with sample/hold u=-k x(t_j), k>1, exact sample multiplier M_k(s)=(k+1)e^-s-k. For iid equal-probability positive H=h±d with h>d>0, conditional variance factor V=E M_k(H)²=k²-2k(k+1)e^-h cosh d+(k+1)² e^-2h(2cosh²d-1), so E X_j²=X_0²V^j exactly. Periodic boundary h_per=log((k+1)/(k-1)); factorization at h_per V-1=2(k-1)(c-1)((k-1)c-1), c=cosh d, produces rescue locally for 1<k<2 by continuity. For k>=2 and h>=h_per, contradiction using u=A-k,v=B-k with A,B positive and u²+v²<2: setting s=u+v in (-2,2) yields AB>(k-1)²+((s+2)(2k+s-2))/2>(k-1)², but AB=(k+1)²e^-2h<=(k-1)². Thus no rescue for any legal d and sharp gain-two iff. Independent rational witness k=3/2, e^-h=19/100, cosh d=6/5 gives V=38567/40000<1 versus periodic 1681/1600>1; symbolic identities in verify.py inspected. All assertions are sample-count mean-square, not physical-time Lyapunov exponents.

## originality

PASS

The published 2022 Jin–Wang–Wang study mixes long and short sampling intervals to enhance average allowed interval and gives sufficient stability conditions, while this result addresses iid, equiprobable symmetric perturbations about a *fixed mean* and identifies a sharp universal gain-two criterion and exact no-go. Li et al (2013) considers random sampling through Markovian period switching and LMI tests, not the same scalar quantified if-and-only-if. Relevant 2022 full text inaccessible; best-of-knowledge priority risk explicitly retained.

## value

PASS

This exact bifurcation between achievable mean-square stochastic stabilization and impossible rescue supplies a design boundary for scalar sampled control; distinguishes average performance from robust worst-case conditions and includes an explicit exact viable witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
