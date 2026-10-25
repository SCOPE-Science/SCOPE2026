# Complete generalized spectrum and inertia of GCD–LCM pencils on divisor lattices

## Finding

For every integer \(n\ge1\), let \(D(n)\) denote the set of its positive divisors. Index the real symmetric matrices \(G_n\) and \(L_n\) by \(d,e\in D(n)\), putting
\[
(G_n)_{d,e}=\gcd(d,e),\qquad (L_n)_{d,e}=\operatorname{lcm}(d,e).
\]
Write \(n=\prod_{i=1}^{r}p_i^{a_i}\), with distinct primes and positive integral exponents, and let \(\tau(n)=\prod_{i=1}^{r}(a_i+1)\). For every nonempty subset \(S\subseteq\{1,\ldots,r\}\), set
\[
m_S=\prod_{i\in S}p_i^{a_i},\qquad
c_S=2^{|S|-1}\prod_{i\notin S}(a_i-1),\qquad
c_\varnothing=\prod_{i=1}^{r}(a_i-1).
\]
Empty products have value one. For every complex parameter \(t\), the **full determinant polynomial** is
\[
\boxed{\det(G_n+tL_n)=\left(\prod_{d\mid n}\varphi(d)\right)
  \bigl(1+(-1)^r t\bigr)^{c_\varnothing}
  \prod_{\varnothing\ne S\subseteq\{1,\ldots,r\}}
     \bigl(1-m_St^2\bigr)^{c_S}.}
\]
Factors raised to exponent zero are understood as one. Equivalently, \(G_n^{-1}L_n\) is diagonalizable over \(\mathbb R\), and its multiset of eigenvalues consists of \((-1)^r\) with multiplicity \(c_\varnothing\), and for each nonempty \(S\), both \(\sqrt{m_S}\) and \(-\sqrt{m_S}\) with multiplicity \(c_S\) apiece.

In particular, \(G_n+L_n\) is singular **if and only if** \(r\) is odd and all \(a_i\ge2\). If singular, its nullity is exactly \(c_\varnothing\). More generally the exact inertia \((i_+,i_-,i_0)\) of \(G_n+L_n\) is
\[
\boxed{(i_+,i_-,i_0)=
\begin{cases}
((\tau(n)+c_\varnothing)/2,\ (\tau(n)-c_\varnothing)/2,\ 0),& r\text{ even},\\
((\tau(n)-c_\varnothing)/2,\ (\tau(n)-c_\varnothing)/2,\ c_\varnothing),& r\text{ odd}.
\end{cases}}
\]
For \(n=1\), these formulas mean \(r=0\), \(G_1+L_1=[2]\), and inertia \((1,0,0)\).

## Assumptions and scope

All integers \(n\) are positive, all \(a_i\) are positive, and \(t\) is arbitrary complex in the determinant identity; the eigenvalue and inertia assertions concern the corresponding real matrices. The index set is the **complete divisor lattice** \(D(n)\), not the initial integer interval \(\{1,\ldots,n\}\), and not the unitary divisors alone. Matrix index ordering does not affect the assertions.

## Proof

**1. Prime-power chain.** Fix a prime \(p\) and \(a\ge1\). Index rows and columns by \(j=0,\ldots,a\), and write \(G_{jk}=p^{\min(j,k)}\), \(L_{jk}=p^{\max(j,k)}\). The identity
\[
p^{\min(j,k)}+p^{\max(j,k)}=p^j+p^k
\]
gives \(G+L=uv^{\mathsf T}+vu^{\mathsf T}\), where \(u=(1,p,\ldots,p^a)^{\mathsf T}\) and \(v=(1,\ldots,1)^{\mathsf T}\). The first and last columns of \(G\) are respectively \(v\) and \(u\). For standard basis vectors \(e_0,e_a\), therefore,
\[
T:=G^{-1}L=-I+e_a v^{\mathsf T}+e_0u^{\mathsf T}.
\]
The inverse exists: \(G\) is positive definite by the factorization in step 3. The subspace \(W=\ker(v^{\mathsf T})\cap\ker(u^{\mathsf T})\) has dimension \(a-1\), since \(v,u\) are independent. On \(W\), \(T=-I\). Furthermore \(Te_0=e_a\) and \(Te_a=p^a e_0\), so \(\operatorname{span}(e_0,e_a)\) is invariant, complementary to \(W\), and carries matrix
\[
\begin{pmatrix}0&p^a\\1&0\end{pmatrix}.
\]
Its eigenvalues are \(\pm p^{a/2}\), which are distinct and are not \(-1\). Consequently \(T\) is diagonalizable and its complete spectrum is \(\{-1\text{ (multiplicity }a-1),\ +p^{a/2},\ -p^{a/2}\}\). For \(a=1\), \(W\) is zero-dimensional, as required.

**2. Multiplicative product lattice.** Coordinatewise exponent indexing \(d=\prod_i p_i^{j_i}\) identifies \(D(n)\) with \(\prod_i\{0,\ldots,a_i\}\). Since gcd and lcm are multiplicative across distinct primes,
\[
G_n=\bigotimes_{i=1}^{r}G_{p_i,a_i},\qquad
L_n=\bigotimes_{i=1}^{r}L_{p_i,a_i},\qquad
G_n^{-1}L_n=\bigotimes_{i=1}^{r}T_{p_i,a_i}.
\]
A tensor eigenvector chooses from each factor either the \((-1)\)-eigenspace of dimension \(a_i-1\) or one of the two one-dimensional eigenspaces with eigenvalues \(\pm p_i^{a_i/2}\). If precisely the coordinates in a nonempty subset \(S\) take the latter choices, the \(2^{|S|}\) sign selections split equally between \(+\sqrt{m_S}\) and \(-\sqrt{m_S}\), each with multiplicity \(c_S\). If no coordinate takes a nontrivial choice, the eigenvalue is \((-1)^r\), with multiplicity \(c_\varnothing\). The eigenvectors form a full basis, since every local eigenbasis does. In particular,
\[
2\sum_{S\ne\varnothing}c_S+c_\varnothing
 =\prod_i\bigl((a_i-1)+2\bigr)=\tau(n),
\]
which also checks dimension. Distinct nonempty subsets yield distinct integers \(m_S>1\), so no accidental coincidences affect the multiplicities.

**3. Determinant normalization.** The elementary identity \(\sum_{k\mid m}\varphi(k)=m\) gives
\[
\gcd(d,e)=\sum_{c\mid d,\,c\mid e}\varphi(c).
\]
Let \(Z_{d,c}=\mathbf1_{c\mid d}\) for \(d,c\mid n\). Ordering divisors compatibly with divisibility makes \(Z\) unit lower triangular. Thus \(G_n=Z\operatorname{diag}(\varphi(c))Z^{\mathsf T}\) is positive definite, with
\[
\det G_n=\prod_{d\mid n}\varphi(d).
\]
The polynomial factors now follow from \(\det(G_n+tL_n)=\det G_n\det(I+tG_n^{-1}L_n)\) and the spectrum in step 2. For the empty prime factorization \(n=1\), this identity reduces directly to \(1+t\).

**4. Singular locus and inertia.** At \(t=1\), every factor \(1-m_S\) is nonzero, as \(m_S>1\). The only possible zero is \(1+(-1)^r\), with multiplicity \(c_\varnothing\). Thus singularity occurs exactly for odd \(r\) with all \(a_i\ge2\); its nullity is \(c_\varnothing\). Since \(G_n\) is positive definite, the inertia of \(G_n+L_n\) equals that of \(I+G_n^{-1/2}L_nG_n^{-1/2}\), whose eigenvalues are \(1+\lambda\) for the generalized eigenvalues \(\lambda\) above. Every nonempty \(S\) yields one positive and one negative contribution, each with multiplicity \(c_S\). The empty-set contribution is positive for even \(r\) and zero for odd \(r\). The asserted inertia formulas follow.

## Verification

A standalone exact-integer checker is provided as `verify_gcd_lcm_sum.py`, with pinned `requirements.txt`. It independently constructs gcd and lcm matrices from their numerical entries and compares their exact determinants against the formula, including symbolic polynomial checks. Its output on SymPy 1.14.0 was:

```
VERIFY_OK: 241 independent exact t=1 determinants; 272 additional integer pencil determinants; 14 exact symbolic characteristic polynomials
```

Examples: \(n=4\) gives singular nullity one, \(n=36\) has inertia \((5,4,0)\), and \(n=900\) has inertia \((13,13,1)\). Finite calculations are checks, not proofs for arbitrary \(n\); the proof above supplies that scope.

## Relationship to prior work

The positive-definiteness and determinant of the GCD matrix on a factor-closed set are classical and are described by Ovall (2004). The spectral theorem **on a single prime-power divisor chain**, with generalized eigenvalues \(\pm p^{a/2}\) and \(-1\), is **already explicitly stated in Section 4.2** of Merikoski, Haukkanen, Sasaki and Tossavainen (2025). Their broader work treats initial intervals and selected other sets, not the complete multi-prime divisor lattice. The claimed new result is specifically the full simultaneous tensor-product spectrum, the multiplicities for *every* prime subset, the determinant pencil for arbitrary \(n\), and the resulting exact rank and inertia classification for the sum. Factor-closed GCD/LCM matrix divisibility is also known and is not claimed as new. A tensorization of an already known prime-power theorem is a significant scope and originality limitation; an equivalent formulation in less readily indexed work has not been excluded definitively.

## Limitations

These statements hold only for the **complete** divisor lattice. Removing even one divisor generally destroys the Kronecker structure, so no corresponding classification is asserted for arbitrary GCD-closed sets or initial intervals. The proof does not address ordinary eigenvalues of \(L_n\) or \(G_n\) separately. The nearest prime-power spectrum was already published; no publication-priority guarantee for the complete product-lattice formulation is asserted.

## References

1. J. S. Ovall, “An analysis of GCD and LCM matrices via the LDLT-factorization,” *Electronic Journal of Linear Algebra* **11** (2004), 51–58, DOI: 10.13001/1081-3810.1121. Full text: https://journals.uwyo.edu/index.php/ela/article/download/243/243/243.
2. J. K. Merikoski, P. Haukkanen, A. Sasaki and T. Tossavainen, “On Generalized Eigenvalues of MAX Matrices to MIN Matrices and LCM Matrices to GCD Matrices,” *Journal of Integer Sequences* **28** (2025), Article 25.7.1, especially Section 4.2. Full text: https://cs.uwaterloo.ca/journals/JIS/VOL28/Tossavainen/tossa12.pdf.
3. P. Gatephan and K. Rodtes, “Divisibility of LCM matrices by totally nonnegative GCD matrices,” *Linear Algebra and its Applications* **619** (2021), 146–159, DOI: 10.1016/j.laa.2021.02.020.
4. On the positive definiteness and eigenvalues of meet and join matrices, *Discrete Mathematics* (2014), DOI: 10.1016/j.disc.2014.02.018 (abstract and introductory background consulted).
