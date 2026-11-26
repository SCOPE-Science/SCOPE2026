# Independent mathematical audit

## correctness

PASS

For a zero-ended edge a_i b_j the only omitted vertices are a_j,b_i. A violation requires their two opposite-shore labels at distinct indices to carry all but at most one unit of the total weight, and their respective matched partners to be zero. Thus weights >=6 cannot fail. At weight 5 the omitted labels are 2,2 and the remaining 1 uses a third index. At weight 4 the omitted labels are 2,2 or 2,1, with a third index in the second case; keeping both orientations and accounting for the repeated opposite-shore 1 gives n(n-1)(3n-5). At weight 3 a 2 may serve alone or with an opposite 1; with only ones, two omitted opposite-shore labels and the one remaining label give the three-distinct-pair pattern. These give 4n(n-1)+n(n-1)(n-2). At weight 2 a singleton 2 or two ones on distinct indices admit a witness; when both ones are on the same shore, the existence of a spare index uses n>=3. Ones on a matched pair cannot be omitted by a zero-ended edge. At weights 0 and 1 there always exists a zero-ended edge. Counting yields the six subtractions as claimed. In K_n,n the neighborhood union of each edge is the entire vertex set; weights 0 and 1 also have a zero-ended edge, giving the claimed comparison. `python3 /workspace/reviews/reproduce.py 2` independently forms the open-neighborhood unions from adjacency and tests all 66339 labelings for n=3,4,5; the invalid coefficients and exact minima match. The frozen n=3..6 output was read and the checker inspected, not executed; its n<=30 pattern arithmetic is not an independent exhaustion of feasible labelings.

## originality

PASS

The bounded comparison supports the stated edge-based crown weight enumerator as distinct. Prior statements on the same graph or with Roman {2} in their title use different conditions; the primary paper that uses the right predicate does not provide an applicable counting theorem in the decisive passages inspected.

## value

PASS

A crown is a natural regular bipartite perturbation of a biclique. The full enumerator quantifies exactly where deletion changes feasible labelings, while the minimum is unchanged. The exhaustive symbolic obstruction counts give an all-orders result and a minimum-structure classification, not a small-instance calculation or a relabeling of a vertexwise result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
