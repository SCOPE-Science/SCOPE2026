# Exact dyadic abelian complexity and Fibonacci growth of the Baum–Sweet word

## Finding

Write \(b=b(0)b(1)\cdots\) for the Baum–Sweet binary word, with \(b(0)=1\), and for \(n\geq1\), \(b(n)=1\) if and only if every maximal run of zeros in the ordinary binary representation of \(n\) has even length. For any \(n\geq1\), let \(M(n)\) be the largest number of ones among all contiguous factors of \(b\) having length \(n\), and let \(\psi_b(n)\) be the number of distinct Parikh vectors of those factors. Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\).

**Theorem.** For every integer \(k\geq0\),
\[
M(2^k)=\sum_{i=0}^{2^k-1}b(i)=F_{k+2},\qquad
\psi_b(2^k)=F_{k+2}+1.
\]
In other words, the initial length-\(2^k\) factor maximizes the number of ones over *every* shifted factor of the same length; every integer one-count between zero and this maximum occurs. More generally, with \(\varphi=(1+\sqrt5)/2\),
\[
\psi_b(n)=\Theta\!\left(n^{\log_2\varphi}\right),\qquad
\lim_{n\to\infty}\frac{\log\psi_b(n)}{\log n}=\log_2\varphi.
\]
The asymptotic statement holds over all positive integer lengths, whereas the displayed exact Fibonacci formula is asserted only at dyadic lengths.

## Assumptions and scope

A factor of a one-sided infinite word means \(b(i)\cdots b(i+n-1)\) for some \(i\geq0\). A binary Parikh vector consists of its numbers of zeros and ones. Thus two factors of the same length have the same Parikh vector precisely when they contain the same number of ones. The convention \(b(0)=1\) is essential and is fixed throughout. All Fibonacci indices are nonnegative and all asymptotic implicit constants are absolute.

## Proof

**1. A four-state presentation.** Use the uniform substitution and coding
\[
\sigma(A)=AB,\quad \sigma(B)=CB,\quad \sigma(C)=BD,\quad \sigma(D)=DD,
\qquad
\tau(A)=\tau(B)=1,\quad\tau(C)=\tau(D)=0.
\]
Because \(\sigma(A)\) begins in \(A\), the infinite fixed point \(y=\sigma^\omega(A)\) exists. Its coded word is exactly \(b=\tau(y)\). For completeness, let \(u(n)=\tau(y_n)\). The two entries of \(\sigma(s)\) give transitions \(\delta(s,0)\) and \(\delta(s,1)\). Checking the four states gives, for all \(n\geq0\),
\[
u(2n+1)=u(n),\qquad u(4n)=u(n),\qquad u(4n+2)=0,\qquad u(0)=1.
\]
The digit-definition word satisfies the same identities: appending a binary one leaves all earlier zero-run lengths unchanged, appending two zeros preserves parity of the final run, and appending exactly one zero followed by one has an odd terminal zero-run. Equivalently, the identities may be checked separately according to the number of terminal zeros before the append. They determine every term inductively and hence \(u=b\).

**2. Coordinatewise block domination.** For \(X\in\{A,B,C,D\}\), write \(X_k=\tau(\sigma^k(X))\), a binary word of length \(L=2^k\). Concatenation of the substitution images gives
\[
A_{k+1}=A_kB_k,\quad B_{k+1}=C_kB_k,\quad
C_{k+1}=B_kD_k,\quad D_{k+1}=D_kD_k.
\]
At level zero, \(A_0=B_0=1\) and \(C_0=D_0=0\). Induction on these four identities shows \(D_k=0^L\) and \(A_k=B_k+C_k\) **coordinatewise over the ordinary integers**. Indeed, if these hold at level \(k\), then the coordinatewise sum of \(B_{k+1}\) and \(C_{k+1}\) is \((C_k+B_k)(B_k+D_k)=A_kB_k=A_{k+1}\), with no coordinate exceeding one. Consequently, \(B_k\), \(C_k\), and \(D_k\) are each coordinatewise at most \(A_k\).

Since \(y=\sigma^k(y)\), every aligned binary block of length \(L\) in \(b\), starting at a position divisible by \(L\), is one of \(A_k,B_k,C_k,D_k\). Fix any starting position \(i=Lq+r\), where \(0\leq r<L\). The length-\(L\) factor beginning at \(i\) consists of the suffix of an aligned block at coordinates \(r,\ldots,L-1\), followed by the prefix of the following aligned block at coordinates \(0,\ldots,r-1\). Coordinatewise domination bounds its number of ones by the number in \(A_k[r:L]A_k[0:r]\). This is a cyclic rotation of \(A_k\), and therefore has exactly \(|A_k|_1\) ones. The first \(L\) symbols of \(b\) are precisely \(A_k\), so equality is attained. Hence \(M(2^k)=|A_k|_1\) for all \(k\geq0\).

**3. Fibonacci count.** Set \(a_k=|A_k|_1\), \(c_k=|C_k|_1\), and \(d_k=|D_k|_1=0\). The block identities give
\[
a_{k+1}=a_k+|B_k|_1,\qquad |B_{k+1}|_1=|C_k|_1+|B_k|_1=a_k.
\]
Thus \(a_{k+2}=a_{k+1}+a_k\). Since \(a_0=1\) and \(a_1=2\), \(a_k=F_{k+2}\). This proves the maximum-one-count identity.

**4. Complete Parikh spectra.** The letter \(D\) occurs in \(y\): it appears in \(\sigma^3(A)=ABCBBDCB\). As \(\sigma^j(D)=D^{2^j}\), the coded word \(b\) contains arbitrarily long contiguous zero factors. Hence the minimum number of ones in length-\(n\) factors is zero for each \(n\geq1\). The one-count of a length-\(n\) sliding window changes by at most one when its start advances by one position. Starting at a factor with \(M(n)\) ones and moving to a sufficiently distant all-zero factor, every integer between \(0\) and \(M(n)\) must occur. Therefore \(\psi_b(n)=M(n)+1\), in particular \(\psi_b(2^k)=F_{k+2}+1\).

**5. Growth for every length.** The function \(M(n)\) is nondecreasing: a factor achieving the maximum at length \(n\) can be extended to its right to length \(n+1\), without decreasing its number of ones. If \(2^k\leq n<2^{k+1}\), then
\[
F_{k+2}+1\leq\psi_b(n)\leq F_{k+3}+1.
\]
The elementary Fibonacci asymptotic \(F_j=\Theta(\varphi^j)\) and \(2^k\leq n<2^{k+1}\) imply \(\psi_b(n)=\Theta(n^{\log_2\varphi})\). Taking logarithms gives the asserted limit. This completes the proof.

## Verification

The included `verify.py` is an independent finite consistency check of the digit definition, substitution blocks, the coordinatewise domination identity, Fibonacci prefix weights, every window in a large prefix at sixteen dyadic lengths, and every Parikh vector at thirteen smaller dyadic lengths. Execute `python3 verify.py` with Python 3.9 or later. The recorded output was:

`VERIFY_OK digit_positions=131072 substitution_levels=17 dyadic_window_cases=2097153 full_parikh_levels=13 last_maximum=2584`

These finite experiments are **not** the proof of the infinitely quantified assertions; the preceding substitution induction is the proof.

## Relationship to prior work

Merta's 2018 study of Baum–Sweet-related words establishes the arithmetic recurrence, zero-run unboundedness, and Fibonacci-related descriptions of positions with value one, but its statements do not bound the number of ones in *every shifted factor* of a fixed dyadic length. Cicalese–Lipták–Rossi (2018) show the general relationship between abelian complexity and extremal one-counts and study infinite prefix-normal words; those general identities do not determine the Baum–Sweet-specific extremal counts. The substitution presentation is classical, rather than newly claimed. The contribution here is the coordinatewise domination of every substitution block by the initial block, producing exact dyadic maximum weights, all dyadic Parikh spectra, and the global exponent. The novelty comparison remains subject to possible unindexed equivalent work.

## Limitations

No exact expression for \(\psi_b(n)\) at arbitrary nondyadic \(n\) is asserted, and dyadic prefix-normality is not generalized here to unrestricted lengths. The computer check covers finitely many symbols and does not establish the infinite identities. Prior-literature searches cannot rule out all undiscovered equivalent formulations. The statement uses a fixed zero-index convention \(b(0)=1\).

## References

1. Ł. Merta, *Composition inverses of the variations of the Baum–Sweet sequence*, arXiv:1803.00292v1 (first publicly posted 2018-03-01), https://arxiv.org/abs/1803.00292 .
2. F. Cicalese, Z. Lipták, and M. Rossi, *On Infinite Prefix Normal Words*, arXiv:1811.06273v1 (first publicly posted 2018-11-15), https://arxiv.org/abs/1811.06273 .
3. J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), discussion of the Baum–Sweet morphism.
