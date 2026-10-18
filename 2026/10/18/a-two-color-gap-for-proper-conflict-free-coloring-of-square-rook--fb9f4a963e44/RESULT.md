# A two-color gap for proper conflict-free coloring of square rook graphs

## Finding

**Theorem.** For every pair of integers \(m,n\geq 2\), let \(R_{m,n}=K_m\square K_n\), the rook graph on an \(m\)-by-\(n\) board (equivalently, the line graph of \(K_{m,n}\)). For proper vertex colorings in which every nonisolated vertex has some color represented **exactly once in its open neighborhood**, the optimal palette size is

\[
\chi_{\mathrm{pCFo}}(R_{m,n})=\begin{cases}
\max\{m,n\},&m\ne n,\\
n+2,&m=n.
\end{cases}
\]

The same formula holds for the **proper odd chromatic number**, which requires a color represented an odd number of times in every open neighborhood. Hence the ordinary chromatic number \(\chi(R_{n,n})=n\) underestimates both neighborhood-sensitive parameters by precisely two for **every** square order \(n\ge2\), whereas rectangular rook graphs have no gap.

## Assumptions and scope

All graphs are finite, simple, undirected, and have no loops. The vertices of \(R_{m,n}\) are board cells \((i,j)\) with \(0\le i<m\) and \(0\le j<n\); two distinct cells are adjacent precisely when they share a row or column. A proper coloring assigns distinct colors within every row and within every column. A proper conflict-free *open-neighborhood* coloring requires, for each cell, at least one color occurring exactly once among its graph neighbors; the cell itself is excluded. The number of available colors is minimized. For this theorem \(m,n\ge2\); no claim about isolated vertices or the closed-neighborhood convention is made.

## Proof

**1. Palette criterion.** Represent a proper coloring by an \(m\)-by-\(n\) matrix \((c_{ij})\). Let \(A_i\) be the set of colors in row \(i\), and \(B_j\) the colors in column \(j\). A neighbor of \((i,j)\) lies in its own row or its own column, but not both. Because the coloring is proper, a color occurs once among those neighbors if and only if it lies in the symmetric difference \(A_i\mathbin\triangle B_j\). (The color \(c_{ij}\) lies in both sets and does not occur among the neighbors.) Thus

\[
(c_{ij})\text{ is proper conflict-free}\quad\Longleftrightarrow\quad A_i\ne B_j\ \text{for all }i,j.
\]

Each neighborhood color occurs zero, once, or twice. Therefore the same equivalence holds for the proper odd-neighborhood condition.

**2. Rectangular boards.** By symmetry assume \(2\le m<n\). A row clique has \(n\) vertices, so at least \(n\) colors are necessary. Assign \(c_{ij}=i+j\pmod n\) for \(0\le i<m\), \(0\le j<n\). Every row uses all \(n\) colors; every column uses exactly \(m<n\) colors, all distinct. Consequently \(A_i\ne B_j\) for every cell, and \(n\) colors suffice. Swapping coordinates covers \(m>n\).

**3. Square-board lower bound.** Let \(m=n=s\ge2\). Every proper coloring needs at least \(s\) colors. If it uses at most \(s+1\), regard its color labels as drawn from a fixed palette \(\mathcal P\) of size \(s+1\), adding an unused formal color if necessary. Each row and column uses exactly \(s\) distinct labels and so misses exactly one label. Denote the missing label of row \(i\) by \(a_i\), and of column \(j\) by \(b_j\). For each \(\alpha\in\mathcal P\), counting its occurrences by rows gives \(s-\#\{i:a_i=\alpha\}\), while counting by columns gives \(s-\#\{j:b_j=\alpha\}\). The counts agree. Hence the two nonempty multisets \((a_i)\) and \((b_j)\) are equal, and in particular there exist \(i,j\) with \(a_i=b_j\). Then \(A_i=\mathcal P\setminus\{a_i\}=\mathcal P\setminus\{b_j\}=B_j\), contradicting Step 1. Thus at least \(s+2\) colors are needed.

**4. Square-board construction.** Set \(k=s+2\). When \(s=2\), use the matrix

\[
\begin{pmatrix}0&1\\2&3\end{pmatrix}.
\]

When \(s=4\), use the six-color matrix

\[
\begin{pmatrix}
0&1&2&3\\2&3&5&4\\5&4&3&2\\4&5&1&0
\end{pmatrix}.
\]

Its four row-omitted two-element subsets (relative to \(\{0,1,2,3,4,5\}\)) are \(\{4,5\},\{0,1\},\{0,1\},\{2,3\}\), while its column-omitted subsets are \(\{1,3\},\{0,2\},\{0,4\},\{1,5\}\); the families are disjoint, so Step 1 applies. Direct inspection also shows distinct entries within each row and column.

For every remaining \(s\ge3\), choose a residue \(q\) modulo \(k\) such that \(\gcd(q,k)=1\) and \(q\not\equiv\pm1\pmod{k}\), as follows:

\[
q=\begin{cases}
2,&s\text{ odd},\\
k/2-1,&s\text{ even and }k\equiv0\pmod4,\\
k/2-2,&s\text{ even and }k\equiv2\pmod4.
\end{cases}
\]

In the first case \(k\ge5\) is odd. In the second, \(k\ge8\) and \(q=k/2-1\) is coprime to \(k\). In the third, \(k\ge10\), \(k=4t+2\) and \(q=2t-1\), whence \(\gcd(q,k)=1\) since \(\gcd(2t-1,4t+2)=\gcd(2t-1,4)=1\). In every case the proposed \(q\) differs from \(\pm1\) modulo \(k\).

Define, for \(0\le i,j<s\),

\[
c_{ij}\equiv i+qj\pmod k.
\]

Each row contains \(s=k-2\) consecutive multiples of the unit \(q\), hence distinct labels; each column contains \(s\) consecutive labels, hence distinct. Relative to all \(k\) colors, the two missing symbols from row \(i\) are \(\{i+qs,i+q(s+1)\}\pmod k\), whose differences are \(\pm q\), whereas the two missing symbols from column \(j\) are \(\{s+qj,s+1+qj\}\pmod k\), whose differences are \(\pm1\). Since \(q\not\equiv\pm1\pmod k\), no row-omission pair can equal a column-omission pair. Thus no row palette equals a column palette. Step 1 proves conflict-freeness with at most \(s+2\) colors, which is optimal by Step 3. The odd-coloring statement follows from Step 1. \(\square\)

## Verification

The standard-library script `check_rook_pcf.py` constructs the prescribed matrices and directly examines every graph-neighborhood color multiplicity, without using the proof's row/column palette criterion. It checked every pair \(2\le m,n\le20\), plus square orders \(21\le n\le120\), totaling \(461\) constructed cases. It also enumerates **all functions**, not only proper ones, from a three-color palette to the \(2\)-square and a four-color palette to the \(3\)-square and confirms none is valid. Run `python3 check_rook_pcf.py`; its recorded output is in `verification_output.txt`. Finite tests only corroborate the formulas; the infinite result follows from the proof above.

## Relationship to prior work

Fabrici, Lužar, Rindošová, and Soták introduced the proper conflict-free open-neighborhood framework (2022, arXiv:2202.02570), studying mainly planar graphs. Cho, Choi, Kwon, and Park's broader theory of relaxations of square coloring (2023, arXiv:2302.06125) proves that proper odd and proper conflict-free chromatic numbers agree for quasi-line graphs and gives a general upper bound \(\frac32\Delta+2\), which applies but does not produce this exact rook-graph formula. Jiménez and collaborators (first public 2023, arXiv:2308.00170) prove a sharper general quasi-line upper bound \(\Delta+4\), also insufficient to fix the precise rook values. Dujmović, Morin, and Odak (2022, arXiv:2202.12882) develop bounded odd coloring for graphs with product structure under distinct assumptions, not this exact family. Liu, Dou, and Yang (2026, DOI:10.3934/math.2026056) determine odd chromatic numbers for several Cartesian products involving paths and cycles and give other product bounds; their stated classifications do not include complete-by-complete rook products. Existing Latin-square and Latin-rectangle representations of proper rook colorings yield \(\chi(R_{m,n})=\max\{m,n\}\), but do not by themselves decide the open-neighborhood witness condition. The new claim is the exact two-regime proper conflict-free/odd formula and its uniform constructions; general definitions, quasi-line equality, and ordinary chromatic numbers are not claimed as new.

## Limitations

This covers only complete-by-complete Cartesian products with each factor of order at least two, **proper** colorings, and **open** neighborhoods; it does not determine the analogous closed-neighborhood or improper conflict-free parameters, nor arbitrary line graphs or higher-dimensional Hamming graphs. Relevant accessible primary statements and mathematical research summaries were compared, but an unindexed or overlooked equivalent enumeration or product theorem could supersede the novelty assessment. Independent scientific validation has not been performed.

## References

1. I. Fabrici, B. Lužar, S. Rindošová, R. Soták, *Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods* (first public 2022-02-05), arXiv:2202.02570, https://arxiv.org/abs/2202.02570.
2. E.-K. Cho, I. Choi, H. Kwon, B. Park, *Brooks-type theorems for relaxations of square colorings* (first public 2023-02-13), arXiv:2302.06125, https://arxiv.org/abs/2302.06125.
3. V. Dujmović, P. Morin, S. Odak, *Odd Colourings of Graph Products* (first public 2022-02-25), arXiv:2202.12882, https://arxiv.org/abs/2202.12882.
4. A. Jiménez et al., *Boundedness for proper conflict-free and odd colorings* (first public 2023-07-31), arXiv:2308.00170, https://arxiv.org/abs/2308.00170.
5. B. Liu, Q. Dou, F. Yang, *The odd coloring of some Cartesian product graphs*, AIMS Mathematics **11** (2026), 1311–1331, DOI:10.3934/math.2026056, https://doi.org/10.3934/math.2026056.
