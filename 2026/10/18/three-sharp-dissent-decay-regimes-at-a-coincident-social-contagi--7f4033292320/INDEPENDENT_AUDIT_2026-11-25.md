# Independent mathematical audit

## correctness

PASS

The unit simplex is invariant, i remains positive, and s and d are positive at every positive time even for admissible boundary data (at s=0 the derivative is m; with s,i>0 the source for d is positive). The bound i'<=-mi² and scalar comparison for d imply convergence to (s,i,d)=(1,0,0). If the integral of d were finite, solving the first equation for i would give i~1/(mt), whereas d'+md>=asi with s tending to 1 would force an unbounded integral on the right. Direct independent differentiation gives, for r=i/d² and dτ=d dt, r_τ=r[(m-k)-r(2as+(2k-m)d)] and (log d)_τ=-m+r[as+(k-m)d], equivalent to RESULT.md (2)–(3). The quadratic coefficient tends to 2a. Thus for k<m, logistic comparison gives r→(m-k)/(2a); for k=m the reciprocal of r has slope tending to 2a in τ. The d equation then yields the stated limits of td and, in the marginal case, τ~(log t)/m, giving the exact physical-time infected constants. For k>m the exponentially decaying r makes both logarithmic corrections integrable, yielding positive finite limits R=lim r e^{(k-m)τ} and D=lim d e^{mτ}, and t~e^{mτ}/(mD). For example, starting the clock at zero with fixed d(0)>0 gives R<=i(0)/d(0)² and D>=d(0), so the positive physical-time amplitude is at most m^(-p)i(0)d(0)^(-p) for p=1+k/m; hence it cannot be universal. The checks are analytic and specific to the frozen ODE and its initial-data domain. The supplied verify.py and requirements.txt were inspected but not executed; finite trajectory diagnostics would not establish the limits, and the frozen metadata records no formal verification or expert attestation.

## originality

PASS

The compartment equations and threshold coincidence are supplied by the original model and receive no novelty credit. Inspection supports the distinct claim of global, sharp relaxation on that coincident surface, particularly the marginal logarithmic law and the positive high-conversion amplitude with variable power.

## value

PASS

The critical surface is determined by coincident transitions in a published dynamical model, not an arbitrary parameter slice. It supports distinct long-time laws even though the limiting state is the same. The quantitative borderline between universal quadratic relaxation and an initial-data-dependent power law is scientifically useful; the theorem does not extrapolate to stochastic networks or claim empirical validity of the compartments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
