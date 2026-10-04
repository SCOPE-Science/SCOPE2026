# Exact nilpotent criterion for a quartic 2-by-2 matrix construction
## Finding
Let \(V=\begin{pmatrix}u&v\\ t&-u\end{pmatrix}\in M_2(\mathbb Z)\) satisfy \(\det V=0\), and let \(U=\begin{pmatrix}x&y\\ z&w\end{pmatrix}\in M_2(\mathbb Z)\). Define \(X=U+V\), \(Y=U-V\), and \(Z=U\). Then
\[
X^4+Y^4=2Z^4
\]
holds if and only if
\[
\operatorname{tr}(UV)=u(x-w)+ty+vz=0.
\]
This gives the complete condition on \(U\) for every traceless singular \(2\times2\) matrix \(V\). In particular it disproves the necessity direction in Theorem 2.1 of Moharana--Jena, which imposes the smaller family \(x=w\), \(y=-nv\), \(z=nt\).

A concrete counterexample satisfying that theorem's additional hypotheses is
\[
V=\begin{pmatrix}2&1\\-4&-2\end{pmatrix},\qquad
U=\begin{pmatrix}1&0\\-2&0\end{pmatrix}.
\]
Here \(\det V=0\), \(u=2\ne0\), and \(u\ne\pm t\) because \(t=-4\), while \(x=1\ne0=w\). Nevertheless \(\operatorname{tr}(UV)=0\), so the quartic equation holds.

## Assumptions and scope
All matrices are \(2\times2\) integer matrices. The proof only uses characteristic zero and therefore works verbatim over any characteristic-zero field. The exact criterion assumes that \(V\) has the displayed traceless form and \(\det V=0\); the extra restrictions \(u\ne0\) and \(u\ne\pm t\) are needed only to compare directly with the hypotheses stated in the source theorem.

The source lists 2020 MSC codes beginning with 11D25 and studies the Diophantine matrix equation \(X^4+Y^4=2Z^4\). Its Theorem 2.1 states an if-and-only-if classification for precisely the substitution \(X=U+V\), \(Y=U-V\), \(Z=U\) with singular \(V\) of the displayed form.

## Proof
Because \(\operatorname{tr}V=0\) and \(\det V=0\), Cayley--Hamilton gives \(V^2=0\). Expanding noncommutatively and cancelling the two copies of \(U^4\), all terms with an odd number of \(V\)'s cancel between \((U+V)^4\) and \((U-V)^4\). Terms containing \(V^2\) vanish. Therefore
\[
X^4+Y^4-2U^4=2igl(UVUV+VU^2V+VUVUigr)
=2(UV+VU)^2.
\]
Thus the quartic equation is equivalent to \((UV+VU)^2=0\).

Put \(\tau=\operatorname{tr}U\) and \(\alpha=\operatorname{tr}(UV)\). A direct entrywise calculation gives the two-dimensional identity
\[
UV+VU=\tau V+\alpha I_2.
\]
Indeed, with \(U=\begin{pmatrix}x&y\\z&w\end{pmatrix}\) and \(V=\begin{pmatrix}u&v\\t&-u\end{pmatrix}\), one has \(\alpha=u(x-w)+ty+vz\), and both sides have entries
\[
\begin{pmatrix}
2ux+ty+vz & v(x+w)\\
t(x+w) & vz+ty-2uw
\end{pmatrix}.
\]
Since \(V^2=0\),
\[
(UV+VU)^2=\alpha^2 I_2+2\alpha\tau V.
\]
If \(\alpha=0\), this square vanishes. Conversely, if it vanishes, taking traces gives \(2\alpha^2=0\), hence \(\alpha=0\) in characteristic zero. This proves the equivalence.

For the displayed counterexample, \(\operatorname{tr}(UV)=2(1-0)+(-4)\cdot0+1\cdot(-2)=0\), while \(x\ne w\). Hence it lies outside the source's claimed necessary family but satisfies the equation.

## Verification
The standalone script `verify.py` uses only exact integer arithmetic. It checks the displayed counterexample directly by fourth matrix powers and then exhaustively tests 26,244 pairs \((U,V)\), with every entry of \(U\) in \([-4,4]\) and four nonzero traceless singular choices of \(V\). In every case it confirms that the quartic equation is equivalent to \(\operatorname{tr}(UV)=0\).

Its replay output is:

`VERIFY_OK explicit_counterexample=1 exhaustive_pairs=26244 criterion=trace(UV)==0`

The exhaustive test is corroboration; the infinite statement follows from the algebraic proof above.

## Relationship to prior work
Moharana and Jena reduce their quartic construction to \((UV+VU)^2=0\) after imposing \(V^2=0\), but their necessity argument then sets \(w=x\) rather than solving the full condition. Their Theorem 2.1 consequently gives only a proper subfamily as an alleged if-and-only-if classification. The criterion above completes that missing necessity step and supplies an explicit counterexample to the published statement.

The same paper cites work on the cubic matrix equation \(X^3+Y^3=2Z^3\) and a separate 2026 structured-class result linking some matrix and scalar Diophantine equations. Those results concern different exponents or restricted matrix classes and do not imply the exact trace criterion here. Targeted searches for the source title, the anticommutator condition, the coordinate equation, and equivalent counterexample formulations did not locate a prior correction or the exact criterion.

## Limitations
This result concerns only the source's \(2\times2\) substitution with traceless singular \(V\). It does not classify arbitrary triples \((X,Y,Z)\) solving the quartic equation, nor the higher-dimensional constructions in the source. Literature searches cannot exclude an unindexed or unpublished independent observation; no such coverage was found in the inspected primary source, related structured-matrix literature, or the searched result database.

## References
1. S. Moharana and P. K. Jena, *Matrix Solutions to the Diophantine equation \(X^4+Y^4=2Z^4\)*, arXiv:2609.32374, first submitted 2026-09-26. https://arxiv.org/abs/2609.32374
2. S. R. Garcia, J. Rajkhowa, and K. Sarma, *The matrix equation \(X^3+Y^3=2Z^3\)*, American Mathematical Monthly 132 (2025), article associated with DOI 10.1080/00029890.2024.2409065.
