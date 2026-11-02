# Exact capacities of ternary cyclic unordered-pair profiles at prescribed composition

## Finding

Let \(C(a,b,c)\) denote the number of distinct unordered adjacent-pair histograms obtainable from indexed circular ternary strings with exactly \(a\) copies of symbol \(0\), \(b\) copies of symbol \(1\), and \(c\) copies of symbol \(2\), where \(a,b,c\ge1\). Then
\[
C(a,b,c)=[t^a u^b v^c]\,\frac{1+tuv}{(1-t)(1-u)(1-v)(1-tu)(1-tv)(1-uv)}-1-\min(a,b)-\min(a,c)-\min(b,c).
\]
In particular, for every integer \(m\ge1\),
\[
\boxed{C(m,m,m)=\frac{m(m^2+3m-2)}{2}}.
\]
This is also the exact maximum size of a zero-error code with that prescribed symbol composition when the receiver observes only these unordered pair multiplicities.

## Assumptions and scope

The alphabet is the **labeled** set \(\{0,1,2\}\). A source is a word \(w=(w_0,\ldots,w_{n-1})\), with \(n=a+b+c\); subscripts on positions are interpreted modulo \(n\). For \(0\le i\le j\le2\), define
\[
h_{ij}(w)=\#\{k:0\le k<n,\ \{w_k,w_{k+1}\}=\{i,j\}\}.
\]
The channel output is the ordered six-coordinate vector \((h_{00},h_{11},h_{22},h_{01},h_{02},h_{12})\), whose off-diagonal coordinates **combine both orientations**, not the full directed two-gram histogram. Rotations of a source give the same histogram, but no quotient by rotations or reversal is imposed on source words. Only distinct outputs are counted. The requirement \(a,b,c\ge1\) is essential to the connected-support subtraction below.

## Proof

**1. Exact graphical realizability.** Represent a histogram by a looped undirected multigraph with vertices \(0,1,2\), having \(h_{ij}\) parallel edges between \(i,j\) for \(i\ne j\), and \(h_{ii}\) loops at vertex \(i\). Reading a circular word traces a closed Euler walk through its adjacent-pair edges. Every loop counts twice toward the ordinary graph degree, so necessarily
\[
2h_{00}+h_{01}+h_{02}=2a,\quad
2h_{11}+h_{01}+h_{12}=2b,\quad
2h_{22}+h_{02}+h_{12}=2c.
\]
The off-diagonal support graph must be connected on all three vertices because all three letters occur. Conversely, a looped undirected multigraph satisfying these degree equalities and connectivity has all degrees even and admits an Euler circuit. Recording the successive vertices of this circuit gives a cyclic word with the prescribed histogram and symbol counts: each visit to vertex \(i\) contributes one to the number of occurrences of letter \(i\), which equals half the degree at \(i\). Hence these conditions are necessary and sufficient, including multiplicities and loops.

**2. Enumeration before connectivity.** Put \(x=h_{01}\), \(y=h_{02}\), \(z=h_{12}\). The three degree equations imply \(x,y,z\) have the same parity. Therefore for a unique choice of \(\delta\in\{0,1\}\) and \(i,j,k\ge0\),
\[
(x,y,z)=(2i+\delta,2j+\delta,2k+\delta),
\quad (h_{00},h_{11},h_{22})
=(a-i-j-\delta,\ b-i-k-\delta,\ c-j-k-\delta).
\]
Nonnegative loop counts give the restrictions
\[
i+j+\delta\le a,\quad i+k+\delta\le b,\quad j+k+\delta\le c.
\]
The ordinary generating function for these candidates, marking the three letter counts with \(t,u,v\), follows by multiplying the three independent loop factors, the three even cross-edge factors, and the common-parity factor:
\[
G(t,u,v)=\frac{1+tuv}{(1-t)(1-u)(1-v)(1-tu)(1-tv)(1-uv)}.
\]
There is no overcounting, because the histogram uniquely determines \(\delta,i,j,k\) and the three loop counts.

**3. Exact connectivity correction.** For \(a,b,c\ge1\), disconnected candidates comprise (i) the unique all-loop histogram, and (ii) candidates with exactly one positive cross-edge count, necessarily even. When only the edge joining symbols \(r,s\) is present, its positive multiplicity has exactly \(\min(a_r,a_s)\) choices (twice each integer from \(1\) to that minimum); loops at the isolated third vertex remain prescribed by its count. These four classes are disjoint. A graph with at least two different positive cross-edge types already connects all three labeled vertices. Hence the number of disconnected candidates is
\[
1+\min(a,b)+\min(a,c)+\min(b,c),
\]
proving the full three-variable coefficient formula.

**4. Equal-composition evaluation.** For integer \(r\ge0\), define
\[
E(r)=\#\{(i,j,k)\in\mathbb Z_{\ge0}^3:i+j\le r,\ i+k\le r,\ j+k\le r\},\qquad E(-1)=0.
\]
Splitting by \(s=i+j+k\) gives the exact finite sum
\[
E(r)=\binom{r+3}{3}+\sum_{h=1}^{\lfloor r/2\rfloor}\binom{r-2h+2}{2}.
\]
Indeed for \(s\le r\), all \(\binom{s+2}{2}\) nonnegative triples qualify; for \(s>r\), each coordinate must be at least \(s-r\), leaving \(\binom{3r-2s+2}{2}\) triples, indexed by \(h=s-r\). Directly summing squares and linear terms over the two parities yields
\[
E(r)=\begin{cases}
\frac{(r+2)(2r^2+5r+4)}{8},&r\text{ even},\\[2pt]
\frac{(r+1)(2r^2+7r+7)}{8},&r\text{ odd}.
\end{cases}
\]
For \(a=b=c=m\), the contributions of \(\delta=0,1\) are respectively \(E(m),E(m-1)\), with
\[
E(m)+E(m-1)=\frac{(m+1)(m^2+2m+2)}{2}.
\]
Removing the \(3m+1\) disconnected candidates now proves
\[
C(m,m,m)=\frac{m(m^2+3m-2)}{2}.
\]
The constructive Euler-circuit step in part 1 also shows every counted profile is realized, so the number of nonconfusable codewords is exactly this count: select one source per distinct output, and no code can contain two sources with the same output.

## Verification

Run \(\texttt{python3 verify.py}\) using the standard Python library. The supplied standalone program directly enumerates all indexed ternary circular words for lengths \(3\) through \(11\), partitions by all-positive compositions, and compares their observed histogram sets with the graph parameterization and coefficient formula. It additionally constructs and checks explicit Eulerian words for every predicted profile with \(1\le a,b,c\le5\), and checks the balanced cubic formula at \(1\le m\le150\). The executed program returned \(165\) composition-class checks, \(2427\) Eulerian witnesses, and passed every test. These finite tests support, but do not replace, the unrestricted proof above.

The first balanced values are \(1,8,24,52,95,156,238,344\) for \(m=1,\ldots,8\).

## Relationship to prior work

Kiah–Puleo–Milenkovic [1] introduce sequence profiles based on the **ordered** multiplicities of length-\(\ell\) factors, including flow constraints. Raviv–Schwartz–Yaakobi [2] analyze feasible **rank permutations** of the full ordered profile. Jacquet–Knessl–Szpankowski [3] count directed Markov types via balanced **directed** frequency matrices, principally asymptotically as total length varies. None of those statements identifies the image cardinality after collapsing opposite off-diagonal directions and simultaneously fixing all three source-symbol counts. The rank constraints and directed profile counts do not imply this exact unordered-composition polynomial. Immink–Cai [4] discuss composition and run-length constraints but do not count such observational equivalence classes. Bulgakova–Buzhinsky–Goncharov [5] consider circular-word balancedness and abelian properties in different senses, not frequency-multiplicity profiles of unordered adjacent pairs.

The undirected Euler-circuit criterion itself is classical and is not claimed as a new graph theorem; the proposed contribution is the exact fixed-composition image enumeration and its cubic equal-composition specialization.

## Limitations

This is a noiseless, complete-coverage, position-agnostic read profile; errors, dropped reads, partial coverage, and longer factors are not treated. Symbol labels are preserved and \(a,b,c\) are positive. The all-composition formula is a coefficient extraction rather than a single piecewise polynomial for arbitrary unbalanced triples. The result counts distinct outputs; it does not count distinct circular necklaces or determine the sizes of all source fibers. The exact overlap of this symmetrized statistic with specialized unindexed literature is not proven absent, and no independent scientific audit has occurred.

## References

1. H. M. Kiah, A. J. Puleo, and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517, first public February 2, 2015. https://arxiv.org/abs/1502.00517
2. N. Raviv, M. Schwartz, and E. Yaakobi, *Rank-Modulation Codes for DNA Storage*, arXiv:1708.02146, first public August 7, 2017. https://arxiv.org/abs/1708.02146
3. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, Discrete Mathematics and Theoretical Computer Science, AofA 2010, pages 387–400. https://dmtcs.episciences.org/articles/2768
4. K. A. S. Immink and K. Cai, *Properties and Constructions of Constrained Codes for DNA-Based Data Storage*, arXiv:1812.06798, first public December 14, 2018. https://arxiv.org/abs/1812.06798
5. D. Bulgakova, S. Buzhinsky, and A. Goncharov, *On Balanced and Abelian Properties of Circular Words Over a Ternary Alphabet*, arXiv:2012.15818, first public December 31, 2020. https://arxiv.org/abs/2012.15818
