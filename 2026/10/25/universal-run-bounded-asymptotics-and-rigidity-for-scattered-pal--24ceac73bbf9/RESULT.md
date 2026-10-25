# Universal run-bounded asymptotics and rigidity for scattered palindromes

## Finding

Fix integers \(q\ge2\) and \(k\ge1\). Among length-\(n\) words over an alphabet of \(q\) symbols having at most \(2k+1\) maximal constant-symbol runs, let \(M_{q,k}(n)\) denote the largest possible number of **distinct nonempty scattered palindromic subsequences**. As \(n\to\infty\), with \(q,k\) fixed,

\[
M_{q,k}(n)=\frac{n^{k+1}}{2^k(k+1)^{k+1}}+O_{q,k}(n^k).
\]

In particular, the dominant coefficient is independent of alphabet size. The following quantitative bounds hold for \(n\ge 2(k+1)\), with \(b=\lfloor n/[2(k+1)]\rfloor\):

\[
b^k(n-2kb)\le M_{q,k}(n)\le\frac{n^{k+1}}{2^k(k+1)^{k+1}}+q\sum_{j=0}^{k-1}(q-1)^j n^{j+1}.
\]

There is also **complete asymptotic rigidity**. A sequence of length-\(n\) words \(w_n\), each with at most \(2k+1\) maximal constant runs, satisfies \(P(w_n)/M_{q,k}(n)\to1\) if and only if, for all sufficiently large \(n\), its run-symbol sequence has exactly \(2k+1\) terms and is a palindrome, and its run lengths \(r_{n,1},\ldots,r_{n,2k+1}\) satisfy

\[
\frac{r_{n,i}}{n}\to\frac1{2(k+1)}\quad(i\ne k+1),\qquad
\frac{r_{n,k+1}}{n}\to\frac1{k+1}.
\]

## Assumptions and scope

A scattered subsequence is obtained by selecting positions in increasing order, without requiring adjacency. Two selected position sequences yielding the same *letter string* count once. A palindrome equals its reversal; the empty string is excluded. Let \(P(w)\) be the number of distinct nonempty palindromic scattered subsequence strings of \(w\). A maximal constant run is a maximal nonempty consecutive block of one symbol; neighboring runs necessarily use different symbols. Throughout \(q,k\) are fixed positive integers with \(q\ge2\), \(k\ge1\), and the alphabet has \(q\) available symbols, not necessarily all used by the word. The \(O_{q,k}\) constant may depend on \(q,k\) but not \(n\).

## Proof

**Run parity and the lower-order contribution.** Every nonempty palindrome has an odd number of maximal constant runs: an even-run palindromic run-symbol sequence would require two adjacent central runs to have the same symbol, contradicting run maximality. A subsequence cannot have more maximal constant runs than the original word, since each transition in the subsequence requires at least one transition between its selected positions in the original. Thus a palindrome drawn from any admissible word has at most \(2k+1\) runs.

For \(0\le j<k\), a palindrome with \(2j+1\) runs is specified by its initial \(j+1\) run symbols and its initial \(j+1\) positive run lengths. The first symbol has at most \(q\) choices, each subsequent initial-run symbol at most \(q-1\) choices; each length is at most \(n\). Therefore, even without requiring realizability as a subsequence, at most \(q(q-1)^j n^{j+1}\) such distinct palindromes exist. Consequently the aggregate \(E(w)\) of palindromes with at most \(2k-1\) runs obeys

\[
0\le E(w)\le B_{q,k}(n):=q\sum_{j=0}^{k-1}(q-1)^j n^{j+1}=O_{q,k}(n^k).
\]

**Exact top-run count.** If \(w\) has fewer than \(2k+1\) runs, there is no palindromic subsequence with \(2k+1\) runs. Otherwise write its run symbols \(a_1,\ldots,a_{2k+1}\) and their positive lengths \(r_1,\ldots,r_{2k+1}\). Any \(2k+1\)-run subsequence necessarily uses at least one selected letter from every original run, in order, so its run-symbol sequence is exactly \((a_i)\). It can be palindromic only when this run-symbol sequence is palindromic. When it is, an arbitrary \(2k+1\)-run palindrome subsequence is uniquely determined by positive lengths \(t_1,\ldots,t_k,c,t_k,\ldots,t_1\), with \(1\le t_i\le\min(r_i,r_{2k+2-i})\) and \(1\le c\le r_{k+1}\). Every such choice occurs by selecting letters independently within each original run, and distinct choices give distinct strings. Thus the exact number of top-run palindromes is

\[
L(w)=r_{k+1}\prod_{i=1}^k\min(r_i,r_{2k+2-i})
\]

when the run-symbol sequence is palindromic and has exactly \(2k+1\) terms, and \(L(w)=0\) otherwise. In every case \(P(w)=L(w)+E(w)\).

**Sharp universal leading constant.** For the nonzero case put \(t_i=\min(r_i,r_{2k+2-i})\), \(c=r_{k+1}\). Since all run lengths sum to \(n\), we have \(2\sum_{i=1}^k t_i+c\le n\). Applying the arithmetic-geometric mean inequality to the \(k+1\) positive quantities \(2t_1,\ldots,2t_k,c\),

\[
L(w)=2^{-k}\bigl(\prod_{i=1}^k(2t_i)\bigr)c
\le\frac{n^{k+1}}{2^k(k+1)^{k+1}}.
\]

Adding the preceding bound on \(E(w)\) proves the global upper bound. For the lower bound choose any alternating two-symbol, hence palindromic, run-symbol sequence of length \(2k+1\); give every run except the middle one length \(b=\lfloor n/[2(k+1)]\rfloor\) and give the middle run length \(n-2kb\). The assumption \(n\ge2(k+1)\) ensures all chosen lengths are positive. Its top-run palindrome count is \(b^k(n-2kb)\), which is the asserted lower bound and equals the stated leading coefficient times \(n^{k+1}\) plus \(O_k(n^k)\).

**Rigidity.** Suppose \(P(w_n)/M_{q,k}(n)\to1\). The uniform estimate on \(E(w_n)\) gives

\[
\frac{L(w_n)}{n^{k+1}}\to\frac1{2^k(k+1)^{k+1}}>0.
\]

Hence for all large \(n\), \(L(w_n)>0\), forcing precisely \(2k+1\) runs with palindromic run-symbol sequence. Put \(t_{n,i}=\min(r_{n,i},r_{n,2k+2-i})\) and \(c_n=r_{n,k+1}\); divide the nonnegative quantities \(2t_{n,1},\ldots,2t_{n,k},c_n\) by \(n\). Their sum is at most \(1\). Compactness of \([0,1]^{k+1}\), the arithmetic-geometric mean inequality, and its **unique** equality case imply that every normalized quantity tends to \(1/(k+1)\). Therefore \(2\sum_i t_{n,i}+c_n=n-o(n)\). Since

\[
n-2\sum_{i=1}^k t_{n,i}-c_n=
\sum_{i=1}^k\lvert r_{n,i}-r_{n,2k+2-i}\rvert,
\]

all paired run differences are \(o(n)\); consequently both members of every mirrored pair have normalized length \(1/[2(k+1)]\), and the center has normalized length \(1/(k+1)\). Conversely the stated skeleton and run-length limits imply \(L(w_n)/n^{k+1}\to1/[2^k(k+1)^{k+1}]\), so \(P(w_n)/M_{q,k}(n)\to1\) by the already proved bounds. This establishes both directions.

## Verification

Run `python3 verify.py` with standard Python 3. The checker enumerates *distinct subsequence strings* directly, not embeddings. It exhausts every word of lengths \(1\) through \(13\) over the binary alphabet and lengths \(1\) through \(9\) over the ternary alphabet, restricted to at most seven runs, and checks the exact top-run formula, run-parity contribution bound, and global upper bound for \(k=1,2,3\) whenever the word meets the run cap. It performed \(54{,}007\) checks of those triples and additionally tested an exact five-run counting formula and the three-run extremal count through length \(35\). The output is `VERIFY_OK 54007 run-cap/leading-count checks; exact 5-run and 3-run spot checks`. The infinite-parameter conclusion comes from the proof, not from finite enumeration.

## Relationship to prior work

Mahalingam and Pandoh (2021, arXiv:2108.02729) study distinct scattered palindromic subsequences, global Fibonacci-type bounds, and extremal behavior involving the number of different letters. Their inspected work does not establish the present sharp extremum and stability classification under a *fixed run budget*. Liron and Langberg (2012, arXiv:1202.1644) study the number of arbitrary subsequences obtained under deletion, including extremal words at a fixed number of runs; their statistic does **not** impose palindromicity or count palindromes across all lengths. The present half-sized peripheral versus double-sized center runs arise from the symmetry constraint and are not implied by their balanced-run result. Müllner and Ryzhikov (2019, arXiv:1901.07502) study the **length of a longest** palindromic subsequence, a different invariant. Holub and Saari (2009) also investigate longest palindromic subsequences and minimal configurations, not this distinct-count run-budget asymptotic. These are statement-level distinctions, not proof of absolute novelty.

## Limitations

The constants in the lower-order \(O_{q,k}(n^k)\) term are not optimized, and an exact finite-\(n\) optimum is not determined for all \(k\). Rigidity applies only to sequences asymptotically attaining the maximum with fixed \(q,k\); it does not assert uniqueness of individual maximizing words or permit \(q,k\) to grow with \(n\). Literature searches cannot rule out all unindexed equivalents. No independent audit of the argument has been carried out.

## References

1. K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729 (first publicly posted August 5, 2021), https://arxiv.org/abs/2108.02729.
2. Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, arXiv:1202.1644 (2012), https://arxiv.org/abs/1202.1644.
3. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, LATA 2019, arXiv:1901.07502, https://arxiv.org/abs/1901.07502.
4. Š. Holub and K. Saari, *On highly palindromic words* (2009), https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf.
