# Sharp fastest-diffusion design and optimal-face transfer for pendant coronas of transitive graphs

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite connected simple graph with \(n\ge3\) vertices and \(m\) edges. Assume its automorphism group acts transitively on both vertices and edges. Write \(L_G\) for its unweighted combinatorial Laplacian and \(\mu=\lambda_2(L_G)>0\). Attach one private leaf to each vertex, obtaining the corona \(H=G\circ K_1\). On each original edge choose an independent rate \(w_e\ge0\), on each leaf edge choose an independent rate \(b_i\ge0\), and require
\[
 t\sum_{e\in E}w_e+\sum_{i\in V}b_i=B,\qquad t>0,\ B>0.
\]
The maximum of the second-smallest eigenvalue of the weighted Laplacian \(L_H(w,b)\) is exactly
\[
 \boxed{\lambda_* = \frac{B}{n(1+2r+2r^2)}},\qquad
 r=\sqrt{\frac{mt}{n\mu}}>0.
\]
Define \(a_* = \lambda_*(2+1/r)/\mu\) and \(b_*=\lambda_*(1+r)\). All base rates equal to \(a_*\) and all leaf rates equal to \(b_*\) attain the maximum. **Every** globally optimal vector of independent edge rates satisfies \(b_i=b_*\) for every private leaf. Its base rates are exactly the optimal rate vectors on \(G\) under the fixed total base rate
\[
 \sum_{e\in E}w_e=W_*=m a_*.
\]
Equivalently, they are exactly the nonnegative base-edge assignments with total \(W_*\) and
\[
 \lambda_2(L_G(w))=\frac{\mu W_*}{m}=\mu a_*.
\]
For \(G=C_n\) (\(n\ge3\)) or \(G=K_n\) (\(n\ge3\)), the full corona optimum is unique, even without an imposed symmetry condition. In the cyclic case \(\mu=4\sin^2(\pi/n)\), \(m=n\), hence \(r=\sqrt{t/\mu}\). The budget fractions spent on the leaf and base edges are respectively
\[
 \frac{1+r}{1+2r+2r^2},\qquad \frac{r+2r^2}{1+2r+2r^2}.
\]
The family thus has an exact continuous crossover at \(mt/(n\mu)\) of order one, and not a support-deletion threshold: both edge classes remain positive at every finite positive price.

## Assumptions and scope

We use the combinatorial Laplacian \(L=\sum_{\{i,j\}} w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T}\) with no normalization by degree; \(\lambda_2\) is its second eigenvalue in increasing order. Only a simple, undirected, connected base with vertex and edge transitivity is assumed, and no restriction to invariant edge assignments is made in the optimization. The unit-cost private leaves form a matching and are attached one-to-one. Base-edge cost is the common positive number \(t\). The constraint is expenditure equality, with total budget \(B>0\). The Markov generator is \(-L\); the spectral gap controls continuous-time convergence to the uniform equilibrium. All displayed rates are finite and positive.

## Proof

**1. Projection certificate.** Let \(F=\ker(L_G-\mu I)\) have dimension \(k\ge1\), let \(P\) be the orthogonal projector onto \(F\), and let \(\phi_1,\ldots,\phi_k\) be an orthonormal basis. Automorphisms commute with \(L_G\), hence with \(P\). Vertex transitivity forces \(P_{ii}=k/n\). Edge transitivity similarly makes \((e_i-e_j)^{\mathsf T}P(e_i-e_j)\) constant across edges, and summing it over edges gives \(\operatorname{tr}(L_GP)=k\mu\); consequently every edge has value \(k\mu/m\).

For each \(\phi_j\), take the mean-zero test vector on the corona whose base entries are \(r\phi_j\) and leaf entries are \((1+r)\phi_j\). The sum of their squared norms is \(kS\), where \(S=r^2+(1+r)^2=1+2r+2r^2\). Their summed Dirichlet energies for arbitrary independent feasible \(w,b\) are
\[
 k\left(\frac{r^2\mu}{m}\sum_{e\in E}w_e+\frac1n\sum_{i\in V}b_i\right)
 =\frac{kB}{n},
\]
using \(r^2\mu/m=t/n\). Every mean-zero Rayleigh quotient is at least \(\lambda_2(L_H)\). Summing therefore yields the **global certificate**
\[
 \lambda_2(L_H(w,b))\le\frac{B}{nS}=\lambda_*.
\]
No symmetry of \(w,b\) was used.

**2. Attainment.** Give every base edge conductance \(a_*\), and every leaf edge conductance \(b_*\). The budget is met since
\[
 mt a_*+nb_*=n\lambda_*[r^2(2+1/r)+(1+r)]
 =n\lambda_*S=B.
\]
If \(\nu\ge0\) is a base Laplacian eigenvalue, its two corresponding corona eigenvalues are the eigenvalues of
\[
 \begin{pmatrix} a_*\nu+b_*&-b_*\\-b_*&b_*\end{pmatrix},
\]
namely
\[
 \Lambda_\pm(\nu)=\frac{a_*\nu+2b_*\pm\sqrt{a_*^2\nu^2+4b_*^2}}2.
\]
For \(\nu=0\) they are \(0,2b_*\). For \(\nu>0\), \(\Lambda_-(\nu)\) is strictly increasing with \(\nu\), and is smaller than \(b_*\). Consequently the corona gap is \(\Lambda_-(\mu)\). Direct substitution of \(a_*\mu=\lambda_*(2+1/r)\), \(b_*=\lambda_*(1+r)\) into the eigenvalue equation shows that \((r,1+r)\) is a positive eigenvector for the lower eigenvalue \(\lambda_*\). Hence the upper bound is attained.

**3. All optimizers and transfer of optimal faces.** Equality in the summed Rayleigh certificate forces *each* lifted \(\phi_j\) to be a second-eigenvalue eigenvector of the candidate corona Laplacian. At the leaf of vertex \(i\), its eigenvalue equation is \(b_i\phi_j(i)=\lambda_*(1+r)\phi_j(i)\). Since \(P_{ii}=k/n>0\), some \(\phi_j(i)\ne0\) for every \(i\); therefore \(b_i=b_*\) for every optimal design. The budget then fixes \(\sum_e w_e=W_*=ma_*\).

For **any** base weight vector \(w\) and constant pendant rate \(b_*\), diagonalizing the base weighted Laplacian gives exactly the same \(2\)-by-\(2\) blocks as above, with \(a_*\nu\) replaced by its weighted eigenvalues \(\xi\). Strict increase of the lower branch means \(\lambda_2(L_H(w,b_*))=\lambda_*\) exactly when \(\lambda_2(L_G(w))=a_*\mu\). The base transitive-projector certificate gives \(\lambda_2(L_G(w))\le(\mu/m)\sum_e w_e=\mu a_*\), with equality attained by uniform base weights. Hence the set of full optimizers maps bijectively onto the full base-graph optimal face, after fixing all pendant weights to \(b_*\).

**4. Unrestricted uniqueness for cycles and cliques.** On \(C_n\), the complex first Fourier mode \(z^i\), with \(z=e^{2\pi \mathrm i/n}\), lies in the base Fiedler space; the equality certificate requires \(L_G(w)z^i=\mu a_*z^i\). Thus
\[
 w_i(1-z)+w_{i-1}(1-z^{-1})=\mu a_*.
\]
Its imaginary part is \((w_{i-1}-w_i)\sin(2\pi/n)=0\). Because \(n\ge3\), all base weights coincide, proving uniqueness. On \(K_n\), the Fiedler eigenspace is the whole orthogonal complement of constants. Equality implies that \(L_G(w)\) acts as the single scalar \(na_*\) there, hence \(L_G(w)=na_*(I-\mathbf1\mathbf1^{\mathsf T}/n)\) and every original edge has weight \(a_*\).

## Verification

A standalone script `VERIFY.py` constructs full \(2n\)-by-\(2n\) weighted Laplacians for cycles, cliques, hypercubes, balanced bicliques, and the Petersen graph. It tests budget normalization, projector symmetry, the exact candidate eigenvalue, randomized noninvariant feasible edge assignments, and exact symbolic price/eigenvalue identities. A complete run passed 4209 finite assertions. These computations are evidence of implementation consistency, not a proof for all graphs or all prices; the proof above supplies the quantified theorem. For \(C_4\), \(t=2\), \(B=20\), the formulas give \(\mu=2\), \(r=1\), \(a_*=3/2\), \(b_*=2\), and \(\lambda_*=1\).

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis introduced the weighted-budget continuous-time fastest-mixing problem, its concavity, semidefinite program, dual certificate, and cycle/path examples [1]. These supply foundational optimization theory, but their inspected problem formulation, duality, and examples do not give the one-leaf corona formula or optimal-face transfer. Barik, Pati, and Sarma gave a general **unweighted** corona Laplacian spectral transformation [2]. This informs the block decomposition but does not optimize arbitrary priced edge conductances. Olesker-Taylor and Zanetti [3] give general qualitative geometric mixing bounds rather than exact pendant-corona optimal prices. Earlier discrete-time sunlet optimization concerns minimizing the modulus of stochastic transition eigenvalues under row constraints; it does not imply the continuous-time weighted-Laplacian formula or unrestricted rigidity here. The present theorem explicitly proves the optimal rate, all pendant weights of every optimizer, and the equivalence of optimal faces. No claim of novelty is made for the general SDP formulation or unweighted corona spectral identity.

## Limitations

No uniqueness for base weights is asserted for arbitrary vertex-and-edge-transitive bases; the theorem identifies the full optimal face through the base-graph problem. Neither graphs that are only vertex-transitive, graphs that are only edge-transitive, variable private-leaf prices, extra cross-leaf connections, directed chains, nor normalized Laplacians are covered. Numerical tests are finite. An equivalent explicit optimal-face theorem in unindexed literature cannot be excluded. Independent audit has not been performed.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699, DOI `10.1137/S0036144504443821`. Electronically published 2006-11-02; relevant material: Sections 1, 3–5.
2. S. Barik, S. Pati, and B. K. Sarma, *The Spectrum of the Corona of Two Graphs*, SIAM Journal on Discrete Mathematics **21** (2007), 47–56, DOI `10.1137/050624029`. Relevant material: Theorem 3.2 and proof.
3. S. Olesker-Taylor and L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, Probability Theory and Related Fields **188** (2024), 1017–1062, DOI `10.1007/s00440-023-01257-x`. Relevant material: Section 4.
