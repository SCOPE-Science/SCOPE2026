# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The field convention is explicit and the standalone verifier first confirms that the
chosen residue class has multiplicative order 127. The displayed ten vectors have
\(\mathbb F_2\)-rank 10.

Scatteredness is checked in two exact ways. First, for every
\(\lambda\in\mathbb F_{128}\setminus\mathbb F_2\), the combined binary span of \(U\)
and \(\lambda U\) has dimension 20, so \(U\cap\lambda U=\{0\}\). This is equivalent to
the required condition that no \(\mathbb F_{128}\)-line meet \(U\) in binary dimension
at least two. Second, all 1023 nonzero elements of \(U\) normalize to distinct points
of \(PG(2,128)\). Both checks are exhaustive.

The maximality statement uses the standard bound
\(\dim_{\mathbb F_q}U\le\lfloor mn/2\rfloor\) for scattered subspaces with respect to a
Desarguesian spread. With \(m=7,n=3\), the bound is 10.

The coding corollary is a direct application of Borello--Polverino--Zullo,
Corollary 3.5: dimension \(m+3=10\) scattered in \(\mathbb F_{2^7}^3\) yields a
nondegenerate \([2m-3,3,m-1]_{2^m/2}=[11,3,6]_{2^7/2}\) rank-metric intersecting code.

## Originality

PASS, qualified as to the best of our knowledge.

The 2026 Borello--Polverino--Zullo paper explicitly reduces extremal
\([2m-3,3,d]\) existence to scattered subspaces of dimension \(m+3\), proves the even
\(m\) case, and states that odd \(m\) remains largely open. The smallest admissible odd
case is \(m=7\). Searches for the exact binary parameter under rank-metric, scattered
linear-set, Desarguesian-spread, and projective formulations did not locate a published
rank-10 scattered subspace in \(\mathbb F_{128}^3\) or an
\([11,3,6]_{2^7/2}\) rank-metric intersecting code.

The Lia--Longobardi--Marino--Trombetti odd-\(m\) constructions have rank \(m+2\),
which is 9 at \(m=7\), and therefore do not imply this extremal instance. Higher-dimensional
exceptional-scattered-sequence constructions were also checked at the level of their
stated parameter families and do not evidently cover this three-dimensional binary
rank-10 instance.

Residual risk remains from older finite-geometry literature, computational tables,
theses, or conference material using a spread-theoretic formulation that may not be
well indexed. The result should therefore be read as a concrete explicit construction
and a to-the-best-of-our-knowledge closure of one open parameter instance, not as a
guarantee of first discovery.

## Value

PASS.

The construction fills the smallest odd-\(m\) extremal instance left open by a recent
structural theorem, at the smallest field \(q=2\). It is compact, exactly checkable,
and immediately yields a new extremal rank-metric intersecting-code parameter instance.
The certificate may also be useful as a seed for classification or lifting searches.

## Limitations

The result treats only \((q,m)=(2,7)\). It does not settle other odd \(m\), does not
provide a symbolic infinite family, and does not classify the equivalence class or
automorphism group of the scattered space. The proof of existence is an exact finite
certificate rather than a conceptual construction formula.

No independent validation, peer review, or formal proof assistant verification is asserted.
