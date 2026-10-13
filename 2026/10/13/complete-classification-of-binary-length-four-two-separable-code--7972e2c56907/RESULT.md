# Complete classification of binary length-four two-separable codes
## Finding
Let \(C\subseteq\{0,1\}^4\). For each nonempty parent set \(P\subseteq C\), define the descendant box
\[
\operatorname{desc}(P)=\prod_{i=1}^4\{x_i:x\in P\}.
\]
Call \(C\) \(\overline{2}\)-separable when distinct parent sets \(P,Q\subseteq C\) with \(1\le |P|,|Q|\le2\) always satisfy \(\operatorname{desc}(P)\ne\operatorname{desc}(Q)\).

The exact maximum is
\[
M(\overline{2},4,2)=7.
\]
There are exactly \(240\) labeled maximum codes. Under the full binary Hamming-isometry group \((C_2)^4\rtimes S_4\), of order \(384\), they form exactly two orbits of sizes \(48\) and \(192\), with stabilizer orders \(8\) and \(2\).

Representatives are
\[
\{0000,0001,0010,0111,1011,1100,1111\}
\]
and
\[
\{0000,0001,0010,0100,0111,1001,1110\}.
\]
Their pairwise Hamming-distance distributions, listed at distances \(1,2,3,4\), are respectively \((4,8,8,1)\) and \((4,10,6,1)\), so the two orbit types are intrinsically distinct.

## Assumptions and scope
The alphabet is binary, the four coordinates are labeled, and descendants use the standard coordinatewise marking assumption. “Labeled” means no quotient by coordinate or symbol symmetries. The equivalence group in the orbit statement consists exactly of all coordinate permutations and independent binary symbol swaps in the four coordinates.

The result concerns \(\overline{2}\)-separability, not \(2\)-frameproofness, strong separability, traceability, or Boolean-sum separability from nonadaptive group testing.

## Proof
There are only \(16\) ambient binary words. The bundled verifier checks every one of the \(\binom{16}{7}=11\,440\) seven-subsets and every one of the \(\binom{16}{8}=12\,870\) eight-subsets.

For each tested family it constructs every singleton and pair descendant twice. One implementation records, in each coordinate, whether the parent symbols are \(\{0\}\), \(\{1\}\), or \(\{0,1\}\). The second independently enumerates all words in the Cartesian descendant box. The two predicates agree on every tested family.

Exactly \(240\) seven-subsets are separable and no eight-subset is. Since separability is hereditary under taking subcodes, any code of size at least \(8\) would contain a separable eight-subcode. Thus the exact maximum is \(7\).

For classification, the verifier generates all \(2^4\cdot4!=384\) binary Hamming isometries, applies them to all \(240\) maxima, and obtains precisely two orbits, of sizes \(48\) and \(192\). Orbit--stabilizer yields stabilizer orders \(8\) and \(2\). Direct recomputation of all pairwise Hamming distances gives the two distributions stated above.

## Verification
Run `python3 verify.py`. The script uses only the Python standard library and rebuilds every object from the definitions.

The replayed terminal line is:

`VERIFY_OK maximum=7 labeled_maxima=240 orbits=2 orbit_sizes=48,192 stabilizers=8,2`

## Relationship to prior work
Cheng, Fu, Jiang, Lo, and Miao give the standard descendant definition of \(\overline{2}\)-separable codes and place the problem in multimedia fingerprinting. Their 2013 open article concentrates on length \(2\) and records the surrounding short-code program. Fuji-Hara's 2014 binary treatment gives a projective-geometric characterization and explicitly constructs a binary \(2\)-separable code with parameters \((4,7,2)\); the same paper quotes the Cheng--Miao upper bound, which is \(9\) at these parameters. Thus a seven-word construction is prior work.

Cheng, Jiang, and Tang later study length \(4\) directly and advertise an equivalent condition plus two infinite construction families, one asymptotically optimal. The accessible abstract does not state an exact binary equality census or a symmetry classification. The new content here is the all-code upper bound at the binary parameter together with the exact \(240\)-extremizer census and its two equivalence classes.

## Limitations
This is a finite classification only for the binary alphabet, length \(4\), and parent sets of size at most \(2\). It does not determine larger alphabets or lengths, stronger fingerprinting properties, or group-testing notions that use Boolean unions instead of coordinatewise descendant boxes.

The full text of the later length-four construction paper was not available in the inspected open material, so it remains a specifically identified originality risk. Its abstract describes constructions and asymptotic optimality rather than a binary extremal census; the accepted claim nevertheless retains a residual risk of an obscure or unindexed finite enumeration.

## References
1. M. Cheng, H.-L. Fu, J. Jiang, Y.-H. Lo, and Y. Miao, “New bounds on \(\overline{2}\)-separable codes of length \(2\),” Designs, Codes and Cryptography, DOI 10.1007/s10623-013-9849-9, first published 2013-06-27.
2. R. Fuji-Hara, “Vector Representation of Descendant Sets and Binary Fingerprinting Codes,” RIMS Kokyuroku 1889 (2014), 21–31.
3. M. Cheng, J. Jiang, and X. Tang, “Asymptotically optimal \(\overline{2}\)-separable codes with length \(4\),” Cryptography and Communications 9 (2017), 397–405, DOI 10.1007/s12095-016-0182-9.
