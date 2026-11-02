# Exact synchronization counts and exponential rarity for three-color cyclic automata on rook graphs

## Finding

Let \(m,n\ge2\) be arbitrary integers. On the rook graph \(R_{m,n}=K_m\square K_n\), with vertices the \(mn\) cells of an \(m\)-by-\(n\) rectangle and two cells adjacent when they share a row or column, run the synchronous three-color cyclic cellular automaton: the color at a vertex advances from \(c\in\mathbb Z/3\mathbb Z\) to \(c+1\) exactly if some neighbor currently has color \(c+1\), and otherwise remains \(c\). Write \(S_{m,n}\) for the number of labelled initial configurations that eventually become monochromatic.

Define the number of full-support \(r\)-by-\(u\) binary matrices by
\[
E(r,u)=\sum_{i=0}^{r}\sum_{j=0}^{u}(-1)^{i+j}\binom ri\binom uj2^{(r-i)(u-j)}\qquad(r,u\ge1).
\]
Then the exact count is
\[
\boxed{S_{m,n}=3\left[2^{mn}-1+\sum_{r=1}^{m-1}\sum_{u=1}^{n-1}\binom mr\binom nu E(r,u)\bigl(2^{(m-r)(n-u)}-1\bigr)\right].}
\]
This formula needs only \(O(m^2n^2)\) integer arithmetic operations when its inner inclusion–exclusion sums are evaluated directly. In particular,
\[
\boxed{S_{2,n}=3\bigl(4^n+2\cdot3^n-4\cdot2^n+1\bigr)\quad(n\ge2).}
\]
Uniformly as \(\max\{m,n\}\to\infty\), keeping \(\min\{m,n\}\ge2\),
\[
\boxed{S_{m,n}\sim 3\cdot2^{mn},\qquad
\frac{S_{m,n}}{3^{mn}}\sim 3\left(\frac23\right)^{mn}.}
\]
Thus even though these graphs have diameter two, eventual synchronization from a uniformly sampled configuration is exponentially rare in the number of vertices. Each synchronizing configuration becomes monochromatic within at most two updates; this last qualitative time bound is a prior general theorem, not a new assertion of the enumeration.

## Assumptions and scope

Graphs are undirected and simple, vertices and their initial colors are labelled, and all vertices update simultaneously. A monochromatic configuration remains monochromatic. The count is over all \(3^{mn}\) initial three-color configurations, not over color permutations or graph automorphisms. A phase shift of all colors gives a distinct initial configuration. No claim about recurrent non-synchronizing orbits is made. The primary MSC2020 class is 37B15.

## Proof

**1. The established dynamical criterion.** For three-color cyclic cellular automata on finite connected graphs, the irrotationality/synchronization theorem of Gravner–Lyu–Sivakoff states that an initial coloring synchronizes if and only if the edge increment \(\delta(u,v)\in\{-1,0,1\}\), chosen as the unique signed difference congruent to \(c(v)-c(u)\pmod3\), has zero sum on every directed cycle. Their theorem also bounds synchronization time by the graph diameter when this criterion holds. Since \(R_{m,n}\) is connected and has diameter two, its synchronization basin is exactly its irrotational colorings.

**2. Integral height representation.** Vanishing circulation is equivalent, by path integration, to an integer function \(h\) with \(h(v)-h(u)=\delta(u,v)\) on every edge. Two such functions differ by a constant. Normalize the minimum of \(h\) to zero. Because the graph has diameter two, any pair of height values differs by at most two, so \(h\) takes values in \(\{0,1,2\}\). Conversely, any array \(h\in\{0,1,2\}^{m\times n}\) whose entries in each row and in each column differ by at most one has edge increments in \(\{-1,0,1\}\) and yields an irrotational coloring \(c(i,j)=a+h(i,j)\pmod3\) for each phase \(a\in\mathbb Z/3\mathbb Z\). The phase and the minimum-zero height array are unique: edge differences recover the height up to a constant, normalization fixes that constant, and then a cell's color fixes \(a\). Thus \(S_{m,n}\) is three times the number of minimum-zero such integer arrays. On these lifted states, the cyclic update is exactly the maximum of the current height over each closed neighborhood: a vertex increases if and only if a neighbor is one level higher, and adjacent heights differ by at most one. Each successive update therefore takes a maximum over a ball of one larger radius. After two updates, every cell has the maximum of the starting height array because the rook graph has diameter two; its color is consequently uniform. This directly confirms the two-update bound without extrapolating from experiments.

**3. Exact counting.** Every minimum-zero array with no entry equal to two uses only \(\{0,1\}\), has at least one zero, and satisfies all row/column conditions. There are \(2^{mn}-1\) such arrays. If both zero and two occur, the zero and two cells cannot share a row or column. Choose the exact \(r\ge1\) rows and \(u\ge1\) columns containing zeros; then \(r\le m-1\) and \(u\le n-1\). All zero cells lie in the chosen \(r\)-by-\(u\) subrectangle, where their indicator must occupy every chosen row and every chosen column. Inclusion–exclusion over empty rows and columns gives \(E(r,u)\), with \(\binom mr\binom nu\) choices of selected row/column sets. The two cells must lie within the complementary \((m-r)\)-by-\((n-u)\) subrectangle. Any nonempty subset of that rectangle may be set to two; put one in all remaining cells. This yields \(2^{(m-r)(n-u)}-1\) possibilities. Every configuration in this decomposition is valid, and the decomposition is disjoint. Multiplication by the three phases proves the displayed sum. For \(m=2\), only \(r=1\) contributes and \(E(1,u)=1\); summing the resulting binomial expression yields the displayed closed formula. Direct evaluation of every \(E(r,u)\) costs \(O(ru)\) operations, and summing these costs over \(r<m,u<n\) gives \(O(m^2n^2)\).

**4. Uniform asymptotic bound.** Let \(A_{m,n}\) be the number of valid arrays containing both zero and two. By symmetry assume \(2\le m\le n\). Each row of such an array can be typed as a zero row, a two row, or an all-one row, because zero and two cannot share a row. For specified sets of \(r\ge1\) zero rows and \(s\ge1\) two rows (other rows all-one), each column has at most \(2^r+2^s-1\) patterns: zeros in a subset of the first set, or twos in a subset of the second set, with all-one counted once. In particular, when \(m\) is fixed,
\[
\frac{A_{m,n}}{2^{mn}}\le 3^m\left(\frac12+2^{-m}\right)^n\longrightarrow0\quad(n\to\infty).
\]
To control growing \(m\), take \(m\ge6\). At most \(2m\) row typings have \((r,s)=(m-1,1)\) or \((1,m-1)\), and their column count is at most \(2^{m-1}+1\). All other typings (at most \(3^m\)) have at most \(2^{m-2}+3\) patterns per column. Since \(n\ge m\),
\[
\frac{A_{m,n}}{2^{mn}}\le 2m\left(\frac12+2^{-m}\right)^n+3^m\left(\frac14+3\cdot2^{-m}\right)^n
\le 2m\left(\frac{33}{64}\right)^m+\left(\frac{57}{64}\right)^m\longrightarrow0.
\]
Combining bounded and unbounded \(m\) proves \(A_{m,n}=o(2^{mn})\) for every sequence \(\max\{m,n\}\to\infty\) with \(m,n\ge2\). Since \(S_{m,n}=3(2^{mn}-1+A_{m,n})\), both asymptotic statements follow.

## Verification

The standalone Python verifier `artifacts/verify_count.py` calculates the inclusion–exclusion expression and independently counts valid arrays via column-mask transfer for twelve rectangles, including \((2,2)\), \((3,3)\), \((4,4)\), \((5,5)\), and \((6,6)\). These programs agree in all cases. The output file is `artifacts/count_output.txt`.

A separately written C++17 program `artifacts/verify_dynamics.cpp` exhaustively constructs the synchronous global update transition table for seven rook graphs, namely \((2,2)\), \((2,3)\), \((2,4)\), \((2,5)\), \((2,6)\), \((3,3)\), \((3,4)\). It obtains synchronization basins by reverse reachability from constant colorings, independently of the height formula. All \(1,148,985\) labelled configurations in these test spaces were examined; their synchronization totals match the exact formula, and no synchronizing configuration requires more than two updates. Build using `g++ -O2 -std=c++17 artifacts/verify_dynamics.cpp -o verify_dynamics` and run the resulting executable. The included `artifacts/dynamics_output.txt` records the output. Finite tests are supplementary checks, not a replacement for the all-size proof.

## Relationship to prior work

Gravner, Lyu and Sivakoff's 2016 irrotationality theorem is the input establishing the synchronization criterion and diameter time bound; neither is claimed as novel here. The general identity \(\operatorname{hom}(G,P_3^{\circ})=\sum_{Z\subseteq V(G)}2^{c(G-Z)}\) for the fully looped three-vertex path is also known, in the Widom–Rowlinson model and in an earlier published exact type-count note. Indeed, the height correspondence above implies the already-available general relation \(S_G=3(\operatorname{hom}(G,P_3^{\circ})-2^{|V(G)|})\) for every connected diameter-two graph. That general relation alone does not provide the polynomial-size binomial evaluation or the uniform exponential-rate asymptotic on rook graphs, which are the contributions claimed here. An unrelated study of bootstrap growth on the Hamming plane deals with irreversible threshold dynamics rather than cyclic excitation.

The generic graph-homomorphism formula has exponentially many summands for rook graphs. Here the row/column support decomposition produces \(O(m^2n^2)\) integer-arithmetic evaluation, a nontrivial explicit specialization. Searches of published mathematical findings and scientific literature for rook-graph Widom–Rowlinson counts, row-column height arrays, and three-color cyclic synchronization did not identify the specialized formula or the uniform asymptotic. Absence from searches does not prove historical novelty.

## Limitations

The result counts only the synchronization basin, not all eventual recurrent orbits of non-synchronizing colorings. Complexity is stated in arithmetic operations on large integers, not in bit operations. The asymptotic is for \(\max\{m,n\}\to\infty\) with both dimensions at least two; it does not assert uniform relative error for tiny graphs. Relevant unindexed Widom–Rowlinson and graph-homomorphism enumeration results might contain an equivalent rook-graph formula. Scientific correctness and originality have not undergone independent external validation.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first public 2016-10-24), especially Theorem 3 and its synchronization criterion.
2. E. Cohen, W. Perkins and P. Tetali, *On the Widom–Rowlinson occupancy fraction in regular graphs*, arXiv:1512.06398v2 (2016); fully looped three-vertex-path homomorphism representation.
3. J. Gravner, D. Sivakoff and E. Slivken, *Neighborhood growth dynamics on the Hamming plane*, arXiv:1609.07202v1 (2016); related geometry but a different irreversible dynamics.
4. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, public mathematical result dated 2026-10-04; contains the generic \(\sum_Z2^{c(G-Z)}\) formula, not the present rook specialization.
