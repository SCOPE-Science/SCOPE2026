# Complete adjacency spectrum of the bipartite zero-divisor–unit graph of finite reduced rings

## Finding
Let \(R=\prod_{i=1}^{r}\mathbb F_{q_i}\) be a finite commutative reduced ring that is not a field; thus \(r\ge2\) and each \(q_i\ge2\) is a prime power. Write \(m_i=q_i-1\), \(M=\prod_i m_i\), \(Q=\prod_i(m_i+1)\), \(F=\prod_i(m_i-1)\), and \(N=Q-M-1\). For \(T\subseteq[r]=\{1,\ldots,r\}\), define \(w_T=\prod_{i\in T}(m_i-1)\), with the empty product equal to one. For each nonempty proper \(T\), put
\[
\lambda_T=\prod_{i\notin T}(m_i^2-m_i+1)-\prod_{i\notin T}(m_i-1)^2.
\]
For the empty set put
\[
\lambda_\varnothing=\sum_{\varnothing\ne J\subsetneq[r]}
 \Bigl(\prod_{i\notin J}m_i\Bigr)
 \Bigl(\prod_{i\in J}m_i-\prod_{i\in J}(m_i-1)\Bigr)^2.
\]
Then the adjacency characteristic polynomial of the bipartite zero-divisor–unit graph of \(R\) is exactly
\[
\boxed{\chi_{\mathcal B(R)}(x)=x^{\,N-M+2F}\prod_{T\subsetneq[r]}(x^2-\lambda_T)^{w_T}.}
\]
Thus, for each proper \(T\) with \(w_T>0\), the adjacency spectrum contains \(\sqrt{\lambda_T}\) and \(-\sqrt{\lambda_T}\), each with multiplicity \(w_T\); equal numerical eigenvalues from distinct supports have their multiplicities added. The zero eigenvalue has multiplicity \(N-M+2F\). The incidence matrix has rank \(M-F\). These formulas include all products of finite fields of unequal orders, including factors \(\mathbb F_2\).

The empty-support eigenvalue also admits the closed form
\[
\lambda_\varnothing=MQ-2M^2+\prod_i(m_i^2-m_i+1)-(M-F)^2.
\]
For \(T=[r]\), set \(\lambda_T=0\). This value occurs in the unit-side Gram spectrum with multiplicity \(F\), not as an additional positive factor in the displayed characteristic polynomial.

## Assumptions and scope
The graph \(\mathcal B(R)\) has disjoint vertex classes \(U(R)\), the unit group, and \(Z(R)^*=Z(R)\setminus\{0\}\), the nonzero zero divisors. A unit \(u\) and a nonzero zero divisor \(z\) are adjacent exactly when \(u+z\) is a zero divisor. It has \(M\) unit vertices and \(N\) nonzero-zero-divisor vertices. The graph uses addition to define edges and is not the traditional multiplicative zero-divisor graph. All multiplicities refer to eigenvalues over \(\mathbb C\) of the real symmetric adjacency matrix. The theorem assumes \(r\ge2\); for a field the graph is edgeless and its spectrum consists solely of zeros.

## Proof
**1. Product-field support description.** A vector \(u=(u_i)\) is a unit precisely when every \(u_i\ne0\). A nonzero zero divisor \(z\) has a nonempty proper set \(J=\{i:z_i\ne0\}\) of nonzero coordinates. Because a vector is a zero divisor exactly when some coordinate is zero, \(z\) is adjacent to \(u\) if and only if \(u_i=-z_i\) for at least one \(i\in J\). Consequently, if \(B\) is the \(N\)-by-\(M\) zero–one incidence matrix, its row indexed by \(z\) is
\[
B_{z,u}=1-\prod_{i\in J}(1-{\bf1}_{\{u_i=-z_i\}}).
\]

**2. Character diagonalization.** Regard the unit group as the finite abelian group \(G=\prod_i\mathbb F_{q_i}^{\times}\), of order \(M\). Multiplying both arguments of \(B\) coordinatewise by any unit leaves adjacency unchanged: \(B_{az,au}=B_{z,u}\). Therefore the unit-side Gram matrix \(H=B^{\mathsf T}B\) commutes with the regular action of \(G\), so the \(M\) complex characters \(\chi=\prod_i\chi_i\) of \(G\) are an orthogonal eigenbasis. Their squared norms as column vectors are \(M\). Define the character support \(T=\{i:\chi_i\text{ is nontrivial}\}\). For each prescribed \(T\), exactly \(w_T=\prod_{i\in T}(m_i-1)\) characters have this support (possibly zero characters if a factor is \(\mathbb F_2\)). Their shared Gram eigenvalue is
\[
\lambda_T=M^{-1}\sum_{z\in Z(R)^*}\left|\sum_{u\in G}B_{z,u}\chi(u)\right|^2.
\]
This formula follows by evaluating the Rayleigh quotient on the eigenvector \(\chi\); no numerical approximation is involved.

**3. Evaluating Fourier coefficients.** For a row of nonzero support \(J\), let \(C_z(\chi)=\sum_{u\in G}B_{z,u}\chi(u)\). If \(T=\varnothing\), the number of adjacent unit vertices gives
\[
C_z(1)=\Bigl(\prod_{i\notin J}m_i\Bigr)
\left[\prod_{i\in J}m_i-\prod_{i\in J}(m_i-1)\right].
\]
If \(T\ne\varnothing\) and \(T\not\subseteq J\), then \(C_z(\chi)=0\), because the row is independent of a coordinate on which \(\chi\) is nontrivial. If \(\varnothing\ne T\subseteq J\), expand the product of indicators in the row formula and sum each character in each coordinate. The cancellation \(\sum_{a\in\mathbb F_{q_i}^\times}\chi_i(a)=0\) for a nontrivial \(\chi_i\), and the fact that every character value has modulus one, give
\[
C_z(\chi)=(-1)^{|T|+1}
\Bigl(\prod_{i\notin J}m_i\Bigr)
\Bigl(\prod_{j\in J\setminus T}(m_j-1)\Bigr)
\prod_{i\in T}\chi_i(-z_i).
\]
The formula is valid even when some \(m_j=1\): the corresponding factor becomes zero as required.

**4. Summing over rows.** The number of rows with support exactly \(J\) is \(\prod_{i\in J}m_i\). For empty \(T\), inserting the expression from Step 3 in the normalized squared Fourier sum, using \(M=\prod_i m_i\), gives the stated sum for \(\lambda_\varnothing\). Expand its square and use the binomial product identity over subsets to obtain the alternative closed form displayed in Finding. For nonempty \(T\), the same substitution gives
\[
\lambda_T=\sum_{T\subseteq J\subsetneq[r]}
\Bigl(\prod_{i\notin J}m_i\Bigr)
\Bigl(\prod_{j\in J\setminus T}(m_j-1)^2\Bigr).
\]
For proper \(T\), evaluating this subset sum as a product over \([r]\setminus T\), minus the excluded term \(J=[r]\), yields exactly the claimed difference of products. For \(T=[r]\), no row support contains \(T\), hence \(\lambda_{[r]}=0\). The empty-support eigenvalue is positive: choose any singleton \(J\), for which its summand is positive. For every nonempty proper \(T\), the summand \(J=T\) is positive; thus \(\lambda_T>0\).

**5. Rank, nullity, and adjacency eigenvalues.** Every character of proper support contributes a strictly positive eigenvalue to \(H\), and precisely the \(w_{[r]}=F\) full-support characters contribute eigenvalue zero. Consequently \(\operatorname{rank}B=\operatorname{rank}H=M-F\). The symmetric adjacency matrix is
\[
A=\begin{pmatrix}0&B^{\mathsf T}\\ B&0\end{pmatrix}.
\]
The singular-value decomposition of \(B\) pairs each positive Gram eigenvalue \(\lambda\) with adjacency eigenvalues \(\sqrt\lambda\) and \(-\sqrt\lambda\), with matching multiplicities. Therefore the remaining \(M+N-2(M-F)=N-M+2F\) eigenvalues are zero, proving the characteristic polynomial and all multiplicities. In particular, the zero exponent is necessarily nonnegative.

## Verification
A standalone Python program `verify.py` constructs the graph directly from the coordinate equality rule, without constructing the character eigenvectors or using the theorem's rank to build the graph. It calculates \(B^{\mathsf T}B\) numerically, compares its entire spectrum with the predicted exact integer eigenvalues and multiplicities, checks the exact edge-count trace identity, and checks Gram rank. The program requires Python and NumPy. On 188 tested tuples of two, three, and four finite-field orders it completed with `SPECTRUM_VERIFY_OK 188 finite product sizes`. Labels for nonzero elements are arbitrary: in each field the map \(z_i\mapsto-z_i\) is a bijection, so the equality rule implemented in the verifier has precisely the same incidence matrix after permuting zero-divisor rows.

For example, \(R=\mathbb F_3^3\) has \(M=8\), \(N=18\), and \(F=1\). Its Gram eigenvalues are \(66\) once, \(8\) three times, \(2\) three times, and \(0\) once. Its graph adjacency eigenvalues are \(\pm\sqrt{66}\) once each, \(\pm\sqrt8\) three times each, \(\pm\sqrt2\) three times each, and zero twelve times. For two field factors \(\mathbb F_{q_1}\times\mathbb F_{q_2}\), the graph is the edge-incidence bipartite graph of a complete bipartite graph on \((m_1,m_2)\) vertices; its Gram eigenvalues simplify to \(m_1+m_2\), \(m_2\), \(m_1\), and zero with the multiplicities given by the character support formula. Finite verification corroborates, but does not substitute for, the all-parameter proof.

## Relationship to prior work
Mehry and Khasadan, *A Bipartite Graph Linking Units and Zero-Divisors*, arXiv:2511.07854v1 (first posted November 11, 2025), define this graph and explicitly pose determining its adjacency eigenvalues for finite reduced rings as Open Problem 1 of Section 8 (page 9). Their inspected preprint provides graph-theoretic properties, not this spectral factorization. The preprint's later version carries a September 2026 withdrawal/restructuring notice; the exact original graph definition and open question remain inspectable in v1. Prior spectral literature on the traditional zero-divisor graph, including Magi, Jose, and Kishore (2020) and Jain, Borse, and Barabde (2026), uses multiplicative adjacency \(xy=0\) between two nonzero zero divisors. Those graphs differ in both the vertex set and adjacency relation and their spectra do not yield the above additive zero-divisor–unit result merely by changing notation. Fourier diagonalization of abelian convolution matrices and the singular-value pairing for bipartite graphs are standard tools; the support-dependent coefficient and full closed spectrum are the contribution here.

## Limitations
The theorem applies to finite reduced commutative nonfields only: finite nonreduced rings have a different edge structure and are not covered. The field case is trivially edgeless. No claim is made about Laplacian, normalized Laplacian, or signless Laplacian spectra. Equality of a displayed eigenvalue for multiple different supports requires adding their stated multiplicities. The 188 tests are finite checks, not a proof of the infinite parameter family. A spectral formula equivalent to this result in less searchable literature cannot be absolutely ruled out, and the initiating 2025 preprint was subsequently withdrawn for revision; the stated priority assessment is qualified.

## References
1. Shahram Mehry and Ali Eisapoor Khasadan, *A Bipartite Graph Linking Units and Zero-Divisors*, arXiv:2511.07854v1, November 11, 2025; Section 2 (definition), Section 8 (spectral open problem). Original-version full text: https://pdfs.assets.alphaxiv.org/2511.07854v1.pdf ; version record: https://arxiv.org/abs/2511.07854 .
2. P. M. Magi, Sr. Magie Jose, and Anjaly Kishore, *Adjacency matrix and eigenvalues of the zero divisor graph \(\Gamma(\mathbb Z_n)\)*, Journal of Mathematics and Computer Science **10** (2020), 1285–1297, DOI:10.28919/jmcs/4590; graph defined by products equaling zero.
3. Sakshi Jain, Y. M. Borse, and R. Barabde, *On main eigenvalues of zero-divisor graphs of reduced rings*, arXiv:2604.26603 (April 29, 2026); spectrum of the different multiplicative zero-divisor graph.
