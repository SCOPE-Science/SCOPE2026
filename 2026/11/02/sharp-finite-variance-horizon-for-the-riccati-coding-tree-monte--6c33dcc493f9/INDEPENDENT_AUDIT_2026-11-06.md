# Independent mathematical audit

## correctness

PASS

The original coding-tree mechanism has deterministic child-code maps Id→(f), f→(f,f'), f'→(f,f''), f''→(f,0), 0→(f,0), with independent Exp(λ) lifetimes and positive weights. Tonelli on nonnegative finite-generation expansions gives second-moment ODE I'=λI+F/λ, F'=λF+FC/λ, C'=λC+4e^{λt}F/λ, I(0)=a²,F(0)=a⁴,C(0)=4a². Transform x=(e^{λt}-1)/λ² and F=e^{λt} Fhat,C=e^{λt} Chat to get Fhat_x=Fhat Chat, Chat_x=4Fhat and invariant Chat²-8Fhat=8a⁴. Explicit solution using b=2√2 a², R=(3-2√2)e^{bx} is Chat=b(1+R)/(1-R), Fhat=b²R/[2(1-R)²]. Blowup x*=κ/a², κ=log(3+2√2)/(2√2), corresponds to t2(λ)=(1/λ)log[1+κλ²/a²]. Near x*, Fhat~1/[2(x*-x)²], so the integral for I blows up λ/{2e^{λt2}(t2-t)}; Tonelli rules out revival of finite second moment after t2. First-moment renewal still gives a/(1-at) for t<1/a. Optimize t2 by z=1+κ(λ/a)²; derivative sign 2(1-1/z)-log z has one root z*>2, yielding optimal rate≈2.508456434a and max horizon≈0.6353007524/a. Independent integration of the unreduced three-moment ODE agreed with explicit formulas at 70% of t2 for three parameter pairs; direct bisection checked the unique rate optimum. Finite ODE checks do not prove boundary integrability.

## originality

PASS

Penent–Privault introduce exactly this exponential-time derivative-code estimator and its first-moment representation, including Riccati examples at time 1/2. Their inspected source does not determine second-moment divergence and unique optimal constant-rate finite-variance horizon. Different Butcher tree-size sampling is not this clock law.

## value

PASS

A precise, natural practical reliability question for an established unbiased Monte Carlo integrator is answered: the finite-mean regime contains a nontrivial unavoidable infinite-variance interval for every constant clock rate, with an optimized sharp numerical threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
