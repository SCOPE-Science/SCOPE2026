# Independent mathematical audit

## correctness

PASS

An order-n de Bruijn cycle is an Euler circuit of the directed de Bruijn graph with vertices length n-1 and arcs length n. Prescribing an (n+1)-word is equivalent to demanding two specified arcs e and f be consecutive. Identical arcs arise exactly for constants and are impossible. For distinct arcs contracting the two-arc path to a shortcut gives a balanced directed graph; such a graph is Eulerian iff its nonisolated support is weakly connected. Deleting any middle vertex leaves the other vertices connected because a lower-order de Bruijn Hamilton cycle supplies a spanning path after deletion. Only the middle vertex can be separated by removing e,f: nonconstant vertices retain nonloop incident arcs for q≥2; constant vertices retain the loop and q-2 other incident edges unless q=2, when choosing the two unique nonloop entering and exiting arcs isolates them. This yields precisely ba^(n-1)b with a≠b in binary. Independently enumerated all candidate shortcut circuits at (q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2), matching the exact forbidden sets. These finite checks do not replace the Eulerian all-q,n proof.

## originality

PASS

Primary published random-generation and arbitrary-length de Bruijn analogues were compared: an Euler sampling algorithm and a single-cycle factor-frequency illustration do not automatically give positive support for each prescribed consecutive arc pair. The complete q,n classification appears original among inspected sources, but Dayhoff 1984 studies prescribed words and is a plausible inaccessible prior equivalence.

## value

PASS

Exact support of a single next-order factor under random or enumerated de Bruijn cycles is a natural and precisely motivated combinatorial invariant. The all-parameter theorem exhibits a genuinely exceptional binary obstruction and classifies feasible motifs constructively, an independent exact fact useful to sequence design and sampling beyond mere sequence existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
