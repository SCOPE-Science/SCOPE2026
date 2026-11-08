# A connected separated counterexample to three-tap cyclic STFT phase retrieval

## Finding

For each integer \(m\ge2\), set \(d=3m\) and let the length-three flat window be \(g_j=1\) for \(j\in\{0,1,2\}\subset\mathbb Z_d\), and \(g_j=0\) otherwise. For any real \(0<a<b\), define two \(d\)-periodic signals \(f,h\) by
\[
(f_{3k},f_{3k+1},f_{3k+2})=(a,b,0),\qquad
(h_{3k},h_{3k+1},h_{3k+2})=(b,a,0).
\]
Both signals have a cyclically \(2\)-connected support and each has a zero (hence is \(1\)-separated). They are not related by global phase, yet
\[
|V_g f(t,\ell)|^2=|V_g h(t,\ell)|^2
\quad\text{for all }(t,\ell)\in\mathbb Z_d^2.
\]
Thus \(2\)-connectivity together with \(\lceil 2/2\rceil\)-separation does not guarantee cyclic STFT phase retrieval for all short windows. In particular, the unrestricted connectedness equivalence asserted in the statement of Theorem 7.2.12(b) of Bartusel's 2024 dissertation has this explicit counterexample; the two-per-block support also lies outside the special one-per-block exception stated in its part (a).

More precisely, in the restricted complex family of all \(3\)-periodic signals with blocks \((A,B,0)\), where \(AB\ne0\), the intensity fiber modulo a common unit phase has exactly two elements if \(|A|\ne|B|\), and one element if \(|A|=|B|\). This is a restricted-family fiber statement, **not** a claim about the complete fiber among all vectors in \(\mathbb C^d\).

## Assumptions and scope

We use the discrete STFT convention
\[
 V_g u(t,\ell)=\sum_{j=0}^{d-1}u_j\,\overline{g_{j-t}}\,
 e^{-2\pi i\ell j/d},\qquad t,\ell\in\mathbb Z_d,
\]
with every subscript modulo \(d\). A signal is \(1\)-separated when it has at least one zero coordinate. A support is cyclically \(2\)-connected when it is connected in the graph joining occupied coordinates at circular distance at most two. The window has support exactly three consecutive sites, so its span parameter is \(L=2<d/2\). The strict inequalities \(m\ge2\) and \(0<a<b\) are assumed for the concrete counterexample. The complex-fiber assertion assumes \(A,B\ne0\).

## Proof

Write \(\zeta=e^{-2\pi i\ell/d}\). If \(u\) repeats the block \((A,B,0)\), then, after removing the harmless unit factor \(\zeta^t\), the three possible short-window Fourier sums, as \(t\) runs through residues modulo \(3\), are
\[
 A+B\zeta,\qquad B+A\zeta^2,\qquad
 \zeta(A+B\zeta).
\]
Thus the complete spectrogram is determined by the two real/complex invariants
\[
 S=|A|^2+|B|^2,\qquad P=A\overline B,
\]
since the squared magnitudes of these sums are respectively
\[
 S+P\overline\zeta+\overline P\zeta,\qquad
 S+\overline P\,\overline\zeta^2+P\zeta^2,\qquad
 S+P\overline\zeta+\overline P\zeta.
\]
Because \(d\ge6\), the full set of sampled frequencies uniquely determines \(S\) and \(P\) by discrete Fourier orthogonality in the first of these rows. Conversely equality of \(S,P\) plainly implies equality of all spectrogram entries.

For the positive real blocks \((a,b,0)\) and \((b,a,0)\), both invariants are \(S=a^2+b^2\) and \(P=ab\). Therefore their complete spectrograms coincide. Their entries have unequal positive magnitudes in the same indexed positions, so no unit scalar transforms one vector into the other.

The nonzero support consists of residues congruent to \(0\) or \(1\) modulo \(3\). The consecutive circular gaps between occupied positions alternate between lengths one and two. Hence the occupied-site graph with edge threshold \(L=2\) is connected; every third site vanishes, giving a one-consecutive-zero gap. All the stated separation and connectivity hypotheses hold.

For the restricted complex-fiber classification, any competing block \((C,D,0)\) with the same intensities must have \(|C|^2+|D|^2=S\) and \(C\overline D=P\). Thus the two positive numbers \(|C|^2,|D|^2\) are the roots of
\[
 X^2-SX+|P|^2=0.
\]
For each ordered choice of roots, fixing the common phase so that \(C>0\) yields the unique representative \(C=\sqrt X\) and \(D=\overline P/\sqrt X\). Distinct roots give exactly two phase classes, while a double root gives one. This proves the fiber assertion without an exhaustive search.

## Verification

The standalone Python 3 program `VERIFY.py` verifies, with exact rational arithmetic and exact aperiodic autocorrelation coefficients, the spectrogram identity for the concrete positive-rational blocks \((2,3,0)\), \((3,2,0)\) and the dimensions \(6,9,12,15,18,21\), all translation classes and Fourier powers. It separately checks the support graph. The arbitrary-dimension theorem and the complex two-fiber classification follow from the displayed analytic identities, not from finite testing.

## Relationship to prior work

Bartusel's June 2022 preprint, later published in August 2023, establishes connected-component phase retrieval for sufficiently separated signals and explicitly proposes extending the equivalence to \(L/2\)-separated signals (2023, end of Section 4). Its Example 4.2.3 treats one occupied residue class per periodic block and does not cover the present connected two-occupied-sites-per-three-block obstruction. Theorem 7.2.12 in his 2024 dissertation formulates a general half-window-separated connectedness characterization; the present pair satisfies its stated conditions but contradicts its part (b), and does not match the exceptional one-occupied-site support in its part (a). This comparison concerns precisely the mathematical statements, without asserting an explanation for the source argument.

Related cyclic STFT phase-retrieval results for nonvanishing signals or two-tap windows rely on conditions not satisfied here. No claim is made that the counterexample defeats stronger recovery hypotheses such as a nonvanishing ambiguity function, or that this is the only type of exceptional periodic pattern.

## Limitations

The counterexample uses a flat three-site window and dimensions divisible by three. The exact two-element fiber theorem is **only** within the \(3\)-periodic family with support pattern \((A,B,0)\), not among arbitrary signals. No statement is made about other windows, dimensions not divisible by three, stability, or the complete ambiguity class. A further specialized historical source containing an equivalent connected periodic counterexample cannot be definitively excluded.

## References

- D. Bartusel, *Injectivity conditions for STFT phase retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)*, arXiv:2206.06729v1, first posted 2022-06-14; *Journal of Fourier Analysis and Applications* 29, article 53 (2023), DOI 10.1007/s00041-023-10026-2; especially Example 4.2.3 and the concluding conjecture in Section 4.
- D. Bartusel, *The role of connectedness in phase retrieval*, dissertation, RWTH Aachen University (2024), DOI 10.18154/RWTH-2024-03402, Theorem 7.2.12 and Appendix A.1; public PDF record 983400.
