# Exact lattice-diameter partition and segment laws for binary polytopes

## Finding
Let \(P\subseteq[0,1]^d\) be any convex hull of at least two distinct vectors in \(\{0,1\}^d\), and let \(n\ge1\) be an integer. The lattice-diameter partition number is exactly its vertex count:
\[
\operatorname{ldiam}(nP)=n,\qquad \beta_{\mathbb Z}(nP\cap\mathbb Z^d)=f_0(P).
\]
Moreover the number \(LD_P(n)\) of its **unoriented lattice-diameter segments** is a rational Ehrhart quasipolynomial for *every* positive integer \(n\), not merely eventually.

Two concrete classes calibrate the strength and limits of this assertion. For the hypersimplex
\(H_{d,k}=\{x\in[0,1]^d:\sum_i x_i=k\}\), where \(d\ge2\) and \(1\le k\le d-1\),
\[
\beta_{\mathbb Z}(nH_{d,k}\cap\mathbb Z^d)=\binom dk,
\qquad LD_{H_{d,k}}(n)=\frac12\sum_{s=1}^{\min(k,d-k)}\binom ds\binom{d-s}s E_{d-2s,k-s}(n),
\]
where \(E_{m,j}(n)=\#\{z\in\{0,\ldots,n\}^{m}:\sum_i z_i=jn\}\), with the empty-vector convention \(E_{0,0}(n)=1\). For \(k=1\) or \(k=d-1\), \(LD_{H_{d,k}}(n)=\binom d2\). For \(d\ge4\) and \(2\le k\le d-2\), this count is a polynomial in \(n\) of degree exactly \(d-3\), with leading coefficient
\[
\frac{\binom d2 A(d-3,k-2)}{(d-3)!},
\]
where \(A(r,j)\) counts permutations of \(\{1,\dots,r\}\) with exactly \(j\) descents.

In sharp contrast, the binary tetrahedron
\[
T=\operatorname{conv}\{(0,0,0),(0,1,1),(1,0,1),(1,1,0)\}
\]
has
\[
LD_T(n)=6+3\mathbf1_{2\mid n}\quad(n\ge1),
\]
with **least quasiperiod two**. Its lattice Borsuk number is four for every positive dilation.

## Assumptions and scope
A segment with distinct integer endpoints \(x,y\in\mathbb Z^d\) contains precisely \(1+\gcd(|x_1-y_1|,\ldots,|x_d-y_d|)\) integer points. The lattice diameter counts the greatest possible number of intervals between successive integer points, so it equals the maximum coordinate-difference gcd. A lattice-diameter segment is an unordered pair of lattice endpoints attaining the maximum, together with the intervening segment. The lattice Borsuk number \(\beta_{\mathbb Z}(S)\) of a finite set of integer points with positive lattice diameter is the smallest number of subsets partitioning \(S\) so that every part has smaller lattice diameter. Empty or singleton parts contribute no positive lattice diameter. No full-dimensionality assumption is imposed on \(P\); dimension means affine dimension where relevant. The ambient lattice is \(\mathbb Z^d\), rather than the vertex-edge graph metric or Euclidean diameter.

## Proof
**Step 1: diameter and exact partition.** Since \(nP\subseteq[0,n]^d\), the gcd of all coordinate differences of two integer points is at most \(n\). Every pair of distinct vertices \(v,w\in P\cap\{0,1\}^d\) gives \(nv,nw\in nP\cap\mathbb Z^d\) with coordinate differences all zero or \(\pm n\); hence its lattice diameter is \(n\). The scaled original vertices form a complete diameter clique on exactly \(f_0(P)\) points, proving \(\beta_{\mathbb Z}\ge f_0(P)\).

For the reverse inequality, associate to each \(x\in nP\cap\mathbb Z^d\) a vertex \(v(x)\) in the unique minimal face of \(P\) whose relative interior contains \(x/n\). For definiteness choose the lexicographically first such vertex. If \(x,y\) have diameter \(n\), some coordinate satisfies \(x_i=0,y_i=n\), after interchanging endpoints. The entire minimal face of \(x/n\) is contained in the exposed coordinate face \(\{z_i=0\}\), and similarly the minimal face of \(y/n\) lies in \(\{z_i=1\}\). Consequently \(v(x)_i=0\) and \(v(y)_i=1\), so the two diameter-adjacent lattice points receive different labels. Each label class has strictly smaller lattice diameter. This yields exactly \(f_0(P)\) nonempty classes because every scaled vertex labels itself, completing the partition proof.

**Step 2: finite Ehrhart decomposition valid from the first dilation.** Every unordered diameter segment \([x,y]\) has difference \(y-x=nu\) for a unique unoriented primitive difference vector \([u]=\{u,-u\}\) with \(u\in\{-1,0,1\}^d\setminus\{0\}\). Choose exactly one orientation for each \([u]\), for example the one whose first nonzero coordinate is \(+1\). Put \(I(u)=\{i:u_i=0\}\). For \(z\in\mathbb R^{I(u)}\), construct endpoints \(a_u(z),b_u(z)\in\mathbb R^d\) by \((a_i,b_i)=(0,1)\) when \(u_i=1\), \((1,0)\) when \(u_i=-1\), and \((z_i,z_i)\) when \(i\in I(u)\). Set
\[
R_u=\{z\in\mathbb R^{I(u)}:a_u(z)\in P\ \text{and}\ b_u(z)\in P\}.
\]
Because \(P\) is a rational polytope, each \(R_u\) is rational, possibly empty or zero-dimensional. Multiplying its two endpoint inequalities by \(n\) sets the nonzero-difference coordinates to \(0\) or \(n\). Thus every lattice point \(z\in nR_u\cap\mathbb Z^{I(u)}\) gives exactly one segment \([na_u(z/n),nb_u(z/n)]\), and every diameter segment with difference direction \([u]\) arises uniquely this way. Hence, with empty sets contributing zero,
\[
LD_P(n)=\sum_{[u]\in(\{-1,0,1\}^d\setminus\{0\})/\pm} \#(nR_u\cap\mathbb Z^{I(u)}).
\]
Rational Ehrhart theory gives a quasipolynomial on *all* positive integers for each summand, irrespective of whether \(R_u\) is full-dimensional in its coordinate space, and therefore for their sum.

**Step 3: the hypersimplex count.** In \(H_{d,k}\), if \(u\) is a diameter direction then its \(+1\) and \(-1\) supports must have equal cardinality \(s\), because both endpoints have coordinate sum \(k\). Choosing these disjoint supports yields \(\binom ds\binom{d-s}s\) oriented differences; the remaining \(d-2s\) common coordinates must sum to \((k-s)n\), giving \(E_{d-2s,k-s}(n)\) choices. The sum over all oriented differences double-counts each unoriented segment, proving the displayed formula. Necessarily \(1\le s\le\min(k,d-k)\).

For \(1\le j\le m-1\), the polytope whose Ehrhart polynomial is \(E_{m,j}\) is the \((m-1)\)-dimensional hypersimplex \(H_{m,j}\). Its leading coefficient is \(A(m-1,j-1)/(m-1)!\). This follows, for example, by taking the highest-degree term of the bounded-composition inclusion-exclusion formula and the Eulerian alternating-sum identity. When \(2\le k\le d-2\), the \(s=1\) contribution has dimension \(d-3\) and positive leading coefficient \(\tfrac12d(d-1)A(d-3,k-2)/(d-3)!\); every \(s\ge2\) contribution has dimension at most \(d-5\), or is zero-dimensional. Thus there can be no leading-term cancellation. The endpoint-rank hypersimplices reduce to simplices and have exactly \(\binom d2\) vertex-pair diameter segments for all \(n\).

**Step 4: parity tetrahedron.** Its dilation is the set of integer triples \((a,b,c)\) satisfying
\[
0\le a,b,c\le n,\quad a+b+c\le2n,\quad a\le b+c,\quad b\le a+c,\quad c\le a+b.
\]
Every diameter direction has support size one, two or three. Support size three would force antipodal cube vertices as endpoints, but the tetrahedron's four even-parity binary vertices have no antipodal pair. Each of its six vertex pairs gives a support-two direction, and the tetrahedral inequalities show its common third coordinate is uniquely \(0\) or \(n\); therefore there are exactly six such segments. For support-one differences, say \(u=(1,0,0)\), the endpoints are \((0,b,c)\) and \((n,b,c)\). The inequalities for both endpoints force \(b=c=n/2\); a lattice segment exists exactly when \(n\) is even. The three coordinate directions contribute three additional segments in that case and none otherwise. Since both parities occur arbitrarily far out, no period-one quasipolynomial can represent this sequence: the two constant constituents \(6\) and \(9\) are distinct.

## Verification
A standalone, standard-library-only checker (`verify.py`) independently constructs integer points and counts primitive-gcd diameter pairs. It checks the hypersimplex formula and residue-class clique counts for every \(2\le d\le7\), \(1\le k\le d-1\), and \(1\le n\le3\): 63 parameter triples. It separately enumerates the parity tetrahedron for \(1\le n\le14\). The checker is evidence for arithmetic and normalization only; the proofs above establish all-parameter conclusions. Run `python3 verify.py` in the directory containing this document.

## Relationship to prior work
Averkov, Brose, De Loera, Lopez-Campos and Torres introduced the lattice-diameter segment enumeration and discrete lattice Borsuk problem, proved an **eventual** quasipolynomial for general integral polytopes (their Theorem 4.6), and proved the universal \(2^d\) partition bound (their Theorem 5.4). These statements do not provide the all-dilation finite-rational-Ehrhart decomposition for binary polytopes, the exact \(f_0(P)\) partition number for every dilation, the hypersimplex segment formula and Eulerian leading term, or the binary tetrahedron's sharp period-two obstruction. They do imply the weaker eventual quasipolynomial statement and an upper bound for partitions; neither is claimed here as new. Related work on uniform-matroid polytopes studies Euclidean/Hamming Borsuk distances, a different diameter notion. The Eulerian normalized volume of hypersimplices is classical; it is used as an ingredient, not claimed as a new result.

## Limitations
The partition equality relies essentially on binary-coordinate vertices. The exact Ehrhart decomposition is stated only for binary polytopes; it does not strengthen the general theorem for arbitrary lattice polytopes. The degree formula concerns hypersimplices, not general binary polytopes. Priority is assessed only against the inspected and searchable literature and may be affected by terminology differences. Independent expert validation has not been performed.

## References
1. G. Averkov, A. E. Brose, J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On Lattice Diameter Segments: Algorithms and Structure*, arXiv:2508.20009 (first public version August 27, 2025; examined version 2, October 3, 2026), especially Theorems 4.6 and 5.4 and Sections 4–5. https://arxiv.org/html/2508.20009v2
2. G. López-Campos, F. Meunier and J. L. Ramírez Alfonsín, *Matroids, intersecting bases, and Borsuk property*, arXiv:2506.17082 (June 20, 2025), on a different Euclidean/Hamming-diameter setting. https://arxiv.org/abs/2506.17082
3. Nan Li, *Ehrhart h*-vectors of hypersimplices*, arXiv:1104.5292 (2011), for classical hypersimplex Ehrhart and Eulerian background. https://arxiv.org/abs/1104.5292
