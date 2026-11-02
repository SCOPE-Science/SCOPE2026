# Pell enumeration of maximum length-three single-overlap codes

## Finding
Let \(q\ge 2\) be an integer and let \(\Sigma\) be a fixed labeled alphabet of size \(q\). A code \(C\subseteq\Sigma^3\) is *2-overlap-free* when the length-two prefix of no member equals the length-two suffix of any member, including itself. Let \(P_0=0\), \(P_1=1\) and \(P_{j+2}=2P_{j+1}+P_j\) be the Pell numbers. The largest possible code has exactly
\[
M(q)=\frac{q^3-q}{3}
\]
words. **The number of distinct labeled codes attaining this size is exactly**
\[
N(q)=q!\bigl(P_{q+1}-P_q\bigr).
\]
More precisely, all maximizers have the ordered-block form described below, with blocks of one or two symbols; the only redundant parameter is the binary diagonal label of a singleton first block. The counts for \(q=2,3,4,5\) are respectively \(6,42,408,4920\).

## Assumptions and scope
No field structure or ordering on \(\Sigma\) is assumed. Codes are subsets, not ordered lists, and labels are fixed: two alphabet permutations generally give distinct codes. Forbidden equality concerns **only overlap length two**, not overlap length one. Accordingly this is not a claim about unrestricted cross-bifix-free codes.

For a binary matrix \(B=(B_{ab})_{a,b\in\Sigma}\), put
\[
C(B)=\{(a,b,c)\in\Sigma^3:B_{ab}=1,\ B_{bc}=0\}.
\]
An *ordered block partition* of \(\Sigma\) is a sequence of nonempty disjoint blocks covering \(\Sigma\), each of cardinality at most two. From such a partition form \(B\) as follows. If \(a\) lies in a strictly earlier block than \(b\), set \(B_{ab}=1\) and \(B_{ba}=0\). For each singleton block \(\{a\}\), choose \(B_{aa}\in\{0,1\}\). For each two-element block \(\{a,b\}\), choose \(e\in\{0,1\}\), put \(B_{ab}=B_{ba}=e\), and put \(B_{aa}=B_{bb}=1-e\). If the first block is a singleton, its diagonal can canonically be fixed to zero. Every maximum code is represented by exactly one canonical ordered-block partition with these choices.

## Proof
**Step 1 (sharp universal bound).** Cyclic rotation partitions \(\Sigma^3\) into \(q\) singleton orbits \((a,a,a)\) and \((q^3-q)/3\) three-element orbits. Constant triples self-overlap. Two different words in the same rotation orbit cannot coexist in a 2-overlap-free code: one is a cyclic shift of the other, making one length-two suffix an equal length-two prefix. Therefore \(|C|\le(q^3-q)/3\). To attain equality, fix an arbitrary total order on \(\Sigma\), choose \(B_{ab}=1\) exactly when \(a<b\), and choose all diagonal entries zero. The code \(C(B)\) is 2-overlap-free, and
\[
|C(B)|=\sum_{b=0}^{q-1}b(b+1)=\frac{q^3-q}{3}
\]
when the ordered symbols are indexed by integers from zero. The factor \(b+1\) counts choices \(c\le b\).

**Step 2 (all codes arise from context partitions).** For any 2-overlap-free \(C\), the sets \(F\) and \(S\) of its length-two prefixes and suffixes are disjoint. Choose any \(B\) with \(B_{ab}=1\) for \((a,b)\in F\) and \(B_{ab}=0\) for \((a,b)\in S\), labeling unused pairs arbitrarily. Then \(C\subseteq C(B)\) and \(C(B)\) itself is 2-overlap-free. At maximum size the sharp upper bound forces \(C=C(B)\). Thus it is enough to classify the matrices \(B\) for which \(|C(B)|=M(q)\).

**Step 3 (all extremal matrices).** The rotation-orbit equality condition for a binary matrix is that each nonconstant cyclic orbit has exactly one edge \(B_{ab}=1,B_{bc}=0\). Equivalently, no nonconstant directed three-cycle of bigram vertices has all three associated entries \(B_{ab},B_{bc},B_{ca}\) equal. For any two distinct letters \(a,b\), the two orbits with repeated symbols imply: if \(B_{ab}=B_{ba}=e\), then \(B_{aa}=B_{bb}=1-e\). Call such \(a,b\) *tied*. No letter can be tied to two different letters: if \(a\) is tied to both \(b\) and \(c\), then its diagonal forces both tie values to be the same \(e\). The directed triples \((a,b,c)\) and \((a,c,b)\) force \(B_{bc}=B_{cb}=1-e\), contradicting the diagonal requirement at \(b\). Hence ties form disjoint pairs.

For every untied pair \(a,b\), exactly one of \(B_{ab},B_{ba}\) is one; write \(a\prec b\) when \(B_{ab}=1\). If \(a,b\) are tied and \(c\) is outside the pair, their orientations toward \(c\) must agree: opposite orientations would make one of the two directed triples on \(a,b,c\) monochromatic, according as the tie value is zero or one. The strict orientations thus descend to a tournament on the singleton and pair blocks. A directed three-cycle of blocks would induce a monochromatic triple of ones, and therefore cannot occur. Every tournament without directed triangles is transitive; consequently its block order is unique. This proves that every extremal matrix has exactly the ordered-block form above. Conversely, its repeated-letter triples cannot be monochromatic by the diagonal rule, and any three distinct symbols lie either in three linearly ordered blocks or have two symbols in one paired block; in either case the directed triple contains both bit values. Thus each constructed matrix attains the bound.

**Step 4 (enumerating distinct codes, not just matrices).** For a structured extremal matrix, every ordered bigram \((a,b)\) occurs in \(C(B)\) as a prefix if \(B_{ab}=1\), or as a suffix if \(B_{ab}=0\), *except* that the diagonal bigram of a singleton first block occurs as neither. Indeed, if \(B_{ab}=1\), some \(c\) with \(B_{bc}=0\) exists whenever \(b\) is not that first singleton (choose an earlier-block letter, or the opposite diagonal inside a tied first pair). Dually, if \(B_{ab}=0\), some \(d\) with \(B_{da}=1\) exists unless \(a=b\) is a singleton first block (choose an earlier-block letter, or an appropriate member of a first pair). Therefore the prefix and suffix sets recover every off-diagonal entry and every nonexceptional diagonal of \(B\). All off-diagonal entries determine the tied pairs and their total block order. Exactly when the first block is a singleton, the two choices for that first diagonal yield the same code. No other two matrices yield the same code.

Let \(T_q\) be the number of extremal matrices divided by \(q!\). Inspect the first block. A singleton contributes two diagonal choices and a size-\((q-1)\) structure; a pair contributes two tie choices, offsetting the \(2!\) unordered-pair divisor, and a size-\((q-2)\) structure. Thus \(T_0=1\), \(T_1=2\) and \(T_q=2T_{q-1}+T_{q-2}\), so \(T_q=P_{q+1}\). Exactly \(2q!T_{q-1}\) extremal matrices have a singleton first block, and they occur in identical-code pairs. Subtracting one copy of each pair from the total gives
\[
N(q)=q!\bigl(T_q-T_{q-1}\bigr)=q!\bigl(P_{q+1}-P_q\bigr).
\]
The canonical choice \(B_{aa}=0\) at a first singleton removes the sole redundancy. This completes the classification.

## Verification
The accompanying independent C++17 brute-force checker enumerates every binary \(q\times q\) context matrix for \(1\le q\le5\), calculates \(|C(B)|\) directly and deduplicates codeword sets. The independent Python checker generates ordered singleton/pair partitions, constructs the corresponding codewords, directly checks disjoint prefix/suffix sets, and confirms all distinct matrix and code counts through \(q=5\). Output tables are embedded separately. Finite checking supports but is not substituted for the all-\(q\) proof.

## Relationship to prior work
Yang and Ding, *Q-Ary (t1,t2)-Overlap-Free Codes*, first publicly available September 22, 2025, formalize fixed-length overlap-free codes, give broad explicit constructions and enumerate sizes of those constructions; their full online text focuses on integer intervals \(t_1<t_2\), particularly intervals starting at one. The present theorem instead treats the single fixed forbidden overlap length two at codeword length three and determines the *global optimum together with all equality cases*. Wang, Fang and Feng (2025) consider the different restrictions involving intervals beginning at one and additional balance/correction requirements. No exhaustive Pell classification or exact all-alphabet equality census was located in inspected primary material or targeted mathematical-record searches. The simple necklace upper bound may be independently known; the nontrivial component is the structural and exact enumeration of its sharpness cases.

## Limitations
This is a statement only for words of length three and forbidden overlap of length two; it does not solve any larger-length or multi-overlap problem. Exhaustive numerical checks stop at alphabet size five, while the theorem for all sizes follows from the proof. Some previous work on maximum directed cuts of de Bruijn graphs or other equivalent combinatorial formulations may contain an implicit equivalent extremizer classification; independent priority verification remains necessary. The scientific review performed here is not an independent mathematical audit.

## References
1. H. Yang and Y. Ding, “Q-Ary (t1, t2)-Overlap-Free Codes,” *IEICE Transactions on Fundamentals*, E109-A (2026), 757–762, DOI: 10.1587/transfun.2025EAL2050. Earliest available 2025-09-22. Full text: https://globals.ieice.org/en_transactions/fundamentals/10.1587/transfun.2025EAL2050/_f
2. X. Wang, Y. Fang and T. Feng, “q-ary (1,k)-overlap-free codes with given restrictions,” *Discrete Mathematics* 348 (2025), 114236. DOI: 10.1016/j.disc.2024.114236. Abstract accessible at https://doi.org/10.1016/j.disc.2024.114236
