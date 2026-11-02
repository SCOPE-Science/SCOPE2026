# Exact maximal period \(106\) of four-symbol order-four orientable sequences

## Finding

For the alphabet \(Q=\{0,1,2,3\}\), the maximum possible period of an orientable cyclic sequence of order four is exactly
\[
\boxed{\mathcal M_4(4)=106}.
\]
Here the standard notation \(\mathcal{OS}_{4}(4)\) denotes a cyclic word whose length-four windows, including wraparound, are all distinct and never equal to the reversal of any window, including themselves. The following explicit cyclic word is optimal; its digits are written from left to right and the last digit precedes the first:

```text
0001231333032331222023231031212302232132212013301220113130302131002113020210230112101300201030010111320332
```

## Assumptions and scope

Let \(S=(s_i)_{i\in\mathbb Z/m\mathbb Z}\) have fundamental period \(m\ge1\) over \(Q\). Its window at position \(i\) is \(e_i=(s_i,s_{i+1},s_{i+2},s_{i+3})\). The orientability condition is \(e_i\ne e_j^R\) for all \(i,j\); in addition the length-four windows are pairwise distinct. A palindrome cannot occur. Equivalently, the selected windows form a reversal-free set of edges of the directed de Bruijn graph on the triple vertices \(Q^3\), with equal in-degree and out-degree at every vertex. No assumption about an algorithm or an unproved finite search is needed for the upper bound.

## Proof

**1. Cyclic edge incidence and the uniform-triple obstruction.** For each \(e=abcd\in Q^4\), let \(x_e\) equal one when this window occurs in \(S\), and zero otherwise. Thus \(m=\sum_e x_e\), \(x_e=0\) for palindromes, and \(x_e+x_{e^R}\le1\) for nonpalindromic \(e\). Every triple \(v\in Q^3\) has balanced incidence:
\[
B(v):=\sum_{t\in Q}x_{vt}-\sum_{t\in Q}x_{tv}=0.
\]
At the uniform vertex \(aaa\), the edge \(aaaa\) is forbidden, and for each \(b\ne a\) the reversal pair \(aaab,baaa\) contributes at most one selected edge. Therefore
\[
T_a:=\sum_{b\ne a}(x_{aaab}+x_{baaa})
=2\sum_{b\ne a}x_{aaab}\le2,
\]
because balance forces the outgoing and incoming counts equal, so \(T_a\) is even and at most three. Summing over the four letters yields \(\sum_a T_a\le8\).

**2. An explicit local inequality.** Define an integer potential \(h\) on triple vertices by
\[
h(abc)=\begin{cases}
1,&a=b\ne c,\\
-1,&a\ne b=c,\\
0,&\text{otherwise}.
\end{cases}
\]
For a length-four word \(e=abcd\), define \(\Delta h(e)=h(abc)-h(bcd)\), and assign a nonnegative reversal-invariant weight
\[
\lambda(e)=\begin{cases}
1,&a\ne b,\ b\ne c,\ c\ne d,\\
3,&b=c\text{ and }a,b,d\text{ are pairwise distinct},\\
0,&\text{otherwise}.
\end{cases}
\]
Finally put \(u(e)=2\) when \(e\) has the form \(aaab\) or \(baaa\) with \(a\ne b\), and \(u(e)=0\) otherwise. For **every nonpalindromic** \(e\in Q^4\),
\[
\boxed{1\le\lambda(e)+u(e)+\Delta h(e)}.\tag{1}
\]
This is checked exhaustively by five disjoint *symbol-equality patterns*, not by a numerical optimization or a restricted class of sequences:

| Nonpalindromic pattern | Number of words | \(\lambda\) | \(u\) | \(\Delta h\) | Right side of (1) |
| --- | ---: | ---: | ---: | ---: | ---: |
| All three adjacent pairs unequal | 108 | 1 | 0 | 0 | 1 |
| Middle two equal, with outer letters and middle letter all distinct | 24 | 3 | 0 | −2 | 1 |
| \(aaab\) or \(baaa\), \(a\ne b\) | 24 | 0 | 2 | −1 | 1 |
| \(aabb\), \(a\ne b\) | 12 | 0 | 0 | 2 | 2 |
| All remaining nonpalindromic words | 72 | 0 | 0 | 1 | 1 |

The counts total \(240=4^4-4^2\), since exactly sixteen length-four words are palindromes. Every displayed value follows by substitution into the explicit definitions. In particular, the last row comprises the remaining cases, all giving \(\Delta h=1\).

**3. Summing the inequality.** There are \(108/2=54\) reversal pairs of weight one and \(24/2=12\) reversal pairs of weight three. Multiplying (1) by \(x_e\) and summing over all nonpalindromic \(e\), the reversal exclusion bounds the total weight by \(54+3\cdot12=90\). The uniform-triple obstruction gives \(\sum_e u(e)x_e=2\sum_aT_a\le16\). The remaining potential telescopes by the incidence identities:
\[
\sum_e x_e\Delta h(e)=\sum_{v\in Q^3}h(v)B(v)=0.
\]
Consequently every orientable cyclic word of order four over four symbols satisfies
\[
m=\sum_e x_e\le90+16+0=106.
\]

**4. Matching construction.** Let \(W\) be the explicit 106-digit word in the Finding. Directly form its 106 cyclic windows \(W_iW_{i+1}W_{i+2}W_{i+3}\), with indices modulo 106. The supplied independent, pure-Python checker enumerates all of them and verifies (i) all 106 windows are distinct; (ii) none is palindromic; (iii) no window is the reversal of any selected window. These finite conditions *completely establish* that the displayed cyclic word is an orientable sequence of period 106. Since all its windows are distinct, the period is fundamental. Together with the proved upper bound, the maximum is 106.

## Verification

Run the self-contained `verify.py` using Python 3 with no third-party packages. It checks the stated literal witness in full, all 256 length-four words, the disjoint five-case local inequality, the reversal-weight pair totals, and the exact upper-bound arithmetic. Expected output is embedded as `verification_output.txt`; all assertions are executable. The proof of the universal upper bound is given above and does not depend on computational search or numerical solver status.

## Relationship to prior work

Mitchell and Wild, *New orientable sequences* (arXiv:2507.02526, first public 2025-07-03), Table 7, reported period 88 as the largest known for \(\mathcal{OS}_4(4)\), together with an upper bound 112, and explicitly identified the unresolved even-alphabet, order-four gap in their Section 7. The present theorem closes that specific gap at 106, strictly below the earlier upper bound; the simple local potential and the complete 106-window witness are not implied by the published bound or construction. Gabrić and Sawada's 2024 work gave asymptotic constructions (and exact optimality for order two), not this exact four-letter, order-four optimum. Mitchell and Wild's 2024 *Special orientable sequences* investigates an additional negative-orientability condition and general constructions, rather than this unrestricted exact optimum. Relevant alternative constructions and subsequent general randomized universal-cycle methods do not establish this sharp value.

## Limitations

This result concerns **ordinary** orientability for exactly four letters and length-four windows, without the additional negative-orientability requirement. It does not classify every optimal cycle, compute their number, or establish analogous maxima at other alphabet sizes or orders. Search of accessible literature and indexed scientific records cannot guarantee absence of an unindexed or independently discovered equivalent result. No independent mathematical review has been performed.

## References

1. C. J. Mitchell and P. R. Wild, *New orientable sequences*, arXiv:2507.02526v1, 2025-07-03, https://arxiv.org/html/2507.02526v1 ; Table 7 and Sections 2, 6–7.
2. D. Gabrić and J. Sawada, *Constructing \(k\)-ary Orientable Sequences with Asymptotically Optimal Length*, arXiv:2407.07029, 2024-07-09, https://arxiv.org/abs/2407.07029 .
3. C. J. Mitchell and P. R. Wild, *Special orientable sequences*, arXiv:2411.17273v1, 2024-11-26, https://arxiv.org/html/2411.17273v1 .
4. J. Sawada and D. Gabrić, *Random generation of universal cycles and de Bruijn sequences*, arXiv:2510.16545, 2025-10-18, https://arxiv.org/abs/2510.16545 .
