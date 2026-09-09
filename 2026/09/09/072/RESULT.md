# Vanishing involutive local class of +Sigma(2,3,13): exact triple (0,0,0), degenerate monotone stem, no connected-sum mismatch

## Context

The integral homology cobordism group $\Theta^3_{\mathbb Z}$ and the order of
Seifert-fibered homology spheres in it form a recognized frontier
(Froyshov, Manolescu, Hendricks-Manolescu-Zemke, Dai-Manolescu).
Dai-Manolescu reduced involutive Heegaard Floer homology of almost-rational
plumbings (hence all Seifert spheres) to graded-root combinatorics, and gave
same-orientation connected-sum formulae for the involutive correction terms
$\underline d$ (dl) and $\bar d$ (du) versus the Ozsvath-Szabo $d$.
This record settles the involutive-local input for one named small-Seifert
sphere outside all settled families: $\Sigma(2,3,13)$.

## Definitions

- $Y=+\Sigma(2,3,13)$: the Brieskorn sphere with Seifert data
  $a=(2,3,13)$, oriented as the boundary of its negative-definite
  star-shaped plumbing (Dai-Manolescu convention). Explicitly
  $b=(1,1,2)$ via $(P/a_i)b_i\equiv -1\bmod a_i$ with $P=78$,
  $P\sum b_i/a_i=77=P-1$, $e_0=-1$, $e=-1/78<0$.
  Hirzebruch-Jung arms: $2/1=[2]$, $3/1=[3]$, $13/2=[7,2]$.
- Plumbing graph $G$ (5 vertices): central $v_0(-1)$ joined to
  $v_1(-2)$, $v_2(-3)$, $v_3(-7)$; $v_3$ joined to $v_4(-2)$.
  Intersection matrix $M$ in order $v_0,\dots,v_4$:
  $[[-1,1,1,1,0],[1,-2,0,0,0],[1,0,-3,0,0],[1,0,0,-7,1],[0,0,0,1,-2]]$.
  Canonical $K=(-1,0,1,5,0)$, characteristic, $K^2=-5$, $\sigma=0$.
- $\chi(x)=-(K\cdot x+x\cdot Mx)/2$ on $L=\mathbb Z^5$;
  $J_0(x)=-x-z_0$ with $Mz_0=K$, $z_0=(-8,-4,-3,-2,-1)$.
- $S_n=\{\chi\le n\}$; graded root $R(Y)$ from components of $S_n$.
- $(d,\underline d,\bar d)$: Ozsvath-Szabo and involutive correction terms.
- $M(Y)$: maximal monotone graded subroot (Dai-Manolescu Sec 6);
  $h(Y)$: involutive local equivalence class.

## Result

For $Y=+\Sigma(2,3,13)$ as above:

1. $(d,\underline d,\bar d)=(0,0,0)$.
2. $M(Y)$ is the degenerate bare stem $M(-2,-2)$; $h(Y)=0$
   (same local class as $S^3$).
3. Consequently every same-orientation multiple $\#_k Y$ ($k\ge 1$) and
   every mixed-sign sum of $\pm Y$ has trivial involutive local class
   ($\underline d=\bar d=d=0$); no Dai-Manolescu
   $(\bar d-\underline d)$ connected-sum mismatch separates any
   $\mathbb Z$-linear combination of $\pm Y$ from $S^3$.
4. The homology-cobordism order of $[Y]$ in $\Theta^3_{\mathbb Z}$ is
   **not** decided (instanton/Seiberg-Witten $r_s$ or other methods may
   still apply). Full $HF^-(Y)$ is nontrivial (short-branch torsion) but
   not a cobordism invariant.

## Proof / evidence

Three agreeing routes (all re-run; 18/18 checks pass in `verify_all.py`):

(a) Neumann-Siebenmann (exact): exhaustive search over all $32$ binary
vectors gives the unique $0/1$ Wu vector $w=(0,0,1,0,1)$ with
$Mw=(1,0,-3,1,-2)$ matching diagonal parities;
$w^T M w=-5=\mathrm{sign}(G)$, so
$\bar\mu=(\mathrm{sign}-w^2)/8=0$.
Dai Theorem 1.2: $\underline d(Y)=-2\bar\mu=0$.
Control: same code on the $\Sigma(2,7,15)$ plumbing returns the
published $\bar\mu=2$.

(b) $d$-invariant (exact): completing the square
$\chi(x)=\chi(x_s)-q/2$ with $Mx_s=-K/2$,
$x_s=(4,2,3/2,1,1/2)$, $\chi(x_s)=-5/8$ exactly;
$-M$ positive definite by exact Sylvester (all five leading principal
minors $=1$); $\chi$ integer-valued ($K$ characteristic), so
$\min\chi=0=\chi(0)$ and $d=-2\min\chi=0$ (Dai Theorem 2.9).
Independently the Dedekind-sum $+$ $\tau$-minimum formula gives shift
$0$, $\min\tau=0$, $d=0$: $N_0=7$,
$\tau=[0,1,0,0,0,0,0,1]$, collapsed extrema $[0,1,0,1]$,
Dedekind sums $s(1,2)=0$, $s(1,3)=1/18$, $s(2,13)=4/13$.
Dai Theorem 1.2: $\bar d(Y)=d(Y)=0$.

(c) Graded-root top plus greedy monotone extraction (Dai Sec 6):
ellipsoid enumeration with exact bound from $Q=(-M)^{-1}$,
$\mathrm{diag}(Q)=(78,20,9,2,1)$, center $x_s$, $\chi(x_s)=-5/8$:
$S_0$: 32 points in 3 components of sizes $(8,8,16)$; $J_0$ swaps the
two size-8 components and fixes the size-16 one (explicit).
$S_1$: 192 points, 1 component; $S_2,S_3,S_4$: 512/992/1792 points,
each single-component and $J_0$-stable; $\chi$ integral throughout.
Since $S_1$ is connected and $S_n$ are nested, $S_n$ is connected for
all $n\ge 1$: exactly one branch event ($3\to 1$ at level $0\to 1$),
bare stem below. The uppermost $J_0$-invariant vertex is at top degree
$-2$ (the fixed middle $S_0$ component); its cluster $C_{-2}$ is
trivial, the outer tip pair (also degree $-2$) fails the
strictly-greater test and is deleted; nothing further occurs.
$M(Y)=$ degenerate stem $M(-2,-2)$: $d_1=h_1+2=0$,
$\underline d=r_1+2=0$, $\bar\mu=0$. Agrees with (a)+(b).
$HFI^-$ top: coker stem top at $-2$ ($\bar d=0$),
ker stem top at $-2$ ($\underline d=0$) (Dai Theorem 1.1).
Structural discriminator: the $J_0$-fixed $S_0$ middle component;
$\Sigma(2,7,15)$ has none, hence a tall non-degenerate root there.

Connected-sum consequence: $h(Y)=0$ implies
$h(\#_k Y)=0^{\otimes k}=0$ and $h(-Y)=0^\vee=0$ via the cited
Hendricks-Hom-Lidman tensor/dual functoriality and Dai Corollary 1.4 /
Theorem 7.2 (same-orientation formulae), so all (mixed-)sign multiples
are locally trivial.

## Limitations

- Decides the involutive-local witness (absent), not the order of $[Y]$.
- Orientation fixed to the Dai plumbing-boundary convention; the triple
  $(0,0,0)$ dualizes to itself so is orientation-robust here.
- Cited theorems used as statements; computational verification is
  independent. Sublevel enumeration uses float arithmetic with tolerance
  (exact $+1$ box margin, post-filter); the triple itself also follows
  from the enumeration-independent exact Wu and completing-the-square
  routes.
- Superseded exploratory drafts (crashed $5$-level search, an early
  $\underline d=-2$ mis-assignment, an $M^{-1}$-pairing $9/8$ draft, a
  hand-evaluated connected-sum note) are dead ends and excluded.

## Reproducibility

Run `python3 output/artifacts/verify_all.py` (stdlib + numpy):
18/18 PASS (graph, Wu + control, tau + d, root top).
Supplements (exact rational unless noted):
`dmax_exact.py` (Sylvester + completing the square),
`seifert_orient.py` (orientation ID),
`sublevel_deep.py` ($S_2$--$S_4$ connectivity),
`stem_lemma.py` (one branch event, greedy terminates),
`hfi_top.py` (explicit $J_0$ swap, ker/coker tops).

## References

- I. Dai, C. Manolescu, Involutive Heegaard Floer homology and plumbed
  three-manifolds, arXiv:1704.02020.
- K. Seetharaman, W. Yue, I. Zhu, Patterns in the Lattice Homology of
  Seifert Homology Spheres, arXiv:2110.13405 (d-periodicity $+\prod$,
  monotone-subroot periodicity $+2\prod$; does not transfer $M$ to 13).
- J. Tweedy, Heegaard Floer homology and several families of Brieskorn
  spheres, arXiv:1206.2558 (disjoint families).
- C. Karakurt, B. Savk, Almost simple linear graphs, homology cobordism
  and connected Heegaard Floer homology, arXiv:2204.06597
  (odd-first-entry families, disjoint).
- K. Hendricks et al., Surgery exact triangles in involutive Heegaard
  Floer homology, arXiv:2011.00113 (complementary tool).
- S. Lee, B. Savk, On homology spheres of the trivial local equivalence
  class, arXiv:2508.15384 (non-lift results).
