# Disproof of the cross-polytope versus box masking acceptance–Rényi tradeoff (TARGET resolution)

## Context

Fiat–Shamir with aborts (Lyubashevsky) uses rejection (abort) sampling to remove
secret dependence from transcripts. At Dilithium scales the standard choice is
uniform box (hypercube) masking. A natural candidate alternative is uniform
masking over the equal-volume $\ell^1$-ball (cross-polytope), calibrated so that
both masking bodies have identical volume. The admitted target claim asserted
that, at Dilithium scales, the equal-volume cross-polytope simultaneously
achieves (A) acceptance rate at least $1.5\times$ the box acceptance rate and
(B) order-$\alpha=2$ Rényi divergence between accepted and ideal transcripts no
larger than the box variant's, uniformly over secret shifts of
$\ell^\infty$-norm at most $\beta$.

## Definitions (canonical abort model)

Fix a masking body $S \subset \mathbb{R}^N$ of finite positive volume and a
secret shift $v$. Draw $y \sim U(S)$; accept iff $y+v \in S$; on acceptance
output $z=y+v$. Then:

- Acceptance rate: $\delta = |S \cap (S+v)| / |S|$.
- Accepted law: $P = U(T)$ with $T := S \cap (S+v)$.
- Ideal transcript law: $Q = U(S)$.

Write $N = 256\,l$. Box: $S_{\mathrm{box}} = [-\gamma_1,\gamma_1]^N$.
Cross-polytope: $C = \{y : \|y\|_1 \le R\}$.
Single-spike shift: $v = \beta e_1$, so $\|v\|_\infty = \beta$.

## Result

**The tradeoff claim is FALSE.** A single in-scope instance violates both
inequalities. Take $l=4$ ($N=1024$), $\gamma_1 = 2^{17} = 131072$,
$\beta = 240 = 60 \cdot 4$ ($\tau=60$, $\eta=4$),
$R = \gamma_1 (N!)^{1/N}$, $\alpha = 2$, $v = 240\,e_1$:

- $\delta_{\mathrm{box}} = 16369/16384 \approx 0.99908447$,
  $R_2^{\mathrm{box}} \approx 0.00091595$;
- $\delta_{\mathrm{cross}} \approx 0.99752504$,
  $R_2^{\mathrm{cross}} \approx 0.00247803$;
- acceptance ratio
  $\delta_{\mathrm{cross}}/\delta_{\mathrm{box}} \approx 0.99844 < 1.5$,
  so (A) fails;
- $R_2^{\mathrm{cross}} / R_2^{\mathrm{box}} \approx 2.71 > 1$,
  so (B) fails (reversed).

## Proof / evidence

**Lemma (divergence = negative log acceptance).** For $P = U(T)$, $Q = U(S)$
with $T \subseteq S$, $|T| > 0$,
$R_\alpha(P \| Q) = -\log \delta$ for every Rényi order
$\alpha \in (0,1) \cup (1,\infty)$ (and also KL), where
$\delta = |T|/|S|$. Proof: $p/q = (|S|/|T|)\mathbf{1}_T$, so
$\int p^\alpha q^{1-\alpha} = (|S|/|T|)^{\alpha-1}$; dividing the log by
$\alpha-1$ gives $\log(|S|/|T|) = -\log\delta$.

Hence for both schemes the divergence comparison is exactly the reversed
acceptance comparison.

**Volumes and calibration.** $|C| = (2R)^N/N!$ by induction via
$V_N(R) = \int_{-R}^{R} V_{N-1}(R-|t|)\,dt$ with $V_1(R) = 2R$.
Equal-volume calibration $|C| = |S_{\mathrm{box}}|$ gives
$(2R)^N/N! = (2\gamma_1)^N$, i.e. $R = \gamma_1 (N!)^{1/N}$.

**Box acceptance (single spike).** Only coordinate 1 changes:
$[-\gamma_1,\gamma_1] \cap [-\gamma_1+\beta,\gamma_1+\beta]
= [-\gamma_1+\beta,\gamma_1]$ of length $2\gamma_1-\beta$. Exactly:
$\delta_{\mathrm{box}} = 1 - \beta/(2\gamma_1) =: 1-x$,
$R_2^{\mathrm{box}} = -\log(1-x)$.

**Cross-polytope acceptance (single spike).** For fixed $z_1$ the remaining
coordinates form an $\ell^1$-ball of radius
$R - \max(|z_1|,|z_1-\beta|)$. With $u = z_1 - \beta/2$ and symmetry,
$|T_{\mathrm{cross}}| = 2^N (R-\beta/2)^N / N!$ (valid since $R > \beta/2$).
Exactly: $\delta_{\mathrm{cross}} = (1-\beta/(2R))^N =: (1-u)^N$,
$R_2^{\mathrm{cross}} = -N\log(1-u)$.

**Refutation of (A).** Since $0 < u < 1$, $\delta_{\mathrm{cross}} < 1$, so
$\delta_{\mathrm{cross}}/\delta_{\mathrm{box}} < 1/(1-x)
= 16384/16369 < 1.00092 < 1.5$ (as $16384\cdot 2 < 3\cdot 16369$).

**Refutation of (B).** Using $-\log(1-t) \ge t$ and
$-\log(1-x) \le x/(1-x)$,
$R_2^{\mathrm{cross}}/R_2^{\mathrm{box}} \ge N(1-x)/M$ with
$M := (N!)^{1/N}$ (since $u = x/M$). AM–GM pairing gives
$M \le (N+1)/2 = 512.5$ for even $N$, so the ratio is at least
$2N(1-x)/(N+1) = (2048/1025)(16369/16384) > 1.99 > 1$.

**Certified numerics.** `output/artifacts/refutation.py` certifies
$M = (1024!)^{1/1024} \in [378.325067766, 378.325067769]$ via Robbins'
two-sided Stirling remainder against the exact-sum $\log(1024!)$ and computes
the values above; an independent 200,000-draw $\ell^1$-ball Monte Carlo gives
$\hat\delta_{\mathrm{cross}} = 0.99766 \pm 0.00011$, agreeing with the exact
$0.997525$ within $\sim 1$ s.e.

**Mechanism.** The reversal is structural: $R_2 = -\log\delta$ for both
schemes; the cross-polytope overlap $(1-\beta/2R)^N$ decays with the full
dimension $N$ while the box single-spike overlap pays only in one coordinate;
equal-volume calibration forces $R/\gamma_1 = (N!)^{1/N} \approx N/e$.

## Limitations

The refutation applies to the canonical abort-sampling model (uniform mask,
accept iff the shifted value stays in the body; accepted-versus-uniform-ideal
Rényi divergence) and the equal-box-volume radius calibration. It does not rule
out reformulated claims using norm-check acceptance, non-uniform masking,
different divergence accounting, or differently scaled radii.

## Reproducibility

Run `python3 output/artifacts/refutation.py` (requires only Python standard
library). It asserts the Robbins bracket, prints the certified $M$ interval,
acceptance/divergence values, the ratio upper bound, and the Monte Carlo
cross-check. The analytic refutations in sections above require no numerics.

## References

- V. Lyubashevsky, Fiat-Shamir with aborts: applications to lattice and
  factoring-based signatures, ASIACRYPT 2009.
- L. Ducas et al., CRYSTALS-Dilithium: a lattice-based digital signature
  scheme, TCHES 2018 / eprint 2017/633.
- J. Devevey, P. Fallahpour, A. Passelègue, D. Stehlé, A detailed analysis of
  Fiat-Shamir with aborts, CRYPTO 2023 / eprint 2023/245.
- H. Bambury, H. Beguinet, T. Ricosset, E. Sageloli, Polytopes in the
  Fiat-Shamir with aborts paradigm, CRYPTO 2024 / eprint 2024/411.
- J. Devevey, Lattice-based signature schemes in the Fiat-Shamir paradigm
  (PhD thesis).
