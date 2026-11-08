# Independent mathematical audit

## correctness

PASS

In K_{2,n}, each leaf yields two orientation bits. Only local patterns 10 and 01 are opposite hub-to-hub directed two-paths, and a directed cycle exists exactly when both occur on different leaves. Hence the class is the union of two 3^n product languages with 2^n overlap, giving |A|=2*3^n-2^n. The residual ternary state (u,a,b) has an exact one-query Littlestone recurrence with independent three-state two-bit factors of rank one after a hub-path signature is forced. Strong induction solves the recurrence F=max(u+a,u+b,ceil((3u+a+b)/2)). Initially Ldim=ceil(3n/2). Static shattered coordinates are exactly forests, giving VCdim=n+1. Independent recurrence verified 4096 states and direct concept-class shattering recursion verified n=1..5, with correct orientation counts.

## originality

PASS

Kozma–Moran 2013 establishes static orientation shattering/forest correspondences; Walker 2022 gives general tree and Littlestone dimension bounds, but neither computes adaptive shattering for acyclic K_{2,n}. The exact residual rank law and its growing gap on 2-vertex-connected planar bicliques are not present in inspected primary statements. Broader online orientation-learning models and unnamed extremal class theorems remain priority risks.

## value

PASS

Shows that adaptive and nonadaptive shattering genuinely separate by an unbounded amount even on 2-vertex-connected planar bipartite graphs. The exact residual state formula is a structural theorem for every n, not a numerical fit, and can serve as a reusable online-learning benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
