# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.**

The argument was checked against the model and normalization in Wang,
arXiv:2609.20491. For \(\nu<1/2\), the reflection matrix in Wang's orthant
representation satisfies
\[
\rho(|I-R|)=\sqrt{|\nu/(1-\nu)|}<1,
\]
so the cited orthant Skorokhod theorem gives a unique continuous candidate.
The second coordinate and the one-dimensional Skorokhod lemma recover
\(V/(1-\nu)=M(W)-x\), exactly as in Wang's proof.

For \(X=W-b\), the martingale part is \(B\), hence
\(\langle X\rangle_t=t\). Tanaka's formula gives
\[
L_t^0(X)/2=K_t+\nu J_t-A_t.
\]
The nonnegative finite-variation process \(F=M(W)-b\) satisfies
\(\mathbf1_{\{F=0\}}dF=0\); together with support of \(dM\) on
\(\{W=M\}\), this yields
\[
J_t=\int_0^t\mathbf1_{\{X=0,F=0\}}\,db.
\]
The displayed defect identity follows. Its weight on the contact set is either
\(1\) or \(1-\nu\), both strictly positive, so vanishing of the defect as a
signed measure is equivalent to vanishing of the restriction of \(db\), and
hence to zero \(|db|\)-mass, on the contact set.

For locally absolutely continuous \(b\), occupation density makes the contact
set Lebesgue-null and \(d|b|=|b'|dt\), proving the stated corollary. The examples
\(b(t)=ct^\alpha\) were checked: they are locally absolutely continuous for
every \(\alpha>0\), while for \(c>0\) condition (PB) fails at
\(\alpha=1/2\) and for every \(0<\alpha<1/2\).

Boundary cases were stress-tested against known statements. For \(b\equiv0\)
the formula reduces to the classical equality between the regulator and half
the local time. For increasing \(b\), the criterion reduces to Wang's
no-\(db\)-charge condition. Wang's singular counterexample is consistent with
the theorem because its orthant candidate has positive boundary charge on the
contact set.

## Originality

**PASS, to the best of our knowledge.**

Wang's full text was inspected around Theorem 1.1, Proposition 2.5, the
\(\nu<1/2\) orthant argument, and Lemma 6.1. Proposition 2.5 proves
\(\int\mathbf1_{\{X=0\}}|db|=0\) under condition (PB) and then identifies the
regulator with half the local time. Lemma 6.1 proves a necessary no-charge
condition for increasing boundaries. The paper does not state the exact
regulator-local-time defect, the necessary-and-sufficient contact-charge
criterion in the subcritical orthant regime, or the locally absolutely
continuous boundary corollary; a full-text search did not locate the phrase
"absolutely continuous".

Williams (1995) supplies the orthant Skorokhod existence/uniqueness mechanism.
Doney-Zhang (2005) treats perturbed Skorokhod equations and reflected
diffusions with fixed reflection geometry. Burdzy-Kang-Ramanan (2009) develops
Skorokhod maps in time-dependent intervals and studies local-time variation.
These sources establish important ingredients and related moving-boundary
theory, but the inspected statements do not give the maximum-perturbed
boundary-charge identity or the consequence that arbitrary locally absolutely
continuous boundaries are admissible for \(\nu<1/2\).

Searches for combinations of perturbed Brownian motion, moving/time-dependent
boundaries, local time, regulator, contact set, and absolute continuity did not
locate a prior statement matching the theorem. Residual originality risk
remains because general reflected-semimartingale literature may contain an
equivalent regulator/local-time identity in more abstract notation. The claim
is therefore limited to the explicit identity and well-posedness consequence
for Wang's maximum-perturbed moving-boundary model.

## Value

**PASS.**

The result materially changes the regularity picture in the subcritical
parameter range. It shows that the square-root modulus threshold is not the
governing obstruction there: even \(t^\alpha\) boundaries with
\(\alpha<1/2\) are well posed when their variation is absolutely continuous.
At the same time, the exact contact-charge criterion explains why singular
boundaries of the same Hölder order can fail. It also upgrades the increasing
boundary no-charge condition from necessary to necessary and sufficient for
the unique orthant candidate when \(\nu<1/2\).

## Sources inspected

- C. Wang, *Perturbed Brownian motion reflected at a time-dependent boundary*,
  arXiv:2609.20491 (2026), especially Theorem 1.1, Proposition 2.5, the
  subcritical orthant construction, and Lemma 6.1.
- R. J. Williams, *Semimartingale reflecting Brownian motions in the orthant*
  (1995), as the orthant Skorokhod source used by Wang.
- R. A. Doney and T. Zhang, *Perturbed Skorohod equations and perturbed
  reflected diffusion processes* (2005).
- K. Burdzy, W. Kang and K. Ramanan, *The Skorokhod problem in a time-dependent
  interval* (2009).

No inaccessible source was identified whose title or abstract specifically
announces the theorem here. The principal residual risk is broader classical
Skorokhod/local-time literature under different terminology.

## Scientific limitations retained

The theorem is confined to \(\nu<1/2\), gives an implicit criterion for general
singular finite-variation boundaries, and does not provide quantitative
stability estimates or a classification of singular boundaries.
