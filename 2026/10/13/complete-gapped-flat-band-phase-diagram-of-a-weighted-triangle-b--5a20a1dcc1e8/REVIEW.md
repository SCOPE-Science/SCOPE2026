# Independent mathematical audit

## correctness

PASS

For Bloch H(z) with H_AB=p+sz,H_BA=p+sz^{-1}, H_AC=r,H_BC=q and diagonals QA,QB,QC, the exact Laurent coefficient of z+z^-1 in det(H−E) is s(qr−p(QC−E)); as s,p>0, a flat band forces E=QC−g, g=qr/p>0. At that energy, the Schur complement of C is [[alpha,sz],[sz^-1,beta]] with alpha=QA−QC+g−pr/q and beta=QB−QC+g−pq/r. Its determinant alpha*beta−s² gives iff flat locus. With alpha*beta=s² both have same nonzero sign. Sylvester inertia with positive g places zero eigenvalue at bottom for alpha>0 and middle for alpha<0; rank 2 for all Bloch phases and compact unit circle imply positive isolation. Exact Laurent nullvector (−sz,alpha,(rsz−q alpha)/g) is nowhere zero and provides two-cell CLS spanning the infinite eigenspace by Laurent polynomial density. Independent SymPy determinant, nullvector and polynomial equalities passed.

## originality

PASS

For the exact three-orbit, four-edge triangle-plus-bridge motif, the equation alpha*beta=s², unique energy, strict positive spectral gap and bottom/middle-band split are derived from a specific Laurent coefficient and Schur complement. The inspected general semialgebraic/generic-nonexistence theorems cannot identify this complete exceptional quadric or the band-order dichotomy. Other named triangle/diamond lattices use different matrices. Best-of-knowledge original motif-specific classification.

## value

PASS

Exact parameter-tuning locus and strict gap and band placement for a minimal three-site connected triangle-bridge motif is a motivated complete phase diagram. It identifies a curved exceptional surface with two distinct localized-state regimes, rather than a single tuned example or generic absence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
