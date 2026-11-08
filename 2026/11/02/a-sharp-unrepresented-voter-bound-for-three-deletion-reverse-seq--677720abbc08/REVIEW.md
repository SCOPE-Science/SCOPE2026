# Independent mathematical audit

## correctness

PASS

One-voter scoring marginal losses are 1/t_j for currently approved deleted candidates and b/(k t_j) for the average surviving winner. Since each actual deletion minimizes loss, five aggregate differences g01,g02,g1w,g12,g2w are <=0. The source supplies a nonnegative rational multiplier vector and explicit 8x2 nonnegative residual table, giving the first deletion bound; later deletions each <=1/(k+1) by two pointwise inequalities. An independently written rational checker verified the dual inequality for all eight deleted-ballot patterns, 0<=b<=k, 2<=k<=40 (finite corroboration only). The displayed symbolic residuals are rationally nonnegative for all integers k>=2 and b>=1. The source constructs integer profiles with n=k(3k+1)(k+2) and attains equality under allowed ties; direct fresh rational scoring verified the 252-voter k=6 example has unique minimum loss x,a,b in order: (62/3 vs127/6), (31 vs63/2), (33 vs100/3). Comparing B_k with 1/k gives exactly k=2..5 guaranteed and k>=6 counterexamples; k=1 follows from zero-loss unsupported alternative.

## originality

PASS

Aziz 2017 proves JR under at most two deletions and gives failure when at least seven deletions; inspected Proposition 2 is not this exactly-three result. Papasotiropoulos 2026 (arxiv 2609.35331) claims three-deletion EJR counterexample and approximate EJR bounds, but full text was inaccessible through the attempted arxiv/OA paths and a further authorized retrieval was safety-blocked. Only its indexed abstract and source package description were available; cannot assert whole-document NON_COVERING. An EJR counterexample need not be a JR counterexample. Best-of-knowledge exact three-deletion fractional bound survives inspected primary Aziz material, with a material priority risk from 2026 source.

## value

PASS

The first sharp quantitative loss fraction with exactly three deletions, its extremizers and the precise JR seat cutoff address the natural open gap between two-deletion guarantees and many-deletion counterexamples. The strict 252-voter witness and dual certificate make the natural bound inspectable without relying on an arbitrary tiny electorate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
