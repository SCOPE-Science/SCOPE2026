# Köthe duality erases the singular defect in Huang's logarithmically monotone examples

## Statement

Let
\[
\psi(t)=\begin{cases}
t,&0<t\le 1,\\
1+\log t,&t>1,
\end{cases}
\qquad E=M_\psi(0,\infty)
\]
with its standard Marcinkiewicz norm
\[
\|h\|_E=\sup_{t>0}\frac1{\psi(t)}\int_0^t \mu(s,h)\,ds.
\]
In arXiv:2609.20270, Huang constructs a finite continuous symmetric lattice seminorm \(\Phi\) on \(E\) satisfying
\[
0\le \Phi(h)\le \|h\|_E,
\]
which is monotone under logarithmic submajorization and, crucially,
\[
\Phi(s)=0
\]
for every bounded finite-support function \(s\).

Two of Huang's examples admit a sharper duality description.

### Theorem A: the equivalent renorming has exactly the same Köthe dual

For \(\lambda>0\), set
\[
N_\lambda(h)=\|h\|_E+\lambda\Phi(h).
\]
Then the associate spaces agree isometrically:
\[
\boxed{(E,N_\lambda)^\times=(E,\|\cdot\|_E)^\times.}
\]
Consequently, because the standard Marcinkiewicz space \(E\) has the Fatou property,
\[
\boxed{(E,N_\lambda)^{\times\times}=E}
\]
isometrically, where the norm on the Köthe bidual is the original standard Marcinkiewicz norm, not \(N_\lambda\).

For Huang's explicit pair from the first construction, one has
\[
\|g\|_E=1,\qquad \Phi(g)=1,
\]
so
\[
N_\lambda(g)=1+\lambda,
\qquad
\|g\|_{(E,N_\lambda)^{\times\times}}=1.
\]
Thus Köthe bidualization erases the whole added \(\lambda\Phi\) defect, and on this explicit vector the collapse realizes the full equivalence factor \(1+\lambda\).

### Theorem B: the proper closed ideal has the same Köthe dual as the ambient space

For Huang's second construction, let
\[
X=\ker\Phi
\]
with the norm inherited from \(E\). Huang proves that \(X\) is a proper closed strongly symmetric Banach function space, that it contains every bounded finite-support function, and that it is logarithmically solid but not Hardy--Littlewood solid.

Then
\[
\boxed{X^\times=E^\times}
\]
isometrically and hence
\[
\boxed{X^{\times\times}=E}
\]
isometrically.

Moreover, for Huang's explicit witness \(g\) in the second construction,
\[
\|g\|_E=1,\qquad \Phi(g)=1,\qquad g\notin X,
\]
and in fact
\[
\boxed{\operatorname{dist}_E(g,X)=1.}
\]
Therefore the failure of Köthe reflexivity is not caused by a norm-small boundary defect: the missing element is a full unit away from the closed ideal even though every Köthe functional sees exactly the same associate space on \(X\) and on \(E\).

Finally, Hahn--Banach gives a norm-one functional \(F\in E^*\) with
\[
F|_X=0,\qquad F(g)=1.
\]
No such separator can be represented by an element of \(E^\times\). Hence the functional detecting this defect necessarily lies in the singular, non-Köthe part of the Banach dual.

## General truncation lemma

The mechanism is elementary and applies more generally.

Let \(E\) be a Banach function ideal over a sigma-finite measure space. Suppose \(N\) is another lattice norm on the same underlying ideal such that
\[
N(f)\ge \|f\|_E
\]
for all \(f\in E\), while
\[
N(s)=\|s\|_E
\]
for every bounded finite-support function \(s\). Then
\[
(E,N)^\times=E^\times
\]
isometrically.

Likewise, if \(Y\subseteq E\) contains every bounded finite-support function and carries the inherited \(E\)-norm, then
\[
Y^\times=E^\times
\]
isometrically.

### Proof

The inclusion \(E^\times\subseteq(E,N)^\times\) is contractive because \(N\ge\|\cdot\|_E\). For the reverse norm inequality, let \(y\in(E,N)^\times\) and let \(x\in E\), \(x\ge0\), with \(\|x\|_E\le1\). Choose an increasing finite-measure exhaustion \((\Omega_n)\) of the measure space and put
\[
x_n=(x\wedge n)\mathbf 1_{\Omega_n}.
\]
Then \(x_n\) is bounded and has finite support, \(\|x_n\|_E\le1\), and therefore \(N(x_n)=\|x_n\|_E\le1\). Hence
\[
\int x_n|y|\le \|y\|_{(E,N)^\times}.
\]
By monotone convergence,
\[
\int x|y|\le \|y\|_{(E,N)^\times}.
\]
Taking the supremum over the positive unit ball of \(E\) gives
\[
\|y\|_{E^\times}\le \|y\|_{(E,N)^\times}.
\]
The opposite inequality was already noted, proving equality of both the set and the norm.

For a subspace \(Y\) containing all bounded finite-support functions, exactly the same truncations belong to \(Y\); the same argument gives \(Y^\times=E^\times\) isometrically.

Applying this lemma to Huang's \(N_\lambda\) proves Theorem A because \(\Phi\) vanishes on bounded finite-support functions. Applying it to \(X=\ker\Phi\) proves the first assertion of Theorem B.

The standard Marcinkiewicz space \(E=M_\psi\) has the Fatou property, so the Lorentz--Luxemburg theorem identifies \(E^{\times\times}\) isometrically with \(E\). This gives both bidual conclusions.

For the distance formula in Theorem B, if \(x\in X\), then the reverse triangle inequality for the seminorm gives
\[
1=|\Phi(g)-\Phi(x)|\le \Phi(g-x)\le \|g-x\|_E.
\]
Hence \(\operatorname{dist}_E(g,X)\ge1\). Since \(0\in X\) and \(\|g\|_E=1\), equality follows.

To see why a separating functional is necessarily non-Köthe, suppose an integral functional represented by \(y\in E^\times\) vanished on \(X\). Since \(X\) contains all bounded finite-support functions, it would vanish on every such test function. Taking bounded indicators, and their signed or phased versions, on finite-measure sets forces \(y=0\) almost everywhere. Such a functional cannot satisfy \(F(g)=1\).

## Context and value

Huang's paper establishes two new separation phenomena for symmetric Banach function spaces: an equivalent norm that is monotone under logarithmic submajorization without being strongly symmetric, and a strongly symmetric logarithmically solid closed ideal that cannot admit an equivalent fully symmetric norm. The observations above locate both failures more precisely in Banach-function-space duality.

The associate space does not detect either deformation at all. In the renorming example, the entire additional seminorm disappears under Köthe bidualization. In the closed-ideal example, the Köthe bidual fills the whole ambient Marcinkiewicz space even though the missing witness has distance exactly one from the ideal. Thus the obstruction is genuinely singular from the duality viewpoint: it is visible in the full Banach dual but invisible to all integral Köthe functionals.

The truncation lemma and the Lorentz--Luxemburg theorem are classical and are not claimed as new. The claimed contribution is their sharp application to Huang's 2026 constructions, including the isometric associate-space identities, the exact bidual collapse, the explicit distance-one witness, and the resulting localization of the obstruction to singular functionals.

## Originality and limitations

To the best of our knowledge, the current version of arXiv:2609.20270 does not discuss Köthe associates, Köthe biduals, Fatou envelopes, or singular separators for these examples. Targeted searches for the paper together with associate-space, Köthe-dual, bidual, Fatou-envelope, Marcinkiewicz, and singular-functional terminology did not locate a prior statement of these consequences.

The main residual originality risk is older Banach-function-space literature on singular functionals, non-Fatou renormings, and order-continuous or Köthe closures. A general theorem in that literature may subsume the truncation mechanism in a broader form. No novelty is claimed for such classical machinery. The specific duality diagnosis of Huang's newly published examples, and in particular the exact distance-one separation in the second example, is the part asserted here to be new to the best of our knowledge.

The associate dual \(E^\times\) must not be confused with the full Banach dual \(E^*\). The result does not say the full duals of \((E,N_\lambda)\), \(X\), and \(E\) coincide isometrically. It says precisely that their Köthe/integral dual information agrees in the stated ways, while the missing information is detected by singular Banach-dual functionals.

## References

1. Jinghao Huang, *A logarithmically monotone symmetric norm which is not fully symmetric*, arXiv:2609.20270 (2026).
2. C. Bennett and R. Sharpley, *Interpolation of Operators*, Academic Press, 1988. Standard background on rearrangement-invariant Banach function spaces, associate spaces, Marcinkiewicz spaces, and the Lorentz--Luxemburg theorem.
