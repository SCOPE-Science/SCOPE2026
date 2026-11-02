# Sharp frame bounds for odd-denominator two-channel hat-spline Gabor lattices

## Finding
Let \(g(t)=(1-|t|)_+\), and let \(q\ge3\) be an odd integer. The Gabor system
\[
\mathcal G_q=\{e^{2\pi i kt}g(t-2j/q):j,k\in\mathbb Z\}
\]
is a frame for \(L^2(\mathbb R)\) with the **exact optimal squared-analysis bounds**
\[
\boxed{A_q=\frac{q^2-1}{6q},\qquad
B_q=\frac{2q^2+1+\sqrt{(q^2-1)^2+9}}{6q}.}
\]
Consequently its sharp spectral condition number is
\[
\boxed{\kappa_q=\frac{B_q}{A_q}
=2+\frac{3}{q^2-1}+\sqrt{1+\frac{9}{(q^2-1)^2}}.}
\]
The numbers \(\kappa_q\) decrease strictly along odd \(q\ge3\), and satisfy the sharp uniform bounds
\[
3<\kappa_q\le\frac{19+\sqrt{73}}8,
\qquad\lim_{q\to\infty}\kappa_q=3.
\]
For instance \(A_3=4/9\) and \(B_3=(19+\sqrt{73})/18\). This is a complete quantitative statement for the first nontrivial rational numerator-two oversampling family at unit modulation spacing, rather than a qualitative frame-set assertion.

## Assumptions and scope
Here \((1-|t|)_+=\max(1-|t|,0)\), the Fourier modulations are \(M_kf(t)=e^{2\pi i kt}f(t)\), and translations are \(T_af(t)=f(t-a)\). The frame inequalities have the convention
\[
A_q\|f\|_2^2\le\sum_{j,k\in\mathbb Z}|\langle f,M_kT_{2j/q}g\rangle|^2\le B_q\|f\|_2^2.
\]
The theorem holds for **every** odd integer \(q\ge3\), not for arbitrary rational lattices, irrational steps, or different windows. Translation by one unit converts this centered hat into the non-centered second-order cardinal spline without changing its Gabor frame bounds.

## Proof
Write \(a=2/q\). Applying Fourier-series Parseval in the unit-length modulation variable to the finitely supported window yields the Walnut representation, initially on compactly supported test functions and then by bounded extension:
\[
(S_qf)(t)=D(t)f(t)+E(t)f(t-1)+E(t+1)f(t+1),
\]
where
\[
D(t)=\sum_{j\in\mathbb Z}g(t-ja)^2,
\qquad E(t)=\sum_{j\in\mathbb Z}g(t-ja)g(t-ja-1).
\]
All sums are locally finite; \(D,E\) are \(a\)-periodic. Because \(q\) is odd, a unit translation interchanges two coefficient values, and a translation by two restores them. The decomposition of \(L^2(\mathbb R)\) into integer-shift fibers followed by the period-two Bloch transform shows that the spectrum of \(S_q\) is the essential union of eigenvalues of the Hermitian matrices
\[
H(t,\varphi)=\begin{pmatrix}
D(t)&E(t+1)+e^{-i\varphi}E(t)\\
E(t+1)+e^{i\varphi}E(t)&D(t+1)
\end{pmatrix},
\quad 0\le t<1/q,\quad0\le\varphi<2\pi.
\]
(This is a unitary fiberization of the positive frame operator, not merely a pointwise approximation.) Since \(E\ge0\), the eigenvalue maximum and minimum over \(\varphi\) both occur at \(\varphi=0\): maximal off-diagonal modulus maximizes the larger eigenvalue and minimizes the smaller one.

Put \(q=2m+1\) and \(z=qt\in[0,1]\). Using the two linear branches of the hat, finite arithmetic-progression sums give
\[
D(t)=\frac{q^2-1+3z^2}{3q},\qquad
D(t+1)=\frac{q^2-1+3(z-1)^2}{3q},
\]
and
\[
E(t)=\frac{q^2-1}{12q}+\frac{m z(1-z)}{q^2},\qquad
E(t+1)=\frac{q^2-1}{12q}+\frac{(m+1)z(1-z)}{q^2}.
\]
For clarity, these identities follow by summing the \(q\) sample locations \(t+2j/q\), \(0\le j<q\), for \(D(t)\), and \(t+(2j+1)/q\) for \(D(t+1)\). In the former sum the branch changes after \(j=m\), and in the latter after \(j=m-1\). For \(E\), only the second branches contribute, with terms \((u-1)(2-u)\); all endpoint terms vanish. This also justifies the formulas at the interval boundaries.

Let \(w=(2z-1)^2\in[0,1]\). The trace, diagonal difference, and off-diagonal sum satisfy
\[
D(t)+D(t+1)=\frac{4q^2-1+3w}{6q},\quad
D(t)-D(t+1)=\frac{2z-1}{q},\quad
E(t)+E(t+1)=\frac{2q^2+1-3w}{12q}.
\]
The two extreme Bloch eigenvalues at phase zero are therefore
\[
\lambda_\pm(w)=\frac{4q^2-1+3w\pm
\sqrt{(2q^2+1-3w)^2+36w}}{12q}.
\]
Set \(R(w)=\sqrt{(2q^2+1-3w)^2+36w}\). Direct differentiation yields
\[
\lambda_\pm'(w)=\frac{1}{4q}\left(1\pm\frac{5-2q^2+3w}{R(w)}\right).
\]
Both derivatives are **strictly positive** since
\[
R(w)^2-(5-2q^2+3w)^2=24(q^2-1)>0.
\]
Hence the smallest eigenvalue is \(\lambda_-(0)=(q^2-1)/(6q)\), while the largest is \(\lambda_+(1)=[2q^2+1+\sqrt{(q^2-1)^2+9}]/(6q)\). Continuity of the fibers ensures that these boundary values are the *essential* spectral infimum and supremum, so the bounds are sharp even though their attaining fibers have measure zero. In particular \(A_q>0\), proving the frame property.

Finally, division gives the displayed \(\kappa_q\). Each term following the constant \(2\) is strictly decreasing in \(q^2-1\); its limit is \(1\). Thus \(\kappa_q\) decreases and tends to \(3\), with its largest value at \(q=3\).

## Verification
Run `python3 CHECK.py` with the Python standard library. The checker verifies 773 assertions: exact fractional-polynomial identities for fifteen odd values of \(q\) and five rational fiber points each, and a separate numerical direct Zak-fiber reconstruction for four odd values of \(q\). The numerical component evaluates the standard \(2\times q\) Zak matrix itself, not the Walnut expressions, checks the stated sharp inequalities across a grid, and tests fibers realizing the extrema. These finite checks are supplementary: all-\(q\) correctness follows from the symbolic sums, unitary fiberization, and strict analytic monotonicity above. The checker is an independent implementation of these finite calculations, not an independent expert mathematical audit.

## Relationship to prior work
Stangl and Frederick (first publicly posted 2026-08-31) characterized the hat-spline Gabor frame set on the integer-oversampled hyperbolas \(ab=1/q\) for \(b\ge3/2\), noting that the full \(p\times q\) rational-oversampling problem for \(p>1\) requires separate control of the least singular value. Their theorem does not determine optimal frame bounds at \(b=1\), \(ab=2/q\), and this result does **not** claim to settle their \(b\ge3/2\) open regime. Atindehou, Frederick, Kouagou, and Okoudjou studied regions of the second-order spline's frame set and dual window constructions, but do not state this all-odd-denominator sharp bound and conditioning formula. The classical Zibulski--Zeevi matrix theorem and the Walnut representation supply the framework; the new step is complete exact optimization of the period-two fibers over their continuous parameters and all odd denominators.

## Limitations
The result does not classify other numerator-two lattices with noninteger modulation spacing, other windows, or arbitrary oversampling fractions. Its asymptotic condition-number limit concerns the non-normalized frame-operator condition number, and is not a claim of canonical dual-window localization or optimal window design. No independent mathematical audit has been performed. A residual possibility of equivalent formulas in older, incompletely indexed frame-operator literature cannot be eliminated solely by available searches.

## References
1. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481 (first submitted 2026-08-31), https://arxiv.org/abs/2609.00481.
2. A. G. D. Atindehou, C. Frederick, Y. B. Kouagou, and K. A. Okoudjou, *On the frame set of the second-order B-spline*, arXiv:1806.05614; Appl. Comput. Harmon. Anal. 62 (2023), 237–250, https://arxiv.org/abs/1806.05614.
3. M. Zibulski and Y. Y. Zeevi, *Analysis of multiwindow Gabor-type schemes by frame methods*, Appl. Comput. Harmon. Anal. 4 (1997), 188–221 (rational Zak-fiber framework).
