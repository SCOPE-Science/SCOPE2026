# Three exact 2-adic image balls for the even-trace Lucas sequence with negative recurrence term

## Finding
Let \(P\in4\mathbb Z\setminus\{0\}\), set \(h=\nu_2(P)\ge2\), and define the integral Lucas sequence
\[
U_0=0,\qquad U_1=1,\qquad U_{n+2}=P U_{n+1}-U_n\quad(n\ge0).
\]
The set of its values has the following **complete 2-adic closure**:
\[
\boxed{\overline{\{U_n:n\ge0\}}=2^h\mathbb Z_2\ \sqcup\ (1+2^{2h}\mathbb Z_2)\ \sqcup\ (-1+2^{2h}\mathbb Z_2).}
\]
For every \(N\ge1\), define \(R_N=\{U_n\bmod2^N:n\ge0\}\). Then
\[
\boxed{|R_N|=2^{\max(0,N-h)}+\min(2,2^{N-1})\,2^{\max(0,N-2h)}.}
\]
The limiting residue proportion, also the Haar measure of the closure, is
\[
\boxed{\lim_{N\to\infty}\frac{|R_N|}{2^N}=2^{-h}+2^{1-2h}.}
\]
For example, this proportion is \(3/8\) when \(P=4\), and \(5/32\) when \(P=8\). These fractions hold at every sufficiently large power of two, not merely asymptotically.

## Assumptions and scope
The parameter \(P\) can be positive or negative but is nonzero and divisible by \(4\). Every index is an integer \(n\ge0\). The characteristic polynomial is \(X^2-PX+1\), so the second recurrence term is **subtracted**; the related recurrence with a plus sign is a different family. The valuation \(\nu_2(x)\) is the exponent of two in a nonzero integer \(x\). All closures and balls are taken in the ring of 2-adic integers \(\mathbb Z_2\). The three displayed balls are disjoint because \(h\ge2\).

## Proof
**Step 1: Companion identities and valuations.** Introduce the companion Lucas sequence
\[
V_0=2,\quad V_1=P,\quad V_{n+2}=P V_{n+1}-V_n.
\]
The standard polynomial identities (obtainable directly by induction from these recurrences) are
\[
U_{2j}=U_jV_j,\qquad V_{2j}=V_j^2-2,\qquad V_{2j+1}=V_jV_{j+1}-P.
\]
Moreover, for nonnegative \(m>n\) of the same parity, one has
\[
U_m-U_n=U_{(m-n)/2}V_{(m+n)/2}.
\]
This last identity holds for integer \(P\) including repeated-root cases, since it is a polynomial identity; it may be established first from the characteristic-root formula at distinct roots and then by polynomial identity, or by direct induction. Here \(|P|\ge4\), so the characteristic roots are distinct.

Because \(P\) is even, the recurrence modulo two gives \(U_{2j+1}\) odd and every \(V_j\) even. The doubling identity gives
\[
V_{2j}=V_j^2-2\equiv2\pmod4,
\]
including \(j=0\), so \(\nu_2(V_{2j})=1\). In \(V_{2j+1}=V_jV_{j+1}-P\), one of \(j,j+1\) is even and one odd. By strong induction starting at \(V_1=P\), the product term is divisible by \(2^{h+1}\), and consequently the odd-indexed companion terms have valuation \(h\). An explicit induction avoids circularity: assuming \(\nu_2(V_{2i+1})=h\) through index \(2j-1\), the two factors \(V_j,V_{j+1}\) have indices at most \(2j\), with even-indexed valuation one, and the odd factor valuation \(h\). Thus
\[
\nu_2(V_{2j})=1,\qquad \nu_2(V_{2j+1})=h.
\]
Iterating \(U_{2j}=U_jV_j\) through the two-adic factorization of \(j\) now yields, for every \(j\ge1\),
\[
\nu_2(U_{2j})=h+\nu_2(j).
\]

**Step 2: Three exact index isometries.** Apply the same-parity difference formula. For distinct nonnegative integers \(a,b\), the parity of \(a-b\) equals that of \(a+b\). If they are odd, \(U_{a-b}\) is odd and \(V_{a+b}\) has valuation \(h\). If even, their valuations add as \(h+\nu_2(a-b)-1+1\). Therefore
\[
\nu_2(U_{2a}-U_{2b})=h+\nu_2(a-b).
\]
For the indices \(4a+1\) and \(4b+1\), their half-difference is \(2(a-b)\), and their half-sum is \(2(a+b)+1\), which is odd. The even-index valuation formula and odd-index companion valuation yield
\[
\nu_2(U_{4a+1}-U_{4b+1})=2h+\nu_2(a-b).
\]
Identically,
\[
\nu_2(U_{4a+3}-U_{4b+3})=2h+\nu_2(a-b).
\]
Since \(U_0=0\), \(U_1=1\) and \(U_3=P^2-1\), all even-index terms lie in \(2^h\mathbb Z_2\), all first odd-branch terms in \(1+2^{2h}\mathbb Z_2\), and all second odd-branch terms in \(-1+2^{2h}\mathbb Z_2\).

**Step 3: Surjectivity in each ball.** The maps on nonnegative indices
\[
a\longmapsto U_{2a}/2^h,\qquad
 a\longmapsto(U_{4a+1}-1)/2^{2h},\qquad
 a\longmapsto(U_{4a+3}+1)/2^{2h}
\]
are integral-valued, and Step 2 says that they all preserve the exact 2-adic distance \(2^{-\nu_2(a-b)}\). For every positive \(k\), the inputs \(0,1,\ldots,2^k-1\) therefore produce pairwise distinct residues modulo \(2^k\). There are precisely \(2^k\) such residues, so each normalized image is **surjective modulo every power of two**. Its image is consequently dense in \(\mathbb Z_2\), and its unique extension from dense nonnegative integers to \(\mathbb Z_2\) is a bijective isometry. This proves that the closure contains each whole displayed ball. Step 2 excludes every other value.

**Step 4: Exact residue count and density.** A ball \(c+2^r\mathbb Z_2\) occupies precisely \(2^{\max(0,N-r)}\) residue classes modulo \(2^N\). The even ball is disjoint from the odd balls at every positive precision. The two odd balls coincide modulo two but are distinct modulo four and all higher powers. Hence their combined count is \(\min(2,2^{N-1})2^{\max(0,N-2h)}\), yielding the formula for \(R_N\). Division by \(2^N\) and passage to the limit prove the density formula.

## Verification
The standalone `VERIFY.py` checks exact finite-level images against direct modular recurrence periods for twelve positive/negative parameters \(P\), with \(1\le N\le11\). It independently checks the claimed valuation-isometry laws using unrestricted integer recurrence arithmetic. The actual recorded execution passes 132 complete modular image comparisons, 13,904 modular recurrence states, and 25,308 valuation-isometry comparisons. The executable is not used as an infinite proof: the four argument steps above establish all quantifiers.

## Relationship to prior work
De Clercq et al. [1, Theorem 5] characterize Lucas sequences whose initial powers-of-two blocks are complete residue systems. For the present recurrence coefficient conventions their favorable trace condition is \(P\equiv2\pmod4\), not \(P\equiv0\pmod4\). Our restriction to \(4\mid P\) lies on the *excluded side* of that boundary. The identity \(U_{2a}(P)=P\,U_a(P^2-2)\), where \(P^2-2\equiv2\pmod4\), shows that the *even-indexed ball alone* also follows from their dyadic permutation theorem after squaring the characteristic roots. This reduction is acknowledged as covered; the odd-indexed image balls and full union are not settled by it. Their result does not provide the exact three-ball image or density in the excluded regime. Ferrari, Luca and Moree [2] develop discriminators for Shallit sequences with trace \(4k+2\); they do not establish the present divisibility-by-four classification. Bragman and Rowland [3] analyze Fibonacci residue density for the plus-sign recurrence, not this one. Sanna [4] and Accossato–Sanna [5] study which numbers of residues can arise when the modulus and/or initial conditions vary, rather than all residue images at dyadic precision for this fixed normalized family. None of these inspected statements yields the displayed three-ball theorem by direct implication. The companion identities themselves are standard and are not claimed as original.

## Limitations
Originality is assessed against the cited and searched literature, not mathematically proven by failed searches. The classification is restricted to negative second recurrence term, nonzero \(P\) divisible by four, the prime two, and the canonical initial conditions. It does not classify discriminators, arbitrary modulus, or other Lucas initial conditions. The finite verifier checks examples; it does not certify the infinite argument. Independent scientific validation has not been performed.

## References
1. A. de Clercq, F. Luca, L. Martirosyan, M. Matthis, P. Moree, M. A. Stoumen, M. Weiß, *Binary recurrences for which powers of two are discriminating moduli*, J. Integer Sequences 23 (2020), Article 20.11.3; original preprint dated 2020-03-03, https://arxiv.org/abs/2003.01559 .
2. M. Ferrari, F. Luca, P. Moree, *On the discriminator of Lucas sequences. II*, original arXiv submission dated 2023-09-22, https://arxiv.org/abs/2309.12843 .
3. N. Bragman, E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, original arXiv submission dated 2022-02-01, https://arxiv.org/abs/2202.00704 .
4. C. Sanna, *On the number of residues of linear recurrences*, arXiv:2109.05734 (2021-09-13), https://arxiv.org/abs/2109.05734 .
5. F. Accossato, C. Sanna, *On the number of residues of certain second-order linear recurrences*, arXiv:2401.07661 (2024-01-15), https://arxiv.org/abs/2401.07661 .
