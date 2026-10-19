# A quadratic ternary resonance excess in exact sixth moments of lacunary Fourier sums

## Finding

For an integer \(q\ge3\) and \(n\ge1\), set
\[
A_{q,n}=\{0\}\cup\{\pm q^j:0\le j<n\},\qquad
P_{q,n}(e^{it})=1+2\sum_{j=0}^{n-1}\cos(q^j t).
\]
The normalized sixth moment, equivalently the ordered threefold additive energy of \(A_{q,n}\), is
\[
E_q(n)=\frac1{2\pi}\int_0^{2\pi}|P_{q,n}(e^{it})|^6\,dt
=\#\{(a_1,\ldots,a_6)\in A_{q,n}^6:a_1+a_2+a_3=a_4+a_5+a_6\}.
\]
Its exact values are
\[
\boxed{ E_q(n)=
\begin{cases}
141,&n=1,\\
120n^3+240n^2-280n-59,&q=3,\ n\ge2,\\
120n^3+80n-59,&q=4,\ n\ge1,\\
120n^3+32n-11,&q=5,\ n\ge1,\\
120n^3+20n+1,&q\ge6,\ n\ge1.
\end{cases}}
\]
In particular, for every \(n\ge2\) the excess above the stable \(q\ge6\) value is
\[
E_3(n)-E_6(n)=60(4n+1)(n-1),\quad
E_4(n)-E_6(n)=60(n-1),\quad
E_5(n)-E_6(n)=12(n-1).
\]
Thus the integer-ratio-three boundary has a quadratic excess in the number of retained scales, whereas ratios four and five have only a linear excess. The common leading growth is \(120n^3\).

## Assumptions and scope

All exponents are integers; \(q\ge3\) is an integer and \(n\ge1\). The polynomial \(P_{q,n}\) has coefficient exactly one at each frequency in \(A_{q,n}\), including zero, and the circle measure is normalized to total mass one. No claim is made about arbitrary coefficient magnitudes, the optimal \(L^2\)-to-\(L^6\) synthesis norm, Fourier extension into the plane, or ratios below three. Every formula is an integer identity valid for the full stated infinite parameter range.

## Proof

Put \(S_n(z)=1+\sum_{j<n}(z^{q^j}+z^{-q^j})\), and denote its constant coefficient by \(\operatorname{CT}\). On the unit circle the function is real, so \(E_q(n)=\operatorname{CT}S_n^6\). Fourier orthogonality also gives the six-tuple count in the finding.

Write \(F_q(n)=\operatorname{CT}S_n^4\), \(m=2n+1\), \(L=q^{n-1}\), \(M=qL\), and \(T=z^M+z^{-M}\). In a product of \(k\) terms from \(S_n\), every exponent has absolute value at most \(kL\). Let \(a_k= [z^M]S_n^k\), equal by symmetry to \([z^{-M}]S_n^k\). Expanding \(S_{n+1}=S_n+T\), and using \(q\ge3\), gives the exact finite identities
\[
F_q(n+1)-F_q(n)=8a_3+12m+6,
\]
\[
E_q(n+1)-E_q(n)=12a_5+30F_q(n)+120a_3+90m+20.
\]
Indeed \(\operatorname{CT}(S_n^3T)=2a_3\), \(\operatorname{CT}(S_n^5T)=2a_5\), \(\operatorname{CT}(S_n^3T^3)=6a_3\), while the terms with two or four occurrences of \(T\) have only their balanced plus/minus contributions. All other terms are excluded by the exponent-support bound. Also \(\operatorname{CT}S_n^2=m\), \(\operatorname{CT}T^4=6\), and \(\operatorname{CT}T^6=20\).

We now count \(a_3\) and \(a_5\) without estimation. For \(q=3\), reaching \(M=3L\) with three elements of \(A_{3,n}\) requires three copies of \(L\), hence \(a_3=1\). For \(q\ge4\), \(a_3=0\).

For \(q\ge6\), five old elements cannot sum to \(M\), so \(a_5=0\). For \(q=5\), exactly five copies of \(L\) work, giving \(a_5=1\). For \(q=4\), exactly four copies of \(L\) and one zero work, giving \(a_5=5\). The bounds here also exclude combinations with negative elements: if fewer positive \(L\)'s occur, the remaining entries are at most \(L/q\) except for negative \(L\)'s and cannot reach \(qL\).

For \(q=3\), distinguish the number \(r\) of positive \(L\)'s in an ordered five-tuple summing to \(3L\). If \(n\ge2\), only the following configurations exist: two \(L\)'s and three copies of \(L/3\) (ten permutations); three \(L\)'s and two zeros (ten permutations); three \(L\)'s with a cancelling pair \(\pm3^j\) for one of the \(n-1\) lower levels (twenty permutations per level); or four \(L\)'s and one \(-L\) (five permutations). The support bound rules out \(r=0,1,5\) and all other cases. Consequently
\[
a_5=20n+5\quad(q=3,n\ge2).
\]
At the first scale, \(n=1\), the first and lower-level configurations are absent and \(a_5=15\).

Direct constant-term expansion at \(n=1\) yields \(F_q(1)=19\) and \(E_q(1)=141\), independently of \(q\). Substituting the \(a_3\) counts into the fourth-moment recurrence and summing gives
\[
F_3(n)=12n^2+14n-7,\qquad F_q(n)=12n^2+6n+1\quad(q\ge4).
\]
For \(q\ge4\), the sixth-moment recurrence therefore simplifies to
\[
E_q(n+1)-E_q(n)=360n^2+360n+140+12c_q,
\quad c_4=5,\quad c_5=1,\quad c_q=0\ (q\ge6).
\]
Summing from \(n=1\), with \(E_q(1)=141\), proves all three stable-range formulas.

For \(q=3\), the first increment is \(E_3(2)-E_3(1)=1160\), giving \(E_3(2)=1301\). For all subsequent increments \(n\ge2\), substitution gives
\[
E_3(n+1)-E_3(n)=360n^2+840n+80.
\]
Summing from \(n=2\) yields the stated cubic polynomial for every \(n\ge2\). Subtraction gives the three resonance-excess identities. This completes the proof.

## Verification

The standalone file `verify.py` computes exact Laurent coefficients by integer convolution, without using the closed-form proof recurrence to obtain the candidate moments. It checks every \(n\) from one through eight for \(q=3,4,5,6\), additional bases through eight, the intermediate fourth moment and the coefficients \(a_3,a_5\). An independent finite-root-of-unity quadrature checks selected cases in floating-point arithmetic. Running `python3 verify.py` reports all checks and exits nonzero on failure. The infinite claims follow from the combinatorial proof, not these finite tests.

## Relationship to prior work

Gonçalves and Ferreira, arXiv:2510.20934 (first posted 2025-10-23), prove a sharp planar Fourier-extension inequality for lacunarity strictly exceeding three, and explicitly describe the boundary ratio-three case as obstructed by extra triple-sum resonances. Their work analyses Bessel-weighted sixfold frequency sums, not the unweighted, equal-coefficient circular sixth moment computed here. In particular their strict-ratio hypothesis does not cover the \(q=3\) formula. Their classification of exceptional triple sums at ratios four and five provides arithmetic background but does not state the simultaneous exact moment laws.

Ciccone and Gonçalves, arXiv:2208.09441 (first posted 2022-08-19), develop the \(\mathrm P(3)\) framework and include the \(q\ge6\) geometric spectra as examples, identifying \(q=3,4,5\) as exceptional. The stable \(q\ge6\) moment is consistent with their generic collision picture; its inclusion above is for an explicit exact comparison. The specific all-length quadratic excess at the ratio-three boundary is not a consequence of their \(\mathrm P(3)\) theorem, since the boundary spectrum fails that property.

## Limitations

The formula is for an equal-coefficient trigonometric polynomial and its *unweighted* additive energy, not for the Bessel-integral weighted expression in the sharp circular Fourier-extension problem. Hence it neither proves nor disproves the corresponding endpoint sharp Fourier-extension conjecture for ratio three. No exhaustive claim is made about possible older, unindexed moment calculations; historical priority is a residual risk. Ratios \(q=2\), nonintegral ratios, and arbitrary coefficient profiles are excluded.

## References

1. F. Gonçalves and J. P. Ferreira, *On a Sharp Fourier Extension Inequality on the Circle with Lacunary Spectrum*, arXiv:2510.20934, first public posting 2025-10-23. https://arxiv.org/abs/2510.20934
2. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441, first public posting 2022-08-19; published in J. Funct. Anal. 286 (2024), no. 2. https://arxiv.org/abs/2208.09441
