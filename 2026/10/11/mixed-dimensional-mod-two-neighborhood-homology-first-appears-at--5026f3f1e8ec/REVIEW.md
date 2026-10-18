# Independent mathematical audit

## correctness

PASS

The triangular graph T_n=L(K_n) has C(n,2) edge-vertices and an open neighborhood of each edge comprising exactly 2(n−2) other incident edges. The package verify.py enumerates every nonempty subface of all these neighborhoods for n=3..7 and reduces every F₂ simplicial boundary column, not a random sample or approximate rank. I separately regenerated neighborhoods directly from the defining adjacency and used independent GF(2) pivot elimination. Reduced Betti profiles: n=3 H̃1=1; n=4 H̃1=1; n=5 H̃3=11; n=6 H̃3=91; n=7 H̃3=246 and H̃4=7, no other nonzero degrees. For n=7 full face vector (21,210,1190,3780,5187,4410,2520,945,210,21) and boundary ranks (20,190,1000,2534,2646,1764,756,189,21) give the claimed Betti numbers exactly. All five n cases are exhausted; since domain is the discrete interval 3≤n≤7, the 'first' statement is complete there. No integral torsion, homotopy or n≥8 result is inferred.

## originality

PASS

Best-of-knowledge PASS for the exact finite triangular-graph open-neighborhood mod-two profiles and first mixed-degree occurrence at T7. Inspected general Matsushita π1 correspondence and Fröberg's full primary neighborhood families; neither reported a result subsuming the exact L(K3)..L(K7) calculation. Same Resultary entry is self evidence only. Other graph classes and higher-depth homology do not imply these Betti values.

## value

PASS

T_n=L(K_n) is a canonical strongly regular/line-graph family, and the first loss of single-degree neighborhood homology is a meaningful exact cutoff, with a mixed-dimensional F₂ signature H̃3=246, H̃4=7. Exhaustive exact ranks across every preceding n, rather than an arbitrary single tiny invariant, make the threshold a reusable benchmark for graph-complex topology. It does not pretend to solve the all-n census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
