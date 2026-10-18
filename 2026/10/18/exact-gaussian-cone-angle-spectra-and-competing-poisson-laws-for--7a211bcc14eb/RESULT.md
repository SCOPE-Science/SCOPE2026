# Exact Gaussian cone-angle spectra and competing Poisson laws for matching-deleted permutohedra

## Finding

For integers \(n\ge3\) and \(0\le k\le\lfloor n/2\rfloor\), let \(M_k\) be a matching consisting of \(k\) disjoint edges of the complete graph \(K_n\), and let \(G_{n,k}=K_n\setminus M_k\). Define the graphical zonotope
\[
 Z_{n,k}=\sum_{\{i,j\}\in E(G_{n,k})}[e_i,e_j]\subset\mathbb R^n.
\]
It is full-dimensional in its natural \((n-1)\)-dimensional affine hull. Normal-cone probabilities below use the intrinsic Euclidean metric: a standard normal vector in the zero-sum subspace selects the unique maximizing vertex almost surely. All statements remain valid if the segments are independently rescaled by strictly positive factors, since this does not change the normal fan.

**Theorem (complete angular spectrum).** For each integer \(s\in\{0,\ldots,k\}\), the number of vertices whose Gaussian normal-cone probability is \(2^s/n!\) is exactly
\[
 N_{n,k}(s)=\frac1{2^s}\sum_{t=s}^{k}(-1)^{t-s}\binom ts\binom kt\,2^t(n-t)!.
\]
Values with \(N_{n,k}(s)=0\) are absent. In particular the two-independent-objective collision probability is
\[
 C_{n,k}:=\Pr\{V(g)=V(g')\}
 =\frac1{(n!)^2}\sum_{t=0}^{k}\binom kt\,2^t(n-t)!,
\]
where \(g,g'\) are independent intrinsic standard Gaussian objectives. The known number of vertices is recovered by
\[
 v_{n,k}=\sum_{t=0}^{k}(-1)^t\binom kt(n-t)!.
\]
The novelty claimed here is not that vertex-count formula, but the full **angular** spectrum, the exact collision probability and its limiting sampling laws.

**Theorem (two inequivalent typical vertices).** Let \(k=k(n)\) with \(k/n\to\rho\in[0,1/2]\), and associate to a vertex the integer \(S\) such that its Gaussian normal-cone angle is \(2^S/n!\). Then
\[
 \begin{aligned}
 S\mid\text{Gaussian-exposed vertex}&\Longrightarrow \operatorname{Poisson}(2\rho),\\
 S\mid\text{uniformly chosen vertex}&\Longrightarrow \operatorname{Poisson}(\rho).
 \end{aligned}
\]
Furthermore,
\[
 \frac{v_{n,k}}{n!}\longrightarrow e^{-\rho},\qquad
 n!C_{n,k}\longrightarrow e^{2\rho},\qquad
 v_{n,k}C_{n,k}\longrightarrow e^{\rho}.
\]
For a deleted perfect matching, these limits are respectively \(e^{-1/2}\), \(e\), and \(e^{1/2}\), and the two Poisson parameters are \(1\) and \(1/2\). Thus the Gaussian-exposed distribution is persistently size-biased relative to the uniform-vertex distribution, despite both being supported on the same polytope vertices.

## Assumptions and scope

The graph is simple, with exactly \(k\) missing edges and with no two missing edges sharing a vertex. Relabeling the matching has no effect. A vertex is the maximizer of a generic linear objective on \(Z_{n,k}\); its intrinsic normal-cone angle is the probability that an isotropic Gaussian objective exposes it. Normal-cone angles are dimensionless probabilities, not angular surface measures in radians. The collision probability uses two independently drawn directions and asks for **exact equality of exposed vertices**. The Poisson claims apply only to sequences \(k(n)/n\to\rho\) within the indicated feasible range; no convergence speed is claimed. The result excludes the zero-dimensional \(n=2,k=1\) case by assumption, although the same finite combinatorics formally extends to it.

## Proof

**1. Gaussian objectives are uniform total orders.** The normal fan of a graphical zonotope is the arrangement of hyperplanes \(g_i=g_j\) for graph edges \(\{i,j\}\). To see this directly, maximize each segment \([e_i,e_j]\) separately: when \(g_i>g_j\), its contribution is \(e_i\), otherwise \(e_j\). Thus every strict ordering \(\pi\) of \(n\) independent continuous, exchangeable coordinates determines an acyclic orientation of the graph and an exposed vertex. Since subtracting the coordinate mean does not alter differences, a standard Gaussian on the zero-sum subspace yields the same uniformly distributed order as \(n\) independent standard normals. Every one of the \(n!\) total orders has probability \(1/n!\).

**2. Exact class size.** Fix a total order \(\pi\) and let \(J(\pi)\) be the number of deleted matching pairs appearing in consecutive positions of \(\pi\). Two total orders expose the same zonotope vertex exactly when they induce the same orientation on all edges of \(G_{n,k}\), equivalently when they are linear extensions of the same directed acyclic graph. Two linear extensions of a finite partial order are connected by swaps of adjacent incomparable elements. Here the only possible incomparable pairs are deleted matching edges. If a deleted pair \(\{a,b\}\) is separated in \(\pi\) by another element \(c\), then both \(\{a,c\}\) and \(\{c,b\}\) are graph edges (the deleted edges form a matching), so \(a\) and \(b\) are comparable via the directed two-edge path through \(c\). Conversely, a consecutive deleted pair is incomparable: a directed path between it would have to contain a vertex strictly between its endpoints in every linear extension, which the displayed total order lacks. Thus the incomparable pairs in that orientation are precisely the \(J(\pi)\) consecutive deleted pairs. Their adjacent swaps are independent because the matching pairs are disjoint, and no other swap is possible. Every orientation class therefore consists of exactly \(2^{J(\pi)}\) total orders, and all its members have the same value of \(J\). The angle at the associated vertex is exactly \(2^{J(\pi)}/n!\).

**3. Enumerating all angle classes.** For each prescribed set of \(t\) deleted edges, the number of permutations in which all \(t\) pairs appear consecutively is \(2^t(n-t)!\): contract the pairs to labeled blocks, permute the \(n-t\) blocks, then choose an internal order for each contracted pair. Let \(A_s\) denote the number of permutations with exactly \(s\) consecutive deleted pairs. Counting pairs consisting of a permutation and a marked subset of its consecutive deleted pairs gives
\[
 \sum_{s=t}^k\binom st A_s=\binom kt2^t(n-t)!.
\]
Binomial inversion therefore yields
\[
 A_s=\sum_{t=s}^k(-1)^{t-s}\binom ts\binom kt2^t(n-t)!.
\]
Each vertex with angle \(2^s/n!\) accounts for exactly \(2^s\) permutations, hence \(N_{n,k}(s)=A_s/2^s\), proving the spectrum. Summing over all vertices yields
\[
 C_{n,k}=\sum_{s=0}^k N_{n,k}(s)\Big(\frac{2^s}{n!}\Big)^2
       =\frac{1}{n!}\,\mathbb E[2^J],
\]
where \(J=J(\pi)\) under a uniform random permutation. Since the elementary identity \(a^J=\sum_{t=0}^J\binom Jt(a-1)^t\) gives
\[
 \mathbb E[a^J]=\sum_{t=0}^k\binom kt\frac{2^t(n-t)!}{n!}(a-1)^t,\tag{1}
\]
substitution \(a=2\) proves the collision formula; substitution \(a=1/2\) proves the stated vertex count because
\[
 v_{n,k}=n!\,\mathbb E[2^{-J}].
\]
These are finite exact identities, with no independence assumption about adjacency events.

**4. Poisson limits and sampling discrepancy.** Put \(\rho_n=k/n\). For every fixed nonnegative integer \(t\), the coefficient in (1) satisfies
\[
 \binom kt\frac{2^t(n-t)!}{n!}
 =\frac{2^t}{t!}\frac{(k)_t}{(n)_t}
 \longrightarrow\frac{(2\rho)^t}{t!}.
\]
Moreover, because \((k-j)/(n-j)\le k/n\) for \(j<k\le n\), the coefficient is bounded by \((2k/n)^t/t!\le1/t!\). The series therefore converges locally uniformly in \(a\), even for complex \(a\), to
\[
 \lim_{n\to\infty}\mathbb E[a^J]=e^{2\rho(a-1)}.
\]
This is the probability-generating function of a Poisson random variable with mean \(2\rho\); hence \(J\) for Gaussian-selected vertices converges to that law. The uniform-vertex law is the exponential tilt
\[
 \Pr_{\rm vertex}\{S=s\}
 =\frac{2^{-s}\Pr_{\rm Gaussian}\{J=s\}}{\mathbb E[2^{-J}]},
\]
which tends to \(\exp(-\rho)\rho^s/s!\), the Poisson law of mean \(\rho\). Finally take \(a=1/2\) and \(a=2\) in (1) to obtain \(v_{n,k}/n!\to e^{-\rho}\) and \(n!C_{n,k}\to e^{2\rho}\), whose product yields the stated sharp ratio. This completes the proof.

## Verification

The standalone `verify_angles.py` performs exhaustive, independent **integer/rational** orientation enumeration for every \(2\le n\le8\) and \(0\le k\le\lfloor n/2\rfloor\). It groups total orders by their graph-edge orientations, checks that each class has \(2^s\) orders with the same \(s\), checks all multiplicities against the alternating factorial sum, checks that the collision probability equals the sum of squared class probabilities, and checks the vertex count against the generating-function evaluation. It passes all 23 parameter pairs. The small degenerate case \(n=2,k=1\) is included solely as a useful boundary test. The test code uses only Python's standard library; run `python3 verify_angles.py`. In addition, high-precision evaluations at \(n=20,100,500\) for perfect-match deletion agree with the proven limits, but finite tests are not offered as an infinite proof.

## Relationship to prior work

The graphical-zonotope fan and its identification with acyclic orientations and linear extensions are standard and are not claimed here. Padrol, Pilaud and Poullot (arXiv:2111.12422, Section 1.3) present the graphical normal fan and its deformation theory. Chapoton and Pilaud (arXiv:2201.06896, Propositions 36--39, 48--50, 98--100) describe the braid-fan coarsening, the complete-multipartite subclass, and its vertex counts. Indeed \(G_{n,k}\) is complete multipartite, with \(k\) parts of size two and \(n-2k\) singleton parts. OEIS A033815 already records the **total number** of acyclic orientations for the perfect-matching case. These general fan and counting statements cover the underlying vertices and their total count; none of the checked statements gives the specialized exact cone-angle multiplicities, the two-direction collision law, or the opposed Poisson limits of direction-sampling versus vertex-sampling. The previously studied complete-bipartite case \(n=4,k=2\) is included as a consistency special case, not presented as a separately new small example.

## Limitations

The proof concerns deleted-edge sets that are matchings. If missing edges share endpoints, the independent-swap class size \(2^s\) is generally false. The Gaussian law uses isotropy in the zonotope's intrinsic metric, not a graph-dependent correlated normal. The asymptotic claims give limits for any \(k/n\to\rho\), not uniform quantitative convergence rates. The vertex-count identity, the general fan--acyclic-orientation correspondence, and the link between linear extensions and braid chambers are prior results. Bibliographic searches cannot rule out an independently discovered equivalent angular-spectrum formula under complete-multipartite or acyclic-orientation terminology. Independent verification of the full argument is not claimed.

## References

1. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (first public version, 2021-11-24), https://arxiv.org/abs/2111.12422. See Section 1.3 and Proposition 1.3.
2. F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896 (first public version, 2022-01-18), https://arxiv.org/abs/2201.06896. See Propositions 36--39, 48--50, 98--100.
3. OEIS Foundation, sequence A033815, *Number of standard permutations ...*, https://oeis.org/A033815. In particular, the recorded acyclic-orientation number of complete graphs with a perfect matching deleted is pre-existing.
