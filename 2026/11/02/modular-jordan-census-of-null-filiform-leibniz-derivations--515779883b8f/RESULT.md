# Modular Jordan census of null-filiform Leibniz derivations

## Finding

Let \(n\ge 2\), let \(p\) be prime, and let \(k=\mathbb F_q\), where \(q=p^e\) with \(e\ge1\). Define the **right null-filiform Leibniz algebra** \(L_n(k)\) with ordered basis \(e_1,\ldots,e_n\) and multiplication
\[
[e_i,e_1]=e_{i+1}\quad(1\le i<n),
\qquad [e_i,e_j]=0\quad(j\ne1),
\]
with out-of-range basis elements zero. All statements below concern ordinary \(k\)-linear derivations \(D([x,y])=[D(x),y]+[x,D(y)]\), not local derivations or Leibniz algebra automorphisms.

For integers \(\ell\ge1\), \(d\ge1\), write \(\mathcal P(\ell,d)\) for the partition obtained by sorting the \(\min(\ell,d)\) positive integers
\[
\left\lfloor\frac{\ell-1-j}{d}\right\rfloor+1,
\quad 0\le j<\min(\ell,d).
\]
It is the nilpotent Jordan block partition of a length-\(\ell\) shift raised to its \(d\)-th power. Put \(s=\lfloor(n-1)/p\rfloor\) and \(m_c=\#\{j:1\le j\le n,\ j\equiv c\pmod p\}\) for \(c\in\{0,\ldots,p-1\}\).

**Complete Jordan-type census.** Every derivation is uniquely parameterized by \((a_1,\ldots,a_n)\in k^n\). The Jordan types, including their eigenvalues and numbers of derivations, are as follows.

1. If \(a_1=0\), there is one zero derivation, with \(n\) one-dimensional blocks of eigenvalue zero. For each \(1\le d<n\), exactly
\[
(q-1)q^{n-d-1}
\]
derivations have only eigenvalue zero and have Jordan partition \(\mathcal P(n,d)\).

2. Fix **any particular** \(a_1=u\in k^\times\). For each \(1\le r\le s\), exactly
\[
(q-1)q^{n-r-1}
\]
derivations have, for every residue \(c\) with \(m_c>0\), eigenvalue \(cu\) with Jordan block partition \(\mathcal P(m_c,r)\). The remaining
\[
q^{n-s-1}
\]
derivations (label \(r=s+1\)) have the same description with \(r=s+1\); in particular they are diagonalizable. The counts are **conditional on the specified value** of \(a_1=u\); distinct values of \(u\) can occasionally define the same unconstrained matrix-similarity class, and should not be counted as different Jordan types merely by their labels.

These formulas give every Jordan-type multiplicity over every prime-power field, including characteristic two and all extension fields. The integer \(r\) is the first nonzero coefficient at a \(p\)-divisible degree in the normalized Toeplitz polynomial; the final label means that all such coefficients vanish. For fixed \(u\), its labels yield distinct Jordan types.

**Rank distribution and invertibility boundary.** Let \(m=\lfloor n/p\rfloor\), and let \(\nu(D)=\dim_k\ker D\). For the derivations with \(a_1=0\), the nullity counts are \((q-1)q^{n-r-1}\) for \(1\le r<n\), plus one derivation of nullity \(n\). For those with \(a_1\ne0\):
\[
\#\{D:a_1\ne0,\ \nu(D)=r\}=
\begin{cases}
(q-1)q^{n-1},&m=0,\ r=0,\\
(q-1)^2q^{n-r-1},&m\ge1,\ 1\le r<m,\\
(q-1)q^{n-m},&m\ge1,\ r=m,\\
0,&\text{otherwise}.
\end{cases}
\]
The rank is \(n-\nu(D)\); adding the two disjoint populations gives each exact rank multiplicity. An invertible derivation exists **if and only if** \(p>n\). When \(p\le n\), every derivation is singular, although many are not nilpotent.

## Assumptions and scope

All formulas require \(n\ge2\), \(q=p^e\) with \(p\) prime and \(e\ge1\), and the explicitly defined multiplication table. No assumption on algebraic closedness, primality of \(q\), or characteristic larger than the dimension is made. Every eigenvalue appearing in the formulas lies in \(k\), so the Jordan types are defined over the given finite field. The proof works over arbitrary fields of characteristic \(p\) for the structural Jordan classification; finite cardinality is needed only for the multiplicities.

This is a census of **labelled derivation maps**. It does not classify derivations modulo Leibniz-algebra automorphism conjugation or classify all algebras with the same nilpotency profile.

## Proof

**1. Derivation matrices, without a characteristic restriction.** Let \(N\) be the nilpotent shift \(N(e_j)=e_{j+1}\) for \(j<n\), and \(N(e_n)=0\). Let \(H(e_j)=j e_j\), with integers interpreted in \(k\). A derivation is determined by \(D(e_1)=\sum_{i=1}^n a_i e_i\). Applying the derivation identity to \([e_j,e_1]=e_{j+1}\) inductively gives
\[
D(e_j)=j a_1e_j+\sum_{r=1}^{n-j}a_{r+1}e_{j+r},
\qquad
D=a_1H+f(N),\quad f(t)=\sum_{r=1}^{n-1}a_{r+1}t^r.
\]
Conversely these maps satisfy the derivation identity for every basis product: the displayed recurrence handles products with second argument \(e_1\), and all products with a different second argument remain zero since \(D(e_j)\) has no \(e_1\)-coefficient for \(j\ge2\). Thus this is a bijective \(n\)-parameter description in every characteristic.

**2. The nilpotent branch.** If \(a_1=0\) and \(f\ne0\), let \(d\) be the least degree of a nonzero coefficient in \(f\). Then \(f(N)=N^d h(N)\), where \(h(0)\ne0\) and \(h(N)\) is invertible and commutes with \(N\). Consequently, for each \(j\ge1\),
\[
\dim\ker(f(N)^j)=\dim\ker(N^{dj})=\min(n,dj).
\]
These nullities determine the Jordan partition \(\mathcal P(n,d)\). Its coefficient count is \((q-1)q^{n-1-d}\). If \(f=0\), the map vanishes, giving the remaining one case.

**3. Resonance-normalizing similarity.** Suppose \(a_1=u\ne0\). The fundamental commutator is \([H,N^j]=jN^j\). Let \(g(t)=1+\sum_{j=1}^{n-1}b_jt^j\), and let \(U=g(N)\), which is invertible. Direct multiplication gives
\[
U^{-1}DU=uH+\Bigl(f(t)+u\,g(t)^{-1}t g'(t)\Bigr)\big|_{t=N}.
\]
Work modulo \(t^n\), and impose \(b_j=0\) whenever \(p\mid j\). At degree \(j\), the coefficient of \(g^{-1}tg'\) is \(j b_j\) plus an expression involving only \(b_1,\ldots,b_{j-1}\). For \(p\nmid j\), the coefficient \(uj\) is invertible, so there is a unique choice of \(b_j\) that eliminates the coefficient at that degree. For \(p\mid j\), set \(b_j=0\) and retain its coefficient \(h_{j/p}\). Induction over all degrees yields
\[
U^{-1}DU=uH+\sum_{r=1}^{s}h_r N^{pr}.
\]
This is a **triangular bijection of finite-field parameter spaces**: for fixed \(u\), the original \(n-1\) coefficients of \(f\) correspond bijectively to the \(n-1-s\) normalization coordinates \(b_j\) with \(p\nmid j\) and the \(s\) retained coefficients \(h_r\). No roots, logarithms, or divisions by multiples of \(p\) are required.

**4. Jordan form of the normalized operator.** Decompose the basis indices into the residue classes \(j\equiv c\pmod p\). Their dimensions are \(m_c\). On class \(c\), \(H\) acts as scalar \(c\) and \(N^p\) acts as a single nilpotent shift \(S_{m_c}\). Thus the restriction is
\[
cuI+\sum_{r=1}^{s}h_r S_{m_c}^r.
\]
If the first nonzero retained coefficient has index \(r\), its nilpotent part is \(S_{m_c}^r\) times a commuting invertible polynomial in \(S_{m_c}\). The dimensions of the kernels of every positive power therefore agree with those of \(S_{m_c}^r\), proving the partition \(\mathcal P(m_c,r)\). If all retained coefficients vanish, set \(r=s+1\). Since \(m_c\le s+1\) for every \(c\), every nilpotent part is then zero. Distinct residue classes have distinct eigenvalues \(cu\) for fixed nonzero \(u\), so their Jordan data do not mix.

**5. Counting and ranks.** For fixed \(u\), the normalization coordinates are free, giving \(q^{n-1-s}\) choices. First nonzero \(h_r\) at \(1\le r\le s\) contributes \((q-1)q^{s-r}\), while all zero contributes one. This proves the stated conditional counts. The zero eigenvalue occurs precisely on the class \(c=0\), whose dimension is \(m=\lfloor n/p\rfloor\). Its nullity is \(\min(m,r)\). Summing the possibilities \(r\) gives the displayed rank distribution, including the boundary cases \(m=0\) and \(m=1\). If \(p>n\), then \(m=0\) and every \(u\ne0\) gives an invertible diagonalizable derivation; if \(p\le n\), the diagonal entry at \(e_p\) is zero for every derivation, forcing singularity. Finally all counts sum to the known total \(q^n\), independently of the computational checks.

## Verification

The accompanying standalone program `verify_jordan.py` constructs the original derivation matrices directly from the multiplication table, and independently recovers all Jordan block partitions from the nullities of powers of \(D-\lambda I\), using finite-field Gaussian elimination. It compares each profile-count distribution conditional on \(a_1\) with the theorem and separately checks every nullity multiplicity. It does **not** use the similarity-normalization argument to obtain expected matrices. The file `check_output.txt` records twenty exhaustive configurations over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), and \(\mathbb F_9\).

For illustration, in characteristic two with \(n=3\), fixing \(a_1=1\) gives two diagonalizable derivations and two derivations having a nontrivial size-two Jordan block at eigenvalue one. All four have nullity one. Thus the Jordan census detects a distinction invisible to the ordinary rank distribution. The proof above, not finite enumeration, establishes the formulas in every dimension and extension field.

## Relationship to prior work

The null-filiform Leibniz multiplication table and the triangular derivation matrix are established background. Khudoyberdiyev and Omirov's 2013 paper explicitly displays the derivation matrix while studying deformations in characteristic zero. Ladra, Rikhsiboev, and Turdibaev's 2011 paper proves general Jordan–Chevalley structure for **complex** Leibniz derivations; it does not state an enumeration of modular Jordan blocks over finite fields. Adashev, Camacho, and Omirov's 2015 work addresses central extensions of null-filiform algebras, not modular derivation spectra. Calderón, Camacho, Kaygorodov, and Omirov's subsequent grading study addresses a different invariant.

The new claim is the explicit **positive-characteristic resonance normal form together with its full Jordan-type and multiplicity census**. It is not a claim that triangular derivation matrices, null-filiform algebras, general Jordan decomposition, or shift-power Jordan partitions are themselves new. The count can be derived using those older inputs together with the normalization argument here. Equivalent earlier modular normal forms or rank enumerations may exist under matrix-theoretic terminology; complete publication priority has not been independently established.

## Limitations

Only the explicitly presented right null-filiform Leibniz algebra and ordinary derivations are treated. These linear similarities are not asserted to be conjugations by Leibniz-algebra automorphisms. The formulas do not describe orbit sizes under that automorphism group, local derivations, or arbitrary filiform deformations. Finite-field exhaustive checks cover bounded dimensions only, and there has been no independent mathematical audit or exhaustive bibliographic certification.

## References

- M. Ladra, I. M. Rikhsiboev, and R. M. Turdibaev, *Automorphisms and derivations of Leibniz algebras*, arXiv:1103.4721v1 (first public posting 2011-03-24), especially Theorem 3.2. https://arxiv.org/abs/1103.4721
- A. Kh. Khudoyberdiyev and B. A. Omirov, *Infinitesimal deformations of null-filiform Leibniz superalgebras*, arXiv:1304.0126v1 (first public posting 2013-03-30), especially Section 3 and the displayed derivation matrix. https://arxiv.org/abs/1304.0126
- J. K. Adashev, L. M. Camacho, and B. A. Omirov, *Central extensions of null-filiform and naturally graded filiform non-Lie Leibniz algebras*, arXiv:1511.07683v1 (first public posting 2015-11-24), especially the null-filiform central-extension classification. https://arxiv.org/abs/1511.07683
- A. Calderón, L. Camacho, I. Kaygorodov, and B. Omirov, *Abelian groups gradings on null-filiform and one-parametric filiform Leibniz algebras*, arXiv:1708.01753v1 (first public posting 2017-08-05). https://arxiv.org/abs/1708.01753
