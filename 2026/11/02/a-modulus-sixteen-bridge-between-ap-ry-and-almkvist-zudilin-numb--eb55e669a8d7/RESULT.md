# A modulus-sixteen bridge between Apéry and Almkvist–Zudilin numbers

## Finding

For every integer \(n\geq0\), define the Apéry numbers and the signed Almkvist–Zudilin numbers, respectively, by
\[
A(n)=\sum_{k=0}^{n}\binom nk^2\binom{n+k}{k}^2,
\qquad
B(n)=\sum_{k=0}^{\lfloor n/3\rfloor}
(-3)^{n-3k}\binom n{3k}\binom{n+k}{k}\binom{2k}k\binom{3k}k.
\]
Let \(\beta(n)\) count maximal blocks of identical digits in the standard binary expansion of \(n\), and set \(\beta(0)=0\). Then
\[
\boxed{B(n)\equiv A(n)+8n\equiv1+4\beta(n)+8n\pmod{16}.}
\]
Thus their generating series satisfy \(\sum_{n\geq0}(B(n)-A(n))x^n\equiv 8x/(1-x)^2\pmod{16}\). In particular \(B(n)\bmod16\) is not eventually periodic. For the alternate normalized sequence \(Z(n)=(-1)^nB(n)\), the equivalent formula is \(Z(n)\equiv(-1)^n(1+4\beta(n)+8n)\pmod{16}\), and its residues are also not eventually periodic.

The Apéry block formula and the mod-eight periodicity of Almkvist–Zudilin numbers were known. The claimed contribution is the *cross-sequence coefficientwise congruence at modulus sixteen*, its resulting binary formula for the Almkvist–Zudilin sequence, and the consequent sharp transition from periodicity modulo eight to nonperiodicity modulo sixteen.

## Assumptions and scope

All indices are arbitrary nonnegative integers. We use ordinary integer binomial coefficients with \(\binom ab=0\) when \(b>a\geq0\). Write the binary expansion \(n=\sum_{j\geq0}b_j2^j\), with \(b_j\in\{0,1\}\) and all but finitely many \(b_j\) zero. Let \(s_2(n)=\sum_j b_j\). The congruences are in \(\mathbb Z/16\mathbb Z\), and no analytic convergence or prime-size hypothesis is needed.

## Proof

**1. The Apéry side.** The binomial identity
\[
\binom nk\binom{n+k}{k}=\binom{n+k}{2k}\binom{2k}k
\]
and Legendre's formula \(\nu_2\bigl(\binom{2k}k\bigr)=s_2(k)\) imply that in \(A(n)\bmod16\), every positive index \(k\) with at least two one-bits contributes zero. For \(k=2^j\), the squared central binomial coefficient equals \(4\pmod{16}\); hence
\[
A(n)\equiv1+4\sum_{j\geq0}\binom{n+2^j}{2^{j+1}}\pmod{16}.
\]
Lucas's parity criterion identifies this binomial coefficient modulo two with \(b_j\oplus b_{j+1}\), where \(\oplus\) denotes exclusive-or. Consequently
\[
A(n)\equiv1+4\sum_{j\geq0}(b_j\oplus b_{j+1})
=1+4\beta(n)\pmod{16}.
\]
This formula was already established by Rowland and Yassawi; the argument is included so the comparison is self-contained.

**2. A known alternative expansion for the other sequence.** Chan and Zudilin, Corollary 4.3, equivalently Sun's equation (5.2), established the integer identity
\[
B(n)=\sum_{k=0}^n(-27)^{n-k}
\binom{n+3k}{4k}\binom{2k}k^{\!2}\binom{4k}{2k}.
\]
Put \(M_k=\binom{2k}k^2\binom{4k}{2k}=(4k)!/(k!)^4\). Legendre's formula gives the exact valuation
\[
\nu_2(M_k)=3s_2(k).
\]
Therefore, modulo sixteen only \(k=0\) and \(k=2^j\) survive. Since \(M_{2^j}/8\) and \((-27)^{n-2^j}\) are odd for eligible indices,
\[
B(n)\equiv(-27)^n+8\sum_{j\geq0}
\binom{n+3\cdot2^j}{2^{j+2}}\pmod{16}.
\]
(The binomial coefficient vanishes if \(2^j>n\).) As \(-27\equiv5\pmod{16}\) and \(5^n\equiv1+4n\pmod{16}\), this is
\[
B(n)\equiv1+4n+8H(n)\pmod{16},\quad
H(n)=\sum_{j\geq0}\binom{n+3\cdot2^j}{2^{j+2}}\pmod2.
\]

**3. The binary carry identity.** Lucas's theorem identifies the summand defining \(H(n)\) with bit \(j+2\) of \(n+3\cdot2^j\). Since \(3\cdot2^j\) adds ones at positions \(j,j+1\), this bit is
\[
b_{j+2}\oplus(b_j\lor b_{j+1}),
\]
where \(\lor\) is Boolean or. Put \(Q=\sum_{j\geq0}b_jb_{j+1}\) and \(s=s_2(n)\). Summing modulo two and using \(a\lor b=a+b-ab\) on binary digits yields
\[
H(n)\equiv s+b_1+Q\pmod2.
\]
On the other hand, the number of binary blocks is exactly
\[
\beta(n)=\sum_{j\geq0}(b_j\oplus b_{j+1})
=2s-b_0-2Q.
\]
Since \(n\equiv b_0+2b_1\pmod4\), the integer \((n+\beta(n))/2\) satisfies
\[
\frac{n+\beta(n)}2\equiv s+b_1-Q\equiv H(n)\pmod2.
\]
Thus \(2H(n)\equiv n+\beta(n)\pmod4\), and substitution gives
\[
B(n)\equiv1+4n+4(n+\beta(n))
=1+4\beta(n)+8n\equiv A(n)+8n\pmod{16}.
\]
All sums over binary positions are finite, including at \(n=0\).

**4. Non-eventual periodicity.** Suppose \(B(n)\bmod16\) had eventual period \(d\geq1\). Write \(d=2^tm\) with \(m\) odd, choose \(r\geq\max(1,t)\) and \(s\geq1\) with \(2^s\equiv1\pmod m\) (any \(s\geq1\) if \(m=1\)), and put \(a=2^r(2^s-1)\). This is an even multiple of \(d\) with binary block count \(\beta(a)=2\). For arbitrarily large \(k>r+s+1\), let \(n=2^k\). Then \(\beta(n)=2\) and \(\beta(n+a)=4\), while both indices are even. The proved congruence gives \(B(n)\equiv9\pmod{16}\) but \(B(n+a)\equiv1\pmod{16}\). Since any multiple of an eventual period is also an eventual period on the same tail, this is a contradiction. Multiplication by the periodic sign \((-1)^n\) cannot turn a non-eventually-periodic residue sequence into an eventually periodic one; the same holds for \(Z(n)\).

## Verification

The standalone `verify.py` uses only the Python standard library. It compares the two independently coded integer binomial representations for \(B(n)\), evaluates \(A(n)\) by its defining sum, and checks the theorem for every \(0\leq n\leq256\). Separately, it tests the binary-carry identity for every \(0\leq n<100000\) and constructs explicit conflicting-period witnesses for candidate periods \(1\leq d\leq512\). Execute `python3 verify.py`. Exact arithmetic is used throughout. These finite tests check the implementation but are not offered as proofs of an infinite assertion.

## Relationship to prior work

Chan and Zudilin (2010), Corollary 4.3, already prove the second binomial representation for the Almkvist–Zudilin sequence; their Theorem 2.2 gives algebraic transformations linking Apéry-like generating functions. Sun (2013), equation (5.2), reproduces that representation. Neither fact is claimed as new. Rowland and Yassawi (2013), Theorems 3.28–3.29, already give the exact \(A(n)\bmod16\) binary-block formula and its nonperiodicity. Malik and Straub (2015), Theorem 5.3, establish the Almkvist–Zudilin mod-eight periodicity. These earlier results are essential premises, but none of the inspected statements specifies the coefficientwise modulus-sixteen difference \(B(n)-A(n)\), the \(B(n)\bmod16\) block formula, or its nonperiodicity. In particular, an exact generating-function transformation does not itself present or simplify the coefficientwise congruence; the two valuation filtrations and the binary-carry identity yield the explicit relationship here.

## Limitations

The result is specific to modulus sixteen and these two normalization-sensitive Apéry-like sequences. It does not classify their difference modulo higher powers of two. Earlier work establishes a stronger general algebraic connection between generating functions; the claimed contribution is the explicit same-index modular comparison, not that underlying relation. Priority assessment is limited by potentially unlocated equivalent binary congruences; independent mathematical audit has not been carried out.

## References

1. H. H. Chan and W. Zudilin, *New representations for Apéry-like sequences*, Mathematika 56 (2010), 107–117, DOI: 10.1112/S0025579309000436. Open full text: https://mrc.sdu.edu.cn/ziliao/60.pdf. See Theorem 2.2 and Corollary 4.3.
2. Z.-H. Sun, *Congruences for Domb and Almkvist-Zudilin numbers*, arXiv:1302.1715 (first posted 2013-02-07). https://arxiv.org/abs/1302.1715. See definition (1.3) and equation (5.2).
3. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635 (first posted 2013-10-31). https://arxiv.org/abs/1310.8635. See Theorems 3.28–3.29.
4. A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297 (first posted 2015-08-03). https://arxiv.org/abs/1508.00297. See Theorem 5.3.
5. J.-C. Liu, *On the binomial transforms of Apéry-like sequences*, arXiv:2406.18059 (first posted 2024-06-26). https://arxiv.org/abs/2406.18059. See the main theorems on individual-sequence congruences to exponential powers.
