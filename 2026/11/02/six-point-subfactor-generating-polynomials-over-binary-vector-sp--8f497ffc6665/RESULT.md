# Six-point subfactor generating polynomials over binary vector spaces

## Finding

Let \(G=\mathbb F_2^d\), where \(d\ge3\), and let \(A\subseteq G\) have exactly six elements. An **\(A\)-subfactor** is a subset \(B\subseteq G\) maximal under inclusion among sets for which the translates \(A+b\), for \(b\in B\), are pairwise disjoint. Define the **subfactor-size generating polynomial**
\[
\Phi_{G,A}(z)=\sum_{B\text{ an }A\text{-subfactor}}z^{|B|}\in\mathbb Z[z].
\]
The sum is over actual subsets \(B\), without quotienting by translation, linear automorphisms, or other symmetries.

Fix any \(a_0\in A\) and put \(A_0=A-a_0\subseteq H=\langle A-A\rangle\), \(s=\dim_{\mathbb F_2}H\), and \(r=2^{d-s}\). Every possible six-point support has \(s\in\{3,4,5\}\). The following table is exhaustive; in the rank-four cases, a **parallelogram** means a set of four distinct support points with zero sum.

| Affine geometry of \(A\) | Local polynomial \(P_A(z)=\Phi_{H,A_0}(z)\) | Full polynomial \(\Phi_{G,A}(z)\) |
| --- | --- | --- |
| \(s=3\) | \(8z\) | \((8z)^r\) |
| \(s=4\), containing a parallelogram | \(24z^2\) | \((24z^2)^r\) |
| \(s=4\), no parallelogram | \(16z\) | \((16z)^r\) |
| \(s=5\) | \(16z^2+120z^4\) | \((16z^2+120z^4)^r\) |

In particular, a six-point subset is index-stable (all subfactors have the same cardinality) if and only if its affine rank is at most four. In affine rank five the complete size distribution is
\[
\#\{B:|B|=2r+2j\}=\binom rj16^{r-j}120^j,
\qquad 0\le j\le r.
\]

There is also an exact finite census: of the \(\binom{32}{6}=906192\) six-point subsets of \(\mathbb F_2^5\), the numbers in the four table rows, in order, are respectively \(17360\), \(416640\), \(27776\), and \(444416\). This census counts labeled subsets of the fixed vector space, not equivalence classes.

## Assumptions and scope

All vector spaces, spans, and differences are over \(\mathbb F_2\); the additive notation coincides with coordinatewise XOR. The support \(A\) consists of **six distinct elements** and \(d\ge3\). The polynomial counts inclusion-maximal (not necessarily maximum-cardinality) disjoint-translate packings. This distinction matters in the affine-rank-five case. Linear or affine changes of coordinates transport the packing problem bijectively.

The terminology *subfactor*, *index stability*, and *well-covered Cayley graph* follows the cited literature. No characterization is claimed for arbitrary-size supports, groups of odd characteristic, or nonabelian groups.

## Proof

**1. Difference criterion and cosets.** Put \(D=A-A\). For distinct \(b,b'\), the translates \(A+b\) and \(A+b'\) intersect precisely when \(b-b'\in D\). Hence \(B\) is a subfactor if and only if
\[
(B-B)\cap D=\{0\},\qquad B+D=G.
\]
The first condition is pairwise disjointness; the second is the exact maximality criterion: an outside point can be added if and only if its difference from every point of \(B\) avoids \(D\). Because \(D\subseteq H\), choices in different cosets of \(H\) are independent, and maximality holds if and only if the restriction to every coset is maximal. Therefore
\[
\Phi_{G,A}(z)=\bigl(\Phi_{H,A_0}(z)\bigr)^{|G/H|}
=\bigl(\Phi_{H,A_0}(z)\bigr)^r.
\]
Translating \(A\) does not change its difference set or its subfactors.

**2. The four affine shapes.** Hereafter, without changing the packing problem, translate the support and write \(A\) for the normalized subset \(A_0\subseteq H\). Translate a support point to zero. The five remaining nonzero vectors span \(H\), so their rank is three, four, or five. In rank five they are independent. In rank four the six-point affine configuration has a one-dimensional space of affine dependencies. Over \(\mathbb F_2\), each nontrivial affine dependency involves an even number of distinct points; a two-point dependency is impossible. Consequently the unique dependency has support four or six. In the former case the support contains a parallelogram; in the latter case it does not. A change of affine coordinates gives the following canonical representatives, where the \(e_i\) are independent standard basis vectors:
\[
\begin{array}{c|l}
s=3 & \{0,e_1,e_2,e_1+e_2,e_3,e_1+e_3\}\\
s=4,\ \text{parallelogram}&\{0,e_1,e_2,e_1+e_2,e_3,e_4\}\\
s=4,\ \text{six-circuit}&\{0,e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}\\
s=5 & \{0,e_1,e_2,e_3,e_4,e_5\}.
\end{array}
\]
Every case in the theorem occurs.

**3. Affine rank three.** The six points lie in the eight-element group \(H\). For every \(h\in H\), the two six-element subsets \(A\) and \(A+h\) intersect; equivalently \(h\in A-A\). Thus \(D=H\), so maximal compatible subsets are exactly the eight singletons. Hence \(\Phi_{H,A}(z)=8z\).

**4. Affine rank four, six-point dependency.** There are \(\binom62=15\) unordered differences of distinct points. If two different unordered pairs had the same difference, their four points would have zero sum and would form a parallelogram (distinct pairs sharing one point cannot have equal differences). The absence of parallelograms therefore makes all 15 differences distinct. They exhaust \(H\setminus\{0\}\), so \(D=H\). There are exactly 16 singleton subfactors and \(\Phi_{H,A}(z)=16z\).

**5. Affine rank four, parallelogram.** For the canonical representative in Step 2, direct subtraction gives
\[
H\setminus D=\{e_1+e_3+e_4,\ e_2+e_3+e_4,\ e_1+e_2+e_3+e_4\}.
\]
These three vectors are linearly independent. Define the *allowed-pair graph* on \(H\) by joining distinct \(b,b'\) precisely when \(b-b'\notin D\). This graph is the disjoint union of two ordinary three-dimensional cube graphs, since its three edge differences are linearly independent and generate an index-two subgroup. Compatible subsets are cliques in this graph. The cube graph has no triangles, and its maximal cliques are its edges; there are \(2\cdot(8\cdot3/2)=24\) such edges. Thus \(\Phi_{H,A}(z)=24z^2\).

**6. Affine rank five: binary distance-three codes.** In the canonical simplex case, the nonzero differences \(D\setminus\{0\}\) are exactly the vectors of Hamming weight one or two. Thus a compatible subset is a binary length-five code of minimum Hamming distance at least three; subfactors are exactly the inclusion-maximal such codes.

Translate one member of a nonempty compatible code to zero. Its remaining words must have weight at least three. If the all-ones word (weight five) is present, no third word is possible, and the resulting antipodal pair is maximal because every vertex lies within Hamming distance two of at least one of its members. There are exactly \(32/2=16\) such pairs.

If the all-ones word is absent, every other word has weight three or four. Two distinct weight-four words are incompatible, and among three distinct weight-three words two must intersect in at least two coordinates (otherwise three three-element supports in a five-element set would have pairwise intersections at most one, an impossibility). Therefore a compatible code has at most \(1+1+2=4\) elements.

Any compatible pair with distance three or four can be extended to a triple: after translating its first word to zero, if the second word has weight three, choose a weight-four word missing one of its three occupied coordinates; if the second has weight four, choose a weight-three word using its missing coordinate and two of its occupied coordinates. In each case the newly chosen word has distance at least three from both existing words. Every compatible triple extends to a four-code: after translating one member to zero, its other two nonzero words cannot both have weight four. If they have weight three, their support intersection is a singleton; choose as fourth word the weight-four vector supported on the other four coordinates. If one has weight three and the other weight four, the weight-three support contains the unique missing coordinate of the weight-four support. The fourth word has weight three, consisting of that missing coordinate and the complementary two coordinates in the weight-four support. The stated fourth words have distance at least three from each previous word. Thus maximal code sizes are precisely two and four.

Every four-code containing zero has exactly one weight-four word and two weight-three words. The weight-four word omits one of five coordinates; the two weight-three supports both contain that omitted coordinate and partition the other four coordinates into two unordered pairs. There are \(5\cdot3=15\) four-codes containing zero. Translation acts transitively on the 32 ambient words, and double-counting incidences between four-codes and their constituent words gives \(32\cdot15/4=120\) four-codes in total. Hence \(\Phi_{H,A}(z)=16z^2+120z^4\).

Combining Steps 1–6 proves the classification and every displayed generating polynomial.

**7. Census in the five-cube.** There are \(4\binom{5}{3}_2=620\) affine three-flats, each containing \(\binom86=28\) six-subsets, giving \(17360\) affine-rank-three supports. There are \(2\binom{5}{4}_2=62\) affine four-flats. Each has \(\binom{16}{6}-30\binom86=7168\) affine-rank-four six-subsets (its 30 affine three-flats account for every lower-rank support). The no-parallelogram class is a single orbit of the affine group \(\operatorname{AGL}_4(2)\), with stabilizer \(S_6\): any permutation of its six points extends uniquely to an affine automorphism because any five points are an affine basis. Its orbit size is \(16\cdot20160/720=448\) per affine four-flat, giving \(62\cdot448=27776\). The other affine-rank-four class therefore has \(62\cdot(7168-448)=416640\) members. The remaining \(\binom{32}{6}-17360-27776-416640=444416\) supports are affine-independent. Each support spans a unique affine flat of its rank, so there is no double counting.

## Verification

The accompanying standalone Python program `check.py` uses only standard-library modules. It independently constructs the difference set and computes all maximal compatible subsets as maximal cliques of the allowed-pair graph for the four canonical shapes. The resulting local size histograms are \(\{1:8\}\), \(\{2:24\}\), \(\{1:16\}\), and \(\{2:16,4:120\}\). A separate algorithm directly enumerates all candidate one-, two-, three-, and four-element codes in the five-cube and confirms that only 16 maximal pairs and 120 maximal quadruples occur. Finally it classifies all \(\binom{31}{5}=169911\) six-point supports containing zero in the five-cube and converts to counts of all \(\binom{32}{6}=906192\) labeled supports. The recorded output ends in `VERIFY_OK`.

The universal theorem for every \(d\) follows from the proof above. Finite computations independently check only the explicitly finite local and five-cube instances; they are not used as infinite-case certification.

## Relationship to prior work

Hooshmand and Yousefian Arani (2023) already exhibited the affine-rank-five six-point support \(\{0,e_1,\ldots,e_5\}\) with subfactors of cardinalities two and four and used it to establish instability of the five-dimensional binary group. Kabenyuk (first posted February 6, 2026), Section 5, Lemma 11, also proves its lower and upper subfactor indices are two and four. **Neither that witness nor those extremal cardinalities are claimed as new here.** The 2026 paper provides the Cayley graph connection and the full-group stability classification.

The result here instead supplies a **complete classification across every six-point support and every ambient dimension**, with exact generating polynomials counting all subfactors, including the 16-versus-120 maximal-code enumeration, the rank-four cube decomposition, and an independent labeled five-cube census. Prior global stability and index bounds do not provide these multiplicities or the all-support partition. Published coding-theory classifications for maximum distance-three codes may imply parts of the local code count; this historical-coverage risk is acknowledged rather than presented as an independence claim.

## Limitations

The theorem concerns six-point supports in elementary abelian two-groups only. It does not classify arbitrary support cardinalities, odd-characteristic vector spaces, or general finite groups. The affine-rank-five instability example, its two extremal sizes, and generic graph/coset reductions are established prior facts. Search-based comparison cannot establish absolute priority over every historical coding or graph-theoretic enumeration. Independent mathematical review has not been performed.

## References

1. M. Kabenyuk, *Factors in finite groups and well-covered graphs*, arXiv:2602.06770, first posted February 6, 2026; especially Sections 1, 2, and 5, Lemma 11. https://arxiv.org/abs/2602.06770
2. M. H. Hooshmand and M. M. Yousefian Arani, *Computational aspects of subindices and subfactors with characterization of finite index stable groups*, arXiv:2310.03438, first posted October 5, 2023; especially Theorem 3.1 and its proof, Step 1. https://arxiv.org/abs/2310.03438
3. M. H. Hooshmand, *Some additive properties of \(\mathbb Z_n\) and \(k\)-index stability of finite groups*, arXiv:2607.08805, first posted July 9, 2026; introduction and index-stability framework. https://arxiv.org/abs/2607.08805
