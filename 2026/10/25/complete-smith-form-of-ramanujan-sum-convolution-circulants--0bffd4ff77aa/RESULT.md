# Complete Smith form of Ramanujan-sum convolution circulants

## Finding

For every integer \(n\ge1\), put \(r=\varphi(n)\) and let the integral \(n\times n\) circulant be
\[
C(n)_{i,j}=c_n(i-j),\quad 0\le i,j<n,\qquad
c_n(t)=\sum_{d\mid\gcd(n,t)}d\,\mu(n/d).
\]
For \(1\le j\le r\), define the following positive integers, with an empty product equal to \(1\):
\[
d_j(n)=\prod_{p^a\parallel n}p^{\,a-1+\mathbf{1}_{\{j>r/(p-1)\}}}.
\]
Then the **complete integral Smith normal form** is
\[
\operatorname{SNF}_{\mathbb Z}C(n)
=\operatorname{diag}\bigl(d_1(n),\ldots,d_r(n),
\underbrace{0,\ldots,0}_{n-r}\bigr).
\]
In particular, these invariant factors satisfy \(d_j(n)\mid d_{j+1}(n)\). Their formula holds also for \(n=1\) and \(n=2\). Consequently,
\[
\operatorname{coker}_{\mathbb Z}C(n)\cong
\mathbb Z^{n-r}\oplus\bigoplus_{j=1}^r\mathbb Z/d_j(n)\mathbb Z.
\]
The finite torsion subgroup has exponent \(n/\gcd(n,2)\) and order
\[
\prod_{j=1}^r d_j(n)=
\frac{n^{\varphi(n)}}{\displaystyle\prod_{p\mid n}p^{\varphi(n)/(p-1)}}.
\]
Its torsion is cyclic exactly for \(n\in\{1,2,3,6\}\). For every positive integer \(m\), the number of solutions of \(C(n)v\equiv0\pmod m\) in \((\mathbb Z/m\mathbb Z)^n\) equals
\[
m^{n-\varphi(n)}\prod_{j=1}^{\varphi(n)}\gcd(m,d_j(n)).
\]

## Assumptions and scope

The modulus \(n\) is any positive integer; its factorization \(\prod_{p^a\parallel n}p^a\) uses distinct primes \(p\) and positive exponents \(a\). The symbol \(p^a\parallel n\) means exact divisibility. Euler's totient is \(\varphi\), and \(\mu\) is the Möbius function. The indicator \(\mathbf1_{\{Q\}}\) is \(1\) when the condition \(Q\) is true and \(0\) otherwise. Rows and columns are indexed by the cyclic group \(\mathbb Z/n\mathbb Z\). Smith equivalence is by two integer unimodular matrices; merely diagonalizing over \(\mathbb C\) does not suffice. The asserted numbers \(d_j(n)\) are canonical invariant factors, not an unordered list of eigenvalues.

## Proof

**1. Prime-power blocks.** For every prime \(p\), every \(a\ge1\), and every integer \(t\), the Ramanujan identity gives
\[
c_{p^a}(t)=p^{a-1}\bigl(p\,\mathbf1_{\{p^a\mid t\}}-
\mathbf1_{\{p^{a-1}\mid t\}}\bigr).
\]
Reorder the indices modulo \(p^a\) by their residue classes modulo \(p^{a-1}\). Entries between different classes vanish. Inside each class, the corresponding \(p\times p\) block is
\[
p^{a-1}(pI_p-J_p),
\]
where \(J_p\) is the all-ones matrix. Therefore \(C(p^a)\) is permutation-equivalent to a direct sum of precisely \(p^{a-1}\) identical blocks.

**2. The integral local form.** Put \(A=pI_p-J_p\). Since the sum of its columns vanishes, replacing its last column by that sum is a unimodular column operation and makes it zero. Subtracting the original last row from each of the first \(p-1\) rows gives, in the remaining first \(p-1\) columns, the matrix consisting of \(pI_{p-1}\) stacked above the row \((-1,\ldots,-1)\). This has rank \(p-1\). Any \(k\times k\) minor, \(1\le k\le p-1\), uses at least \(k-1\) rows divisible by \(p\); thus it is divisible by \(p^{k-1}\). Choosing the bottom row together with \(k-1\) distinct coordinate rows and an additional coordinate column yields a minor exactly \(\pm p^{k-1}\). Hence its \(k\)-th determinantal divisor is exactly \(p^{k-1}\), and
\[
\operatorname{SNF}(pI_p-J_p)=
\operatorname{diag}(1,\underbrace{p,\ldots,p}_{p-2},0).
\]
Multiplication by \(p^{a-1}\) and the direct sum in step 1 show that \(C(p^a)\) has \(p^{a-1}\) nonzero local Smith entries equal to \(p^{a-1}\), \((p-2)p^{a-1}\) equal to \(p^a\), and \(p^{a-1}\) zeros. For \(p=2\), the middle multiplicity is zero.

**3. Chinese-remainder tensor factorization.** For coprime positive integers \(u,v\), multiplicativity of Ramanujan sums gives \(c_{uv}(t)=c_u(t)c_v(t)\). The Chinese remainder bijection of row and column indices therefore gives an equality, after a simultaneous permutation,
\[
C(uv)\simeq C(u)\otimes C(v).
\]
Tensoring the integral unimodular equivalences from step 2 yields an integral unimodular diagonalization of \(C(n)\), with nonzero diagonal entries the products of nonzero local Smith entries. The count of nonzero entries is
\[
\prod_{p^a\parallel n}(p-1)p^{a-1}=\varphi(n)=r.
\]
Thus exactly \(n-r\) diagonal entries are zero.

**4. Assemble canonical invariant factors.** Fix a prime \(p^a\parallel n\). Among those \(r\) nonzero product entries, precisely
\[
p^{a-1}\prod_{\substack{q^b\parallel n\\q\ne p}}(q-1)q^{b-1}
=\frac{r}{p-1}
\]
have \(p\)-adic valuation \(a-1\); the rest have valuation \(a\). The integer \(r/(p-1)\) is thus automatically integral. For a diagonal integer matrix, the \(p\)-valuations of its nonzero Smith invariant factors are the corresponding valuations sorted in nondecreasing order: this follows directly from determinantal divisors or localization over \(\mathbb Z_{(p)}\). Sorting independently at each prime, then multiplying the resulting prime powers at the common positions \(1\le j\le r\), proves the stated \(d_j(n)\) and their divisibility chain. No unproved assumption that tensor products preserve *ordered* Smith factors has been used.

**5. Consequences and boundary cases.** The last factor is \(d_r(n)=n/\gcd(n,2)\): for odd \(p\), \(r>r/(p-1)\), while for \(p=2\) equality holds. Summing the valuations of all \(r\) nonzero factors gives the torsion-order formula. The number of solutions modulo \(m\) follows from the diagonal form. For cyclicity, a nontrivial \(p\)-primary torsion group is cyclic exactly when at most one \(d_j(n)\) is divisible by \(p\). If \(4\mid n\), at least two entries are divisible by \(2\). If some odd prime \(p\ge5\) divides \(n\), then \(r-r/(p-1)\ge3\) entries are divisible by \(p\). If \(9\mid n\), then at least \(r\ge6\) entries are divisible by \(3\). These exclusions leave precisely \(n=1,2,3,6\), whose displayed Smith factors confirm cyclicity. For \(n=1\), \(C(1)=[1]\), so the empty product and zero-count conventions verify the claim directly.

## Verification

The accompanying standalone `verify_ramanujan_smith.py` constructs the full integer matrix from the divisor-sum definition, computes its Smith normal form independently using exact integer arithmetic, and compares every diagonal factor with the formula. It verified \(28\) moduli from \(1\) through \(42\) (nonconsecutively, covering prime, prime-power, squarefree and mixed cases). These are finite diagnostics only; the all-moduli statement follows from steps 1–5.

## Relationship to prior work

Fowler, Garcia, and Karaali, *Ramanujan sums as supercharacters* (first posted January 5, 2012), derive the prime-power evaluation and multiplicativity of Ramanujan sums and study Kronecker products of **divisor-indexed supercharacter tables**. In contrast, the present \(C(n)\) is the full \(n\times n\) **difference circulant**, and the claim is an integral Smith classification rather than a complex spectral or divisor-table identity. Schlage-Puchta, *A determinant involving Ramanujan sums and So's conjecture* (2021), establishes a determinant for the \(\tau(n)\times\tau(n)\) divisor-indexed matrix \((c(d,t))_{d,t\mid n}\), which is distinct in dimensions, rank, and indexing. Le and Sander (2013) investigate spectral classification of Ramanujan integral circulant graphs; the matrix here is not their graph adjacency matrix. A Fourier transform of \(C(n)\) yields eigenvalues \(n\) (multiplicity \(\varphi(n)\)) and \(0\) (otherwise), but complex eigenvalues do not determine integral Smith factors. Searches for direct invariant-factor and cokernel formulas found no covering statement in the inspected sources; this is a best-knowledge originality assessment, not proof of historical priority.

## Limitations

This result classifies the specific full Ramanujan-sum convolution kernel, not arbitrary integer circulants or gcd-matrix pencils. The proof does not claim new identities for Ramanujan sums themselves. Numerical Smith calculations up to dimension \(42\) are corroboration, not an infinite certificate. Coverage by unindexed prior literature, or by an earlier general integer-convolution Smith theorem not located in the inspected search, remains possible. Independent mathematical validation has not been performed.

## References

1. C. F. Fowler, S. R. Garcia, and G. Karaali, *Ramanujan sums as supercharacters*, arXiv:1201.1060 (initial submission 2012-01-05; full text inspected, Sections 2–3). https://arxiv.org/abs/1201.1060
2. J.-C. Schlage-Puchta, *A determinant involving Ramanujan sums and So's conjecture*, Archiv der Mathematik 117 (2021), 379–384, DOI:10.1007/s00013-021-01643-8 (open full text inspected). https://doi.org/10.1007/s00013-021-01643-8
3. T. A. Le and J. W. Sander, *Integral Circulant Ramanujan Graphs of Prime Power Order*, Electron. J. Combin. 20 (2013), P35, DOI:10.37236/3159 (abstract and published scope checked). https://doi.org/10.37236/3159
