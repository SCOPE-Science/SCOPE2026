# Spectral rigidity of LCM-top divisor matrices

## Finding

For an integer \(n\ge1\), define \(B_n\) as the real symmetric matrix whose rows and columns are indexed by the positive divisors \(d,e\mid n\) and whose \((d,e)\) entry equals \(1\) exactly when \(\operatorname{lcm}(d,e)=n\), and \(0\) otherwise.

**Theorem.** Let \(n=\prod_{i=1}^{r}p_i^{a_i}\), where the primes are distinct and \(a_i\ge1\). Put
\[
\lambda_\pm(a)=\frac{1\pm\sqrt{4a+1}}{2}.
\]
Then the nonzero eigenvalues of \(B_n\), **with algebraic multiplicities**, form the multiset
\[
\left\{\prod_{i=1}^{r}\lambda_{\epsilon_i}(a_i):\epsilon_i\in\{+,-\}\right\};
\]
the zero eigenvalue has multiplicity \(\prod_{i=1}^{r}(a_i+1)-2^r\). More strongly, the nonzero eigenvalue multiset uniquely determines the unordered multiset \(\{a_1,\ldots,a_r\}\). Thus \(B_m\) and \(B_n\) are cospectral if and only if the positive prime-power exponent multisets of \(m\) and \(n\) agree; this is also equivalent to isomorphism of their divisor lattices. For \(n=1\), the empty-product convention gives \(B_1=(1)\).

When \(r\ge1\), the inertia of \(B_n\) consists of \(2^{r-1}\) positive eigenvalues, \(2^{r-1}\) negative eigenvalues, and \(\tau(n)-2^r\) zeros. The ordinary \(n\times n\) matrix \(A_n=(\mathbf 1_{\operatorname{lcm}(i,j)=n})_{1\le i,j\le n}\) has exactly these nonzero eigenvalues, with \(n-\tau(n)\) additional zeros.

## Assumptions and scope

All indices, divisors and primes are positive integers. The spectrum is counted over the real numbers with multiplicity, including repeated products from distinct sign choices. Every statement holds for every \(n\ge1\), without squarefreeness or restrictions on the exponents. Cospectrality means equality of complete eigenvalue multisets of matrices of the same size; equality of **nonzero** eigenvalue multisets alone already forces equality of exponent multisets and therefore automatically of matrix sizes.

## Proof

**1. Prime-power tensor factorization.** Under the bijection between divisors of \(n\) and exponent vectors \((j_1,\ldots,j_r)\), with \(0\le j_i\le a_i\), the condition \(\operatorname{lcm}(d,e)=n\) says \(\max(j_i,k_i)=a_i\) for each \(i\). Consequently, after a simultaneous permutation of rows and columns,
\[
B_n=\bigotimes_{i=1}^r L_{a_i},\qquad
(L_a)_{j,k}=\mathbf1_{\max(j,k)=a}\quad(0\le j,k\le a).
\]
In \(L_a\), the upper-left \(a\times a\) block is zero, and the last row and column are all ones. Define the two vectors \(u=(1,\ldots,1,0)\) and \(v=(0,\ldots,0,1)\), with \(a\) initial coordinates in \(u\). Direct multiplication gives \(L_a u=a v\) and \(L_a v=u+v\). On their span, the representing matrix is \(\left(\begin{smallmatrix}0&1\\a&1\end{smallmatrix}\right)\), with characteristic polynomial \(t^2-t-a\) and roots \(\lambda_+(a)>0>\lambda_-(a)\). All vectors whose last coordinate is zero and whose first \(a\) coordinates sum to zero form an \((a-1)\)-dimensional kernel. The local eigenvalues are thus \(\lambda_+(a),\lambda_-(a)\) and \(a-1\) zeros.

Tensor products of real symmetric matrices multiply eigenvalues with multiplicities. Since both local nonzero roots are nonzero, precisely \(2^r\) tensor eigenvalues are nonzero and have the displayed values, with \(\tau(n)-2^r\) remaining zeros. The sign choices are equally split when \(r\ge1\), proving the inertia claim. For \(n=1\), there is a single divisor and the theorem is immediate. Moreover, if \(1\le i,j\le n\) and \(\operatorname{lcm}(i,j)=n\), then both \(i\) and \(j\) divide \(n\). Thus \(A_n\) consists of \(B_n\) as its divisor-index principal block and zeros elsewhere, proving the final assertion.

**2. Inverse recovery from nonzero eigenvalues.** For each \(a\ge1\), one has \(0<-\lambda_-(a)<\lambda_+(a)\). Therefore the unique eigenvalue of largest absolute value is
\[
\rho=\prod_{i=1}^{r}\lambda_+(a_i)>0,
\]
with multiplicity one. Normalize the *absolute values* of the nonzero eigenvalues by \(\rho\). The resulting multiset is
\[
P=\left\{\prod_{i\in S}q_i:S\subseteq\{1,\ldots,r\}\right\},\quad
q_i=\frac{-\lambda_-(a_i)}{\lambda_+(a_i)}
=\frac{\sqrt{4a_i+1}-1}{\sqrt{4a_i+1}+1}\in(0,1).
\]
We claim that any finite subset-product multiset with factors strictly between zero and one uniquely determines the multiset of factors. Its cardinality determines \(r\). If \(r=0\), there is nothing to reconstruct. Otherwise its largest element is the unique product of the empty subset, namely \(1\), and its largest *remaining occurrence* equals \(q=\max_i q_i\). Choose one factor equal to \(q\), and let \(U\) be the subset-product multiset of the other \(r-1\) factors. Then, with multiplicities, \(P=U\sqcup qU\).

This decomposition is **unique**: begin with the multiset \(P\); take its largest remaining member \(u\), place one copy in \(U\), and remove one occurrence each of \(u\) and \(qu\); repeat. Indeed, if an element belongs to \(qU\), its unscaled partner \(u/q\in U\) is strictly larger and was therefore already processed, together with the corresponding scaled copy. The largest remaining member must accordingly come from \(U\). This induction is unaffected by coinciding numerical subset products or repeated factors, since the operation is on *multisets*. It determines \(U\) uniquely. Applying the same argument recursively reconstructs all factors \(q_i\) without knowing their labels.

Finally, solving the displayed expression for \(q_i\) yields
\[
a_i=\frac{q_i}{(1-q_i)^2}.
\]
Hence the nonzero spectrum reconstructs every prime-power exponent, up to permutation. Conversely, equal exponent multisets plainly give identical tensor spectra and dimensions. Their divisor lattices are the same finite product of chains, up to permutation. An isomorphism of finite divisor lattices also forces equal chain lengths, since the atoms have intrinsic join-irreducible chain lengths; equivalently each factor \([0,a_i]\) is recovered from the connected components of the join-irreducible comparability graph. This proves the claimed equivalences.

## Verification

The accompanying standard-library script `verify.py` directly builds \(B_n\), computes exact integer traces and characteristic polynomials via Newton identities, and compares traces with those predicted by the local recurrence \(s_k(a)=s_{k-1}(a)+a s_{k-2}(a)\), with \(s_0(a)=2\) and \(s_1(a)=1\). It covers 16 different integers, checks the cospectral pairs \((72,500)\) and \((12,18)\), checks a same-size/same-rank but noncospectral pair \((72,96)\), and tests recursive inversion even with repeated subset products, using 100-digit decimal arithmetic. Run: `python3 verify.py`. These finite tests are independent evidence of implementation consistency; the proof of the universal theorem is the tensor decomposition and multiset-recovery argument above, not extrapolation from the tests.

## Relationship to prior work

OEIS A034444 records Yuval Dekel's August 11, 2003 observation that the rank of the \(n\times n\) indicator matrix \(\mathbf1_{\operatorname{lcm}(i,j)=n}\) equals the number of unitary divisors, \(2^{\omega(n)}\). The rank identity also follows here, but is *not* claimed new. Established arithmetic matrix work studies weighted GCD/LCM, meet/join matrix factorizations, spectral bounds, and tensor products; see Ovall (2004), Mattila–Haukkanen (2013), and Hilberdink–Pushnitski (2021). Their inspected assertions do not give the **nonzero-spectrum-to-prime-exponent rigidity** of this binary top-indicator matrix, nor the consequent exact cospectral classification. The tensor-product technique itself is standard; the asserted contribution is the particular exact spectral formula together with inverse recovery in the natural A034444 matrix family.

## Limitations

The matrix spectrum does **not** distinguish the underlying prime bases: for example, \(72=2^3\cdot3^2\) and \(500=2^2\cdot5^3\) have identical divisor-matrix spectra. The theorem reconstructs exponent multisets, not the integer \(n\). An extensive search of all prior join-matrix spectral literature has not been completed; in particular, the full text of Mattila–Haukkanen's related 2014 meet/join paper was not inspected. Thus mathematical priority is provisional. The numerical inversion tests use finite precision; the theorem's inverse argument is exact and does not rely on stability under noisy eigenvalues. No independent audit is asserted.

## References

1. OEIS Foundation, *A034444: Number of unitary divisors of n*, comment by Yuval Dekel, August 11, 2003. https://oeis.org/A034444
2. J. S. Ovall, *An analysis of GCD and LCM matrices via the LDL^T-factorization*, Electronic Journal of Linear Algebra (2004). https://journals.uwyo.edu/index.php/ela/article/download/243/243
3. M. Mattila and P. Haukkanen, *On the eigenvalues of certain number-theoretic matrices*, arXiv:1309.0320v1 (2013). https://arxiv.org/html/1309.0320v1
4. T. Hilberdink and A. Pushnitski, *Spectral asymptotics for a family of LCM matrices*, arXiv:2110.14323v1 (2021). https://arxiv.org/html/2110.14323v1
