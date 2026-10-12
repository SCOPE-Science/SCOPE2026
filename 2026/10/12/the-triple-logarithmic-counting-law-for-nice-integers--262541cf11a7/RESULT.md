# The triple-logarithmic counting law for nice integers

## Finding
For each integer \(n\ge2\), call \(n\) **nice** if for every divisor \(d\mid n\) with \(d>1\), a residue class \(a_d\pmod d\) can be chosen such that whenever two chosen congruences have a simultaneous integer solution, their moduli are coprime. **There is no requirement that the union of the classes cover the integers.** Set
\[
N(x)=\#\{n\in\mathbb Z:2\le n\le x,\ n\text{ is nice}\}.
\]
The asymptotic number of nice integers is
\[
\boxed{N(x)\sim \frac{e^{-\gamma}x}{\log\log\log x}},\qquad x\longrightarrow\infty,
\]
where \(\gamma\) is the Euler–Mascheroni constant and every logarithm is natural. Consequently, nice integers have natural density zero, despite having an explicit, much larger-than-power-saving first-order count.

## Assumptions and scope
The assertion holds unconditionally for arbitrary real \(x\to\infty\); no congruence or prime-factor-support restriction is imposed. For the proof we take \(x\) sufficiently large that \(L=\log\log x>8\). Write \(P^-(n)\) for the least prime divisor of \(n\ge2\), and \(\omega(n)\) for its number of *distinct* prime divisors, with \(\omega(1)=0\).

We use the published equivalence [1, 2]
\[
n\text{ is nice}\quad\Longleftrightarrow\quad
\omega\!\left(\frac{n}{P^-(n)}\right)<P^-(n),\qquad n\ge2.
\tag{1}
\]
Adenwalla proved necessity and Jia–Li–Liu proved sufficiency. This is an external, explicitly identified input. The new contribution is the quantitative counting law with its leading constant. Other classical inputs are the prime harmonic sum and Mertens product theorems, whose uses are specified below.

## Proof
**1. A concentration estimate with explicit scale.** Put \(L=\log\log x\), \(z=x^{1/3}\), and
\[
W_z(n)=\sum_{p\le z}\mathbf 1_{p\mid n},\qquad A_z=\sum_{p\le z}\frac1p.
\]
At most two distinct prime divisors of an integer \(n\le x\) exceed \(x^{1/3}\), hence
\[
W_z(n)\le\omega(n)\le W_z(n)+2.
\tag{2}
\]
By the prime harmonic sum theorem,
\(A_z=\log\log z+O(1)=L+O(1)\). Expanding the square and using
\(\sum_{n\le x}\mathbf 1_{d\mid n}=\lfloor x/d\rfloor\) gives
\[
\begin{aligned}
\frac1{\lfloor x\rfloor}\sum_{n\le x}(W_z(n)-A_z)^2
&=\sum_{p\le z}\left(\frac1p-\frac1{p^2}\right)
+O\!\left(\frac{\pi(z)^2+A_z\pi(z)+1}{x}\right)\\
&=O(L).
\end{aligned}
\tag{3}
\]
Indeed, diagonal prime terms contribute \(\lfloor x/p\rfloor\), off-diagonal pairs contribute \(2\lfloor x/(pq)\rfloor\), and replacing every floor by its real argument costs at most \(O(\pi(z)^2)\) in total. Since \(\pi(z)\le z=x^{1/3}\), the normalized error is negligible. From (2), (3), and Chebyshev's inequality, for sufficiently large \(x\),
\[
E(x):=\#\left\{1\le n\le x:\left|\omega(n)-L\right|>\frac L4\right\}=O\!\left(\frac{x}{L}\right).
\tag{4}
\]
This is a quantitative normal-order estimate, proved here with elementary second moments; no probabilistic independence assumption is made.

**2. A two-sided rough-integer sandwich.** For any real \(y\ge2\), let
\[
R_y(x)=\#\{1\le n\le x:\text{no prime }p\le y\text{ divides }n\}.
\]
Set \(y_-=L/2\), \(y_+=2L\). Suppose \(n\) is nice and \(P^-(n)\le y_-\). By (1), since \(\omega(n)\le\\\(\\omega(n/P^-(n))\\)+1\),
\[
\omega(n)\le P^-(n)\le L/2.
\]
Such an \(n\) lies in the exceptional set counted in (4). Conversely, if \(P^-(n)>y_+\) and \(\omega(n)\le2L\), then
\[
\\\(\\omega(n/P^-(n))\\)\le\omega(n)\le2L<P^-(n),
\]
so \(n\) is nice by (1). The integers with \(\omega(n)>2L\) also lie in (4). Accounting for the exceptional integer \(n=1\), the two implications give
\[
R_{2L}(x)-E(x)-1\ \le\ N(x)\ \le\ R_{L/2}(x)+E(x).
\tag{5}
\]

**3. Uniform evaluation of the two rough counts.** Let \(Q_y=\prod_{p\le y}p\). Inclusion–exclusion, with no asymptotic sieve remainder hidden, gives
\[
\begin{aligned}
R_y(x)&=\sum_{d\mid Q_y}\mu(d)\left\lfloor\frac xd\right\rfloor\\
&=x\prod_{p\le y}\left(1-\frac1p\right)+O\!\left(2^{\pi(y)}\right).
\end{aligned}
\tag{6}
\]
For either \(y=L/2\) or \(y=2L\), the elementary bound \(\pi(y)\le y\) implies
\(2^{\pi(y)}\le2^{2L}=(\log x)^{2\log 2}=o(x/\log L)\).
Mertens' product theorem supplies
\[
\prod_{p\le y}\left(1-\frac1p\right)
\sim\frac{e^{-\gamma}}{\log y}
\sim\frac{e^{-\gamma}}{\log L}
\qquad(y=L/2\text{ or }2L).
\tag{7}
\]
Because \(x/L=o(x/\log L)\), the exceptional term (4) is negligible relative to (6)–(7). The two bounds in (5) thus both have the same leading term \(e^{-\gamma}x/\log L\). The asserted asymptotic follows since \(\log L=\log\log\log x\). \(\square\)

## Verification
Run the standalone Python 3 program `nice_integers_verifier.py` without third-party dependencies. It constructs the least-prime-divisor and distinct-prime-factor-count arrays through \(2{,}000{,}000\), compares both with independent elementary factorizations through \(2{,}000\), and directly checks the existence or nonexistence of compatible residue-class assignments for each \(2\le n\le36\), without using the published criterion inside the backtracking search. It then reports the exact counts, concentration exceptions, and two rough-count bounds at four finite cutoffs. Its replay output is in `nice_integers_verification_output.txt`.

These finite tests check definitions, arithmetic, and the logical inclusions; they do **not** prove the asymptotic. The infinite proof is the calculation (1)–(7), relying on the stated published classification and classical prime-distribution theorems.

## Relationship to prior work
Adenwalla [1] defined the relevant non-overlap property, proved its necessary prime-factor obstruction, and studied the density **of residue classes covered by a fixed congruence system**. Jia–Li–Liu [2] proved the converse prime-factor criterion and gave explicit constructions. Neither of the inspected primary papers gives the asymptotic count \(N(x)\). Their theorems establish the arithmetic characterization, but not the new prevalence theorem or the Euler–Mascheroni leading constant. The needed analytic ingredients (second moments, inclusion–exclusion, and Mertens' theorems) are classical; the application and the precise counting statement concern the new naturally characterized integer class.

## Limitations
The result gives the leading asymptotic only, not a secondary term or an effective numerical error bound at accessible cutoffs. Convergence is exceptionally slow because of the triple logarithm. No claim is made about genuine covering systems, which are ruled out by [1]. The combinatorial equivalence (1) is taken from [1, 2], not independently reproved here; the remaining asymptotic proof is self-contained modulo the specified classical prime theorems. Unindexed or unpublished equivalent counting results cannot be excluded by a finite literature search.

## References
[1] Sarosh Adenwalla, *A Question of Erdős and Graham on Covering Systems*, arXiv:2501.15170, first public version 25 January 2025. https://arxiv.org/abs/2501.15170

[2] Zhengkun Jia, Huixi Li and Yushuo Liu, *Resolving Adenwalla's conjecture related to a question of Erdős and Graham about covering systems*, arXiv:2504.09579, first public version 13 April 2025; current revised text used for the constructive theorem. https://arxiv.org/abs/2504.09579

[3] Mertens' prime harmonic sum and prime-product theorems; classical results used in (3) and (7).
