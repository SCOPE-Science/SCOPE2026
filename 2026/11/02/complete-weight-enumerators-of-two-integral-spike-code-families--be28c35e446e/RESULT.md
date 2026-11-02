# Complete weight enumerators of two integral spike-code families

## Finding

For every integer \(k\ge 2\) and every modulus \(q\ge 2\), define the codes over the residue ring \(\mathbb Z/q\mathbb Z\) by the integral generator matrices
\[
G_N=\bigl(I_k\mid J_k-I_k\bigr),\qquad
G_Z=\bigl(I_k\mid J_k-I_k\mid\mathbf 1_k\bigr),
\]
where \(I_k\) is the identity matrix, \(J_k\) is the all-ones matrix, and \(\mathbf 1_k\) is the all-ones column. Write \(W_N(z)\) and \(W_Z(z)\) for their ordinary Hamming weight enumerators, \(W(z)=\sum_{c}z^{\mathrm{wt}(c)}\). Let
\[
S_{k,q}=\sum_{j=0}^{k}\binom{k}{j}\gcd(q,j-1),
\]
using the convention \(\gcd(q,0)=q\), and put
\[
B_{k,q}(z)=\frac{(1+(q-1)z^2)^k+(q-1)(1-z^2)^k}{q},
\]
\[
H_{k,q}(z)=\frac{z^k}{q}\left((q-1)(2+(q-2)z)^k
+\bigl(qS_{k,q}-(2q-1)2^k\bigr)(1-z)^k\right).
\]
Then, simultaneously for all such \(k,q\), the **complete** Hamming weight enumerators are
\[
\boxed{W_N(z)=B_{k,q}(z)+H_{k,q}(z),\qquad
W_Z(z)=B_{k,q}(z)+zH_{k,q}(z).}
\]
In particular, for every \(k\ge5\), both codes have exactly \(\binom{k}{2}(q-1)\) words of minimum weight four. These expressions determine every weight multiplicity, not only the full-support coefficient.

## Assumptions and scope

The integer \(q\) need not be prime or a prime power; the codes are modules over \(\mathbb Z/q\mathbb Z\), and Hamming weight counts nonzero coordinates. Every message maps injectively because the generator matrices contain \(I_k\). The theorem is for the displayed integral matrices for each \(k\ge2\), with no asymptotic or generic-modulus exclusions. It concerns ordinary Hamming weight enumerators, not the complete symbol-composition enumerators or arbitrary representations of spike matroids.

## Proof

Write a message as \(u=(u_1,\ldots,u_k)\) and \(s=\sum_i u_i\pmod q\). Its images are
\[
c_N(u)=(u_1,\ldots,u_k,s-u_1,\ldots,s-u_k),\qquad
c_Z(u)=(c_N(u),s).
\]
Because the first \(k\) coordinates recover \(u\), summing over messages counts codewords exactly once.

**Zero-sum messages.** If \(s=0\), each nonzero \(u_i\) contributes exactly two to the weight. The number of \(r\)-tuples of nonzero residues summing to zero is
\[
\frac{(q-1)^r+(q-1)(-1)^r}{q}.
\]
Indeed, insert the character projector \(q^{-1}\sum_{a=0}^{q-1}\exp(2\pi i a\sum u_i/q)\); the trivial character gives \((q-1)^r\) and each nontrivial character gives \((-1)^r\). Choosing the \(r\) occupied positions and summing over \(r\) gives \(B_{k,q}(z)\). The last coordinate of \(c_Z\) is zero in this case.

**Nonzero-sum messages.** Fix \(s\ne0\). The pair \((u_i,s-u_i)\) has Hamming weight one exactly when \(u_i=0\) or \(u_i=s\), two distinct choices; otherwise its weight is two. For an additive character \(\chi_a(v)=\exp(2\pi i av/q)\), the one-coordinate weight transform equals
\[
F_{a,s}(z)=\sum_{v\in\mathbb Z/q\mathbb Z}z^{\mathrm{wt}(v,s-v)}\chi_a(v)
=\begin{cases}
2z+(q-2)z^2,&a=0,\\
z(1-z)(1+\chi_a(s)),&a\ne0.
\end{cases}
\]
The fixed-sum condition \(\sum_i u_i=s\) therefore yields
\[
H_{k,q}(z)=\frac1q\sum_{s\ne0}\sum_{a=0}^{q-1}\chi_a(-s)F_{a,s}(z)^k.
\]
The trivial character contributes \((q-1)(2z+(q-2)z^2)^k/q\). Expand the nontrivial part by the binomial theorem and use the exact root-of-unity identity
\[
\sum_{s\ne0}\sum_{a\ne0}\chi_a((j-1)s)
=q\bigl(\gcd(q,j-1)-1\bigr)-(q-1).
\]
This holds for composite moduli too: among all \(s\pmod q\), precisely \(\gcd(q,j-1)\) solve \((j-1)s\equiv0\pmod q\). Summing with coefficients \(\binom{k}{j}\) gives the stated expression for \(H_{k,q}(z)\). The extra coordinate of \(c_Z\) is nonzero for these messages, so it raises every corresponding weight by one. This proves both formulas.

For \(k\ge5\), the nonzero-sum component begins in degree \(k\), and the zero-sum component has degree-four coefficient \(\binom{k}{2}((q-1)^2+(q-1))/q=\binom{k}{2}(q-1)\). The previously established minimum-distance bound of four for \(k\ge4\) also follows directly from these enumerators, so the coefficient counts minimum words.

## Verification

The standalone, dependency-free `verify.py` computes the formula coefficients using integer binomial sums and greatest common divisors. Independently, it enumerates all messages and computes Hamming weights directly from the displayed generator representation for 41 parameter pairs. It also tests 1,421 additional parameter pairs against the published full-support formulas, coefficient nonnegativity, total \(q^k\), both known minimum distances, and the minimum-weight multiplicity. The program prints `NZ_WEIGHT_ENUMERATORS_OK direct_pairs=41 structural_cases=1421` when all checks succeed.

These finite checks are not the proof for unbounded \(k,q\); the character-sum argument above establishes the theorem for all claimed parameters.

## Relationship to prior work

Imamura, Nakashima, and Saito (arXiv:2601.21121, originally submitted January 28, 2026) introduce these same integral matrices, establish minimum distances in their Section 5, and give explicit *full-support* counts in Theorem 5.3. Their Section 5 explicitly distinguishes those counts from a complete Hamming spectrum. The displayed all-weight formulas extend those results, and their top-degree coefficients agree algebraically with Theorem 5.3.

Kuroda, Nakashima, and Tsujie (arXiv:2512.10838) develop the general coboundary quasi-polynomial formalism, which is related to weight distributions; that framework does not itself give the displayed closed expressions for these two matrices in the inspected material. Classical Tutte-polynomial descriptions of binary spikes may encode some prime-field specializations implicitly. The present theorem specifically provides one explicit formula for *every* modulus \(q\ge2\), including composite rings.

## Limitations

The theorem treats two specified families and ordinary Hamming weights; it does not characterize all integral representations of spike matroids, generalized Hamming weights, or optimality under decoding. It does not claim the general character-sum or Tutte methods as new. Although targeted comparisons did not identify an earlier equivalent formula, a previously published arithmetic Tutte evaluation or an unindexed calculation may cover this statement. Independent mathematical review and publication-priority confirmation have not been performed.

## References

1. K. Imamura, N. Nakashima, and T. Saito, *Periodicity of weight enumerators for codes generated by an integral matrix*, arXiv:2601.21121v2 (2026), Sections 4–5, especially Proposition 5.1, Corollary 5.2, and Theorem 5.3. https://arxiv.org/html/2601.21121v2
2. M. Kuroda, N. Nakashima, and S. Tsujie, *The Coboundary Quasi-Polynomials of Hyperplane Arrangements over Residually Finite Dedekind Domains*, arXiv:2512.10838v3 (2026 revision). https://arxiv.org/html/2512.10838v3
3. P. Brändén and L. Moci, *The multivariate arithmetic Tutte polynomial*, Transactions of the American Mathematical Society 366 (2014), 5523–5540.
