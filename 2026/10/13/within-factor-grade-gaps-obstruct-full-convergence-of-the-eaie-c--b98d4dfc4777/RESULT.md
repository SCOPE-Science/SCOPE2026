# Within-factor grade gaps obstruct full convergence of the EAIE correction dynamics
## Finding
For the correction dynamics of Liao (2025), fix a finite factor set \(F\) with \(n=|F|\ge 2\), maximal grades \(d_m\ge 1\), and a multichoice characteristic mapping \(H\). Definition 4.2 updates every positive-grade coordinate of a fixed factor by the same correction:
\[
x^{q+1}_{{m,k}}=x^q_{{m,k}}+\alpha\Delta_m(x^q),
\]
where \(\Delta_m\) depends on the top-grade excesses but not on \(k\). Therefore, for every \(1\le k\le d_m\),
\[
x^q_{{m,k}}-x^q_{{m,d_m}}=x^0_{{m,k}}-x^0_{{m,d_m}}
\]
for all \(q\).

For \(0<\alpha<2/n\), Theorem 4.4 correctly gives convergence of each top-grade coordinate to \(\Psi_{{m,d_m}}\). The invariant then gives the exact full-coordinate limit
\[
x^q_{{m,k}}\longrightarrow \Psi_{{m,d_m}}+x^0_{{m,k}}-x^0_{{m,d_m}}.
\]
Consequently the whole vector converges to the EAIE \(\Psi\) if and only if
\[
x^0_{{m,k}}-x^0_{{m,d_m}}=\Psi_{{m,k}}-\Psi_{{m,d_m}}
\]
for every factor and positive grade.

The plurality-completeness condition PCOMR used in Theorem 4.5 does not imply these identities. Indeed, PCOMR implies only
\[
x^0_{{m,k}}-x^0_{{m,d_m}}=H(d_{{-m}},k)-H(d),
\]
so Theorem 4.5 requires the additional compatibility condition
\[
H(d_{{-m}},k)-H(d)=\Psi_{{m,k}}-\Psi_{{m,d_m}}
\]
for every \(m,k\). Without it, the published full-vector convergence claim fails.

A smallest explicit witness has two factors with maximal grades \((d_1,d_2)=(2,1)\). Set
\[
H(0,0)=H(1,0)=H(2,0)=H(0,1)=H(2,1)=0,
\qquad H(1,1)=1.
\]
For the payoff vector
\[
(x_{{1,1}},x_{{1,2}},x_{{2,1}})=(1,0,0),
\]
all PCOMR equations hold. The separate effects and grand value are all zero, hence \(\Psi=(0,0,0)\). Both top-grade excesses are zero, so every correction in Definition 4.2 vanishes for every admissible \(\alpha\). Thus \(x^q=(1,0,0)\) for every \(q\), not \(\Psi\). In particular, the published stopping rule based on \(\lVert x^{{q+1}}-x^q\rVert\) stops immediately at a non-EAIE fixed point.

## Assumptions and scope
A multichoice situation is used exactly as in the source: \(H\) is an arbitrary real-valued characteristic mapping on the finite grade grid with \(H(0)=0\). No monotonicity, convexity, superadditivity, or positivity of \(H\) is assumed in the source, and none is needed here. The explicit witness is therefore admissible. The result concerns the full-vector statement in Theorem 4.5 and the associated iteration; it does not dispute Theorem 4.4, which concerns only top-grade coordinates.

The classification above is valid for every initial vector in the source set \(X(F,H)\) and every \(0<\alpha<2/n\). For an initial vector satisfying PCOMR, the displayed compatibility identities are necessary and sufficient for convergence to the complete EAIE vector.

## Proof
Definition 4.2 has the form
\[
g_{{m,k}}(x)=x_{{m,k}}+\alpha\sum_{{r\ne m}}\bigl(e_m(x)-e_r(x)\bigr),
\]
where \(e_m(x)\) denotes the source's excess at the single-factor top-grade vector \((d_m,0_{{-m}})\). The sum on the right contains no occurrence of \(k\). Hence, for any two positive grades \(k,\ell\) of the same factor,
\[
g_{{m,k}}(x)-g_{{m,\ell}}(x)=x_{{m,k}}-x_{{m,\ell}}.
\]
Iteration proves the grade-gap invariant.

Theorem 4.4 establishes, under \(0<\alpha<2/n\),
\[
x^q_{{m,d_m}}\to\Psi_{{m,d_m}}.
\]
Adding the invariant difference \(x^0_{{m,k}}-x^0_{{m,d_m}}\) gives the exact limit of every lower-grade coordinate. Equality of this limit with \(\Psi_{{m,k}}\) is equivalent to the stated offset condition.

Now assume PCOMR. Its equation for grade \(k\) of factor \(m\) is
\[
x^0_{{m,k}}+\sum_{{r\ne m}}x^0_{{r,d_r}}=H(d_{{-m}},k).
\]
The same equation at \(k=d_m\) is
\[
x^0_{{m,d_m}}+\sum_{{r\ne m}}x^0_{{r,d_r}}=H(d).
\]
Subtracting gives
\[
x^0_{{m,k}}-x^0_{{m,d_m}}=H(d_{{-m}},k)-H(d).
\]
Substitution into the general offset condition proves the PCOMR compatibility criterion.

For the explicit witness, the EAIE step effects are
\[
H(1,0)-H(0,0)=0,\qquad H(2,0)-H(1,0)=0,\qquad H(0,1)-H(0,0)=0,
\]
and \(H(2,1)=0\), so the EAIE balance term and all three EAIE coordinates are zero. PCOMR is checked by
\[
1+0=H(1,1),\qquad 0+0=H(2,1),\qquad 0+0=H(2,1).
\]
The two top-grade excesses equal zero, so the common correction for each factor is zero. The initial vector is therefore a fixed point distinct from the EAIE, disproving Theorem 4.5 as stated.

## Verification
The standalone `verify.py` reconstructs the source definitions with exact rational arithmetic. It verifies the PCOMR equations for the two-factor witness, computes the EAIE exactly, evaluates the top-grade excesses, checks that the iteration is stationary for several admissible learning rates, and independently checks the within-factor grade-gap invariant on a nonstationary rational example.

Run

```text
python verify.py
```

and require the output `VERIFY_OK`. No floating-point arithmetic is used.

## Relationship to prior work
Liao (2025), DOI 10.3934/math.2025671, defines the correction map in Definition 4.2, proves only top-grade convergence in Theorem 4.4, and then states in Theorem 4.5 that PCOMR upgrades this to convergence of the entire payoff vector. The proof of Theorem 4.5 is only the sentence that it follows from Theorem 4.4. The invariant above identifies why that implication is invalid.

A separate earlier finding on the same 2025 EAIE concerned its covariant-transformation axiom. That result does not imply the present dynamic obstruction: Theorem 4.5 neither invokes covariance nor follows from the axiomatic characterization, and the present counterexample uses no transformed game. The two defects concern different mathematical mechanisms.

A useful comparison is Hwang, Liao, Chen, and Wang (2021), DOI 10.3390/sym13081474. Their multichoice dynamic update is grade-dependent: the correction for coordinate \((m,k)\) explicitly uses a surfeit indexed by \(k\). Their Theorem 3 therefore obtains a coordinatewise contraction for every grade. That earlier scheme does not cover the 2025 EAIE iteration; rather, it shows that full-coordinate contraction is possible when the update retains grade information that Definition 4.2 discards.

Targeted searches of the source title, DOI, Theorem 4.5, PCOMR, EAIE dynamic convergence, fixed points, and correction-function aliases did not locate a public correction or a statement of the invariant/compatibility criterion. These searches support comparison but are not a proof that no unindexed discussion exists.

## Limitations
The result does not claim that the EAIE itself is unusable, nor that every PCOMR initialization fails. Full convergence does occur precisely when the initial within-factor offsets already match the EAIE offsets; under PCOMR this is the displayed compatibility condition. The top-grade convergence theorem remains untouched.

The source's 2012 duplicate-EANSC paper was located only through bibliographic metadata and an abstract during this run; its full dynamic construction was not inspected. A 2021 open full-text multichoice dynamic paper by overlapping authorship was inspected and provides the closest formula-level comparison found.

The exact public date used for the 2025 source is the publisher's dated record, 30 June 2025. A ResearchGate page labels the article by month as January 2025 but does not provide a verified exact earlier day.

## References
1. Y.-H. Liao, “Integrating axiomatic and dynamic mechanisms under industrial management situations: game-theoretical analysis,” *AIMS Mathematics* 10(6), 14975–14995 (2025). DOI: 10.3934/math.2025671. See Definition 4.2 and Theorems 4.4–4.5.
2. Y.-A. Hwang, Y.-H. Liao, E.-C. Chen, and J.-W. Wang, “Axiomatic and Dynamic Processes for a Symmetric Allocation Rule,” *Symmetry* 13, 1474 (2021). DOI: 10.3390/sym13081474. See the symmetric revising function and Theorem 3.
