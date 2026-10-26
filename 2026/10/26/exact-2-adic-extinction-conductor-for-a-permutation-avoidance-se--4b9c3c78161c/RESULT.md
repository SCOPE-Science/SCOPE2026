# Exact 2-adic extinction conductor for a permutation-avoidance sequence

## Finding
Let \(a_n\) count permutations of \(\{1,\ldots,n\}\) avoiding both \(1342\) and \(2143\), with \(a_0=1\). Let \(s_2(u)\) be the binary digit sum of a nonnegative integer. For every integer \(\alpha\ge1\), define
\[
K_\alpha=\max\{k\in\{0,\ldots,\alpha-1\}:k+s_2(k+1)-1<\alpha\},\qquad N_\alpha=3K_\alpha+2.
\]
Then \(N_\alpha\) is the **exact least eventual-zero cutoff**:
\[
 a_n\equiv0\pmod{2^\alpha}\quad\text{for every }n\ge N_\alpha,
 \qquad a_{N_\alpha-1}\not\equiv0\pmod{2^\alpha}.
\]
Moreover, for all integers \(n\ge0\),
\[
\nu_2(a_n)\ge \left\lceil\frac{n-1}{3}\right\rceil_+,
\quad \left\lceil u\right\rceil_+=\max\{0,\lceil u\rceil\},
\]
and equality holds **exactly** for \(n=0,1\) and
\[
n\in\bigcup_{r\ge1}\{3(2^r-1)-1,\ 3(2^r-1),\ 3(2^r-1)+1\}.
\]
In particular, \(N_{2^r}=3\cdot2^r-1\) for every integer \(r\ge0\). These results imply all four forbidden-residue assertions in Rowland–Yassawi Open Question 3.25.

## Assumptions and scope
All indices, congruences, maxima, and valuations have the integer domains just specified. The \(2\)-adic valuation \(\nu_2(t)\) for positive \(t\) is the unique exponent of \(2\) in \(t\). The Catalan number is \(C_k=\binom{2k}{k}/(k+1)\). No primality assumptions or asymptotic approximations are used. The generating function is the established one from Le and the OEIS, not a newly derived enumeration formula.

## Proof
By the published generating function and the Catalan identity,
\[
F(x)=\sum_{n\ge0}a_nx^n=(1-x)\sum_{k\ge0}C_k\,[2x(1-x)^2]^k.
\]
Consequently coefficient extraction yields the *previously recorded* exact formula
\[
a_n=\sum_{\lceil(n-1)/3\rceil_+\le k\le n}
(-1)^{n-k}\,2^k C_k\binom{2k+1}{n-k}.
\tag{1}
\]
Terms outside the usual binomial range are zero. Kummer's binary-carry theorem, or the standard Catalan parity valuation, gives
\[\nu_2(C_k)=s_2(k+1)-1.\tag{2}\]
Indeed \(\nu_2\binom{2k}{k}=s_2(k)\) and subtracting \(\nu_2(k+1)\) yields \(s_2(k+1)-1\) using \(s_2(k+1)=s_2(k)+1-\nu_2(k+1)\).

Each summand in (1) is divisible by \(2^{k+\nu_2(C_k)}\), so all \(n\ge N_\alpha\) have only indices \(k>K_\alpha\), hence all summands vanish modulo \(2^\alpha\). At the preceding index \(n=3K_\alpha+1\), terms with \(k<K_\alpha\) are absent and all those with \(k>K_\alpha\) vanish modulo \(2^\alpha\). The sole surviving boundary term equals
\[
a_{3K_\alpha+1}\equiv-2^{K_\alpha}C_{K_\alpha}\not\equiv0\pmod{2^\alpha},\]
by the definition of \(K_\alpha\). This proves both cutoff assertions, including the boundary \(\alpha=1\).

The least index in (1) is \(L(n)=\lceil(n-1)/3\rceil_+\), proving the stated valuation lower bound. To decide equality, reduce (1) modulo \(2^{L(n)+1}\); only the term at \(k=L(n)\) can survive. For \(n=3m\) and \(n=3m+1\), where \(m\ge1\), its coefficient after dividing by \(2^m\) is respectively \((2m+1)C_m\) and \(-C_m\), both odd exactly when \(C_m\) is odd. For \(n=3m+2\), where \(m\ge0\), the coefficient after dividing by \(2^{m+1}\) is \(-\binom{2m+3}{2}C_{m+1}=-(2m+3)(m+1)C_{m+1}\); it is odd exactly when \(C_{m+1}\) is odd, since odd Catalan \(C_{m+1}\) forces \(m+1=2^r-1\) odd. Catalan parity, obtained from (2), says \(C_t\) is odd if and only if \(t=2^r-1\). The initial \(n=0,1\) both have valuation zero. These cases produce the claimed complete equality set.

When \(\alpha=2^r\), \(K_\alpha=\alpha-1\), because \(C_{\alpha-1}\) is odd and no \(k\ge\alpha\) can satisfy the strict inequality. Hence \(N_\alpha=3\alpha-1\).

To prove the published forbidden-residue question directly, (1) gives \(4\mid a_n\) for \(n\ge5\), while \(a_0,\ldots,a_4=1,1,2,6,22\). For \(\alpha\ge6\), all four proposed residues \(2^{\alpha-1}+1,2^{\alpha-1}+2,2^{\alpha-1}+6,2^{\alpha-1}+22\) have valuation zero or one modulo \(2^\alpha\), and none equals an initial value modulo \(2^\alpha\). Thus none can occur.

## Verification
Run `python3 verify.py` with Python's standard library. It independently evaluates the published Catalan coefficient sum and the quadratic generating-function recurrence, compares coefficients through index \(229\), checks all sharp cutoffs for \(1\le\alpha\le64\), and compares the complete lower-bound equality classification on the same indices. The unbounded claims are proved above; finite checks do not substitute for (1)–(2).

## Relationship to prior work
Le (2005) proves the generating function. OEIS A109033 has recorded the Catalan coefficient formula since a contribution by Paul Barry dated December 15, 2008. Rowland and Yassawi (arXiv submission October 31, 2013; journal publication 2015), Example 3.24 and Open Question 3.25, supply the explicit modular problem. The coefficient formula and Catalan valuation (2) are acknowledged prior art. The stated sharp eventual-zero threshold and equality-index classification are deductions from these known facts; their new contribution is a uniform exact criterion and terminal-boundary argument, not a new generating function or a new Catalan identity.

## Limitations
This concerns only the avoidance class \(\operatorname{Av}(1342,2143)\) and powers of two. An equivalent conductor classification could exist in unlocated literature. The exact formula is an elementary consequence of previously known coefficient expansions, so novelty is limited to the extracted global arithmetic classification and its sharpness. It does not provide a full formula for \(\nu_2(a_n)\) away from the lower-bound equality set. The result has not been independently audited.

## References
1. Ian Le, *Wilf Classes of Pairs of Permutations of Length 4*, Electronic Journal of Combinatorics 12 (2005), #R25, DOI: 10.37236/1922, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v12i1r25 .
2. OEIS Foundation, A109033, https://oeis.org/A109033 ; Paul Barry's December 15, 2008 coefficient formula.
3. Eric Rowland and Reem Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, Section 3.5, Example 3.24 and Open Question 3.25, https://arxiv.org/html/1310.8635v2 .
