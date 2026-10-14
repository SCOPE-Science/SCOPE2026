# Independent mathematical audit

## correctness

PASS

For a,c,alpha>0 with q=alpha*a and y=x sqrt(a/c), the exact min cap/Polyak rule is F_q(y)=(1-q)y on q<=1/2+1/y² and F_q(y)=y/2-1/y otherwise; formulas agree at the boundary. For 0<q<2, capped steps strictly reduce |y| and once capped remain so; the uncapped condition forces y²>1/(q-1/2)>2/3, on which |y/2-1/y|<|y|. A hypothetical perpetually uncapped orbit would have a nonzero magnitude limit satisfying |r/2-1/r|=r, hence r²=2/3, contradicting the branch lower bound. Therefore every orbit eventually caps and geometrically converges (zero is absorbing). For q>=2, y*=sqrt(2/3) has proposal exactly 2 and F_q(y*)=-y*, producing a persistent 2-cycle; f=c/3, δ=4c/3*(1-1/q) by direct substitution. Independently tested normalized cycle at q=2,2.5,10; verifier.py checks additional representative cases but analytic argument handles all q. RESULT contains nonessential double braces in some displayed TeX, not a different mathematical map.

## originality

PASS

An exact sharp global dynamical classification and persistent loose-floor two-cycle at q=2, beyond general stability-index bounds and exact-minimum interpolation regimes in sources read. The classic GD threshold by itself does not entail this nonlinear capped iteration result.

## value

PASS

The loose but valid component lower bound is an intrinsic SPS modeling choice, and the result pinpoints the universal convergence boundary and an explicit obstruction despite bounded stability-index quantity. This motivated scalar boundary/counterexample meaningfully separates a cited stability estimate from pointwise dynamics, without claiming new stochastic generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
