# Self-review

## Correctness
PASS. The code contains every singleton characteristic vector, so the message map has rank \(k\). For an \(r\)-space \(U\) of messages, the inactive face coordinates are exactly \(D\cap U^\perp\). Every \((k-r)\)-space \(W\) has an information set \(P\) of \(k-r\) coordinate positions; projection on \(P\) is injective on \(W\), and downward closure sends every projected face to \(\Delta|_P\). Hence \(|D\cap W|\le|\Delta|_P|\), with equality for the coordinate space \(\mathbb F_q^P\). This proves both displayed formulas and all quantifiers. Boundary cases \(r=1\) and \(r=k\) match the published distance and code length.

## Originality
PASS. The 2026 source treats arbitrary abstract simplicial complexes but proves a first-weight/minimum-distance result. The closest primary generalized-weight paper, arXiv:2310.11873v1, gives the standard subspace-intersection formulation and explicitly states that the general simplicial-complex maximum is difficult before treating special cases. Searches for the source title combined with “generalized Hamming weights,” “information set,” “coordinate subspace,” and “arbitrary simplicial complex” did not locate the sharp projection formula. The current and prior ledgers were also checked for statement-level overlap; their generalized-weight entries concern different code families and do not imply this arbitrary-complex theorem.

## Value
PASS. The result replaces an all-subspaces optimization by a purely combinatorial induced-subcomplex maximum, simultaneously computes every generalized Hamming weight of the arbitrary-complex family, explains field independence, and recovers the source's minimum-distance theorem as the first case. This is a structural reduction rather than a routine parameter increment.

## Closest literature and limitations
The closest literature is Lorite López--Camazón Portela--López Ramos (DOI 10.3934/math.2026414) for the arbitrary characteristic-face construction and Liu--Zheng--Lu--Wang (arXiv:2310.11873v1; DOI 10.1016/j.disc.2024.114240) for generalized weights of related simplicial defining-set codes. The claim is limited to the characteristic-face code and leaves the induced-subcomplex maximization problem itself to the combinatorics of \(\Delta\).

Self-review: passed. Independent audit: not yet performed.
