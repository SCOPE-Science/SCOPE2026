# Exact ternary length-three strongly \(\overline{2}\)-separable codes

## Finding

There are exactly \(54\) labeled maximum ternary length-three strongly \(\overline{2}\)-separable codes, including exactly \(20\) that contain \(000\). They form one orbit under the Hamming-isometry group \((S_3)^3\rtimes S_3\), and each has stabilizer order \(24\). The common maximum size is the previously established value \(10\) [3]. The new claim is the complete classification at that size, not the value of the maximum or the forbidden configurations used to find it.

The lexicographically least labeled maximum is
\[
\{000,001,012,022,102,110,121,202,211,220\}.
\]
In each coordinate, every maximum has sorted symbol multiplicities \((4,3,3)\). Its \(45\) unordered pairs have Hamming-distance counts \(3,30,12\) at distances \(1,2,3\), respectively. Among the boxes \(\operatorname{desc}(\{x,y\})\cap C\) indexed by these pairs, \(33\) contain exactly two words of \(C\) and \(12\) contain exactly three.

## Assumptions and scope

Let \(Q=\{0,1,2\}\). A labeled code is an unordered set of distinct elements of \(Q^3\), with coordinates and symbols fixed. For a nonempty coalition \(A\subseteq Q^3\), write \(A(j)\) for the set of symbols in coordinate \(j\) and \(\operatorname{desc}(A)=A(1)\times A(2)\times A(3)\). The code \(C\) is strongly \(\overline{2}\)-separable if for every nonempty \(C_0\subseteq C\) with \(|C_0|\le2\), the intersection of all nonempty \(A\subseteq C\) with \(\operatorname{desc}(A)=\operatorname{desc}(C_0)\) equals \(C_0\). Equivalence permits arbitrary coordinate permutations and independent symbol relabelings in each coordinate.

## Proof

A singleton cannot witness failure, because its descendant box contains only its one codeword. For a pair \(\{x,y\}\), write \(D=\operatorname{desc}(\{x,y\})\). An endpoint can be omitted precisely when some coalition contained in \(C\cap D\) omits that endpoint and has descendant \(D\). Indeed, any same-descendant coalition must be contained in \(D\), and the pair itself is one of the coalitions in the intersection. Thus a failure is exactly containment of a set \(\{x,y\}\cup A\) for a coalition \(A\) with this witness property. Taking inclusion-minimal such forbidden sets preserves the test. Enumerating all ambient pairs and all subsets of each pair box yields \(891\) minimal forbidden sets, all of size four, in agreement with [3].

Every nonempty code can be moved by independent symbol permutations to contain \(000\). To enumerate the maxima, begin with \(000\) and recursively decide membership of each of the other \(26\) words. A partial set containing a forbidden set cannot be extended to a valid code. A branch whose current cardinality plus the number of undecided words is below the running best cannot contain a maximum; branches reaching the running best are retained, including ties. The verifier enumerates exactly \(20\) valid ten-word sets containing \(000\). It also reproduces the known extremal size \(10\).

Applying all coordinatewise symbol permutations to the \(20\) normalized maxima yields the complete labeled census: any labeled maximum can be mapped into that normalized list and recovered by an inverse relabeling. The union contains \(54\) distinct sets, consistent with the incidence count \(20\cdot 27=54\cdot 10\), since every word occurs equally often among labeled maxima. The orbit of the displayed representative under the full group of order \(6^4=1296\) contains exactly these \(54\) sets. Hence the stabilizer order is \(1296/54=24\). The multiplicity, pair-distance and pair-box counts are computed on the representative; each distribution is invariant under the group. The verifier additionally recomputes the profiles on every labeled maximum.

## Verification

Run `python3 verify.py` with the Python standard library. The verifier regenerates the obstructions and normalized search, expands and counts all labeled maxima, replays the original coalition-intersection definition on every maximum, and checks the full orbit and profiles. In the output, `maximum=10` and `forbidden_minimal=891` reproduce known facts. The equality check reports `normalized_maxima=20 labeled_maxima=54 natural_group=1296 orbits=1 orbit_size=54 stabilizer=24` and labeled census SHA-256 `9f5c2de392d26f636c02b9e938b3b637e73f0e7eb4908e67cffeef3753e8f616`.

## Relationship to prior work and limitations

Jiang, Cheng and Miao [1] construct length-three strongly \(\overline{2}\)-separable codes; their general construction gives size \(9\) at \(q=3\). The inherited bound in Zhang, Jiang and Cheng [2] gives \(12\) at these parameters. The same size-ten optimum, a ten-word witness, and the \(891\) four-word obstructions appear in [3], which explicitly does not classify all optimal ten-word codes up to equivalence. The equality census determines that its exhibited optimum belongs to the unique isometry type, rather than merely exhibiting another code of the same size.

The classification is finite and exhaustive only for this parameter triple. The claim is not a classification of multimedia IPP or frameproof codes, which impose different conditions. The comparison does not rule out unindexed equality-case enumerations.

## References

1. J. Jiang, M. Cheng, and Y. Miao, “Strongly Separable Codes,” arXiv:1412.6128; *Designs, Codes and Cryptography* 79, 303–318, DOI 10.1007/s10623-015-0050-1.
2. X. Zhang, J. Jiang, and M. Cheng, “Bounds and Constructions for \(\overline{3}\)-Strongly Separable Codes with Length \(3\),” arXiv:1611.04349; *Cryptography and Communications* 10, 555–565.
3. “Exact ternary length-three strongly two-separable code size,” [Resultary record fc51dbba75e2](https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-exact-ternary-length-three-strongly-two-separable-code-size--fc51dbba75e2/RESULT.md).
