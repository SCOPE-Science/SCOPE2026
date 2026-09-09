# Exact linear Mahler-deficit rate on the 4D diagonal shadow path (reversal of the cubic obstruction)

## Context

Mahler's conjecture is open for $n \ge 4$: the cube / Hanner polytopes are
conjectured minimizers of the symmetric volume product. The unit cube
$B^n_\infty$ is a strict local minimizer in Banach–Mazur distance
(Nazarov–Petrov–Ryabogin–Zvavitch), Hanner polytopes likewise (Kim), and
Kim–Zvavitch give qualitative reverse-Blaschke–Santalo stability near
unconditional bodies. No sharp deficit rate near the 4-cube was known.
The admitted target conjectured a flat cubic upper envelope
$P(K_s) \le P(B)(1+Cs^3)$, $C \le 2$, along the diagonal truncation family
below. The finding refutes that envelope for every $C$ and reverses the
intended obstruction.

## Definitions

Let $B = [-1,1]^4$ and for $s \in [0,1/2]$

$$K_s = \{x \in \mathbb{R}^4 : |x_i| \le 1,\ |x_1+x_2+x_3+x_4| \le 4-s\}.$$

$K_s$ is the 4-cube with the two diagonal corners $\pm(1,1,1,1)$ truncated
by the slab orthogonal to $u=(1,1,1,1)$; it is centrally symmetric and
convex. Write $P(K)=\mathrm{Vol}(K)\,\mathrm{Vol}(K^\circ)$ for the Mahler
product and $\delta(s)=\ln d_{BM}(K_s,B)$ for the log Banach–Mazur distance.

## Result (headline claim)

With $P(B)=32/3$:

1. **Exact volumes.**
   $$\mathrm{Vol}(K_s) = 16 - \frac{s^4}{12}, \qquad
     \mathrm{Vol}(K_s^\circ) = \frac{2}{3} + \frac{s}{12(4-s)},$$
   hence
   $$P(s) := P(K_s) = \left(16-\frac{s^4}{12}\right)
     \left(\frac{2}{3}+\frac{s}{12(4-s)}\right), \quad P(0)=\frac{32}{3}.$$
2. **Exact deficit, linear rate.** With $D(s)=P(s)-P(B)$,
   $$D(s) = \frac{4s}{3(4-s)} - \frac{s^4}{18} - \frac{s^5}{144(4-s)},$$
   so $D(s)/s \to 1/3$ as $s \to 0^+$ (i.e. $P'(0^+)=1/3$), and
   $$D(s) \ge \frac{2631}{8064}\,s \ge \frac{s}{4} \quad \text{on }(0,1/2].$$
3. **No cubic envelope.** For every fixed $C$, $P(K_s) \le P(B)(1+Cs^3)$
   fails on every interval $[0,r]$, $r>0$. In particular the $C=2$ envelope
   is violated at $s=1/1000,\,1/100,\,1/10$ (exact rational check).
4. **Reversal: quadratic stability confirmed on this path.** The inclusion
   $(1-s/4)B \subset K_s$ gives
   $$\delta(s) \le -\ln(1-s/4) \le \frac{s(4+s)}{16} \le \frac{9s}{32}$$
   on $(0,1/2]$. Hence $D(s) \ge \delta(s)$, so
   $D(s)/\delta(s)^2 \ge 1/\delta(s) \to +\infty$: every fixed-constant
   quadratic stability bound $D \ge c\,P(B)\,\delta^2$ holds eventually on
   this path — including $c=10^{-3}$. This diagonal family is therefore
   **not** a flat-rate obstruction direction.
5. **Certified band for $\delta$.** $\delta(s)$ lies in the linear band
   $[s/140,\,s(4+s)/16]$ at the checked nodes
   $\{1/1000,1/100,1/10,1/4,1/2\}$ (lower end via Mahler monotonicity,
   upper end from the inclusion). The stronger bound $\delta \ge s/8$ is
   left open and is not needed for (3)–(4).

## Proof / evidence

- $P(B)=32/3$: $\mathrm{Vol}(B)=16$; $B^\circ=\{y:\sum|y_i|\le 1\}$ is the
  union of 16 orthant simplices each of volume $1/24$, so
  $\mathrm{Vol}(B^\circ)=16/24=2/3$ (exact `Fraction` determinants).
- Truncation: near $(1,1,1,1)$ put $t_i=1-x_i$; the cut piece
  $\{t_i\ge 0,\sum t_i<s\}$ is the 4-simplex $\mathrm{conv}\{0,se_1,\dots,
  se_4\}$ of volume $s^4/24$, box constraints vacuous for $s\le 1/2$;
  symmetric at $-(1,1,1,1)$. Hence $\mathrm{Vol}(K_s)=16-2(s^4/24)$.
- Polar: $K_s=B\cap S_s$, $S_s=\{|u\cdot x|\le 4-s\}$; polar of a symmetric
  slab intersection is the convex hull of slab polars:
  $K_s^\circ=\mathrm{conv}\{\pm e_1,\dots,\pm e_4,\pm u/(4-s)\}$.
  With $p=u/(4-s)=(a,a,a,a)$, $a=1/(4-s)$, facet values of the
  cross-polytope at $p$ are $a\sum\varepsilon_i$: only $++++$ gives
  $4a>1$, all others give $\le 2a\le 4/7<1$. By the one-visible-facet
  lemma the hull adds exactly two disjoint pyramids over
  $F=\mathrm{conv}\{e_1,\dots,e_4\}$. Base 3-volume: edge Gram
  $I+J_3$ has determinant 4, so $\mathrm{vol}_3(F)=\sqrt{4}/6=1/3$.
  Height $|4a-1|/|u|=s/(2(4-s))$ ($|u|=2$); each pyramid has volume
  $(1/4)(1/3)h=s/(24(4-s))$. Vertex extremality of all 10 points by exact
  separating functionals.
- Deficit: multiplying out gives $D(s)$; leading term
  $4s/(3(4-s))=s/3+O(s^2)$. Uniform lower bound: $4s/(3(4-s))\ge s/3$ and
  the negative terms are $\le s(1/144+1/8064)$ for $s\le 1/2$, giving
  $D(s)\ge s(1/3-57/8064)=2631s/8064\ge s/4$.
- No cubic envelope: $D(s)\ge 2631s/8064$ vs $P(B)Cs^3=(32/3)Cs^3$ gives
  violation for $0<s^2<2631/(86016C)$, nonempty for every $C$; exact
  `Fraction` evaluations witness $C=2$ at $1/1000,1/100,1/10$, plus an
  analytic interval version on $(0,1/10]$.
- Reversal: $(1-s/4)B\subset K_s$ since $\sum|(1-s/4)x_i|\le 4-s$ on $B$;
  with $-\ln(1-x)\le x+x^2$ on $[0,1/4]$,
  $\delta(s)\le s(4+s)/16\le 9s/32$. Since $2631/8064>9/32$,
  $D(s)\ge\delta(s)$ on $(0,1/2]$, so $D/\delta^2\to+\infty$.

## Limitations

- Proved: exact product formula, linear deficit rate $D(s)\sim s/3$,
  impossibility of any cubic upper envelope, and the reversal.
- Not proved: the target's $\delta(s)\ge s/8$ lower bound (best certified
  here is $\delta\ge s/140$ at nodes via Mahler monotonicity; unnecessary
  for the conclusion). No claim about any other Mahler family, $n\ne 4$,
  or global (non-path) stability.
- The preset 1D fallback inequality
  $J(f)\ge 4(1+\tfrac18\min(1,(m(f)-1/3)^2))$ is **false**:
  $f(x)=e^{-|x|}$ is admissible with $J(f)=4<9/2=\mathrm{RHS}$; reported
  only to document why the fallback route was abandoned.

## Reproducibility

Stdlib-only, exact-`Fraction` scripts:

    python3 output/artifacts/verify_target.py
      -> VERIFY_OK (cubic falsified at 1/1000, 1/100, 1/10) + analytic
         interval blocks + exact determinant cross-checks + delta band.
    python3 output/artifacts/verify_fallback_counterexample.py
      -> FALLBACK_REFUTED (margin 1/2).

## References

- F. Nazarov, F. Petrov, D. Ryabogin, A. Zvavitch, A remark on the Mahler
  conjecture: local minimality of the unit cube. arXiv:0905.0867.
- J. Kim, Minimal volume product near Hanner polytopes. arXiv:1212.2544.
- J. Kim, A. Zvavitch, Stability of the reverse Blaschke–Santalo
  inequality for unconditional convex bodies. arXiv:1302.5719.
- F. Barthe, K. J. Böröczky, M. Fradelizi, Stability of the functional
  forms of the Blaschke–Santalo inequality. arXiv:1206.0369.
- M. Fradelizi, E. Nakhle, On Mahler's conjecture for even s-concave
  functions in dimensions 1 and 2. arXiv:2412.12372.
