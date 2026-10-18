# Independent mathematical audit

## correctness

PASS

Any six-recovery all-symbol PIR generator forces all seven nonzero codewords to have weight >=6: choose a stored column detected by each nonzero information covector; each disjoint recovery of that target must meet the support. The binary dimension-three Griesmer bound gives n>=6+3+2=11. Independently read all 924 actual certificates.tsv rows (blob 5a9d3704278c0abefc12c0e22bcc2b0e3dff37bf) and checked in a separately implemented JS decoder that all sorted six-request multisets occur once, every target lies in the XOR span of its indicated distinct 1-based coordinates, groups are pairwise disjoint, and block-size counts are 3798 singleton/1669 pair/77 triple (5,544 groups; zero errors). Zero-target recovery follows because a span contains 0. Exhaustion is only over the finite specified six-request alphabet; the lower bound is general.

## originality

PASS

Prior functional PIR at these parameters establishes eleven for repeated requests, which does not imply mixed-request service. The actual 924-request certificate closes this strictly stronger functional batch case; the 2026 all-symbol paper and published Resultary neighboring t=5 result do not supply a t=6 mixed certificate.

## value

PASS

Simultaneous arbitrary linear-functional service is a natural strictly stronger retrieval objective than repeated-target PIR or all-symbol requests. It is mathematically informative that six arbitrary queries can be served at the classical minimum Griesmer length, using at most triples of coordinates. This exact naturally defined small parameter is a meaningful benchmark for code constructions, not a toy perturbation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
