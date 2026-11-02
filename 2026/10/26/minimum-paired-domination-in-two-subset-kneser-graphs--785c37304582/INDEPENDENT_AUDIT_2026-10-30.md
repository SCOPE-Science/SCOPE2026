# Independent mathematical audit

## correctness

PASS

For a selected 4-edge K_n subgraph H, an undominated outside pair is exactly a two-vertex transversal of H; any selected transversal would be isolated in the Kneser induced subgraph and contradict matching. Therefore paired domination is equivalent to vertex-cover number >=3 plus induced perfect matching. Decomposing all four-edge simple graphs into components leaves four cover-number-3 candidates, of which K3⊔K2 gives K1,3 in the disjointness graph, no perfect matching. Other three types have displayed perfect matchings and automorphism orders 4,16,384. No 2-set can dominate. Explicit exhaustive independent Python construction of KG(n,2), direct domination and recursive matching found optimum counts n4=1,n5=125,n6=180,n7=1575,n8=7665; the all-n classification follows from the structural proof, not this finite test. Complement-type census gives n5 orbit sizes 5,60,60.

## originality

PASS

Best-of-knowledge new classification/count for paired minima; earlier KG(n,2) ordinary and k-tuple domination results do not impose selected perfect matching.

## value

PASS

Classifies all optimum paired-dominating configurations for every KG(n,2), not just the minimum integer, with three symmetry types and explicit polynomial in binomial coefficients. The natural matching constraint models two-at-a-time internal redundancy and the n=5 Petersen boundary is a nontrivial exceptional orbit census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
