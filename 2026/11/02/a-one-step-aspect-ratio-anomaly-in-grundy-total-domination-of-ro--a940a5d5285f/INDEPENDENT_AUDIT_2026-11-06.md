# Independent mathematical audit

## correctness

PASS

Identify each rook cell with root edge of K_(m,n). Undominated rook vertices correspond precisely to root edges between unused roots plus selected isolated matching edges. For root-edge set H, potential Phi=number used roots minus number isolated selected edges gains 1 or 2 per legal addition; first nonmatching step gains 2. Thus any sequence with nontrivial component has length<=m+n-1. To attain equality, exactly one step has gain 2, no isolated selected edge survives, and the last unused root must enter at that gain-2 step. This forces a matching covering all but one root, possible iff |m-n|=1; successive attachments are forced structurally. The matching/attachment choices count product (a+1)! a! times a (a-1)! times product_(j=1)^(a-1)(2j+1). An explicit row/column sequence constructs length m+n-2 otherwise. Independent full open-neighborhood dynamic programming agrees on 2x3: 72, 3x4:12960, and multiple other boards.

## originality

PASS

Grundy total domination and its equivalence with skew zero forcing were already developed. Prior product-paper Cartesian results concern paths/cycles and their complete-graph observation concerns direct rather than Cartesian product. The inspected primary literature does not state exact rook-graph aspect-ratio formula or all equality sequences, while literature aliases remain a risk.

## value

PASS

Natural open-neighborhood longest-sequence invariant of the ubiquitous rook graph family; a single-step anomaly precisely at aspect ratio differing by one and exhaustive optimizer count expose nontrivial structure useful for both Grundy domination and skew zero forcing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
