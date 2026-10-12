# Complete equality classification in the smallest two-block ordered Hamming MDS problem
## Finding
Let \(Q=\mathbb Z/q\mathbb Z\) with \(q\ge2\), and write a word of the ordered Hamming space \(\overrightarrow H(q,2,2)\) as two ordered blocks \((a,b;c,d)\). Give one block ordered weight \(0\) at \((0,0)\), weight \(1\) when its second coordinate is \(0\) and its first is nonzero, and weight \(2\) when its second coordinate is nonzero; the distance is the sum of the two block weights. Then every code of minimum ordered distance at least \(3\) has at most \(q^2\) words. Equality holds exactly for the codes \[C=\{(F(u,v),u;G(u,v),v):u,v\in Q\},\] where, for each fixed \(u\), the map \(v\mapsto F(u,v)\) is a permutation of \(Q\), and for each fixed \(v\), the map \(u\mapsto G(u,v)\) is a permutation of \(Q\). Consequently the number of labeled maximum codes is exactly \((q!)^{2q}\). For \(q=2\), there are exactly \(16\) labeled maxima; every one is an affine two-flat in \(\mathbb F_2^4\), and the natural affine ordered-metric isometry group acts transitively on these sixteen maxima.

## Assumptions and scope
The alphabet is the additive group \(Q=\mathbb Z/q\mathbb Z\) with \(q\ge2\). A word is written \((a,b;c,d)\), with two ordered blocks of length two. For a block \((x,y)\), its ordered weight is \(0\) if \((x,y)=(0,0)\), \(1\) if \(y=0\) and \(x\ne0\), and \(2\) if \(y\ne0\). The ordered distance is the weight of the difference. The statement concerns arbitrary codes, not only linear or additive codes.

## Proof
The Singleton bound for ordered codes gives \(M\le q^{nr-d+1}\). Here \(n=r=2\) and \(d=3\), so every code has \(M\le q^2\).

Now suppose \(|C|=q^2\). Consider the projection \(\pi(a,b;c,d)=(b,d)\) onto the rightmost coordinate of each ordered block. If two distinct codewords had the same value of \(\pi\), then their difference would have both rightmost coordinates equal to zero, hence ordered weight at most \(1+1=2\), contradicting minimum distance \(3\). Thus \(\pi\) is injective. Since both \(C\) and \(Q^2\) have \(q^2\) elements, \(\pi\) is bijective. Therefore there are unique functions \(F,G:Q^2\to Q\) such that
\[
C=\{(F(u,v),u;G(u,v),v):u,v\in Q\}.
\]

Fix \(u\) and take two distinct values \(v,v'\). The second ordered block of the corresponding codeword difference has weight \(2\), while the first block has equal rightmost coordinate. To reach total distance at least \(3\), its first coordinate must be nonzero. Hence \(F(u,v)\ne F(u,v')\). Thus, for each fixed \(u\), \(v\mapsto F(u,v)\) is a permutation of \(Q\). The symmetric argument with fixed \(v\) shows that, for each fixed \(v\), \(u\mapsto G(u,v)\) is a permutation.

Conversely, suppose these permutation conditions hold. Two distinct parameter pairs \((u,v)\) and \((u',v')\) differ in either one or both coordinates. If both differ, each ordered block contributes weight \(2\), giving distance \(4\). If only \(v\) differs, the second block contributes \(2\) and the permutation condition for \(F(u,\cdot)\) forces a nonzero first coordinate in the first block, giving at least \(3\). If only \(u\) differs, the corresponding condition for \(G(\cdot,v)\) gives the same conclusion. Hence every such pair \((F,G)\) defines a maximum code.

There are \(q!\) choices for each of the \(q\) permutations \(F(u,\cdot)\), independently, and another \(q!\) choices for each of the \(q\) permutations \(G(\cdot,v)\). Therefore the exact number of labeled maxima is \((q!)^{2q}\).

For \(q=2\), each permutation of \(\mathbb F_2\) is either the identity or the transposition. Hence \(F(u,v)=v+\alpha u+\beta\) and \(G(u,v)=u+\gamma v+\delta\) for uniquely determined \(\alpha,\beta,\gamma,\delta\in\mathbb F_2\). Thus all sixteen maxima are affine two-flats. Translations alter \(\beta,\delta\), while the two independent ordered-block shears alter \(\alpha,\gamma\), so the natural affine ordered-metric isometry group is transitive on the sixteen maxima.

## Verification
The supplied checker independently rebuilds the binary ordered metric, exhaustively enumerates all subsets of the sixteen binary words, verifies maximum size \(4\), finds exactly sixteen labeled maxima, checks that every maximum is affine, and confirms transitivity under translations, the two block shears, and block swap. It also enumerates all \((3!)^6=46{,}656\) codes supplied by the theorem for \(q=3\), verifies that they are pairwise distinct and all have minimum ordered distance at least \(3\), and checks the formula directly.

## Relationship to prior work
Barg and Purkayastha define the ordered Hamming, or NRT, space and state the Singleton bound \(M\le q^{nr-d+1}\) for arbitrary ordered codes. Their paper develops general existence, nonexistence, and linear-programming bounds, including a special treatment of block length two, but the inspected text does not classify the equality cases at \(n=r=2,d=3\) or count them. Barg and Park study linear ordered codes and ordered MDS weight distributions; that linear framework does not imply the classification above for arbitrary nonlinear maximum codes. The present result identifies the complete equality layer in the smallest case where two nontrivial ordered blocks interact.

## Limitations
The theorem classifies only the parameter set \(n=r=2,d=3\). It does not classify maximum ordered codes for larger numbers of blocks, longer blocks, or other distances. The binary orbit statement is for the natural affine ordered-metric isometry group generated by translations, independent block shears, and block permutation; no claim is made here about a larger permutation automorphism group of the finite compatibility graph.

## References
1. A. Barg and P. Purkayastha, “Bounds on ordered codes and orthogonal arrays,” arXiv:cs/0702033, first submitted 5 February 2007; Moscow Mathematical Journal 9 (2009), 211–243. In particular, Section 1-A defines the NRT distance and Section 2-B.1 states the Singleton bound.
2. A. Barg and W. Park, “On Linear Ordered Codes,” Moscow Mathematical Journal 15 (2015), 679–702. The paper treats linear ordered codes, including ordered MDS weight distributions.
