# Exact scattered-palindrome spectrum of partial cyclic-permutation powers

## Finding
Let \(q\ge3\), \(k\ge1\), and \(0\le s<q\) be integers, and let \(\Sigma_q=\{0,1,\ldots,q-1\}\). Put
\[
W_{q,k,s}=(0\,1\,\cdots\,(q-1))^k\,(0\,1\,\cdots\,(s-1)),
\]
where the final parenthesized word is empty for \(s=0\). Let \(p_{q,k,s}(\ell)\) count **distinct nonempty palindromic words of length \(\ell\)** occurring as scattered subsequences (not necessarily contiguous factors) of \(W_{q,k,s}\).

**Exact membership theorem.** A nonempty palindrome \(v=v_1\cdots v_\ell\) has a unique first half \(h=v_1\cdots v_{\lceil\ell/2\rceil}\). Define \(m=\lfloor\ell/2\rfloor\) and \(e(h)=|\{i:1\le i<|h|,\ h_i=h_{i+1}\}|\). Then \(v\) occurs as a subsequence of \(W_{q,k,s}\) if and only if
\[
m+e(h)<k\quad\text{or}\quad (m+e(h)=k\ \text{and}\ v_1<s).
\]
In particular, membership depends on the first half only through its number of equal adjacent pairs and its initial letter; it does **not** depend on the cyclic distances between distinct successive letters.

**Complete exact length spectrum.** For \(m\ge0\), define \(C(n,r)=\binom nr\) for \(0\le r\le n\) and \(C(n,r)=0\) otherwise. For odd lengths \(\ell=2m+1\),
\[
p_{q,k,s}(2m+1)=q\sum_{e=0}^{\min(m,k-m-1)}\binom{m}{e}(q-1)^{m-e}
+s\binom{m}{k-m}(q-1)^{2m-k},
\]
where the last term is taken as zero unless \(0\le k-m\le m\), and a sum with negative upper limit is zero. For even lengths \(\ell=2m\), \(m\ge1\),
\[
p_{q,k,s}(2m)=q\sum_{e=0}^{\min(m-1,k-m-1)}\binom{m-1}{e}(q-1)^{m-1-e}
+s\binom{m-1}{k-m}(q-1)^{2m-1-k},
\]
where again the final term is zero unless \(0\le k-m\le m-1\). These formulas yield zero for all lengths outside their indicated ranges.

Equivalently, the **entire bivariate generating function** (formal in \(z,u\)) is
\[
\boxed{\begin{aligned}
F_{q,s}(z,u)&=\sum_{k\ge1}\sum_{\ell\ge1}p_{q,k,s}(\ell)z^k u^\ell\\
&=\frac{quz(1+uz)}{(1-z)[1-u^2z(q-1+z)]}
+\frac{su^2z[1+u(q-1+z)]}{1-u^2z(q-1+z)}.
\end{aligned}}
\]
Thus each extra letter in the final incomplete period adds the **same length-resolved increment**. The maximum palindromic-subsequence length is \(2k-1\) for \(s=0\) and \(2k+1\) for \(1\le s<q\). At that maximum there are respectively \(q(q-1)^{k-1}\) and \(s(q-1)^k\) distinct palindromes. The total count and its recurrence follow by setting \(u=1\).

## Assumptions and scope
All source symbols are distinct within each complete period and follow the same cyclic order in every period. There are \(k\ge1\) complete periods and a final prefix of length \(s<q\); all target words are distinguished by their symbol sequences rather than by embeddings. The empty palindrome is excluded. The theorem is for \(q\ge3\); the previously determined alternating binary case is not claimed anew.

## Proof
**1. Greedy embedding.** Index the letters of the source from zero. The symbol at source index \(j\) is \(j\bmod q\). The earliest embedding of any nonempty target word \(v_1\cdots v_\ell\) starts at index \(v_1\) and advances from symbol \(a\) to symbol \(b\) by \(\delta(a,b)\in\{1,\ldots,q\}\), the least strictly positive integer congruent to \(b-a\pmod q\). This embedding exists within a given finite prefix if and only if its last greedy position lies within the prefix: choosing a later occurrence at any step cannot improve later completion. Consequently, with \(T=\sum_{i=1}^{\ell-1}\delta(v_i,v_{i+1})\), the necessary and sufficient condition is \(v_1+T<kq+s\).

**2. Cancellation for palindromes.** If \(a\ne b\), then \(\delta(a,b)+\delta(b,a)=q\). If \(a=b\), both transitions cost \(q\) and their sum is \(2q\). In any odd palindrome \(v=h\,h_{|h|-1}\cdots h_1\), the \(m\) successive transitions of its first half are paired with their reflected reverses; each unequal pair costs \(q\), and each equal pair costs \(2q\). Hence \(T=q(m+e(h))\). In an even palindrome \(v=h\,h_{|h|}\cdots h_1\), the central equal-symbol transition costs an additional \(q\), while the other \(m-1\) reflected pairs contribute \(q(m-1+e(h))\). Again \(T=q(m+e(h))\). Thus the last greedy index is \(v_1+q(m+e(h))\), with \(0\le v_1<q\).

**3. Sharp endpoint test.** If \(m+e(h)\le k-1\), then \(v_1+q(m+e(h))\le kq-1<kq+s\), so the palindrome occurs. If \(m+e(h)=k\), the final index is \(kq+v_1\), which is in the final partial period precisely when \(v_1<s\). If \(m+e(h)\ge k+1\), the final index exceeds \(kq+s-1\). This proves the membership equivalence, including \(s=0\), \(k=1\), and the boundaries.

**4. Exact count.** A half-word of length \(t\) with exactly \(e\) equal adjacent pairs has \(q\binom{t-1}{e}(q-1)^{t-1-e}\) possibilities: choose the initial letter, choose the equality positions, and choose one of the \(q-1\) different symbols at every other transition. Constraining the first letter to \(\{0,\ldots,s-1\}\) replaces the factor \(q\) by \(s\). Apply the sharp endpoint test with \(t=m+1\) for odd length and \(t=m\) for even length. This gives both coefficient formulas, with the boundary term only when \(e=k-m\).

**5. Rational generating function.** Set \(A=u^2z(q-1+z)\). Summing half-words at all costs gives \(\sum_{m\ge0}A^m=(1-A)^{-1}\). The complete-period contributions over \(k\ge1\) are \(quz(1+uz)/[(1-z)(1-A)]\). The partial-period contributions arise only at exact cost \(k=m+e\), giving \(su^2z[1+u(q-1+z)]/(1-A)\). Adding them proves the displayed generating function as an identity of formal series, without analytic convergence assumptions.

**6. Extremal lengths.** For a palindrome of length \(2m+1\), the cost is at least \(m\); for length \(2m\), it is also at least \(m\). With \(s=0\) the greatest permitted cost is \(k-1\), so the maximum length is \(2k-1\) and it is realized by all halves of length \(k\) with unequal successive letters: \(q(q-1)^{k-1}\) choices. If \(s>0\), cost \(k\) is permitted exactly for first letters below \(s\); the maximum length is \(2k+1\), realized by halves of length \(k+1\) with every transition unequal: \(s(q-1)^k\) choices.

## Verification
Run \(`python3 verify.py`\) in the directory containing this result. The independent finite checker explicitly builds every distinct palindromic subsequence from index subsets in \(49\) small host cases, compares all resulting length coefficients with the claimed formulas, tests \(67{,}121\) candidate palindrome membership conditions, and compares \(50{,}932\) integer coefficients of two independently implemented finite-formula and formal-series methods. The full reported result is

`VERIFY_OK literal_parameter_cases=49 literal_palindromes=3086 palindrome_membership_tests=67121 exact_formal_coefficients=50932 q=3..9 k=1..34 all_prefixes=yes`

These finite checks corroborate but do not replace the proof for all \(q,k,s\).

## Relationship to prior work
Mahalingam–Pandoh (2021, arXiv:2108.02729) define and study distinct scattered palindromes, prove general bounds and characterize words with minimum counts; their Theorem 4.2 and Section 5 give global and alphabet-sensitive upper bounds. Their inspected treatment does not give the present exact full length spectrum for arbitrary cyclic-permutation powers with incomplete final cycles. Müllner–Ryzhikov (2019, arXiv:1901.07502) study longest palindromic or antipalindromic subsequences, principally for circular words, rather than counting all distinct palindromic targets by length. An earlier exact binary alternating-word spectrum exists; the domain here explicitly starts at \(q=3\), and the new full alphabet-size and incomplete-period parameters are not consequences of the binary count alone.

## Limitations
This is a statement for periodic permutation words and their initial prefixes, not for arbitrary strings, arbitrary reordered periods, or concatenations with repeated symbols within a period. The proof establishes the exact theorem but not publication priority or independent certification. The binary case is intentionally excluded; no claim is made to have discovered it. Related specialized results not located in the inspected sources may exist. The finite program is a falsification check rather than a proof of the infinite family.

## References
1. K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729v1 (first posted 2021-08-05), https://arxiv.org/pdf/2108.02729 . Read the abstract and relevant theorem statements and arguments in Sections 3–5 of the accessible preprint.
2. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502v1 (first posted 2019-01-22), https://arxiv.org/pdf/1901.07502 . Read the abstract, definitions, and relevant circular-word extremal statements in the accessible preprint.
