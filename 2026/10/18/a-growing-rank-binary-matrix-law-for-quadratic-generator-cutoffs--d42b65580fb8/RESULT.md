# A growing-rank binary-matrix law for quadratic generator cutoffs

## Finding

Let \(r\ge 1\), let \(p_1,\ldots,p_r\) be distinct odd primes, and set \(n=\prod_{i=1}^r p_i\). Write \(\ell_1=2,\ell_2=3,\ldots\) for the increasing sequence of rational primes. Define \(J(n)\) as the least positive integer \(t\) for which the coprime prime bases among \(\ell_1,\ldots,\ell_t\) generate the full elementary two-quotient
\[
 (\mathbb Z/n\mathbb Z)^\times/((\mathbb Z/n\mathbb Z)^\times)^2.
\]
Equivalently, \(J(n)\) is the least \(t\) such that the \(r\times t\) binary matrix of Legendre symbols \(\bigl((1-(\ell_j/p_i))/2\bigr)\), with omitted zero-symbol columns, has rank \(r\). Let \(G(n)\) be the least positive cutoff for which all integers not exceeding it and coprime to \(n\) generate \((\mathbb Z/n\mathbb Z)^\times\). Then \(G(n)\ge\ell_{J(n)}\).

Sample \(p_1,\ldots,p_r\) uniformly as **distinct** primes from \((X,2X]\), and let \(X\to\infty\). For every fixed \(r,t\ge1\),
\[
 \lim_{X\to\infty}\Pr(J(n)\le t)
 =\begin{cases}0,&t<r,\\[2pt]
 \displaystyle\prod_{j=0}^{r-1}(1-2^{j-t}),&t\ge r.
 \end{cases}
\]
The same formula is uniform, up to an \(o_{C,s}(1)\) error, whenever \(r=r(X)\ge1\) and \(r\log(r+2)\le C\log\log X\) for fixed \(C>0\), with \(t=r+s\) and fixed integer \(s\ge0\). Consequently, if \(r(X)\to\infty\) in this range, the excess \(J(n)-r\) has a proper limiting integer law with cumulative distribution
\[
 \Pr(H\le s)=F(s):=\prod_{j=s+1}^{\infty}(1-2^{-j})\quad(s\ge0),
 \qquad \Pr(H<0)=0.
\]
Its expected excess is \(\mathbb E H=\sum_{j\ge1}(2^j-1)^{-1}=1.606695\ldots\). In particular \(F(0)=0.288788\ldots\): at the information-theoretic minimum of \(r\) initial prime bases, about \(71.12\%\) of these growing-prime-product tuples still have a quadratic-character obstruction to generation. This statement concerns the quadratic quotient, **not** the exact distribution of \(G(n)\).

## Assumptions and scope

All probabilities are uniform over ordered \(r\)-tuples of distinct primes in \((X,2X]\); unordered tuples give the same values because \(J(n)\) is symmetric. The fixed-\(r\) statement holds for any fixed integer \(t\ge1\). In the growing-\(r\) assertion, \(C>0\) and \(s\ge0\) are fixed independently of \(X\), and \(r\log(r+2)\le C\log\log X\). The first \(r+s\) rational primes are then below \(X\) for sufficiently large \(X\), so none divides \(n\). The limit \(F(s)\) is asserted only when \(r\to\infty\). No generalized Riemann hypothesis is assumed.

## Proof

**1. Quadratic quotient and the cutoff.** For each odd prime \(p\), the cyclic group \((\mathbb Z/p\mathbb Z)^\times\) has exactly two square classes, detected by its Legendre character. The Chinese remainder theorem gives a canonical isomorphism of elementary two-groups
\[
 (\mathbb Z/n\mathbb Z)^\times/((\mathbb Z/n\mathbb Z)^\times)^2\cong(\mathbb F_2)^r.
\]
Under this map a prime \(\ell\nmid n\) becomes the column with entries \((1-(\ell/p_i))/2\). Every positive integer coprime to \(n\) is a product of coprime prime bases no larger than itself. Thus its image is in the span of the corresponding prime columns, and generation of the full unit group forces full rank of those columns. This proves \(G(n)\ge\ell_{J(n)}\). The least \(J(n)\) exists because a proper subgroup of the quadratic quotient has a nontrivial character, and a nontrivial Dirichlet character takes value \(-1\) at some prime not dividing \(n\).

**2. Exact uniformity of fixed-prime Legendre patterns.** For \(t\ge1\) set
\[
 M_t=8\prod_{\substack{3\le\ell\le\ell_t\\\ell\text{ prime}}}\ell.
\]
On the reduced residue classes modulo \(M_t\), the \(t\) characters \(a\mapsto(\ell_j/a)\) take every sign pattern in \(\{\pm1\}^t\) exactly \(\varphi(M_t)/2^t\) times. Indeed, the sign for \(\ell_1=2\) is controlled by the residue modulo \(8\); after fixing it (and thus the residue modulo \(4\)), quadratic reciprocity expresses the sign for each odd \(\ell_j\) as a fixed factor times \((a/\ell_j)\). The Chinese remainder theorem lets those latter signs be chosen independently and each has equally many allowed residues. This works for composite reduced representatives as well, with the usual Jacobi/Kronecker character interpretation.

**3. Uniform arithmetic-to-matrix coupling.** Fix \(C>0\), take \(t=r+s\) with fixed \(s\ge0\), and assume \(r\log(r+2)\le C\log\log X\). Elementary prime bounds and Chebyshev's estimate give \(\ell_t=O(t\log(t+2))\) and
\[
 \log M_t=O(t\log(t+2))=O_C(\log\log X),
 \qquad M_t\le(\log X)^{A_C}
\]
for some constant \(A_C\). The Siegel--Walfisz theorem, with any desired fixed logarithmic saving, gives uniform equidistribution of primes in \((X,2X]\) among the reduced residue classes modulo \(M_t\). Summing the error over the \(\varphi(M_t)\) classes and choosing a saving exponent larger than \(A_C\), the total-variation distance between the Legendre-sign vector of a uniformly chosen prime in \((X,2X]\) and a uniform vector in \((\mathbb F_2)^t\) is \(O_{C,K}((\log X)^{-K})\) for each fixed \(K>0\), after increasing the Siegel--Walfisz saving exponent. For \(r\) independent prime samples the product-law distance is at most \(r\) times this error. Conditioning the samples to be distinct contributes at most \(O(r^2/\#\{p\in(X,2X]\})=o(1)\). Hence the complete \(r\times t\) Legendre-bit matrix is, in total variation, \(o(1)\)-close to an iid uniform binary matrix. For fixed \(r,t\) the same argument applies with fixed \(M_t\).

**4. Exact rank law and growing-rank limit.** A uniform \(r\times t\) binary matrix has independent rows uniformly distributed in \((\mathbb F_2)^t\). If \(t\ge r\), its first \(r\) rows are linearly independent with probability
\[
 \prod_{j=0}^{r-1}\frac{2^t-2^j}{2^t}
 =\prod_{j=0}^{r-1}(1-2^{j-t});
\]
if \(t<r\), full row rank is impossible. Combined with Step 3, this proves the fixed- and growing-rank statements. Setting \(t=r+s\) transforms the finite product into \(\prod_{j=s+1}^{r+s}(1-2^{-j})\), converging to \(F(s)\). Since \(F(s)\to1\) as \(s\to\infty\), this defines a proper limiting distribution. In the iid matrix-column process of height \(r\), going from rank \(k\) to rank \(k+1\) has success probability \(1-2^{k-r}\). Summing the means of the geometric waiting times gives a mean total of \(r+\sum_{j=1}^r(2^j-1)^{-1}\); letting \(r\to\infty\) yields \(\mathbb E H\). This is the mean of the **limiting matrix-law random variable**, not an assertion about convergence of the untruncated arithmetic expectations of \(J(n)\).

## Verification

Run `python3 verify.py` from the extracted package directory (Python standard library only). The script checks exact rank probabilities by a separate integer-count recurrence across the suite of \(130\) exact and finite checks, exhaustively enumerates moderate binary matrices, verifies equidistribution of the quadratic sign patterns over the complete reduced-residue rings for the first five base-prime cutoffs, compares the quadratic cutoff with directly generated finite unit groups, and prints four illustrative finite prime-sample frequencies. Its final marker is `VERIFY_OK`. The prime-number-theorem and uniformity statements are analytical and are **not** inferred from these finite checks.

## Relationship to prior work

Bellotti's 2026 paper studies the full least-generator cutoff \(G(n)\), proving mean-value and almost-all upper bounds via small prime-order characters. The result here concerns a different, explicitly defined necessary obstruction: the image of small primes in the full quadratic quotient of a product of many large odd primes. Bellotti's published estimates do not provide the exact law of this obstruction. Fulman and Goldstein develop rank laws of uniformly random finite-field matrices, including the rectangular full-rank probability. That algebraic factor is already known and is **not** claimed as new; the arithmetic claim is the growing-rank, uniformly coupled Legendre matrix and its consequence for a natural generator cutoff. The proof uses classical quadratic reciprocity and Siegel--Walfisz equidistribution. This is a synthesis of standard methods, and an unlocated prior formulation of the same application remains possible.

## Limitations

The theorem gives no exact asymptotic distribution for \(G(n)\): characters of orders above two may obstruct generation after the quadratic quotient is spanned. It makes no claim about convergence of arithmetic means of \(J(n)\), about arbitrary squarefree integers with small prime factors, or about \(r\) growing outside the stated logarithmic range. The Siegel--Walfisz error constants in the growing-rank argument may be ineffective. The originality comparison cannot exclude implicit earlier derivations combining standard quadratic-character and random-matrix results. The review is not independent mathematical validation.

## References

1. C. Bellotti, *Improved average and almost-all bounds for \(G(n)\)*, arXiv:2610.10177v1, first posted 7 October 2026, especially Sections 1--3.
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504; *Annals of Probability* 43 (2015), 1274--1314, especially Section 1 and the rectangular-matrix model.
3. The classical quadratic reciprocity law, the Chinese remainder theorem, and the Siegel--Walfisz prime-number theorem in arithmetic progressions, used in the forms stated in the proof.
