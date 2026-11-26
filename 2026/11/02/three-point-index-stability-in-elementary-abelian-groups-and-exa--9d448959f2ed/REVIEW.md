# Independent mathematical audit

## correctness

PASS

The exact independent-domination criterion follows from overlap of translates and the condition for adding an outside vertex. In characteristic two and in the collinear ternary case D is the entire difference subgroup, so the subfactors are exactly transversals. In the noncollinear ternary case the only allowed nonzero differences within the nine-element difference subgroup are the two nonzero elements of <a+b>; a maximal choice therefore fills exactly one of its three cosets in each outer coset. This proves both ternary sizes and all counts of actual subsets. Rank one in characteristic two is vacuous. For exceptional cyclic orders independent enumeration of all anchored triples and all candidate subsets gives the claimed table; anchoring by translation does not change the difference set or subfactors. In the plane the fiber witnesses work because no nonzero forbidden difference has zero projection and the projected sets are independently dominating; independently reconstructed greedy witnesses have sizes (5,7), (7,13), (22,31) against the fiber witnesses respectively. For p>=13, independence for A={0,1,3} requires each cyclic gap to be at least four, and domination requires it to be at most seven. Thus exactly 4k<=p<=7k is needed for k>=2. At p=13,17,19 the two displayed sizes work; for p>=23 write p=5k+s with 0<=s<=4, k>=4; both k and k+1 meet the inequalities. These negative witnesses lift by independent choices in difference-subgroup cosets, so no larger dimensions need enumeration. Bounded checks were independently written and run: replay python3 /workspace/branches/01139dfa-c2e7-448b-bf77-7b2f503dcd2a/record1_independent.py with smoke, finite, or gaps (SHA-256 c5737b7f3526d9080e04a2309c73a2b21e4c1ad30cde6813f1cfca95409c759a); no frozen script was executed.

## originality

PASS

The supported distinct claim is the uniform all-prime/all-rank three-point classification and exact binary and ternary subfactor descriptions and counts. The independent-set representation, particular small examples, and a fixed cyclic support classification are not credited as new here.

## value

PASS

The result answers a motivated three-point extension problem uniformly in prime and rank. It isolates exactly the two structural positive families and three exceptional cyclic cases, exhibits the rank-two boundary, and describes and counts every subfactor in the positive binary and ternary families. That gives both a decision criterion and an exact packing description, not merely a finite recensus of known examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
