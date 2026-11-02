# Independent mathematical audit

## correctness

PASS

Use the original p-strong Roman convention f(u)>=1+ceil(|N(u) intersect B0|/p) for every zero with a neighbor u and labels bounded by 1+ceil(Delta/p). On K_{a1,...,ar} a selected positive defender in part i sees Z-z_i zeros. Either a sole defender lies in a zero-free part or two defenders in distinct parts cover all zeros; reducing all other effective defenders to 1 cannot hurt coverage. In the sole case, zeroing positives outside its part yields a_i+ceil((N-a_i)/p) minimized at m. In the two-defender case with t positive units in other parts, weight F_ij(t)=2+t+ceil((N-a_i-1-t)/p)+ceil((N-a_j-1-t)/p). F(t+p)=F(t)+(p-2), and for 0<=s<p only s=1 can reduce F(0), exactly if both numerator residues are 1 mod p. r>=3 ensures t=1 is available. The closed min formula follows. Independent optimization over all zero-count profiles and all subsets of defender parts matched the formula in 517 small (part-profile,p) cases; K_(5,5,5),p=4 gives 7. The proof and the capacity/boundary hypotheses, not finite checks, cover all r>=3 and 3<=p<=N-m-1.

## originality

PASS

The original primary p-strong Roman article, read in full relevant sections, proves r=2 and general bounds, but not complete multipartite r>=3 or the mod-p one-unit saving. Previously published ordinary and total strong Roman multipartite formulas are p=2 and/or impose a distinct support condition. This distinction is mathematical, not just terminology.

## value

PASS

The exact weight for every multipartite part-size profile and nontrivial integer p is a natural domination invariant and is computed in O(r^2). The residue-dependent two-defender configuration beats the established upper bound; for fixed p balanced tripartite graphs improve the one-defender construction by linear order in part size. This is substantive beyond finite experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
