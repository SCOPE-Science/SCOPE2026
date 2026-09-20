# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The explicit counterexample was checked directly from the definitions.  On
\(X=C^1[0,1]\) with \(\|f\|_\sigma=|f(0)|+\|f'\|_\infty\), pointwise
conjugation \(Tf=\overline f\) is a conjugate-linear surjective isometry and
\(T^2=I\).  For \((\lambda_1,\lambda_2)=(1,i)\),
\[
P_1=(T-iI)/(1-i),\qquad P_2=(I-T)/(1-i)
\]
satisfy \(P_i^2=P_i\), \(P_1P_2=P_2P_1=0\), \(P_1+P_2=I\), and
\(P_1+iP_2=T\).  Both maps are nonzero and distinct.  Thus the family is a
GBCI although \(\lambda_1+\lambda_2\ne0\).  On the constant \(f=i\),
\((P_1-P_2)f=2-i\), whose norm is \(\sqrt5\), so the family is not BCI.

The general conjugate-linear lemma was checked with scalar conjugation
handled explicitly.  The identity
\[
\overline{\lambda_1-\lambda_2}
=-(\lambda_1-\lambda_2)/(\lambda_1\lambda_2)
\]
for unimodular phases gives \(TP_1=\lambda_1P_1\) whenever \(T^2=I\), hence
idempotency.  Conversely, for complementary idempotents associated with a
conjugate-linear \(T\), conjugating the scalar coefficients in the second
application of \(T\) gives \(T^2=P_1+P_2=I\).  No complex-linearity is used.

The coordinate map \(Jf=(f(0),f')\) is an isometric isomorphism from
\(C^1[0,1]\) onto \(\mathbb C\oplus_1C[0,1]\).  Under this map, the four
Miura forms split into linear and conjugate-linear blocks.  For a
complex-linear block \(S\), the interpolation idempotency condition is the
usual quadratic
\((S-\lambda_1I)(S-\lambda_2I)=0\); for a conjugate-linear block it is
\(S^2=I\).  Applying these independently proves the stated Form II and Form
III criteria.

For Form IV both blocks are conjugate-linear.  The scalar block
\(a\mapsto c\bar a\) squares to the identity because \(|c|=1\); the function
block
\[
Wh(t)=\beta(t)\overline{h(\phi(t))}
\]
satisfies
\[
W^2h(t)=\beta(t)\overline{\beta(\phi(t))}h(\phi^2(t)).
\]
Thus the advertised conditions are exactly equivalent to \(T^2=I\).
The non-BCI assertion is forced already on constants: two nonzero
complementary real rank-one projections of the Euclidean plane cannot have
all independent phase combinations isometric.  The proof uses the varying
cross term in \(|\alpha u+\gamma v|^2\).

No complementability, compactness, or inheritance statement is used.

## Originality

**PASS, to the best of our knowledge.**

The primary source inspected was H. Kumar, H. Kumar and A. Bin Abu Baker,
*Structure of Generalized bi-circular idempotents and isometric reflections
on \(C^1[0,1]\)*, arXiv:2609.18967v1, submitted 4 August 2026.  Its abstract
states that a GBCI is either associated with antipodal phases or is
bi-circular.  Its preliminary section explicitly allows nonlinear maps,
records real-linearity of associated isometries, and quotes Miura's four
forms.  Theorems 3.2--3.4 give the corresponding semilinear classifications.
The pointwise-conjugation example satisfies those definitions but contradicts
the abstract dichotomy.

The closest historical source is F. Botelho and T. Miura's 2019 corrigendum
to their 2018 JMAA paper.  That corrigendum explicitly says an earlier
classification of GBCIs on spaces of continuously differentiable functions
was incomplete because one case was omitted, producing additional examples.
This is strong prior art for the general warning that nonreflection GBCIs
exist, so no novelty is claimed for that broad phenomenon.  The inspected
2026 v1 cites the corrigendum but nevertheless makes the new
antipodal-or-BCI assertion addressed here.

Searches by the current arXiv identifier, theorem topic, conjugate-linear /
semilinear formulations, generalized bi-circular idempotents, and the older
corrigendum did not locate a public correction of arXiv:2609.18967v1 or the
specific universal lemma and corrected Form IV criterion stated here.
Related 2026 work on generalized idempotents in analytic function spaces was
also considered, but it does not supply a located correction of this
\(C^1[0,1]\) statement.

The semilinear interpolation lemma is elementary and could have appeared
implicitly in older nonlinear-idempotent or real-linear isometry literature.
The originality claim is therefore deliberately narrow: the explicit
counterexample to the current v1, the diagnosis of the conjugate-linear
phase cancellation, and the corrected semilinear block criteria are claimed
only to the best of our knowledge.

## Value

**PASS.**

The counterexample invalidates the main dichotomy stated in the abstract of a
current functional-analysis preprint, not merely a peripheral estimate.
The correction also explains the mechanism: on a conjugate-linear block,
the second application of the associated isometry conjugates the phase, so
the complex-linear quadratic relation is replaced by an involution relation
that is independent of the chosen phase pair.  This produces a reusable
criterion rather than an isolated counterexample.

The Form IV replacement is exact and simple, while the block formulation
shows how to repair the mixed Forms II and III without disturbing the
complex-linear Form I analysis.

## Limitations

This result concerns the current v1 of arXiv:2609.18967 and may become moot
if a later version corrects the statements.  It does not classify GBCIs on
arbitrary normed spaces and does not assert that every result in the source
paper is invalid.  Form I is not challenged.  The 2019 corrigendum is
acknowledged as prior art for earlier incompleteness, and the elementary
semilinear lemma itself is not claimed to inaugurate a new general theory.

No independent validation or independent audit has been performed.
