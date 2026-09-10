# No chirally cosmetic slope pairs with |H1| <= 30 on the asymmetric L-space census knot t12533

## Context

Let $K=t12533$, the sporadic asymmetric hyperbolic L-space census knot: closure of the positive 4-braid of length 27
$[1,1,2,2,1,2,2,2,2,2,2,2,2,2,1,2,2,3,2,1,1,2,2,1,3,2,2]$
(Teragaito, arXiv:2510.04403, Table 2; Baker–Teragaito, arXiv:2510.07618),
genus 12. Its two literature-recorded consecutive quasi-alternating slopes are
$\{37,38\}$ (Seifert basis) with branch sets $K12n407$, $L12n789$
(Teragaito Table 1; Baker–Kegel–McCoy, arXiv:2409.09839, Tables 2–3).
Purely cosmetic L-space cells are closed by general theorems, but
orientation-reversing (chirally cosmetic) pairs
$S^3_r(K) \cong -S^3_s(K)$ on chiral hyperbolic knots do occur elsewhere
(Ren), leaving $t12533$ open. This record decides the $|H_1|\le 30$ chiral cell.

## Definitions

Slopes $r=m/n$, $s=m/n'$ are written with $m>0$, $\gcd(m,n)=\gcd(m,n')=1$;
$|H_1(S^3_{m/n})|=|m|$. Chirally cosmetic means $S^3_r(K)\cong -S^3_s(K)$
with $r\ne s$. Types (Ichihara–Ito–Saito): $++$/$--$ (same/opposite sign,
$n+n'\ne 0$) and $00$ ($n+n'=0$). Finite-type data: $a_2,a_4$ Conway
coefficients; $v_3(K)=-V_K'''(1)/144-V_K''(1)/48\in \frac14\mathbb Z$
($1/4$ on right trefoil); chiral constant
$C_0=(7a_2^2-a_2-10a_4)/(8v_3)$ when $v_3\ne 0$.

## Result

For $K=t12533$, no distinct slopes $r\ne s$ with $|H_1|\le 30$ give an
orientation-reversing homeomorphism $S^3_r(K)\cong -S^3_s(K)$.
Exact per-knot values:
$$a_2=52,\quad a_4=681,\quad v_3=323/4,\quad
C_0=\frac{7a_2^2-a_2-10a_4}{8v_3}=\frac{12066}{646}=\frac{6033}{323}$$
irreducible ($\gcd(6033,323)=1$; $6033=3\cdot 2011$, $323=17\cdot 19$).
Every same-sign pair would need $m/(n+n')=C_0$, forcing $6033\mid m$
(none in scope); opposite-sign pairs are excluded as $t12533$ is a
nontrivial L-space knot (Varvarezos Thm 1.8); $00$-type is excluded since
$v_3\ne 0$ (IIS Thm 1.1); integral distinct pairs (including QA
$\{37,38\}$) already differ in $|H_1|$. No Floer d-sum is claimed.

## Proof / evidence

1. Frozen object: 4-braid word (length 27) and QA slopes $\{37,38\}$
   from Teragaito/BKM tables (both outside $|H_1|\le 30$).
2. Alexander via reduced Burau (trefoil/figure-8 validated):
   $\Delta(t)=t^{24}-t^{23}+t^{20}-t^{19}+t^{17}-t^{16}+t^{15}-t^{14}
   +t^{12}-t^{10}+t^9-t^8+t^7-t^5+t^4-t+1$,
   $\Delta(1)=1$, symmetric, $\deg 24=2g$ ($g=12=(27-4+1)/2$);
   $\det=|\Delta(-1)|=1=|V(-1)|$. Auditor independently recomputed via
   standard quotient-Burau: identical quotient.
3. Conway via exact $T_k$ solve, independently confirmed by
   interpolation in $w=t+1/t-2$: $a_2=52$, $a_4=681$, $\nabla(0)=1$.
4. Jones via Temperley–Lieb categorical trace ($\dim\mathrm{Catalan}(4)=14$,
   trefoil-validated):
   $V(t)=-t^{26}+t^{25}-t^{24}+t^{23}-t^{22}-t^{19}+t^{18}-t^{17}+t^{16}+t^{14}+t^{12}$,
   $V(1)=1$, $V''(1)=-312$, $V'''(1)=-10692$; cross-route
   $-V''(1)/6=52=a_2$; $v_3=323/4$ (trefoil control $1/4$).
5. Numerator $7a_2^2-a_2-10a_4=12066\ne 0$, so IIS Thm 1.3 alternative (i)
   impossible; every $\pm$-type pair must satisfy $m/(n+n')=6033/323$.
   Coprimality forces $m=6033k$, $n+n'=323k$, hence $|m|\ge 6033$;
   machine enumeration over $1\le m\le 30$ empty; analytic bound
   $(n+n')=323m/6033\le 1.61<3$ contradicts distinct same-sign
   ($n+n'\ge 3$; negative same-sign contradicts $C_0>0$).
6. Opposite-sign: Varvarezos arXiv:2112.03144 Thm 1.8.
   $00$-type: IIS Thm 1.1 since $v_3=323/4\ne 0$.
   Integral distinct: $|H_1|$ values differ. Cases exhaust scope.
   IIS Thm 1.10(i-c) verified NOT to fire ($O(K)=12066/323>52/3$) and unused.
7. Replay: `python3 output/artifacts/verify_target.py` $\to$ `VERIFY_OK (31/31)`
   (stdlib + sympy, exact rational arithmetic).

## Limitations

Cited theorems (IIS Thms 1.1/1.3, Varvarezos Thm 1.8) used as stated
(statements verified against arXiv HTML; proofs not re-derived);
conventions checked via trefoil controls. No Ni–Wu d-formula and no Walker
surgery formula invoked: no d-invariant is claimed; the Walker-type equation
and Dedekind values are logged datum only (Walker normalization unchecked,
vacuous-in-scope, not load-bearing). No SnapPy/Sage in this environment:
canonical-triangulation volume logs not available and not claimed; slope
datum uses BKM quotients + Teragaito Kirby proofs + exact homology orders.
$\det=1$ doubly corroborated. Torsion table $t_0..t_{11}=[4,4,4,3,3,2,2,2,1,1,1,1]$
is slope datum only, not load-bearing.

## Reproducibility

Frozen word, polynomials, $C_0$, Diophantine enumeration, torsion table,
Dedekind values all recomputed by `output/artifacts/verify_target.py`
(31 checks). Scripts: `alexander_t12533.py`, `jones_tl.py`,
`jones_state.py`, `chiral_analysis.py`, `dsums.py`.

## References

- Baker–Kegel–McCoy, Quasi-alternating surgeries, arXiv:2409.09839.
- Ichihara–Ito–Saito, On constraints for knots to admit chirally cosmetic surgeries, arXiv:2112.04156.
- Varvarezos, Heegaard Floer homology and chirally cosmetic surgeries, arXiv:2112.03144.
- Teragaito, Quasi-alternating surgeries on asymmetric L-space knots in the census, arXiv:2510.04403.
- Baker–Teragaito, On asymmetric hyperbolic L-space knots of braid index four, arXiv:2510.07618.
