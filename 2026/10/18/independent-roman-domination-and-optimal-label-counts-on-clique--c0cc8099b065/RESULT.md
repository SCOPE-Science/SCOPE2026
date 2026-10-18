# Independent Roman domination and optimal-label counts on clique–cycle products

## Finding
For integers \(q\ge3\) and \(n\ge3\), put \(G_{q,n}=K_q\square C_n\). Write \(i_R(G)\) for the minimum weight of an independent Roman dominating function and \(M(q,n)\) for the number of minimizing functions on the labeled vertex set. Then
\[
i_R(G_{q,n})=\begin{cases}\lceil 3n/2\rceil,&q=3,\\2n,&q\ge4,\end{cases}
\]
and
\[
M(q,n)=\begin{cases}
2\big(2^{n/2}+2(-1)^{n/2}\big),&q=3,\ n\text{ even},\\
n\big(2^{(n+1)/2}+2(-1)^{(n+1)/2}\big),&q=3,\ n\text{ odd},\\
(q-1)^n+(-1)^n(q-1),&q\ge4.
\end{cases}
\]
Every minimum function is characterized below, not merely counted. For example, on the triangular clique-cycle with \(n=5\), there are exactly \(30\) minimum labelings of weight \(8\), while for \(q=4,n=5\) there are \(240\) minimum labelings of weight \(10\).

## Assumptions and scope
The simple graph \(C_n\) has vertex set \(\mathbb Z/n\mathbb Z\), with edges between consecutive residues; \(K_q\) has vertices \(\{1,\ldots,q\}\). The Cartesian product has vertices \((a,j)\), with adjacency when exactly one coordinate changes along an edge of its corresponding factor. A map \(f:V(G)\to\{0,1,2\}\) is an independent Roman dominating function if its positive support \(\{v:f(v)>0\}\) is independent, and every vertex labeled zero has a neighbor labeled two. Its weight is \(\sum_v f(v)\). All functions are counted on labeled vertices, without quotienting by symmetries.

A *fiber* is the \(q\)-clique \(\{(a,j):1\le a\le q\}\) at cycle index \(j\). The classification is as follows. Each fiber has one positive vertex, so record its row \(c_j\in\{1,\ldots,q\}\) and label \(t_j\in\{1,2\}\). Necessarily \(c_j\ne c_{j+1}\). When \(q\ge4\), every \(t_j=2\); every proper \(q\)-coloring of the cycle gives one valid function. When \(q=3\), let \(S=\{j:t_j=1\}\). Validity is equivalent to (i) \(c_j\ne c_{j+1}\) for all \(j\), (ii) \(S\) is independent in \(C_n\), and (iii) for each \(j\in S\), the three colors \(c_{j-1},c_j,c_{j+1}\) are pairwise distinct. Minimum weight occurs exactly when \(S\) has maximum cardinality \(\lfloor n/2\rfloor\).

## Proof
**One positive vertex in each fiber.** Independence permits at most one positive vertex per fiber because each fiber is a clique. Suppose some fiber were empty. Every one of its \(q\ge3\) zero vertices would require a label-two neighbor in the same row in one of its two adjacent fibers. Those two fibers together contain at most two positive vertices, and hence can cover at most two different rows, a contradiction. Thus every fiber contains exactly one positive vertex. Independence between neighboring fibers is precisely the proper-color constraint \(c_j\ne c_{j+1}\).

**When labels one are possible.** Suppose the unique positive vertex in fiber \(j\) has label one. Its other \(q-1\) vertices have label zero and must be defended by label-two vertices in adjacent fibers, as no label two occurs in their own fiber. Each adjacent fiber supplies at most one such defending row. Hence \(q-1\le2\). As \(q\ge3\), this forces \(q=3\), and both neighboring fibers must carry label two in the two rows different from \(c_j\). Conversely, these conditions, proper colors, and one positive per fiber guarantee domination of every zero vertex: any zero in a label-two fiber is defended internally, and the two zeros in a label-one fiber are defended by its two neighbors. Thus the stated classification of all valid functions holds.

**Sharp minimum weight.** For \(q\ge4\) all \(n\) positives carry label two, giving weight \(2n\). For \(q=3\), the weight is \(2n-|S|\), where \(S\) is independent in \(C_n\). Hence \(|S|\le\lfloor n/2\rfloor\). To realize equality, choose any maximum independent set \(S\). If \(n=2k\), there are two alternating choices of \(S\), and the \(k\) remaining label-two fibers form a cyclic list. Choose their colors so that consecutive members of that list have unequal colors; assign every intervening label-one fiber the unique third color. Such colors exist for all \(k\ge2\). If \(n=2k+1\), there are exactly \(n\) choices of maximum independent \(S\); their complement has \(k+1\) label-two fibers, with one adjacent pair and the remaining successive pairs separated by one label-one fiber. Choose distinct colors for consecutive members of this cyclic list and again assign the third color to each label-one fiber. For \(k=1\), there are only two label-two fibers, which simply receive distinct colors. All constraints hold, proving the minimum value.

**Counting every minimum.** The number of proper \(q\)-colorings of a labeled cycle of length \(r\ge3\) is \((q-1)^r+(-1)^r(q-1)\). This follows, for example, by taking the trace of the \(q\)-by-\(q\) zero-diagonal all-ones-off-diagonal matrix, whose eigenvalues are \(q-1\) once and \(-1\) with multiplicity \(q-1\). For \(q\ge4\), this immediately gives \(M(q,n)\).

For \(q=3,n=2k\), there are exactly two maximum independent choices \(S\). For fixed \(S\), the \(k\) label-two positions can be colored in \(2^k+2(-1)^k\) ways when \(k\ge3\). At the boundary \(k=2\), the two label-two positions must have unequal colors, giving \(6=2^2+2\) choices. The intermediate label-one colors are then uniquely forced. Thus \(M(3,2k)=2(2^k+2(-1)^k)\).

For \(q=3,n=2k+1\), a maximum independent set \(S\) is uniquely specified by the single consecutive pair of indices in its complement; there are \(n\) possibilities. Its \(k+1\) label-two positions form a cyclic list whose consecutive colors must differ, including at the single direct adjacency; each label-one position forces the third color. For \(k+1\ge3\), the list has \(2^{k+1}+2(-1)^{k+1}\) colorings. When \(k=1\), it has two vertices with unequal colors and hence \(6=2^2+2\) colorings. Multiplication by \(n\) proves the odd formula and exhausts all minima.

## Verification
The included standard-library program `verify.py` implements two differently structured finite checks. The first enumerates row/color and label-type assignments and validates every local constraint, checking the formulas for thirteen pairs with \(3\le q\le5\) and \(3\le n\le8\) within the specified finite ranges. The second constructs the Cartesian graph directly, exhaustively enumerates independent positive supports and their one/two assignments, and verifies seven parameter pairs, including \((q,n)=(3,6),(4,4),(5,3)\). Run `python verify.py`; successful output is `VERIFIED: 13 independent layer-state enumerations and 7 direct graph enumerations`. Finite checks corroborate but do not replace the preceding proof for all integers.

## Relationship to prior work
Duan et al. study independent Roman domination, establishing hardness on chordal bipartite graphs and linear-time computation for trees; their results do not concern the labeled clique–cycle family or enumeration of all optimizers. Cabrera Martínez and Hernández Mira report numerical results for some product graphs; their public abstract does not state a counting theorem, but their full text was not available for a decisive complete comparison. Gao et al. investigate *outer*-independent Roman domination on path–cycle products, a different positivity condition (independence of the zeros instead of the positive support). Earlier enumeration research by Abu-Khzam, Fernau, and Mann concerns minimal ordinary Roman dominating functions, not minimum independent Roman functions. The exact explicit labeled count and fiber-coloring classification above were not found in the accessible materials searched; this is not a claim of exhaustive bibliographic novelty.

## Limitations
The graph parameters are restricted to \(q\ge3,n\ge3\); the different two-row case is not addressed. The statements concern minimum-weight independent Roman functions, not all ordinary Roman functions. Literature that was indexed only by abstracts, or absent from the searched records, could contain equivalent results; in particular, full-text coverage of the 2023 product-graph study could not be determined. No independent validation is claimed.

## References
1. Z. Duan, H. Jiang, X. Liu, P. Wu, and Z. Shao, “Independent Roman Domination: The Complexity and Linear-Time Algorithm for Trees,” *Symmetry* **14** (2022), article 404. DOI: 10.3390/sym14020404 (public 18 February 2022).
2. A. Cabrera Martínez and F. A. Hernández Mira, “Further results on the independent Roman domination number of graphs,” *Quaestiones Mathematicae* **46** (2023), 347–357. DOI: 10.2989/16073606.2021.2014595 (abstract and bibliographic record consulted).
3. H. Gao, D. Qiu, S. Du, Y. Zhao, and Y. Yang, “Outer Independent Roman Domination Number of Cartesian Product of Paths and Cycles,” arXiv:2410.06486 (9 October 2024).
4. F. N. Abu-Khzam, H. Fernau, and K. Mann, “Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes,” *MFCS 2023*, LIPIcs **272**, article 6. DOI: 10.4230/LIPIcs.MFCS.2023.6.
