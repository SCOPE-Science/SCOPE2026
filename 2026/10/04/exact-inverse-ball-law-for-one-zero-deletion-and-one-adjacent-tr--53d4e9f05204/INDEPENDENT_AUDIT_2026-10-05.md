# Independent mathematical audit

## correctness

PASS

In zero-gap coordinates, reversing the channel restores one zero in a gap and optionally transfers one zero between adjacent gaps. A positive donor gap contributes \((m-1)\deg(a)\) transfer constructions after removing the insertion-at-donor cases already counted by deletion-only parents; different donors cannot collide, and the two transfer directions of one interior donor have exactly one collision. This gives \(m+(2m-3)p-(m-2)e\). Optimizing support size and endpoint occupancy gives \(\lfloor n^2/2\rfloor-n+2\) and the stated even/odd extremizers. Fresh direct string-channel enumeration for every \(2\le n\le8\) reproduced the pointwise formula and maxima \(2,3,6,9,14,19,26\).

## originality

PASS

The complete Wang--Vu--Tan treatment uses the same zero-gap representation and identifies zero deletion with a coordinate decrement and adjacent transposition with a unit transfer, but focuses on code construction, decoding/list decoding and redundancy. It does not state the uncoded inverse received-word degree, its exact worst-case law, or extremizers. Ye--Ge treat forward error balls and code-size bounds. Resultary searches found no equivalent inverse-degree theorem.

## value

PASS

Worst inverse degree is a natural list-decoding/ambiguity invariant of this asymmetric channel. The theorem gives every received word's parent count, the exact global maximum, and all extremizers for every length, so it is a motivated complete classification rather than a finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
