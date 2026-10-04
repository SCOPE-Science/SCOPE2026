# Exact inverse regular norms for the elementary positive Miljutin maps

## Finding
Let \(E\neq\{0\}\) be a real Banach lattice. Write \(c(E)\) for the Banach lattice of norm-convergent \(E\)-valued sequences with the supremum norm. For \(a,b>1\) and \(c>0\), consider the elementary positive isomorphisms used in Proposition 3.1 of Laguna-Ricart--Martínez-Cervantes--Rondoš--Salguero-Alarcón:
\[
\Phi_E^a:c(E)\longrightarrow c(E)\oplus_\infty E,
\qquad
\Phi_E^a(z)=\bigl((z_n+a z_{n+1})_{n\ge1},z_1\bigr),
\]
and
\[
\Psi_E^{b,c}:c(E)\oplus_\infty E\longrightarrow c(E),
\]
where
\[
[\Psi_E^{b,c}(z,e)]_1=z_1+ce,
\qquad
[\Psi_E^{b,c}(z,e)]_n=z_n+bz_{n-1}\quad(n\ge2).
\]
Then the published regular-norm upper bounds for the inverses are exact already at the ordinary operator-norm level:
\[
\boxed{\ \| (\Phi_E^a)^{-1}\|=\|(\Phi_E^a)^{-1}\|_{\mathrm r}
      =\max\left\{1,\frac1{a-1}\right\}\ },
\]
and
\[
\boxed{\ \| (\Psi_E^{b,c})^{-1}\|=\|(\Psi_E^{b,c})^{-1}\|_{\mathrm r}
      =\max\left\{\frac1{b-1},\frac{b}{c(b-1)}\right\}\ }.
\]
Consequently, using the exact positive-map norms from the same proposition, the corresponding regular distortions are
\[
D_\Phi(a)=(1+a)\max\left\{1,\frac1{a-1}\right\},
\]
and
\[
D_\Psi(b,c)=(1+\max\{b,c\})
\max\left\{\frac1{b-1},\frac{b}{c(b-1)}\right\}.
\]
The first family has the sharp minimum
\[
\min_{a>1}D_\Phi(a)=3,
\]
attained uniquely at \(a=2\). For fixed \(b>1\), the second is minimized at \(c=b\), with value
\[
\min_{c>0}D_\Psi(b,c)=\frac{b+1}{b-1},
\]
so
\[
\inf_{b>1,\,c>0}D_\Psi(b,c)=1,
\]
and this infimum is not attained at finite parameters.

## Assumptions and scope
The result concerns exactly the two elementary sequence-space isomorphisms in Proposition 3.1 of the cited 2026 positive Miljutin paper. The lattice \(E\) is only assumed nonzero; no order continuity, separability, or distinguished unit is needed. The symbol \(\|\cdot\|_{\mathrm r}\) denotes the regular norm used in that paper.

The result sharpens the local inverse estimates used in the construction. It does not claim that the final constant \(9+6\sqrt3\) in the paper's positive Miljutin theorem is globally optimal, because composition can introduce information not captured by multiplying isolated operator norms.

## Proof
The focal paper gives the inverse of \(\Phi_E^a\) explicitly. If \((y,e)\in c(E)\oplus_\infty E\), then its preimage \(z\) satisfies
\[
z_n=(-1)^{n-1}a^{-(n-1)}e+
\sum_{m=1}^{n-1}(-1)^{m-1}a^{-m}y_{n-m}.
\]
Taking absolute values in the lattice and summing the geometric coefficients gives the published regular-norm estimate
\[
\|(\Phi_E^a)^{-1}\|_{\mathrm r}\le
\max\left\{1,\frac1{a-1}\right\}.
\]
To prove the reverse inequality at the ordinary operator-norm level, choose \(u\in E\) with \(\|u\|=1\). For an integer \(N\ge1\), put
\[
e=(-1)^{N-1}u,
\qquad
y_k=(-1)^{N-k-1}u\quad(1\le k<N),
\qquad
y_k=0\quad(k\ge N).
\]
Then \(\|(y,e)\|=1\), while the \(N\)-th coordinate of the inverse is a positive scalar multiple of \(u\) with norm
\[
a^{-(N-1)}+\sum_{m=1}^{N-1}a^{-m}.
\]
As \(N\) ranges from \(1\) to infinity these values interpolate monotonically between \(1\) and \(1/(a-1)\); hence their supremum is
\[
\max\left\{1,\frac1{a-1}\right\}.
\]
Because the ordinary operator norm never exceeds the regular norm, equality follows for both norms.

For \(\Psi_E^{b,c}\), the focal paper gives
\[
z_n=\sum_{j\ge1}(-1)^{j-1}b^{-j}y_{n+j},
\qquad
e=\frac{y_1-z_1}{c}.
\]
Its lattice absolute-value estimate yields
\[
\|(\Psi_E^{b,c})^{-1}\|_{\mathrm r}\le
\max\left\{\frac1{b-1},\frac{b}{c(b-1)}\right\}.
\]
Again take \(\|u\|=1\). To force the first term, fix \(n\), choose a finite alternating tail
\[
y_{n+j}=(-1)^{j-1}u\quad(1\le j\le N),
\]
and set all other coordinates to zero. The input has norm \(1\), while
\[
\|z_n\|=\sum_{j=1}^N b^{-j}\longrightarrow\frac1{b-1}.
\]
To force the second term, choose
\[
y_1=u,
\qquad y_{1+j}=(-1)^j u\quad(1\le j\le N),
\]
with zero tail afterward. Then
\[
z_1=-\left(\sum_{j=1}^N b^{-j}\right)u,
\]
so
\[
\|e\|=\frac{1+\sum_{j=1}^N b^{-j}}{c}
\longrightarrow\frac{b}{c(b-1)}.
\]
Thus the ordinary inverse norm is at least both terms in the published upper bound, proving the second exact identity.

The parameter optimization is elementary but sharp. For \(1<a\le2\),
\[
D_\Phi(a)=\frac{1+a}{a-1},
\]
which decreases to \(3\); for \(a\ge2\), \(D_\Phi(a)=1+a\), which increases from \(3\). Hence the unique minimizer is \(a=2\).

For fixed \(b>1\), if \(c\ge b\), then
\[
D_\Psi(b,c)=\frac{1+c}{b-1},
\]
whose minimum on that region is at \(c=b\). If \(0<c\le b\), then
\[
D_\Psi(b,c)=\frac{b(1+b)}{c(b-1)},
\]
which decreases up to \(c=b\). Thus the unique minimizer in \(c\) is \(c=b\), giving \((b+1)/(b-1)\), and this tends to \(1\) as \(b\to\infty\) without ever equaling \(1\).

## Verification
Both lower-bound constructions use finitely supported sequences, so they belong to \(c(E)\) and require no convergence subtlety. Substitution into the published inverse formulas aligns every scalar coefficient with the same unit vector \(u\), making the triangle-inequality upper bounds exact in the limit. The endpoint regimes \(a=2\) and \(c=b\) were checked directly in the closed formulas.

The proof uses no finite experiment or numerical approximation. The only limiting arguments are geometric-series limits, and they establish suprema of operator norms rather than claiming that a maximizing input exists.

## Relationship to prior work
Laguna-Ricart, Martínez-Cervantes, Rondoš and Salguero-Alarcón introduce the two maps above as the elementary engine of their positive Cantor--Bernstein argument and prove the corresponding inverse regular-norm upper bounds. Their main theorem then constructs positive isomorphisms between \(C(K)\)-spaces of uncountable compact metric spaces with regular inverse and uniform distortion at most \(9+6\sqrt3\).

The present observation is not a stronger Miljutin theorem. It identifies the exact local constants in Proposition 3.1 and shows that the paper's geometric-series estimates cannot be improved for either elementary inverse merely by a sharper norm estimate. The two elementary families also have sharply different parameter behavior: the \(\Phi\)-family has unavoidable distortion \(3\), whereas the \(\Psi\)-family approaches distortion \(1\).

Related 2026 work on positive Banach--Mazur distance and positive isomorphism classification studies quantitative positivity for \(C(K)\)-spaces, but the inspected statements concern different maps and do not imply these exact sequence-operator norms.

## Limitations
The claim is confined to the specific elementary maps \(\Phi_E^a\) and \(\Psi_E^{b,c}\). It does not establish optimality of the final global Miljutin constant, nor does it classify all positive isomorphisms between \(c(E)\) and \(c(E)\oplus_\infty E\).

Because the lower bounds are short sign-alignment arguments, an equivalent exactness observation could be folklore or could appear in literature under different notation. Targeted searches did not locate such a statement, but very recent literature may be incompletely indexed.

## References
1. J. Laguna-Ricart, G. Martínez-Cervantes, J. Rondoš, A. Salguero-Alarcón, *A positive version of Miljutin's Theorem*, arXiv:2609.14148v1, first public 2026-09-12. See Proposition 3.1 and the main quantitative theorem.
2. M. Cúth, J. Havelka, J. Rondoš, B. Sarı, *The classification of \(C(K)\) spaces for countable compacta by positive isomorphisms*, arXiv:2601.11463v1, 2026.
3. M. Korpalski, G. Plebanek, *On positive Banach--Mazur distance*, arXiv:2604.23637v1, 2026.
