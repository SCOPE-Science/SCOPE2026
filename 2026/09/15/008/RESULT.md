# Leaf-density dichotomy for nef-model foliations is false: parabolic suspension counterexample

## Context

The admitted target asked whether a holomorphic foliation by curves on a smooth complex projective surface, under a nef-model hypothesis package (canonical bundle nef of numerical dimension one, no rational first integral, hyperbolic singularities, generalized curve along an invariant curve with vanishing log Baum-Bott defect), must satisfy a dichotomy: either there is an invariant algebraic curve off the given invariant curve, or every leaf off it is dense. Either a proof or a rigorous counterexample is a complete two-sided resolution.

## Definitions

Let $X$ be a smooth complex projective surface, $F$ a holomorphic foliation by curves, $K_F$ its canonical bundle, and $D \subset X$ a connected simple-normal-crossing compact curve invariant by $F$. Numerical dimension $\nu(K_F)=1$ means $K_F$ is nef, $K_F^2=0$, $K_F\not\equiv_{\mathrm{num}}0$. A rational first integral is a nonconstant rational function constant on leaves. A singularity is hyperbolic if the ratio of eigenvalues is nonreal; the empty set is vacuously hyperbolic. Generalized curve along $D$ with defect $\Delta(F,D)=0$ means the logarithmic Baum-Bott residues vanish compatibly with $2\mathrm{GSV}$. A suspension Riccati foliation is the horizontal foliation on $(\tilde B\times\mathbb{P}^1)/\pi_1(B)$ transverse to the fibres of the induced $\mathbb{P}^1$-bundle.

## Result

The dichotomy is FALSE. There exist $X,F,D$ satisfying every hypothesis for which both horns fail simultaneously:

- $X=\mathbb{P}(E)$ over a smooth projective curve $B$ of genus $g\ge 2$, where $E$ is the non-split extension $0\to\mathcal{O}_B\to E\to\mathcal{O}_B\to 0$ from the unipotent representation $\gamma\mapsto \bigl(\begin{smallmatrix}1&n(\gamma)\\0&1\end{smallmatrix}\bigr)$ for a surjection $n:\pi_1(B)\to\mathbb{Z}$.
- $F$ the Riccati suspension foliation acting by $\gamma\cdot(x,z)=(\gamma\cdot x,z+n(\gamma))$, everywhere transverse to fibres, hence regular with $\mathrm{Sing}(F)=\varnothing$.
- $D$ the section at infinity, smooth connected and invariant.
- $K_F=\pi^*K_B$ is nef of numerical dimension $1$; $F$ has no rational first integral; $F$ is a generalized curve along $D$ with defect $0$.
- (A) fails: no invariant algebraic curve distinct from components of $D$ exists.
- (B) fails: for $z_0\in\mathbb{C}$, the leaf $L_{z_0}$ satisfies $\overline{L_{z_0}}=L_{z_0}\cup D\ne X$, hence is not dense.

## Proof / evidence

Realize the translation action $\rho(\gamma)(z)=z+n(\gamma)$ on $\mathbb{P}^1=\mathbb{C}\cup\{\infty\}$ parabolically fixing $\infty$. By Riemann-Hilbert and GAGA the flat rank-2 bundle is algebraic, so $X$ is a smooth projective ruled surface and $F$ is an algebraic Riccati foliation transverse to fibres, hence regular and reduced. Transversality gives $d\pi:T_F\cong\pi^*T_B$, so $K_F=\pi^*K_B\equiv_{\mathrm{num}}(2g-2)F_{\mathrm{fib}}$: $K_F\cdot C=0$ on fibres and $(2g-2)\deg(\pi|_C)\ge 0$ otherwise, $K_F^2=0$, $K_F\not\equiv_{\mathrm{num}}0$. Thus nef with $\nu=1$. Generic leaves are $\tilde B/\ker n$, infinite etale covers of $B$, noncompact and non-algebraic, so no rational first integral exists. Empty singular set is vacuously hyperbolic and reduced; with $\mathrm{Sing}(F)\cap D=\varnothing$ all local Baum-Bott, Camacho-Sad, GSV sums vanish, giving generalized curve with $\Delta=0$. Fibres are transverse hence not invariant; any other irreducible invariant curve dominates $B$ and would contain a global leaf, but the only compact leaf is $D$ since translations $z\mapsto z+1$ on $\mathbb{C}$ have no finite orbit, so (A) fails. Fibrewise $L_{z_0}\cap X_b=z_0+\mathbb{Z}$ is discrete with closure adding $\infty$; over simply connected $U\subset B$ leaves are horizontal sections whose closure adds $U\times\{\infty\}$; by properness of $\pi$ globally $\overline{L_{z_0}}=L_{z_0}\cup D$, a proper analytic subset, so (B) fails. No exceptional minimal set disjoint from $D$ occurs; the obstruction is $D$ itself in the closure.

## Limitations

One explicit infinite family (parabolic suspensions over genus at least two) disproves the dichotomy; it does not classify where the dichotomy holds, does not treat modified dichotomies allowing invariant curves in leaf closures, and relies on standard suspension, Riccati, ruled-surface, and Riemann-Hilbert facts rather than re-proving them.

## Reproducibility

Take any genus $g\ge 2$ curve $B$, any surjection $H_1(B,\mathbb{Z})\to\mathbb{Z}$, and the above unipotent representation. Form $X=\mathbb{P}(E)$ and the suspension foliation. Compute $K_F=\pi^*K_B$, check regularity by transversality, verify leaf topology via stabilizers, and compute closures fibrewise plus properness as above.

## References

- M. Brunella, Foliations on complex projective surfaces (arXiv:math/0212082) — nef models, Riccati/turbulent classification, Kodaira dimension.
- M. Correa, F. Lourenco, D. Machado, Log Baum-Bott residues for foliations by curves (arXiv:2411.04015) — logarithmic residues, GSV/Camacho-Sad relations.
- S. Druel, On foliations with nef anti-canonical bundle, Trans. AMS (2017) — screened neighboring nef-foliation result.
