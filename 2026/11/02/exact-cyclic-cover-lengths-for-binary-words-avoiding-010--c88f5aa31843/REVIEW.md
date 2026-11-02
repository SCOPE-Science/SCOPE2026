# Scientific review: cyclic covers of finite `010`-avoiding words

## Correctness — PASS

The claim has precise quantifiers for every integer \(n\ge3\) and allows unrestricted supplementary windows. The required de Bruijn graph is strongly connected on nonisolated vertices; its only nonzero imbalances are one-unit sources starting `10` and sinks ending `01`, with the mutually exceptional overlap removed. A path from any sink to any source needs at least the first internal `10` position in the sink, or \(m-1\) shifts if none occurs. The explicit reversal-of-prefix map is a bijection of sinks with sources, realizes exactly that distance for each sink, and makes the graph Eulerian. Thus lower and upper bounds match. The rational generating function counts the path lengths and yields the claimed recurrence/closed form. The standalone finite checker reconstructs covers at orders 3–16, verifies the formal-series identity through degree 50 and excludes shorter covers exhaustively at orders 3–4; an independent full-graph integer min-cost-flow check matched all fourteen orders. None of these finite checks substitutes for the proof.

## Originality — PASS, with priority qualification

The 2004 Moreno–Matamala WG paper and the 2007 preprint concern exact-once cycles over a *periodically admissible* subshift language, not shortest single-circle coverage of every ordinary finite `010`-avoiding word. Cazaux–Rivals' shortest cyclic cover algorithm targets a potentially multiple-circle cover, not the connected one-cycle optimum here; its abstract and introductory material were examined, without claiming a complete negative search of the publisher full text. The 2017 restricted-word universal-cycle work addresses a different exact-once setting. Searches of the indexed mathematical literature identified distinct `000` and `001` avoidance cases, but no equivalent or stronger all-order `010`-avoidance covering theorem. The formula is not a corollary of the distinct forbidden-class statements. An unindexed paper giving this exact result remains a genuine priority risk; the unavailable publisher full text of one general cyclic-cover algorithm does not resolve every priority question, though its definition and scope are distinguishable.

## Value — PASS

This determines an infinite family of natural shortest cyclic superstring parameters, with an explicit exact nonzero augmentation cost and a constructive Eulerian algorithm. The `010` forbidden-factor orbit is the third distinct binary length-three orbit under reversal and bit complementation, after the `000` and `001` orbits, making it a structurally motivated missing class rather than an arbitrary parameter slice. The matching theorem explains the obstruction and supplies a potential reusable approach for other forbidden languages. Its value lies in a natural all-order optimum rather than a finite table alone.

## Scientific limitations and priority references

The result covers one forbidden factor of length three, binary alphabets and one cyclic cover, not general forbidden lists or a classification of minimizing cycles. The 2004 WG conference occurred June 21–23; the earliest individually verified publication date used in metadata is December 21, 2004, for the printed proceedings, not a conjectured presentation day. Relevant primary sources: Moreno–Matamala, WG 2004, DOI 10.1007/978-3-540-30559-0_14, and arXiv:0711.1695; Cazaux–Rivals, DOI 10.1016/j.jda.2016.05.001; Gardner–Godbole, arXiv:1711.07029.

Self-review: passed. Independent audit: not yet performed.
