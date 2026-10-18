# Complete adjacency spectrum of the bipartite zero-divisor–unit graph of finite reduced rings

## Finding
Let \(R=\prod_{i=1}^{r}\mathbb F_{q_i}\) with \(r\ge 2\), where each \(q_i\) is a prime power. The bipartite zero-divisor–unit graph \(\mathcal B(R)\) has vertices the nonzero zero-divisors and the units of \(R\), and an edge \(z\sim u\) exactly when \(z+u\) is a zero-divisor.

Put \(m_i=q_i-1\), \(b_i=q_i-2\), \(c_i=m_i+b_i^2\), \(Q=\prod_iq_i\), \(M=\prod_im_i\), \(B=\prod_ib_i\), and \(C=\prod_ic_i\). Define, for each subset \(T\subseteq[r]\), the nonnegative integer
\[
\lambda_T=\begin{cases}
MQ-3M^2+2MB+C-B^2,&T=\varnothing,\\
\displaystyle\prod_{i\notin T}c_i-\prod_{i\notin T}b_i^2,&T\ne\varnothing.
\end{cases}
\]
Then \(\lambda_T>0\) for every proper subset \(T\subsetneq[r]\), \(\lambda_{[r]}=0\), and the complete adjacency characteristic polynomial is
\[
\boxed{\det(tI-A_{\mathcal B(R)})
=t^{\,Q-1-2(M-B)}
\prod_{T\subsetneq[r]}
(t^2-\lambda_T)^{\prod_{i\in T}b_i}.}
\]
A factor with exponent zero is omitted; coincident eigenvalues have their multiplicities added. Equivalently, the nonzero adjacency spectrum consists of \(\pm\sqrt{\lambda_T}\), each with multiplicity \(\prod_{i\in T}b_i\), for all proper subsets \(T\subsetneq[r]\). Thus the full adjacency nullity is
\[
\boxed{Q-1-2M+2B},
\]
and the rank of the zero-divisor-by-unit incidence matrix is exactly \(M-B\).

For a single finite field \(r=1\), the graph has \(q_1-1\) isolated vertices and only the zero eigenvalue; this boundary is excluded from the displayed formula.

As a check on the boundary, when \(r=2\) the graph is the edge-subdivision of the complete bipartite graph \(K_{q_1-1,q_2-1}\). The formula specializes to the classical signless-Laplacian subdivision spectrum. The all-factor result, including \(r\ge3\), is not a consequence of that two-factor observation.

## Assumptions and scope
All fields are finite, and no assumption is made that the field orders or characteristics agree. The adjacency matrix is the real symmetric, unweighted matrix of the simple bipartite graph. The zero-divisor vertex class omits zero, and the unit class includes all units. We count \(0\) as a zero-divisor in the condition \(z+u\in Z(R)\), although it cannot occur as a sum of a zero-divisor and a unit in this finite product-of-fields setting. Products over an empty index set equal one. Graph eigenvalues are counted with algebraic multiplicity.

## Proof
**Step 1: Incidence rows.** Write \(G=R^\times=\prod_i\mathbb F_{q_i}^\times\), so \(|G|=M\). A nonzero zero-divisor \(z\) has a unique nonempty proper support \(S=\{i:z_i\ne0\}\subsetneq[r]\). For each such \(z\), its incidence row, considered as a function on \(G\), is
\[
f_z(u)=1-\prod_{i\in S}(1-\mathbf 1_{\{u_i=-z_i\}}).
\]
There are \(\prod_{i\in S}m_i\) rows with support \(S\). The incidence matrix \(H=(f_z(u))\) has \(Q-1-M\) rows and \(M\) columns. The full graph adjacency matrix has block form \(\left(\begin{smallmatrix}0&H\\H^\top&0\end{smallmatrix}\right)\), with exactly \(Q-1\) vertices.

**Step 2: Multiplicative characters diagonalize the Gram matrix.** For \(g\in G\), simultaneous coordinate multiplication preserves the edge predicate: \(f_{gz}(gu)=f_z(u)\). Consequently \(H^\top H\) commutes with the right regular action of \(G\). The characters \(\chi=\prod_i\chi_i\) are therefore eigenvectors. If \(T=\{i:\chi_i\ne1\}\), the eigenvalue is
\[
\lambda_\chi=\frac1M\sum_z\left|\sum_{u\in G}f_z(u)\overline{\chi(u)}\right|^2.
\]
The number of characters with prescribed nontrivial-coordinate set \(T\) is \(\prod_{i\in T}(m_i-1)=\prod_{i\in T}b_i\).

**Step 3: Nontrivial characters.** Suppose \(T\ne\varnothing\). For a row with support \(S\), the Fourier sum in Step 2 vanishes if \(T\not\subseteq S\). Otherwise, the constant term of \(f_z\) has zero transform, and the negative product term has squared Fourier magnitude
\[
\left(\prod_{i\notin S}m_i^2\right)
\left(\prod_{i\in S\setminus T}b_i^2\right).
\]
Indeed, summing \(1-\mathbf 1_{\{u_i=-z_i\}}\) against the trivial character gives \(b_i\), whereas summing against a nontrivial character gives a number of modulus one. Multiplying the displayed square by the \(\prod_{i\in S}m_i\) rows and dividing by \(M\) gives
\[
\lambda_T=\sum_{T\subseteq S\subsetneq[r]}
\left(\prod_{i\notin S}m_i\right)
\left(\prod_{i\in S\setminus T}b_i^2\right).
\]
Choosing independently whether each coordinate outside \(T\) belongs to \(S\), then deleting the forbidden full support \(S=[r]\), produces
\[
\lambda_T=\prod_{i\notin T}(m_i+b_i^2)-\prod_{i\notin T}b_i^2.
\]
This remains valid for \(T=[r]\), giving zero.

**Step 4: Trivial character.** For support \(S\) the row sum is
\[
D_S=M-\left(\prod_{i\notin S}m_i\right)
\left(\prod_{i\in S}b_i\right).
\]
Consequently
\[
\lambda_\varnothing=\frac1M
\sum_{\varnothing\ne S\subsetneq[r]}
\left(\prod_{i\in S}m_i\right)D_S^2.
\]
Expansion by the finite product identity \(\sum_{S\subseteq[r]}\prod_{i\in S}a_i=\prod_i(1+a_i)\), omitting the empty and full supports, yields exactly \(MQ-3M^2+2MB+C-B^2\). Since \(r\ge2\), at least one incidence row has positive degree, so \(\lambda_\varnothing>0\).

**Step 5: Rank and full spectrum.** For every nonempty proper \(T\), the complement \([r]\setminus T\) is nonempty and all \(m_i>0\), so \(\prod_{i\notin T}(b_i^2+m_i)>\prod_{i\notin T}b_i^2\). Hence every proper-subset eigenvalue is positive and the full-set eigenvalue is zero. The sum of the character multiplicities over proper subsets equals
\[
\prod_i(1+b_i)-\prod_i b_i=M-B.
\]
Thus \(\operatorname{rank}(H)=M-B\). Singular-value symmetry of the bipartite block matrix contributes paired eigenvalues \(\pm\sqrt{\lambda_T}\) and \((Q-1)-2(M-B)\) zero eigenvalues. This proves the characteristic polynomial and all multiplicities. \(\square\)

## Verification
The self-contained Python program `check_spectrum.py` independently forms the incidence matrix, computes its integer Gram matrix, obtains the complete characteristic polynomial from Newton identities in exact integer arithmetic, and compares it with the formula above. It also directly checks coordinatewise addition in products of prime fields. Tested field-order tuples are \((2,2)\), \((2,3)\), \((3,3)\), \((2,5)\), \((3,5)\), \((2,2,2)\), \((2,3,3)\), \((3,3,3)\), \((2,3,4)\), \((2,2,2,2)\), \((2,2,3,3)\), \((2,4,5)\), and \((4,4,4)\). All thirteen exact comparisons succeeded with the final `VERIFY_OK` message. Use `python3 check_spectrum.py` from the extracted package directory; Python's standard library is the only dependency. Finite computations test the formula but are not used to infer the arbitrary-parameter theorem.

## Relationship to prior work
Mehry and Eisapoor Khasadan introduced this zero-divisor–unit bipartite graph, with the same vertex and adjacency conventions, in arXiv:2511.07854v1 (2025). Their Section 8 explicitly asks for its adjacency spectrum over finite reduced rings. Sections 2–7 study other graph properties but do not give a spectrum formula. The later revision carries a withdrawal/restructuring notice, so the original formulation is identified by its v1 identifier rather than represented as a currently endorsed theorem. The present result settles that explicitly stated spectral question for arbitrary finite products of finite fields and in particular determines nullity and incidence rank.

Spectra computed by Masalkar, Khairnar, Lande, and Patil for standard zero-divisor graphs (arXiv:2106.15977v2) concern the different relation \(xy=0\) between zero-divisors, not sums \(z+u\) between zero-divisors and units. Spectral character arguments used by Demiroğlu Karabulut and Espinosa for unit Cayley graphs on matrix rings (arXiv:2605.05457v2) concern the relation that a difference of two arbitrary matrices is invertible. Neither statement entails the specific Gram spectrum here.

## Limitations
The theorem addresses finite reduced commutative rings, not finite rings with nilpotents or infinite rings. It concerns adjacency spectra, not Laplacian spectra. Character labels with the same eigenvalue must be merged to obtain distinct-value counts. The cited source's revision/withdrawal means the historical open-problem wording should be checked against any future replacement publication; possible equivalent formulations in algebraic graph theory remain a bibliographic uncertainty. No independent external mathematical audit is claimed.

## References
1. S. Mehry and A. Eisapoor Khasadan, *A Bipartite Graph Linking Units and Zero-Divisors*, arXiv:2511.07854v1 (first public 2025-11-11), Sections 2–3 and 8. https://arxiv.org/html/2511.07854v1
2. K. D. Masalkar, A. S. Khairnar, A. M. Lande, and A. A. Patil, *Spectra of the zero-divisor graph of finite rings*, arXiv:2106.15977v2 (2022). https://arxiv.org/abs/2106.15977
3. Y. Demiroğlu Karabulut and H. Espinosa, *Spectrum of the Unit-Graph on* \(\mathrm{Mat}_3(\mathbb F_q)\), arXiv:2605.05457v2 (2026). https://arxiv.org/abs/2605.05457
4. MSC2020, 13A70: general commutative ring theory and combinatorics, including zero-divisor graphs. https://mathscinet.ams.org/msc/msc2020.html
