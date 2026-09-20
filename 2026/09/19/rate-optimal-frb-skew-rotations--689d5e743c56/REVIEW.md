# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

For \(A=\gamma LJ\), \(B=LJ\), scaling by \(h=\lambda L\) reduces FRB and RFB to the characteristic polynomial
\[
(1+i\gamma h)r^2-(1-2ih)r-ih=0.
\]
Its discriminant is exactly
\[
1-4(1+\gamma)h^2.
\]
For \(\gamma>-1\), the two discriminant regimes admit the closed modulus formulas stated in `RESULT.md`. Their monotonicity is elementary after introducing \(u=\sqrt{1-4(1+\gamma)h^2}\) below the coalescence point and the normalized variable
\[
w=\frac{\sqrt{4(1+\gamma)h^2-1}}{2\sqrt{1+\gamma}\,h}
\]
above it. This proves a unique global spectral-radius minimum at the discriminant-zero step. The repeated root is genuinely defective because the two-step companion matrix has a nonzero lower-left entry and cannot equal a scalar matrix.

For \(\gamma<-1\), the discriminant remains positive and the same real-root-modulus expression has derivative sign determined by \(\gamma+1<0\), giving strict decrease and the stated limit. At \(\gamma=-1\), the direct factor \(r=1\) agrees with the degenerate solution set.

The standalone verification artifact evaluates the quadratic roots independently and agrees with the formulas to floating-point accuracy. The small discrepancies at a repeated root are consistent with the conditioning of the quadratic formula near coalescence.

## Originality

**PASS, to the best of our knowledge.**

The primary recent source inspected was Y. Shehu, arXiv:2609.18373v1. It proves the exact FRB/RFB stability threshold for the pure-skew family and the wider \(A=aI+\gamma J\) phase diagram. Its Figure 1 displays spectral-radius curves, while its theorem statements and discussion concern the unit-circle stability crossing. Its landscape remark explicitly distinguishes the new threshold result from earlier rate tightness at \(A=0\).

The rate benchmark at \(\gamma=0\) is known and is excluded from the novelty claim. S. Soe, V. Vetrivel and J.-C. Yao, arXiv:2509.02005, state that the FRB rotation example has tight spectral radius \(1/\sqrt2\), citing Malitsky--Tam for the FRB case.

Searches for the exact \(\gamma\)-dependent optimum, the discriminant-coalescence condition, and an equivalent spectral-radius formula did not locate an earlier statement. No overlapping SCOPE record was located by searches for the source identifier, the skew-rotation claim family, or reflected-splitting spectral-radius terminology.

The most relevant older sources are Malitsky--Tam (2020), Cevher--Vũ (2021), and the 2025 GFRB paper. Their general convergence results and the \(\gamma=0\) rate example are prior work. The specific \(\gamma\)-dependent rate phase diagram derived here is not attributed to them. Residual originality risk remains because the motivating preprint is very recent and contemporaneous follow-up work may not yet be indexed.

## Value

**PASS.**

The recent source determines how far a stable step may be pushed. The present result answers a different numerical question on the same sharp family: which fixed step is actually fastest asymptotically. The answer is explicit and shows a substantial separation. For the matched-skew worst case, the stability ceiling is \(h=1/2\), whereas the unique rate optimum is \(h=1/(2\sqrt2)\) with spectral radius \(1/\sqrt3\). For \(\gamma\ge3\), every finite step is stable but the fastest step remains finite. These facts give a concrete warning against using the largest admissible fixed step as a proxy for fastest convergence.

The coalescence characterization also exposes the mechanism behind the optimum: the two characteristic modes balance exactly at a defective double root. That adds a useful qualification for practice, because the asymptotically optimal spectral radius comes with a polynomial transient.

## Limitations

The theorem is confined to the exact two-dimensional linear skew family and fixed scalar steps. It does not provide a universal optimal step for FRB/RFB on nonlinear monotone inclusions and does not optimize finite-horizon error. The Jordan prefactor at the discriminant-zero step can matter before the asymptotic regime. The \(\gamma=0\) rate is prior work and is used only as a consistency check.
