# Exact distance-two vertex colouring of Möbius ladders

## Finding

For each integer \(n\ge 3\), let \(M_{2n}\) be the graph on \(\mathbb Z/(2n)\mathbb Z\) with edges from \(i\) to \(i+1\) and to \(i+n\), modulo \(2n\). Let \(G^2\) join distinct vertices whenever their distance in \(G\) is at most two. Then

\[
\chi(M_{2n}^{2})=
\begin{cases}
6,&n=3\\
8,&n=4\\
6,&n=8\\
4,&n\ge6\text{ and }n\equiv2\pmod4\\
5,&\text{all remaining }n\ge5.
\end{cases}
\]

In particular, the infinite four-colourable class is exactly the class of Möbius ladders admitting a perfect one-error-correcting vertex code; apart from the three small exceptional widths, every other ladder needs exactly five colours. The correspondence between efficient domination and the four-colour *obstruction* is elementary; efficient domination of Möbius ladders itself was previously classified [3]. The result here determines the full square-chromatic number, including the five-colour constructions and the sixteen-vertex exceptional obstruction.

## Assumptions and scope

All graphs are finite, undirected and simple. Distance-two colouring here means **distance at most two**, not colouring only vertices at distance exactly two. Vertex colours are named integers, and the chromatic number does not distinguish colour permutations. The parameter \(n\) counts antipodal pairs (rungs), so the graph has \(2n\) vertices. No assertion is made for \(n<3\).

Write a two-row colouring word of length \(n\) as \((a_0,b_0),\ldots,(a_{n-1},b_{n-1})\), where vertices \(i\) and \(i+n\) receive colours \(a_i\) and \(b_i\). Consecutive columns have parallel horizontal edges except at the final-to-first seam, which has crossed horizontal edges. This is a twisted (Möbius), not an untwisted circular, ladder.

## Proof

**Lower bounds.** In any cubic graph, the closed neighbourhood of each vertex is a clique of size four in its square. Therefore, if the square admits a colouring with four colours, every closed neighbourhood contains all four colours exactly once. Each colour class is consequently an *efficient dominating set* (perfect radius-one code): its closed neighbourhoods partition the graph.

No such code exists in \(M_{2n}\) unless \(n\equiv2\pmod4\). Here is a self-contained necessity proof. Let \(x_i\in\{0,1\}\) indicate membership in a code. Efficiency requires
\[
x_{i-1}+x_i+x_{i+1}+x_{i+n}=1\quad(i\bmod 2n).
\]
Adding these equations over all \(2n\) vertices gives \(4\sum_i x_i=2n\), so \(n\) must be even. If \(n\equiv0\pmod4\), put \(z_i=x_i-x_{i+n}\). Subtracting the equations indexed by \(i\) and \(i+n\) yields \(z_{i-1}+z_{i+1}=0\); hence \(z_{i+4}=z_i\). Since \(n\) is a multiple of four, \(z_{i+n}=z_i\), but by definition \(z_{i+n}=-z_i\). Thus \(z_i=0\) for all \(i\). The efficiency equation reduces to \(x_{i-1}+2x_i+x_{i+1}=1\), which precludes any \(x_i=1\), a contradiction. Consequently four colours are impossible if \(n\not\equiv2\pmod4\). This code characterization was also established by Knor and collaborators [3]; the argument is included to make the colouring proof independent.

When \(n=8\), an independent set of four vertices in \(M_{16}^2\) would have four disjoint four-vertex closed neighbourhoods in \(M_{16}\), necessarily constituting an efficient dominating set. As none exists, \(\alpha(M_{16}^2)\le3\), and the elementary chromatic lower bound gives \(\chi(M_{16}^2)\ge\lceil16/3\rceil=6\).

For \(n=3\), the original graph is \(K_{3,3}\) and its square is \(K_6\). For \(n=4\), the eight-vertex Wagner graph has diameter two and its square is \(K_8\). These prove the exceptional lower bounds.

**Four-colour construction.** For every \(n\ge6\) with \(n\equiv2\pmod4\), colour vertex \(i\) with residue \(i\bmod4\). Every difference of endpoints of a path of length at most two is, modulo \(2n\), one of \(\pm1,\pm2,n,n\pm1\); since \(n\equiv2\pmod4\), all these differences are nonzero modulo four. Thus the colouring is valid.

**Five- and six-colour constructions.** The following words give complete finite colourings, with each pair denoting one column and the crossed final-to-first seam understood:

\[
\begin{array}{c|l}
 n& (a_i,b_i),\quad i=0,\ldots,n-1\\\hline
5&(0,4),(1,3),(2,0),(3,4),(1,2)\\
7&(0,2),(1,3),(2,0),(3,4),(0,1),(4,2),(1,3)\\
8&(0,2),(1,3),(2,0),(3,1),(0,5),(4,2),(5,3),(1,4)\\
9&(0,2),(1,3),(2,0),(3,1),(0,2),(1,3),(4,0),(3,2),(1,4)\\
12&(0,2),(1,3),(2,0),(3,1),(0,2),(4,3),(1,0),(2,4),(0,3),(4,1),(3,2),(1,4).
\end{array}
\]

Every word except the \(n=8\) word uses only colours \(0,1,2,3,4\); that exceptional word uses \(0,\ldots,5\). Their validity follows by checking for each vertex the colours within graph distance at most two, as implemented independently by the two attached stand-alone programs.

To obtain arbitrary larger lengths, take any of the three base words with \(n=7,9,12\). Write it as \(Q R\), with \(Q\) its first four columns. The two-row word \(Q Q R\) is again a proper square colouring, verified explicitly by the same local check. More generally, \(Q^kR\) is proper for every integer \(k\ge1\): all horizontal or rung paths of length at most two occur in at most three consecutive columns, with a possible row swap only at the crossed last-to-first seam. Each three-column local pattern inside \(Q^kR\) already occurs in \(Q R\) or \(Q Q R\); the three-column patterns across the unique twisted seam are identical in all words because \(Q\) is the initial block and the final two columns of \(R\) are unchanged. Since \(|R|\ge3\) for all three bases, the two interfaces cannot interact through a length-two path. Therefore the finite checks prove the whole infinite extension, not just finitely many examples.

The lengths \(7+4j\), \(9+4j\) and \(12+4j\), for \(j\ge0\), cover all odd lengths at least seven and all multiples of four at least twelve. Together with the \(n=5\) word, the \(n=8\) six-colour word, the four-residue family and the two complete-graph cases, this proves the formula for all \(n\ge3\).

## Verification

Run `python3 constructive_check.py` and `python3 independent_check.py` with Python 3 and no external dependencies. The first generates square-graph distance conflicts directly from the circular model and checks the five finite words, twelve successive four-column extensions of each base, and 25 representative residue-four cases. The second independently constructs the graph as two paths with crossed end links, checks all base colourings, exhaustively finds no independent four-set in the sixteen-vertex square, and exhaustively excludes the stated smaller colour counts for selected small widths. These finite tests support the exact boundary instances and the local extension step; the proof above establishes the infinite statement.

## Relationship to prior work

Petrosyan [1] determines *interval edge colouring* properties of Möbius ladders, not the chromatic number of their vertex-square graphs. Sopena and Wu [2], including their discussion of the earlier Chiang–Yan theorem, study the square-colouring problem for untwisted Cartesian grid and torus products. The Möbius ladder has a crossed boundary, so those graph families do not include its square-colouring classification. Knor, Potočnik and collaborators [3, Lemma 2.2] already characterize efficient dominating sets in Möbius ladders, and this established ingredient is explicitly credited; existence or nonexistence of a perfect code alone does not provide the five-colour upper bounds or the special six-colour obstruction at \(n=8\). Yang and Wu [4] determine *strong edge* chromatic indices, a different adjacency-conflict graph and invariant. No publication-priority claim of uniqueness beyond the sources checked is made.

## Limitations

The lower bound for the exceptional sixteen-vertex case uses packing and the known efficient-code obstruction rather than a general lower bound of six for the remaining family. The extension depends on the explicitly given base colourings; it does not classify all optimal colourings. The source comparison covers accessible principal statements and material but is not an exhaustive survey of unindexed publications; the full publisher PDF of [3] was not available through the consulted reading route. Independent external scientific validation remains outstanding.

## References

[1] P. A. Petrosyan, *Interval Edge Colorings of Mobius Ladders*, arXiv:0801.0159, first publicly posted 2007-12-31, https://arxiv.org/abs/0801.0159.

[2] É. Sopena and J. Wu, *Coloring the square of the Cartesian product of two cycles*, 2009 manuscript, https://www.labri.fr/perso/sopena/sw09a_v1.pdf.

[3] M. Knor, P. Potočnik, et al., *Efficient domination in cubic vertex-transitive graphs*, European Journal of Combinatorics 33 (2012), 1755–1764, DOI:10.1016/j.ejc.2012.04.007 (notably Lemma 2.2 on Möbius ladders).

[4] Z. Yang and B. Wu, *Strong edge chromatic index of the generalized Petersen graphs*, Applied Mathematics and Computation 321 (2018), 431–441, DOI:10.1016/j.amc.2017.10.047. For the Möbius-ladder strong edge index, see *Strong chromatic index of Möbius ladders*, Journal of Mathematics (Chinese), 2018, https://sxzz.whu.edu.cn/html/2018/3/20180313.htm.
