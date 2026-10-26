# Sharp minimum and first-appearance spectrum of letter-duplicated subsequences

## Finding
For an alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\), \(q\geq2\), a **letter-duplicated subsequence** (LDS) is a nonempty scattered subsequence whose every maximal constant-letter run has length at least two. Define \(\operatorname{LLDS}(w)\) to be the maximum length of an LDS in \(w\), or zero when none exists. For every \(n\geq0\), write \(n=(q+1)t+s\), where \(t\geq0\) and \(0\leq s\leq q\). Then
\[
\boxed{\min_{w\in\Sigma_q^n}\operatorname{LLDS}(w)
=2t+\mathbf{1}_{\{t\geq1,\ s=q\}}.}
\]
The minimum is attained by the length-\(n\) prefix of the infinite cyclic word \(\mathcal C_q=012\cdots(q-1)012\cdots\). This includes the degenerate range \(0\leq n\leq q\), when the minimum is zero.

More precisely, let \(e_q(p)\) be the least positive integer \(j\) such that an LDS word \(p\) occurs as a scattered subsequence of the length-\(j\) prefix of \(\mathcal C_q\). Count **distinct LDS words**, not embeddings. If \(E_{q,j,\ell}\) is the number of such words \(p\) of length \(\ell\) with \(e_q(p)=j\), their exact first-appearance generating function is
\[
\boxed{\sum_{j\geq0}\sum_{\ell\geq0}E_{q,j,\ell}z^jy^\ell
=\frac{z^q(z+z^2+\cdots+z^q)y^2}
{1-z^qy-z^q(z+z^2+\cdots+z^{q-1})y^2}.}
\]
Thus the joint generating function for the number of distinct length-\(\ell\) LDS words *present* in the length-\(n\) cyclic prefix is this rational function divided by \(1-z\). The latter counts an LDS word at each prefix length at least its first-appearance index.

## Assumptions and scope
The source alphabet is exactly \(\Sigma_q\) and \(q\geq2\), with no requirement that every symbol occur in a particular length-\(n\) input. Subsequence means deletion of zero or more input positions, retaining their relative order; the selected positions need not be consecutive. The empty word is not an LDS. A word with no duplicated symbol therefore has longest LDS length zero. All minima concern indexed finite words, not cyclic rotation orbits. The cyclic construction is an infinite periodic *linear* word and its ordinary finite prefixes, not a circular embedding convention.

## Proof
**1. Uniform existence.** For each integer \(r\geq1\), establish by induction the statements:

(A) every word of length at least \((q+1)r\) has an LDS of length at least \(2r\);

(B) every word of length at least \((q+1)r+q\) has an LDS of length at least \(2r+1\).

For (A), the first \(q+1\) letters contain two equal letters by pigeonhole. These two positions give a length-two constant-letter run. If \(r=1\), this suffices. For \(r>1\), at least \((q+1)(r-1)\) input positions remain after the second selected equal letter, and induction (A) gives an LDS in that suffix of length \(2(r-1)\) or greater. Concatenating its selected positions with the initial equal pair produces an LDS: if the two adjacent chosen runs use the same letter, they merge into a longer permitted run.

For (B) at \(r=1\), an input of length at least \(2q+1\) contains some letter at least three times, giving a length-three LDS. For \(r>1\), again select a repeated pair in the first \(q+1\) positions. The remaining suffix has length at least \((q+1)(r-1)+q\), so induction (B) yields an LDS of length at least \(2(r-1)+1\). Concatenation yields an LDS of length at least \(2r+1\). Both inductions permit arbitrary greater input lengths.

**2. Exact cyclic embedding cost.** Express any LDS word as \(p=x_1^{d_1}\cdots x_r^{d_r}\), where \(r\geq1\), \(d_i\geq2\), consecutive \(x_i\) are different, and \(L=|p|=\sum_i d_i\). Identify each symbol with its integer residue in \(\{0,\ldots,q-1\}\). Greedy left-to-right subsequence embedding in \(\mathcal C_q\) is optimal for the last used input position: any later choice for an earlier symbol cannot improve availability of subsequent symbols. Starting with \(x_1\) at one-indexed position \(1+x_1\), repeating a symbol takes exactly \(q\) additional positions each time. Between different run symbols the least forward cyclic distance is \(\delta_i=(x_{i+1}-x_i)\bmod q\in\{1,\ldots,q-1\}\). Hence the exact earliest prefix length is
\[
e_q(p)=1+x_1+q(L-r)+\sum_{i=1}^{r-1}\delta_i.
\]
Because \(x_1\geq0\) and \(\delta_i\geq1\),
\[
e_q(p)\geq qL-(q-1)r\geq qL-(q-1)\lfloor L/2\rfloor.
\]
For every \(L\geq2\), equality is realized by taking first symbol \(0\), successive run symbols advancing by \(+1\) modulo \(q\), and exactly \(\lfloor L/2\rfloor\) runs: all of length two if \(L\) is even, and one length-three run with all others length two if \(L\) is odd. Consequently the least prefix lengths supporting some LDS of lengths \(2r\) and \(2r+1\), for \(r\geq1\), are respectively
\[
h_q(2r)=(q+1)r,\qquad h_q(2r+1)=(q+1)r+q.
\]
The function \(h_q\) strictly increases over LDS lengths \(L\geq2\). For \(n=(q+1)t+s\), \(0\leq s\leq q\), the cyclic prefix therefore has longest LDS length \(2t\) when \(t\geq1,s<q\), length \(2t+1\) when \(t\geq1,s=q\), and zero when \(t=0\). Uniform existence in step 1 supplies the matching lower bound for every word. This proves the minimax formula including boundaries.

**3. First-appearance spectrum.** The decomposition of \(p\) into maximal constant runs is unique. Give the initial symbol \(x_1=a\) weight \(z^{a+1}\), with aggregate \(A(z)=z+\cdots+z^q\). A run of length \(d\geq2\) contributes \(z^{q(d-1)}y^d\), so summing over possible run lengths gives \(B(z,y)=z^qy^2/(1-z^qy)\). After any run, the next run symbol differs from the preceding one, and is uniquely determined by a forward cyclic displacement \(\delta\in\{1,\ldots,q-1\}\); its aggregate transition weight is \(S(z)=z+\cdots+z^{q-1}\). The exact greedy cost in step 2 guarantees that these multiplicative weights record \(e_q(p)\), with each distinct word represented precisely once. Summing over the number of maximal runs \(r\geq1\) gives
\[
\sum_{r\geq1} A(z)B(z,y)^rS(z)^{r-1}
=\frac{A(z)B(z,y)}{1-B(z,y)S(z)}
=\frac{z^q(z+\cdots+z^q)y^2}{1-z^qy-z^q(z+\cdots+z^{q-1})y^2}.
\]
All coefficients are well-defined as formal power series because every LDS has positive earliest embedding position. The cumulative count over prefixes is obtained by convolution with \(1/(1-z)\), completing the proof.

## Verification
A standalone Python 3 checker, `verify_llds.py`, has no external dependencies. Running `python3 verify_llds.py` returns `LLDS_MINIMAX_SPECTRUM_PASS qary_source_words_tested=67752 distinct_subsequence_occurrences_tested=207 spectrum_entries_checked=290 generating_coefficients_n=0..80 q=2..5`. Independently, it computes longest admissible subsequences by a two-state-per-letter dynamic program and checks against explicit position subsets on small cases. It verifies the minimax formula for all words up to the enumerated finite bounds, directly enumerates distinct cyclic-prefix LDS subsequences for alphabets of sizes two through five, and checks first-appearance counts against the formal rational recurrence through prefix degree eighty. These computations are finite corroboration; the general statements are proved by the pigeonhole induction, exact greedy embedding cost, and formal run decomposition above.

## Relationship to prior work
Lai, Liyanage, Zhu, and Zou introduced the longest letter-duplicated subsequence problem and proved a linear-time optimization algorithm in its unconstrained form, together with results for full-appearance-constrained and weighted variants [1,2]. Those source results define precisely the same run-length-at-least-two admissibility criterion used here. The present claim instead concerns the *sharp worst-case optimum over all indexed words* and the *distinct-LDS first-appearance distribution* on an extremal periodic source. Neither is implied by the existence or running-time bounds of an algorithm for a fixed input. The authors explicitly distinguish the longest run subsequence problem, which requires each letter to occupy at most one run but does not require every run length to be at least two [1]. Thus results about that other admissibility constraint are not equivalent. The relevant published articles were compared at the level of their definitions, claimed theorems, algorithms, and concluding discussion; no matching minimax formula or bivariate distribution was identified. This is a literature comparison, not an exhaustive uniqueness guarantee.

## Limitations
The global minimax result gives one explicit family of extremizers, but does not classify every minimizing input word. The spectral formula addresses a fixed increasing cyclic ordering and distinct scattered output words, not their embedding multiplicities; it does not determine distributions over arbitrary random inputs. The source literature could contain an equivalent reformulation not detected in the comparison, and independent mathematical validation has not been performed.

## References
[1] W. Lai, A. Liyanage, B. Zhu, P. Zou, *Beyond the Longest Letter-duplicated Subsequence Problem*, arXiv:2112.05725, first version 10 December 2021; CPM 2022, LIPIcs 223, Article 7, https://arxiv.org/abs/2112.05725 and https://doi.org/10.4230/LIPIcs.CPM.2022.7.

[2] W. Lai, A. Liyanage, B. Zhu, P. Zou, *The longest letter-duplicated subsequence and related problems*, Acta Informatica 61 (2024), 315–329, https://doi.org/10.1007/s00236-024-00459-7.
