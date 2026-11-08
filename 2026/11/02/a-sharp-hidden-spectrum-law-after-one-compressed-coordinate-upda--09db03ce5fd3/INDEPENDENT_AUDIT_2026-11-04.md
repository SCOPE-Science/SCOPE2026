# Independent mathematical audit

## correctness

PASS

For 0<s<1, objective derivative along e0+alpha e1 is alpha³+(1-s²)alpha-s, strictly increasing with unique zero alpha=s. At c=(1,s,0), active stored b=(-A,-sA) exactly cancels gradient, true leaf gradient 4sv. A 2x2 Schur complement gives L(L-A)=(L-1)vT(D+LI)^(-1)v; D>=gamma I and |s v_j|<=tau yield a sharp monotone Lstar frontier, attained for D=gamma I and all leaves at threshold. m=r², v_j=1/r gives a fixed three-mode spectral block despite tau->0. Independent symbolic/secular sanity checks corroborate but all-m proof follows inequalities.

## originality

PASS

The foundational 2019 CDFCI algorithm initializes and stores H e0 and drops updates on newly untouched entries. The later 2026 compression paper considers convergence/error under decay hypotheses rather than this reached one-step false-gradient plus dimension-sharp energy frontier. General Schur complement law is admitted as standard. Full 2026 text was inaccessible, recorded as priority risk, not automatic failure.

## value

PASS

PASS. It identifies a method-reachable and quantitatively sharp reliability boundary for coordinate compression of a natural numerical eigenvalue scheme, including the precise aggregate discarded mass rather than an arbitrary tiny instance; it avoids claims about production stopping rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
