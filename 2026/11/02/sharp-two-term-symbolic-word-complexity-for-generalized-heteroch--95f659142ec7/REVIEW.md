# Independent mathematical audit

## correctness

PASS

An admissible bracket string corresponds uniquely to a word skeleton of m labeled pushes and unlabeled pops. Free closing labels occur exactly at new maxima of pop-minus-push walk, giving weight m^H. With upward probability 1/(m+1) and downward m/(m+1), first hitting generating function f=pz+qzf² and the tail-sum identity for m^H give U=(1-f)/[(1-z)(1-mf)]. Analytic f at z=1 has f(1)=1/m, f’(1)=(m+1)/(m(m-1)), giving pole coefficients ((m-1)²)/(m(m+1)) double and 4/(m+1) simple. Square-root branch points at modulus (m+1)/(2sqrt(m))>1 give O((2sqrt(m))^n n^-3/2). Independent complete word enumerations for m=2,n≤8; m=3,n≤6; m=4,n≤5 matched independent skeleton sum. Proof covers all m,n; finite count is corroboration.

## originality

PASS

Best-knowledge PASS with substantial caveat: Dyck shift coding and entropy are known; 2018 paper numerically anticipated 3+3/n. Inspected older Dyck orbit-counting primary text explicitly treats periodic points, not finite-language words. A long-established but unindexed formula for Dyck-shift word complexity could cover this claim; further specialized symbolic dynamics review advisable.

## value

PASS

Exact full language enumeration rather than periodic orbits or leading entropy is a natural dynamical invariant. The proof replaces previously numerical ratio evidence with a general all-m sharp coefficient and finite-length generating function, useful for symbolic state-count asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
