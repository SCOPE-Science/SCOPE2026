# Independent mathematical audit

## correctness

PASS

In a tournament an acyclic/transitive vertex set has a source. In the cyclic block, that source forces all other vertices into one interval of length \(m+1\), while any subset of such an interval is transitive; hence its flag complex is the cyclic nerve \(N(n,m)\), homotopy equivalent to \(S^1\) for \(1\le m<n/2\) by the primary circular-arc nerve classification. No transitive face intersects all three blocks, so the full complex is the cyclic union of the three pairwise joins. Its two-stage homotopy pushout has three join summands, three suspensions and one extra \(S^1\) from the two-component final intersection. Thus the claimed wedge follows with \(X*X\simeq S^3\) and \(\Sigma X\simeq S^2\). The actual verify.py enumerates transitive faces and boundary ranks for \(n=3,5\), gives \(n=5\) face vector \((15,105,315,450,300,75)\) and Betti vector \((1,1,3,3,0,0)\); this agrees with, but does not replace, the proof. Each vertex has outdegree \(m+n=(3n-1)/2\); common out-neighbor counts vary, excluding double regularity.

## originality

PASS

The strongest same-object census is Govc (2020), which classifies regular tournaments only to order 13, including the \(n=3\), order-nine member; it cannot contain the infinite tail beginning at order 15. The circular nerve theorem supplies only the block homotopy type and not the three-block tournament construction and wedge. Related directed tournaplex and directed-flag work also does not state the all-odd-block lexicographic family. Searches for equivalent tournament substitution/lexicographic formulations located no covering formula, although the relevant published-result service was temporarily unavailable and cannot be counted as a negative search.

## value

PASS

A uniform infinite family of regular, non-doubly-regular tournaments with a prescribed mixed-dimensional sphere wedge is a natural structural extension beyond low-order enumerations. The result relates tournament substitution to explicit directed-flag homotopy types and is not merely re-enumeration of the order-nine table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
