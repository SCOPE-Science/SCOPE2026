# Antipalindromic sparsity removes the limit assumption for binary generalized reflection complexity

## Finding
For every non-ultimately-periodic binary infinite word \(\mathbf u\), antipalindromic factors have asymptotically negligible density relative to all factors in the strong sense
\[
\lim_{n\to\infty}\frac{P_E(n)\log(P_E(n)+1)}{C_{\mathbf u}(n)}=0.
\]
If the language of \(\mathbf u\) is additionally invariant under both reversal and bit-complementation, its generalized reflection complexity has the unconditional limit
\[
\boxed{\displaystyle \lim_{n\to\infty}\frac{C_H(n)}{C_{\mathbf u}(n)}=\frac14.}
\]
There is no assumption that this limit exists, no recurrence hypothesis, and no constraint on the growth rate of factor complexity.

## Assumptions and scope
All words are one-sided infinite words over the alphabet \(\{0,1\}\), and aperiodic means **not ultimately periodic**. For each \(n\ge1\), \(C_{\mathbf u}(n)\) denotes the number of distinct length-\(n\) contiguous factors. Let \(R\) reverse a finite word, let \(C\) flip all its bits, and let \(E=CR\). An **antipalindrome** is a finite word fixed by \(E\); \(P_E(n)\) counts antipalindromic length-\(n\) factors. The group \(H=\{\mathrm{id},R,C,E\}\) acts on finite binary words. If the factor language is invariant under \(H\), \(C_H(n)\) is the number of \(H\)-orbits of its length-\(n\) factors. The natural logarithm is used, and terms with zero palindrome count are zero.

Define the first-difference infinite word \(\mathbf d\) by \(d_i=u_i\oplus u_{i+1}\), where \(\oplus\) is addition modulo two. Let \(P_R^{\mathbf d}(m)\) denote the number of ordinary palindromic length-\(m\) factors of \(\mathbf d\).

## Proof
**1. The first-difference word remains aperiodic.** Suppose \(\mathbf d\) were eventually periodic with period \(h\ge1\), from index \(N\). For \(i\ge N\), the sum modulo two of \(h\) consecutive differences, \(s=\bigoplus_{j=0}^{h-1}d_{i+j}\), is independent of \(i\), since every length-\(h\) window of an \(h\)-periodic tail has the same multiset of bits. Telescoping gives \(u_{i+h}=u_i\oplus s\), hence \(u_{i+2h}=u_i\) for all \(i\ge N\). This contradicts non-ultimate periodicity of \(\mathbf u\).

**2. Antipalindromes project to palindromes.** For a finite binary word \(w=w_0\cdots w_{n-1}\), write \(\partial w=(w_0\oplus w_1,\ldots,w_{n-2}\oplus w_{n-1})\). If \(w\) is fixed by \(E\), then \(w_i=1-w_{n-1-i}\), and consequently
\[
(\partial w)_i=w_i\oplus w_{i+1}
=(1-w_{n-1-i})\oplus(1-w_{n-2-i})
=(\partial w)_{n-2-i}.
\]
Thus \(\partial w\) is an ordinary palindrome. A prescribed derivative word has at most two preimages of length \(n\), one for each first bit; both are complements of each other. The derivative of any length-\(n\) factor of \(\mathbf u\) is a length-\(n-1\) factor of \(\mathbf d\). Consequently, for every \(n\ge2\),
\[
P_E(n)\le2P_R^{\mathbf d}(n-1),\qquad
C_{\mathbf d}(n-1)\le C_{\mathbf u}(n).
\]
The first inequality also holds trivially for odd \(n\), when \(P_E(n)=0\).

**3. Apply ordinary palindrome sparsity to the difference word.** Shallit's theorem states that for every infinite non-ultimately-periodic word \(\mathbf x\) over a finite alphabet,
\[
\frac{P_R^{\mathbf x}(m)\log(P_R^{\mathbf x}(m)+1)}{C_{\mathbf x}(m)}\longrightarrow0.
\]
It applies to \(\mathbf d\) by Step 1. Since \(\log(2a+1)\le2\log(a+1)\) for all \(a\ge0\), Step 2 yields
\[
0\le\frac{P_E(n)\log(P_E(n)+1)}{C_{\mathbf u}(n)}
\le4\frac{P_R^{\mathbf d}(n-1)\log(P_R^{\mathbf d}(n-1)+1)}{C_{\mathbf d}(n-1)}\longrightarrow0.
\]
Hence in particular \(P_E(n)/C_{\mathbf u}(n)\to0\). Directly applying the same Shallit theorem to \(\mathbf u\) also gives \(P_R^{\mathbf u}(n)/C_{\mathbf u}(n)\to0\).

**4. Count group orbits.** Suppose the factor language is invariant under \(H\). Burnside's orbit lemma gives
\[
C_H(n)=\frac14\bigl(C_{\mathbf u}(n)+P_R^{\mathbf u}(n)+P_E(n)+\operatorname{Fix}_C(n)\bigr).
\]
For every nonempty binary word, bitwise complementation fixes no word, so \(\operatorname{Fix}_C(n)=0\) for \(n\ge1\). Divide by \(C_{\mathbf u}(n)\) and apply Step 3. This proves the asserted limit without assuming existence in advance. \(\square\)

## Verification
The standalone script `check_antipalindromic_derivative.py` exhaustively verifies the derivative-palindrome implication, the factor-count inequalities for all binary finite words through length 11, and Burnside's orbit formula for all \(H\)-closures of finite factor sets through length 9. It additionally verifies both inequalities for finite prefixes of two classical morphic sequences. Its exact output is in `check_antipalindromic_derivative_output.txt`. These tests check the local identities only; the infinite limit follows from the symbolic reduction plus Shallit's published theorem.

## Relationship to prior work
Blažek, Dvořáková, and Pelantová, *Generalized reflection complexity* (2026), prove in Theorem 36 that for an aperiodic binary word whose language is \(H\)-invariant, **if** the ratio \(C_H(n)/C_{\mathbf u}(n)\) converges, then the limit is \(1/4\). Their Remark 37 explicitly identifies the missing antipalindromic sparsity estimate as the obstruction to removing this hypothesis. The present deduction establishes that missing estimate and hence unconditional convergence. Their Burnside formula and their earlier group-complexity theory are used as prior results.

Shallit, *Palindrome complexity versus factor complexity* (2026), proves the strong bound for **ordinary** palindromes in every non-ultimately-periodic infinite word. The additional observation here is that antipalindromes of a binary word are controlled by ordinary palindromes of its XOR first-difference word, whose non-ultimate periodicity and factor complexity are preserved sufficiently for Shallit's theorem to apply. The older group-symmetry inequality of Pelantová and Starosta (2013) is acknowledged; it bounds adjacent palindromic complexities but does not itself assert unconditional limit convergence.

## Limitations
The conclusion is for binary words and the four-element group generated by reversal and bit-complementation; no analogous result for arbitrary alphabet involutions or other finite symmetry groups is asserted. The ratio theorem assumes invariance of the complete factor language under \(H\), not merely an approximate closure property. The estimate is asymptotic and provides no uniform finite-length convergence rate. The result relies on the published infinite-word palindrome-sparsity theorem; finite computations are corroboration only. No independent validation has been performed.

## References
1. Adam Blažek, Lubomíra Dvořáková, Edita Pelantová, *Generalized reflection complexity*, arXiv:2610.14637v1 (first posted 2026-10-10), particularly Lemma 22, Theorem 36, and Remark 37. https://arxiv.org/html/2610.14637v1
2. Jeffrey Shallit, *Palindrome complexity versus factor complexity*, arXiv:2606.08127v3 (first posted 2026-06-06), particularly Theorem 4. https://arxiv.org/html/2606.08127v3
3. Edita Pelantová, Štěpán Starosta, *Languages invariant under more symmetries: overlapping factors versus palindromic richness*, Discrete Mathematics 313 (2013), 2432–2445; arXiv:1103.4051. https://arxiv.org/abs/1103.4051
