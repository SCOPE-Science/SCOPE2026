# Bott-Chern (1,1) jump versus rigidity on a named pluriclosed Hopf/class-VII-type solvmanifold 3-fold stratum

## Context

Bott-Chern numbers are the accepted Hodge-number replacement on compact
non-Kahler manifolds (Schweitzer/Angella/Popovici program). How
$h^{1,1}_{BC}$ varies under deformation, and how it obstructs
pluriclosed (SKT) metrics, has few concrete witnesses. Oeljeklaus-Toma
(OT) and Hopf-type 3-folds are the natural solvmanifold window with
invariant-form control. The literal "pluriclosed OT type-(2,1)" fibre is
empty: OT admits pluriclosed iff $s=t$
(Angella-Dubickas-Otiman-Stelzig, arXiv:2201.06377, Cor. 3; Otiman,
arXiv:2009.02599). The admitted strict-solvmanifold alternate below
preserves the target's family (solvmanifold, pluriclosed, universal
cover $\\mathbf{H}\\times\\mathbf{C}$ factor, $b_1(S)$-window).

## Definitions

- $M\\in SL(3,\\mathbf{Z})$ the companion matrix of $x^3-x-1$
  (roots $\\alpha\\approx 1.3247$ real, $\\beta,\\bar\\beta$ complex,
  $\\alpha|\\beta|^2=1$), with admissible rank-one totally-positive unit
  group from $\\alpha$.
- $S_M$ the Inoue-Bombieri surface of OT type $(1,1)$ for $M$,
  with left-invariant $(1,0)$-coframe $(\\omega,\\gamma)$ satisfying
  $d\\omega=\\frac{i}{2}\\omega\\wedge\\bar\\omega$,
  $d\\gamma=A\\,\\omega\\wedge\\gamma+B\\,\\bar\\omega\\wedge\\gamma$,
  $A=ib/4-c/2$, $B=-ib/4+c/2$, $A+B=0$, where
  $b=2\\log|\\beta|/\\log\\alpha=-1$ (SKT number condition).
- $E_i=\\mathbf{C}/(\\mathbf{Z}+i\\mathbf{Z})$ with coordinate $u$.
- $X_0=S_M\\times E_i$ (compact complex non-Kahler 3-fold,
  $b_1(X_0)=3$), with product pluriclosed metric
  $\\omega_0=\\mathrm{pr}_S^*\\omega_S+\\mathrm{pr}_E^*\\omega_E$
  ($\\omega_S$ Gauduchon $=$ SKT on a surface, $\\omega_E$ flat).
- $\\alpha_0=i\\,du\\wedge d\\bar u$ (invariant $d$-closed $(1,1)$-form).
- $\\mu=\\bar\\omega\\otimes\\partial_u$
  (invariant Beltrami differential).
- $\\beta:=\\tau=\\omega\\wedge\\gamma\\wedge du\\wedge\\bar\\gamma$
  ($(3,1)$-form; $\\bar\\partial$-closed, hence
  $\\partial\\bar\\partial$-closed test class, iff $b=-1$).
- $\\mathcal{B}$ the Kuranishi versal base of $X_0$;
  $\\mathcal{S}\\subset\\mathcal{B}$ the analytic germ through $0$ of
  the Bott-Chern extendability locus of $[\\alpha_0]_{BC}$;
  $B_\\mu\\hookrightarrow\\mathcal{B}$ the immersed disk with
  Kodaira-Spencer class $[\\mu]$.

## Result

Let $X_0,\\alpha_0,\\mu,\\beta$ be as above. Then:

1. $[\\alpha_0]_{BC}\\ne 0$ in $H^{1,1}_{BC}(X_0)$
   (E-fibre period $2\\,\\mathrm{Area}(E_i)>0$).
2. $P:=\\int_{X_0}(\\mu\\lrcorner\\alpha_0)\\wedge\\beta
   =-\\int dV\\ne 0$ (invariant volume pairing).
3. $[\\mu\\lrcorner\\alpha_0]\\ne 0$ in
   $H^{0,2}_{\\bar\\partial}(X_0)$, hence $[\\mu]\\ne 0$ in
   $H^1(X_0,T_{X_0})$, and $\\phi(t)=t\\mu$ solves Maurer-Cartan
   exactly, defining $B_\\mu$ with Kodaira-Spencer class $[\\mu]$.
4. The fixed de Rham class $[\\alpha_0]_{dR}$ has
   $(0,2)_t$-component $t[\\mu\\lrcorner\\alpha_0]\\ne 0$ to first
   order: $[\\alpha_0]$ admits no Dolbeault, hence no Bott-Chern,
   extension to first order along $B_\\mu$. The Xia first BC
   obstruction $o_1([\\alpha_0]_{BC})\\ne 0$ (arXiv:1403.0285,
   Thm 1.2).
5. $\\mathcal{S}\\cap B_\\mu=\\{0\\}$ as germs, so $\\mathcal{S}$
   is proper.
6. With $h^{p,q}_{BC}(t)$ finite and upper semicontinuous
   (Schweitzer Hodge theory; Xia Sec. 3) and the Xia jump theorem
   (Thm 1.1/3.1),
   $$h^{1,1}_{BC}(X_t)\\le h^{1,1}_{BC}(X_0)-1
     \\qquad (0\\ne t\\in B_\\mu\\ \\text{small}),$$
   i.e. $h^{1,1}_{BC}(X_0)\\ge h^{1,1}_{BC}(X_t)+1$ for nearby
   $t\\notin\\mathcal{S}$ along the certified direction.

The computable record is: $M$ as above, $b=-1$,
$\\mu\\lrcorner\\alpha_0=i\\,\\bar\\omega\\wedge d\\bar u$,
$\\bar\\partial\\tau=\\frac{i(1+b)}{2}(\\cdots)=0$,
$P=-\\int dV\\ne 0$, $[\\alpha_0]_{BC}\\ne 0$ by $E$-fibre period.
This strictly subsumes the preset first-order obstruction criterion
(named $X_0/\\alpha_0/\\mu/\\beta$, closedness certificates,
nonzero pairing number).

## Proof / evidence

Lemma 1 (invariant coframe): $\\bar\\partial\\mu=0$ since
$\\bar\\partial\\bar\\omega=0$ ($d\\bar\\omega$ is pure $(1,1)$);
$\\mu\\lrcorner\\alpha_0=i\\,\\bar\\omega\\wedge d\\bar u$ is
$\\bar\\partial$-closed as a wedge of closed forms;
$\\bar\\partial_{X_0}=\\bar\\partial_S+\\bar\\partial_E$ gives
$\\bar\\partial\\tau=\\bar\\partial_S(\\omega\\wedge\\gamma
\\wedge\\bar\\gamma)\\wedge du
=(\\frac{i}{2}-B-\\bar A)\\,
\\omega\\wedge\\bar\\omega\\wedge\\gamma\\wedge\\bar\\gamma$
with $B+\\bar A=-ib/2$, i.e. coefficient $i(1+b)/2$, zero iff
$b=-1$, which holds.

Lemma 2 (Stokes certificates): if $\\alpha_0=\\partial\\bar\\partial f$,
restriction to an $E$-fibre
$j_s:E\\hookrightarrow X_0$ gives
$\\int_E j_s^*\\alpha_0=0$ against $2\\,\\mathrm{Area}>0$.
$(\\mu\\lrcorner\\alpha_0)\\wedge\\tau$ is a wedge of all six
coframe covectors, hence nowhere-zero $(3,3)$ $c\\,dV$, $c=-1$.
If $\\mu\\lrcorner\\alpha_0=\\bar\\partial\\eta$ then
$P=\\pm\\int\\eta\\wedge\\bar\\partial\\tau=0$ (Stokes;
$\\partial(\\eta\\wedge\\tau)$ has type $(4,2)=0$), contradiction.
If $\\mu=\\bar\\partial V$ then
$\\mu\\lrcorner\\alpha_0=\\bar\\partial(V\\lrcorner\\alpha_0)$ by
$\\bar\\partial\\alpha_0=0$, contradiction.
$\\beta=\\tau$ is $\\bar\\partial$-closed hence a valid
Aeppli/Serre test class; $P$ is the Xia Rem. 2.3 pairing number for
$r_{BC,\\bar\\partial}([\\alpha_0]_{BC})$.

Lemma 3 + jump: $[\\mu,\\mu]=0$ ($S$-pullback coefficients killed by
$\\partial_u$), so $\\phi(t)=t\\mu$ is a genuine deformation curve.
Standard Griffiths/Kodaira-Spencer calculus (Xia Thm 1.2) gives the
$o_1\\ne 0$ obstruction; naturality of $r_{BC,\\bar\\partial}$ lifts
Dolbeault non-extendability to Bott-Chern non-extendability.
$\\mathcal{S}$ is the zero locus of the holomorphic relative-BC
obstruction series (analytic germ by Grauert coherence, cf. Xia
Sec. 3); nonzero directional derivative gives
$\\mathcal{S}\\cap B_\\mu=\\{0\\}$. Semicontinuity + Xia jump
theorem yields the $\\ge 1$ drop. Replayed by
`artifacts/verify_target.py` (ALL VERIFY_OK).

## Limitations

- Uses cited authorities for: Gauduchon existence on surfaces;
  Schweitzer finite-dimensionality/semicontinuity of $H_{BC}$;
  Xia relative-BC obstruction formula and jump theorem;
  OT/Inoue construction and pluriclosed criterion.
- $\\mathcal{S}$ is a Kuranishi germ; only $B_\\mu$-transverse
  properness and the nearby drop along $B_\\mu$ are proved.
- Exact $h^{1,1}_{BC}(X_0)$ is not computed; only
  $h^{1,1}_{BC}(X_0)\\ge 1$ and the $\\ge 1$ drop.
- The $\\arg$-parameter $c$ cancels; no explicit $c$ needed.

## Reproducibility

`artifacts/verify_target.py` (stdlib + sympy) checks: OT-$(2,1)$
degeneracy ($s\\ne t$); $A+B=0$ and
$\\bar\\partial(\\tau)$ coefficient $i(1+b)/2$ vanishing at $b=-1$;
pairing wedge signs giving $P=-\\int dV\\ne 0$; Kunneth count
$h^{0,2}(X_0)=1$. Run: `python3 artifacts/verify_target.py`.

## References

- Angella-Dubickas-Otiman-Stelzig, arXiv:2201.06377 (OT double
  complex, Bott-Chern, $s=t$ SKT criterion).
- Otiman, arXiv:2009.02599 (OT pluriclosed characterization).
- Kasuya, arXiv:2008.06649 (OT type-$(s,1)$ harmonics;
  Angella-Tomassini check).
- Xia (Lin-Ye), arXiv:1403.0285 (BC/Aeppli obstruction formula,
  jump theorem; Iwasawa application).
- Hu-Xia, arXiv:2506.12288 (canonical Aeppli/BC jumping formulas;
  general theory, different object).
- Schweitzer (BC/Aeppli Hodge theory); Inoue-Bombieri surface
  theory; Tosatti-Weinkove arXiv:1209.2662 and Sferruzza-Tomassini
  arXiv:2206.06904 (Inoue-adjacent, no jump/pairing).
