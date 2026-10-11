# Exact dead-end cone for the two-break induction counterexample
## Finding
For the rotational interval-exchange scheme
\[
\sigma=\{(\omega_1\mathrm b,\alpha\mathrm e),(\beta\mathrm b,\alpha\mathrm b,\omega_2\mathrm b,\omega_1\mathrm e,\beta\mathrm e,\omega_2\mathrm e)\},
\]
consider positive *linear* interval rearrangement ensembles, with interval lengths \(v_\alpha,v_\beta,v_{\omega_1},v_{\omega_2}>0\). The admissibility equations force \(v_\alpha=v_{\omega_1}\).

For this scheme the source identifies exactly two elementary induction steps that are not prohibited by its commuting-collection constraints: \(\Pi^{\mathrm{lb}}_{\beta\omega_2}\) and \(\Pi^{\mathrm{rb}}_{\omega_2\omega_1}\). The complete dead-end locus for these permitted moves is
\[
v_\beta\le v_{\omega_2}\le v_{\omega_1}.
\]
Equivalently, at least one permitted elementary step is applicable exactly outside that closed cone. Hence
\[
v_\beta<v_{\omega_2}<v_{\omega_1}
\]
is an open, full-dimensional dead-end region relative to the admissible positive length cone. The source's numerical choice \(v_{\omega_1}=3\), \(v_{\omega_2}=2\), \(v_\alpha=3\), \(v_\beta=1\) lies strictly inside this region.

## Assumptions and scope
The statement concerns the linear IRE attached to the displayed scheme and the source's own notion of permitted versus prohibited elementary induction steps for the corresponding commuting-collection construction. All four lengths are positive. No assertion is made for a different scheme, for a nonlinear IRE after perturbation, or for an enlarged induction algorithm that introduces moves other than the source's elementary steps.

The source defines an allowed endpoint vector by
\[
v_\xi=x_{\sigma(\xi\mathrm b)}-x_{\xi\mathrm b}
      =x_{\xi\mathrm e}-x_{\sigma(\xi\mathrm e)}.
\]
For the displayed scheme, the first two-cycle immediately gives \(v_\alpha=v_{\omega_1}\).

## Proof
For the left-beginning move \(\Pi^{\mathrm{lb}}_{\beta\omega_2}\), the source's applicability inequality is
\[
x_{\omega_2\mathrm e}<x_{\sigma(\beta\mathrm b)}=x_{\alpha\mathrm b}.
\]
The endpoint equations for this scheme give
\[
v_\beta=x_{\alpha\mathrm b}-x_{\beta\mathrm b},
\qquad
v_{\omega_2}=x_{\omega_2\mathrm e}-x_{\beta\mathrm b}.
\]
Subtracting the common endpoint therefore shows that the move is applicable exactly when
\[
v_\beta>v_{\omega_2}.
\]

For the right-beginning move \(\Pi^{\mathrm{rb}}_{\omega_2\omega_1}\), applicability is
\[
x_{\omega_2\mathrm b}<x_{\sigma(\omega_1\mathrm e)}=x_{\beta\mathrm e}.
\]
The endpoint equations give
\[
v_{\omega_2}=x_{\omega_1\mathrm e}-x_{\omega_2\mathrm b},
\qquad
v_{\omega_1}=x_{\omega_1\mathrm e}-x_{\beta\mathrm e},
\]
so this move is applicable exactly when
\[
v_{\omega_2}>v_{\omega_1}.
\]

The source states that these are the only non-prohibited elementary steps for this scheme. Thus no permitted step is applicable precisely when both strict applicability inequalities fail, namely
\[
v_\beta\le v_{\omega_2}\le v_{\omega_1}.
\]
The strict subcone has nonempty relative interior in the positive length space subject only to \(v_\alpha=v_{\omega_1}\), proving robustness under sufficiently small admissible linear perturbations.

## Verification
The two applicability tests were reconstructed directly from the source definitions and reduced symbolically to the length differences \(v_\beta-v_{\omega_2}\) and \(v_{\omega_2}-v_{\omega_1}\). Equality is correctly included in the dead-end boundary because the source's applicability conditions are strict inequalities. No finite enumeration is used to infer the universal statement.

The first public version of the motivating source is dated 2026-09-30 and lists MSC 37E05 first, followed by 37E10.

## Relationship to prior work
Teplinsky's *Interval Rearrangement Ensembles* introduces the IRE formalism, Rauzy--Veech-type elementary induction, and duality. *Rotational Interval Exchange Transformations* characterizes rotational IETs in that formalism. The 2026 source extends the machinery to commuting collections with multiple breaks and, for the displayed scheme, exhibits the single numerical dead-end vector \(3,2,3,1\) while observing that small perturbations can produce nonlinear examples.

The present statement is the exact linear length-space classification for that displayed counterexample scheme: it identifies both applicable half-spaces and their complete common failure cone. Searches for the exact source, the scheme, the two move names, dead-end or blocked induction, rotational IRE aliases, and broader Rauzy--Veech obstruction language found no published statement implying this if-and-only-if cone.

## Limitations
The result is local to one scheme and to the elementary moves declared non-prohibited in the motivating construction. It does not prove that every nonlinear perturbation remains trapped, does not classify dead ends for all multiple-break rotational schemes, and does not rule out a future enlarged induction procedure that escapes this cone. An equivalent derivation could exist in unindexed notes or under different induction terminology.

## References
1. A. Teplinsky, *Linear-fractional rotational interval exchange transformations*, arXiv:2609.40261v1, 2026.
2. A. Teplinsky, *Interval Rearrangement Ensembles*, arXiv:2010.16389, 2020; later journal version.
3. A. Teplinsky, *Rotational Interval Exchange Transformations*, arXiv:2404.11211, 2024.
