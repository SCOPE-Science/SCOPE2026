# Independent mathematical audit

## correctness

PASS

Checked exact fractional H-description of bipartite k-matching polytopes against Torres, arXiv:2306.11910, Theorem 3.1, and verified Hall saturation by biregular degree counting. For k<p the affine hull has sum_e x_e=k and projected support normals squared 1-1/m, a(1-1/p), b(1-1/q); summation gives coordinate, left, right candidate bounds, with the right strictly weaker for p<q. Uniform x=k/m saturates the minimum, and equality constraints prove the entire locus and dimension m-p in the left-dominated phase, unique otherwise including ties. At k=p the affine hull has independent left-star equalities, projected norms sqrt(1-1/a) and sqrt(b(1-1/a)), giving coordinate/right radius competition. Right equality yields lambda*1+(1-a*lambda)*T_G, affine dimension m-p-q+1 by connected signed-incidence rank. For vertex-edge incidence support of K_n, explicitly substituted p=n,q=n(n-1)/2,m=n(n-1), giving n4 radius=1/sqrt12, dimension3, and n>=5 unique center with radius 1/sqrt((n-1)(n-2)); n5 radius also 1/sqrt12. Read check_inballs.py, testing LP support normal distances over 132 numerical cases, a corroborating bounded check not a universal proof.

## originality

PASS

Known exact k-matching H-descriptions (Torres all bipartite and Gill–Linusson complete bipartite) are correctly treated as inputs, not new. The new subject is intrinsic standard-Euclidean inball radius and full center locus for arbitrary connected simple biregular p<q supports, including the cycle-rank center dimension and sparse-incidence transition. Resultary returned related graph-polytope inradius phases, root/symmetric edge polytopes, and a square-assignment incenter indexed result but no broader exact biregular sparse matching center theorem. A plausible unindexed graph-supported transportation incenter characterization is an explicit risk.

## value

PASS

A parameter-sharp geometric classification on arbitrary connected biregular graph supports distinguishes unique center from graph cycle-space transportation families. The incidence(K4) to incidence(K5) exact same-radius but nonunique-to-unique collapse makes a motivated sparse-support phase transition, not a gratuitous finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
