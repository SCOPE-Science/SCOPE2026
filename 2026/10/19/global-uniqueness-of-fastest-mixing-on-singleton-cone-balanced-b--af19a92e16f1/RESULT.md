# Global uniqueness of fastest mixing on singleton-cone balanced bipartite graphs

## Finding
For every integer \(m\ge 2\), let \(G_m=K_1\vee K_{m,m}=K_{1,m,m}\): its vertices consist of a distinguished hub \(o\) and two independent vertex classes \(L\) and \(R\), each of size \(m\). There are all hub-to-periphery edges and all \(m^2\) edges joining \(L\) to \(R\), but no edges within either class. Among **all** real symmetric, entrywise nonnegative row-stochastic matrices \(P\) whose off-diagonal support is contained in \(E(G_m)\), the unique minimizer of the second-largest eigenvalue modulus is
\[
P^*_{o,x}=\frac{1}{2m}\quad(x\in L\cup R),\qquad
P^*_{x,y}=\frac{2m-1}{3m^2}\quad(x\in L,\ y\in R),
\]
with symmetric reverse entries, hub diagonal \(P^*_{o,o}=0\), and every peripheral diagonal \(P^*_{x,x}=(2m-1)/(6m)\). Its optimal objective value is
\[
\boxed{\mu_m^*=\frac{2m-1}{6m}=\frac13-\frac{1}{6m}.}
\]
In particular, this is **global uniqueness without presupposing symmetry of a competing kernel**: every optimal design uses all permitted edges with exactly these weights and puts no holding probability at the hub. The analogous optimum on \(K_{m,m}\) is \(1/3\), so adding the hub improves SLEM by exactly \(1/(6m)\).

## Assumptions and scope
Fix an integer \(m\ge2\). Diagonal entries (holding probabilities) are allowed, and edge probabilities may be zero; no irreducibility or symmetry under graph automorphisms is assumed beyond matrix symmetry \(P=P^\top\). Let \(N=2m+1\), \(J=\mathbf1\mathbf1^\top/N\), and define \(\mu(P)=\|P-J\|_{2}\). As \(P\) is real symmetric and stochastic, this equals the largest modulus of an eigenvalue other than the fixed eigenvalue \(1\), counting multiplicity on \(\mathbf1^\perp\). The result concerns the discrete-time, uniform-stationary fastest-mixing objective, not continuous-time optimization or arbitrary nonuniform stationary distributions. For \(m=1\), the graph is \(K_3\), whose optimal kernel is \(J\); the stated formulas are not intended for that boundary.

## Proof
**1. Averaging and spectral reduction.** The feasible set is convex and \(P\mapsto\|P-J\|_2\) is convex. Averaging any candidate over the graph automorphisms (permutations of each class and interchange of the two classes) cannot increase \(\mu\). An invariant kernel has one common hub-edge probability \(a\) and one common class-crossing probability \(b\), with
\[
0\le a\le\frac1{2m},\qquad 0\le mb\le1-a.
\]
The corresponding diagonal entries are \(1-2ma\) at the hub and \(1-a-mb\) at every other vertex. Decomposing \(\mathbb R^{2m+1}\) into the constant line, the hub-versus-classes direction, the difference of class means, and the classwise zero-sum subspace gives exactly
\[
1,\quad 1-(2m+1)a,\quad 1-a-2mb,\quad
\underbrace{1-a-mb,\ldots,1-a-mb}_{2m-2\ \mathrm{times}}.
\]

**2. Sharp lower bound.** Put \(s=1-a\), \(y=mb\). Since \(0\le y\le s\),
\[
\max\{|s-y|,|s-2y|\}\ge\frac{s}{3},
\]
with equality **only** at \(y=2s/3\). Indeed, \(s-y<s/3\) would require \(y>2s/3\), while \(|s-2y|<s/3\) would require \(y<2s/3\). Thus any invariant kernel satisfies
\[
\mu(P)\ge\frac{1-a}{3}\ge\frac{1-1/(2m)}3=\frac{2m-1}{6m}=\mu_m^*.
\]
Equality forces \(a=1/(2m)\) and \(mb=2(1-a)/3\), which give exactly the probabilities in the finding. At this kernel the displayed eigenvalues on \(\mathbf1^\perp\) are \(-1/(2m)\), \(-\mu_m^*\), and \(+\mu_m^*\) with multiplicity \(2m-2\). Since \(1/(2m)\le\mu_m^*\) for every \(m\ge2\), the proposed kernel attains the lower bound and is the **unique invariant optimizer**.

**3. Global uniqueness, with no invariance assumption.** Let \(P\) be any feasible globally optimal kernel, and let \(\overline P\) be its automorphism average. From Step 2, \(\overline P=P^*\). Consider
\[
Q(P)=\mu_m^*I-P+J\succeq0.
\]
For every graph automorphism \(g\), also \(Q(gPg^\top)\succeq0\); their average is \(Q(P^*)\). Let
\[
U_L=\{x:\operatorname{supp}(x)\subseteq L,\ \sum_{i\in L}x_i=0\},\quad
U_R=\{x:\operatorname{supp}(x)\subseteq R,\ \sum_{j\in R}x_j=0\}.
\]
By the spectrum in Step 2, \(Q(P^*)\) annihilates \(U_L\oplus U_R\). The average of nonnegative quadratic forms can vanish only if each summand vanishes. In particular, \(Q(P)x=0\), or \(Px=\mu_m^*x\), for every \(x\in U_L\oplus U_R\). Every coordinate of the hub-to-\(L\) edge vector must therefore be equal (it annihilates every \(L\)-zero-sum vector); likewise for hub-to-\(R\). For the \(m\times m\) matrix \(B\) of \(L\)-to-\(R\) edge probabilities, \(B^\top U_L=0\) forces all its rows equal, while \(B U_R=0\) forces all its columns equal, hence \(B=b\mathbf1\mathbf1^\top\). Finally, no within-class off-diagonal entries exist, so \(Px=\mu_m^*x\) implies every peripheral diagonal is exactly \(\mu_m^*\). Row-stochasticity gives hub-edge weights \(a_L=a_R=1-mb-\mu_m^*\), equal on both sides. Consequently \(P\) itself is invariant and equals its average \(P^*\). This proves uniqueness among **all** feasible kernels.

## Verification
Run `python verify.py` with SymPy and NumPy. The program builds the full kernel from the stated weights, confirms exact row sums and entrywise nonnegativity, and checks the exact rational eigenvalue multiset for every \(2\le m\le9\), merging the two negative eigenvalues when \(m=2\). It additionally computes full symmetric-matrix spectra for \(2\le m\le12\), including \(120\) independently sampled admissible nonsymmetric-under-automorphisms kernels per size. The executed checks returned `exact distinct-eigenvalue counts: 31`, `full-matrix checks: 1331`, and `PASS`. The proof, rather than the finite checks, establishes the theorem for all integers \(m\ge2\) and global uniqueness. The script's random tests do not constitute an exhaustive search or a numerical uniqueness certificate.

## Relationship to prior work
Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955, Section 5.3.2) give a general orbit-based/block-diagonal construction and a reduced semidefinite program for **every complete multipartite graph**. Their section directly covers the spectral *reduction* relevant here and must not be portrayed as absent; it does not state this complete explicit optimum on the singleton-cone balanced bipartite family, nor characterize every optimal kernel without imposing automorphism invariance. Jafarizadeh (arXiv:1008.2588, Section III) gives explicit weights for specific path- or cycle-arranged multipartite networks whose parts have equal cardinality; its symmetric instances do not have part sizes \(1,m,m\). The clique-lifted-graph results of Jafarizadeh (arXiv:2501.02421; journal work originally published in 2020) concern different graph substitutions. This finding's strongest separation from general prior machinery is the positive-semidefinite **global uniqueness** statement, not merely the small reduced optimization. The graph is distinct from the cone over a *crown* graph, whose peripheral cross-edges omit a perfect matching.

## Limitations
Global novelty cannot be inferred from database non-retrieval; an equivalent unindexed uniqueness result might exist. The general complete-multipartite spectral decomposition and convexity framework are established prior results. The explicit optimum can be found by specializing that decomposition; the independently necessary contribution here is the exact all-competitors rigidity, with its forced positive edges and zero hub holding. The proof does not address nonsymmetric transition matrices, nonuniform stationary distributions, other multipartite part sizes, or fastest mixing under a different objective (such as finite-time total variation). Independent external validation has not been performed.

## References
1. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first public 2007-09-06), especially Section 5.3.2; SIAM J. Optim. 20 (2009), 792–819, DOI:10.1137/070689413.
2. S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network*, arXiv:1008.2588 (first public 2010-08-16), Sections III and V.
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, IEEE Trans. Signal Inf. Process. Netw. (2020), accessible full-text version arXiv:2501.02421, especially Sections 1 and 3.
