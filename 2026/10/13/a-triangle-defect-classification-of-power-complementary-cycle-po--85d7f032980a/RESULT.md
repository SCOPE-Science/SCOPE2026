# A triangle-defect classification of power–complementary cycle powers

## Finding

For every integer \(n\geq3\), every integer \(k\geq1\), and every integer \(p\geq2\), the following equivalence holds:

\[
  (C_n^k)^p\cong\overline{C_n^k}
  \quad\Longleftrightarrow\quad
  k=1\ \text{and}\ n=2p+3.
\]

Thus the positive examples among all powers of cycles consist precisely of the ordinary odd cycles \(C_{2p+3}\), one for each exponent \(p\geq2\). The square case includes the previously known \(C_7\), and the cube case includes the previously known \(C_9\); these individual positive examples are not claimed as new.

More precisely, if \(k\geq1\), \(p\geq2\), and \(n=2(p+1)k+1\), then \(H=(C_n^k)^p\) and \(J=\overline{C_n^k}\) have the same degree but their triangle counts satisfy the exact identity

\[
  t(H)-t(J)=\frac{n k(k-1)}2,
\]

where \(t(X)\) is the number of unordered three-vertex cliques of \(X\). The defect is strictly positive for \(k\geq2\), giving a simple invariant obstruction that applies simultaneously to every exponent \(p\geq2\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Vertices of \(C_n\) are \(\mathbb Z/n\mathbb Z\), with edges between residues at cyclic distance one. The graph \(C_n^k\) joins distinct vertices at cyclic distance at most \(k\). Exponentiation of a graph means its ordinary graph-distance power; \(\overline G\) denotes the simple complement, and \(\cong\) an unlabelled graph isomorphism. The parameters have the full ranges \(n\geq3\), \(k\geq1\), \(p\geq2\), including complete cycle powers and powers that become complete. An assertion about triangle counts at the degree-equality parameter \(n=2(p+1)k+1\) does not claim that the graphs are already isomorphic.

## Proof

**1. A necessary degree equation.** For any \(n,k,p\), the distance structure of a cycle gives \((C_n^k)^p=C_n^{pk}\): traversing at most \(p\) jumps, each of cyclic distance at most \(k\), is equivalent to cyclic distance at most \(pk\). If \(C_n^k\) is complete, then its power is complete and its complement edgeless, so the two are not isomorphic for \(n\geq3\). If \(C_n^k\) is not complete but \(C_n^{pk}\) is complete, the same conclusion holds because the complement contains at least one edge. Otherwise both \(k\) and \(pk\) are strictly less than \(\lfloor n/2\rfloor\); \(C_n^{pk}\) has degree \(2pk\), whereas \(\overline{C_n^k}\) has degree \(n-1-2k\). An isomorphism therefore requires

\[
   2pk=n-1-2k,
   \qquad\text{hence}\qquad n=2(p+1)k+1.
\]

At this candidate order, put \(r=pk\). We have \(n>2r\), so all cyclic gaps of length at most \(r\) are unambiguously short.

**2. Count triangles in the powered cycle.** Represent a triangle by its three vertices in cyclic order and their positive consecutive cyclic gaps \((a,b,c)\), with \(a+b+c=n\). An edge belongs to \(C_n^r\) precisely when its associated directed gap is either at most \(r\) or at least \(n-r\). Since \(n>2r\), at most one of the three gaps can be at least \(n-r\). If exactly one is that large, the three vertices lie in a cyclic interval of length at most \(r\). Its unique first vertex after the large gap has \(\binom r2\) choices of two further offsets. Thus these triangles number \(n\binom r2\).

If no gap is large, all three gaps lie between one and \(r\). Write \(a=r-u\), \(b=r-v\), \(c=r-w\). The nonnegative deficits satisfy

\[
  u+v+w=3r-n=(p-2)k-1.
\]

For \(p=2\), the right side is negative, and there are no such triangles. For \(p\geq3\), its nonnegative solutions automatically have \(u,v,w<r\), and there are \(\binom{(p-2)k+1}{2}\) solutions. Each unordered triangle is represented by exactly three cyclic choices of first vertex. Consequently, including the valid zero contribution for \(p=2\),

\[
 t(C_n^r)=n\binom r2+\frac n3\binom{(p-2)k+1}{2}.
\]

**3. Count triangles in the complement.** Three vertices in cyclic order form a triangle of \(\overline{C_n^k}\) if and only if each consecutive cyclic gap is at least \(k+1\). Necessity follows because a smaller gap would be an edge in \(C_n^k\). For sufficiency, the other two gaps are also at least \(k+1\), so no gap can reach \(n-k\) and thereby create a short reverse distance. Subtracting \(k+1\) from each gap leaves nonnegative numbers with total

\[
 n-3(k+1)=(2p-1)k-2.
\]

There are \(\binom{(2p-1)k}{2}\) ordered gap triples. As before, each triangle is counted three times among starting vertices, giving

\[
  t(\overline{C_n^k})=\frac n3\binom{(2p-1)k}{2}.
\]

**4. Simplify the triangle defect.** Subtract the two exact counts, substitute \(r=pk\), and expand:

\[
\begin{aligned}
\frac{6}{n}\bigl[t(C_n^{pk})-t(\overline{C_n^k})\bigr]
 &=3pk(pk-1)+((p-2)k+1)(p-2)k\\
 &\quad-((2p-1)k)((2p-1)k-1)\\
 &=3k(k-1).
\end{aligned}
\]

Therefore \(t(C_n^{pk})-t(\overline{C_n^k})=nk(k-1)/2\). For every \(k\geq2\), this is positive. The graphs cannot be isomorphic because triangle number is an isomorphism invariant.

**5. Construct every positive case.** For \(k=1\), the degree equation gives \(n=2p+3\). The graph \(C_n^p\) contains every unordered pair except the pairs at cyclic distance \(p+1\), whereas \(\overline{C_n}\) contains every unordered pair except those at cyclic distance one. Since \(\gcd(p+1,2p+3)=1\), multiplication by \(p+1\) modulo \(n\) is a permutation of vertices taking the missing edges of \(\overline{C_n}\) bijectively onto the missing edges of \(C_n^p\). It is therefore an explicit isomorphism \(\overline{C_n}\cong C_n^p\), completing both implications.

## Verification

The standalone `verify.py` reconstructs cycle-power edges from cyclic distances, counts all triangles directly, and checks the two triangle formulae and exact defect on 48 parameter profiles with \(2\leq p\leq7\) and \(1\leq k\leq8\). It also verifies the explicit multiplier isomorphisms for the six instances \(2\leq p\leq7\), \(k=1\); 3,800 additional triples with \(3\leq n\leq40\), \(1\leq k\leq20\), and \(2\leq p\leq6\) check the degree and triangle obstructions, including complete-graph boundaries. Exact output appears in `verification_output.txt`. The computations are finite corroboration; the general theorem follows from the counting proof, not from extrapolation.

## Relationship to prior work

Aboulker, Milanič, Muršič, and Pizaña (first public September 23, 2026) study the square–complement graph equation and rule out nontrivial chordal and distance-hereditary solutions. The structural classification here concerns the different, unbounded family of *cycle powers* and all exponents \(p\geq2\). Darda, Milanič, and Pizaña (2021) study structural exclusions and the complexity of recognising square-complementary graphs; their paper cites the original squco treatment by Milanič, Pedersen, Pellicer, and Verret (2014). The familiar \(C_7\) is already in that literature. Alomari, Abudayah, and Al-Ezeh (2015, 2016) study cube-complementary graphs and explicitly establish that the only ordinary cycle which is cube-complementary is \(C_9\); the 2016 paper also constructs other, nonconsecutive-jump circulant solutions. The theorem above does not deny those broader circulant examples and does not claim the earlier cycle cases as original. Its distinct mathematical statement is the simultaneous complete classification for *consecutive-jump cycle powers* for all \(p\geq2\), including the uniform quantitative triangle defect.

## Limitations

This result does not classify arbitrary circulant graphs, arbitrary non-cycle-power graphs, or other graph equations. The 2014 and 1981 historical graph-equation papers, and the full 2026 preprint, were not all available for complete page-by-page text inspection; a currently undiscovered equivalent statement is therefore a residual literature risk. The exact proof is self-contained and does not rely on any asserted novelty of the already known \(C_7\) or \(C_9\) cases. Independent external mathematical review has not been performed.

## References

1. P. Aboulker, M. Milanič, P. Muršič, and M. A. Pizaña, *There are no nontrivial chordal square-complementary graphs*, arXiv:2609.28702 (first public 2026-09-23), https://arxiv.org/abs/2609.28702.
2. R. Darda, M. Milanič, and M. A. Pizaña, *Searching for square-complementary graphs: complexity of recognition and further nonexistence results*, Discrete Mathematics 344 (2021), 112369, DOI:10.1016/j.disc.2021.112369. Author manuscript https://xamanek.izt.uam.mx/map/papers/newsquco14z.pdf.
3. M. Milanič, A. S. Pedersen, D. Pellicer, and G. Verret, *Graphs whose complement and square are isomorphic*, Discrete Mathematics 327 (2014), 62–75, DOI:10.1016/j.disc.2014.03.018.
4. O. Alomari, M. Abudayah, and H. Al-Ezeh, *Graphs whose complement and cube are isomorphic*, Journal of Combinatorial Mathematics and Combinatorial Computing 94 (2015), 261–271, https://combinatorialpress.com/jcmcc-articles/volume-094/graphs-whose-complement-and-cube-are-isomorphic/.
5. O. Alomari, M. Abudayah, and H. Al-Ezeh, *Regular cubeco graphs*, Global Journal of Pure and Applied Mathematics 12 (2016), 1663–1669, https://www.ripublication.com/gjpam16/gjpamv12n2_40.pdf.
6. J. Akiyama, H. Era, and G. Exoo, *Further results on graph equations for line graphs and n-th power graphs*, Discrete Mathematics 34 (1981), 209–218, DOI:10.1016/0012-365X(81)90001-7 (historical comparison; full text not inspected).
