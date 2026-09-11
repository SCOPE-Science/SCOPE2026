# Cubic triangle chamber: first-order theta-product coefficient equals two-pointed log invariant (both 1)

## Context

The pair $(X,D_{\mathrm{tri}})$ with $X$ a smooth cubic surface ($dP_3$) and
$D_{\mathrm{tri}}=D_1+D_2+D_3$ a triangle (cycle) of lines is the flagship
reducible-boundary (Looijenga) log Calabi–Yau surface. Gross–Hacking–Keel
construct its mirror via theta functions defined by broken lines, but no
published identity pins the broken-line product coefficient for a named line
class to a two-pointed log invariant with split contacts. This record gives the
minimal such test.

## Definitions

- Toric model: $(\bar Y,\bar D)=(\mathbf P^2,\{x=0\}+\{y=0\}+\{z=0\})$;
  $\pi:(X,D)\to(\bar Y,\bar D)$ blows up two distinct interior (non-node)
  points on each $\bar D_i$. Then $X$ is smooth cubic, $D_i=H-E_{i1}-E_{i2}$
  are $(-1)$-curves with $D_i\cdot D_j=1$ ($i\ne j$), $D\sim -K_X$.
- Tropical base: $\mathbf R^2$ with rays $\rho_1=(1,0),\rho_2=(0,1),
  \rho_3=(-1,-1)$; $v_1=(1,0)$, $v_2=(0,1)$; chamber
  $\sigma_{12}=\langle\rho_1,\rho_2\rangle$ (cubic triangle chamber).
- Line class: $L:=H-E_{31}$ (strict transform of $\mathbf P^2$-line through
  exactly one blown-up point on $\bar D_3$). Then
  $L\cdot D=(1,1,0)$, $L^2=0$, $L\cdot(-K_X)=2$.
- Invariant $N_{L,(1,1,0)}$: genus-0 log invariant in class $L$ with contact
  orders $(1,1,0)$ to $(D_1,D_2,D_3)$ (two boundary markings) plus one interior
  marking with a point insertion. Virtual dimension:
  $\mathrm{vdim}=-1+n=-1+3=2$, cut by $\mathrm{ev}_3^*([\mathrm{pt}])$
  (codimension 2) to a 0-dimensional count.
- Product coefficient $c$: coefficient of $\vartheta_{v_1+v_2}$ at curve class
  $0$ in $\vartheta_{v_1}\cdot\vartheta_{v_2}$, i.e. class-0 broken-line pairs
  $(\gamma_1,\gamma_2)$ with $s(\gamma_1)+s(\gamma_2)=v_1+v_2$,
  $e(\gamma_1)+e(\gamma_2)=0$. Work mod $\mathfrak m^2\subset
  \mathbf k[\mathrm{NE}(X)]$.

## Result

In chamber $\langle\rho_1,\rho_2\rangle$:

$$\vartheta_{v_1}\cdot\vartheta_{v_2}
  =1\cdot\vartheta_{v_1+v_2}+(\text{terms }z^E,\ E>0),$$

i.e. $c=1$, and

$$N_{L,(1,1,0)}=1,$$

hence $c=N_{L,(1,1,0)}=1$ with no obstructing broken-line class.

## Proof / evidence

1. **Setup (intersection theory).** $D_i^2=-1$, $D_i\cdot D_j=1$,
   $L\cdot D=(1,1,0)$, $L^2=0$, $L\cdot(-K_X)=2$ by direct
   $\mathrm{Pic}(X)$ computation (replayed in `artifacts/verify.py` §A).
2. **First-order scattering.** Each initial wall carries $f_i=1+w_i$,
   $w_i\in\mathfrak m/\mathfrak m^2$; $\log\theta_i=\langle n_i,\cdot\rangle w_i
   =O(\mathfrak m)$. Commutators are $O(\mathfrak m^2)$, so the ordered product
   around the origin is order-independent mod $\mathfrak m^2$: the three
   initial walls are consistent to first order with no outgoing walls.
   Standard Gross–Siebert first-order vanishing; pairing matrix recorded in §B.
3. **Broken-line count $c=1$.** Endpoint $Q=(5,5)\in\mathrm{Int}(\sigma_{12})$.
   Straight rays $Q+\mathbf R_{\ge0}v_i$ avoid all three wall rays
   ($y=0$; $x=0$; $x=y\le0$) — checked in §C. Straight lines exist wall-free
   with class $0$. Any bent line carries nonzero effective class $E>0$, so
   class-0 pairs force straight+straight; straight lines are unique, giving
   exactly one pair, $c=1$. Exhaustive class-0 pair search in §C.
4. **Log invariant $N=1$.** Explicit witness (replayed §D): with
   $p_{31}=[1{:}2{:}0]$, other blowups $[0{:}1{:}7],[0{:}1{:}11],
   [1{:}0{:}13],[1{:}0{:}17],[1{:}5{:}0]$, general $y=[1{:}3{:}5]$, the unique
   line $\ell=\overline{p_{31}y}$ ($10x-5y+z=0$) meets $\bar D_1,\bar D_2$
   transversely at non-nodes, avoids other blowups, and meets $\bar D_3$ only
   at blown-up $p_{31}$; its strict transform in class $L$ has contacts
   $(1,1,0)$. Nonempty. Uniqueness: any contributor pushes to a
   $\mathbf P^2$-line ($H$-degree 1); disjointness from $D_3$ forces passage
   through $p_{3j}$; with general $y$ two points fix a unique line. No multiple
   covers (primitive), no contracted/split components ($L\cdot H=1$
   indecomposable; $L=D_3+E_{32}$ splitting lies in boundary/exceptional locus
   and cannot pass through general interior point). Transverse immersion is
   unobstructed ($H^1(\mathbf P^1,\mathcal O)=0$), contributing $+1$. Hence
   $N_{L,(1,1,0)}=1$.
5. **Identity.** $c=1=N_{L,(1,1,0)}$; the target's equality branch holds and the
   obstructing-class branch is vacuous.

## Limitations

- First-order (class-0 coefficient) statement only; higher-order walls and
  deeper bends not computed.
- One labelled representative $L=H-E_{31}$; other $(1,1,0)$ distributions
  follow by $S_3$ relabelling (stated, not separately replayed).
- General-position hypotheses via explicit witness plus standard dimension
  count, not machine-checked; rigid-line $+1$ uses standard unobstructedness,
  no general virtual-class computation.

## Reproducibility

`python3 artifacts/verify.py` (stdlib only) prints
`ALL CHECKS PASSED: c=1, N=1`, replaying §§A–D.

## References

- Gross–Hacking–Keel, Mirror symmetry for log Calabi-Yau surfaces I,
  doi:10.1007/s10240-015-0073-1 — general theta algebra; no $(1,1,0)$ numeric
  coefficient for cubic triangle line class.
- Gross–Siebert, Canonical wall structure / intrinsic mirror symmetry,
  doi:10.1007/s00222-022-01126-9 — consistency machinery used mod $\mathfrak m^2$.
- Bousseau–Brini–van Garrel, Stable maps to Looijenga pairs,
  doi:10.2140/gt.2024.28.393 — maximal-contact closed forms, not split-contact.
- Gräfnitz, Theta functions, broken lines and 2-marked log GW invariants,
  doi:10.1007/s00229-025-01640-z — smooth-divisor case, complementary boundary.
- Mandel, Theta bases and log GW of cluster varieties,
  doi:10.1090/tran/8398 — different (cluster) setting.
- Arguz, Explicit equations for mirrors to log CY surfaces, arXiv:1810.08356 —
  equations only.
