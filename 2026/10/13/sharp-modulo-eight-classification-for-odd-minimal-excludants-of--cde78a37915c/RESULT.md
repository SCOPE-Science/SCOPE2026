# Sharp modulo-eight classification for odd minimal excludants of overpartitions

## Finding
For an overpartition \(\lambda\), write \(\operatorname{mex}(\lambda)\) for the least positive integer absent from its parts, ignoring whether any parts are overlined. Let \(\operatorname{mex}_{o}(\lambda)\) equal this least missing part when odd and equal zero when even. Set
\[
F(n)=\sum_{\lambda\in\overline{\mathcal P}(n)}\operatorname{mex}_{o}(\lambda),\qquad F(0)=1.
\]
For every integer \(n\ge1\), define \(s=\lfloor\sqrt n\rfloor\), let \(I_{\square}(n)\) indicate positive perfect squares and \(I_{2\square}(n)\) indicate positive integers twice a square. Then
\[
\boxed{F(n)\equiv 2(-1)^n-2(-1)^s I_{\square}(n)
+4\left(I_{2\square}(n)+\lfloor\sqrt{n-1}\rfloor+\left\lfloor\frac{n-1}{2}\right\rfloor\right)\pmod8.}
\]
In particular, \(F(n)\equiv0\pmod8\) if and only if \(n\) is a positive perfect square. For nonsquares its residue is \(2\) or \(6\) modulo \(8\). The uniform square divisibility cannot be increased to \(16\): \(F(36)\equiv8\pmod{16}\).

## Assumptions and scope
This is an exact coefficient congruence for each integer \(n\ge1\), not an asymptotic or a finite-range observation. All manipulations below occur in formal power-series rings with integer coefficients; reduction modulo \(8\) is coefficientwise. The empty overpartition is assigned \(F(0)=1\), and the formula involving square roots is claimed only for positive \(n\). Parts are considered present regardless of overlining; imposing absence only among non-overlined parts defines a different statistic.

## Proof
Write \(\mathscr F(q)=\sum_{n\ge0}F(n)q^n\). The exact generating-function identity of Veena V. S. and S. N. Fathima [1, Theorem 1.1] is
\[
\mathscr F(q)=\frac1{\prod_{m\ge1}(1-q^m)}\sum_{j\ge0}
(2j+1)4^j q^{j(2j+1)}(1-q^{2j+1})\prod_{m\ge2j+2}(1+q^m).
\]
For modulo \(8\), all terms with \(j\ge2\) vanish because \(16\mid4^j\). The \(j=0\) term is \(G(q)=\prod_{m\ge2}(1+q^m)/(1-q^m)\). For \(j=1\), reducing the other factors modulo \(2\) gives
\[
\mathscr F(q)\equiv G(q)+\frac{4q^3}{(1-q)(1-q^2)}\pmod8. \tag{1}
\]
Introduce the integer-coefficient formal series
\[
A(q)=\frac{-q}{1+q}=\sum_{m\ge1}(-1)^m q^m,
\qquad S(q)=\sum_{k\ge1}(-1)^k q^{k^2}.
\]
Jacobi's triple-product identity gives
\[
1+2S(q)=\prod_{m\ge1}\frac{1-q^m}{1+q^m}.
\]
It follows that
\[
G(q)=\frac{1-q}{1+q}\frac1{1+2S(q)}
=(1+2A(q))(1+2S(q))^{-1}.
\]
The constant term of \(1+2S\) is one; its formal inverse exists. Expanding the geometric inverse modulo \(8\) yields the exact formal congruence
\[
G(q)\equiv1+2(A-S)+4(S^2-AS)\pmod8. \tag{2}
\]
In characteristic two, \(S(q)^2\equiv\sum_{k\ge1}q^{2k^2}\); consequently its coefficient at \(q^n\) modulo \(2\) is \(I_{2\square}(n)\). Similarly, the coefficient of \(AS\) modulo \(2\) counts positive \(k\) with \(k^2<n\), hence equals \(\lfloor\sqrt{n-1}\rfloor\pmod2\). Finally
\[
[q^n]\frac{q^3}{(1-q)(1-q^2)}=\left\lfloor\frac{n-1}{2}\right\rfloor
\qquad(n\ge1),
\]
with both sides zero at \(n=1,2\). Extracting coefficients from (1)--(2), using \([q^n]A=(-1)^n\) and \([q^n]S=(-1)^s I_{\square}(n)\), proves the displayed residue formula.

If \(n=k^2\), its first two terms cancel, \(I_{2\square}(n)=0\), and \(k-1+\lfloor(k^2-1)/2\rfloor\) is even: both addends are even for odd \(k\) and odd for even \(k\). Thus \(F(k^2)\equiv0\pmod8\). If \(n\) is not square, the first part equals \(2(-1)^n\) and the other part is divisible by \(4\), so the residue is one of \(2,6\) and never zero. This establishes the equivalence for all positive integers.

To certify sharpness, the independent finite coefficient calculations described next obtain \(F(36)\equiv56\pmod{64}\), in particular \(F(36)\equiv8\pmod{16}\). This uses an exact finite coefficient of a formal series, not asymptotic extrapolation.

## Verification
Run \(\texttt{python3 artifacts/verify.py}\), using only the Python standard library. The accompanying verifier reconstructs all coefficients \(F(0),\ldots,F(300)\) in two independent ways: direct first-missing-part overpartition generating factors and the full source generating series. It compares both exact residues modulo \(128\), checks the theorem's formula modulo \(8\) for every index, and verifies the exact \(n=36\) obstruction modulo \(16\). The captured output is embedded in \(\texttt{artifacts/verify_output.txt}\). These checks support finite reproducibility; the formal-series proof establishes the infinite theorem.

## Relationship to prior work
The preprint [1], first public 26 September 2026, introduces this exact odd-filtered overpartition mex statistic and proves its complete modulo-four square criterion (Theorem 1.4). It proves a separate congruence modulo eight for the **self-convolution** of the coefficients (Theorem 1.7), not their individual residues. Its exact generating function (Theorem 1.1) is the starting point here; the present coefficientwise residue-eight identity is obtained by retaining the first two summands and resolving an additional quadratic theta contribution.

The arithmetic sums in [2] and [3] use different overpartition mex conventions, while the unspecialized overpartition mex of [4] retains both odd and even excludants. Results on ordinary partitions' odd/even mex sums likewise concern a different summation domain. Thus the statement is not a restatement of their tables or congruences. Literature and database coverage remain subject to unindexed or inaccessible prior equivalent work.

## Limitations
No congruence modulo \(16\) for every index is asserted. In fact the uniform strengthening on squares fails at \(36\). The result concerns the odd-filtered mex by all-part presence only; other overpartition mex definitions are not interchangeable. Independence and external auditing are not claimed.

## References
[1] Veena V. S. and S. N. Fathima, *On the sum of odd minimal excludants over overpartitions*, arXiv:2609.32207v1 (26 September 2026), Theorems 1.1, 1.4, 1.7 and Sections 3--5, https://arxiv.org/abs/2609.32207.

[2] V. M. R. Aricheta and J. A. L. Donato, *Minimal Excludant over Overpartitions*, arXiv:2309.04398v1 (2023), https://arxiv.org/abs/2309.04398.

[3] A. Dhar, A. Mukhopadhyay and R. Sarma, *On new minimal excludants of overpartitions related to some q-series of Ramanujan*, arXiv:2409.06121 (2024), https://arxiv.org/abs/2409.06121.

[4] J. A. L. Donato, *On Minimal Excludant over Overpartitions*, arXiv:2507.04402v1 (2025), https://arxiv.org/abs/2507.04402.
