# Sharp binary fourth moments on the four-cube and quadratic path rigidity through seven variables

## Finding

For an integer \(d\geq 2\), let \(\mathbb T^d\) have normalized Haar measure and let
\[
P_a(z)=\sum_{x\in\{0,1\}^d}a_x\prod_{j=1}^d z_j^{x_j},\qquad a_x\in\{-1,1\}.
\]

**Exact unrestricted binary result in dimension four.** Among all \(2^{16}\) binary coefficient arrays when \(d=4\),
\[
\min_a\int_{\mathbb T^4}|P_a(z)|^4\,dm(z)=336.
\]
Equality holds exactly when there are a sign \(\sigma\in\{-1,1\}\), a vector \(b\in\mathbb F_2^4\), and a permutation \(\pi\) of \(\{1,2,3,4\}\) such that, for every \(x\in\{0,1\}^4\),
\[
a_x=\sigma(-1)^{\sum_{j=1}^4 b_jx_j+
 x_{\pi(1)}x_{\pi(2)}+x_{\pi(2)}x_{\pi(3)}+x_{\pi(3)}x_{\pi(4)}}.
\]
There are exactly \(384\) different minimizing sign arrays, falling into \(12\) classes modulo global sign and the four independent coordinate-sign modulations. Coordinate permutation identifies all twelve classes.

**Quadratic subclass in dimensions four through seven.** Let \(4\le d\le7\), let \(G\) be a simple labeled graph on \(\{1,\ldots,d\}\), and restrict the coefficients to the quadratic Boolean phases
\[
a_x=\sigma(-1)^{\sum_{\{i,j\}\in E(G)}x_ix_j+\sum_{j=1}^d b_jx_j}.
\]
Within precisely this subclass, the sharp fourth-moment minimum is
\[
\boxed{\min_{G,\sigma,b}\int_{\mathbb T^d}|P_a|^4\,dm
=\frac{2^d\bigl(2^{d+2}-(-1)^d\bigr)}{3}.}
\]
Equality occurs exactly for graphs \(G\) that are spanning paths. The values in dimensions \(4,5,6,7\) are respectively \(336,1376,5440,21888\), with \(d!/2\) distinct path graphs and \(2^{d+1}d!/2\) distinct minimizing coefficient arrays in dimension \(d\).

## Assumptions and scope

The measure is normalized Haar measure; thus \(\int_{\mathbb T^d}1\,dm=1\). Frequencies are the vertices of the integer unit cube, not the elements of a Boolean group under cyclic convolution. The coefficients are required to be real binary signs. The dimension-four assertion quantifies over **all** such arrays, without a restriction on algebraic degree. The assertion for dimensions five through seven quantifies only over the specified quadratic Boolean family. Affine phase terms and graph vertex relabelings have the precise meanings given above. There is no assertion about arbitrary complex unimodular phases, arbitrary binary coefficients in dimensions five through seven, or all higher dimensions.

## Proof

**Fourier-convolution identity.** Write \(c_t=\sum_{x+y=t}a_xa_y\), where \(x,y\in\{0,1\}^d\) and \(t\in\{0,1,2\}^d\), with integer rather than modulo-two addition. Orthogonality on the torus yields the exact identity
\[
\int_{\mathbb T^d}|P_a|^4\,dm
=\sum_{t\in\{0,1,2\}^d}|c_t|^2.
\]
Every term is an explicitly computable integer square. This establishes the complete finite decision procedure for all binary arrays in dimension four.

**Quadratic phases and induced Eulerian subgraphs.** For a graph \(G\) on \(d\) vertices define \(q_G(x)=\sum_{\{i,j\}\in E(G)}x_ix_j\pmod2\). In a convolution fiber \(x+y=t\), let \(S=\{j:t_j=1\}\). Outside \(S\) the coordinates of \(x\) and \(y\) agree and are fixed. Inside \(S\) they are complementary. Thus the parity of \(q_G(x)+q_G(y)\) is affine in the free coordinates of \(x\), with coefficient at vertex \(i\in S\) equal to the degree of \(i\) in the induced graph \(G[S]\), modulo two. Summing its sign over the \(2^{|S|}\) free choices gives \(0\) if any induced degree is odd, and \(\pm2^{|S|}\) otherwise. The affine Boolean phase does not change the absolute convolution coefficient. There are exactly \(2^{d-|S|}\) fibers with that same free-coordinate set. Consequently, for **every** integer \(d\ge2\) and every graph \(G\),
\[
\boxed{\int_{\mathbb T^d}|P_a|^4\,dm
=2^d\!\sum_{\substack{S\subseteq V(G)\\\deg_{G[S]}(v)\ \mathrm{even}\ \forall v\in S}}2^{|S|}.}
\]
This is a proved identity, not an assertion of universal optimality. It reduces the quadratic-phase optimization to a finite weighted count of induced Eulerian subgraphs.

**The path candidate.** When \(G\) is a forest, an induced subgraph with all degrees even must have no edges, because a nonempty forest has a vertex of degree one. Hence the weighted sum above becomes the independence polynomial evaluated at \(2\). For a path, this polynomial obeys \(J_d=J_{d-1}+2J_{d-2}\) with \(J_0=1\) and \(J_1=3\), so
\[
J_d=\frac{2^{d+2}-(-1)^d}{3}.
\]
This establishes the asserted attained values, but not by itself their minimality among arbitrary graphs or sign arrays.

**Exhaustive finite certificates and equality.** The embedded standalone `checker.cpp` exactly enumerates all \(2^{11}=2048\) sign arrays satisfying \(a_0=a_{e_1}=\cdots=a_{e_4}=1\). Every one of the \(2^{16}\) sign arrays has exactly one such representative after a global-sign change and four coordinate-sign changes; these transformations preserve the Haar integral. The program computes all \(81\) squared convolution coefficients using integer arithmetic. Its complete minimum set has \(12\) members and agrees *as a set*, not merely in cardinality, with the sign arrays generated by the \(12\) distinct labeled four-vertex paths. The gauge group has size \(32\), acts freely, and gives exactly \(12\cdot32=384\) equality arrays.

For each \(d\in\{2,3,4,5,6,7\}\), the checker then enumerates all \(2^{\binom d2}\) simple labeled graphs using a bijective Gray-code enumeration of their edge masks. For each graph it evaluates the derived weighted Eulerian formula over **every** one of its \(2^d\) vertex subsets. It records the exact minimum and the complete set of minimizing edge masks, and independently generates all \(d!/2\) labeled path edge masks by permutations. The two sets agree for each of the six dimensions, with the minimum given by \(J_d\). In particular, this is an exhaustive proof of the asserted quadratic subclass result for \(4\le d\le7\), with no extrapolation to \(d\ge8\). The smaller dimensions provide internal boundary checks, not separate novelty claims.

## Verification

From the directory containing the embedded source file run `g++ -O3 -std=c++17 checker.cpp -o checker && ./checker`. The actual embedded source was compiled and executed. It returned `CHECK_PASS`, the dimension-four minimum \(336\) with \(12\) normalized and \(384\) total sign extremizers, and the graph counts \(2,8,64,1024,32768,2097152\) for dimensions two through seven respectively. The graph minimum sequence was \(20,88,336,1376,5440,21888\), with minimizing graph counts \(1,3,12,60,360,2520\). All comparisons and arithmetic in this test are integer-exact.

The checker contains a direct convolution calculation for the unrestricted four-cube, not just a repetition of the graph formula. The graph enumeration compares its entire set of minimizers with the path enumeration, which tests uniqueness as well as optimality. Mathematical completeness of the enumerations follows from their explicit fixed-width binary masks and complete loop bounds, not from extrapolation from sampled instances.

## Relationship to prior work

The path-shaped quadratic Boolean forms are not new constructions. Pai and Chen (2021), in their development of generalized-Boolean-function complementary array *pairs*, explicitly describe this path construction and its permutation count. Zhang, Fan and Mesnager (2021) likewise treat generalized-Boolean-function constructions of complementary array *pairs*. Neither inspected paper establishes the sharp fourth moment for an individual unrestricted binary sixteen-mode four-dimensional cube, nor the optimality of path graphs among all quadratic Boolean phases in dimensions five through seven. In those works, cancellation occurs in sums of autocorrelations of two arrays; here the object is one array's entire squared-autocorrelation mass.

Danielsen and Parker's work on graph interlace polynomials (published before the motivating sources) gives the **unweighted** count of induced Eulerian subgraphs as an interlace-polynomial evaluation and discusses a different Clifford merit factor. That does not furnish the cardinality-weighted sum in this claim or prove its path-optimality statement. The earlier eight-mode three-dimensional cube calculation is a covered lower-dimensional antecedent; the unrestricted sixteen-mode statement and the dimension-five-through-seven quadratic optimality are not consequences of it.

## Limitations

The sharp lower bound \(336\) is proved for **binary coefficients**, not for all complex phases. The higher-dimensional bounds are proved **only for quadratic Boolean coefficients**. Although the graph moment identity is valid in every dimension, the assertion that paths globally minimize its weighted induced-Eulerian count has only been proved here through dimension seven. The complete finite verification is an exhaustive computational proof with accompanying source; it is not an independent mathematical review. Specialized array-design and graph-polynomial literature could contain equivalent optimum statements under alternative normalization. No claim of independent validation or absolute bibliographic novelty is made.

## References

1. C.-Y. Pai and C.-Y. Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, first posted 8 February 2021, https://arxiv.org/html/2102.04043v1 . Relevant material: definitions of aperiodic correlation, Theorem 12, Corollary 15 and its Hamilton-path permutation count, conclusions.
2. H. Zhang, C. Fan and S. Mesnager, *New constructions of q-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1, first posted 24 July 2021, https://arxiv.org/html/2107.11599v1 . Relevant material: Definitions 4–6, Lemma 1, Theorems 1–2, conclusions.
3. L. E. Danielsen and M. G. Parker, *Interlace Polynomials: Enumeration, Unimodality, and Connections to Codes*, arXiv:0804.2576v2, https://arxiv.org/html/0804.2576v2 . Relevant material: the evaluation of the global interlace polynomial at \(4\), Table 5, and the Clifford merit-factor discussion.
