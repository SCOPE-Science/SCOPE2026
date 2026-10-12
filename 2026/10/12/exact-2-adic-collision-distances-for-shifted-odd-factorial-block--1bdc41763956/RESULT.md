# Exact 2-adic collision distances for shifted odd-factorial blocks

## Finding

For every integer \(e\ge 2\), put \(M=2^e\) and define the odd-block product
\[
P_e(A)=\prod_{\substack{1\le i<M\\i\text{ odd}}}(MA+i),\qquad A\in\mathbb Z.
\]
Write \(\nu_2\) for the exponent of two dividing a nonzero integer, with \(\nu_2(0)=+\infty\). For every pair of integers \(A,B\), the **exact valuation law** is
\[
\boxed{\nu_2(P_e(A)-P_e(B))=3e-2+\nu_2\bigl((A-B)(A+B+1)\bigr).}
\]
In particular, the integer-valued polynomial \(P_e\) has exactly the two collision mechanisms \(A=B\) and \(A=-B-1\). For every integer \(s\ge1\),
\[
P_e(A)\equiv P_e(B)\pmod{2^{3e-2+s}}
\quad\Longleftrightarrow\quad
B\equiv A\ \text{or}\ B\equiv -A-1\pmod{2^s}.
\]
Thus the induced map on residue classes modulo \(2^s\), with values reduced modulo \(2^{3e-2+s}\), has exactly \(2^{s-1}\) values and every value has exactly two preimages.

The same exact precision persists after powering: for every integer \(j\ge0\),
\[
\nu_2\bigl(P_e(A)^{2^j}-P_e(B)^{2^j}\bigr)
=3e-2+j+\nu_2\bigl((A-B)(A+B+1)\bigr).
\]
The case \(j=0\) is the displayed valuation law. This identifies all improvements beyond the published universal shifted-product congruence.

## Assumptions and scope

All products are finite, over all positive odd integers strictly below \(2^e\). The exponent \(e\) is an integer at least two; the shifts \(A,B\) may be any positive, negative, or zero integers; the precision \(s\) is a positive integer and the power exponent \(j\) is a nonnegative integer. Congruence classes for the fiber statement are taken modulo \(2^s\). The convention \(\nu_2(0)=+\infty\) handles equality without exceptions.

## Proof

**Step 1: pair the odd factors.** Put \(m=2^{e-2}\) and index the \(m\) odd integers strictly below \(2^{e-1}\) as \(i_r=2r+1\), \(0\le r<m\). Each \(i_r\) is paired with \(M-i_r\). Because the number of factors is even, the resulting identity has no sign ambiguity:
\[
P_e(A)=\prod_{r=0}^{m-1}\bigl(i_r(M-i_r)+M^2A(A+1)\bigr).
\]
Write \(c_r=i_r(M-i_r)\), which is odd, and \(G(T)=\prod_{r=0}^{m-1}(c_r+T)\). Hence \(P_e(A)=G(M^2A(A+1))\) and the symmetry \(P_e(A)=P_e(-A-1)\) is exact.

**Step 2: compute the first derivative's exact valuation.** Work in the ring of two-adic integers, where all \(c_r\) are invertible, and put \(f(r)=c_r^{-1}\). For \(0\le k<e-2\) and \(0\le r<2^k\), the shift \(i_{r+2^k}=i_r+2^{k+1}\) gives
\[
\begin{aligned}
c_{r+2^k}-c_r
&=2^{k+1}(M-2i_r)-2^{2k+2}\\
&\equiv0\pmod{2^{k+2}}.
\end{aligned}
\]
Both \(c_r\) are odd, so \(f(r+2^k)\equiv f(r)\pmod{2^{k+2}}\). With \(S_k=\sum_{r=0}^{2^k-1}f(r)\), this gives
\[
S_{k+1}=2S_k+2^{k+2}u_k,\quad u_k\in\mathbb Z_2.
\]
Since \(S_0=f(0)\) is odd, induction shows \(S_k\equiv2^k\pmod{2^{k+1}}\) for \(0\le k\le e-2\). (For \(e=2\), only the odd base case is needed.) Therefore
\[
\nu_2\left(\sum_{r=0}^{m-1}c_r^{-1}\right)=e-2,
\qquad
\nu_2(G'(0))=e-2,
\]
because \(G'(0)=G(0)\sum_r c_r^{-1}\) and \(G(0)\) is odd.

**Step 3: obtain the exact difference.** Set \(T_A=M^2A(A+1)\) and \(T_B=M^2B(B+1)\); both lie in \(2^{2e+1}\mathbb Z\). The difference quotient
\[
Q(A,B)=\frac{G(T_A)-G(T_B)}{T_A-T_B}
\]
is an integer polynomial in \(T_A,T_B\), even when \(T_A=T_B\) if defined by the polynomial divided-difference identity. Its constant term in those two variables is \(G'(0)\). Consequently
\[
Q(A,B)\equiv G'(0)\pmod{2^{2e+1}}
\]
and hence \(\nu_2(Q(A,B))=e-2\), since \(e-2<2e+1\). Now
\[
P_e(A)-P_e(B)=2^{2e}(A-B)(A+B+1)\,Q(A,B).
\]
Taking valuations proves the formula whenever the two factors are nonzero. When they vanish, the exact factorization proves equality, and the formula holds by the convention on \(\nu_2(0)\). It also shows these are the only integer collisions.

**Step 4: residues and powers.** The integers \(A-B\) and \(A+B+1\) have odd sum \(2A+1\); exactly one is even. Thus the valuation of their product is at least \(s\) if and only if one factor is divisible by \(2^s\), giving precisely the two stated residue classes. They are distinct modulo \(2^s\), since their difference is \(2A+1\), odd. Therefore the induced map has exactly \(2^{s-1}\) distinct values with fibers of size two.

Lastly, every \(P_e(A)\) is odd, and for any nontrivial pair \(P_e(A)-P_e(B)\) has valuation at least \(3e-1\ge5\). Thus \(P_e(A)\equiv P_e(B)\pmod 4\), so their sum has valuation exactly one. The usual difference-of-squares identity, applied repeatedly, raises the difference valuation by exactly one at each squaring. This gives the \(2^j\)-power formula; equal pairs remain equal.

## Verification

Run `python3 verify.py` using the included Python standard-library script. It directly forms the odd products with signed integer shifts, checks two-adic valuations and exact reflections, and independently checks the induced modular fibers and first two power lifts. The saved output in `verify_output.txt` records 2,048 exact nontrivial pair comparisons, 264 equalities, 224 direct power comparisons, 576 additional modular comparisons, and 2,032 modular fiber memberships. The theorem for all integer parameters is established by the proof, not by these finite tests.

## Relationship to prior work

Davis's 2025 preprint, published as *Some 2-adic Integers Related to the Odd Part of \(2^e!\)*, proves (Theorem 16) that \(P_e(A)\equiv P_e(0)\pmod{2^{3e-1}}\) for every integer shift. Its Corollary 17 deduces congruences modulo \(2^{3e-1+j}\) between arbitrary \(2^j\)-th powers of two shifted products. These are uniform **lower bounds** for the two-adic difference valuations. The present result gives the **exact pairwise valuations** for every shift pair, including all extra powers beyond the uniform modulus, and completely classifies the residue fibers. Davis's coefficient lemmas share important arithmetic ingredients, but his stated theorem and corollary do not give the exact collision law or fiber classification.

Earlier work of Davis on limits of unit parts of factorials and OEIS A359349 provides context for these 2-adic block products, not a stated exact finite-block pairwise valuation law.

## Limitations

This is an arithmetic theorem only for shifts by multiples of \(2^e\) of the complete positive odd block below \(2^e\); it does not address truncated blocks, odd primes, or fractional shifts. It does not establish a general formula for arbitrary products or higher-order derivatives. An equivalent result may exist in unindexed literature or as an unstated derivation from known 2-adic factorial identities. No independent audit has been performed.

## References

1. Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of \(2^e!\)*, arXiv:2510.22078, first posted October 24, 2025; *Journal of Integer Sequences* 29 (2026), Article 26.3.1, Theorem 16, Corollary 17, Lemmas 18–19. https://arxiv.org/abs/2510.22078 ; https://cs.uwaterloo.ca/journals/JIS/VOL29/Davis/davis9.pdf
2. Donald M. Davis, *Binomial Coefficients Involving Infinite Powers of Primes*, *American Mathematical Monthly* 121 (2014), 734–737; arXiv:1301.6285. https://arxiv.org/abs/1301.6285
3. OEIS Foundation, A359349, odd parts of factorials of powers of two. https://oeis.org/A359349
