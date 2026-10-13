# Fano-plane rigidity of optimal seven-symbol four-multiset deletion codes

## Finding
Let \(P=\{0,1,2,3,4,5,6\}\). A profile is \(x\in\mathbb Z_{\ge0}^{P}\) with \(\sum_{i\in P}x_i=4\). A code \(C\) corrects one deletion of an **unordered** multiset if no two different profiles have a common three-symbol submultiset.

Every maximum such code has exactly \(35\) profiles and has the following form for a Steiner triple system \(\mathcal F\) on \(P\):
\[
C_{\mathcal F}=\{4e_i:i\in P\}\ \cup\ \{2e_i+2e_j: i,j\in P,\ i<j\}\ \cup\ \Big\{\sum_{i\in P\setminus L}e_i:L\in\mathcal F\Big\}.
\]
Here a Steiner triple system on seven points is the Fano plane: seven triples, each unordered pair in exactly one triple. Conversely every such system produces an optimal code. There are exactly \(30\) distinct optimal codes on the **labeled** alphabet, forming one orbit under the full symbol-permutation group. Every optimal code contains the same \(28\) even-coordinate profiles, and the group preserving any one optimal code has order \(168\).

The previously known maximum cardinality \(35\) and the Fano-based construction are not new. The assertion that **these exhaust all optimal codes**, with its precise orbit and common-core classification, is the finding.

## Assumptions and scope
The alphabet is the fixed labeled seven-set \(P\); all profiles have total multiplicity four; exactly one occurrence of any symbol may be deleted. The received object is a multiset (multiplicity vector), not an ordered sequence. Two profiles \(u,v\) share a possible three-symbol deletion output if and only if \(\sum_i\min(u_i,v_i)\ge3\). Hence the coding condition is that, for distinct codewords, \(\sum_i\min(u_i,v_i)\le2\), equivalently \(\|u-v\|_1\ge4\).

## Proof
**The upper bound and equality conditions.** Partition weight-four profiles into five multiplicity types \((1,1,1,1)\), \((2,1,1)\), \((2,2)\), \((3,1)\), and \((4)\), with respective numbers \(x,y,z,a,b\) in a code.

Supports of distinct \((1,1,1,1)\)-words are four-subsets meeting in at most two points. There are at most seven: every such four-subset contains four triples, no triple appears twice, and only \(\binom73=35\) triples exist, so at most eight blocks. Eight blocks are impossible. They would have a total of \(32\) point incidences; writing the seven point degrees as \(d_i\), convexity gives \(\sum_i\binom{d_i}{2}\ge 4\binom52+3\binom42=58\), whereas pairwise block intersections of size at most two give \(\sum_i\binom{d_i}{2}\le2\binom82=56\). Thus \(x\le7\).

Different \((3,1)\) and \((4)\) words cannot put their entry at least three in the same coordinate, since they would share multiplicity at least three. Thus \(a+b\le7\).

An **ordered arc** \((i,j)\), \(i\ne j\), is used by a word \(u\) when \(u_i\ge2\) and \(u_j\ge1\). Distinct codewords cannot use the same arc, for then they share at least two occurrences at \(i\) and one at \(j\). A word of type \((2,1,1)\), \((2,2)\), or \((3,1)\) uses respectively two, two, or one arcs. There are \(7\cdot6=42\) arcs. Hence \(2y+2z+a\le42\), so
\[
|C|=x+y+z+a+b\le7+\frac{42-a}{2}+7\le35.
\]
If equality holds, then \(x=7\), \(a=0\), \(b=7\), \(y+z=21\), and every ordered arc is used exactly once. In particular all seven pure powers \(4e_i\) occur.

**The squarefree layer is a Fano plane.** Let \(Q_1,\ldots,Q_7\) be supports of the seven squarefree words. They each have four points and pairwise meet in at most two. Their point degrees total \(28\), so \(\sum_i\binom{d_i}{2}\ge7\binom42=42\); the pairwise-intersection bound gives at most \(2\binom72=42\). Both inequalities are equalities. Therefore each point has degree four and every two distinct blocks meet in exactly two points. Their complements \(L_r=P\setminus Q_r\) are seven triples with pairwise intersection exactly one. No pair of points can occur in two triples, and the seven triples contain all \(7\binom32=21\) unordered pairs. Thus \(\mathcal F=\{L_r\}\) is a Steiner triple system \(S(2,3,7)\), necessarily a Fano plane.

**No mixed \((2,1,1)\) words survive.** If a word \(u\) of type \((2,1,1)\) belongs to \(C\), its three-point support \(S\) cannot be contained in any \(Q_r\), since it would share at least three occurrences with the corresponding squarefree codeword. Thus \(S\) meets every Fano line. Any three-point subset of a Fano plane meeting every line is itself a line. Indeed, identify its points with the nonzero elements of \(\mathbb F_2^3\) and its lines with triples summing to zero. If \(S=\{r,s,t\}\) is not a line, \(r,s,t\) are linearly independent; the line \(\{r+s,s+t,t+r\}\) is disjoint from \(S\). This is a contradiction. Hence every type \((2,1,1)\) support must be a Fano line.

Fix two distinct symbols \(i,j\). If the code omits \(2e_i+2e_j\), then neither of the ordered arcs \((i,j)\) and \((j,i)\) is used by such a \((2,2)\) word. Since all arcs are used, the first must occur in a \((2,1,1)\) word doubled at \(i\), and the second in a \((2,1,1)\) word doubled at \(j\). Both words have support equal to the unique Fano line containing \(\{i,j\}\). Their common multiplicity is at least one at each of that line's three points, violating the deletion-correcting condition. Thus every one of the \(\binom72=21\) pair-square words \(2e_i+2e_j\) occurs. Since \(y+z=21\), no \((2,1,1)\) words occur. The displayed form of \(C_{\mathcal F}\) is forced.

**Attainment, enumeration and symmetry.** In the displayed construction, distinct pure-fourth powers, distinct pair-squares, and mixed comparisons have common multiplicity at most two. Fano lines have pairwise intersection one, so their four-point complements meet in two points; the corresponding squarefree words are also compatible. Thus every \(C_{\mathcal F}\) is a one-deletion-correcting code of size \(7+21+7=35\).

Every Steiner triple system on seven labeled points is isomorphic to the Fano plane. Realize it on the seven nonzero vectors of \(\mathbb F_2^3\), with lines \(\{r,s,r+s\}\). Its automorphism group is \(\mathrm{GL}(3,2)\), of order \((8-1)(8-2)(8-4)=168\); the number of labeled planes is therefore \(7!/168=30\). Distinct planes yield distinct squarefree layers, hence distinct codes. Symbol permutations act transitively and the code stabilizer has order \(168\), proving the enumeration and orbit statements.

## Verification
The included standalone standard-library `verify.py` enumerates all \(\binom73=35\) candidate triples, exact-covers all \(\binom72=21\) pairs, and obtains exactly \(30\) labeled Fano planes. For each it constructs the indicated \(35\)-profile code and verifies all pairwise \(\ell_1\) distances. A second direct permutation check produces one orbit of size \(30\). The program also verifies the arc counts for all \(\binom{10}{6}=210\) weak compositions of four into seven coordinates. Running `python3 verify.py` printed `VERIFY_OK`. The unrestricted optimality and exhaustiveness are established by the preceding symbolic proof, not inferred from enumeration.

An explicit model of the seven Fano lines, on symbols \(0,1,\dots,6\), is `012`, `034`, `056`, `135`, `146`, `236`, `245`; each line corresponds to its complementary squarefree four-set in the code.

## Relationship to prior work
Chen, Ma and Zhang give the general weight-four \(\ell_1\)-code size formula and a packing construction (Theorem III.2, arXiv:2003.00483). The special value \(35\) and the existence of the even-coordinate-plus-Fano construction follow from their work. Machacek (arXiv:2010.11112) studies the number of maximum independent sets for analogous monomial graphs and proves rigidity in three and four variables, but gives no count in seven variables at degree four. Kreindel, Essayag and Zabokritskiy (arXiv:2601.05636, first posted January 9, 2026, primary MSC 94B25) develop single-deletion codes for unordered multisets and address uniqueness for smaller alphabets. Zabokritskiy (arXiv:2607.13733) establishes the optimal seven-alphabet cardinalities and uses Fano constructions, without classifying every optimizer at this degree in the inspected manuscript. The distinction here is **necessity and complete labeled classification** of the Fano construction, not the cardinality or its existence.

## Limitations
The conclusion is specific to one unordered deletion of a size-four multiset on exactly seven symbols. It does not classify ordered-sequence deletion codes or the maximum families at other weights or alphabet sizes. The literature review checked the identified primary manuscripts and indexed mathematical records; an earlier unindexed optimizer census could still exist. 

## References
1. T. Chen, Y. Ma, X. Zhang, *Optimal codes with small constant weight in \(\ell_1\)-metric*, arXiv:2003.00483 (2020), Theorem III.2, https://arxiv.org/pdf/2003.00483.
2. J. Machacek, *Unique maximum independent sets in graphs on monomials of a fixed degree*, arXiv:2010.11112 (2020), Section 4.1, https://arxiv.org/pdf/2010.11112.
3. A. Kreindel, I. B. Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636 (January 9, 2026), https://arxiv.org/html/2601.05636v2.
4. A. L. Zabokritskiy, *Independent Sets in Multiset Profile Graphs via Weighted Local Covers*, arXiv:2607.13733 (2026), Section 7, https://arxiv.org/pdf/2607.13733.
