# Strict trianguline tangent drop at the first bad-pair cell (GL4, w=[4231], w'=[1324])

## Context

The trianguline variety $X_{\mathrm{tri}}$ parametrizes trianguline deformations of a
mod-$p$ Galois representation. Breuil–Hellmann–Schraen (BHS, arXiv:1702.02192)
modelled its completed local rings at crystalline regular generic points by
algebraic local models $\widetilde{X}_w$ built from Grothendieck's simultaneous
resolution, yielding a predicted tangent integer $d_{\mathrm{BHS}}$ and a
non-strict upper bound (Prop 4.1.5(ii)). Mowlavi (arXiv:2303.06022) proved an
exact tangent formula for *good* pairs $(w',w)$, gave counterexamples to the BHS
conjecture for *bad* pairs starting at $n=4$, and left open whether the BHS
bound becomes strict for bad pairs ("We do not know if this upper bound
becomes strict for bad pairs", Intro; cf. Prop 3.3.3 which is only a partial
converse).

This record settles that strictness at its minimal instance.

## Definitions

- $p=3$, $K=\mathbf{Q}_3$, $n=4$, regular Hodge–Tate weights $(0,1,2,3)$.
- $w=[4231]$, $w'=[1324]$ in $\mathcal{S}_4$ (one-line notation), $\ell(w)=5$,
  $\ell(w')=1$, $w'\le w$ Bruhat via saturated chain
  $1324<1342<1432<2431<4231$.
- $ww'^{-1}=[4321]=w_0$, $d_{ww'^{-1}}=4-\mathrm{cycles}(w_0)=2$,
  $\mathfrak{t}^{ww'^{-1}}$: $t_1=t_4,\ t_2=t_3$.
- Orbits of $ww'^{-1}$ on $\{1,2,3,4\}$: $\{1,4\},\{2,3\}$;
  Mowlavi's $(a,b)=(1,2)$ lie in distinct orbits, so the pair is bad and the
  good-pair formula is inapplicable.
- $x$ is the crystalline companion point on $X_{\mathrm{tri}}$ attached to
  $(w,w')$ for a generic crystalline $\rho:G_K\to\mathrm{GL}_4(\bar{\mathbf{Q}}_3)$
  with distinct Frobenius eigenvalues (existence assumed via Kisin).
- $d_{\mathrm{BHS}}=\dim X_{\mathrm{tri}}-d_{ww'^{-1}}
  +\dim T_{\overline{BwB/B},w'B}-\ell(w')=26-2+5-1=28$,
  with $\dim X_{\mathrm{tri}}=n^2+[K:\mathbf{Q}_p]n(n+1)/2=16+10=26$.
- $x_{\mathrm{pdR}}=(B,w'B,0)$ (crystalline so $N_W=0$).
- $F(\lambda)$: Mowlavi Lemma 5.3.3 equation for $q=1$, $(a,b)=(1,2)$:
  $F(\lambda)=s_1D(\lambda)x_{31}+s_2E(\lambda)x_{41}-P_2(\lambda)x_{31}$
  with $D=(t_2+\lambda)(t_3+\lambda)$, $E=(t_2+\lambda)u_{34}$,
  $P_2=(t_4+\lambda)(t_2+\lambda)$, i.e. $F=(t_2+\lambda)A$,
  $A=s_1(t_3-t_4)x_{31}+s_2u_{34}x_{41}$ ($s_1,s_2=\pm1$).

## Result

**Theorem.** At the above point,
$$\dim T_x X_{\mathrm{tri}} \le d_{\mathrm{BHS}}-1 = 27,$$
witnessed by transfer of the named local-model extra equation to a nonzero
linear relation (class of $d(t_1-t_2)$) on $T_x X_{\mathrm{tri}}$.

Strict improvement over the BHS non-strict bound $28$; settles the open
strictness at the minimal bad cell. Exact equality $=27$ is NOT claimed.

## Proof / Evidence

- **BHS injection + bridge (cited):** BHS Prop `inegtangent`(i)/Prop 2.5.3 gives
  $T_{X_w}\hookrightarrow T_{\overline{U}_w}(11)\oplus\mathfrak{t}^{ww'^{-1}}(2)
  \oplus(\mathfrak{u}\cap\mathrm{Ad}(w')\mathfrak{u})(5)$, an 18-dim bound space
  $W_{\mathrm{BHS}}$. BHS Cor `localdescrip`/THEdiagram/Cor `represent2` give
  framed maps formally smooth of relative dimension $[K:\mathbf{Q}_p]n(n+1)/2=10$,
  framing quotient dropping $[K:\mathbf{Q}_p]n^2=16$; BHS Prop 4.1.5(i) gives
  $\dim T_{X_{\mathrm{tri}}}=\dim X_{\mathrm{tri}}-16+\dim T_{X_w}=10+\dim T_{X_w}$
  (applies as $\rho$ is crystalline hence de Rham).
- **Explicit $F$ (computed):** In dehomogenized chart $t=u=0$, $x_{31}=1+dx_{31}$,
  $x_{41}=dx_{41}$: $F_1=A$, $F_0=t_2A$ vanish at $x_{\mathrm{pdR}}$;
  $dF_0=0$, $dF_1=s_1(dt_3-dt_4)\ne0$ for all sign choices. With
  $R_1=(1,0,0,-1)$ ($dt_1-dt_4$), $R_2=(1,-1,1,-1)$ ($dt_1+dt_3-dt_2-dt_4$),
  t-rank goes $2\to3$, cutting the t-tangent $4\to1$ (all-equal line).
  Modulo $R_2$ and flag/$u$ rows, $[dF_1]=-s_1\,d(t_1-t_2)$ (unit multiple).
  Hence $\dim T_{X_w}\le 11+1+5=17$.
- **Pullback nonzero:** framed/bridge maps induce tangent surjections
  (formal smoothness); framing quotient drops only framing directions on which
  $dF_1$ has no component. So $L_{\mathrm{tri}}$ is a nonzero functional
  vanishing on $T_xX_{\mathrm{tri}}$: one dependence among the $d_{\mathrm{BHS}}$-sized
  candidate basis, certifying rank $\le d_{\mathrm{BHS}}-1$.
- **Schubert smoothness fixing $d_{\mathrm{BHS}}=28$ (computed):** full chart
  enumeration in $Z^*P_{w'}$ chart at $w'B$ gives sole generator
  $f=z_{31}z_{43}-z_{41}$, $df(0)=-dz_{41}\ne0$; every other $(p,q)$ bound is
  vacuous ($r+1$ exceeds submatrix size). Hence
  $\dim T_{\mathrm{closure}}=5=\ell(w)$.
- **Ledger:** local model $\le18-1=17$; bridge $+10$: $\le27=d_{\mathrm{BHS}}-1$.
- **Machine replay (stdlib only):**
  `python3 output/artifacts/verify_target.py` → `VERIFY_OK`;
  `python3 output/artifacts/jacobian_F.py` → `JACOBIAN_OK`;
  `python3 output/artifacts/transfer_certificate.py` → `TRANSFER_CERTIFICATE_OK`.

## Limitations

- Exact equality ($=d_{\mathrm{BHS}}-1$, full target) not claimed; ruling out
  further hidden equations at $x_{\mathrm{pdR}}$ remains open.
- Generic crystalline $\rho$ existence assumed (Kisin); no $\rho$ constructed.
- $(\varphi,\Gamma)$-side enters via cited BHS diagram (theorem numbers logged),
  not a direct cocycle matrix; covered by Prop 4.1.5(i) equality.
- Cited results (BHS diagram/smoothness/injection, BB–Ginsburg $t=0$ inclusion,
  Mowlavi lemmas/propositions/theorems) cited with numbers, not re-proved.
  All recomputable combinatorics/Jacobians machine-checked.

## Reproducibility

Frozen identifiers ($w,w'$, chain, $ww'^{-1}$, $d$, orbits, witness,
Gale sets, Schubert count, $d_{\mathrm{BHS}}$) plus $F$-Jacobian and transfer
ledger replay from the record alone via the three scripts above.

## References

- C. Breuil, E. Hellmann, B. Schraen, A local model for the trianguline
  variety and applications, arXiv:1702.02192.
- S. Mowlavi, The trianguline variety, tangent spaces and the
  Grothendieck–Springer resolution, arXiv:2303.06022 (esp. Sec. 5.3,
  Lemma 5.3.3, Prop 5.3.4, Ex. 5.3.5, Thm 5.3.7; Prop 3.3.3 open strictness).
- S. Mowlavi, Tangent spaces on the trianguline variety at companion points,
  arXiv:2303.05472 (good-pair boundary only).
- L. Qian, The Local Companion Points Conjecture, arXiv:2510.00281
  (companion existence, no tangent bound).
