# Scientific review: complete shortest-border profiles of binary order-five de Bruijn cycles

## Correctness — PASS

The de Bruijn condition identifies each order-five cycle with a unique Euler tour once edge `00000` is fixed. Every Euler tour determines a bijective pairing of incoming and outgoing edges at each of the 16 vertices, so the \(2^{16}\) pairing search is exhaustive. Conversely, each single-cycle edge permutation is a valid tour. A separately implemented Euler-tour depth-first enumeration produces exactly the same 2048 normalized words. No border of a rotation can have length at least five: two distinct circular positions would begin the same five-bit factor. The two independent computations of minimal borders (full prefix/suffix comparison and short centered squares) match at all 65536 cuts, and seven profile frequencies and symmetry-orbit totals agree with independently constructed partitions. These checks are backed by inspected standalone source code and complete finite search spaces, rather than output logs alone.

## Originality — PASS against inspected sources; residual risk acknowledged

Harju–Nowotka (2004) introduced binary border correlations. Blanchet-Sadri–Clader–Simpson (manuscript 2008, journal 2010) defines and studies refined minimal-border correlations, but focuses on general/partial words and related bounds rather than order-five de Bruijn classes. Holub–Müller (arXiv:1504.02222, 2015) classifies all binary words with only two unbordered conjugates; every cycle here has 8–10. Clokie–Gabric–Shallit (arXiv:1904.08187, 2019) obtains general maxima, attainability and random-word expectations for unbordered conjugates; this does not determine the de Bruijn-restricted population distribution, nor seven shortest-border-count profiles. OEIS A321162 tabulates the maximum over all binary words of a specified length, not the distribution over order-five de Bruijn cycles. Multiple targeted scientific-record searches and the accessible local historical claims yielded no equivalent implication. The closest 2004 source's full text remained inaccessible; a historical equivalent enumeration cannot be ruled out definitively.

## Mathematical value — PASS

Unbordered conjugates and local minimal borders are long-established natural string invariants. De Bruijn cycles provide an especially constrained and central class of universal cyclic words, and order five is the first full binary order with 2048 distinct cycles. The seven-cell classification gives the complete local-period spectrum, exact attainable range, nontrivial frequency distribution and symmetry-orbit structure, strengthening the simple universal upper bound. Fixed length-one and length-two border counts explain the phenomenon structurally; the remaining larger short borders capture a genuine arrangement-dependent distribution. The statement is not an arbitrary word sample or another known extremal-table recomputation.

## Limits and comparison risks

The exact result is restricted to order five, and the certificate is a finite exhaustive computation. The 2004 Harju–Nowotka paper is plausible relevant prior art but was unavailable in full; its abstract and later full papers describing its main results were inspected. The population distribution under the de Bruijn constraint may have appeared elsewhere without searchable indexing. The checker has no dependencies outside the Python standard library, but this is not independent external scientific certification.

Self-review: passed. Independent audit: not yet performed.
