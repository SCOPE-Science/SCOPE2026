# Uniform half-density in every \(14/5\)-free binary rich word
## Finding
Let \(w\) be an infinite binary word that is rich and \(14/5\)-free. Write
\[
\Delta(u)=|u|_1-|u|_0
\]
for the signed letter imbalance of a finite binary word \(u\).

For every integer \(n\ge1\), there is a constant \(C_n<\infty\), depending on \(w\) and \(n\) but not on the factor \(u\), such that every finite factor \(u\) of \(w\) satisfies
\[
|\Delta(u)|\le 2^{-n}|u|+C_n.
\]
Consequently the letter frequency \(1/2\) holds uniformly over all long factors:
\[
\lim_{L\to\infty}\ \sup_{\substack{u\text{ factor of }w\\|u|=L}}
\left|\frac{|u|_1}{L}-\frac12\right|=0.
\]
Thus every infinite binary rich word below exponent \(14/5\) has asymptotically equal zero and one densities not merely along its prefixes, but uniformly in the starting position of a long factor.

## Assumptions and scope
A finite or infinite binary word is rich when every finite factor has the maximum possible number of distinct palindromic factors. A word is \(14/5\)-free when it has no finite factor of exponent at least \(14/5\).

The proof uses the structural theorem of Currie, Mol, and Rampersad. Define morphisms
\[
f(0)=0,\quad f(1)=01,\quad f(2)=011,
\]
\[
g(0)=011,\quad g(1)=0121,\quad g(2)=012121,
\]
and
\[
h(0)=01,\quad h(1)=02,\quad h(2)=022.
\]
Their theorem states that, for every \(n\ge1\), every infinite binary rich \(14/5\)-free word has a suffix of the form \(f(h^n(v_n))\) or \(f(g(h^n(v_n)))\) for some infinite ternary word \(v_n\).

The conclusion is an asymptotic frequency statement. It does not assert a bounded discrepancy independent of factor length.

## Proof
Assign weights to the ternary letters by
\[
d(0)=-1,\qquad d(1)=0,\qquad d(2)=1.
\]
For a ternary word \(x\), let \(d(x)\) be the sum of its letter weights. Directly from the definitions,
\[
\Delta(f(a))=d(a)\qquad(a\in\{0,1,2\}).
\]
Moreover both ternary morphisms preserve this weight letter by letter:
\[
d(h(a))=d(a),\qquad d(g(a))=d(a)
\]
for every \(a\in\{0,1,2\}\). By additivity, for every \(n\ge0\),
\[
\Delta(f(h^n(a)))=d(a)
\]
and
\[
\Delta(f(g(h^n(a))))=d(a).
\]
Hence every source-letter block in either structural decomposition has absolute binary imbalance at most \(1\).

Fix \(n\ge1\) and choose the suffix decomposition supplied by the structural theorem. Let \(m_n\) and \(M_n\) be respectively the minimum and maximum lengths of its three possible source-letter blocks. Every image under \(h\) has length at least \(2\), while every image under \(f\) is nonempty. Therefore
\[
m_n\ge 2^n.
\]
The number \(M_n\) is finite because there are only three source letters.

Consider first a factor \(u\) lying entirely in the chosen suffix. Apart from at most two partial boundary blocks, \(u\) is a concatenation of complete source-letter blocks. Each complete block has absolute imbalance at most \(1\), and there are at most \(|u|/m_n+1\) complete blocks. The two partial blocks together contain at most \(2M_n\) symbols. Thus
\[
|\Delta(u)|\le \frac{|u|}{m_n}+1+2M_n
\le 2^{-n}|u|+1+2M_n.
\]

Let \(p_n\) be the number of symbols of \(w\) before this suffix. An arbitrary factor of \(w\) can contain at most \(p_n\) symbols before the suffix, whose total imbalance has absolute value at most \(p_n\). Therefore every factor \(u\) of \(w\) satisfies
\[
|\Delta(u)|\le 2^{-n}|u|+C_n,
\qquad
C_n=1+2M_n+p_n.
\]

For factors of length \(L\), divide by \(L\) and take the supremum over starting positions. For every fixed \(n\),
\[
\limsup_{L\to\infty}
\sup_{|u|=L}\frac{|\Delta(u)|}{L}
\le 2^{-n}.
\]
Because \(n\) is arbitrary, the left side is \(0\). Finally,
\[
\left|\frac{|u|_1}{|u|}-\frac12\right|
=\frac{|\Delta(u)|}{2|u|},
\]
which proves the stated uniform half-density.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The script checks from the explicit morphisms that \(f\) converts the ternary weight \((-1,0,1)\) exactly into binary letter imbalance and that both \(g\) and \(h\) preserve that weight. It then replays iterates through \(n=12\), checks the block imbalance identities and the lower bound \(m_n\ge2^n\), and checks the additive identities for every ternary word of length at most \(6\).

These computations are regression checks for the algebra used in the proof. The passage from the published suffix theorem to the uniform factor bound is analytic and holds for all \(n\), not only for the tested iterates.

## Relationship to prior work
Currie, Mol, and Rampersad determine the repetition threshold for binary rich words and prove the suffix-structure theorem used here. Their paper later analyzes the letter frequency of a particular Sturmian word arising in the construction of an extremal rich word, but it does not state that every infinite binary rich \(14/5\)-free word has uniform binary frequency \(1/2\).

Later work identifies a lexicographically least binary rich word achieving the repetition threshold, and another line studies symmetries of individual rich sequences with minimum critical exponent. Those results concern distinguished extremal words rather than a uniform factor-frequency law for the entire \(14/5\)-free rich class.

The present observation extracts a global statistical consequence from the source morphisms: their signed incidence invariant survives every level of the suffix decomposition, while source-letter blocks grow exponentially. Searches for equivalent formulations in terms of letter frequency, density, and the rich-word repetition threshold found no published statement of this uniform half-density conclusion.

## Limitations
The theorem does not show bounded discrepancy, finite balance, or a rate independent of the suffix constants \(C_n\). It also does not imply unique ergodicity of the whole orbit closure, because only the one-letter frequency is controlled here.

The argument applies under the strict \(14/5\)-free hypothesis and uses the published structure theorem as an essential premise. It does not classify rich words that contain a factor of exponent at least \(14/5\).

A short corollary of a structural theorem can be overlooked in indexing, so an unindexed note or remark remains a residual originality risk.

## References
1. J. Currie, L. Mol, and N. Rampersad, “The repetition threshold for binary rich words,” arXiv:1908.03169v1, first public version 2019-08-08; Discrete Mathematics & Theoretical Computer Science 22(1), 2020, DOI 10.23638/DMTCS-22-1-6.
2. J. Currie, L. Mol, N. Rampersad, and K. Shallit, “The Lexicographically Least Binary Rich Word Achieving the Repetition Threshold,” The Electronic Journal of Combinatorics 31(4), 2024, DOI 10.37236/12464.
3. L. Dvořáková and E. Pelantová, “Symmetries of rich sequences with minimum critical exponent,” arXiv:2501.15135, 2025; Developments in Language Theory 2025, DOI 10.1007/978-3-031-97548-6_11.
