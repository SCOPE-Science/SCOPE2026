# Independent mathematical audit

## correctness

PASS

For normalized standard LSV invariant density and fixed 0<gamma<1, branch renewal h(x)=sum_n q(g^n(x))(g^n)′(x) with q(u)=h((1+u)/2)/2, q0=H/2, q1=H1/4. Abel coordinate A(f(x))=A(x)-1 has expansion x^(-gamma)/(gamma b)-(gamma+1)log(x)/2 + [(gamma+1)(2gamma+1)b/(12gamma)]x^gamma+..., b=2^gamma. I independently expanded the Abel equation in z=x^gamma and checked coefficients 0, z, z² vanish identically in symbolic gamma,b. Euler--Maclaurin on W=-q(X)X′ yields integral +W(t)/2-W′(t)/12 plus bounded higher derivative tail, hence h=-A′∫_0^xq +q/2+qA′′/(12A′²)-q′/(12A′)+..., the Bernoulli sign and x^gamma coefficient match the exact RESULT proof. This gives H x^-gamma/2^(gamma+1) +(gamma+2)H/4 +H1 x^(1-gamma)/2^(gamma+3) -gamma(gamma+1)2^gamma H x^gamma/12 +O(x^min(1,2gamma)); the two corrections coincide gamma=1/2. The derivative bounds for W and differentiable Abel remainder were asserted based on Korepanov--Wei--Wormell but its full primary text was inaccessible this run, making that critical imported regularity lemma a recorded verification risk. No parameter-endpoint uniformity or nonzero H1 for gamma>1/2 is claimed.

## originality

PASS

The nearest Korepanov--Wei--Wormell 2026 preprint supplies an analytic Abel coordinate, exact density renewal and leading terms M0x^-gamma plus M1x^(1-gamma) with bounded residual according to the inspected source package; the proposed independent extraction of constant intercept and x^gamma term is more specific. However its original source full text could not be retrieved, so its Section 6 was not newly reread; if their omitted bound actually encodes these coefficients, coverage could change. Bonanno--Lenci addresses leading density order, not these coefficients. Resultary query returned only focal same-formula record, not independently prior. This is conditional best-of-knowledge priority with a material explicitly named high-relevance access risk.

## value

PASS

The constant intercept and sign-fixed fractional neutral term refine the singular invariant density and mark a universal exponent collision at gamma=1/2 in a canonical intermittent dynamical system. These local coefficients are natural invariants of neutral transfer asymptotics and may be needed to calibrate refined density computation and error estimates, even without a general map theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
