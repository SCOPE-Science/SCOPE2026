# Quadratic lifting rigidity for the central exterior bosonization over D8

## Context

Let $k$ be algebraically closed of characteristic $0$ and
$D_8 = \langle r,s \mid r^4 = s^2 = 1,\ srs = r^{-1}\rangle$
(the dihedral group of order $8$).
Its centre is $Z(D_8) = \{1, r^2\}$.
Let $\rho$ be the $2$-dimensional irreducible representation with
$\rho(r) = \mathrm{diag}(i,-i)$,
$\rho(s) = \left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$,
so $\rho(r^2) = -I$.
The admitted target asked for the quadratic lifting census of the
bosonization $A_0 = B(V_0)\# kD_8$ with $V_0 = M(\{r^2\},\rho)$,
conjecturing exactly two finite-dimensional liftings ($A_0$ plus one
nontrivial quadratic lifting).

## Definitions

- $g_0 = r^2$, $V_0 = M(\{g_0\},\rho)$: the $2$-dimensional
  Yetter-Drinfeld module supported on the central class $\{g_0\}$
  with action $\rho$. With basis $x_1,x_2$,
  $c(x_i\otimes x_j) = (g_0\cdot x_j)\otimes x_i = -x_j\otimes x_i$,
  i.e. $c = -\tau$ (minus the flip).
- $B(V_0)$: Nichols algebra of $V_0$.
- $A_0 = B(V_0)\# kD_8$: Radford-Majid bosonization.
- A *lifting* $H$ is a finite-dimensional pointed Hopf algebra with
  $\mathrm{gr}\,H \cong A_0$ for the coradical filtration.

## Result

**Theorem.** Up to isomorphism there is exactly **one**
finite-dimensional pointed Hopf algebra $H$ with
$\mathrm{gr}\,H \cong A_0$: the bosonization $A_0$ itself
($\dim 32$). The conjectured count of exactly two is false: the
putative nontrivial quadratic lifting does not exist. All three
quadratic relation values are primitive in any lifting, hence lie in
$P(kD_8) = 0$, and every admissible scalar deformation parameter is
forced to zero by the relation $G$-degree $g_0^2 = 1$ and the counit.

In particular $B(V_0) = T(V_0)/\langle x_1^2, x_2^2,
x_1x_2+x_2x_1\rangle$ is the exterior algebra $\Lambda(V_0)$ of
dimension $4$, so $\dim A_0 = 4\cdot 8 = 32$.

## Proof / evidence

1. **Yetter-Drinfeld data and braiding.** $\rho$ is certified a
   homomorphism with $\rho(r)^4 = \rho(s)^2 = I$,
   $\rho(s)\rho(r)\rho(s) = \rho(r)^{-1}$, and
   $\rho(r^2) = -I$. Hence $c = -\tau$ with eigenvalues $-1$
   (mult. 3), $+1$ (mult. 1).
2. **Nichols algebra.** $S_2 = \mathrm{id}+c$ has rank $1$
   (nullity $3$), so $\ker S_2 =
   \mathrm{span}\{x_1^2,x_2^2,x_1x_2+x_2x_1\}$ and the degree-2
   quotient is $1$-dimensional. $S_3$ (built from $c$ on
   $V^{\otimes 3}$) has rank $0$. Thus $B(V_0)$ is the exterior
   algebra, $\dim B(V_0) = 1+2+1 = 4$, $\dim A_0 = 32$.
3. **Coproduct rigidity.** Let $H$ lift $A_0$ with strict
   $(1,g_0)$-skew-primitive lifts $a_1,a_2$ of $x_1,x_2$
   (justified below), so $g_0 a_i = -a_i g_0$ and
   $\Delta(a_i) = a_i\otimes 1 + g_0\otimes a_i$. Exact symbolic
   normal-form computation in
   $k\langle a_1,a_2\rangle \rtimes k[g_0]/(g_0^2-1)$ certifies
   $\Delta(u) = u\otimes 1 + 1\otimes u$ for
   $u \in \{a_1^2, a_2^2, a_1a_2+a_2a_1\}$; cross terms cancel
   pairwise, e.g. $a_1g_0\otimes a_1 + g_0a_1\otimes a_1 = 0$.
4. **Correction lemma.** On $kD_8$:
   $\dim P_{g,1} = 1$ for $g\ne 1$, $P(kD_8) = 0$; the correction map
   $\Phi(z) = \Delta z - z\otimes 1 - g_0\otimes z$ has rank $7$,
   and rank $6$ on $\ker\varepsilon$, equal to the normalized
   twisted-$2$-cocycle dimension $6$. Every normalized defect is a
   coboundary, so any partial lift is correctable to a strict
   skew-primitive. This justifies step 3.
5. **Deformation space vanishes — two arguments.**
   (a) Relation-degree/counit: each relation has $G$-degree
   $g_0^2 = 1$, so $\lambda(1-g_r) = 0$; the YD-trivial isotypic of
   the relation space is the $1$-dim $w$-line
   ($w = x_1x_2+x_2x_1$), and $\varepsilon(a_i) = 0$ forces the
   scalar $\lambda = 0$.
   (b) Primitivity: each corrected relation value lies in
   $P(H)\cap H_0 = P(kD_8) = 0$ in characteristic $0$.
   Hence all relation values vanish in $H$. A nonzero primitive in
   characteristic $0$ would generate a polynomial subalgebra, so
   any $H$ with a nonzero relation value is infinite-dimensional
   and excluded by hypothesis.
6. **No higher deformations.** The Nichols ideal is generated in
   degree $2$ (degree-3 component already vanishes), and every
   normalized $2$-cocycle with the relevant twisting is a
   coboundary, so no cocycle deformation produces a new algebra.
   The canonical surjection $A_0 \twoheadrightarrow H$ is an
   isomorphism; $\dim H = 32$.

## Limitations

Base field algebraically closed of characteristic zero as stated.
Positive characteristic (where $P(kD_8)$ need not vanish) is not
addressed. Infinite-dimensional liftings with nonzero primitive
relation values are excluded by hypothesis, not classified. The
computation certifies finite-dimensional linear algebra and exact
normal-form coproduct identities; lift-correction iteration,
generation in degree one, and the polynomial-subalgebra step are
hand proofs.

## Reproducibility

Run `output/artifacts/verify_d8_lifting.py` (requires `numpy`);
it prints all certificates and writes
`output/artifacts/verification_summary.json`: $D_8$
presentation/centre, $\rho$ homomorphism with
$\rho(r^2) = -I$, braiding eigenvalues, ranks of $S_2,S_3$,
exact primitivity of the three quadratic relations,
$\dim P_{g,1}(kD_8)$, correction-map ranks versus cocycle
dimensions, and $\dim\mathrm{Hom}_{YD}(R,k_{\mathrm{triv}}) = 1$
killed by the counit.

## References

- Fantino–Garcia, On pointed Hopf algebras over dihedral groups,
  Pacific J. Math. 252 (2011), 69–91; arXiv:1007.0227. Scope
  $D_m$, $m = 4t \ge 12$; does not cover $D_8$.
- Andruskiewitsch–Fantino, On pointed Hopf algebras associated with
  alternating and dihedral groups, Rev. Union Mat. Argent. 48-3
  (2007), 57–71; arXiv:math/0702559. Nichols-necessity data for
  $D_n$; no $D_8$ lifting census.
- Andruskiewitsch–Schneider, On the classification of
  finite-dimensional pointed Hopf algebras, Ann. Math. 171 (2010),
  375–417. General lifting method.
