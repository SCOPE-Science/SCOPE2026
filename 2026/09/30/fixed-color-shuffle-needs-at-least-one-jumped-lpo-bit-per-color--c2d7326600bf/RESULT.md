# Fixed-color shuffle needs at least one jumped-LPO bit per color
## Finding
For every integer \(m\geq 2\), let \(\mathsf{cShuffle}_m\) be the fixed-\(m\)-color color-output shuffle problem for colorings of \(\mathbb Q\), in the notation of Pauly, Pradic, and Soldà. Then
\[
\mathsf{cShuffle}_m\not\leq_{\mathrm W}(\mathsf{LPO}')^n
\qquad\text{for every }n<m.
\]
Combining this with their lower bound
\[
(\mathsf{LPO}')^{m-1}\leq_{\mathrm W}\mathsf{cShuffle}_m
\]
gives the strict inequality
\[
(\mathsf{LPO}')^{m-1}<_{\mathrm W}\mathsf{cShuffle}_m
\qquad(m\geq2).
\]
In the first nontrivial case, their upper bound and reverse nonreduction specialize to
\[
\mathsf{cShuffle}_2\leq_{\mathrm W}(\mathsf{LPO}')^2
\quad\text{and}\quad
(\mathsf{LPO}')^2\not\leq_{\mathrm W}\mathsf{cShuffle}_2.
\]
Hence Question 30 of that work is completely resolved for two colors:
\[
\mathsf{LPO}'<_{\mathrm W}\mathsf{cShuffle}_2<_{\mathrm W}(\mathsf{LPO}')^2.
\]
Equivalently, any reduction of \(\mathsf{cShuffle}_m\) to a finite power of \(\mathsf{LPO}'\) requires at least \(m\) parallel calls.

## Assumptions and scope
Inputs to \(\mathsf{cShuffle}_m\) are \(m\)-colorings of \(\mathbb Q\). An output is the nonempty set of colors occurring on a shuffle interval, meaning that each output color is dense in that interval and no color outside the output set occurs there.

The argument uses ordinary Weihrauch reducibility. The target \((\mathsf{LPO}')^n\) is single-valued with discrete codomain \(2^n\), so it has exactly \(2^n\) possible output values.

The cited source proves
\[
(\mathsf{LPO}')^n\leq_{\mathrm W}\mathsf{cShuffle}_{n+1},
\qquad
(\mathsf{LPO}')^n\not\leq_{\mathrm W}\mathsf{cShuffle}_{n},
\]
and
\[
\mathsf{cShuffle}_m\leq_{\mathrm W}(\mathsf{LPO}')^{2^m-2}.
\]
It explicitly asks for the relationship between the individual powers \((\mathsf{LPO}')^n\) and \(\mathsf{cShuffle}_m\).

## Proof
We first isolate a finite-output obstruction.

Call a discrete value \(y\) a persistently uniquely forceable output of a problem \(F\) if every finite prefix of an input that is compatible with the domain of \(F\) has an extension \(x\) with
\[
F(x)=\{y\}.
\]
Suppose \(F\leq_{\mathrm W}G\), where \(G\) is single-valued and has only \(s\) possible discrete output values. Then \(F\) has at most \(s\) distinct persistently uniquely forceable outputs.

To prove this, fix a Weihrauch reduction with forward functional \(H\) and backward functional \(K\). Choose a realizer of \(G\) that returns one fixed canonical name for each discrete output value. Assume that \(y_0,\ldots,y_s\) are distinct persistently uniquely forceable outputs of \(F\). Starting with the empty input prefix, choose an extension \(x_0\) having unique output \(y_0\). Let \(a_0\) be the discrete value returned by \(G(H(x_0))\). Since \(K\) outputs \(y_0\) from \(x_0\) and the canonical name of \(a_0\), continuity gives a finite prefix \(\sigma_0\prec x_0\) on which the output is already committed to \(y_0\).

Inductively, after obtaining \(\sigma_j\), extend it to an input \(x_{j+1}\) whose unique output is \(y_{j+1}\), and let \(a_{j+1}\) be the value of \(G(H(x_{j+1}))\). If \(a_{j+1}=a_i\) for some \(i\leq j\), then \(x_{j+1}\) extends \(\sigma_i\) and the target realizer supplies the same canonical output name as at stage \(i\). The continuity commitment at \(\sigma_i\) would force \(K\) to output \(y_i\), contradicting the fact that \(x_{j+1}\) has the unique valid output \(y_{j+1}\). Thus the \(a_j\) are pairwise distinct, requiring at least \(s+1\) target values, a contradiction.

Now consider \(\mathsf{cShuffle}_m\). Every nonempty subset \(C\subseteq m\) is persistently uniquely forceable. Indeed, start from any finite partial coloring of the fixed computable presentation of \(\mathbb Q\). Extend it so that, outside the finitely many already colored points, every color in \(C\) is dense in every nonempty rational interval, while colors outside \(C\) occur nowhere else. Such an extension is computable from the finite prefix and \(C\): enumerate a countable basis of rational intervals and place fresh points of each color in \(C\) into every basis interval.

For the resulting total coloring, choose a rational interval avoiding the finitely many preassigned points whose colors lie outside \(C\). On that interval, precisely the colors in \(C\) occur, and every one of them is dense. Hence \(C\) is a valid output. It is the unique output: no color outside \(C\) is dense anywhere, while every color in \(C\) is dense in every nonempty interval, so no proper subset of \(C\) can be the full color set of a shuffle interval.

Therefore \(\mathsf{cShuffle}_m\) has
\[
2^m-1
\]
distinct persistently uniquely forceable outputs. If
\[
\mathsf{cShuffle}_m\leq_{\mathrm W}(\mathsf{LPO}')^n,
\]
the finite-output obstruction gives
\[
2^m-1\leq 2^n.
\]
For \(n<m\), however,
\[
2^n\leq2^{m-1}<2^m-1,
\]
a contradiction. Thus \(\mathsf{cShuffle}_m\not\leq_{\mathrm W}(\mathsf{LPO}')^n\) whenever \(n<m\).

Taking \(n=m-1\) and combining with the cited reduction \((\mathsf{LPO}')^{m-1}\leq_{\mathrm W}\mathsf{cShuffle}_m\) yields strictness. For \(m=2\), the cited upper bound becomes \(\mathsf{cShuffle}_2\leq_{\mathrm W}(\mathsf{LPO}')^2\), while the cited reverse nonreduction gives \((\mathsf{LPO}')^2\not\leq_{\mathrm W}\mathsf{cShuffle}_2\). Together with the new lower separation this proves the displayed two-color strict sandwich.

## Verification
The proof was reconstructed at the level of represented-space continuity rather than by output counting alone. The key point is that every finite input prefix can still be extended to make any prescribed nonempty color set the unique shuffle output. This permits a nested-prefix argument that turns a repeated target value into a contradiction with continuity of the backward functional.

The edge cases were checked explicitly. For singleton \(C\), all unassigned rationals receive that color, while the finitely many forced other colors can be avoided by an interval. For \(C=m\), every color is made dense everywhere. For arbitrary finite prefixes, finitely many colors outside \(C\) do not obstruct uniqueness because an interval can avoid their finitely many occurrences.

The included `verify.py` checks the finite cardinal inequalities underlying the separation for \(2\leq m\leq20\), including the threshold fact that \(2^m-1>2^n\) exactly throughout the asserted range \(n<m\).

## Relationship to prior work
Pauly, Pradic, and Soldà prove the two complementary families
\[
(\mathsf{LPO}')^n\leq_{\mathrm W}\mathsf{cShuffle}_{n+1}
\quad\text{and}\quad
(\mathsf{LPO}')^n\not\leq_{\mathrm W}\mathsf{cShuffle}_{n},
\]
as well as the general upper bound
\[
\mathsf{cShuffle}_m\leq_{\mathrm W}(\mathsf{LPO}')^{2^m-2}.
\]
They then ask explicitly for the relationship between the individual parameters \(n\) and \(m\).

A later study of indivisibility and uniform computational strength summarizes this point as still unresolved, noting that the precise relationship between the number of colors and the number of parallel \(\mathsf{LPO}'\) instances was left open. The present argument supplies a general necessary condition \(n\geq m\) for reductions in the direction \(\mathsf{cShuffle}_m\leq_{\mathrm W}(\mathsf{LPO}')^n\), and this combines with the existing upper bound to settle the complete two-color comparison.

## Limitations
For \(m\geq3\), the result does not determine the least \(n\) for which
\[
\mathsf{cShuffle}_m\leq_{\mathrm W}(\mathsf{LPO}')^n.
\]
It only raises the general lower bound to \(n\geq m\), while the published upper bound remains \(n=2^m-2\).

The finite-output obstruction requires a single-valued target with finitely many discrete output values, or an equivalent fixed canonical-output setup. It should not be applied unchanged to arbitrary multivalued targets.

The originality assessment is best-of-knowledge. The explicit source question and later literature confirm that the parameter relationship remained open, and targeted searches did not locate the cardinality obstruction or the resulting two-color strict sandwich.

## References
Arno Pauly, Cécilia Pradic, and Giovanni Soldà, “On the Weihrauch degree of the additive Ramsey theorem,” arXiv:2301.02833v1, 7 January 2023; later published in *Computability* 13(3–4), DOI:10.3233/COM-230437.

Kenneth Gill, “Indivisibility and uniform computational strength,” arXiv:2312.03919, first public version 6 December 2023; later published in *Logical Methods in Computer Science* 21(2), DOI:10.46298/lmcs-21(2:22)2025.
