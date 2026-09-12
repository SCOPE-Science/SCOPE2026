# Sharp local (non-)unimodularity dichotomy at isolated rank-zero points in dimension 4

## Context

Let $(M^4,\pi)$ be a real Poisson manifold with bivector $\pi$ and sharp map
$\pi^\sharp:T^*M\to TM$. For a volume form $\mu$, the modular vector field
$X_\mu$ is defined by $\mathcal{L}_{X_f}\mu = X_\mu(f)\,\mu$ for all
$f\in C^\infty(M)$, where $X_f=\pi^\sharp(df)$ is the Hamiltonian field.
In coordinates with $\mu=dx_1\wedge\cdots\wedge dx_4$,
$(X_\mu)^j=\sum_i\partial_i\pi^{ij}$ up to a global sign convention fixed once.
Changing volume $\mu'=e^\varphi\mu$ shifts
$X_{\mu'}=X_\mu-X_\varphi$ up to sign, so the class
$[X_\mu]\in H^1_\pi(M)$ (Poisson cohomology) is well defined.
$(M,\pi)$ is unimodular if $[X_\mu]=0$, i.e. some volume is invariant under
all Hamiltonian flows, and non-unimodular otherwise.
A vector field $V$ is Poisson if $\mathcal{L}_V\pi=0$.

The admitted compact target asked whether every compact oriented Poisson
$4$-fold with exactly one nondegenerate rank-zero point and regular rank $2$
elsewhere is non-unimodular. The natural first step is the transverse-local
question: do the qualitative local data (isolated rank-zero point, rank $2$
on the punctured neighbourhood) already determine (non-)unimodularity?
This record answers that local question in the negative, inside the
degenerate stratum where the $1$-jet of $\pi$ at the zero vanishes.

## Definitions

- Isolated rank-zero point: $p$ with $\pi(p)=0$ and $\pi(x)\ne 0$ for
  $0<|x-p|$ small; regular rank $2$ on the punctured neighbourhood means
  $\mathrm{rk}\,\pi(x)=2$ there (as opposed to rank $4$).
- Degenerate stratum: the $1$-jet $j^1_p\pi$ vanishes (abelian linearization);
  nondegenerate means $j^1_p\pi$ defines a nondegenerate Lie-algebra structure.
- Germ (non-)unimodularity: $[X_\mu]\ne 0$ (resp. $=0$) in germ Poisson
  cohomology, i.e. no (resp. some) local volume near $p$ is
  Hamiltonian-invariant; for the zero-field case this is witnessed by
  $X_\mu\equiv 0$ for the standard volume.
- Conformal germ: $\pi_c=f\,\pi_0$ with $\pi_0=\partial_1\wedge\partial_2$
  and $f=|x|^2=x_1^2+x_2^2+x_3^2+x_4^2$ on $\mathbb{R}^4$.
- Jacobian germ: $\pi_J^{ij}=\sum_{k,l}\epsilon_{ijkl}\,\partial_kC_1\,\partial_lC_2$
  with $C_1=x_1x_3+x_2x_4$ and $C_2=(x_1^2+x_2^2-x_3^2-x_4^2)/2$.

## Result

Theorem (certified local dichotomy). In dimension $4$, the qualitative
hypotheses of an isolated rank-zero point with regular rank $2$ on the
punctured neighbourhood do not determine (non-)unimodularity, even locally
and even within the degenerate stratum where the $1$-jet of $\pi$ vanishes.
Both alternatives occur:

(a) The conformal germ $\pi_c=|x|^2\,\partial_1\wedge\partial_2$ has zero set
exactly $\{0\}$, rank $2$ off $0$, vanishing $1$-jet, modular field
$X=(-2x_2,2x_1,0,0)$ with nonzero linearization $DX(0)\ne 0$ while every
Hamiltonian field $X^c_g=f\,X^0_g$ vanishes to order $\ge 2$ at $0$; hence
$[X]\ne 0$ in germ cohomology and no neighbourhood admits a
Hamiltonian-invariant volume.

(b) The Jacobian germ $\pi_J$ from $(C_1,C_2)$ above has real zero set exactly
$\{0\}$ via $\pi^{13}+\pi^{24}=|x|^2$, rank exactly $2$ at every $x\ne 0$,
vanishing $1$-jet, and identically zero modular field; hence unimodular as a germ.

(c) Flow-fixing lemma: at any isolated zero of $\pi$, every Poisson vector
field vanishes, so $X_\mu(p)=0$ always and point evaluation can never witness
$[X_\mu]\ne 0$; any transverse witness must use jets.

Consequence. No purely transverse-local argument ignoring nondegeneracy and
global topology can prove universal compact non-unimodularity; the $1$-jet
witness of (a) is sharp but not universal since (b) has the identical
vanishing pattern with zero modular field. Any future proof of the compact
nondegenerate claim must use the nondegenerate linearization and a global
volume pairing essentially.

## Proof / evidence

Lemma proof: the flow $\phi_t$ of a Poisson field satisfies
$(\phi_t)_*\pi=\pi$, hence preserves the zero set; an isolated zero is fixed
for small $t$, so $V(p)=0$.

Part (a): $[\pi_c,\pi_c]=0$ verified symbolically; $f$ vanishes only at $0$,
so rank drops only there; components are homogeneous quadratics. Modular
components $X^2=\partial_1f=2x_1$, $X^1=-\partial_2f=-2x_2$ (up to the tracked
global sign). Structural divisibility $\pi_c=f\pi_0$ forces every Hamiltonian
to be $O(|x|^2)$ while $X$ has nonzero linear part; if $X=X^c_h$ then
$DX(0)=0$, a contradiction, and the same kills $X-X^c_\varphi$ for any volume
change.

Part (b): Jacobi $[\pi_J,\pi_J]=0$; $C_1,C_2$ are Casimirs so rank $\le 2$.
With $A=D^2C_1$, $B=D^2C_2$, $\det(sA+tB)=(s^2+t^2)^2>0$ for real
$(s,t)\ne(0,0)$, so $dC_1,dC_2$ are independent off $0$; equivalently
$\pi^{13}+\pi^{24}=|x|^2$ forces $\pi_J(x)=0\Rightarrow x=0$. A nonzero
skew-symmetric matrix has rank $\ge 2$, capped at $2$ by the Casimirs, giving
rank exactly $2$ off $0$. Direct divergence gives $X\equiv 0$. All components
are homogeneous quadratics, so $j^1_0\pi_J=0$.

All identities are certified by exact rational arithmetic in
`output/artifacts/verify.py` (sympy only), printing `VERIFY_OK`.
Sign conventions for the modular field are tracked explicitly; all
zero/nonzero verdicts hold for either sign.

## Limitations

Proved as germ statements with machine certificates: Lemma, Propositions A/B,
and the dichotomy theorem. Not proved: the compact universal target in either
direction; no global non-unimodularity proof and no one-point compact
invariant-volume model are claimed. Both germs have abelian linearization and
hence lie outside the nondegenerate compact hypothesis; they bound it sharply
from the degenerate side. Compactification of the unimodular germ faces
Morse/Casimir global obstructions (a second zero or rank drop at infinity is
generic) not overcome here.

## Reproducibility

Run `python3 output/artifacts/verify.py` (requires only `sympy`; exact
rational arithmetic, no numerical approximation). Expected output ends with
`VERIFY_OK`. Checks A1-A5 cover the conformal germ; J1-J6 cover the Jacobian
germ as labelled in the script.

## References

- Y. Kosmann-Schwarzbach, Poisson Manifolds, Lie Algebroids, Modular Classes:
  A Survey (SIGMA 2008.005 / ESI1973).
- R. Flores-Espinoza, On Poisson structures on R^4 (arXiv:1306.5254v2):
  trace/divergence formulas, rank and modular-field identities.
- G. Ortenzi, V. Rubtsov, S. Tagne Pelap, Integer solutions and H-invariant
  Jacobian Poisson structures (arXiv:1103.4267): Jacobian bracket, rank two,
  Casimir structure.
- R. Ibanez et al., Duality and modular class of a Nambu-Poisson structure
  (math/0004065); P. Damianou, F. Petalidou, Poisson Brackets with Prescribed
  Casimirs; R. Caseiro, R. Fernandes, Modular class of a Poisson map.
