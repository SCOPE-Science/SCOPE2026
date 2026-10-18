# Independent mathematical audit

## correctness

PASS

Derived step M(a,b)=[[1−a−a²/(2b),a²/(2b)],[1,0]], then P=M(y,x)M(x,y), det=xy/4 and trace=1−L+L²/2+xy/4. Quadratic Schur conditions give decay iff 0<L<2, a simple unit root at L=2, and a root >1 for L>2. The discriminant factors nonnegatively; the larger root decreases with d=xy/4 at fixed L and AM–GM maximizes d uniquely at equal steps. Equal-step scalar characteristic roots provide the global lower bound 1/3 with equality at 2/3; exact matrix gives P=I/3. Direct singular limit yP(L−y,y)→(L²/2)[[−1,1],[−1,1]] establishes operator norm L², with stable limiting spectral radius 1−L+L²/2.

## originality

PASS

Best-of-knowledge PASS for the combined exact two-period Floquet threshold, unique optimal damping and transient law; pre-1990 variable-step Adams/Nordsieck sources are highly relevant but only abstracts were accessible, so hidden equivalent special cases remain a material risk.

## value

PASS

Exact sharp stability/damping boundaries and arbitrarily large stable transients are useful for interpreting real-negative scalar AB2 timestep control; the contrast between asymptotic rate and norm amplification is nontrivial even for this natural simple scheme.

The dated certificate retains the supplied scientific assessment, sources and limitations.
