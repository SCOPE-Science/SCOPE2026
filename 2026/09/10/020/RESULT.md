# Rossi CR Paneitz degree-2 kernel theorem (with refutation of the degree-2 negativity witnesses)

## Context

The Rossi sphere is the standard compact strictly pseudoconvex non-embeddable
CR 3-manifold family. For real $|t|<1$ let
$T^{1,0}_t=\mathbb{C}(Z_1+t\bar Z_1)$ on $S^3\subset\mathbb{C}^2$, with $Z_1$ the
standard $(1,0)$ field and fixed standard contact form $\theta$. Classical
work (Rossi; Burns–Epstein; Kohn; Boutet de Monvel; Lempert) makes the
embeddability-stability boundary of this family a recognized question.
Chanillo–Chiu–Yang proved qualitative Rossi Paneitz negativity with
degree-$1$ negative directions; Takeuchi proved infinitely many negative
Paneitz eigenvalues via subspaces $V_k$ in odd total degree $2k-1$.
The admitted target assumed the lowest even-degree trial function
$u^*=z_1^2+\bar z_1^2$ gives a uniform negativity witness
$\langle P_t u^*,u^*\rangle\le -c|t|^2$.

## Definitions

- $S^3=\{|z|^2+|w|^2=1\}$, $(z,w)=(z_1,z_2)$.
- $Z_1=\bar w\,\partial_z-\bar z\,\partial_w$,
  $Z_{\bar1}=w\,\partial_{\bar z}-z\,\partial_{\bar w}$,
  $X=Z_1^2$, $Y=Z_{\bar1}^2$, $s=1-t^2$.
- Rossi frame $Z(t)=Z_1+tZ_{\bar1}$, $Z_{\bar{}}(t)=Z_{\bar1}+tZ_1$.
- Standard Kohn Laplacians $\Box=\Box_b=-Z_1Z_{\bar1}$,
  $\bar\Box=\bar\Box_b$; Rossi operators $\Box_t,\bar\Box_t$;
  CR Paneitz $P_t=\bar\Box_t\Box_t+\mathcal{Q}_t$.
- Takeuchi Lemma 5.1 (fixed standard $\theta$):
  $(1-t^2)\Box_t=\Box-tX-tY+t^2\bar\Box$,
  $(1-t^2)^2\mathcal{Q}_t=4tY-4t^2(\Box+\bar\Box)+4t^3X$.
- $\mathcal{H}_{p,q}(S^3)$: bidegree-$(p,q)$ spherical harmonics;
  Folland eigenvalues $\Box=(p+1)q$, $\bar\Box=p(q+1)$ on
  $\mathcal{H}_{p,q}$.
- $u^*(z)=z_1^2+\bar z_1^2\in\mathcal{H}_{2,0}\oplus\mathcal{H}_{0,2}$.

## Result

**Theorem.** For every real $t$ with $|t|<1$, with fixed standard $\theta$,

$$P_t|_{\mathcal{H}_{2,0}(S^3)\oplus\mathcal{H}_{0,2}(S^3)}\equiv 0.$$

In particular for $u^*=z_1^2+\bar z_1^2$ (nonzero, $u^*(1,0)=2$,
$\|u^*\|_{L^2}^2=4\pi^2/3$),

$$P_t u^*\equiv 0,\qquad \langle P_t u^*,u^*\rangle\equiv 0
\quad\forall\,|t|<1,$$

under any $L^2$ pairing (fixed or deformed volume form).

**Corollaries.** (i) The inequality
$\langle P_t u^*,u^*\rangle\le -c|t|^2$ with $c\ge 1/2$ on
$0<|t|\le 1/2$ is false — indeed it fails for every $c>0$ at every
$t\ne 0$. (ii) The point certificate
$\langle P_{1/4}u^*,u^*\rangle\le -1/8$ is false (the pairing is $0$).

## Proof / evidence

By conjugation it suffices to treat $f=z^2\in\mathcal{H}_{2,0}$,
$a=Xf=2\bar w^2\in\mathcal{H}_{0,2}$. Exact polynomial differentiation in
$(z,w,\bar z,\bar w)$ gives $Xf=a$, $Yf=0$, $Xa=0$, $Ya=4f$,
$\Box f=0$, $\bar\Box f=2f$, $\Box a=2a$, $\bar\Box a=0$
(the Folland values verified via the $T$-action, not merely quoted).
Writing $B_t,\bar B_t$ for the numerators $(1-t^2)\Box_t$,
$(1-t^2)\bar\Box_t$:

$$B_t f=-ta+2t^2f,\quad \bar B_t f=2f-ta,\quad
  \bar B_t a=-4tf+2t^2a,$$

so $\bar B_tB_t f=8t^2f-4t^3a$, while
$(1-t^2)^2\mathcal{Q}_t f=-8t^2f+4t^3a$. Their sum vanishes:
$(1-t^2)^2P_t f=0$, and $s=1-t^2\ne0$ gives $P_t f=0$.
Conjugation gives the $g=\bar z^2$ branch; linearity gives
$P_t u^*=0$. Independent routes confirm it: direct vector-field
construction of $-Z(t)Z_{\bar{}}(t)$, $-Z_{\bar{}}(t)Z(t)$,
$+4tZ_{\bar{}}(t)^2$ (no eigenvalue table; real $t$ and formal
$s=\bar t$); Chanillo normalization
($\Box^C_t$, $A=4ti/s$, $P^t_0=\tfrac14(\Box^C\bar\Box^C-4i(Af_1)_1)$)
giving $P^t_0(z^2)=P^t_0(\bar z^2)=0$; full
$\mathcal{H}_{2,0}\oplus\mathcal{H}_{0,2}$ basis sweep
($YX=4\mathrm{Id}$, $XY=4\mathrm{Id}$); structure re-derivation
($l=1-t^2$, $A^{11}=i4t/(1-t^2)^2$, Takeuchi (6.1) match
$P_1z=-3t^2z$); stdlib-only `Fraction` replay.
Nontriviality: $\|u^*\|^2=2\mathrm{Vol}(S^3)/3=4\pi^2/3>0$ and $f$ is
standard-CR but not Rossi-CR for $t\ne0$, so this is not the trivial
pluriharmonic-kernel fact. Sharpness: $P_t\ne0$ on
$\mathcal{H}_{1,0}$ ($-3t^2(1-t^2)^{-2}$), on $\mathcal{H}_{3,0}$ and on
tested $\mathcal{H}_{1,1}$ directions.

## Limitations

Proved for fixed standard $\theta$ under Takeuchi and Chanillo
conventions (real $t$; formal complex-$t$ robustness checked as a
polynomial identity). Says nothing new about Kohn closed range or
Szegő sign beyond classical context. The verified degree-$1$ negative
direction is context only, not a packaged claim. No uniform interval
obstruction is established; the window question stays open for other
witnesses.

## Reproducibility

From the lane directory:

```
python3 output/artifacts/verify_target_pairing.py   # 31 checks
python3 output/artifacts/verify_kernel_bruteforce.py
python3 output/artifacts/verify_kernel_sweep.py
python3 output/artifacts/verify_structure.py
python3 output/artifacts/verify_chanillo_norm.py
python3 output/artifacts/verify_stdlib.py           # stdlib only
```

Expected: `ALL_VERIFY_OK` / `ALL_STRUCTURE_OK` / `ALL_CHANILLO_OK` /
`ALL_STDLIB_OK` (sympy 1.12 for differentiation artifacts).

## References

- Y. Takeuchi, CR Paneitz operator on non-embeddable CR manifolds,
  arXiv:2407.16185 v2 (Lemma 5.1, Sec. 5–6).
- S. Chanillo, H.-L. Chiu, P. C. Yang, Embeddability for
  three-dimensional CR manifolds and CR Yamabe invariants,
  arXiv:1007.5020 / Duke Math. J. 161 (2012) (Thm 1.3, Ex. 2.4/Prop. 2.5,
  Sec. 4 degree-1 directions and (BE) positivity).
- T. Abbas et al., Spectrum of the Kohn Laplacian on the Rossi sphere,
  arXiv:1708.05624.
- D. Bosch et al., CR embeddability of quotients of the Rossi sphere via
  spectral theory, arXiv:2110.12413.
