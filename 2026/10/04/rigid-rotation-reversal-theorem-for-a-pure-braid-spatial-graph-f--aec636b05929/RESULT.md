# Rigid-rotation reversal theorem for a pure-braid spatial-graph family
## Finding
For the fixed \(8\)-vertex, \(12\)-edge cubic pure-braid family \(\mathcal N_w\) introduced by Akgün, Yan, Liu, Chen and Lee, let
\[
w\in\{A,B\}^\ast,\qquad A=\sigma_1^2,\qquad B=\sigma_2^2.
\]
Write \(\operatorname{rev}(w)\) for the reversed word. Then
\[
\mathcal N_w\cong_{\mathrm{ambient}}\mathcal N_{\operatorname{rev}(w)}
\]
as ordinary unoriented unlabelled spatial graphs.

More precisely, before the constructor's final coordinate normalization, if \(m=|w|\), the orientation-preserving half-turn
\[
\rho_w(x,y,z)=(2m-x,\;y,\;-z)
\]
maps the constructed embedding for \(w\) exactly to the constructed embedding for \(\operatorname{rev}(w)\), up to the evident left-right graph automorphism.

Consequently both the raw and normalized Yamada polynomials satisfy
\[
\Upsilon(\mathcal N_w;Y)=\Upsilon(\mathcal N_{\operatorname{rev}(w)};Y).
\]
For \(m\ge1\), the number of ambient-isotopy classes represented by all length-\(m\) words is therefore at most
\[
2^{m-1}+2^{\lceil m/2\rceil-1},
\]
the exact number of binary words modulo reversal.

## Assumptions and scope
The statement concerns the specific pure-square constructor in the cited public source: each letter \(A\) expands to the two positive Artin generators \((1,1)\), each \(B\) to \((2,2)\), and the surrounding cubic graph and nested closure routes are those in the source notebook.

Spatial graphs are considered without vertex labels, edge orientations or a distinguished left/right direction. If implementation vertex names are retained, the half-turn realizes the graph automorphism
\[
LT\leftrightarrow RT,\quad LMB\leftrightarrow RMB,\quad LMC\leftrightarrow RMC,\quad LB\leftrightarrow RB.
\]
No assertion is made that reversal is the only ambient-isotopy coincidence among words.

## Proof
Let \(w=w_1\cdots w_m\). Its expanded braid has \(n=2m\) positive generators \(g_0,\ldots,g_{n-1}\), each in \(\{1,2\}\). The source constructs the braid body in the \(x\)-direction. On one generator step \(k\), with parameter \(t\in[0,1]\), the moving strands use
\[
x=k+t,\qquad
s(t)=\frac12-\frac12\cos(\pi t),\qquad
b(t)=\sin(\pi t),
\]
with \(y\) obtained by \(s(t)\)-interpolation between the two participating lanes and \(z=\pm c\,b(t)\), where the positive sign marks the over-strand.

Apply the rigid rotation
\[
\rho_w(x,y,z)=(n-x,y,-z).
\]
It is a rotation through angle \(\pi\) about the line \(\{(m,y,0):y\in\mathbb R\}\), so it is orientation preserving and connected to the identity through rotations about the same line.

Set \(u=1-t\). Then
\[
n-(k+t)=(n-1-k)+u,
\]
while
\[
s(1-u)=1-s(u),\qquad b(1-u)=b(u).
\]
Thus the \(y\)-interpolation on step \(k\) becomes the same interpolation traversed from the terminal lanes back to the initial lanes on step \(n-1-k\). At the reversed step the two participating strand identities have exchanged lanes. The sign change \(z\mapsto-z\) therefore makes the strand now occupying the upper lane the over-strand, exactly reproducing the same positive Artin generator. Hence \(\rho_w\) sends the expanded generator sequence to
\[
g_{n-1}\cdots g_0.
\]

Each block is internally palindromic:
\[
A=(1,1),\qquad B=(2,2).
\]
Therefore reversing the expanded generator sequence is exactly the expansion of \(\operatorname{rev}(w)\).

It remains to inspect the surrounding fixed graph. Since the right braid coordinate is \(x_R=n\), the same half-turn exchanges the four left boundary vertices with their four right partners. The left and right side-coupling edges and the two middle spacer edges are exchanged in pairs. The three published external closure routes use symmetric horizontal margins \(\pm3\), \(\pm2\) and \(\pm1\); each route is consequently mapped to itself with reversed parametrization. Hence the entire pre-normalization embedding is carried exactly to the reversed-word embedding.

A rigid rotation is an ambient isotopy endpoint. The constructor's subsequent coordinate normalization is topology preserving, so the returned spatial graphs remain ambient isotopic. The Yamada-polynomial identities follow from ambient-isotopy invariance.

Finally, reversal acts as an involution on the \(2^m\) binary words. Its fixed words are the palindromes, of which there are \(2^{\lceil m/2\rceil}\). Burnside's lemma therefore gives
\[
\frac12\left(2^m+2^{\lceil m/2\rceil}\right)
=
2^{m-1}+2^{\lceil m/2\rceil-1}
\]
reversal orbits, proving the stated upper bound on represented ambient-isotopy classes.

## Verification
The proof above is symbolic and applies to every word. The bundled self-contained regression checker reimplements the source's braid-body coordinate formulas and verifies the half-turn identity for every binary word of length at most \(10\), a total of \(2047\) words. Its output is:

`VERIFY_OK words=2047 max_length=10 max_coordinate_error=1.776e-15`

A separate source-data check used the frozen repository commit listed in the references. The released table has \(324\) records; among the \(293\) records whose reversed word is also present, there were zero raw-polynomial-hash mismatches and zero normalized-polynomial-hash mismatches. This finite agreement is supporting evidence only, not the proof.

## Relationship to prior work
The 2026 source introduces the fixed cubic pure-braid family and emphasizes that braid-word order is retained: already
\[
\overline{\Upsilon}(\mathcal N_{AAB};Y)
=
\overline{\Upsilon}(\mathcal N_{BAA};Y)
\ne
\overline{\Upsilon}(\mathcal N_{ABA};Y).
\]
Its supplementary data audit records that all tested raw reversals match and that, within the short exact dataset, same-count raw collisions occur only through reversal. The accompanying certificate simultaneously records `all_word_realization_proved` as false. The source paper and repository do not state an all-word ambient-isotopy theorem explaining the reversal equality.

The present result supplies that missing structural explanation: \(AAB\) and \(BAA\) are not merely an invariant collision in this family; they are related by the explicit orientation-preserving half-turn above. The argument also converts the observed reversal redundancy into an exact all-length quotient bound.

Targeted searches for a reversal theorem for this specific family, a spatial-graph braid-word reversal isotopy, and a Yamada-polynomial reversal identity did not locate an equivalent result.

## Limitations
The theorem is constructor-specific. It uses the palindromic positive-square blocks \(A=\sigma_1^2\) and \(B=\sigma_2^2\), the left-right symmetric host graph, and its symmetric closure routes. It does not imply reversal isotopy for an arbitrary braid closure or arbitrary spatial-graph host.

The reversal-orbit formula is an upper bound for ambient-isotopy classes represented by length-\(m\) words, not a proof that different reversal orbits always give different spatial graphs. The released finite audit found no same-count raw-polynomial collisions beyond reversal in its tested range, but that finite observation is not promoted to an infinite uniqueness statement.

## References
1. H. Akgün, X. Yan, K. Liu, Z. Chen and C. H. Lee, *KnottedGraph: Scalable knotted-graph topology for scientific and mathematical discovery*, arXiv:2609.31152v1, first posted 2026-09-25.
2. Public source notebook at commit `9a0f379c38050e80e57967841904917da86c7528`, `User_guide/applications/05_yamada_formula_discovery.ipynb`, containing the pure-square block definitions and `fixed_cubic_pure_braid_graph` constructor.
3. Public audit files at the same commit, `audit/discovery/certificate.json`, `audit/discovery/exhaustive_short_word_checks.json`, and `data/figure4_pure_braid_324.csv`.
