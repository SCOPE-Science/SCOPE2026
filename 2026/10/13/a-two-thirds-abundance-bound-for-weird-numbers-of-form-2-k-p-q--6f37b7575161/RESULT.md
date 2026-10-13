# A two-thirds abundance bound for weird numbers of form \(2^k p q\)
## Finding
Let \(k\ge1\) and let \(p<q\) be distinct odd primes. If \(n=2^k p q\) is weird, set
\[
M=2^{k+1}-1,\qquad a=\sigma(n)-2n.
\]
Then
\[
\boxed{M<a<\frac23 M^2+M.}
\]
In particular, the previously known universal upper bound \(a<\frac34M^2+M\) can be replaced by a strictly smaller coefficient \(2/3\), uniformly for all exponents \(k\ge1\).

## Assumptions and scope
Here \(\sigma(n)\) is the positive-divisor sum. An integer is *weird* if it is abundant (\(\sigma(n)>2n\)) but is not a sum of distinct proper divisors. Every prime variable in the theorem is an ordinary positive prime; there is no cutoff on \(p\), \(q\), or \(k\).

The classical necessary conditions for this family, established by Iannucci, include \(M<p<2M\) and \(a>M\). Put \(x=p-M\), \(y=q-M\), so \(x\) is even and \(2\le x<M\). Multiplicativity gives
\[
a=M(p+1)-xq=M(M+1)-xy.
\]
Every integer between \(0\) and \(M=1+2+\cdots+2^k\) is a sum of distinct powers of two among \(1,2,\ldots,2^k\). Consequently, any representation
\[
a=r+sp+tq,\qquad 0\le r,s,t\le M
\]
provides a subset of distinct proper divisors with sum \(a\); its complement among all proper divisors sums to \(n\), contradicting weirdness. Thus such a representation is impossible. Conversely, no equivalence is needed below: only this obstruction is used.

## Proof
First observe that \(a<Mp\), since
\[
a=Mp+M-xq<Mp+M-2p<Mp.
\]
We derive two restrictions from the absence of a bounded representation of \(a\).

**Lemma 1 (the larger prime is beyond twice the binary scale).** Every weird \(2^k p q\) as above has \(q>2M\).

Suppose instead \(q\le2M\). Write \(q=p+d\), where \(d\ge2\) is even and \(d\le M-x<M\). Then
\[
a=p(2M-p-d)+M(d+1).
\]
Euclidean division gives
\[
u=\left\lfloor\frac{M(d+1)}p\right\rfloor,\quad
r=M(d+1)-up,\quad
\ell=2M-p-d+u=M-x-d+u,
\]
with \(0\le r<p\) and \(a=\ell p+r\). Because \(p<2M\) and \(d\) is even, \(u\ge d/2\). Moreover \(u\le d\), and \(d\le M-x\); thus \(0\le\ell\le M-1\). The key exact identity is
\[
\ell d-(r-M)=u(p+d)-d(x+d)
\ge \frac d2(M-x-d)\ge0.
\]
If \(r\le M\), we already have \(a=r+\ell p\). Otherwise take \(T=\lceil(r-M)/d\rceil\). The inequality above guarantees \(1\le T\le\ell\), and \(d<M\) guarantees \(0\le r-Td\le M\). Therefore
\[
a=(r-Td)+(\ell-T)p+Tq,
\]
with all coefficients between zero and \(M\), a contradiction. Hence \(q>2M\).

**Lemma 2 (residue packing).** Every such weird integer has
\[
a<(x-1)q.
\]
Otherwise for each integer \(0\le t\le x-1\), \(b_t=a-tq\) is nonnegative and less than \(Mp\). Its quotient \(s_t=\lfloor b_t/p\rfloor\) therefore belongs to \([0,M-1]\). As \(q\) and \(p\) are distinct primes, the \(x\) residues \(b_t\bmod p\) are pairwise distinct: their index differences are strictly between zero and \(p\). But only \(p-(M+1)=x-1\) residues modulo \(p\) lie outside \(\{0,1,\ldots,M\}\). At least one residue \(r_t\) lies in that set. This yields the prohibited equality \(a=r_t+s_tp+tq\). The lemma follows.

We now split by \(x\). If \(x\ge M/3\), Lemma 1 gives
\[
a=M(p+1)-xq<M(M+x+1)-2Mx=M(M+1-x)
\le\frac23M^2+M.
\]
If \(x<M/3\), Lemma 2 gives \(M(p+1)-xq<(x-1)q\), hence \(q>M(p+1)/(2x-1)\). It follows that
\[
a<\frac{x-1}{2x-1}M(p+1)
<\frac12 M(M+x+1)
<\frac23 M^2+\frac12 M
<\frac23 M^2+M.
\]
Every case is strict. Combined with Iannucci's lower bound \(a>M\), this proves the theorem. \(\square\)

## Verification
A standalone script `verify.py` recomputes the bounded-divisor representation obstruction for all candidate odd-prime pairs in the first eight binary exponents. It reproduces the published counts \(1,1,5,3,10,23,29,53\) and tests the strict new inequality and \(q>2M\) for all found weird integers. It reports `VERIFY_OK candidate_pairs=29490` on successful replay. This is finite corroboration; the universal assertion rests on the proof, not an extrapolation.

## Relationship to prior work
Iannucci (2015, arXiv:1504.02761v1) derives the abundance identity, necessary conditions, and a criterion for avoiding proper-divisor subset representations, and conjectures \(a<(M+1)(M+2)/3\). A later published result, *A uniform three-quarter abundance bound for weird numbers of form \(2^k p q\)* (2026), proves \(a<\frac34M^2+M\). That inequality does **not** imply the stronger \(\frac23\)-coefficient estimate here. Our argument adds the paired prime-scale exclusion and a two-regime application of residue packing. The new result remains weaker than Iannucci's conjecture and makes no assertion about the conjecture's resolution.

## Limitations
Neither the coefficient \(2/3\) nor the threshold of Lemma 1 is claimed to be optimal; no existence or infinitude of new weird-number families follows. The proof is confined to \(2^k p q\) with distinct odd primes. A differently phrased unindexed prior inequality might predate this argument; the originality assessment reflects the inspected literature and database comparisons, not a proof of global uniqueness.

## References
1. D. E. Iannucci, “On primitive weird numbers of the form \(2^k p q\),” arXiv:1504.02761v1, first public 7 April 2015, https://arxiv.org/abs/1504.02761.
2. “A uniform three-quarter abundance bound for weird numbers of form \(2^k p q\),” published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-uniform-three-quarter-abundance-bound-for-weird-numbers-of-for--b810d8b66c9f.
3. G. Melfi, “On the conditional infiniteness of primitive weird numbers,” *Journal of Number Theory* 147 (2015), 508–514, https://doi.org/10.1016/j.jnt.2014.07.024.
