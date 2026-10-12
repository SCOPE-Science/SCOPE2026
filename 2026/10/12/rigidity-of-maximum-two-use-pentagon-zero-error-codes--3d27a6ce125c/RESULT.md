# Rigidity of maximum two-use pentagon zero-error codes
## Finding
For the pentagon confusability channel with input alphabet \(\mathbb Z/5\mathbb Z\), two symbols are confusable exactly when they are equal or differ by \(\pm1\) modulo \(5\). A two-use zero-error code is therefore an independent set in the strong square \(C_5^{{\boxtimes 2}}\).

The maximum code size is \(5\). More strongly, there are exactly \(10\) labeled maximum codes. They are precisely
\[
\mathcal C_{{a,+}}=\{{(i,a+2i):i\in\mathbb Z/5\mathbb Z\}},\qquad
\mathcal C_{{a,-}}=\{{(i,a-2i):i\in\mathbb Z/5\mathbb Z\}},
\]
with \(a\in\mathbb Z/5\mathbb Z\). Hence every maximum code is an affine transversal of slope \(2\) or \(-2\).

Under the natural channel-isometry group \((D_{{10}})^2\rtimes S_2\), of order \(200\), these ten codes form one orbit. Consequently each maximum code has stabilizer order \(20\).

## Assumptions and scope
The graph \(C_5\) is the confusability graph: distinct letters are adjacent when they differ by \(\pm1\) modulo \(5\). In the strong square, two distinct words \((x_1,x_2)\) and \((y_1,y_2)\) are confusable exactly when in each coordinate the two symbols are equal or adjacent in \(C_5\).

The result classifies maximum codes for exactly two independent uses of this channel. It does not classify maximum codes in higher strong powers and does not by itself reprove the asymptotic identity \(\Theta(C_5)=\sqrt5\).

## Proof
For a code \(\mathcal C\subseteq(\mathbb Z/5\mathbb Z)^2\), let
\[
A_i=\{j:(i,j)\in\mathcal C\}
\]
be the fiber in row \(i\). Within one row, two selected second coordinates must be nonadjacent in \(C_5\), so \(\lvert A_i\rvert\le2\).

Suppose some row has two codewords. The two second coordinates must differ by \(\pm2\). A codeword in either adjacent first-coordinate row would need its second coordinate to be simultaneously nonconfusable with both of those values. For two vertices at cyclic distance \(2\) in \(C_5\), no vertex is nonconfusable with both. Hence both neighboring rows are empty. The two remaining rows are adjacent to each other; their total contribution is at most \(2\), because if one of them contained two codewords the other would be empty, while if both are nonempty each contains at most one. Thus any code having a two-point row has size at most \(4\).

Therefore every code of size \(5\) has at most one point in each row, and hence exactly one point in each row. It is the graph of a function \(f:\mathbb Z/5\mathbb Z\to\mathbb Z/5\mathbb Z\). For adjacent first coordinates \(i\) and \(i+1\), the corresponding second coordinates must be nonconfusable, so
\[
f(i+1)-f(i)\in\{2,-2\}.
\]
Let \(p\) of the five cyclic increments equal \(2\), with the other \(5-p\) equal to \(-2\). Summing around the cycle gives
\[
0\equiv 2p-2(5-p)=4p-10\equiv4p\pmod5.
\]
Thus \(p\in\{0,5\}\). All increments have the same sign, so \(f(i)=a+2i\) for all \(i\), or \(f(i)=a-2i\) for all \(i\). Conversely, either form is plainly independent because any two distinct first coordinates that are equal or adjacent force the second-coordinate difference to be nonconfusable. There are five offsets and two signs, hence exactly \(10\) maximum codes.

Translations and reflections in the two \(C_5\) coordinates, together with coordinate swap, act transitively on these ten codes. The natural group has order \(10\cdot10\cdot2=200\), so orbit-stabilizer gives stabilizer order \(200/10=20\).

## Verification
The standalone `verify.py` constructs the \(25\)-vertex strong square directly from the confusability rule, enumerates every five-vertex independent set, checks that no six-vertex independent set exists, and compares the full maximum-set census with the ten affine transversals above. It also enumerates the \(200\) natural channel isometries and verifies one orbit of size \(10\) with stabilizer \(20\). Its expected terminal line is `VERIFY_OK maximum=5 labeled_maxima=10 natural_orbits=1 orbit_size=10 stabilizer=20`.

The proof, not the finite computation, establishes the classification. The computation is a complete independent finite replay of the stated parameter.

## Relationship to prior work
Shannon's 1956 paper introduced zero-error capacity and exhibited the celebrated five-word two-use pentagon code \(00,12,24,31,43\), thereby showing the gain from coding across channel uses. The primary paper states this construction and then turns to the general capacity problem; in the inspected original text it does not classify all two-use five-word codes.

A later full-text survey by Briët, Buhrman, and Gijswijt again presents the pentagon channel and a five-word two-use code as the foundational example, while framing zero-error codes as independent sets in strong graph powers. The sources inspected for this result state the extremal size/construction but not the exact ten-code equality classification or its single natural-isometry orbit.

## Limitations
This is a finite equality classification at block length two. It does not address equality structures for block lengths greater than two, quantum or entanglement-assisted variants, or arbitrary confusability graphs. Literature search cannot exclude an obscure unindexed prior observation of the ten-code classification; that residual bibliographic risk remains despite exact-parameter searches and inspection of the primary construction and a later full-text treatment.

## References
1. C. E. Shannon, “The Zero Error Capacity of a Noisy Channel,” *IRE Transactions on Information Theory* 2(3), 8–19 (1956), DOI `10.1109/TIT.1956.1056798`.
2. J. Briët, H. Buhrman, and D. Gijswijt, “Violating the Shannon capacity of metric graphs with entanglement,” full-text preprint, introductory pentagon example and graph formulation.
3. Capacity Atlas, “Pentagon zero-error channel,” historical summary of the two-use lower bound and Lovász upper bound.
