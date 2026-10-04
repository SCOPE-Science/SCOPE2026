# A certified robustness interval for strict entanglement-of-purification nonadditivity
## Finding
Let \(\Psi_-\) be the two-qubit singlet projector and let
\[
W(f)=f\Psi_-+\frac{1-f}{3}(I-\Psi_-).
\]
For every
\[
f\in\left[\frac{199}{40000},\frac{201}{40000}\right]
=\left[\frac1{200}-\frac1{40000},\frac1{200}+\frac1{40000}\right],
\]
the ordinary von Neumann entanglement of purification is strictly nonadditive along tensor powers:
\[
E_P^\infty(W(f))<E_P(W(f)).
\]
More quantitatively, throughout this interval,
\[
E_P(W(f))>0.96702637,
\qquad
E_P^\infty(W(f))<0.966531,
\]
so the certified separation is greater than \(0.00049537\) bit.

## Assumptions and scope
The input theorem is the rigorous pointwise result of Krohn-Grimberghe for \(f_0=1/200\): \(E_P(W(f_0))>97/100\), together with the certified endpoint witness \(E_P(W(1/100))\le U_+\), where
\[
U_+=\frac{922616583105498918071628209679061634159251672167426749996626}{10^{60}}.
\]
The regularized quantity is \(E_P^\infty(\rho)=\inf_{n\ge1}E_P(\rho^{\otimes n})/n\). The argument uses the Chen--Winter convexity inequality for \(E_P^\infty-S\), and the finite-dimensional ancilla bound that for a rank-four two-qubit state an optimal purification may be taken with ancillary factors of dimension at most four.

## Proof
Write \(f_0=1/200\). First control the one-copy value. Let \(f\) be in the stated interval and choose an optimal purification of \(W(f)\) with \(A'\cong B'\cong\mathbb C^4\). By Uhlmann's theorem there is a purification of \(W(f_0)\) on the same ancillary system whose overlap with the chosen purification equals the root fidelity. Partial trace cannot increase trace distance, so the two \(AA'\) reductions, which have dimension eight, are at trace distance at most the purified distance
\[
\delta(f)=\sqrt{1-F(W(f),W(f_0))^2}.
\]
The states commute in the Bell basis, hence
\[
F(W(f),W(f_0))=\sqrt{ff_0}+\sqrt{(1-f)(1-f_0)}.
\]
Fannes--Audenaert continuity in dimension eight gives
\[
E_P(W(f))\ge E_P(W(f_0))-g(\delta(f)),
\qquad
g(\delta)=\delta\log_2 7+h_2(\delta).
\]
Indeed, apply the entropy bound to the chosen optimal purification of \(W(f)\) and its Uhlmann partner for \(W(f_0)\), then use the defining minimum of \(E_P(W(f_0))\).

The fidelity derivative is positive for \(f<f_0\) and negative for \(f>f_0\), so \(\delta(f)\) is maximized at an endpoint of the interval. Exact outward square-root enclosures at both endpoints give
\[
\delta(f)<0.000178.
\]
Since \(g\) is increasing on this range, directed rational logarithm bounds give
\[
g(0.000178)<0.00297363,
\]
and the source theorem therefore yields
\[
E_P(W(f))>0.97-0.00297363=0.96702637.
\]

For the regularized upper bound, every \(f\in[0,1/100]\) satisfies the exact affine identity
\[
W(f)=(1-100f)W(0)+100f\,W(1/100).
\]
The symmetric-support endpoint has \(E_P^\infty(W(0))=1\). Applying the Chen--Winter inequality and the source endpoint witness gives
\[
E_P^\infty(W(f))\le U(f),
\]
where
\[
U(f)=S(W(f))+(1-100f)(1-S(W(0)))+100f(U_+-S(W(1/100))).
\]
Here
\[
S(W(f))=h_2(f)+(1-f)\log_2 3.
\]
Its derivative is
\[
U'(f)=\log_2\!\left(\frac{1-f}{3f}\right)+100\bigl(U_+-S(W(1/100))-1+S(W(0))\bigr).
\]
The first term decreases with \(f\). Directed rational logarithm bounds at the left endpoint certify \(U'(f)<-8\) on the whole interval. Thus \(U\) is strictly decreasing there, and an outward evaluation at \(f=199/40000\) gives
\[
U(f)<0.966531.
\]
Combining the two uniform bounds gives the claimed separation greater than \(0.00049537\) bit.

## Verification
The accompanying `verify.py` uses only exact integers and rational numbers in deciding comparisons. Square roots are enclosed by dyadic rationals checked by integer squaring. Logarithms use the positive atanh series after range reduction, with an explicit rational remainder bound. It checks both endpoint purified distances, the continuity penalty, the regularized upper bound, the derivative sign, and the final positive gap. Running `python3 verify.py` prints `VERIFY_OK`.

The finite computation is not a substitute for the analytic argument: the proof that endpoint checks control the whole interval is the monotonicity of the Werner fidelity and of \(U\), while the entropy continuity step follows from Uhlmann plus Fannes--Audenaert.

## Relationship to prior work
Terhal, Horodecki, Leung, and DiVincenzo introduced \(E_P\), its regularization, and Werner-state numerics. Chen and Winter proved the convexity of \(E_P^\infty-S\) and gave strong numerical evidence of nonadditivity near \(f=1/200\). Krohn-Grimberghe supplied the first rigorous ordinary von Neumann nonadditivity theorem at the single parameter \(f_0=1/200\), proving \(E_P(W(f_0))>0.97\) and an exact regularized upper chain. The present result does not re-prove that finite certificate; it combines its exact margins with a dimension-eight continuity argument and a uniform endpoint interpolation to turn the isolated certified parameter into an explicit robustness interval.

Claim-specific searches for a Werner-state nonadditivity neighborhood, continuity-based robust nonadditivity, and an open interval for ordinary von Neumann \(E_P\) found the point theorem, the 2012 numerical program, and general background on \(E_P\), but no statement covering the interval above. The closest primary source explicitly states its theorem at \(f=1/200\) and lists the absence of exact values or a witnessing tensor power as limitations.

## Limitations
The interval is a certified convenience, not claimed maximal. The argument does not identify the least tensor power witnessing strict subadditivity, does not compute either \(E_P\) or \(E_P^\infty\) exactly, and does not imply nonadditivity outside the displayed interval. The lower bound inherits the rigorous \(E_P(W(1/200))>0.97\) theorem as a literature premise; the new verifier certifies the continuity and interpolation steps, not the source paper's 25,383-leaf certificate.

## References
1. A. Krohn-Grimberghe, *The entanglement of purification is not additive*, `arXiv:2609.29539v1` (2026).
2. J. Chen and A. Winter, *Non-Additivity of the Entanglement of Purification (Beyond Reasonable Doubt)*, `arXiv:1206.1307v1` (2012).
3. B. M. Terhal, M. Horodecki, D. W. Leung, and D. P. DiVincenzo, *The entanglement of purification*, Journal of Mathematical Physics 43, 4286--4298 (2002), DOI `10.1063/1.1498001`.
4. M. Fannes and K. M. R. Audenaert, sharp finite-dimensional continuity bound for the von Neumann entropy; the form used here is \(|S(\rho)-S(\sigma)|\le T\log_2(d-1)+h_2(T)\) for trace distance \(T\) in the stated small-distance regime.
