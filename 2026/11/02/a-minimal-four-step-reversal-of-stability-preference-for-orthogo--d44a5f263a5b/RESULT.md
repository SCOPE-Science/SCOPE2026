# A minimal four-step reversal of stability preference for orthogonally similar damped shears

## Finding
For the two opposite, damped planar shears
\[
U=\begin{pmatrix}a&k\\0&a\end{pmatrix},\qquad
L=\begin{pmatrix}a&0\\-k&a\end{pmatrix},
\qquad 0<a<1,\ k\geq0,
\]
consider a repeated four-step schedule with exactly two occurrences of each. Up to cyclic permutation, there are only two possibilities: grouped \(UULL\) and alternating \(ULUL\). Let \(q=a^2\), \(x=k^2\). The exact strict exponential-stability thresholds are
\[
\begin{aligned}
UULL\text{ stable}&\iff 0\leq x<X_{\rm grp}(q)
=\frac{(1+q^2)^2}{4q},\\
ULUL\text{ stable}&\iff 0\leq x<X_{\rm alt}(q)
=(1+q)^2.
\end{aligned}
\]
There is exactly one damping crossover,
\[
q_*=1+\sqrt3-\sqrt{3+2\sqrt3}
=0.1895910507314648\ldots.
\]
If \(0<q<q_*\), every \(X_{\rm alt}(q)<x<X_{\rm grp}(q)\) gives an exponentially stable grouped schedule but an unstable alternating schedule. If \(q_*<q<1\), every \(X_{\rm grp}(q)<x<X_{\rm alt}(q)\) gives the reverse. At \(q=q_*\) the thresholds coincide; at their common boundary the grouped four-step monodromy has multipliers \(-1,-q^4\), whereas the alternating monodromy has multipliers \(+1,+q^4\).

Each individual one-step map has double eigenvalue \(a\), and the two one-step matrices are orthogonally similar, so both schedules have exactly the same multiset of one-step eigenvalues *and* singular values. Four is the smallest word length allowing any spectral distinction by rearranging two fixed invertible matrices while preserving both multiplicities.

## Assumptions and scope
The dynamics are the linear nonautonomous recurrence \(v_{n+1}=B_nv_n\) on \(\mathbb R^2\), with a periodically repeated finite word of matrices \(B_n\in\{U,L\}\) and period four. Parameters satisfy \(0<a<1\) and \(k\geq0\). A schedule is *exponentially stable* when every solution tends to zero at an exponential rate, equivalently when the spectral radius of one period's monodromy is strictly less than one. At the boundary, a multiplier on the unit circle excludes exponential attraction; no claim of nonlinear dynamics or chaos is made.

## Proof
**Products and spectra.** Because each matrix has determinant \(a^2=q>0\), all factors are invertible and cyclic permutation preserves a product's characteristic polynomial. Exactly-two-of-each four-letter words form two cyclic classes, with representative product matrices \(G=U^2L^2\) and \(A=(UL)^2\). Direct multiplication gives
\[
\operatorname{tr}(G)=2q^2-4qx,\qquad
\operatorname{tr}(A)=2q^2-4qx+x^2,
\qquad\det G=\det A=q^4.
\]
In particular \(\operatorname{tr}(A)-\operatorname{tr}(G)=x^2=k^4\). Both characteristic polynomials are \(\lambda^2-t\lambda+q^4\), with \(t\) the respective trace.

**Sharp stability inequalities.** For a real quadratic \(\lambda^2-t\lambda+d\) with \(0<d<1\), both roots have modulus strictly less than one if and only if \(-(1+d)<t<1+d\) (the degree-two Schur criterion). For \(G\), its trace strictly decreases from \(2q^2<1+q^4\), and the lower boundary is reached precisely at
\[
x=\frac{1+2q^2+q^4}{4q}=X_{\rm grp}(q).
\]
For \(A\), complete the square:
\[
\operatorname{tr}(A)=(x-2q)^2-2q^2.
\]
Its minimum \(-2q^2\) strictly exceeds \(-(1+q^4)\), since \((1-q^2)^2>0\). Its only nonnegative upper-bound crossing is at
\[
x=2q+(1+q^2)=(1+q)^2=X_{\rm alt}(q).
\]
These establish both necessary-and-sufficient thresholds, including equality cases.

**Unique reversal.** The difference between the thresholds has sign equal to that of
\[
q^4-4q^3-6q^2-4q+1
=q^2\big[(q+q^{-1})^2-4(q+q^{-1})-8\big].
\]
The variable \(q+q^{-1}\) strictly decreases from infinity to two as \(q\) increases from zero to one; the bracket has exactly one zero in that range, at \(q+q^{-1}=2+2\sqrt3\). Its unique \(q\in(0,1)\) solution is \(q_*\) as displayed. Below it the grouped threshold is larger; above it the alternating threshold is larger. At either threshold the characteristic polynomial factors as \((\lambda+1)(\lambda+q^4)\) for grouped and \((\lambda-1)(\lambda-q^4)\) for alternating.

**Smallest possible order dependence.** Any two words of length at most three with the same number of \(U\)'s and \(L\)'s are cyclic permutations. Since both factors are invertible, their products are conjugate and have identical spectra. Length four is the first occurrence of two non-cyclic ordering classes. Orthogonal similarity of the one-step factors follows by conjugating \(U\) with \(R=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\), obtaining \(L=RUR^{\mathsf T}\). This proves the identical one-step spectral and singular-value data.

**Exact rational witnesses.** For \(a=1/4,k=3/2\), the grouped and alternating traces are respectively \(-71/128\) and \(577/128\), with common determinant \(1/65536\); the grouped word is strictly stable and the alternating word is unstable. For \(a=1/2,k=7/6\), the respective traces are \(-89/72\) and \(799/1296\), with determinant \(1/256\); now grouped is unstable and alternating strictly stable.

## Verification
The standalone script `verify.py` uses only the Python standard library and exact rational arithmetic. It recomputes both product traces and determinants for rational parameter grids, checks all six arrangements of two \(U\)'s and two \(L\)'s against the cyclic-class formulas, compares exact Schur signs with the derived thresholds, and checks both explicit instability-reversal witnesses and rational enclosures for the crossover. These finite checks supplement, not replace, the all-parameter proof above. To replay, run `python verify.py` in the directory containing this document and the script.

## Relationship to prior work
Sornette, Saiprasad, and Troude (2026, arXiv:2609.18017v1) investigate the ordering of non-normal tangent maps in Hénon-type and Ikeda dynamics, including an autonomous reciprocal-shear alternation. Their main text and complete supplement were examined. The present claim does not assert that order-sensitive growth or stabilizing reorientation is new; it provides a separate exact classification of every balanced four-letter word of the explicitly specified damped triangular pair, including a unique crossover where the preferred order reverses.

Their earlier *Non-Normal Route to Chaos* (arXiv:2603.08191) demonstrates switching-driven instability in a spectrally contracting nonlinear model, with a two-step singular-value proxy; it does not provide these four-step Schur boundaries. Sturman and Thiffeault's *Lyapunov Exponents for the Random Product of Two Shears* (2018 online; arXiv:1706.03398) gives bounds for random positive and negative shear products, including the negative-shear regime, but not a deterministic four-step damping-crossover classification. Classical Floquet theory, the Schur criterion and elementary shear algebra are used without originality claims. Historical priority against specialized switching-sequence literature remains provisional.

## Limitations
The theorem concerns the two matrices displayed, a fixed-periodic deterministic linear system, and exact two-of-each schedules. It does not classify arbitrary length words, stochastic switches, nonlinear stability, or chaotic attractors. The stability boundaries are nonhyperbolic and are not included in the strict exponential-stability statements. The exact crossing does not establish a global schedule-design rule for other matrix families. Searches and inspected primary sources cannot establish absolute historical priority.

## References
1. D. Sornette, V. R. Saiprasad and V. Troude, *A New Route to Chaos through the Geometric Composition of Non-Normal Amplification*, arXiv:2609.18017v1, first public 16 September 2026. https://arxiv.org/abs/2609.18017
2. D. Sornette, V. R. Saiprasad and V. Troude, *Non-Normal Route to Chaos*, arXiv:2603.08191, first public 9 March 2026. https://arxiv.org/abs/2603.08191
3. R. Sturman and J.-L. Thiffeault, *Lyapunov Exponents for the Random Product of Two Shears*, Journal of Nonlinear Science 29, 593–620 (2019), first published online 21 September 2018. DOI: 10.1007/s00332-018-9497-3. https://doi.org/10.1007/s00332-018-9497-3
