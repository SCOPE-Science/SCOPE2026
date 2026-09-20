# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The argument reduces to two exact facts from Moradi's construction and one
norm calculation.

First, Moradi places both \(\tau_\infty\) and \(\gamma\) in the weak-star
closure \(K\) of normalized traces of finite-dimensional unital
representations. Because \(A\) is separable, the diagonal approximation
argument used at the end of Lemma 3.1 applies to every element of \(K\),
not only to the particular trace \(\tau\). Thus
\(\tau_\infty,\gamma\in T_{\mathrm{qd}}(A)\).

Second, Theorem 4.1 gives
\(\nu(e^0)=\nu(e^1)=1/2\) for every quasidiagonal trace \(\nu\), while
Lemma 3.2 gives
\(\mu_0(e^1-e^0)=-1\) and
\(\mu_1(e^1-e^0)=1\). Since \(e^0,e^1\) are complementary projections,
\(h=e^1-e^0\) is a norm-one self-adjoint unitary. It therefore supplies
the lower bound
\[
\operatorname{dist}(\omega_{c,t},T_{\mathrm{qd}}(A))
\ge c|2t-1|.
\]

For the upper bound, the quasidiagonal midpoint
\(q_c=(1-c)\gamma+c\tau_\infty\) satisfies
\[
\omega_{c,t}-q_c
=
c(t-\tfrac12)(\mu_1-\mu_0).
\]
The same unitary \(h\) shows
\(\|\mu_1-\mu_0\|=2\), so the norm of this difference is exactly
\(c|2t-1|\). Lower and upper bounds coincide.

The faithfulness claim uses only the strictly positive coefficient of
Moradi's faithful trace \(\gamma\) when \(c<1\). Amenability follows from
the standard fact that quasidiagonal traces are amenable and that amenable
traces form a face: \(q_c\) is the midpoint of the two endpoints, so both
endpoints are amenable, hence so is their entire segment.

No complementability, compactness, duality, or inheritance assertion is
used implicitly.

## Originality

**PASS, to the best of our knowledge.**

The primary source arXiv:2609.18793v1 was inspected in full where relevant.
It states an asymmetric face-property counterexample, constructs
\(\tau_\infty,\gamma,\mu_0,\mu_1\), proves the sector decomposition, and
proves that all quasidiagonal traces have equal sector mass. It explicitly
remarks that both \(\mu_0\) and \(\mu_1\) are non-quasidiagonal.

The inspected paper does not state that its construction yields a
one-parameter family of faithful quasidiagonal midpoints of faithful
non-quasidiagonal endpoints, nor does it compute the norm distance from
those chords to \(T_{\mathrm{qd}}(A)\). Searches using exact and synonymous
phrasing around quasidiagonal traces, midpoint decompositions, norm
distance, faithful non-quasidiagonal traces, and affine/trace-simplex
geometry did not locate the formula
\[
\operatorname{dist}(\omega_{c,t},T_{\mathrm{qd}}(A))
=c|2t-1|.
\]

The standard ingredients are not claimed as original: weak-star diagonal
approximation in the separable setting, the norm-two separation of states
supported on complementary projections, and the faciality of amenable
traces are prior art or immediate facts.

Residual risk remains that older quasidiagonal-trace literature contains
an abstract convex-geometric lemma equivalent to the norm calculation.
The specific application to Moradi's newly posted construction, including
the faithful family for every \(0<c<1\), could not have appeared in that
form before the construction itself. No inaccessible source supplied
concrete evidence of prior coverage.

## Value

**PASS.**

Moradi's theorem establishes existence of a faithful quasidiagonal trace
with a non-quasidiagonal component. The refinement here shows a stronger
and quantitatively rigid phenomenon: for every \(c\in(0,1)\) there is a
faithful quasidiagonal trace that is the midpoint of two faithful amenable
non-quasidiagonal traces, each exactly distance \(c\) from the
quasidiagonal trace set. The entire connecting chord has a closed-form
distance profile and contains exactly one quasidiagonal point.

This distinguishes a robust norm-geometric failure of faciality from an
example that could have been caused only by a nonfaithful boundary
component or by an arbitrarily small perturbation.

## Scientific limitations

The theorem is specific to Moradi's algebra. It does not classify
\(T_{\mathrm{qd}}(A)\), does not assert that sector balance is sufficient
for quasidiagonality, and does not claim analogous midpoint geometry for
all C*-algebras whose quasidiagonal traces fail to form a face.

The source is currently arXiv:2609.18793v1, so later revisions may
incorporate or alter related observations. Originality should therefore be
understood relative to the inspected version and the literature search
described above.
