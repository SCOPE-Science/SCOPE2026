# Paired-Lagrangian Smith forms and composite-qudit entanglement on binary symplectic graphs

## Finding

Let \(m\ge2\), let \(V=\mathbb F_2^{2m}\) carry a nondegenerate alternating form \(\beta\), and let \(G\) be the graph on \(V\setminus\{0\}\) with distinct vertices adjacent exactly when \(\beta(x,y)=1\). Choose any complementary maximal totally isotropic subspaces \(U,W\) (so \(V=U\oplus W\)) and bipartition the vertex set into \(A=(U\setminus\{0\})\cup(W\setminus\{0\})\) and its complement \(B\). Put \(n=2^m-1\), so \(|A|=2n\), \(|B|=n^2\).

Let \(C\) be the integer \(2n\times n^2\) adjacency matrix across this cut. Its **complete nonzero Smith normal form** is
\[
\operatorname{SNF}(C)_{\ne0}
=\operatorname{diag}\Bigl(
\bigl(2^j\bigr)^{\times\left(2\binom m{j+1}-\mathbf 1_{\{j=m-1\}}\right)}
:0\le j\le m-1\Bigr),
\]
with \(\operatorname{rank}_{\mathbb Q}C=2n-1\). Here the exponent \(\times r\) denotes multiplicity \(r\), not ordinary exponentiation, and Smith factors are listed in increasing order.

For **every integer local dimension \(D\ge2\)**, prepare the pure, unit-edge-weight \(D\)-level graph state on \(G\) using controlled phase \(\exp(2\pi i xy/D)\). Its reduction to \(A\) has precisely \(R_{m,D}\) nonzero eigenvalues, all equal to \(1/R_{m,D}\), where
\[
R_{m,D}=
\frac{\gcd(D,2^{m-1})}{D}
\left[\prod_{j=0}^{m-1}
\left(\frac{D}{\gcd(D,2^j)}\right)^{\binom m{j+1}}
\right]^2.
\]
Thus every positive-order Rényi entropy and the von Neumann entropy equal \(\log_D R_{m,D}\) in base-\(D\) units. In particular, for every odd \(D\), \(R_{m,D}=D^{2n-1}\), exactly one unit below maximal entropy \(2n\), while for \(D=2\), \(R_{m,2}=2^{2m}\) and the entropy equals \(2m\) bits. This dyadic/non-dyadic contrast holds throughout the infinite family.

## Assumptions and scope

The binary alternating space and its symplectic graph are fixed independently of the choice of qudit local dimension. A binary maximal isotropic subspace gives a commuting context in the underlying **binary** Pauli geometry; using \(D>2\) does not identify it with the Pauli geometry of a \(D\)-level system. All edge weights in the graph state are one, including at composite \(D\); the state is pure. Only the cut consisting of two complementary binary Lagrangian contexts is asserted. A symplectic change of basis takes any such ordered pair to the standard pair and preserves the graph and cut spectrum.

## Proof

**1. Identify the cross matrix.** In coordinates \(V=U\oplus W\), the alternating form is \(\beta((a,b),(a',b'))=a\cdot b'+a'\cdot b\pmod2\). List nonzero binary \(m\)-vectors using \(1,\ldots,n\), and introduce the integer matrix \(H\) with \(H_{xy}=x\cdot y\pmod2\) represented in \(\{0,1\}\). Rows of \(C\) are indexed first by \((x,0)\), then by \((0,y)\), and columns by \((a,b)\) with both components nonzero. Hence
\[
 C_{(x,0),(a,b)}=H_{xb},\qquad
 C_{(0,y),(a,b)}=H_{ya}.
\]
Consequently the image of \(C^\top\) over \(\mathbb Z/D\mathbb Z\) consists of all matrices \((u_b+v_a)_{a,b}\) with \(u,v\in I_D=\operatorname{im}(H\bmod D)\).

**2. Recall and reconstruct the single-context integral structure.** Let \(Z_{xT}=\mathbf1_{\{T\subseteq\operatorname{supp}(x)\}}\) for nonempty subsets \(T\subseteq[m]\), with rows and columns ordered by their binary indicator masks. The Boolean-lattice zeta matrix \(Z\) is unimodular: after ordering by cardinality it is triangular with diagonal ones. The parity expansion
\[
 \mathbf1_{\{r\text{ odd}\}}=\sum_{j=1}^{r}\binom rj(-2)^{j-1}
\]
gives the integral identity
\[
 H=Z\operatorname{diag}_{\varnothing\ne T\subseteq[m]}
 \left((-2)^{|T|-1}\right)Z^\top.
\]
Thus \(H\) has Smith factors \(2^j\), with multiplicities \(\binom m{j+1}\). This is the known Sylvester–Hadamard design incidence Smith form, included explicitly in Hacıoğlu's 2013 theorem and **not claimed as a new result**. It gives
\[
 |I_D|=\prod_{j=0}^{m-1}
 \left(D/\gcd(D,2^j)\right)^{\binom m{j+1}}.
\]

**3. Identify the additional, paired-context compatibility constraint.** The map \(I_D\times I_D\to(\mathbb Z/D\mathbb Z)^{n\times n}\), \((u,v)\mapsto(u_b+v_a)\), has kernel exactly the pairs \((c\mathbf1,-c\mathbf1)\) with \(c\mathbf1\in I_D\). Therefore \(|\operatorname{im}C^\top|=|I_D|^2/|I_D\cap\langle\mathbf1\rangle|\). Since \(H\mathbf1=2^{m-1}\mathbf1\) and \(H^2=2^{m-2}(I+J)\) (where \(J\) is the all-ones matrix),
\[
 H(2H-J)=2^{m-1}I,\qquad (2H-J)\mathbf1=\mathbf1.
\]
If \(Hz\equiv c\mathbf1\pmod D\), multiplication by the integral matrix \(2H-J\) shows \(2^{m-1}z\equiv c\mathbf1\pmod D\), forcing \(\gcd(D,2^{m-1})\mid c\). Conversely, if this divisibility holds, choose \(t\) with \(2^{m-1}t\equiv c\pmod D\) and take \(z=t\mathbf1\). Hence
\[
 |I_D\cap\langle\mathbf1\rangle|=D/\gcd(D,2^{m-1}).
\]
Inserting this into the previous image formula proves the exact displayed expression for \(R_{m,D}\) for every positive integer modulus \(D\).

**4. Deduce the new rectangular Smith form.** Over \(\mathbb Q\), \(H\) is invertible and the only pairs \((u,v)\) giving the zero sum-matrix are \((c\mathbf1,-c\mathbf1)\). Thus \(C\) has rational rank \(2n-1\). The already-proved formula \(|\operatorname{im}(C\bmod D)|=R_{m,D}\), valid simultaneously for all \(D\), uniquely determines its integral invariant factors. Indeed the suggested diagonal list has precisely this image size, because its multiplicities are twice those of \(H\) except for one missing \(2^{m-1}\) factor. For odd moduli, all factors are units; for dyadic prime-power moduli the cumulative valuations determine the powers of two; no odd prime may divide a factor. This establishes the Smith form including its single zero row.

**5. Establish the full quantum spectrum.** Write the graph-state computational basis amplitudes as \(D^{-|V\setminus\{0\}|/2}\omega^{\Phi(z)}\), where \(\omega=\exp(2\pi i/D)\) and \(\Phi\) is the quadratic edge-phase function. Tracing out \(B\) gives
\[
(\rho_A)_{a,a'}=D^{-|A|}
\omega^{\Phi_A(a)-\Phi_A(a')}
\mathbf1_{\{C^\top(a-a')\equiv0\pmod D\}}.
\]
Conjugating by the diagonal local phase unitary removes \(\Phi_A\). Each coset of \(K=\ker(C^\top\bmod D)\) yields one rank-one constant block, with eigenvalue \(|K|/D^{|A|}\). There are \(D^{|A|}/|K|=|\operatorname{im}C^\top|=R_{m,D}\) such cosets, proving the complete flat nonzero spectrum and every entropy statement. No primality of \(D\) is used.

## Verification

The accompanying `verify.py` builds the actual binary symplectic cut matrices and checks integer Smith forms for \(m=2,3\), the zeta factorization through \(m=6\), exact modular image counts for several even, odd and composite local dimensions, and a direct normalized Hilbert-space partial trace of the fifteen-qubit \(m=2,D=2\) state. The exact program ran successfully and printed `VERIFY_OK checks=32`. Its tests are finite consistency checks; the preceding derivation establishes the unbounded theorem.

For example, at \(m=2\), \(C\) has Smith factors \(1,1,1,1,2\) and rank five; for \(D=2,3,4,6\), its Schmidt ranks are respectively \(16,243,512,3888\). At \(m=3\), its nonzero Smith factors are six ones, six twos and one four, giving qubit Schmidt rank \(64\) versus \(3^{13}\) for qutrits.

## Relationship to prior work

Planat–Saniga describe the binary Pauli commutation geometry and maximal isotropic contexts; Abiad–Haemers define and study the same binary symplectic graph's global binary adjacency rank. Looi–Yu–Gheorghiu–Griffiths define graph states in arbitrary local dimension; Hein–Eisert–Briegel and Helwig describe general graph-state entanglement/cut-rank principles, with Helwig's main full-rank criterion in prime dimension. Hacıoğlu already computed the full integral Smith form of the Sylvester–Hadamard design incidence matrix \(H\). The distinct statement proved here is the **paired-context rectangular cross-matrix Smith form**, in which the compatibility of constant vectors deletes exactly one top invariant factor, together with the composite-dimensional quantum spectrum of the corresponding natural cut. The known single-context Smith form by itself does not state the two-context rank; its role as a prerequisite is explicitly credited.

## Limitations

The result does not describe arbitrary vertex partitions, nontransverse Lagrangian pairs, nonuniform edge weights, mixed states, or the symplectic graph over an odd-characteristic field. It is not a universal local-unitary classification or a thermodynamic statement. The algebra is independently reproducible, but neither historical priority nor the scientific result has undergone an independent external audit; a specialized earlier theorem on paired incidence matrices could still imply the claim.

## References

1. M. Planat and M. Saniga, *On the Pauli graphs of N-qudits*, arXiv:quant-ph/0701211 (first public 2007-01-29), https://arxiv.org/abs/quant-ph/0701211.
2. S. Y. Looi, L. Yu, V. Gheorghiu and R. B. Griffiths, *Quantum-error-correcting codes using qudit graph states*, arXiv:0712.1979, https://arxiv.org/abs/0712.1979.
3. İ. Hacıoğlu, *Derived and residual Sylvester-Hadamard designs and the Smith normal form*, Turkish Journal of Mathematics 37 (2013), 398–403, DOI:10.3906/mat-1112-18, https://doi.org/10.3906/mat-1112-18.
4. A. Abiad and W. H. Haemers, *Switched symplectic graphs and their 2-ranks*, arXiv:1412.2945, https://arxiv.org/abs/1412.2945.
5. W. Helwig, *Absolutely maximally entangled qudit graph states*, arXiv:1306.2879, https://arxiv.org/abs/1306.2879.
6. M. Hein, J. Eisert and H. J. Briegel, *Multiparty entanglement in graph states*, arXiv:quant-ph/0307130, https://arxiv.org/abs/quant-ph/0307130.
