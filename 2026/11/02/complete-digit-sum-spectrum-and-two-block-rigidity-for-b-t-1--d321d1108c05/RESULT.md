# Complete digit-sum spectrum and two-block rigidity for \(b^t-1\)

## Finding

Fix integers \(b\ge2\) and \(t\ge1\), and put \(M=b^t-1\). Write \(s_b(n)\) for the sum of the base-\(b\) digits of a nonnegative integer \(n\). The complete spectrum of digit sums of *positive* multiples of \(M\) is
\[
\boxed{\{s_b(N):N\in\mathbb Z_{>0},\ M\mid N\}=
\{k(b-1):k\in\mathbb Z,\ k\ge t\}.}
\]

There is also a sharp length threshold. Every positive multiple \(N<b^{2t}\) of \(M\) has digit sum in the **two-element set**
\[
\{t(b-1),\ 2t(b-1)\},
\]
and both values occur below \(b^{2t}\). For every \(t\ge2\) and \(1\le r<t\), the smallest possible number of base-\(b\) digits of a positive multiple of \(M\) having sum \((t+r)(b-1)\) is **exactly** \(2t+1\).

In base two this says that the binary weights of positive multiples of \(2^t-1\) are exactly the integers \(t,t+1,t+2,\ldots\), with the first intermediate weights \(t+1,\ldots,2t-1\) requiring \(2t+1\) binary digits.

## Assumptions and scope

All variables are integers unless stated otherwise. The base is \(b\ge2\), the exponent is \(t\ge1\), and digit sums refer to the *ordinary, unsigned* base-\(b\) expansion, with no leading zeros counted as significant digits. The divisibility condition uses positive integers \(N\); zero is excluded. For \(t=1\), there are no intermediate values in the length-threshold assertion.

## Proof

**Lower bound and congruence.** Since \(b\equiv1\pmod{b-1}\), every \(N\) satisfies \(s_b(N)\equiv N\pmod{b-1}\). As \(b-1\mid M\), the digit sum of every multiple of \(M\) is a positive multiple of \(b-1\).

For the lower bound, start with any positive multiple \(S\) of \(M\). If \(S\ge b^t\), write \(S=Qb^t+R\), where \(Q\ge1\) and \(0\le R<b^t\), and replace it by \(T(S)=Q+R\). This operation preserves the residue modulo \(M\), since \(b^t\equiv1\pmod M\). Moreover, \(T(S)>0\), \(T(S)<S\), and
\[
s_b(T(S))=s_b(Q+R)\le s_b(Q)+s_b(R)=s_b(S).
\]
The inequality is the elementary subadditivity of digit sums under addition, obtained by carrying. Repeating the operation terminates with a positive multiple \(S'\) of \(M\) below \(b^t=M+1\), necessarily \(S'=M\). Thus \(s_b(S)\ge s_b(M)=t(b-1)\).

**Constructing all admissible sums.** Put \(W_0=M\). For each \(1\le r<t\), set
\[
W_r=M(b^t+b^r+1)=b^{2t}+b^{t+r}-b^r-1.
\]
Since
\[
b^{t+r}-b^r-1=(b^t-2)b^r+(b^r-1),
\]
the two terms on the right have disjoint base-\(b\) digit supports. The digits of \(b^t-2\) have sum \(t(b-1)-1\) and the digits of \(b^r-1\) have sum \(r(b-1)\). Adding the leading digit at exponent \(2t\) gives
\[
s_b(W_r)=(t+r)(b-1),\qquad 1\le r<t.
\]
The formula also holds for \(r=0\) with \(W_0=M\). Every integer \(k\ge t\) can be written uniquely as \(k=t+r+qt\), with \(q\ge0\) and \(0\le r<t\). Define
\[
N=W_r+M\sum_{j=1}^{q}b^{3tj}.
\]
The summands have pairwise disjoint digit supports: \(W_r<b^{2t+1}\), while the translated copies of \(M\) occupy positions from \(3tj\) through \(3tj+t-1\). Consequently \(M\mid N\) and
\[
s_b(N)=s_b(W_r)+q\,s_b(M)=(t+r+qt)(b-1)=k(b-1).
\]
This establishes the spectrum in both directions.

**Two-block rigidity.** Let \(0<N<b^{2t}\) and \(M\mid N\). Write \(N=Ab^t+B\), with \(0\le A,B\le M\). Then \(M\mid A+B\), while \(0<A+B\le2M\). Therefore \(A+B=M\) or \(A+B=2M\). In the first case \(B=M-A\) is the digitwise base-\(b\) complement of the \(t\)-digit (zero-padded) representation of \(A\); hence \(s_b(N)=s_b(A)+s_b(B)=t(b-1)\). In the second case \(A=B=M\), giving \(s_b(N)=2t(b-1)\). Both are attained, respectively by \(M\) and \(M(b^t+1)=b^{2t}-1\).

For \(1\le r<t\), the intermediate value \((t+r)(b-1)\) is thus impossible below \(b^{2t}\), and \(W_r\) lies in the interval \([b^{2t},b^{2t+1})\) while attaining it. Its shortest possible base-\(b\) length is exactly \(2t+1\). This completes the proof.

## Verification

A standalone exact-arithmetic verifier is supplied as `verify.py`. It checks 1,728 explicitly constructed weights across bases \(2\) through \(13\), exponents \(1\) through \(8\), residues and concatenation counts. It also checks 25,200 small multiples against the digit-sum lower bound and exhaustively enumerates all multiples below the two-block boundary for 16 parameter pairs. Its finite checks corroborate, but do not replace, the universal proof above.

## Relationship to prior work

Digit sums along arithmetic progressions are studied in Toumi's 2025 work, including its Remark 1.1 on first-hitting thresholds in progressions. The theorem here gives a complementary **exact finite first-hitting length** for the missing intermediate *integer-valued* digit sums, for every modulus of the form \(b^t-1\), together with the complete support for this modulus family; asymptotic residue-distribution estimates do not specify those finite boundary values.

Phunphayap, Noppakaew and Pongsriiam introduced the set of digit sums of multiples and proved the general congruence obstruction and concatenation inclusion. For \(M=b^t-1\), their results give the congruence restriction and sums divisible by \(t(b-1)\), but do not determine the sums \((t+r)(b-1)\) with \(1\le r<t\), nor the sharp \(2t+1\) threshold. Their preprint first appeared in March 2023, before its September 2025 journal publication; the preprint date is explicitly respected in this comparison.

The binary minimal-weight bound for multiples of \(2^t-1\) was previously known, and the specific lower bound for multiples of decimal \(99\) was previously discussed. Neither establishes the complete all-base spectrum or the two-block rigidity and attained shortest lengths. Work on *same-weight nontrivial multiples* addresses a different question.

## Limitations

This result applies only to the moduli \(b^t-1\), not to arbitrary moduli or general repunits \((b^t-1)/(b-1)\). It determines the shortest witness length only for the first intermediate digit sums; it does not minimize numerical value or length for every higher digit sum. Mathematical priority has not been independently audited, and equivalent statements may exist under other terminology.

## References

1. Nathan Toumi, *The level of distribution of the sum-of-digits function in arithmetic progressions*, arXiv:2504.02784 (first posted April 3, 2025), https://arxiv.org/abs/2504.02784 .
2. P. N. Phunphayap, P. Noppakaew and P. Pongsriiam, *Directed graphs of integers with arcs determined by an arithmetic function*, arXiv:2303.13017 (first posted March 23, 2023); *Utilitas Mathematica* 124 (2025), 101–114, https://doi.org/10.61091/um124-06 .
3. Christian Elsholtz, *Almost all primes have a multiple of small Hamming weight*, *Bulletin of the Australian Mathematical Society* 94 (2016), 224–235, https://doi.org/10.1017/S000497271600023X .
4. Cécile Dartyge, Florian Luca and Pantelimon Stănică, *On digit sums of multiples of an integer*, *Journal of Number Theory* 129 (2009), 2820–2830, https://doi.org/10.1016/j.jnt.2009.04.003 .
5. OEIS A000120, notes on binary weights of multiples of \(2^t-1\), https://oeis.org/A000120 .
