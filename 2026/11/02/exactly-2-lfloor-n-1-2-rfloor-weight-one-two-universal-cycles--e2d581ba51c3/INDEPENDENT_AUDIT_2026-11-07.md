# Independent mathematical audit

## correctness

PASS

For every n>=2 the directed de Bruijn-type overlap graph has one directed edge per length-n binary word of Hamming weight 1 or 2 and vertices of length n-1 with weights 0,1,2. Weight-0 and weight-2 vertices have forced outgoing edges; weight-1 states have two. A cyclic universal word corresponds bijectively to an edge-distinct Euler tour normalized at the unique root edge 0^(n-1)1. BEST gives the number as the in-arborescence count. At weight-1 index i, append-0 moves to i+1 (or root) and append-1 then forced shifts moves to n-2-i; an upper-half append-one creates a closed interval away from root, so is forbidden. Every independent lower-half choice strictly increases the index until root and is valid. Exactly floor((n-1)/2) independent choices yield 2^floor((n-1)/2); all lengths n>=2 and rotation primitivity covered. Independent exact root-Laplacian cofactors n=2..8 reproduce counts and edge totals; all-n follows from forest bijection.

## originality

PASS

Ruskey-Sawada-Williams and Sawada-Williams-Wong establish existence and construction of fixed/weight-range Ucycles. Sawada-Gabric 2025 develops sampling via Eulerian arborescences and has small examples (including n=3). The full all-n closed count and classification of forced/free arborescence choices are not in primary material inspected; a small case count is known and explicitly not claimed new.

## value

PASS

Exact enumeration up to cyclic rotation of a natural shorthand de Bruijn/weight-window class is a useful invariant, stronger than existence. The arborescence mechanism isolates the binary choice structure and all-n closed formula, potentially informing exact uniform generation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
