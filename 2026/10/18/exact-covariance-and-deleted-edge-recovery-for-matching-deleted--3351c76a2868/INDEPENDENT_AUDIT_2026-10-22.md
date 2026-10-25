# Independent mathematical audit

## correctness

PASS

Actual RESULT.md gives a disjoint anchored-coordinate stratification: ordinary range≤1 charts with total volume N and exceptional range>1 charts indexed by 2m oriented missing edges, each carrying beta variable L=2−range with density (N−1)L^(N−2). Exceptional volume 2m/(N−1) and total T/(N−1) follow with no overlap away from boundaries. Conditional independent uniform remaining coordinates yield EL²=(N−1)/(N+1), E(2−L)²=(N²+3N+4)/(N(N+1)), so mixing ordinary covariance (N+2)/(12N)P with exceptional terms gives exactly A=(N−1)(N²+3N+2m+2)/(12(N+1)T), B=(N²+3N+4)/(N(N+1)T), C=(N−1)/(6(N+1)T). An independent SymPy simplification checked all three coefficient identities, without relying on stored logs. The four orthogonal H-subspaces have top eigenvalue A+B−C on matched antisymmetric differences; B>C strictly for every N≥3, including s=0 and m=1. U_ab=−1/2 exactly on missing pairs. The exact lattice/Ehrhart checker was inspected: it covers only eight N≤6 cases and is not the infinite proof.

## originality

PASS

Prior Lipschitz-free and symmetric edge polytope texts develop extreme points, faces, normalized volume/Ehrhart and volume products, not centered interior covariance reconstruction for matching-deleted complete graphs. The K_2,2 covariance instance and anchored volume are known supporting special cases; they are not separately claimed. Resultary matching and John/Löwner-ellipsoid findings concern different invariants (extreme enclosing ellipsoid vs uniform interior second moment) and do not imply the exact deleted-matching eigenspace theorem. The novelty is the complete (N,m) covariance and inverse recovery of the labeled missing matching, subject to bibliographic risk.

## value

PASS

Recovering a graph’s missing labeled edges solely from the top eigenspace of a canonical covariance on uniform Lipschitz potentials is a mathematically motivated inverse-metric problem. Complete exact rational eigencomponent classification across every allowed N,m is not an arbitrary finite table or routine moment alone; strong spectral separation is meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
