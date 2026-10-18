# Gaussian normal-cone moment condensation for complete-bipartite graphical zonotopes

## Finding

Let \(Z_{p,q}\) be the graphical zonotope of the complete bipartite graph \(K_{p,q}\), for integers \(p,q\ge2\). For integer \(t\ge2\), let \(C_t(p,q)\) be the probability that \(t\) independent uniformly distributed Euclidean directions in its affine-span direction space all expose the **same vertex**. Define the formal power series
\[
F_t(z)=\sum_{j\ge1}(j!)^{t-1}z^j.
\]
There is an exact identity
\[
\boxed{C_t(p,q)=\frac{p!q!}{(p+q)!^t}[x^py^q]\frac{F_t(x)+F_t(y)+2F_t(x)F_t(y)}{1-F_t(x)F_t(y)}.}\tag{1}
\]
In particular, for any **fixed** integers \(p\ge2\) and \(t\ge2\), as \(q\to\infty\),
\[
\boxed{C_t(p,q)=\frac{p!(q!)^t}{(p+q)!^t}\left(\sum_{r=0}^{p}[r!(p-r)!]^{t-1}+O_{p,t}(q^{-(t-1)})\right)\sim K_{p,t}q^{-pt},}\tag{2}
\]
where \(K_{p,t}=p!\sum_{r=0}^p[r!(p-r)!]^{t-1}\). Formula (1), all assertions below, and the normal-cone probabilities are **independent of strictly positive edge weights**.

More precisely, each exposed vertex corresponds to a unique alternating sequence of nonempty blocks of first-side and second-side labels. Call an orientation *condensed* if the \(q\) second-side labels form a **single** block. There are exactly \(2^p\) such vertices; altogether their unconditioned exposure probability is
\[
\boxed{\Pr(\text{condensed})=\frac{(p+1)p!q!}{(p+q)!}=O_p(q^{-p}),}\tag{3}
\]
which vanishes. Yet **conditional on a collision among \(t\) independent directions**, the probability of condensation tends to one with error \(O_{p,t}(q^{-(t-1)})\). Moreover, conditional on the collision, if \(r\) is the number of first-side labels preceding the unique second-side block, then
\[
\boxed{\Pr(r\mid t\text{-collision})\longrightarrow
\frac{[r!(p-r)!]^{t-1}}{\sum_{j=0}^{p}[j!(p-j)!]^{t-1}}\quad(0\le r\le p).}\tag{4}
\]

The vertex count satisfies \((p+1)^q\le f_0(Z_{p,q})\le p!(p+1)^q\). Therefore its order-\(t\) Rényi entropy \(H_t=(1-t)^{-1}\log C_t\) obeys
\[
\boxed{H_t(Z_{p,q})=\frac{pt}{t-1}\log q-\frac{\log K_{p,t}}{t-1}+o(1),}\tag{5}
\]
although \(\log f_0(Z_{p,q})=q\log(p+1)+O_p(1)\). For example, \(C_2(2,q)\sim10q^{-4}\), despite \(f_0(Z_{2,q})=2\cdot3^q-2^q\).

## Assumptions and scope

The bipartition is \(A\sqcup B\), with \(|A|=p\) and \(|B|=q\). The polytope is \(Z_{p,q}=\sum_{a\in A,b\in B}\lambda_{ab}[e_a,e_b]\), with every \(\lambda_{ab}>0\). Its intrinsic direction space is the zero-coordinate-sum subspace of \(\mathbb R^{p+q}\). Expose a vertex using a continuously distributed isotropic Gaussian objective in this subspace, equivalently its normalization to a uniform unit direction. Hyperplane ties have probability zero. The collision event concerns the **same vertex label**, not equality of the support values or closeness of independently exposed points. The limit requires \(p,t\) fixed and \(q\to\infty\); no uniformity in growing \(p\) or \(t\) is asserted. Every power series in (1) is **formal**: convergence as an analytic series is not used.

## Proof

**1. Normal cones and linear extensions.** For a generic objective \(u\), each weighted segment \(\lambda_{ab}[e_a,e_b]\) contributes its maximizing endpoint; its choice depends solely on the sign of \(u_a-u_b\). These signs orient the graph acyclically. Conversely every acyclic orientation has an exposing objective. Thus vertices correspond bijectively to acyclic orientations, and positive edge weights do not change their normal cones. The ranks of independent identically distributed Gaussian coordinates form a uniform random permutation; orthogonally subtracting their common mean does not change comparisons. Write \(\ell(\omega)\) for the number of permutations compatible with an acyclic orientation \(\omega\). Then
\[
\Pr(\omega)=\frac{\ell(\omega)}{(p+q)!},\qquad
C_t(p,q)=\sum_{\omega}\left(\frac{\ell(\omega)}{(p+q)!}\right)^t.\tag{6}
\]

**2. Canonical alternating blocks.** A permutation of \(A\sqcup B\) decomposes uniquely into its maximal nonempty monochromatic runs (\(A\)-runs or \(B\)-runs), with alternating colors. Two permutations determine the same orientation of the *complete* bipartite graph if and only if these alternating ordered blocks agree as labeled sets. Indeed, the relative position of any \(a\in A\) and \(b\in B\) determines the orientation of their connecting edge. Swapping consecutive same-side elements preserves all orientations. Conversely, any two linear extensions of the same acyclic orientation are linked by adjacent swaps of incomparable elements; a cross-side pair is always adjacent in the graph and hence comparable in its induced poset, so only same-side swaps are possible. If the block sizes are \(r_1,\ldots,r_a\) and \(s_1,\ldots,s_b\), the number of compatible permutations is
\[
\ell(\omega)=\prod_{i=1}^{a}r_i!\prod_{j=1}^{b}s_j!,\quad
|a-b|\le1,\quad a,b\ge1.
\]
For fixed block sizes the number of ways to distribute the labeled vertices among the ordered blocks is \(p!q!/(\prod r_i!\prod s_j!)\). Consequently the total weight \(\sum_\omega\ell(\omega)^t\) is \(p!q!\) times the sum over all alternating compositions of \(p,q\) of \(\prod_i(r_i!)^{t-1}\prod_j(s_j!)^{t-1}\). An alternating block sequence is either a singleton of one color, or contains equal numbers of blocks starting with either color, or one more block of the starting color. The generating function for these three cases is exactly
\[
\frac{F_t(x)+F_t(y)+2F_t(x)F_t(y)}{1-F_t(x)F_t(y)}.
\]
Extracting \([x^py^q]\) proves (1).

**3. The complete leading family.** If there is exactly one \(B\)-block, the permitted sequences are \(B\)-then-\(A\), \(A\)-then-\(B\), and \(A\)-\(B\)-\(A\). Writing \(r\) for the size of the \(A\) portion before the \(B\)-block, \(0\le r\le p\), their total weighted contributions sum exactly to
\[
\boxed{p!(q!)^t\sum_{r=0}^{p}[r!(p-r)!]^{t-1}.}\tag{7}
\]
The endpoints \(r=0,p\) encode the two-block sequences; the interior values encode the three-block sequences.

**4. Uniformly suppressing all other block patterns.** For \(b\ge1\) define the positive integer
\[
R_b(q)=\sum_{\substack{s_1+\cdots+s_b=q\\s_i\ge1}}\prod_{i=1}^b s_i!.
\]
For every integer \(m\ge2\), the elementary binomial bound
\[
\sum_{s=1}^{m-1}\binom ms^{-1}\le \frac4m\tag{8}
\]
holds (the two endpoints contribute \(2/m\), and the remaining terms admit a bound using \(\binom m2\); small \(m\) is direct). Induction on \(b\), via the convolution for \(R_b\), gives
\[
R_b(q)\le 4^{b-1}(q-b+1)!\qquad(q\ge b).\tag{9}
\]
Indeed, insert the induction bound into \(R_b(q)=\sum_{s=1}^{q-b+1}s!R_{b-1}(q-s)\), put \(m=q-b+2\), and apply (8) to \(\sum_{s=1}^{m-1}s!(m-s)!\).

For integer \(t\ge2\), positivity implies
\[
\sum_{s_1+\cdots+s_b=q}\prod_i(s_i!)^{t-1}\le R_b(q)^{t-1}.
\]
Thus for each fixed \(b\ge2\), after dividing by \((q!)^{t-1}\), this expression is \(O_{b,t}(q^{-(b-1)(t-1)})\). An alternating sequence with \(p\) total first-side labels has at most \(p+1\) second-side blocks, and its first-side block-size contributions are constants depending only on \(p,t\). Summing finitely many patterns, all sequences having \(b\ge2\) are an \(O_{p,t}(q^{-(t-1)})\) relative correction to (7). Division by \((p+q)!^t\) proves the first equality in (2); \(q!/(p+q)!\sim q^{-p}\) proves its equivalent form.

**5. Conditional condensation.** Exactly one second-side block means that every \(B\) label is contiguous in every compatible permutation, and the orientation is specified by choosing the subset of \(A\) labels above it: \(2^p\) orientations. For each \(r\), there are \(\binom pr\) such orientations, each with \(\ell=r!(p-r)!q!\). Their total *unconditioned* probability is
\[
\frac{q!}{(p+q)!}\sum_{r=0}^{p}\binom pr r!(p-r)!=\frac{(p+1)p!q!}{(p+q)!},
\]
proving (3). In the collision-power measure, the same family carries precisely the leading sum (7); (9) bounds the remaining mass, establishing condensation and (4).

**6. Exponential combinatorial complexity versus logarithmic angular entropy.** Fix an ordering of the \(p\) first-side labels. Each of the \(q\) second-side labels may be placed into one of the \(p+1\) gaps; different gap assignments produce distinct orientations, giving the lower bound \((p+1)^q\). Conversely, every orientation is represented by at least one of \(p!\) possible first-side orders together with a gap assignment of each second-side label, giving the upper bound \(p!(p+1)^q\). Substitute (2) into the definition \(H_t=(1-t)^{-1}\log C_t\) to obtain (5).

## Verification

The standalone Python 3 checker `CHECKER.py` independently enumerates all \((p+q)!\) permutations for each pair \(1\le p\le4\), \(1\le q\le5\) with \(p+q\le8\). It groups permutations by their complete cross-edge orientation sign matrices and sums powers of their class sizes for \(t=2,3,4\); separately it evaluates (1) by dynamic programming on alternating block compositions. All 57 such exhaustive finite checks agree, and 15 additional integer comparisons confirm the exact leading contribution is a lower bound at \(q=25\). The checker prints `PASS 72 independent exhaustive collision-moment and leading-term checks`. The proof of (2) is the analytic estimate (8)–(9), not finite extrapolation.

## Relationship to prior work

Padrol, Pilaud and Poullot develop graphical zonotopes and their deformations and establish the normal-fan/acyclic-orientation setting [1]. Iriarte studies how linear-extension counts determine the probabilities of acyclic orientations under random total orders [2]; that normalization is used explicitly in (6), not presented as new. Chapoton and Pilaud describe graphical-zonotope shuffles and the complete-bipartite construction [3]. Cameron, Glass, Rekvényi and Schumacher study acyclic-orientation numbers of complete bipartite graphs [4], an unweighted count, not the powers of Euclidean normal-cone masses. Khera and Lundberg study the longest directed path under a different, uniformly random orientation law [5]. Related earlier geometric results determine enclosing ellipsoids, contact sets and circumspheres of complete-bipartite/multipartite graphical zonotopes [6,7], rather than moment spectra of Gaussian cone volumes. The contribution here is (1) together with the fixed-small-side moment condensation, explicit constants, and entropy separation (2)–(5).

## Limitations

The asymptotic analysis fixes the smaller part size and the integer collision order; it is not uniform for growing \(p\) or real orders \(t\). The distribution sampled here is Gaussian/spherical normal-cone exposure, not uniformly random acyclic orientations. The high-order moment identity may have an equivalent earlier formulation in weighted ordered-partition or linear-extension enumerations; the literature comparison does not prove bibliographic uniqueness. Numerical checks are exhaustive only for the stated finite bounds. Independent mathematical validation has not been carried out.

## References

[1] A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (first version publicly posted 2021-11-24), https://arxiv.org/abs/2111.12422 .

[2] B. Iriarte, *Graph Orientations and Linear Extensions*, arXiv:1405.4880 (2014), https://arxiv.org/abs/1405.4880 .

[3] F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896 (2022), https://arxiv.org/abs/2201.06896 .

[4] P. J. Cameron, C. A. Glass, K. Rekvényi and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685 (2014), https://arxiv.org/abs/1412.3685 .

[5] S. Khera and E. Lundberg, *The distribution of the length of the longest path in random acyclic orientations of a complete bipartite graph*, arXiv:2408.12716 (2024), https://arxiv.org/abs/2408.12716 .

[6] *Exact Löwner ellipsoid and contact vertices of complete-bipartite graphical zonotopes*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-l-wner-ellipsoid-and-contact-vertices-of-complete-bipartit--3af21ae2f6c8 .

[7] *Complete multipartite graphical zonotopes have cubic-moment circumspheres*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-multipartite-graphical-zonotopes-have-cubic-moment-circ--2fc427ff213b .
