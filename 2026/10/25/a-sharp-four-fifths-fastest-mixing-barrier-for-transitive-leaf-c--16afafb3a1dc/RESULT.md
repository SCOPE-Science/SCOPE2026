# A sharp four-fifths fastest-mixing barrier for transitive leaf coronas

## Finding

**Theorem (sharp universal threshold and equality classification).** Let \(H\) be any finite, connected, noncomplete, simple graph whose automorphism group is transitive both on vertices and on undirected edges. Write \(d\ge2\) for its common degree and form its *one-leaf corona* \(G=H\circ K_1\) by adjoining a private pendant vertex to each vertex of \(H\). For any real symmetric, entrywise nonnegative, row-stochastic transition matrix \(P\) with off-diagonal support restricted to edges of \(G\), let
\[
\mu(P)=\left\|P-\frac{\mathbf1\mathbf1^{\mathsf T}}{2|V(H)|}\right\|_2.
\]
Then
\[
\boxed{\min_P\mu(P)\ge\frac45.}
\]
**Equality holds if and only if \(H\) is a regular complete multipartite graph having \(r\ge2\) parts of a common size \(m\ge2\).** For these and only these cores, \(d=(r-1)m\), the optimal mixing modulus is exactly \(4/5\), and the unique transition matrix *within the core-automorphism-invariant class* attaining the bound has probability \(3/(5d)\) on every core edge and \(2/5\) on every private pendant edge; the core holding probabilities are zero and each leaf holds with probability \(3/5\). The classification and global optimality apply to arbitrary, not necessarily automorphism-invariant, feasible matrices. Uniqueness among all unrestricted matrices is not asserted.

The result is an extremal characterization **across all noncomplete vertex- and edge-transitive cores**, not a claim that the individual complete-multipartite optimum is unknown: star–mesh consensus work already addresses the latter topology, as discussed below. For any other core in the stated class, the optimal SLEM is strictly greater than \(4/5\).

For a balanced complete multipartite core of degree \(d\), the maximum-degree and uniform-target Metropolis prescriptions both assign \(1/(d+1)\) to every edge of the corona. Their SLEM is
\[
\mu_{\mathrm{heur}}=\frac{d+\sqrt{d^2+4}}{2(d+1)},\qquad
\lim_{d\to\infty}\frac{1}{d}\frac{1-4/5}{1-\mu_{\mathrm{heur}}}=\frac15.
\]
The graph-wide structural threshold is the principal claim; the benchmark formula quantifies its optimization implications.

## Assumptions and scope

All graphs are finite, simple, connected, undirected, and unweighted before transition probabilities are assigned. Noncomplete means at least one pair of distinct core vertices is not joined by an edge. Transitivity means the automorphism group of the core acts transitively on vertices and separately transitively on undirected edges. Holding probabilities are allowed; transition weights are nonnegative and stochastic, and there is no requirement that each permitted edge have strictly positive weight. The stationary distribution is uniform. All optimization assertions concern the second-largest eigenvalue *modulus* of the symmetric stochastic matrix, not total-variation mixing time, and concern exactly one private leaf at each core vertex.

## Proof

**1. Symmetry without restricting global competitors.** The map \(P\mapsto\|P-J\|_2\) is convex and invariant under simultaneous permutation of rows and columns. Averaging any feasible \(P\) over the inherited automorphism group of \(H\) yields a feasible matrix of no greater objective. Vertex and edge transitivity therefore reduce the search for a global minimum to matrices with one common core-edge weight \(a\), one common leaf-edge weight \(b\), and constraints \(a,b\ge0\), \(da+b\le1\). The corresponding core and leaf holding probabilities are \(1-da-b\) and \(1-b\). This reduction does **not** establish unrestricted uniqueness.

**2. Spectral blocks.** Let \(A\) be the core adjacency matrix and order its real eigenvalues \(d=\lambda_1>\lambda_2\ge\cdots\ge\lambda_n\). On the two-dimensional span of the core and leaf copies of an eigenvector for \(\lambda\), the matrix acts as
\[
B_\lambda=\begin{pmatrix}1-da-b+a\lambda&b\\b&1-b\end{pmatrix}.
\]
For \(\lambda=d\), the block has eigenvalues \(1\) and \(1-2b\). For each \(\lambda<d\) define \(t=a(d-\lambda)/2\); the two other eigenvalues are exactly
\[
E_\pm(t,b)=1-t-b\pm\sqrt{t^2+b^2}.
\]
All modes with \(\lambda<d\) lie in the orthogonal complement of the uniform vector. Thus their eigenvalue magnitudes, and \(|1-2b|\), control \(\mu(P)\).

**3. A spectral barrier at \(4/5\).** A noncomplete regular core has a nonedge \(u,v\). The vector \(e_u-e_v\) is perpendicular to \(\mathbf1\) and has adjacency Rayleigh quotient zero; hence \(\lambda_2\ge0\). Moreover \(\lambda_n<0\), since \(A\) has trace zero, \(d>0\), and at least one nontrivial negative eigenvalue. If \(\lambda_2=0\), \(B_0\) is an actual nontrivial block. If \(\lambda_2>0\), the matrix \(B_0\) is a convex combination of the *actual* nontrivial blocks \(B_{\lambda_2}\) and \(B_{\lambda_n}\):
\[
B_0=\frac{-\lambda_n}{\lambda_2-\lambda_n}B_{\lambda_2}
+\frac{\lambda_2}{\lambda_2-\lambda_n}B_{\lambda_n}.
\]
Consequently, if \(\mu(P)\le4/5\), the matrix \((4/5)I-B_0\) must be positive semidefinite in **both** cases. Put \(x=da\). Its determinant and lower-right entry are
\[
\det((4/5)I-B_0)=(x+b-1/5)(b-1/5)-b^2,\qquad b-1/5.
\]
The positive-semidefinite condition forces \(b\ge1/5\); since \(x+b\le1\),
\[
0\le\det((4/5)I-B_0)
\le\frac45(b-1/5)-b^2=-(b-2/5)^2.
\]
Thus \(b=2/5\); equality in the preceding inequality also forces \(x+b=1\), so \(x=3/5\), or \(a=3/(5d)\). In particular no feasible \(P\) can have \(\mu(P)<4/5\); the sharp candidate is *forced* in the invariant class.

**4. Rigidity and attainment.** If \(\lambda_2>0\), that forced candidate has \(t=(3/10)(1-\lambda_2/d)<3/10\) for the \(\lambda_2\)-block. For fixed \(b=2/5\), \(E_+(t,b)\) is strictly decreasing in \(t\ge0\), and \(E_+(3/10,2/5)=4/5\). Hence its \(\lambda_2\)-eigenvalue exceeds \(4/5\); no matrix with \(\mu\le4/5\) exists. Since the feasible set is compact, the minimum is *strictly* greater than \(4/5\).

If \(\lambda_2=0\), all nontrivial core eigenvalues lie in \([-d,0]\). At the forced weights \(a=3/(5d)\), \(b=2/5\), their \(t\) parameters lie in \([3/10,3/5]\). Here \(E_+\) decreases from \(4/5\), while \(E_-\) decreases from \(-1/5\) to \(-\sqrt{13}/5\). Thus both have modulus at most \(4/5\), since \(\sqrt{13}<4\). The radial block has other eigenvalue \(1/5\). Therefore \(\mu=4/5\), attained exactly when \(\lambda_2=0\).

**5. Graph-theoretic equality criterion.** Suppose \(\lambda_2=0\). Then \(A\) is negative semidefinite on \(\mathbf1^\perp\). For every distinct nonadjacent pair \(u,v\), the vector \(e_u-e_v\) lies in \(\mathbf1^\perp\) and satisfies \((e_u-e_v)^{\mathsf T}A(e_u-e_v)=0\); negative semidefiniteness forces \(A(e_u-e_v)=0\). Thus any two nonadjacent vertices have identical adjacency rows. Nonadjacency is therefore an equivalence relation (adjoining equality), and different equivalence classes are completely joined. Hence \(H\) is complete multipartite. Regularity forces every part to have equal size; noncompleteness forces \(m\ge2\). Conversely, \(K_{m,\ldots,m}\) with \(r\ge2,m\ge2\) has adjacency eigenvalues \((r-1)m\), \(0\), and \(-m\), with \(0\) occurring, so \(\lambda_2=0\). This completes the global sharp iff classification.

**6. Heuristic comparison on the equality class.** On a balanced complete \(r\)-partite core of degree \(d=(r-1)m\), maximum-degree and uniform-target Metropolis both use \(a=b=1/(d+1)\). For the zero adjacency eigenmode, \(t=d/[2(d+1)]\), so the positive mode equals \([d+\sqrt{d^2+4}]/[2(d+1)]\). Since all remaining nontrivial \(\lambda\) lie in \([-m,0]\), \(t\) lies between that value and at most \(d/(d+1)\). Monotonicity of \(E_+\) bounds all other positive modes; the most negative mode has modulus at most \(\sqrt{d^2+1}/(d+1)\), strictly less than the displayed positive one. The other radial mode also has smaller modulus. Finally expansion or rationalization yields \(1-\mu_{\mathrm{heur}}\sim1/d\), giving the stated limit.

## Verification

The standalone `verify.py` computes exact symbolic determinant and block identities using SymPy; checks 30 balanced multipartite graph orders against explicit dense spectra and the benchmark formula; exercises 540 invariant and 150 noninvariant feasible matrices; checks ten noncomplete transitive cycle and cube cores and the adjacency-quotient implications; and proves an asymptotic ratio algebraically. Execute from the extracted package with `python verify.py` after installing the listed NumPy and SymPy dependencies from `requirements.txt`. The computations test the formulas; the preceding quantified proof supplies the universal classification. A finite test does not establish a universal claim.

## Relationship to prior work

Boyd–Diaconis–Xiao formulate fastest mixing as convex semidefinite optimization, and Boyd–Diaconis–Parrilo–Xiao prove symmetry averaging and solve several graph families including complete multipartite cores **without** one-leaf attachments. Jafarizadeh–Jamalipour (2010/2011) solve fastest distributed consensus on *star–mesh hybrid networks with a complete multipartite core and attached star branches*; specializing their topology to one unit-length branch per core vertex includes the **equality-family instances** of this theorem. Consequently, the exact complete-multipartite optimizer is **not represented as independently new** here. The claimed additional statement is the graph-wide sharp barrier for every noncomplete vertex- and edge-transitive core together with the *only-if* and strict non-multipartite portions, not supplied by that family-specific work. The earlier complete-core corona and cycle-corona formulas likewise provide isolated special cases but not the global graph-theoretic characterization. Standard spectral graph theory underlies the nonpositive-adjacency characterization, proved directly above. A narrowly similar universal corona bound in other literature cannot be ruled out categorically.

## Limitations

Only symmetric, entrywise nonnegative, uniform-stationary chains, core graphs transitive on both vertices and edges, and one private leaf per core vertex are covered. The theorem gives no exact optimum for non-multipartite cores beyond the strict \(4/5\) lower bound. It does not prove uniqueness among arbitrary noninvariant optimizers or a quantitative positive separation uniform across all core graphs. The prior exact treatment of complete multipartite star–mesh graphs is acknowledged. Independent external mathematical audit has not been performed.

## References

1. Boyd, S., Diaconis, P., Xiao, L., *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: 10.1137/S0036144503423264. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. Boyd, S., Diaconis, P., Parrilo, P., Xiao, L., *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first public September 6, 2007; SIAM Journal on Optimization 20 (2009). https://arxiv.org/abs/0709.0955.
3. Jafarizadeh, S., Jamalipour, A., *Fastest Distributed Consensus on Star-Mesh Hybrid Sensor Networks*, arXiv:1009.4569, first public September 23, 2010; ICC 2011, DOI: 10.1109/ICC.2011.5963080. https://arxiv.org/abs/1009.4569.
4. Jafarizadeh, S., Jamalipour, A., *A Solution to Fastest Distributed Consensus Problem for Generic Star & K-cored Star Networks*, arXiv:1201.4480 (2012). https://arxiv.org/abs/1201.4480.
