# Independent mathematical audit

## correctness

PASS

Direct substitution into Condat–Richtárik RandProx-LC Algorithm 4 with scalar K=1, b=g=0, f(x)=µx²/2, γ=1/µ and unbiased Bernoulli R(z)=Iz/p gives xhat=−γu, u_next=(1−aI)u and x_next=−γ(1−aI/p)u. Independence yields q=1−pa(2−a), c=1−2a+a²/p; mean-square stability iff 0<a<2 (given u0≠0), and the accumulated primal-squared feasibility S=c/[pa(2−a)]. Differentiation yields S'=2((1−p)a²+pa−p)/(p²a²(2−a)²), one strictly increasing numerator root a*=2√p/(√p+√(4−3p)) in (p,1), hence unique global optimum. As p→0 S(a*)~p^(−3/2) versus S(p)~(1/2)p^(−2) and S(1)~p^(−2). Independent SymPy differentiation plus all 15 separate short Bernoulli-trees corroborated; the iid recurrence/geometric series proves the full horizon.

## originality

PASS

Condat–Richtárik arXiv:2207.12891 Algorithms 4/5 and Theorem 4 already give RandProx-LC and the general sufficient γτ≤p after specialization. The user-visible finding is neither a new algorithm nor a global stability recommendation: it proves the scalar exact stability interval and optimizes a distinct cumulative constraint-violation criterion outside the sufficient source region. Mishchenko et al. ProxSkip 2022 optimize communications/iteration coupling, not this free scalar dual step at fixed p. Originality remains subject to possible equivalent one-dimensional stochastic splitting analyses.

## value

PASS

The mean-square rate alone can hide rare but costly primal constraint excursions. A unique cumulative feasibility optimizer and asymptotically unbounded risk gain over both the general certified step and rate-optimal dual step provide a sharp, motivated algorithmic boundary example, even though the instance is scalar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
