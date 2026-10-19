# Middle-layer actuators are exactly optimal on every odd hypercube

## Finding
Let \(n=2r+1\) with integer \(r\ge1\). Let \(Q_n\) be the undirected unweighted Boolean hypercube with vertex set \(\{0,1\}^n\) and combinatorial Laplacian \(L_n\). A vertex-actuation set \(T\) supplies one independent scalar input to each vertex of \(T\), and the continuous-time dynamics are \(\dot z=-L_nz+B_Tu\), with \(B_T\) the columns of the identity indexed by \(T\).

**Theorem.** The minimum number of input vertices needed for full-state controllability is exactly
\[
\gamma(Q_{2r+1})=\binom{2r+1}{r}.
\]
The entire Hamming-weight-\(r\) layer \(T_r=\{x\in\{0,1\}^{2r+1}:|x|=r\}\) is an explicit optimal input set, and so is its complementary weight-\(r+1\) layer. More sharply, for every \(j=0,\ldots,n\), the matrix of weight-\(j\) Walsh characters restricted to \(T_r\) has full column rank \(\binom nj\).

**Parity boundary.** On \(Q_{2r}\) with \(r\ge1\), no input set consisting of one complete Hamming-weight layer is controllable: all noncentral layers contain fewer vertices than the maximum Laplacian eigenspace dimension \(\binom{2r}{r}\), while the central-layer restriction to that eigenspace is singular. The theorem does not determine the even-dimensional unrestricted minimum.

## Assumptions and scope
Vertices are all \(n\)-bit vectors, with an edge of unit weight between vectors differing in exactly one coordinate. Each selected vertex is driven by its own independent unrestricted real-valued input. The scalar state at every vertex is part of the controllability objective; controllability is in the standard finite-dimensional Kalman/PBH sense. The result is not asserted for directed, anisotropically weighted, perturbed, time-varying, or structurally uncertain graphs, nor for one shared input acting on multiple vertices.

For subsets \(S,X\subseteq[n]\), put \(\chi_S(X)=(-1)^{|S\cap X|}\). For an integer \(j\), denote by \(V_j\) the real vector space of functions on \(j\)-subsets of \([n]\). Define \(M_{r,j}\colon V_j\to V_r\) by
\[
(M_{r,j}f)(X)=\sum_{|S|=j}(-1)^{|S\cap X|}f(S),\qquad |X|=r.
\]
The matrix \(M_{r,j}\) is the restriction of the weight-\(j\) Fourier eigenvectors to the selected input sites.

## Proof
**1. Lower bound from spectral multiplicities.** The Walsh characters form a complete orthogonal eigenbasis of \(L_n\), satisfying \(L_n\chi_S=2|S|\chi_S\). Hence the eigenspace of eigenvalue \(2j\) has dimension \(\binom nj\). The Popov–Belevitch–Hautus test for symmetric state matrices requires the restriction of every eigenspace to \(T\) to be injective. Therefore every controllable input set has size at least \(\max_j\binom nj=\binom{2r+1}{r}\).

**2. Harmonic slice decomposition.** For \(t\le k\le r\), select \(t\) pairwise disjoint ordered coordinate pairs \((a_i,b_i)\) and define a function on \(k\)-subsets,
\[
h_{t,k}(S)=\prod_{i=1}^t\bigl(\mathbf1_{a_i\in S}-\mathbf1_{b_i\in S}\bigr).
\]
In \(V_k\), the spans \(H_{t,k}\) of these functions for different \(t=0,\ldots,k\) are mutually orthogonal, have dimensions \(\binom nt-\binom n{t-1}\) (interpreting \(\binom n{-1}=0\)), and give
\[
V_k=\bigoplus_{t=0}^k H_{t,k}.
\]
For completeness, this is the standard harmonic decomposition of the Johnson slice: let \(U\colon V_k\to V_{k+1}\) be inclusion summation and \(D=U^*\). The elementary identity \(DU-UD=(n-2k)I\) on \(V_k\) gives injectivity of each raising map strictly below the middle rank. Its primitive level-\(t\) kernel \(\ker(D:V_t\to V_{t-1})\) has dimension \(\binom nt-\binom n{t-1}\); the pair-difference functions at level \(t\) span this kernel (the harmonic-basis/straightening lemma, in Filmus, Lemma 2.3). Their raised functions are \((k-t)!h_{t,k}\). Adjointness and the primitive-kernel property make the distinct raised levels orthogonal, and their dimensions sum to \(\binom nk\). Thus the displayed decomposition holds, including the claimed independence at levels \(k=j\) and \(k=r\).

**3. Exact scalar action of Fourier restriction.** Fix disjoint pairs as above, a level \(0\le t\le j\le r\), and a row subset \(X\) of size \(r\). The vector \(M_{r,j}h_{t,j}\) vanishes at \(X\) if any selected pair is wholly inside or wholly outside \(X\). Otherwise one member of each pair belongs to \(X\), and summing over the two choices in each pair contributes \(-2\) times the corresponding sign in \(h_{t,r}(X)\). The remaining \(j-t\) selected coordinates contribute the coefficient of \(z^{j-t}\) in a binomial product. Hence, *as an equality of functions*,
\[
M_{r,j}h_{t,j}=\alpha_{r,t,j}h_{t,r},\qquad
\alpha_{r,t,j}=(-2)^t[z^{j-t}](1-z)^{r-t}(1+z)^{n-r-t}.
\]
For \(n=2r+1\), this reduces to
\[
\alpha_{r,t,j}=(-2)^t[z^{j-t}](1-z^2)^{r-t}(1+z)
=(-2)^t(-1)^{\lfloor(j-t)/2\rfloor}\binom{r-t}{\lfloor(j-t)/2\rfloor}.
\]
The final integer is nonzero for every \(0\le t\le j\le r\). Consequently \(M_{r,j}\) maps each independent harmonic sector \(H_{t,j}\) injectively onto a scalar multiple of its corresponding sector \(H_{t,r}\); distinct sectors have independent images. Therefore \(M_{r,j}\) is injective for all \(j\le r\).

**4. Higher Fourier degrees.** If \(j>r\), complementing the frequency subset gives a bijection \(S\mapsto S^c\) from \(j\)-subsets to \((n-j)\)-subsets and, on the fixed row layer \(|X|=r\),
\[
\chi_{S^c}(X)=(-1)^r\chi_S(X).
\]
Thus the columns of \(M_{r,j}\) are a signed permutation of those of \(M_{r,n-j}\), where \(n-j\le r\). Injectivity follows. By the PBH test the selection \(T_r\) gives controllability; the lower bound in Step 1 makes it optimal. Complementing vertex coordinates carries \(T_r\) to the weight-\(r+1\) layer by a graph automorphism.

**5. Even-dimensional boundary.** Put \(n=2r\). The maximum eigenspace dimension is \(\binom{2r}r\), larger than any other Hamming-layer size. The only possible full-layer candidate is therefore the weight-\(r\) layer. But for each frequency set \(|S|=r\), its distinct complement also has size \(r\), and the two restricted columns satisfy \(\chi_{S^c}(X)=(-1)^r\chi_S(X)\). Thus the central restriction has dependent columns and fails PBH. This proves the stated parity boundary, without asserting the unrestricted even-dimensional optimum.

## Verification
Run `python3 artifacts/verify.py` using only the Python 3 standard library. The checker builds the actual Walsh restriction matrices and computes their ranks modulo the prime 1,000,003 for odd dimensions \(3,5,7,9\), verifies the pair-difference Fourier-image identity row by row, checks the explicit binomial coefficients for all \(1\le r\le50\), and detects the central-layer obstruction in even dimensions \(2,4,6,8\). A successful execution prints `VERIFICATION_OK` with 25,752 assertions. The prime-modulus ranks at these finite test sizes imply exact characteristic-zero full rank for those examples; they do not substitute for the harmonic-decomposition proof for arbitrary \(r\). All verifier inputs, calculations, and expectations appear in its self-contained source.

## Relationship to prior work
The PBH spectral-multiplicity lower bound and graph-controllability setting are standard. Notarstefano and Parlangeli (arXiv:1203.0129, initial 1 March 2012), in particular Section V and Remark 5.4, give general controllability criteria and grid-eigenvector decompositions, but not this explicit odd-hypercube optimal middle-layer construction and parity boundary. Zhang, Camlibel, and Cao (CDC-ECC 2011) treat distance-regular networks and provide multi-leader tests while identifying explicit choices for cycles and complete graphs; no matching all-odd-hypercube minimum appears in their examined paper. The harmonic pair-difference/Young basis used in Step 2 is pre-existing: see Filmus (arXiv:1406.0142, first 1 June 2014), Lemma 2.3 and Theorem 4.1. The nonvanishing scalar action in Step 3 and its precise controllability consequences are the contribution assessed here, not the known basis or the PBH theorem.

Related published Fourier-concentration work on Hamming *balls*, nonbinary alphabets, or mixed low-pass bands does not by itself imply an injective restriction for every individual *homogeneous* Walsh eigenspace of the binary odd cube. In particular, a mixed-degree restriction can have a kernel even when each separate degree is injective. Despite these distinctions, equivalent formulations in the wider Johnson-association-scheme and controllability literature cannot be completely excluded without an independent exhaustive review.

## Limitations
The theorem concerns the uniform undirected hypercube, separately addressable vertex actuators, exact state controllability, and odd dimensions only for the minimum. The even-dimensional result rules out complete single-weight-layer sets but does not settle the optimal heterogeneous set size. The number of required actuators grows as a central binomial coefficient; the construction does not address actuator placement with robustness, cost, energy, or bounded-input constraints. Although finite verification confirms exact algebra in tested cases, the unlimited-dimensional statement relies on the mathematical argument and the classical harmonic-basis lemma. Independent scientific audit has not been performed.

## References
1. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129 (initial submission 2012-03-01), https://arxiv.org/abs/1203.0129.
2. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (initial submission 2014-06-01), https://arxiv.org/abs/1406.0142.
3. S. Zhang, M. K. Camlibel and M. Cao, *Controllability of diffusively-coupled multi-agent systems with general and distance regular coupling topologies*, CDC-ECC 2011, pp. 759–764, https://pure.rug.nl/ws/files/13905758/2011ProcCDCZhang.pdf.
