# Sharp Berger positivity and strict quarter-pinching window with certified triaxial boxes and a volume-normalized systolic bound on S^3

## Context

The differentiable quarter-pinched sphere theorem turns on which metrics satisfy
$K>0$ and strict $1/4$-pinching ($K_{\max}/K_{\min}<4$). The Berger and
left-invariant triaxial families on $S^3$ are the classical testbed where the
boundary between pinched and non-pinched, positive and indefinite curvature is
often quoted pointwise. This record certifies the exact global window on the
Berger line, exact-fraction triaxial boxes, and a sharp volume-normalized
systolic upper bound, with an honest statement of what is not classified.

## Definitions

Let $E_1,E_2,E_3$ be left-invariant fields on $SU(2)=S^3$ with
$[E_1,E_2]=2E_3$ cyclically, $\theta^i$ dual to $E_i$, $a,b,c>0$, and

$$g_{a,b,c}=a^2\,\theta^1\otimes\theta^1+b^2\,\theta^2\otimes\theta^2+c^2\,\theta^3\otimes\theta^3.$$

Put $e_i=E_i/a_i$ orthonormal ($a_1=a,a_2=b,a_3=c$),
$u=a^2$, $v=b^2$, $w=c^2$. The Berger line is $a=b=1$, $c=\tau>0$,
$s=\tau^2$. Write $K_{ij}=\langle R(e_i,e_j)e_j,e_i\rangle$.
Let $\mathrm{sys}$ denote the shortest closed-geodesic length and
$\mathrm{Vol}(g_{a,b,c})=2\pi^2abc$ (scaling from $\mathrm{Vol}(1,1,1)=2\pi^2$).

## Result

**Lemma (curvature formula).** With $c_1=2a/(bc)$, $c_2=2b/(ca)$,
$c_3=2c/(ab)$, the curvature operator is diagonal in the coordinate
$2$-planes and

$$K_{12}=\frac{(u-v)^2+2w(u+v)-3w^2}{uvw},\quad K_{23}=\frac{(v-w)^2+2u(v+w)-3u^2}{uvw},\quad K_{31}=\frac{(w-u)^2+2v(w+u)-3v^2}{uvw}.$$

Every sectional curvature is the convex combination
$K(x\wedge y)=K_{23}n_1^2+K_{31}n_2^2+K_{12}n_3^2$ for orthonormal $x,y$
with $n=x\times y$ in the $\{e_i\}$ frame. Each principal circle
$t\mapsto\exp(tE_i)$ is a closed geodesic of length $L_i=2\pi a_i$.

**Theorem A (Berger line, sharp).** For $g_{1,1,\tau}$,
$K_{12}=4-3s$, $K_{23}=K_{31}=s$ with $s=\tau^2$.
(i) $K>0$ everywhere iff $\tau^2<4/3$, i.e. $\tau\in(0,2/\sqrt{3})$;
at $s=4/3$, $K_{12}=0$; e.g. $\tau=2$ gives $K_{12}=-8$.
(ii) Strict $1/4$-pinching $K_{\max}/K_{\min}<4$ holds iff

$$4/7<s<16/13,\quad\text{i.e.}\quad 2/\sqrt{7}<\tau<4/\sqrt{13}\approx(0.7559,1.1094),$$

with ratio exactly $4$ at both endpoints. The $s<4/3$ threshold is
classical (Volper/Berestovskii) and is reproved here; no originality is
claimed for it alone. The sharp pinching window is the new exact statement.

**Theorem B (certified triaxial boxes, $c=1$ slice).**
(a) Every $g_{a,b,1}$ with $(a,b)\in[0.92,1.08]^2$ has $K>0$ everywhere:
numerators $N_{12}\ge 241/625>0$, $N_{23},N_{31}\ge 64009/390625>0.16$.
(b) Every $g_{a,b,1}$ with $(a,b)\in[0.98,1.02]^2$ is strictly
$1/4$-pinched: all sectionals lie in $[1999/2601,\,7300000/5764801]$ and
$K_{\max}/K_{\min}\le 18987300000/11523837199\approx1.648<2<4$.
Witnesses: $(a,b,c)=(1/4,1/4,1)$ has $K_{12}=-704$.

**Theorem C (systolic envelope).** For all $a,b,c>0$, with
$C=2^{4/3}\pi^{2/3}\approx5.4051353801$,

$$\mathrm{sys}(g_{a,b,c})^2\le C\,\mathrm{Vol}(g_{a,b,c})^{2/3},$$

via $\mathrm{sys}\le L_{\min}=2\pi\min(a,b,c)$ and
$L_{\min}^2/\mathrm{Vol}^{2/3}=C(\min^3/abc)^{1/3}\le C$ since
$\min^3\le abc$, with equality in the constant iff $a=b=c$ (round metric,
where $\mathrm{sys}=2\pi$ classically).

## Proof / evidence

Cartan computation $2\langle\nabla_{e_i}e_j,e_k\rangle=
\langle[e_i,e_j],e_k\rangle-\langle[e_j,e_k],e_i\rangle
+\langle[e_k,e_i],e_j\rangle$ plus
$R(e_i,e_j)e_k$ from the left-invariant formula. Independently
re-derived by the auditor in sympy: structure constants as above give $6$
nonzero connection components with $\Gamma_{ii,k}=0$ exactly; the three
coordinate sectionals minus the closed form simplify to $0$; all probed
off-diagonal components ($R_{1223},R_{1231},R_{2331}$, etc.) are $0$,
proving diagonality and the convex-combination formula. The artifact
additionally checks the closed form against the Cartan computation at $6$
rational triples in exact arithmetic and the convex-combination identity
on random planes only as float evidence (residual $\le3\times10^{-15}$).

Berger branch: substitution gives $K_{12}=4-3s$, $K_{23}=K_{31}=s$
exactly; global extrema $K_{\min}=\min(s,4-3s)$,
$K_{\max}=\max(s,4-3s)$ when $4-3s>0$; positivity iff $s<4/3$;
pinching for $s\le1$: $(4-3s)/s<4\iff s>4/7$; for $s\ge1$:
$s/(4-3s)<4\iff s<16/13$; exact ratio $4$ at $s=4/7$ and $s=16/13$ by
integer arithmetic.

Boxes: exact-fraction numerator/denominator bounds. Positivity box uses
$(u-v)^2\ge0$ and monotone lower bounds $2(u+v)-3\ge4u_{lo}-3$,
$2v+2-3u\ge2u_{lo}+2-3u_{hi}$. Pinching box uses
$|u-v|\le\bar u-\underline u$ for the upper bound and drops
nonnegative squares for lower bounds, with denominators bounded by
$\underline u^2\le uv\le\bar u^2$; positivity of the dropped-constant
lower numerators justifies the denominator direction. Witness and
systolic algebra are exact rational checks.

## Limitations

Full $[0.25,2]^2$ doubly-warped classification is not achieved and not
claimed; only the Berger line globally plus the two small $c=1$ boxes.
Systolic bound is one-sided ($\mathrm{sys}\le L_{\min}$); no lower bound
on $\mathrm{sys}$. $\mathrm{Vol}=2\pi^2abc$ scaling and round
$\mathrm{sys}=2\pi$ are invoked as classical standard facts. The
artifact's random-plane check for the diagonal-operator identity is float
evidence only; the general identity is closed auditor-symbolically.

## Reproducibility

Stdlib-only verifier `output/artifacts/verify_berger_pinching.py` prints
`ALL_OK` with exit $0$:
`env -u PYTHONPATH python3 output/artifacts/verify_berger_pinching.py`.
Covers Cartan-vs-closed-form (6 triples), geodesic circles, Berger
identities, sharp thresholds, box certificates, witnesses, systolic
algebra.

## References

- Inoguchi–Munteanu, Homogeneity of magnetic trajectories in the Berger
  sphere, arXiv:2406.15886 — Berger preliminaries; no region/pinching/
  systolic classification.
- Chen–Gaspar, Volume spectrum of fiber bundles and the widths of Berger
  spheres, arXiv:2505.09548 — Berger widths; no positivity/pinching
  region or systolic rigidity over doubly-warped rectangle.
- Olmos–Rodriguez-Vazquez, Hopf fibrations and totally geodesic
  submanifolds, arXiv:2302.11711 — cites Volper/Berestovskii positivity
  iff $\tau\in(0,4/3)$; no $1/4$-pinching window or systolic inequality.
- Brendle–Schoen, Sphere theorems in geometry, arXiv:0904.2604; Caramello–
  Neubauer, Transverse sphere theorems, arXiv:2505.01378 — general sphere
  theorems, not the Berger pinching locus.
- Live arXiv searches for quarter-pinched Berger, Berger systole/systolic,
  Berger sectional-curvature formula, left-invariant $S^3$ pinched returned
  no overlapping classification.
