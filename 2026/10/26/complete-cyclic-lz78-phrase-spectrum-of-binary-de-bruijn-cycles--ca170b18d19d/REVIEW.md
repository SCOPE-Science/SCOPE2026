# Review of the cyclic LZ78 phrase-spectrum

## Correctness — PASS
The claim concerns only 2048 cycles of length 32, allowing an exhaustive proof. Local incoming-to-outgoing switches give a bijection from all cyclic de Bruijn traversals to single-orbit maps among 65536 possible switches. The independently generated Euler-tour set coincides with the complete switch set. The set-based phrase parser and trie-based parser agree phrase-by-phrase across all 65536 rooted cuts. The exact six histogram bins sum to 2048; the anchored distribution sums to 2048; the certificate contains all 2048 sorted canonical representatives and is reproduced exactly by `verify.py`. The terminal-residual convention is fixed and tested.

## Originality — PASS, subject to a priority caveat
Ziv and Lempel's complete foundational paper defines incremental parsing and coding but does not enumerate order-five de Bruijn cycles or their rotation extrema. Ziv's 2014 note studies universal compression properties, while Köppl studies factorization algorithms and substring queries. Etzion–Lempel's similarly titled complexity work addresses the shortest *linear recurrence* and therefore does not imply LZ78 phrase counts. An existing separate LZ76 exhaustive-history profile for the same 2048 cycles does not imply these figures: LZ76 permits the full previous text as source, whereas the present LZ78 parse references only completed dictionary phrases. Related research-record and textual searches did not identify this exact joint table; lack of a search hit does not establish uniqueness. The possibility of older unindexed computations remains.

## Value — PASS
All order-five de Bruijn cycles have exactly the same circular length-five factor profile. Nevertheless, their dictionary-parsing behavior depends on arrangement and where a linear cut is placed. The six-class exact profile simultaneously quantifies this difference and identifies an exceptional class of 30 rotation-insensitive cycles. LZ78 is a natural compression statistic, and this is a complete reproducible classification of a nontrivial 2048-object family, rather than an arbitrary sample or a recomputation of linear complexity. No general-order theorem or coding-rate conclusion is claimed.

## Limitations
The result is finite and tied to this parsing convention. A month-only 1978 publication record is not silently converted to a precise date. Several potentially relevant indexed items were checked through substantive excerpts or abstracts rather than whole documents, leaving a limited historical-priority risk. No outside validation was performed.

Self-review: passed. Independent audit: not yet performed.
