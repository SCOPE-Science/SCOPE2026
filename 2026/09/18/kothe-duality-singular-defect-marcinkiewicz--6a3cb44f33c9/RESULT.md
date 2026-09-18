# Köthe duality erases the singular defect in Huang's logarithmically monotone examples

## Result

Let
\[
\psi(t)=
\begin{cases}
t,&0<t\le 1,\\
1+\log t,&t>1,
\end{cases}
\qquad
E=M_\psi(0,\infty)
\]
with its standard Marcinkiewicz norm
\[
\|h\|_E=\sup_{t>0}\frac{\int_0^t h^*(s)\,ds}{\psi(t)}.
\]
Huang [1] constructs, for suitable parameters, a continuous symmetric lattice seminorm
\(\Phi\) on \(E\) such that

1. \(0\le \Phi(h)\le \|h\|_E\);
2. \(\Phi(h)=0\) whenever \(h\) is bounded and has support of finite measure;
3. \(\Phi\) is monotone under logarithmic submajorization.

Two consequences of that construction admit an exact Köthe-duality description.

### Theorem A: the renormed example has the same associate space isometrically

For \(\lambda>0\), let
\[
N_\lambda(h)=\|h\|_E+\lambda\Phi(h).
\]
Then
\[
\boxed{(E,N_\lambda)^\times=(E,\|\cdot\|_E)^\times}
\]
isometrically. Consequently,
\[
\boxed{(E,N_\lambda)^{\times\times}=(E,\|\cdot\|_E)}
\]
isometrically, because the standard Marcinkiewicz norm has the Fatou property.

Thus Köthe bidualization deletes the entire singular term \(\lambda\Phi\):
\[
\|h\|_{(E,N_\lambda)^{\times\times}}=\|h\|_E
\qquad(h\in E).
\]

For Huang's first example (\(\alpha=1\)), the explicit functions \(f,g\) satisfy
\[
\|f\|_E=\|g\|_E=1,\qquad
\Phi(f)=1-e^{-1},\qquad
\Phi(g)=1.
\]
Hence
\[
\|g\|_{N_\lambda}=1+\lambda,
\qquad
\|g\|_{N_\lambda^{\times\times}}=1.
\]
The upper equivalence constant
\[
N_\lambda(h)\le (1+\lambda)\|h\|_E
\]
is therefore attained at \(g\), while the Köthe bidual norm collapses that maximal factor exactly.

### Theorem B: the closed logarithmically solid ideal has full Marcinkiewicz Köthe bidual

For Huang's second example (\(\alpha=\tfrac12\)), let
\[
X=\ker\Phi\subset E
\]
with the inherited norm \(\|x\|_X=\|x\|_E\). Then
\[
\boxed{X^\times=E^\times}
\]
isometrically and
\[
\boxed{X^{\times\times}=E}
\]
isometrically.

In particular, \(X\) is a proper norm-closed symmetric ideal whose entire deficit from the ambient Marcinkiewicz space is invisible to the associate space. Huang's functions satisfy
\[
f\in X,\qquad g\notin X,\qquad
\|f\|_E=\|g\|_E=1,\qquad
\Phi(g)=1,
\]
and in fact
\[
\boxed{\operatorname{dist}_E(g,X)=1.}
\]
Thus the missing element \(g\) lies at the largest possible distance from the closed subspace \(X\) among unit vectors, even though \(X\) and \(E\) have exactly the same Köthe dual with exactly the same norm.

As a further consequence, Hahn--Banach yields \(F\in E^*\) with
\[
\|F\|=1,\qquad F|_X=0,\qquad F(g)=1.
\]
No such separator can be represented by an element of \(E^\times\). Hence the obstruction \(X\ne E\) is necessarily detected by the singular, non-Köthe part of the Banach dual.

## General truncation lemma

The mechanism is elementary and applies beyond this example.

Let \(E\) be a Banach function ideal on a sigma-finite measure space, and assume the standard truncations
\[
x_n=|x|\wedge n
\]
followed by restriction to an increasing exhaustion by finite-measure sets belong to \(E\). Suppose a second lattice norm \(N\) on the same underlying space satisfies

\[
N(x)\ge \|x\|_E
\]
for every \(x\), and
\[
N(s)=\|s\|_E
\]
for every bounded function \(s\) with finite-measure support. Then
\[
(E,N)^\times=E^\times
\]
isometrically.

Likewise, if \(Y\subset E\) contains all bounded finite-support functions and carries the inherited \(E\)-norm, then
\[
Y^\times=E^\times
\]
isometrically.

### Proof

For the renorming statement, \(N\ge\|\cdot\|_E\) gives
\[
B_N\subseteq B_E,
\]
hence
\[
\|y\|_{(E,N)^\times}\le \|y\|_{E^\times}.
\]

Conversely, fix \(x\in E\) with \(\|x\|_E\le1\). Choose a finite-measure exhaustion
\(\Omega_n\uparrow\Omega\) and set
\[
x_n=(|x|\wedge n)\mathbf 1_{\Omega_n}.
\]
Then \(x_n\) is bounded with finite support,
\[
\|x_n\|_E\le1,\qquad N(x_n)=\|x_n\|_E\le1,
\]
and \(x_n\uparrow |x|\) almost everywhere. For every measurable \(y\ge0\), monotone convergence gives
\[
\int x_n y\longrightarrow\int |x|y.
\]
Therefore the supremum over the \(N\)-unit ball is at least the supremum over the \(E\)-unit ball, proving equality of the associate norms.

The subspace statement is identical: every \(x_n\) belongs to \(Y\), so the \(Y\)-associate unit ball tests all \(E\)-unit-ball elements by monotone truncation.

For Huang's \(E=M_\psi\), Proposition 2.4 of [1] states that the standard Marcinkiewicz norm has the Fatou property. The classical Lorentz--Luxemburg theorem therefore gives
\[
E^{\times\times}=E
\]
isometrically. Applying the preceding identities gives Theorems A and B.

For the distance assertion in Theorem B, seminorm subadditivity gives
\[
|\Phi(g)-\Phi(x)|\le \Phi(g-x)\le\|g-x\|_E
\]
for every \(x\in X\). Since \(\Phi(g)=1\) and \(\Phi(x)=0\),
\[
\|g-x\|_E\ge1.
\]
Taking \(x=0\) and using \(\|g\|_E=1\) gives equality.

Finally, if an integral functional represented by \(y\in E^\times\) vanished on \(X\), it would vanish on every bounded finite-support function. Testing against bounded functions supported on finite-measure sets forces \(y=0\) almost everywhere. Hence the nonzero Hahn--Banach separator of \(g\) from \(X\) is necessarily non-Köthe.

## Context and originality

Huang [1] proves that \(N_\lambda\) is logarithmically monotone but not strongly symmetric, and that \(X=\ker\Phi\) is strongly symmetric and logarithmically solid but admits no equivalent fully symmetric norm. The paper does not discuss Köthe duals, associate spaces, biassociate spaces, or the singular-dual localization above.

The truncation lemma itself is not claimed as new; it is an elementary associate-space observation. The contribution claimed here is the exact duality diagnosis of Huang's two new examples:

\[
N_\lambda^\times=E^\times,\qquad
N_\lambda^{\times\times}=E,
\]
\[
X^\times=E^\times,\qquad
X^{\times\times}=E,
\]
together with the exact distance formula
\[
\operatorname{dist}_E(g,X)=1
\]
and the conclusion that every functional separating \(g\) from \(X\) lies outside the Köthe part of the dual.

Targeted searches for Huang's construction together with "Köthe dual", "associate space", "Köthe bidual", "Fatou envelope", and "singular dual" did not locate an earlier statement of these consequences. The classical Lorentz--Luxemburg theorem and standard theory of Marcinkiewicz associate spaces are prior art and are not part of the novelty claim.

## Limitations

The result concerns Köthe/associate duality, not the full Banach dual. Equivalent renorming leaves the underlying topological dual as a vector space unchanged, although its dual norm changes. The singular part of the Banach dual is not classified here.

No claim is made that the truncation lemma is new. No explicit identification of \(E^\times\) with a particular Lorentz-space normalization is needed or asserted. The conclusions use the sigma-finite structure of \((0,\infty)\), Huang's vanishing of \(\Phi\) on bounded finite-support functions, and the Fatou property of the standard Marcinkiewicz norm.

## References

[1] J. Huang, *A logarithmically monotone symmetric norm which is not fully symmetric*, arXiv:2609.20270v1 (2026).

[2] C. Bennett and R. Sharpley, *Interpolation of Operators*, Academic Press, 1988. See the standard theory of associate spaces, Marcinkiewicz spaces, and the Lorentz--Luxemburg theorem.
