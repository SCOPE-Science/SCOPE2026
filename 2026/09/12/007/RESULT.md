# Outermost tilt wall W3 for the branch-fixed Kuznetsov class on a general special Gushel–Mukai threefold

## Context

Special Gushel–Mukai (GM) threefolds are double covers of ordinary GM
threefolds branched over a divisor, with a covering involution. Their
Kuznetsov components are the natural home of Bridgeland stability questions
that feed special-fourfold stability transport and Enriques-category moduli.
Prior work establishes existence and Serre-invariance of stability conditions
on GM Kuznetsov components, preservation under pullback–pushforward, K-stability
of special GM manifolds, and moduli-stack descriptions, but computes no
explicit involution-equivariant tilt wall for a primitive branch-related class
on a general special GM threefold.

## Definitions

Let $X$ be a general special GM threefold: a double cover
$\pi\colon X\to Y$ of an ordinary GM threefold branched over general
$B\in\lvert 2H\rvert$, with covering involution $\iota$.
Generality gives $\mathrm{Pic}(X)=\mathbb{Z}\cdot H$, $H^{3}=10$,
$H\cdot c_{2}(T_{X})=24$, $c_{1}(T_{X})=H$ (index one, $-K_{X}=H$).
Let $\mathcal{U}$ be the rank-2 tautological subbundle and
$\mathrm{Ku}(X)=\langle\mathcal{O}_{X},\mathcal{U}^{\vee}\rangle^{\perp}
\subset D^{b}(X)$.
Hirzebruch–Riemann–Roch reads
$\chi(F)=\mathrm{ch}_{3}(F)+\tfrac12H\!\cdot\!\mathrm{ch}_{2}(F)
+\tfrac{17}{6}k+r$ for $\mathrm{ch}(F)=(r,kH,e,t)$.

For $x$ in the branch locus ($\iota(x)=x$) let
$E_{x}=\mathbf{L}_{\mathcal{O}_{X}}\mathbf{L}_{\mathcal{U}^{\vee}}
(\mathcal{O}_{x})=\mathrm{pr}(\mathcal{O}_{x})\in\mathrm{Ku}(X)$.
Write $v=-\mathrm{ch}(E_{x})=(r,k,e,t)=(5,-2,-2,5/3)$.
Then $e=-2r-4k$, $t=-5k/6$, $\chi(\mathcal{O}_{X},v)=0$,
$\gcd(5,2)=1$ (primitive), $\Delta_{H}(v)=100k^{2}-20re=600$.
Tilt data at $\beta=-3/2$: $D(v)=H^{2}\!\cdot\!\mathrm{ch}_{1}^{\beta}
=10k+15r=55$, $A(v)=H\!\cdot\!\mathrm{ch}_{2}^{\beta}
=e+15k+45r/4=97/4$.
All data are $\iota$-equivariant by canonicity of the mutations and
fixedness of $x$.

## Result

For $v=(5,-2,-2)$ at $\beta=-3/2$, among all integral
($e\in\tfrac12\mathbb{Z}$) factor classes $w$ with
$0<D_{w}<D_{v}$ and Bogomolov inequalities
$\Delta_{H}(w)\ge 0$, $\Delta_{H}(v-w)\ge 0$,
the section heights
$\alpha^{2}(w)=(A_{v}D_{w}-A_{w}D_{v})/5(r_{v}D_{w}-r_{w}D_{v})$
with $\alpha^{2}>0$ are finite: 9 walls (18 oriented records), with maximum
$\alpha^{2}_{\max}=13/10$ attained uniquely up to swap by
$w=(1,0,-7)$, $u=(4,-2,5)$.
The top wall $W_{3}$ is the semicircle
$F(b)=-100b^{2}-330b-140=0$ with endpoints $b_{1}=-14/5$, $b_{2}=-1/2$,
centre $c=-33/20$, $R^{2}=529/400$, $R=23/20$, apex $23/20$,
section $\alpha^{2}=13/10$ at $\beta=-3/2$.
The vertical line $\beta=-3/2$ itself carries no wall, and the ray
$\{\beta=-3/2,\ \alpha>\sqrt{13/10}\}$ is a tilt chamber:
no strictly tilt-semistable equivariant object of class $v$ exists there.
Tilt-stable objects induce Serre-invariant Bridgeland-stable objects in
$\mathrm{Ku}(X)$ by the standard double-tilt construction.

## Proof / evidence

Exact `Fraction`-arithmetic certificates using only Python stdlib.
`ku_lattice.py` gives `HRR_LATTICE_OK`: $\chi(\mathcal{O}_{X})=1$,
$\chi(\mathcal{U}^{\vee})=5$, $\chi(\mathcal{U}^{\vee},\mathcal{U}^{\vee})=1$,
$\chi(\mathcal{U}^{\vee},\mathcal{O}_{X})=0$, Ku relations for $v$,
primitivity, $\Delta_{H}(v)=600$.
`wall_enumeration.py` gives `CERTIFICATE_OK`:
(i) denominator lemma $G=25(5m-11r_{w})\ne 0$ for $1\le m\le 10$
($11$ prime); (ii) exact-line check $A_{w}=97m/44\in\tfrac14\mathbb{Z}$
iff $11\mid m$, impossible; (iii) negative-width lemma excluding
$r_{w}\le-1$, $G>0$ walls with both discriminants, verified analytically
($N=5f/4-2\ge 19/8>0$) and by machine; (iv) swap symmetry reducing to the
finite box $r_{w}\in\{0,\dots,5\}$; (v) complete enumeration of
half-integral $e_{w}$ with both discriminants giving 18 records topped by
$13/10$; (vi) $W_{3}$ semicircle expansion verified.
Wall-freeness above the top section plus standard large-volume
nonemptiness yields the chamber claim; equivariance is automatic since
Harder–Narasimhan and Jordan–Hölder filtrations are canonical.

## Limitations

Pic rank one uses generality (Noether–Lefschetz general); higher Picard-rank
specializations are not covered. The Bogomolov input is the classical
$H$-discriminant for tilt-semistable factors; the generalized BG inequality
is not needed for this upper envelope. $D=0$ torsion factors cut out no
$(b,a)$-wall and are excluded by definition. Object existence in the chamber
uses the wall-free ray plus cited standard large-volume/moduli nonemptiness.
Serre-invariant induction uses the standard double-tilt construction; no new
construction is claimed.

## Reproducibility

Run `python3 artifacts/ku_lattice.py` (expect `HRR_LATTICE_OK`) and
`python3 artifacts/wall_enumeration.py` (expect `CERTIFICATE_OK`,
18 records, top $13/10$, $W_{3}$ data). Stdlib only, exact arithmetic.

## References

- K-stability of special Gushel–Mukai manifolds (doi:10.46298/epiga.2026.13743).
- Pertusi–Robinett, stability conditions on Kuznetsov components of GM
  threefolds and Serre functor (doi:10.1002/mana.202200010).
- Perry–Pertusi–Zhao, stability conditions and moduli spaces for Kuznetsov
  components of GM varieties (doi:10.2140/gt.2022.26.3055).
- Debarre–Kuznetsov, Gushel–Mukai varieties: moduli
  (doi:10.1142/s0129167x20500135).
