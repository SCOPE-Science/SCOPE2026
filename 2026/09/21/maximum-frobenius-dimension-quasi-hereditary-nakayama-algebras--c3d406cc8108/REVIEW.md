# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness: PASS

The proof was checked at the level of the Kupisch-series and uniserial-module
identities.

For a cyclic Nakayama algebra, the lifted endpoints
\(\rho_i=i+c_i\) are nondecreasing and satisfy
\(\rho_{i+n}=\rho_i+n\). If \(S_0\) has projective dimension \(2\), the explicit
second syzygy gives \(\rho_a=\rho_1\) for \(a=c_0\). Monotonicity therefore
forces the plateau \(\rho_1=\cdots=\rho_a\). Periodicity then forces
\(a\le n\), and comparing with \(\rho_n\) forces the second plateau parameter
\(b\le n\). These two inequalities are what keep all projective and injective
lengths below \(2n\).

The injective-start formula
\[
\lambda_s=\min\{i:\rho_i>s\}
\]
was checked against the co-Kupisch construction. It gives
\[
\ell(I_s)>n\iff c_s>n,
\]
and on the long indices it yields the common top \(S_1\). The standard
uniserial Hom formula then shows that a two-dimensional Hom requires both
modules to be long. Only \(P_1\) contains the long-injective top twice, and
the earlier of those two occurrences is allowed only for \(I_{q-1}\).
Therefore at most one of the \(n^2\) summands in
\(\operatorname{Hom}_A(D(A),A)\) can have dimension \(2\), with every other
summand of dimension at most \(1\).

The equality family was checked directly: its simple \(S_0\) has projective
dimension \(2\), its co-Kupisch series is
\((n,n+1,2,3,\ldots,n-1)\), every injective has top \(S_1\), and exactly one
Hom space has dimension \(2\) while all others have dimension \(1\).

The finite verification artifact independently reproduces the maxima
\(5,10,17,26,37\) for \(2\le n\le6\).

## Originality: PASS, to the best of our knowledge

The 2020 MathOverflow question explicitly asks for this maximum, records the
initial sequence, and conjectures \(n^2+1\). The currently accessible page has
no answer.

Targeted searches were made for combinations and synonyms of:
“Frobenius dimension”, “Frobdim”, “Hom(D(A),A)”, “Nakayama algebra”,
“serial algebra”, “quasi-hereditary Nakayama”, and the numerical expression
“n^2+1”.

The classical Uematsu--Yamagata paper supplies the quasi-heredity criterion
used in the proof; it is not a Frobenius-dimension result. The
Marczinzik--Sen paper gives modern structural characterizations of
quasi-hereditary Nakayama algebras and restates the projective-dimension
criterion, but does not state the Frobenius-dimension maximum.

The full text of the July 2026 preprint *Bounds on Frobenius dimension*
(arXiv:2607.15999) was inspected because it is the most directly relevant
recent work on the invariant. It treats global bounds in terms of
\(\dim_k A\), low-dimensional algebras, and truncated path algebras; full-text
search gives no occurrence of “Nakayama”, “quasi-hereditary”, or “serial”.
Thus it does not appear to cover this theorem.

The 2015 nearly-Frobenius paper develops general constructions and a
combinatorial algorithm for certain gentle algebras, but the searches did not
locate the present extremal theorem or the unique-double-Hom mechanism.

Residual risk remains because the argument becomes short after combining
standard uniserial combinatorics with the old projective-dimension-\(2\)
criterion. An implicit consequence in older serial-ring literature or an
unindexed source cannot be excluded. No concrete source found in the search
substantially suggests prior coverage.

## Value: PASS

The result settles an explicit 2020 extremal question for all \(n\ge2\), not
just additional computed cases. It also gives a structural reason for the
simple formula: quasi-heredity creates a plateau in the lifted Kupisch
endpoints, which allows at most one “wrap-around” second map from an
indecomposable injective to an indecomposable projective. The explicit equality
family proves sharpness uniformly.

## Scope and limitations

The theorem is stated for split basic finite-dimensional Nakayama algebras.
It resolves the maximum problem (Question 2 of the cited post) but does not
settle the separate lower-bound question \(F(A)\ge\operatorname{gldim}(A)\).
The finite computation is corroborative only; the general claim rests on the
symbolic proof.
