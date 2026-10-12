# Self-review

## Claim

For the binary LCD code \(C\) of parameters \([57,8,25]_2\) displayed by Lim, An, and Kim (arXiv:2609.02096v1), expand each hexadecimal digit into four binary digits in most-significant-bit-first order and delete the three appended zero columns. Among all \(\binom{57}{2}=1596\) double punctures of this displayed representative, exactly four coordinate pairs—\(\{9,18\}\), \(\{10,30\}\), \(\{34,48\}\), and \(\{41,42\}\), with coordinates numbered from \(1\)—produce an LCD code of minimum distance \(24\). Hence a binary LCD \([55,8,24]_2\) code exists. Since the general binary linear-code bound gives \(d(55,8)=24\), it follows that \(d_{\mathrm{LCD}}(55,8)=24\). This improves the value \(23\) reached at length \(55\), dimension \(8\), in the source's reported shortest-embedding experiments to the sharp bound \(24\).

## Correctness

**PASS.** The parent matrix was reconstructed independently from the source and its stated parameters were reproduced before any puncturing. The verifier then visits all \(1596\) coordinate pairs and all \(255\) nonzero words of each relevant row span. Four and only four double punctures are LCD with minimum distance \(24\). The explicit witness has full row rank and nonsingular Gram matrix. Grassl's exact unrestricted \([55,8]_2\) optimum \(24\) supplies the matching upper bound.

## Originality

**PASS.** The closest source is Lim–An–Kim, which prints the parent \([57,8,25]_2\) code and gives an upper bound \(24\) at \((55,8)\), but its dimension-eight table reaches only \(23\) at that parameter. Exact-parameter, alias, published-finding corpus, arXiv/web, and ordinary-code-table searches found no prior LCD \([55,8,24]_2\) construction or equivalent exact-value statement. Grassl's table contains ordinary \([55,8,24]_2\) codes, which do not imply the LCD condition. A residual risk remains for obscure or poorly indexed literature.

## Value

**PASS.** The result closes the source's explicit one-unit construction gap at a natural optimal-distance invariant and determines \(d_{\mathrm{LCD}}(55,8)\) exactly. Exhaustively identifying all four optimal double punctures of the parent representative also makes the mechanism reproducible rather than accidental.

## Closest literature and limitations

The result is local to one displayed parent code and does not classify every optimal LCD \([55,8,24]_2\) code. The exact-value conclusion is nevertheless global because the ambient binary linear optimum at \((55,8)\) is \(24\).

Self-review: passed. Independent audit: not yet performed.
