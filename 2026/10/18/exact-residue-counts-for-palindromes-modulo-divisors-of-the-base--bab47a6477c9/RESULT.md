# Exact residue counts for palindromes modulo divisors of the base plus one

## Finding

Fix integers \(b\ge2\) and \(q\ge2\) with \(q\mid b+1\). For each integer length \(L\ge1\) and residue \(0\le r<q\), let \(N_{b,q}(L,r)\) count positive integers with exactly \(L\) base-\(b\) digits, palindromic canonical digit expansions, and residue \(r\pmod q\). Define \(\delta_q(r,s)=1\) when \(r\equiv s\pmod q\) and zero otherwise, and \(\varepsilon_q=1\) for even \(q\) and zero for odd \(q\).

For one-digit palindromes, the exact counts are
\[
N_{b,q}(1,r)=\frac{b+1}{q}-\delta_q(r,0)-\delta_q(r,-1).
\]
For each integer \(k\ge1\), all even-length palindromes lie in residue zero, exactly:
\[
N_{b,q}(2k,r)=(b-1)b^{k-1}\delta_q(r,0).
\]
For each integer \(k\ge1\), the **complete odd-length law** is
\[
\boxed{N_{b,q}(2k+1,r)=\frac{(b-1)b^k+\varepsilon_q(-1)^r(b-1)b^{k-1}}{q}
+(-1)^{k+1}\left[\delta_q(r,1)+\delta_q(r,-1)-\frac2q+\frac{2\varepsilon_q(-1)^r}{q}\right].}
\]
In particular, the absolute discrepancy from the first fractional term on the right is **strictly less than one**, for every allowed \(b,q,k,r\). Consequently, for a uniformly chosen exact-length odd palindrome, the limiting residue distribution as \(k\to\infty\) is
\[
\lim_{k\to\infty}\frac{N_{b,q}(2k+1,r)}{(b-1)b^k}
=\frac{1+\varepsilon_q(-1)^r/b}{q}.
\]
Thus odd moduli give uniform limiting residues; for even moduli a persistent, explicit parity bias remains. All assertions include composite moduli.

## Assumptions and scope

Digits are taken in \(\{0,1,\ldots,b-1\}\), and the first digit of a canonical expansion is nonzero. Exactly \((b-1)b^k\) palindromes have \(2k+1\) digits. The condition \(q\mid b+1\) is essential: the result is not asserted for arbitrary moduli. The notation \((-1)^r\) uses the canonical residue \(0\le r<q\); when \(q\) is odd, it is multiplied by zero and causes no ambiguity. The one-digit formula is stated separately from the odd-length formula for \(k\ge1\).

## Proof

Write the digits of an odd palindrome, from outside to center, as \(d_0,\ldots,d_k\), where \(1\le d_0<b\) and \(0\le d_j<b\) for \(1\le j\le k\). As \(b\equiv-1\pmod q\), the palindrome's residue is
\[
n\equiv 2\sum_{j=0}^{k-1}(-1)^j d_j+(-1)^k d_k\pmod q.
\]
The corresponding even-length residue is zero because its paired digit positions have opposite parities. Counting free leading and interior digits gives the even-length formula. Counting the digits \(1\le d_0<b\) in each residue class gives the one-digit formula: \(b+1\) is divisible by \(q\), and the digits omit residues \(0\) and \(-1\) from a complete set of \((b+1)/q\) periods.

For the odd case put \(\zeta=\exp(2\pi i/q)\), and define the finite Fourier sum \(F(h)=\sum_n\zeta^{hn}\), over exactly the palindromes under consideration, for \(0\le h<q\). The zero frequency is \(F(0)=(b-1)b^k\). If \(q\) is even, the frequency \(h=q/2\) satisfies \(\zeta^h=-1\); since \(b\) is odd, every paired digit contributes phase one, while the central digits have alternating signs and sum to one. Therefore
\[
F(q/2)=(b-1)b^{k-1}.
\]

For every other nonzero frequency set \(z=\zeta^h\), so \(z^2\ne1\). Since \(z^q=1\) and \(b\equiv-1\pmod q\), the geometric sums obey
\[
\sum_{a=0}^{b-1}z^{2sa}=-z^{-2s},\qquad
\sum_{a=0}^{b-1}z^{sa}=-z^{-s}\quad(s\in\{-1,1\}),
\]
and the leading-digit sum is \(\sum_{a=1}^{b-1}z^{2a}=-(1+z^{-2})\). Multiplying the independent-digit factors and using
\[
-2\sum_{j=1}^{k-1}(-1)^j-(-1)^k=1
\]
(which holds for both parities of \(k\)), we obtain the **length-independent nonexceptional Fourier spectrum**
\[
F(h)=(-1)^{k+1}(z+z^{-1}).
\]

Fourier inversion gives \(N_{b,q}(2k+1,r)=q^{-1}\sum_{h=0}^{q-1}F(h)\zeta^{-hr}\). The identity
\[
\sum_{h=0}^{q-1}(\zeta^{h}+\zeta^{-h})\zeta^{-hr}
=q\big(\delta_q(r,1)+\delta_q(r,-1)\big)
\]
permits replacing the nonexceptional frequency sum by the complete sum, subtracting the zero frequency's contribution \(2\) and, when \(q\) is even, subtracting the exceptional term \(-2(-1)^r\). Inserting \(F(0)\) and \(F(q/2)\) proves the displayed exact odd-length formula.

Finally, let \(B_q(r)=\delta_q(r,1)+\delta_q(r,-1)-2/q+2\varepsilon_q(-1)^r/q\). For odd \(q\ge3\), the only possible values are \(1-2/q\) and \(-2/q\). For \(q=2\), the value is zero. For even \(q\ge4\), the value is zero at even residues, \(1-4/q\) at residues \(\pm1\), and \(-4/q\) at remaining odd residues (if any). In all cases \(|B_q(r)|<1\). Dividing the exact count by \((b-1)b^k\) and letting \(k\to\infty\) proves the limiting distribution.

## Verification

The provided standalone script `verify.py` independently enumerates all canonical palindromes for bases \(2\le b\le14\), all divisors \(q\ge2\) of \(b+1\), and all lengths from one through seven. It compares residue counts against the formula using exact rational arithmetic, and checks that the counts are integers, their sum equals the exact population, and the discrepancy is strictly below one. The script makes no external requests and needs only Python's standard library. Execute `python verify.py`. Finite testing is corroborative, not the proof of the universal statement.

For example, for base ten and modulus eleven, exact five-digit counts are \(81\) in residues \(1\) and \(10\), and \(82\) in the other nine residues. This is an instance of the exact result, not an assumption.

## Relationship to prior work

Banks, Hart, and Sakata [1] established congruence distribution estimates for palindromes when the modulus is coprime to \(b(b^2-1)\); their hypothesis excludes every modulus treated here. Col [2] refined distribution estimates: his main Theorems 1 and 2 require that coprimality hypothesis, but his later sieve Lemma 22 does analyze selected factors of \(b+1\) for special averaged zero-residue counts. Those results do not state the complete fixed-odd-length, all-residue formula or the strict unit discrepancy proved here. Onphaeng and collaborators [3] derived exact arithmetic-progression counts in the regimes \(b\equiv0,1\pmod q\) (Theorems 7 onward). The present setting \(b\equiv-1\pmod q\) is distinct for \(q>2\); the \(q=2\) case is not claimed novel independently. The classical fact that even-digit palindromes are divisible by \(b+1\) is likewise not claimed novel. The new object of comparison is the full odd-length residue-count formula, including its two exceptional Fourier frequencies and its parity-biased limit. Related recurrence/digit-sum formulas may yield the result as an unstated special consequence; equivalence to all unpublished or unindexed work is not excluded.

## Limitations

This is a fixed-length result for moduli dividing \(b+1\), not a distribution theorem for arbitrary moduli or arbitrary truncation bounds. No claim is made about simultaneous congruence constraints, primes among palindromes, or independent verification. Known special cases such as modulus two and even-length divisibility are contextual rather than new. The novelty comparison covered specified published sources and search results, not the entire mathematical literature.

## References

[1] W. D. Banks, D. N. Hart, M. Sakata, *Almost All Palindromes Are Composite*, arXiv:math/0405056v1, 2004-05-04; https://arxiv.org/abs/math/0405056.

[2] S. Col, *Palindromes dans les progressions arithmétiques*, Acta Arithmetica 137 (2009), 1–41, doi:10.4064/aa137-1-1; https://www.impan.pl/shop/en/publication/transaction/download/product/83451.

[3] K. Onphaeng, P. N. Phunphayap, T. Khemaratchatakumthorn, P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8; https://cs.uwaterloo.ca/journals/JIS/VOL27/Phunphayap/phun7.pdf.
