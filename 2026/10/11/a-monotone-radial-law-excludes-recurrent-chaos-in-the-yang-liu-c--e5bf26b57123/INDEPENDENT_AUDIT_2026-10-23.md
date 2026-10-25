# Independent mathematical audit

## correctness

PASS

For the displayed polynomial vector field F=(yzw,ay−xzw,−bz+xyw,−cw+xyz), R=x²+y² satisfies L_F R=2x(yzw)+2y(ay−xzw)=2ay² for every state and any real a,b,c. For a≠0, R is strictly monotone along any time interval on which y is not identically zero. If p is positive-time recurrent, the monotone scalar R(φ_t(p)) returns arbitrarily close to its initial value, hence is constant on [0,∞); continuity and the identity imply y(t)=0 throughout the recurrent orbit. There z(t)=z(0)e^{−bt} and w(t)=w(0)e^{−ct}; when b,c>0 recurrence forces z(0)=w(0)=0, and the entire orbit is the equilibrium (x,0,0,0). For a compactly supported invariant probability μ, generator invariance for R yields 0=∫L_FR dμ=2a∫y² dμ; continuity and positivity give supp μ⊂{y=0}. Generator invariance for z² and w² then gives 0=−2b∫z²dμ and 0=−2c∫w²dμ, so supp μ⊂{(x,0,0,0)}. These generator tests are justified for polynomial observables on compact flow-invariant support. Independent SymPy calculation reconstructed L_FR=2ay², (L_F z²)|_{y=0}=−2bz², (L_F w²)|_{y=0}=−2cw², and F(x,0,0,0)=0. The inspected verify.py checks only the first identity, not the recurrence/measure arguments; those latter steps were checked analytically. No assertion concerns a=0, b≤0, c≤0, non-compact measures, infinite-time numerics, or unbounded/non-recurrent orbits.

## originality

PASS

Best-of-knowledge PASS for a model-specific global no-recurrence obstruction: the exact algebraic Lyapunov identity and its consequences were independently reconstructed, then compared at statement/implication level with the introducing Yang–Liu paper, the same-system Rech follow-up, Resultary exact-equation searches and stronger analogous results for other flows. The available primary passages report chaos rather than the obstruction; the same-result Resultary hit is self-indexing and not independent earlier priority. Generic monotonicity principles do not identify this R for the printed system. Both full same-system articles remained inaccessible after lawful retrieval attempts; prior equivalent treatment remains a material priority risk and non-detection is not novelty proof.

## value

PASS

PASS because the compact invariant-state obstruction is not just an arbitrary algebraic check: it contradicts the specifically published interpretation of positive-parameter numerical attractors as hyperchaotic recurrent sets for this exact cubic ODE. One simple global identity rules out all non-equilibrium recurrent points and compact stationary distributions simultaneously over a three-parameter sign domain, with an explicit diagnostic for distinguishing long transients or numerical drift from true bounded recurrent dynamics. The computation is elementary, but its precise source-relevant dynamical correction and parameter scope make it a motivated mathematical obstruction rather than a textbook restatement. Value does not imply a general theorem about other chaotic flows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
