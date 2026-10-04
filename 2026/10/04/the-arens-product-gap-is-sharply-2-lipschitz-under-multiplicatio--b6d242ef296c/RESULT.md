# The Arens-product gap is sharply \(2\)-Lipschitz under multiplication perturbations
## Finding
Let \(X\) be a complex Banach space and let \(m,n:X\times X\to X\) be bounded bilinear maps. Denote their two Arens extensions by \(m^{\square},m^{\diamond}:X^{**}\times X^{**}\to X^{**}\), and define
\[
\Delta_A(m)=\lVert m^{\square}-m^{\diamond}\rVert.
\]
Then
\[
\Delta_A(m)=0
\quad\Longleftrightarrow\quad
m\text{ is Arens regular},
\]
and the gap is globally \(2\)-Lipschitz:
\[
\bigl|\Delta_A(m)-\Delta_A(n)\bigr|
\le 2\lVert m-n\rVert.
\]
If \(m\) and \(n\) are associative products, the same inequality applies. Therefore
\[
\operatorname{dist}\bigl(m,\mathcal R_{\mathrm{alg}}(X)\bigr)
\ge \frac{\Delta_A(m)}{2},
\]
where \(\mathcal R_{\mathrm{alg}}(X)\) is the set of Arens-regular associative bounded products on the fixed Banach space \(X\).

The factor \(2\) and the distance factor \(1/2\) are simultaneously sharp. On
\[
E=\ell_1\oplus_1\ell_1\oplus_1\mathbb C,
\]
let \(\sigma_{ij}=1\) for \(i<j\) and \(\sigma_{ij}=-1\) for \(i\ge j\), put
\[
b(x,y)=\sum_{i,j\ge1}\sigma_{ij}x_i y_j,
\]
and define
\[
(x,y,c)\cdot(x',y',c')=(0,0,b(x,y')).
\]
This is an associative Banach-algebra multiplication of norm \(1\), it satisfies \(E^3=0\), and
\[
\Delta_A=2.
\]
The zero multiplication is Arens regular and lies at distance \(1\), so the lower bound is attained exactly.

## Assumptions and scope
The Banach-space norm is fixed. The quantity \(\lVert m-n\rVert\) is the usual norm of the difference as a bounded bilinear map \(X\times X\to X\). No renorming is used in the proof. The distance statement is to Arens-regular associative products on that same normed space. The sharpness example is complex, but the same construction also works over the real scalars.

## Proof
For every bounded bilinear map \(h:X\times X\to X\), each Arens extension is linear in \(h\) and has the same norm as \(h\):
\[
\lVert h^{\square}\rVert=\lVert h^{\diamond}\rVert=\lVert h\rVert.
\]
The upper bound follows from the standard extension estimate, while equality follows because both extensions restrict to \(h\) on the canonical copy of \(X\times X\).

Define
\[
D(h)=h^{\square}-h^{\diamond}.
\]
The map \(D\) is linear, and
\[
\lVert D(h)\rVert
\le \lVert h^{\square}\rVert+\lVert h^{\diamond}\rVert
=2\lVert h\rVert.
\]
Since \(\Delta_A(h)=\lVert D(h)\rVert\), the reverse triangle inequality gives
\[
\begin{aligned}
\bigl|\Delta_A(m)-\Delta_A(n)\bigr|
&=\bigl|\lVert D(m)\rVert-\lVert D(n)\rVert\bigr|\\
&\le \lVert D(m)-D(n)\rVert\\
&=\lVert D(m-n)\rVert\\
&\le2\lVert m-n\rVert.
\end{aligned}
\]
Also \(D(h)=0\) exactly when the two Arens extensions agree, which is precisely Arens regularity.

If \(r\in\mathcal R_{\mathrm{alg}}(X)\), then \(\Delta_A(r)=0\), so
\[
\Delta_A(m)\le2\lVert m-r\rVert.
\]
Taking the infimum over \(r\) gives the distance bound.

It remains to prove sharpness. The coefficient matrix \((\sigma_{ij})\) has entries of modulus one, so the bilinear form \(b:\ell_1\times\ell_1\to\mathbb C\) has norm \(1\). Hence the displayed multiplication on \(E\) has norm \(1\). Every product lies in the third coordinate, while the multiplication ignores the third coordinate in both arguments. Thus every triple product is zero and the multiplication is associative.

Choose free ultrafilters \(\mathcal U\) and \(\mathcal V\) on \(\mathbb N\). They define norm-one elements \(F,G\in\ell_1^{**}=(\ell_\infty)^*\) by ultralimits of coordinates. For the matrix \(\sigma_{ij}\),
\[
\lim_{i\to\mathcal U}\lim_{j\to\mathcal V}\sigma_{ij}=1,
\qquad
\lim_{j\to\mathcal V}\lim_{i\to\mathcal U}\sigma_{ij}=-1,
\]
because for fixed \(i\), eventually \(j>i\), while for fixed \(j\), eventually \(i\ge j\). Therefore the two Arens extensions of \(b\) differ by \(2\) at \((F,G)\). Embedding these functionals in the first and second \(\ell_1^{**}\) coordinates of \(E^{**}\) shows \(\Delta_A\ge2\). The general bound \(\Delta_A\le2\lVert m\rVert=2\) gives equality.

Finally, the zero multiplication has gap zero and lies exactly one bilinear-norm unit away. Hence
\[
\operatorname{dist}\bigl(m,\mathcal R_{\mathrm{alg}}(E)\bigr)=1=\frac{\Delta_A(m)}2,
\]
and
\[
\frac{|\Delta_A(m)-\Delta_A(0)|}{\lVert m-0\rVert}=2.
\]
This proves sharpness of both constants within associative products.

## Verification
The proof uses only norm identities for Arens extensions, linearity of the extension procedure, the reverse triangle inequality, and an explicit ultrafilter evaluation of the triangular sign matrix. No finite experiment is used to infer an infinite statement. The sharpness algebra was checked directly: its multiplication is bounded with norm \(1\), all triple products vanish, and the two iterated ultralimits are exactly \(1\) and \(-1\).

## Relationship to prior work
Rajoriya's 2026 note proves that each individual Arens product changes by at most the multiplication perturbation size and derives qualitative stability of Arens irregularity under sufficiently small perturbations. The result here packages the two products into a single intrinsic norm gap, proves a global sharp \(2\)-Lipschitz law, converts it into an explicit distance-to-regularity lower bound, and shows both constants are best possible even for a cube-zero Banach algebra.

Earlier literature measures non-Arens regularity mainly through weakly almost periodic functionals, topological centers, or structural notions such as extreme and strong Arens irregularity. Those notions are not the same as the operator-norm gap \(\Delta_A\), and the inspected sources do not state the sharp perturbation/distance theorem above.

## Limitations
The gap \(\Delta_A\) is an operator-norm invariant of a fixed normed multiplication; it is not claimed to classify the finer structural notions of extreme or strong Arens irregularity. The theorem gives a sharp universal lower bound on distance to the regular locus, not an exact distance formula for every Banach algebra. The sharp example is deliberately elementary and nilpotent; no claim is made that its other Banach-algebra invariants are extremal.

## References
1. Deepika Rajoriya, *A note on the stability of Arens products under small perturbations of multiplication*, arXiv:2609.11379v1, 2026.
2. Mahmoud Filali and Jorge Galindo, *On the extreme non-Arens regularity of Banach algebras*, Journal of the London Mathematical Society 104 (2021), DOI: 10.1112/jlms.12485.
3. A. Ülger, *Some stability properties of Arens regular bilinear operators*, Proceedings of the Edinburgh Mathematical Society 34 (1991), DOI: 10.1017/S0013091500005216.
