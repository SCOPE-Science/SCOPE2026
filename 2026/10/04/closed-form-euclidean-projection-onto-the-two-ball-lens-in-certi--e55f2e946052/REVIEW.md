# Independent mathematical audit

## correctness

PASS

For the nondegenerate lens \(C=B(a,r)\cap B(b,R)\), convexity gives a unique Euclidean projector. If \(z\in C\), the projector is \(z\). If the one-ball projector onto either ball is feasible for the other ball, it is also the projector onto the intersection by the variational characterization. If neither one-ball projector is feasible, the minimizer must have both ball constraints active: otherwise the normal cone would coincide with that of a single active ball, contradicting failure of the corresponding one-ball projection. Subtracting the two sphere equations gives the radical hyperplane \(\langle x-c,e\rangle=0\), where \(e=(b-a)/D\), \(s=(r^2-R^2+D^2)/(2D)\), \(c=a+se\), and the common seam has radius \(\rho=\sqrt{r^2-s^2}>0\). Minimizing distance to this seam is equivalent to maximizing \(\langle x-c,w\rangle\), with \(w=(I-ee^\top)(z-c)\); Cauchy-Schwarz gives \(c+\rho w/\|w\|\). In the both-active branch \(w\neq0\), since \(w=0\) would make all seam points equally nearest and violate uniqueness of projection onto the convex lens. The one-dimensional case has no genuine seam sphere and is exhausted by the interior and one-ball branches.

## originality

PASS

The closest primary geometric source gives explicit projection onto the intersection of two sphere boundaries, including the same radical-hyperplane seam geometry, but it does not solve projection onto the convex intersection of two closed balls with its interior/one-active/both-active branch structure. The motivating stochastic-optimization preprint assumes Euclidean projection onto intersections of certified balls as an oracle; the accessible primary material does not provide the audited active-set formula. Targeted web and Resultary searches for a closed-form projector onto an intersection of two Euclidean balls did not locate a prior implication-equivalent formula.

## value

PASS

The theorem closes a concrete oracle-level gap in a current certified-ball optimization construction and gives a complete dimension-independent formula, including degeneracy boundaries, rather than a numerical approximation. The result is a motivated structural projection lemma; the seam formula alone is known, but the complete convex active-set law is the useful missing object.

The dated certificate retains the supplied scientific assessment, sources and limitations.
