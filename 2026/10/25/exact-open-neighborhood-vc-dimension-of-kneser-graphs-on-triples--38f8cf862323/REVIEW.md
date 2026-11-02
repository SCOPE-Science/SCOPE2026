# Independent mathematical audit

## correctness

PASS

For KG(n,3) with open adjacency by disjoint triples, complementing neighborhood traces converts shattering to all hit traces. Singleton hit witnesses force a private coordinate p_i in each sampled triple F_i, leaving a residual pair e_i; the resulting loopless multigraph H is allowed parallel edges. A 3-center realizing full hit trace gives a vertex cover of H of size <=3 by replacing any selected private point with a residual endpoint. Therefore every hypothetical seven-shattered family is represented by three core edge multiplicities and a multiset of peripheral incidence vectors (a,b,c), i.e. all multigraphs with seven labeled edges and 3-vertex cover up to index permutation; possible center traces are unions of <=3 vertex stars or edge singletons. Independent enumeration of the complete 9177 profile classes recovered generating-function count [z^7](1−z)^−3 ∏_{s=1}^7 (1−z^s)^−C(s+2,2)=9177, max 124<128 attainable patterns, so no seven-shattered sample for any n. Independent enumeration for m=5/6 found min residual shared vertex counts 3/4. Empty hit trace needs three outside points; private m plus residual 2/3/4 gives sharp n onset m+5 for m<=4, 11 for m=5, 13 for m=6; explicit common-point block constructions realize all 2^m patterns. Accordingly v(n)=0 n=3..5,1 at6,2 at7,3 at8,4 at9,10,5 at11,12,6 at13+. Source verifier source code and independent profile generator examined; exhaustive reduction, not small-n extrapolation, proves uniform bound.

## originality

PASS

Qualified PASS: Adler–Benediktsson–Macpherson proved VC dimension at most four for Johnson adjacency (for triples overlap in two elements) and three for Hamming, a different edge relation from disjointness. Coudert et al compute graph VC dimension algorithmically, typically closed neighborhoods, but do not state this all-n open-neighborhood Kneser step function. Generic KG(n,3) is not strongly regular, so a recent SRG-specific classification does not cover arbitrary n. Seven-edge obstruction and threshold classification are the surviving candidate original result.

## value

PASS

An exact complete n-dependent VC dimension for the natural fixed-rank Kneser graph neighborhood system, including first saturation at 13 and a universal seven-sample obstruction, is a mathematically motivated uniform finite classification. Private-coordinate and 3-cover reduction plus a complete bounded obstruction expose structural reasons; not merely recomputing a small graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
