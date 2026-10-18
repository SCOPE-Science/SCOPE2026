# Sharp strong-majority vertex-colouring numbers of Boolean hypercubes

## Finding
For every integer \(d\ge2\), the Boolean hypercube \(Q_d\) has vertex set \(\mathbb F_2^d\), with two vertices adjacent exactly when they differ in one coordinate. A **strong-majority vertex-colouring** is a (not necessarily proper) vertex colouring such that, at every vertex, every individual colour appears on at most half of its open neighbours. The minimum number of colours is \(\operatorname{Maj}(Q_d)\).

The complete classification is
\[
\boxed{\operatorname{Maj}(Q_d)=
\begin{cases}
2,&d\text{ even},\\
4,&d=3\text{ or }d=5,\\
3,&d\ge7\text{ odd}.
\end{cases}}
\]
The exceptional five-dimensional case has a combinatorial obstruction rather than a computationally assumed lower bound. The first odd dimension with a three-colouring is seven. A three-colouring of the seven-cube is also implicit in previously published \((3,3,2)\)-partitions into multifold Hamming perfect codes; the explicit syndrome construction here supplies a convenient witness, and that seven-dimensional existence result alone is not claimed as new.

## Assumptions and scope
The graph is finite, simple, and undirected; all neighbourhoods are **open**. Colours need not give a proper graph colouring. Throughout \(d\) is an integer at least two; every vertex therefore has degree \(d\) and the strong-majority threshold for each colour is \(\lfloor d/2\rfloor\). Coordinates and all sums defining syndromes are over \(\mathbb F_2\), except when a colour is explicitly added modulo three. The one-cube, with pendant vertices, is outside this invariant's defined domain.

## Proof
**1. Even dimensions.** One colour is impossible in any graph with positive degree. If \(d=2k\), assign to a vertex \(x\) the parity of its first \(k\) coordinates. Of its \(2k\) neighbours, exactly \(k\) have the same colour and exactly \(k\) have the other. Thus \(\operatorname{Maj}(Q_{2k})=2\) for all \(k\ge1\).

**2. Odd-dimensional lower bound and small-cube upper bounds.** If \(d\) is odd, two colours cannot suffice: the maximum \(\lfloor d/2\rfloor\) for each would leave one of the \(d\) neighbours uncoloured. Hence at least three colours are needed. For the three-cube, a three-colouring would force every open neighbourhood to use all three colours once. The four odd-parity vertices are pairwise at distance two and any two share a common even-parity neighbour. Consequently all four odd-parity vertices require distinct colours; so \(\operatorname{Maj}(Q_3)\ge4\).

For either \(d=3\) or \(d=5\), choose a linear map \(h:\mathbb F_2^d\to\mathbb F_2^2\) whose columns are respectively \((01,10,11)\) or \((01,01,10,10,11)\). Colour \(x\) by \(h(x)\). These maps are surjective, so exactly four colours are used. For every \(x\), flipping coordinate \(j\) changes the syndrome by column \(j\); each nonzero syndrome change occurs at most \(\lfloor d/2\rfloor\) times. Thus this is a valid four-colouring.

**3. The five-cube has no three-colouring.** Consider the even and odd parity classes, each having sixteen vertices. Suppose a three-colouring existed. Every even vertex sees five odd neighbours and each colour can occur at most twice; hence each of the three colours occurs **once or twice** among those neighbours.

Fix one colour and let \(S\) be its set of odd-parity vertices; write \(s=|S|\). If \(t\) even vertices see two members of \(S\), the remaining \(16-t\) see one. Counting their incidences with \(S\) gives \(5s=16+t\), hence \(4\le s\le6\). Also every distinct pair of odd vertices at Hamming distance two has exactly two common even neighbours; pairs at distance four have none. Counting pairs inside neighbourhoods therefore gives
\[
t=5s-16=2e_2(S),
\]
where \(e_2(S)\) counts unordered distance-two pairs in \(S\). Consequently \(s\) is even: \(s=4\) or \(s=6\).

We prove \(s=6\) impossible. In that case \(e_2(S)=7\), so among the fifteen pairs of \(S\), exactly eight have distance four. Define \(H\) on the sixteen odd-parity vectors by making distance-four pairs adjacent. Every neighbour of \(x\) in \(H\) has the form \(x\oplus\mathbf1\oplus e_i\) for one of the five coordinate vectors \(e_i\). Distinct vertices of \(H\) have at most two common neighbours, because a common neighbour requires their difference to equal \(e_i\oplus e_j\), which has exactly two ordered representations. Adjacent vertices have none, so \(H\) is triangle-free.

**Six-vertex lemma.** A triangle-free graph on six vertices in which every pair of distinct vertices has at most two common neighbours has at most seven edges. Indeed, if it has an odd cycle, that cycle must have length five. Its five vertices induce a chordless cycle, and the sixth vertex has at most two neighbours on the cycle; there are at most seven edges. Otherwise it is bipartite. Eight edges force part sizes two and four (the complete bipartite graph) or three and three (at most one edge missing from the complete bipartite graph). In the former case two vertices share four neighbours; in the latter two share three, a contradiction. This proves the lemma.

The six vertices in \(S\) would induce eight edges in \(H\), contradicting the lemma. Thus every one of the three colours has **exactly four** vertices in the odd parity class. But these classes must partition all sixteen odd-parity vertices, whereas three times four is twelve. This contradiction proves \(\operatorname{Maj}(Q_5)\ge4\). With step 2, both exceptional values are exactly four.

**4. Seven-dimensional three-colouring.** Let \(h:\mathbb F_2^7\to\mathbb F_2^3\) be linear with columns the seven distinct nonzero vectors of \(\mathbb F_2^3\). Partition the eight syndromes into three nonempty classes of sizes \(3,3,2\), and colour \(x\) by the class containing \(h(x)\). Because \(h\) is onto, all three colours appear. The seven neighbours of every vertex have seven **distinct** syndromes (all syndromes except that of the vertex itself). Each colour consequently occurs at most three times, the permitted threshold. Hence \(\operatorname{Maj}(Q_7)=3\).

**5. Two-coordinate lifting.** Suppose \(d\ge7\) is odd and \(c:\mathbb F_2^d\to\mathbb Z/3\mathbb Z\) is a strong-majority three-colouring. Define
\[
C(x,u,v)=c(x)+v\pmod 3\qquad(x\in\mathbb F_2^d,\ u,v\in\mathbb F_2).
\]
The \(d\) old-coordinate neighbours of \((x,u,v)\) have the original colour multiplicities, permuted by addition of \(v\), each at most \((d-1)/2\). The two new-coordinate neighbours have **different** colours: flipping \(u\) preserves the colour and flipping \(v\) changes it. They therefore increase the multiplicity of any one colour by at most one. The resulting colour multiplicities are at most \((d+1)/2\), precisely the new strong-majority threshold. This lifting preserves the use of all three colours. Starting from the seven-cube yields the three-colouring for every larger odd \(d\). Together with the lower bound, this completes the classification. \(\square\)

## Verification
The accompanying dependency-free script `verify_cube_majority.py` constructs the stated two-, three-, and four-colour assignments independently from the proof descriptions. It directly checks every vertex neighbourhood for dimensions \(2\) through \(14\), and tests that the required number of colours is used. It also enumerates all \(\binom{16}{6}=8008\) six-subsets of the odd parity half of the five-cube and confirms that the distance-four graph induces at most seven edges in any such six-subset; its distance-four codegree and triangle-freeness are independently checked. Executing `python3 verify_cube_majority.py` returns `CERTIFICATE_OK`. These finite checks do not replace the unrestricted construction and the six-vertex lemma proved above.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak, and Woźniak (2026, arXiv:2605.23828), Section 2, introduced the strong-majority vertex-colouring invariant, determined the cycle and complete-graph cases, and proved a general maximum-degree upper bound. The inspected full section does not determine Boolean hypercubes. The present theorem explicitly uses the same open-neighbourhood convention. Their strong-majority **edge** invariant is different, even when the underlying graph is a hypercube.

Krotov and Valyuzhenich (2023, arXiv:2311.05566), in Section 4.3.1, explicitly treat \((3,3,2)\)-partitions of the seven-cube into multifold radius-one perfect codes. **Those previously known partitions already imply the three-colour upper bound in dimension seven**: each closed neighbourhood meets the three cells in sizes \(3,3,2\), and removing the central vertex leaves each open-neighbourhood count at most three. That special-case upper bound is credited, not presented as novel. Their Theorem 3 also counts perfect three-colourings of the five-cube, but does **not** prove the nonexistence of arbitrary, possibly non-perfect, strong-majority three-colourings established by the six-subset lemma here. The present contribution is the complete all-dimension optimum, with that unrestricted five-cube obstruction and the two-coordinate reduction. General coupon-colouring only imposes the existence of colours in open neighbourhoods and does not by itself impose the required multiplicity caps.

## Limitations
The theorem addresses Boolean hypercubes in dimensions at least two, not general Hamming graphs or other Cartesian products, and does not classify all optimal colourings. The seven-cube syndrome construction is an existence proof, not a uniqueness statement. The small-dimensional obstruction is mathematically proved; finite computations are corroboration only. No independent scientific validation or comprehensive bibliographic-priority determination has been performed.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, and M. Woźniak, *Strong majority colorings of graphs* (2026), arXiv:2605.23828, first posted 2026-05-22. https://arxiv.org/abs/2605.23828.
2. D. S. Krotov and A. A. Valyuzhenich, *On degree-3 and (n-4)-correlation-immune perfect colorings of n-cubes* (2023), arXiv:2311.05566. https://arxiv.org/abs/2311.05566.
