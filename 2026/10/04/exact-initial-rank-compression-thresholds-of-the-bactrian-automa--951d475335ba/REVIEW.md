# Independent mathematical audit

## correctness

PASS

The half-range compression law follows from a genuine infinite argument, not the finite verifier. After the first effective \(a\), the image lies in \(R=\{1,\ldots,n-2\}\). Direct action analysis shows that every word of length at most three is injective on \(R\), while among length-four words only \(b^3a\) creates a collision and it creates exactly one. Hence a further one-state loss costs at least four letters and a two-state loss at least five. Combining these local costs gives the lower bounds \(5k\) and \(5k+1\), while the two displayed periodic words have the claimed disjoint hole sets throughout deficiency \(\le(n+1)/2\). A fresh independent power-set BFS for \(n=5,7,9\) reproduced the initial profiles \((1,1,5)\), \((1,1,5,6)\), and \((1,1,5,6,10)\).

## originality

PASS

The defining Bactrian paper proves the endpoint reset threshold \((n-1)(n-2)\) and develops the full-reset coin argument, but does not state shortest words for each intermediate rank. The later slowly-synchronizing paper again treats endpoint synchronization. Resultary searches under rank, image size, deficiency, compressing word and subset compression returned no implication-equivalent half-range profile. The local spacing lemma plus explicit periodic hole propagation are additional structure not forced by the endpoint reset theorem.

## value

PASS

Intermediate rank is a natural invariant of a classical slowly synchronizing extremal family. The theorem resolves an entire growing half-range, exhibits alternating one-state/two-state compression costs, and gives sharp words rather than an arbitrary finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
