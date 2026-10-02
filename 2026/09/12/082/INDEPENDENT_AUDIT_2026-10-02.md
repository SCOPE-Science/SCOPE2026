# Independent mathematical audit

## correctness

PASS

Every one of the 1458 frozen matrices was independently materialized with its original SHA-256 checked, and numeric tuples were checked distinct. Fresh exact integer arithmetic verifies both Gram identities and all row/column sums; exact GF(3) elimination gives rank 18 for every matrix. Self-orthogonality and half dimension imply self-duality, so every word has weight divisible by three. All 28560 weight-three candidates up to sign per matrix have nonzero syndrome, excluding every nonzero weight below six. A meet-in-the-middle search of 57120 signed triples produces a disjoint-support collision and an explicit weight-six word per matrix; each word is independently checked against all 36 incidence rows. The full run finished successfully in 11.431530248373747 seconds. This proves the same minimum-distance claim without relying on the old success log or rerunning 3^18 words per matrix.

## originality

PASS

The prior recorded exact searches and comparison are retained. Additionally the relevant primary sections and tables were read beyond abstracts: Rukavina--Tonchev Theorem 2.4 and Section 3 classify extremal-spanning involution designs; Harada--Ishizuka Sections 3--4 classify near-extremal codes and their Hadamard matrices, including code dimensions and distances in Section 4.3. Neither theorem implies the exact invariant for all of these archived Goethals-Seidel matrices. The claim is the archived finite construction-family dataset, not 1458 isomorphism classes or a general existence novelty inferred merely from labels.

## value

PASS

A complete exact finite barrier at the natural length-36 extremal ternary-code/design interface would be useful benchmark data: it separates plentiful rank-18 self-dual spanning from distance-12 extremality in a motivated construction family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
