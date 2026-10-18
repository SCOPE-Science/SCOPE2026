# Independent mathematical audit

## correctness

PASS

For original map T(x,y)=(y+g(x),-x+g(y+g(x))) with g(s)=mu*s+2(1-mu)s²/(1+s²), primitive period-two orbits force successive x values p≠q, g(p)=q, g(q)=p and both planar y-coordinates zero. The factor g(x)-x=(mu-1)x(x-1)²/(1+x²) and sign algebra yield pq<0 and mu=-(K+2S)/(K-2S)<-1, with exceptional mu=1 explicitly a shear having only fixed periodic points. For mu=-1-t,t>0, independently re-derived and checked full exact sextic factorization (g(g(x))-x)(1+x²)H_t=x(mu-1)(x-1)²Q_t. Q_t(0)<0, Q_t(-1/(1+t))>0, Q_t(-infty)<0 provide >=2 distinct negative roots. Q_t(-u) coefficient signs descending are (-,-,-,-,*,+,-), exactly two Descartes sign changes for any t>0: at most two negative roots including multiplicity; hence exactly two simple negative roots corresponding to two distinct primitive cycles. Independent symbolic scale limits Q_t(sqrt(t)u)/t→16u²-1, e²Q_{e^4}(v/e)→-v²(v²-4)(v²+4), and outer next coefficient 128(w-2)e confirm inner -sqrt(t)/4 and outer -2t^-1/4+2; applying g gives displayed positive partners. All algebra exact SymPy checks independently redone, not merely verifier exit logs.

## originality

PASS

The exact same g_mu rational nonlinearity appears in Ambika & Ambika original primary, but their full article §2–§6 focuses on dissipative a=0.008,b=0.05, mu roughly -0.3 to +0.0039, 4/7/11-period numerics and synchronization, not conservative a=0 for all real mu or exact primitive two-orbit count. Other GM literature analyzed integrable odd nonlinearities or nonconservative settings. No exact threshold mu=-1 plus two contrasting algebraic asymptotic scales was identified in Resultary primary inspection, with historical 1980/1985 inaccessible texts retained as risks.

## value

PASS

This is an exact complete bifurcation classification for primitive 2-cycles of a natural conservative slice of the well-studied Gumowski–Mira recurrence, with sharp mu=-1 existence cutoff and a mathematically distinctive coexistence of an inner vanishing orbit and outer escaping orbit on different sqrt(t) and t^-1/4 scales. The root structure and boundary asymptotics are reusable in dynamics stability/infinity analyses; value is not merely a trivial fixed-point test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
