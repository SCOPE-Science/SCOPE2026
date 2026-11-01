# A modulo-\(16\) correction and sparse modulo-\(8\) spectrum for support-based odd mex over overpartitions

## Finding

For every integer \(n\ge1\), let \(\mathcal O(n)\) be the set of overpartitions of \(n\). For an overpartition \(\lambda\), let \(m_o(\lambda)\) be the **least positive odd integer that is absent from its complete part support**, whether ordinary or overlined. Define
\[
F(n)=\sum_{\lambda\in\mathcal O(n)}m_o(\lambda),\qquad
\overline p(n)=|\mathcal O(n)|.
\]
Then, writing \(N=n-1\),
\[
\boxed{F(n)-\overline p(n)\equiv 4+8\left(\lfloor\sqrt N\rfloor-N-\lfloor N/3\rfloor\right)\pmod{16}.}
\]
In particular, the residue of the difference modulo \(16\) is **always exactly \(4\) or \(12\)**, and each occurs for infinitely many values of \(n\).

The resulting **complete modulo-\(8\) spectrum** of \(F\) for \(n\ge1\) is
\[
\boxed{F(n)\equiv\begin{cases}
6\pmod 8,&n=k^2\text{ with }k\text{ odd},\\
2\pmod 8,&n=k^2\text{ with }k\text{ even},\\
0\pmod 8,&n=2k^2\text{ with }k\ge1,\\
4\pmod 8,&\text{otherwise},
\end{cases}}
\]
where all square roots \(k\) are positive integers. The cases are disjoint. If \(X\) is a positive integer, put \(s=\lfloor\sqrt X\rfloor\) and \(t=\lfloor\sqrt{X/2}\rfloor\). Among \(1\le n\le X\), the exact frequencies of residues \(6,2,0,4\), respectively, are
\[
\left\lceil\frac s2\right\rceil,\qquad\left\lfloor\frac s2\right\rfloor,\qquad t,\qquad X-s-t.
\]
Thus \(F(n)\equiv4\pmod8\) on a set of natural density one.

## Assumptions and scope

All congruences are coefficientwise integer congruences. An overpartition allows the first occurrence of any distinct size to be overlined. Here presence means presence **in either form**; this convention is not interchangeable with the convention that ignores overlined parts. The empty overpartition has \(F(0)=\overline p(0)=1\), so the displayed difference formula is asserted only for \(n\ge1\). The result covers all positive integers without an unproved hypothesis.

## Proof

**Step 1: overlining orbits.** Remove all overlines from an overpartition to obtain an ordinary partition \(\pi\). If \(d(\pi)\) is the number of distinct positive part sizes of \(\pi\), there are exactly \(2^{d(\pi)}\) ways of overlining its distinct first occurrences, and each has the same support-based odd mex \(m_o(\pi)\). Consequently
\[
F(n)-\overline p(n)=\sum_{\pi\vdash n}2^{d(\pi)}\bigl(m_o(\pi)-1\bigr).
\]
The parenthesized difference is even. If \(\pi\) has at least three distinct part sizes, its contribution is therefore divisible by \(16\). If \(1\) is absent, then \(m_o(\pi)=1\) and the contribution is zero. The sole one-distinct-size partition containing \(1\) is \(1+\cdots+1\) (\(n\) copies), whose contribution is \(2(3-1)=4\). Every two-distinct-size partition containing \(1\) has the form \(1^a m^b\), with integers \(a,b\ge1\) and \(m\ge2\). When \(m=3\), its odd mex is \(5\), yielding \(4(5-1)=16\), which vanishes modulo \(16\). For every other \(m\), its odd mex is \(3\) and its contribution is \(4(3-1)=8\). Therefore
\[
F(n)-\overline p(n)\equiv4+8T(n)\pmod{16},\qquad
T(n)=\sum_{\substack{2\le m\le n-1\\m\ne3}}\left\lfloor\frac{n-1}{m}\right\rfloor.
\]
No partition shape has been omitted: the cases exhaust the possibilities according to presence of \(1\) and the number of distinct sizes.

**Step 2: divisor-parity collapse.** Set \(N=n-1\), and let \(d(k)\) denote the number of positive divisors of \(k\). Double counting divisor pairs gives
\[
\sum_{m=1}^{N}\left\lfloor\frac Nm\right\rfloor=\sum_{k=1}^{N}d(k).
\]
Since divisors pair except at squares, \(d(k)\equiv1\pmod2\) precisely when \(k\) is a square. Thus
\[
T(n)\equiv\lfloor\sqrt N\rfloor-N-\lfloor N/3\rfloor\pmod2.
\]
Substituting establishes the modulo-\(16\) formula. For infinitely many \(n\), select \(N\equiv0\pmod3\) inside each interval \([k^2,(k+1)^2)\). For all sufficiently large \(k\), such an \(N\) exists; on these choices, the correction parity equals \(k\pmod2\). Alternating \(k\) proves that both \(4\) and \(12\) occur infinitely often.

**Step 3: the modulo-\(8\) coefficients of the overpartition series.** The classical overpartition generating function is
\[
P(q)=\sum_{n\ge0}\overline p(n)q^n=\prod_{j\ge1}\frac{1+q^j}{1-q^j}.
\]
Jacobi's triple-product identity gives the formal power-series inverse
\[
P(q)^{-1}=\sum_{k\in\mathbb Z}(-1)^kq^{k^2}=1+2S(q),\qquad
S(q)=\sum_{k\ge1}(-1)^kq^{k^2}.
\]
Hence in \(\mathbb Z[[q]]/8\mathbb Z[[q]]\),
\[
P(q)\equiv1-2S(q)+4S(q)^2.
\]
In characteristic two, the square of a series has only doubled exponents, giving
\[
S(q)^2\equiv\sum_{k\ge1}q^{2k^2}\pmod2.
\]
Thus for positive \(n\), the coefficients \(\overline p(n)\) are congruent modulo \(8\) to \(2\) for odd squares, \(6\) for even squares, \(4\) for twice a positive square, and \(0\) otherwise. Positive squares and twice squares cannot coincide. Reduction of Step 2 modulo \(8\) gives \(F(n)\equiv\overline p(n)+4\pmod8\). This proves the four-way formula. Counting odd and even positive square roots at most \(s\) and square roots of twice squares at most \(t\) yields the exact frequencies.

## Verification

The accompanying standalone `verify.py` constructs the overpartition product in exact modular arithmetic and, independently, the odd-mex sector generating functions. It checks the exact modulo-\(16\) formula for every degree \(0\le n\le1024\), including the special value at zero, and the four-way modulo-\(8\) classification over the same range. It also enumerates every ordinary partition for \(0\le n\le23\), weights each by its exact \(2^{d(\pi)}\) overlining multiplicity, and checks both generating-function sequences. These computations are finite checks; the preceding proof is the justification for all \(n\).

## Relationship to prior work

Veena V. S. and S. N. Fathima (2026) study the sum of odd minimal excludants over overpartitions, including modulo-\(4\) coefficient congruences and modulo-\(8\) statements about a self-convolution. The currently accessible abstract does not state this support-convention modulo-\(16\) correction or the full coefficientwise modulo-\(8\) spectrum. Its full text was not available for comparison, and the precise convention must be checked before declaring priority. Indeed, the abstract's stated modulo-\(4\) square condition differs from the support convention at \(n=1\); this is a **comparison limitation**, not an allegation of error in the paper.

Judy Ann Donato (2025) explicitly distinguishes the overlined-only, nonoverlined-only, and complete-support notions of overpartition mex; her inspected paper studies the unrestricted smallest missing integer rather than its odd-restricted counterpart. Dhar, Mukhopadhyay, and Sarma (2024) study an odd mex on overpartitions **into odd parts**, a different ambient class. Their definitions and generating-series sections were consulted. The Jacobi identity and divisor-parity argument are classical and are not claimed as new.

## Limitations

The result does not assert that a broader, unindexed theorem cannot imply these formulas, nor does it provide independent priority certification. Full-text access to the closely related September 2026 paper was unavailable; only its bibliographic record and abstract could be compared. The theorem depends on the explicitly stated support convention; it should not be transferred to a nonoverlined-only odd-mex definition.

## References

1. Veena V. S. and S. N. Fathima, *On the sum of odd minimal excludants over overpartitions*, arXiv:2609.32207 (first posted 2026-09-26), https://arxiv.org/abs/2609.32207.
2. Judy Ann L. Donato, *On Minimal Excludant over Overpartitions*, arXiv:2507.04402 (first posted 2025-07-06), https://arxiv.org/abs/2507.04402.
3. Aritram Dhar, Avi Mukhopadhyay, and Rishabh Sarma, *On new minimal excludants of overpartitions related to some \(q\)-series of Ramanujan*, arXiv:2409.06121 (first posted 2024-09-10), https://arxiv.org/abs/2409.06121.
4. Jacobi's triple-product identity (classical); divisor pairing in elementary number theory (classical).
