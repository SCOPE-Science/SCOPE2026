# Classification of optimal binary length-six Z-channel codes
## Finding
For binary length-six one-error-correcting Z-channel codes \(C\subseteq\{0,1\}^6\), where a transmitted \(1\) may change to \(0\) and a transmitted \(0\) is unchanged, the known optimum \(M_Z(6,1)=12\) has exactly \(30\) labeled equality cases.

Every maximum contains \(000000\) and \(111111\) and has weight distribution \((1,0,3,4,3,0,1)\). Its three weight-two words are the incidence vectors of a perfect matching of the six coordinate positions. Its three weight-four words are their binary complements. Relative to that matching, the eight weight-three transversals split into two parity classes of four, and the code contains exactly one of those two classes. Conversely, every perfect matching and either parity class gives a valid maximum code. Since there are \(15\) perfect matchings, this gives exactly \(30\) maxima.

The \(30\) maxima form one orbit under the natural action of \(S_6\) by coordinate permutations. The stabilizer of any maximum has order \(24\). Each maximum has exactly \(16\) free points, so all optimal length-six codes are F-optimal in the free-point sense used in later Z-channel work.

## Assumptions and scope
For words \(x,y\in\{0,1\}^6\), write \(N(x,y)\) for the number of coordinates with \(x_i=1\) and \(y_i=0\), and define the asymmetric distance
\[
d_Z(x,y)=\max\{N(x,y),N(y,x)\}.
\]
A code corrects one Z-channel error exactly when every distinct pair has \(d_Z(x,y)\ge 2\). The classification here is only for binary length \(6\) and one asymmetric error. It does not claim an equality classification for other lengths or error radii.

## Proof
For each word \(x\), let its one-error Z-ball be \(B(x)=\{x\}\cup\{x-e_i:x_i=1\}\), where subtraction means changing one \(1\) to \(0\). Two words are compatible precisely when their Z-balls are disjoint, equivalently when \(d_Z\ge2\).

An exhaustive enumeration of the resulting compatibility graph on all \(64\) binary words finds maximum clique size \(12\) and exactly \(30\) maximum cliques. An independent fixed-size clique enumeration again finds exactly those \(30\) twelve-cliques and no thirteen-clique.

The equality cases have a uniform internal form. In each maximum, the three weight-two supports are pairwise disjoint and cover all six coordinates, hence form a perfect matching. The three weight-four words are exactly their complements. Every weight-three word in the code meets each matching edge in exactly one coordinate, so it is a transversal. After orienting each of the three matching edges, the eight transversals identify with \(\mathbb F_2^3\); the four selected transversals are exactly one parity class. Reversing an orientation exchanges the names of the two classes but does not change the intrinsic two-class partition.

Conversely, fix any perfect matching. The two parity halves of its transversals each combine with \(000000\), \(111111\), the three matching-edge words, and their three complements to give a twelve-word code with pairwise asymmetric distance at least \(2\). There are \(15\) perfect matchings and two parity choices, giving \(30\) codes. The generated family is exactly the exhaustive list.

## Verification
The supplied `verify.py` uses two independent compatibility tests: the asymmetric-distance formula and direct disjointness of one-error Z-balls. It then performs both maximal-clique enumeration and a separate increasing-order fixed-size clique enumeration. It independently generates the \(30\) matching/parity constructions and checks set equality with the exhaustive maxima.

The verifier also checks the common weight distribution, the \(16\) free points, and the coordinate-permutation orbit. Applying all \(720\) coordinate permutations to the published 1997 length-six example produces exactly the \(30\) maxima, and exactly \(24\) permutations stabilize that example. The recorded replay is in `verification_output.txt`.

## Relationship to prior work
The optimum \(M_Z(6,1)=12\) is not claimed as new. Al-Bassam, Venkatesan, and Al-Muhammadi gave a length-six twelve-word single-asymmetric-error-correcting example in 1997; that exact code appears among the \(30\) classified maxima. Later Z-channel work tabulates the same optimum, the free-point value \(16\), and the weight distribution \((1,0,3,4,3,0,1)\) for a length-six optimum. General Z-channel sphere-packing work provides broader bounds but does not itself classify all equality cases at this parameter.

The contribution here is the complete labeled census and the structural equality characterization: every optimum arises from a perfect matching plus a parity half of its transversals, all optima lie in one coordinate-permutation orbit, and every optimum is F-optimal.

## Limitations
This is a finite exact classification at one small parameter. It does not establish an analogous matching/parity description for other lengths. The coordinate-permutation action suffices to prove transitivity on the \(30\) maxima; no claim is made that \(S_6\) is the full automorphism group of the compatibility graph. An obscure or unindexed earlier equality-case enumeration remains a residual literature risk.

For cohort dating, an exact day-resolved public date was verified for the 2014 arXiv source below. Earlier journal literature is scientifically relevant but was not assigned an invented day-level public date.

## References
- S. A. Al-Bassam, B. S. Venkatesan, and S. Al-Muhammadi, “New single asymmetric error-correcting codes,” DOI:10.1109/18.623162.
- K. A. S. Abdel-Ghaffar, R. H. Weber, and collaborators’ classical Z-channel coding literature, including the table lineage indexed by OEIS:A010101.
- M. Fazeli, A. Vardy, and E. Yaakobi, “Generalized Sphere Packing Bound,” arXiv:1401.6496v1.
- A. Lebedev, I. Vorobyev, A. Lebedev, and C. Deppe, “Non-adaptive and two-stage coding over the Z-channel,” arXiv:2202.00136.
