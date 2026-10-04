# Exact ternary length-three strongly two-separable code size
## Finding
For \(Q=\{0,1,2\}\), the maximum size of a strongly \(\overline{2}\)-separable code \(C\subseteq Q^3\) is \(10\). Equivalently, a \(\overline{2}\)-SSC\((3,10,3)\) exists, while no \(\overline{2}\)-SSC\((3,11,3)\) exists.

An explicit optimal code is
\[
\{001,011,020,022,102,110,121,200,212,221\}.
\]

## Assumptions and scope
Let \(Q=\{0,1,2\}\). For \(X\subseteq Q^3\), define
\[
\operatorname{desc}(X)=X(1)	imes X(2)	imes X(3),
\]
where \(X(i)\) is the set of symbols occurring in coordinate \(i\). A code \(C\subseteq Q^3\) is strongly \(\overline{2}\)-separable when, for every nonempty \(C_0\subseteq C\) with \(|C_0|\le2\), the intersection of all subsets \(C'\subseteq C\) satisfying \(\operatorname{desc}(C')=\operatorname{desc}(C_0)\) is exactly \(C_0\).

The claim concerns unrestricted ternary codes of length three under this definition; no linearity or algebraic closure is assumed.

## Proof
The displayed ten words are checked directly from the definition.

For the upper bound, fix a pair \(\{x,y\}\subseteq C\). Strong separability fails for this pair precisely when one member, say \(x\), can be omitted while other codewords inside \(\operatorname{desc}(\{x,y\})\) still realize every symbol used by the pair in every coordinate. If this happens, choose at most one replacement word for each of the three coordinates in which a replacement is needed. Together with \(x\) and \(y\), this gives a bad subset of at most five codewords.

Direct exhaustive classification of all subsets of \(Q^3\) of sizes two through five gives no bad subsets of sizes two or three, exactly \(891\) bad four-subsets, and every bad five-subset contains one of those bad four-subsets. Thus a ternary length-three code is strongly \(\overline{2}\)-separable exactly when it contains none of these \(891\) four-subsets.

Independent permutations of the three coordinate alphabets preserve descendants and the strongly separable property. Hence, if an eleven-word code existed, one of its words could be normalized to \(000\). An exact branch-and-bound search over the remaining \(26\) words, rejecting a branch as soon as it completes one of the \(891\) forbidden four-subsets, exhausts the normalized search tree without finding eleven words. The ten-word witness supplies the matching lower bound.

## Verification
Run `python3 verify.py`. The verifier derives the forbidden family directly from the definition rather than reading it from a stored table. It also checks the size-five reduction, verifies the ten-word witness, and performs the symmetry-normalized exact upper-bound search. The expected terminal line begins `VERIFY_OK maximum=10`.

## Relationship to prior work
Jiang, Cheng and Miao introduced strongly separable codes and studied \(q\)-ary strongly \(\overline{2}\)-separable codes of length three. Their construction gives size
\[
rac{9q^2-w^2}8,
\]
with the residue-dependent parameter \(w\); at \(q=3\) this yields nine codewords. Their presentation explicitly leaves the largest possible size as a general problem and notes that larger length-three codes may exist. The present result determines the exact ternary value and improves the construction value from nine to ten.

The nearby strong multimedia identifiable-parent property is a weaker fingerprinting structure and has a different extremal problem; an exact value for that class does not imply the strongly separable value proved here.

## Limitations
The proof is a complete finite classification only for alphabet size three, length three, and coalition bound two. It does not classify all optimal ten-word codes up to equivalence, and it does not give a formula for larger alphabets.

## References
1. J. Jiang, M. Cheng, Y. Miao, *Strongly Separable Codes*, arXiv:1412.6128, first public version 2014-11-25; Designs, Codes and Cryptography 79 (2016), 303–318, DOI 10.1007/s10623-015-0050-1.
2. X. Zhang, J. Jiang, M. Cheng, *Bounds and Constructions for Strongly Separable Codes with Length 3*, arXiv:1611.04349. This later paper concerns the \(\overline{3}\) condition rather than the \(\overline{2}\) ternary instance settled here.
