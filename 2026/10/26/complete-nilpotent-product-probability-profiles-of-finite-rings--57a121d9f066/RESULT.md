# Complete nilpotent-product probability profiles of finite rings

## Finding
Let \(R\) be any finite nonzero associative ring with identity. Write its semisimple quotient in Wedderburn form
\[
R/J(R)\cong\prod_{i=1}^{t}M_{n_i}(\mathbb F_{q_i}),\qquad n_i\ge1,
\]
where each \(q_i\) is a prime power. For every integer \(k\ge1\), choose \(k\) independent uniformly distributed elements of \(R\) and let \(P_k(R)\) denote the probability that their ordered product is nilpotent. Then
\[
\boxed{P_k(R)=\prod_{i=1}^{t}\left[1-\left(1-q_i^{-n_i}\right)^k\right].}
\]
Furthermore, for any two such finite rings \(R,S\), equality \(P_k(R)=P_k(S)\) for *every* positive integer \(k\) holds if and only if the multisets
\[
\big\{\!\big\{q_i^{n_i}:1\le i\le t\big\}\!\big\}
\]
and the corresponding multiset for \(S\) are equal. Thus the complete probability profile determines precisely the multiset of cardinalities of simple left modules of the semisimple quotient (with one copy per simple matrix factor), but does not determine the ring up to isomorphism. In particular, a field \(\mathbb F_{q^n}\), the matrix ring \(M_n(\mathbb F_q)\), and all finite rings whose semisimple quotient is either have the same profile for all \(k\), even though for \(n\ge2\) the displayed semisimple examples are nonisomorphic.

## Assumptions and scope
All rings are finite, nonzero, associative, and unital, not assumed commutative. Factors are uniformly and independently sampled *with replacement*. A product is nilpotent if a positive integer power of that product is zero. The Wedderburn decomposition is unique up to permuting its simple matrix factors. The theorem concerns this probability sequence and its exact equivalence classes; it does not assert that equal profiles imply ring isomorphism or the same radical.

## Proof
**Step 1: Reduction through the radical.** The Jacobson radical \(J(R)\) is a nilpotent ideal of any finite ring. If \(J(R)^e=0\), then for any \(x\in R\), nilpotence of its image in \(R/J(R)\) means \(x^a\in J(R)\) for some \(a\), and consequently \(x^{ae}=0\). The converse is immediate. The quotient map sends independent uniform elements of \(R\) to independent uniform elements of \(R/J(R)\). Hence \(P_k(R)=P_k(R/J(R))\). Nilpotence in a finite direct product is componentwise, and uniform independence across direct-product coordinates gives the product formula after computing its single matrix factor.

**Step 2: Nilpotent square-matrix count.** For each \(r\ge0\), exactly \(q^{r(r-1)}\) matrices in \(M_r(\mathbb F_q)\) are nilpotent. Here is a derivation. Let \(N_r\) be this count, \(G_r=|\operatorname{GL}_r(\mathbb F_q)|\), and set \(G_0=N_0=1\). Fitting decomposition associates to every linear endomorphism a unique invariant direct sum of its nilpotent and invertible parts. The number of ordered complementary subspaces of respective dimensions \(j\) and \(r-j\) is \(G_r/(G_jG_{r-j})\). Counting all endomorphisms by these unique parts gives
\[
\frac{q^{r^2}}{G_r}=\sum_{j=0}^{r}\frac{N_j}{G_j}.
\]
Subtract the corresponding relation at \(r-1\) to obtain
\[
\frac{N_r}{G_r}=\frac{q^{r^2}}{G_r}-\frac{q^{(r-1)^2}}{G_{r-1}}.
\]
Since \(q^{r^2}/G_r=\prod_{j=1}^{r}(1-q^{-j})^{-1}\), the right-hand side equals \(q^{-r}q^{r^2}/G_r\). Thus \(N_r=q^{r^2-r}\), and the nilpotence probability of a uniform endomorphism of an \(r\)-space is \(q^{-r}\).

**Step 3: The \(k\)-factor matrix formula.** Let \(V=\mathbb F_q^n\) and independently sample \(A_1,\ldots,A_k\) uniformly from \(\operatorname{End}(V)\). Condition on \(C=A_1\cdots A_{k-1}\), of rank \(r\) and image \(U\). The random product \(CA_k\) is a uniform linear map from \(V\) into \(U\): postcomposition by the fixed surjection \(C:V\to U\) sends the uniform endomorphism \(A_k\) to the uniform member of \(\operatorname{Hom}(V,U)\). Consequently its restriction to \(U\) is uniform in \(\operatorname{End}(U)\). Since its image lies in \(U\), \(CA_k\) is nilpotent if and only if this restriction is nilpotent. By Step 2 the conditional nilpotence probability is \(q^{-r}\).

For an independent uniform vector \(v\in V\), the conditional probability that \(Cv=0\) is also \(q^{-r}\). Therefore
\[
\Pr(A_1\cdots A_k\text{ nilpotent})=\Pr(A_1\cdots A_{k-1}v=0).
\]
If \(v\ne0\), the image of \(v\) under a uniform independent random matrix is uniform on \(V\). Conditional on a nonzero current vector, each subsequent random matrix preserves nonzeroness with probability \(1-q^{-n}\), independent of the past. Thus the right side is exactly \(1-(1-q^{-n})^k\). This proves the stated factor formula for every \(n,q,k\), including \(k=1\), where \(C\) is interpreted as the identity.

**Step 4: The profile is a complete invariant of simple-module orders.** Set \(s_i=1-q_i^{-n_i}\), so \(0<s_i<1\) and \(P_k(R)=\prod_i(1-s_i^k)\). The multiset of \(s_i\) clearly determines every \(P_k\). Conversely, suppose the full sequence is known. If the multiset is nonempty, put \(s=\max_i s_i\) and let \(m\) be its multiplicity. By expanding the finite product and comparing the largest exponential rate,
\[
1-P_k(R)=m s^k+o(s^k)\quad(k\to\infty).
\]
Hence \(s=\lim_{k\to\infty}(1-P_k(R))^{1/k}\), and \(m=\lim_{k\to\infty}(1-P_k(R))/s^k\). Divide \(P_k(R)\) by \((1-s^k)^m\) and repeat to recover every smaller value with its multiplicity; the finite procedure terminates. Thus the full probability profile determines the multiset of \(s_i\), equivalently the multiset of \(q_i^{n_i}\). This proves the if-and-only-if assertion.

## Verification
A standalone exact-enumeration checker accompanies this result. It independently forms all tuples of lengths \(1\) through \(4\) over \(M_2(\mathbb F_2)\), lengths \(1\) through \(2\) over \(M_2(\mathbb F_3)\), and lengths \(1\) through \(5\) over both \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) and the noncommutative upper-triangular ring \(\operatorname{UT}_2(\mathbb F_2)\). It tests nilpotence of each product and matches all rational probabilities, printing `VERIFY_OK`. The infinite theorem follows from the exact argument, not those finite checks.

## Relationship to prior work
The 2026 study of Sarma and Subedi (arXiv:2610.07892) studies the nilpotent product of **two** elements and gives a detailed commutative-ring classification. Wästlund (arXiv:2008.13017, Proposition 14) already gives the two-factor rectangular finite-field matrix probability. Dolžan (arXiv:2504.12886) gives detailed **two-factor** multiplication probabilities in semisimple rings. Sarma and Subedi (arXiv:2506.10392) study the probability that a product of \(k\) elements is **zero**, not nilpotent. These are acknowledged, and the case \(k=2\) over semisimple rings is not claimed as new. The assessed contribution is the exact nilpotence-probability profile for **all lengths and all finite associative unital rings** together with the converse classification of indistinguishable full profiles.

## Limitations
The data are sampled uniformly and independently; the formula does not apply without these assumptions. Equal profiles do not identify Morita or ring isomorphism classes; only the simple-module size multiset is recovered. Potential implicit treatment in older random-matrix-product or ring-probability literature remains a priority risk. This is a mathematical argument with limited finite corroboration, not an external or independent certification.

## References
- D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892 (first posted 2026-10-06).
- J. Wästlund, *Padlock Solitaire: A martingale trick for combinatorial enumeration*, arXiv:2008.13017 (2020), Sections 14–15.
- D. Dolžan, *The multiplication probability of a finite ring*, arXiv:2504.12886 (2025).
- D. Sarma and T. Subedi, *The probability that the product of k elements in a finite ring is zero*, arXiv:2506.10392 (2025).
- N. Fine and I. Herstein, *The probability that a matrix be nilpotent*, Illinois J. Math. 2 (1958), 499–504.
