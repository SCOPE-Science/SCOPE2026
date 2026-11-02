# Sharp inverse-list maximum for a single palindromic duplication at every block length

## Finding

For integers \(q\ge 2\), \(k\ge 1\), and \(m\ge 2k\), let \(\Sigma\) be an alphabet of size \(q\) and consider the exact-one palindromic-duplication channel
\[
 u v w\longmapsto u v v^{\mathrm R}w,\qquad |v|=k,
\]
where reversal is literal symbol reversal, **not** complementation. Given a received word \(y\in\Sigma^m\), let \(d_k(y)\) count distinct source words of length \(m-k\) that can produce \(y\) by exactly one such operation (distinct event positions producing the same source count once).

Define the arithmetic separation parameter
\[
 s_k=\min\{s\in\mathbb Z:s\ge 2,\;2s\nmid k\}.
\]
Then the sharp maximum inverse-list size, for **every** permitted length and alphabet, is
\[
 \boxed{\max_{y\in\Sigma^m}d_k(y)=1+\left\lfloor\frac{m-2k}{s_k}\right\rfloor.}
\]
A binary periodic construction attains the bound, so increasing \(q\) beyond two cannot increase this worst-case number. In particular, \(s_1=s_2=s_3=2\), \(s_4=3\), \(s_{12}=4\), and \(s_{24}=5\). The theorem includes the boundary case \(m=2k\), when the maximum is one.

## Assumptions and scope

All words are linear and indexed from zero, with no wraparound. The source can contain any symbols and has prescribed length \(m-k\). Exactly one length-\(k\) block is copied, reversed, and immediately appended after its original occurrence. There are no other errors, no reverse-complement operation, no variable block length, and no constraint on source composition. We count **distinct sources** consistent with a particular received word, not the number of possible edit positions, and we maximize over received words that are in the channel's image. The alphabet has at least two symbols. No statement about maximum code cardinality or more than one duplication is inferred.

Write \(N=m-2k\). A feasible inverse start is an integer \(i\) with \(0\le i\le N\) and an even-palindromic factor \(y[i:i+2k]\). Its parent is
\[
 D_i(y)=y[0:i+k]\,y[i+2k:m].
\]
Every possible parent is of this form and every such start gives a valid parent.

## Proof

**1. Exact collision test.** For any two feasible starts \(0\le i<j\le N\), compare the two parent outputs at their common length-\(m-k\) coordinates. Before coordinate \(i+k\) both use the same received symbol; at and after coordinate \(j+k\) both use the symbol shifted right by \(k\). In between, one copies the symbol at coordinate \(t+k\) and the other copies at coordinate \(t\). Consequently,
\[
 \boxed{D_i(y)=D_j(y)\iff y_t=y_{t+k}\quad\text{for every }i+k\le t<j+k.} \tag{1}
\]
This test is exact and requires no periodicity assumption.

**2. Overlap of palindromic factors.** Suppose two factors of length \(2k\), starting at \(i\) and \(i+s\), are both palindromes and \(1\le s<2k\). Reflection across their respective centers sends a coordinate \(t\) to \(2i+2k-1-t\) and \(2(i+s)+2k-1-t\). Composing the reflections (where both are defined) gives
\[
 y_t=y_{t+2s}\qquad(i\le t<i+2k-s). \tag{2}
\]
Thus the union is periodic by steps \(2s\) through the indicated range.

If \(s=1\), relation (2) gives period two throughout the union. The first palindrome also gives equality of its two central symbols; this bridges the two parity classes, so the entire union is constant. In particular, the equality in (1) holds, and \(D_i(y)=D_{i+1}(y)\), for **all** \(k\ge1\).

If instead \(s\ge2\) and \(2s\mid k\), then \(k\ge2s\). For every \(t\) with \(i+k\le t<i+k+s\), repeated applications of (2) show \(y_t=y_{t+k}\): each intermediate step begins at most at \(i+2k-s-1\). By (1) the resulting parents again coincide.

By the defining minimality of \(s_k\), every positive \(s<s_k\) is either one or satisfies \(2s\mid k\). Moreover, \(s_k\le k\) when \(k\ge2\), so these offsets satisfy \(s<2k\); the case \(k=1\) only needs offset one. Hence **two feasible starts less than \(s_k\) apart can never generate different parents**.

**3. The universal upper bound.** Choose one feasible start for each distinct parent, and order these representatives increasingly. All successive gaps are at least \(s_k\); otherwise Step 2 would give the same parent. Representatives lie in the integer interval \([0,N]\), which contains at most
\[
 1+\left\lfloor N/s_k\right\rfloor
\]
points at this spacing. This proves the claimed upper bound for every alphabet.

**4. Explicit matching construction.** Put \(d=s_k\) and choose distinct letters \(\alpha,\beta\in\Sigma\). Define \(y\) as the length-\(m\) prefix of the period-\(2d\) word given by
\[
 y_t=\begin{cases}
 \beta,&t\equiv k-1\text{ or }k\pmod{2d},\\
 \alpha,&\text{otherwise}.
 \end{cases} \tag{3}
\]
The two marked residues are adjacent and distinct, since \(d\ge2\). At every start \(i=rd\) with \(0\le rd\le N\), reflection about the midpoint of \([i,i+2k-1]\) exchanges these marked residues and leaves all other residues unmarked. This is because \(2i\equiv0\pmod{2d}\). Therefore all the \(1+\lfloor N/d\rfloor\) selected starts are feasible.

It remains to distinguish their parent outputs. For any selected start \(i\) that has a later selected start (so \(i+d\le N\)), the length-\(d\) interval \([i+k,i+k+d)\) lies inside the received word and contains exactly one \(\beta\). When \(i\equiv0\pmod{2d}\), it is the **first** symbol. If all those \(d\) symbols agreed with their shifts by \(k\), mapping the marked symbol would force \(k\equiv0\) or \(-1\pmod{2d}\). The first is excluded by the definition of \(d\); in the second case the immediately following \(\alpha\) would shift to a \(\beta\), contradiction (the following position exists because \(d\ge2\)). When \(i\equiv d\pmod{2d}\), the sole \(\beta\) is the **last** symbol; a putative full agreement forces \(k\equiv0\) or \(+1\pmod{2d}\), with the second case contradicted by its immediately preceding \(\alpha\). Thus in either case
\[
 \exists\,t\in[i+k,i+k+d):\quad y_t\ne y_{t+k}. \tag{4}
\]
For any later selected start \(j\ge i+d\), this well-defined mismatch belongs to the comparison interval \([i+k,j+k)\); (1) shows \(D_i(y)\ne D_j(y)\). There are precisely \(1+\lfloor N/d\rfloor\) distinct parents, matching Step 3. This proves the theorem. \(\square\)

## Verification

The accompanying standalone `verify_pal_inverse.py` constructs the exact inverse-parent sets directly from the channel definition. It exhaustively checks 73 binary and ternary parameter cases, totaling 832,346 received words; tests local collisions; checks the maximum; verifies the periodic witness for all \(1\le k\le700\) at multiple lengths; and performs 7,000 additional alphabet-independent randomized checks through five-letter alphabets. It prints:

```text
VERIFY_OK exhaustive_cases=73 exhaustive_received_words=832346 sampled_or_witness_cases=11200 k_witness_range=1..700 max_alphabet_tested=5
```

Run `python verify_pal_inverse.py`. The finite checks are only corroboration; Steps 1–4 prove the statement for all parameters. All construction strings, equations and tests are defined here and in the included program; no external certificate is required.

## Relationship to prior work

Lenz, Wachter-Zeh and Yaakobi (2017, [1]) developed palindromic-duplication/deletion error spheres and an upper bound using runs of zero columns in a palindrome-test matrix. Their expanded study [2] gives exact formulas for length-one and (binary) length-two deletion spheres (Lemma 14) and a general zero-column-run upper bound (Lemma 15), with equivalence conditions for different deletion positions (Appendix B). These results explain why adjacent feasible positions collapse and, for small block lengths, include special cases. They do **not** state the present all-block-length sharp worst-case formula, its arithmetic parameter \(s_k\), or its binary periodic attaining construction. In particular, excluding separations \(s>1\) with \(2s\mid k\) strengthens the consecutive-position restriction that underlies their general zero-column bound.

Yohananov and Schwartz [3] establish capacity for codes correcting **any number** of reverse and reverse-complement duplications, rather than the maximal exact-one inverse list. Sun and Ge [4] study code constructions and redundancy bounds. The later work [5] addresses **two** sequential palindromic errors and their forward descendant count, a different quantifier and direction. None of those stated results implies the theorem above; the possibility of a differently formulated earlier result remains a bibliographic limitation.

## Limitations

This is an exact-one, fixed-block-length inverse-list theorem, not an optimal coding-rate or code-size result. It does not cover reverse-complement, simultaneous substitutions, multiple duplications, or a one-symbol alphabet. The arithmetically defined spacing \(s_k\) can change with divisibility of \(k\), so a uniform two-position packing bound would be false for some lengths. Although the substantive relevant sections of the primary texts in [1]–[4] were compared and a later related abstract [5] reviewed, undiscovered equivalent statements remain possible; independent validation has not been performed.

## References

[1] A. Lenz, A. Wachter-Zeh, E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052, first posted 2017-06-30. https://arxiv.org/abs/1707.00052

[2] A. Lenz, A. Wachter-Zeh, E. Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345, first posted 2017-12-24. https://arxiv.org/abs/1712.09345

[3] L. Yohananov, M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394, first posted 2023-12-01. https://arxiv.org/abs/2312.00394

[4] Y. Sun, G. Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151, posted 2026-02. https://arxiv.org/abs/2602.01151

[5] A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first posted 2026-09-01. https://arxiv.org/abs/2609.00779
