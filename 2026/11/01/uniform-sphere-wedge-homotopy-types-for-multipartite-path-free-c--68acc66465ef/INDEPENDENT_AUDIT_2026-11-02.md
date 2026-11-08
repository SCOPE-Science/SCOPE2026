# Independent mathematical audit

## correctness

PASS

For a complete multipartite induced subgraph on k vertices with maximum part occupancy M, the longest simple path has min(k,2(k-M)+1) vertices: an alternating arrangement achieves the upper bound using multiset rearrangement. Thus faces of size k>=t are exactly those with k-M<=s=floor((t-2)/2). For t>=5 and k>=t-1 the dominant part is unique. Pair each high face with the legal pivot-insertion/deletion of that part, leaving only dimension<=t-2 faces; no nontrivial gradient path can follow a matched edge because other downward faces still contain the relevant pivot and cannot be lower matched faces. The complex includes the full (t-2)-simplex skeleton, hence is (t-3)-connected; Forman Morse bound dim<=t-2 plus Hurewicz/Whitehead yields wedge B spheres S^(t-2), where B=comb(N-1,t-1)-sum_i sum_{b=0}^s comb(N-ni,b)comb(ni-1,t-b-1) by exact signed Euler. For t>N the whole simplex is contractible and formula B=0. Independently checked forbidden-path DP, face count, and Euler for small examples incl K_(2,3,3) t5 B35/t6 B21, K_(3,3,3) t5 B70, and K_(4,4,4) source formula t5 B306/t6 B378. Finite checks corroborate only; the pairing proof covers all positive n_i,r>=3,t>=5.

## originality

PASS

PASS by bounded best-of-knowledge: Deshpande–Goyal–Sawant arXiv:2607.05358 (2026) is very close (same complete multipartite path-free objects). Its accessible abstract reports general structural decompositions and shellability thresholds but advertises complete sphere-wedge homotopy calculation for the bipartite family; the claimed uniform r>=3,t>=5 multiplicity was not found in accessible material. The source full 19 pages could not be inspected: its undisclosed corollary could overturn priority. Restricted t=4 and bipartite r=2 results do not by themselves imply the present all-r/all-t classification.

## value

PASS

Natural all-parameter homotopy classification of complete multipartite path-free complexes extends beyond the published bipartite case and shellable ranges. It determines every integral Betti rank and proves a structural uniform Morse matching for all t>=5, giving e.g. hundreds of top spheres for K_(4,4,4). This is more than finite enumerations, parameter substitution, or a routine combinatorial Euler count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
