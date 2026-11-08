# Independent mathematical audit

## correctness

PASS

From Q_0=empty, all naturally updated states are unions of whole tripartite classes. The first nonempty class requires >=m+1 targeted other-class vertices; simultaneous two-class activation costs >=m+2; all three immediately costs ceil[3(m+1)/2]>=m+3 for m>=2. Under cost <=m+2, the one-class case leaves <=1 intervention, unable to produce two naturally positive classes; the two-class case leaves none, and unforced updates alternate two classes to the third and then empty. The upper schedule targets class C plus one vertex in A,B (m+2), then one C vertex, yielding all classes naturally positive (m+3). For m=1, three is necessary and sufficient. Static initial-only activation iff a+b,a+c,b+c >=m+1, minimum ceil[3(m+1)/2]. We independently solved exact labelled-state Dijkstra for m=1,2,3, obtaining (3,5,6); all-m proof is structural.

## originality

PASS

Qualified best-of-knowledge originality: compared exact claim and possible implications with relevant primary literature and two actual semantic published-record searches; a failed search is not proof of novelty. Published timed-target-set upper/lower inequalities can neither imply the sharp T(m) nor the gap U(m)-T(m); the described construction and first-activation lower bound are additional. An unindexed equal-family result is a remaining risk.

## value

PASS

The exact temporal cost and initial-only cost quantify a strict, unbounded additive and asymptotically one-third relative improvement from timing interventions on a natural dense graph family, rather than a parameter renaming. It separates synchronous non-progressive dynamics from irreversible diffusion and establishes a sharp integer threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
