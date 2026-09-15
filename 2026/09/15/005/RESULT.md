# Sharp wall-crossing irreducibility for coherent continuation of standard Harish-Chandra modules of SL(n,R) at a minimal singular wall

## Context

Let $(G_0,K_0)=(SL(n,\mathbf{R}),SO(n))$, $n \ge 3$, with complexified pair
$(\mathfrak{g},K)=(\mathfrak{sl}(n,\mathbf{C}),SO(n,\mathbf{C}))$.
Let $X=G/B$ be the full flag variety. Translation of Harish-Chandra modules
to a singular infinitesimal character is a classical but delicate operation:
at singular parameters Beilinson-Bernstein global sections need not be exact
in general, reducible standard sheaves can have irreducible global sections,
and vanishing is controlled by the Hecht-Milicic-Schmid-Wolf (HMSW) criterion.
This record gives a necessary and sufficient wall-crossing trichotomy at a
minimal singular wall in terms of explicit orbit geometry, SL(2) parity, and
HMSW survival data.

## Definitions

- $\lambda \in \mathfrak{h}^*$ regular antidominant; $\lambda_0$ antidominant in the
  closure of the chamber of $\lambda$ with integral singular root set
  $\Sigma_{\lambda_0}=\{\pm\alpha\}$ for a single simple root $\alpha$
  (minimal wall). Integrality hypothesis: $\lambda-\lambda_0$ lies in the
  $G$-weight lattice, so a finite-dimensional $G$-representation of extremal
  weight $\lambda_0-\lambda$ exists and the Jantzen-Zuckerman translation
  functor $T_\lambda^{\lambda_0}$ is defined.
- $P_\alpha$ the corresponding parabolic, $X_\alpha=G/P_\alpha$ the minimal
  partial flag variety, $\pi_\alpha:X \to X_\alpha$ the $\mathbf{P}^1$-bundle
  projection.
- $Q \subset X$ a $K$-orbit, $\tau$ an irreducible $K$-homogeneous connection
  on $Q$ compatible with $\lambda+\rho$ such that $\mathcal{I}(Q,\tau)$
  satisfies Milicic's irreducibility criterion at $\lambda$
  (so $\mathcal{I}(Q,\tau)=\mathcal{L}(Q,\tau)$).
- $\Phi$ the coherent continuation family with
  $\Phi(\lambda)=\Gamma(X,\mathcal{I}(Q,\tau))$; hence
  $\Phi(\lambda_0)=T_\lambda^{\lambda_0}\Phi(\lambda)$.
- Orbit datum: $Q_\alpha=\pi_\alpha(Q)$, saturation
  $S=\pi_\alpha^{-1}(Q_\alpha)$ (1, 2, or 3 $K$-orbits), Vogan root type of
  $\alpha$ relative to $Q$, SL(2)-parity of $\tau$ at $\alpha$ (trivial vs
  nontrivial fiber monodromy), and HMSW nonvanishing data of the transported
  data $(Q'_\alpha,\sigma)$ on $X_\alpha$ at $\lambda_0$.

## Result

With the hypotheses above, $\Phi(\lambda_0)$ is exactly one of
{irreducible nonzero, reducible, zero}, determined as follows
(parity branches are conditional on existence of a Milicic-compatible
$\tau$ of that parity):

- (S) $S=Q$ saturated (compact imaginary, fiber $\mathbf{P}^1$):
  $\Phi(\lambda_0)=\Gamma(X_\alpha,\mathcal{I}(Q_\alpha,\sigma))$;
  irreducible nonzero iff HMSW nonzero, else zero; never reducible.
- (C$^-$) $S=\{Q,Q'\}$, $Q$ closed (fiber a point):
  same irreducible-or-zero conclusion; never reducible.
- (C$^+$) $S=\{Q,Q'\}$, $Q$ open (fiber $\mathbf{A}^1$):
  nontrivial parity gives the clean intermediate extension, hence
  irreducible-or-zero; trivial parity gives a two-step-filtered object with
  subquotients the HMSW-surviving factors (length 2 iff both survive, the
  surviving simple iff exactly one survives, zero iff none).
- (N) triple with $Q$ closed (noncompact imaginary type I, fiber a point):
  irreducible-or-zero by the single transported closed HMSW datum.
- (R) triple with $Q$ open (real, fiber $\mathbf{C}^*$):
  nontrivial parity gives $\Phi(\lambda_0)=0$ identically;
  trivial parity gives the analogous filtered trichotomy by count of
  surviving HMSW data (open plus two closed).
- Singular-localization preimage: with
  $\Delta_{\lambda_0} \dashv \Gamma_{\lambda_0}$ on $X_\alpha$,
  $\Delta_{\lambda_0}\Phi(\lambda_0)$ is the HMSW-surviving
  quotient/image of $\pi_{\alpha+}\mathcal{I}(Q,\tau)$ (kernel exactly the
  HMSW-vanishing factors), not the identity in general.

Reducibility statements are filtered composition-factor counts; no claim is
made that any nonsplit extension class survives $\Gamma$.

## Proof / evidence

Lemma 1 (translation = pushforward + sections, needs integrality, cited
Jantzen-Zuckerman/Beilinson-Bernstein): under the integrality hypothesis,
$T_\lambda^{\lambda_0}\Gamma(X,\mathcal{F}) \cong
\Gamma(X_\alpha,\pi_{\alpha+}\mathcal{F})$, with exact $\Gamma$ at
antidominant $\lambda_0$. Lemma 2 (saturation/fiber table): the five-row
$1$/$2$/$3$-orbit classification with fibers
$\mathbf{P}^1$/point/$\mathbf{A}^1$/point/$\mathbf{C}^*$, verified
geometrically by a signed-involution census for $n=3$ (7 SO-orbits, 14
orbit-root pairs, all five fiber types realized). Lemma 3 plus Remark 1
(SL(2)-parity pushforward): point and $\mathbf{P}^1$ fibers are clean;
$\mathbf{A}^1$ gives clean vs length-2 by parity via a cited
attaching-triangle local-cohomology $\mathrm{Ext}^1=\mathbf{C}$ computation
(Hotta-Takeuchi-Tanisaki; Borel et al.; BBD); $\mathbf{C}^*$ gives total
vanishing vs a two-degree object by Euler-characteristic/monodromy reasons.
Lemmas 4-5 (HMSW criterion; singular-antidominant preservation/filtration:
exact $\Gamma$, simples with nonzero sections go to simples, length-2
filtration counts, counit quotient/image — all cited, not re-proved) convert
pushforward data into the stated irreducible/reducible/zero outcomes row by
row. Parity branches are stated conditionally; both parities exist
topologically and are simultaneously Milicic-compatible at generic
$\lambda$, with case-by-case checking at special $\lambda$.

## Limitations

Assumes regular antidominant $\lambda$ with Milicic irreducibility at
$\lambda$, integral $\lambda-\lambda_0$, minimal single-root wall, split
pair $(SL(n,\mathbf{R}),SO(n))$ with $n \ge 3$. HMSW nonvanishing and
singular Beilinson-Bernstein exactness/quotient descriptions are invoked as
cited criteria. C$^+$/R reducibility is a filtered count only. Parity
branches are conditional as stated. Multi-wall crossings and
non-antidominant parameters are outside scope.

## Reproducibility

The geometric census script enumerates signed involutions for $n=3$ and
checks every fiber type occurs; it was re-executed during audit. The fiber
model script records Euler characteristics and Betti ranks as illustration
only and is not used as proof of any extension class. Cited textbook and
paper results (Beilinson-Bernstein, Jantzen, HMSW, Hotta-Takeuchi-Tanisaki,
Borel et al.) supply the D-module machinery.

## References

Beilinson-Bernstein localization (including singular/antidominant forms);
Jantzen-Zuckerman translation functors; Milicic irreducibility criterion
and intertwining-functor paper; Vogan K-orbit/root-type combinatorics;
Hecht-Milicic-Schmid-Wolf vanishing; singular localization adjunction;
Hotta-Takeuchi-Tanisaki and Borel et al. for D-module pushforward;
Beilinson-Bernstein-Deligne for perverse Ext.
