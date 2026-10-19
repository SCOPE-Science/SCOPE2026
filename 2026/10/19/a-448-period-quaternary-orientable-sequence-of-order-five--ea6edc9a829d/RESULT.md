# A 448-period quaternary orientable sequence of order five

## Finding

There exists an orientable cyclic word of **length \(448\)** and order \(5\) on the four-letter alphabet \(\{0,1,2,3\}\). Consequently, writing \(\lambda(5,4)\) for the maximum possible period of such a word,

\[\boxed{\lambda(5,4)\ge 448.}\]

The displayed explicit finite witness improves the published 2026 lower bound of \(404\) by \(44\) positions; combined with the published upper bound of \(452\), the resulting certified interval is

\[\boxed{448\le\lambda(5,4)\le452.}\]

No assertion of optimality at \(448\) is made.

## Assumptions and scope

An order-five orientable cyclic word is a word \(s=s_0s_1\dots s_{L-1}\) over \(\{0,1,2,3\}\), interpreted with indices modulo \(L\), such that each circular factor \(f_i=s_is_{i+1}s_{i+2}s_{i+3}s_{i+4}\) is different from every reversed factor \(f_j^R\), including when \(i=j\), and no two equal five-factors occur at different positions. Its period is the least positive period of the corresponding bi-infinite sequence. The claim concerns precisely the parameter pair of alphabet size four and factor order five, not arbitrary alphabet sizes or orders.

## Proof

The explicit word below is provided in \(7\) consecutive blocks of \(64\) symbols for legibility; concatenating these blocks *without separators* gives the exact \(448\)-letter word (also in the standalone file `witness.txt`):

```
0000210100212311200321210003100102102001311001203002031111002212
0122010112031221002300023100303101032133001101222310202103102111
0300312312102200013321013210231130022213133030121103310113010031
3102222331202313113310232300123020111322030130230110213011323320
0213203032011220200223012320033202033003221033221121203202232032
3103332033110223321113323013120332322302202112303301023313013330
2213313211312323122312330311213032220313223331212211333321223211
```

The following exhaustive finite certificate proves the claim. For each integer \(i\) with \(0\le i<448\), form the tuple

\[f_i=(s_i,s_{i+1},s_{i+2},s_{i+3},s_{i+4})\]

using subscripts modulo \(448\), and its canonical reversal representative \(c_i=\min_{\mathrm{lex}}\{f_i,f_i^R\}\). Direct evaluation of all \(448\) tuples gives all three exact facts:

1. Each \(f_i\) differs from its reversal.
2. The \(448\) canonical representatives \(c_i\) are pairwise distinct.
3. Every one of the four alphabet symbols occurs \(112\) times in \(s\).

Facts 1 and 2, independently checked in the supplied `verify.py`, establish orientability: no circular factor is a palindrome or agrees with the reverse of another factor. They also imply all factors are distinct, because equal factors have equal canonical representatives. If the infinite repetition of \(s\) had a proper period \(d<448\), then positions \(0\) and \(d\) would have identical length-five factors, contradicting Fact 2. Therefore the least period is exactly \(448\). This is a finite existence proof, with its explicit witness and exhaustive deterministic comparison as its certificate; it does not rely on a numerical solver reporting an optimum.

## Verification

Run `python3 verify.py` beside `witness.txt`. The checker uses only the Python standard library. Its direct modulo-indexed enumeration checks all \(448\) length-five circular windows and all reversal classes; a separate wraparound-string enumeration confirms the window set. It also checks absence of palindromic factors and the exact uniform symbol counts. The expected standard output is embedded as `verification_output.txt`. The enumeration is exhaustive **for this specific \(448\)-letter witness**, not an exhaustive search over all possible orientable words; it proves the lower bound but not maximality.

## Relationship to prior work

Mitchell and Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period* (arXiv:2603.18646; first publicly posted March 19, 2026), Table 4, give \(404\) as the largest known period at order \(5\), alphabet size \(4\), and the published upper bound \(452\). Their discussion identifies the search for longer periods as open. Their earlier *New orientable sequences* (arXiv:2507.02526; journal publication 2026) develops the general construction and period bounds, but its reported order-five quaternary constructions do not furnish the present \(448\)-letter example. The 2024 preprint of Gabrić and Sawada (arXiv:2407.07029) develops general large-period constructions, without a covering claim at this parameter in the literature compared here. The present statement is a **new explicit lower-bound witness**, not a revision of those construction theorems.

## Limitations

The exact value of \(\lambda(5,4)\) remains unresolved by this result; periods \(449\) through \(452\) have not been excluded. The certificate does not classify other \(448\)-period words and provides no uniform construction for other orders. Historical priority remains subject to additional literature review, and no independent scientific audit is represented.

## References

1. C. J. Mitchell and P. R. Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period*, arXiv:2603.18646, first posted 2026-03-19, especially Table 4 and §6. https://arxiv.org/abs/2603.18646
2. C. J. Mitchell and P. R. Wild, *New orientable sequences*, arXiv:2507.02526 (2025), *Acta Informatica* 63 (2026), article 14. https://arxiv.org/abs/2507.02526
3. D. Gabrić and J. Sawada, *Constructing k-ary orientable sequences with asymptotically optimal length*, arXiv:2407.07029 (2024), *Designs, Codes and Cryptography* 93 (2025), 2349–2367. https://arxiv.org/abs/2407.07029
