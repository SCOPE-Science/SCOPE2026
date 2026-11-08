# Independent mathematical audit

## correctness

PASS

The graph distances are 2 between matched endpoints, 3 between distinct subdivision vertices, 2 between each subdivision vertex and other original vertices, and 1 on all remaining distinct original pairs. On the zero-sum hyperplane, endpoint-antisymmetric directions have eigenvalue -2^p, unmatched-original contrasts eigenvalue -1, and the paired-block standard modes form r-1 identical 2x2 quadratic blocks S=[[2a-4,-2(a-1)],[-2(a-1),-b]], a=2^p,b=3^p, det S=2[b(2-a)-2(a-1)^2]. This determinant has one root in (0,1), by monotonicity of 2(a-1)^2/[b(2-a)]. At that root standard modes each contribute a single equality direction. Crucially, the possible global orbit-constant block is strictly negative there: for t=m-2r>0 its leading principal entry and determinant 2r(1-c)k+(r/t)(6-2c+4(r-1)k) are positive with c=a-1, k=2c-(b-1)>0; if t=0 the restriction is -2r[3-c+2(r-1)k]x². This excludes extra nullity. Li-Weston negative-type interval then gives strictness for smaller powers and the standard-mode positive direction rules out every higher power. Schoenberg centering identifies embedding dimension from rank. Independently reconstructed shortest paths and centered powered-distance eigenvalues on 16 (r,t) graphs, at exponents below/at/above p*; the family proof is analytic.

## originality

PASS

Obata and Zakiyyah (2018), Theorem 3.9, determine the unpowered quadratic embedding constant when disjoint edges are deleted from a clique, with no new vertices; their r>=2 value is zero. Here each edge is replaced by a two-edge path, enlarging the metric and introducing distance-three new-vertex pairs, so their deleted-matching formula does not imply the power threshold, endpoint kernel, or Hilbert dimensions. Lou-Obata-Huang and Mlotkowski-Obata study ordinary QEC for joins, but the subdivided-matching graph has no nontrivial complete-join decomposition. Li-Weston gives the general negative-type interval theorem, not this exact root. Best-knowledge PASS with possible historical metric-spectrum equivalence risk.

## value

PASS

A matching is a canonical set of independent edge modifications to a dense graph, and subdivision is a natural metric operation distinct from deletion. That a two-parameter family has an identical nontrivial negative-type exponent while its endpoint equality space grows exactly with r is a robust structural property of Hilbert snowflake embeddability, not a table lookup or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
