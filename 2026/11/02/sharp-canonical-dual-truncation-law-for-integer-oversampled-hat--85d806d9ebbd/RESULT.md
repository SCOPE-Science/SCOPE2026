# Sharp canonical-dual truncation law for integer-oversampled hat Gabor frames

## Finding

Let \(g(x)=(1-|x|)_+\) and let \(q\ge2\) be an arbitrary integer. For the (unnormalized) Gabor family
\[
\mathcal G_q=\{e^{2\pi i m x}g(x-k/q):m,k\in\mathbb Z\}
\]
on \(L^2(\mathbb R)\), denote the frame operator by \(S_q\) and its canonical (minimum-energy) dual window by \(\gamma_q=S_q^{-1}g\). The frame is well-defined for every such \(q\), with sharp bounds \(A_q=(q^2-1)/(3q)\) and \(B_q=q\). Those bounds serve here as background, not as the novelty claim.

Define the constants
\[
\begin{split}
c_q^*&=\frac{2q^2+1}{12q},\quad d_q^*=\sqrt{\frac{q^2-1}{3}},\\
R_q&=\frac{q-d_q^*}{q+d_q^*},\\
E_q&=\frac1{(d_q^*)^2}\sqrt{\frac{\pi c_q^*d_q^*}{2q^2}}
\sum_{j=0}^{q-1}\left[1-(1+R_q)\frac{j+1/2}{q}\right]^2.
\end{split}
\]
Here \(E_q>0\) and \(0<R_q<1\). The new sharp, **cellwise spatial localization law** is
\[
\boxed{\displaystyle\int_n^{n+1}|\gamma_q(x)|^2\,dx
\sim E_q\,\frac{R_q^{2n}}{\sqrt n}\qquad(n\to\infty).}
\]
Because \(\gamma_q\) is even, the associated exact **symmetric truncation-error asymptotic** is
\[
\boxed{\displaystyle\int_{|x|\ge N}|\gamma_q(x)|^2\,dx
\sim\frac{2E_q}{1-R_q^2}\,\frac{R_q^{2N}}{\sqrt N}\qquad(N\to\infty,\ N\in\mathbb N).}
\]
In particular, the canonical dual has infinite support, and the optimal exponential rate \(R_q\) is strictly decreasing in \(q\), with \(R_2=1/3\) and \(\lim_{q\to\infty}R_q=2-\sqrt3>0\). The fixed nonzero limiting rate distinguishes the canonical dual from other, potentially compactly supported, dual windows.

## Assumptions and scope

All functions are complex-valued elements of \(L^2(\mathbb R)\); the window \(g\) is real, even, unnormalized, and supported on \([-1,1]\). The translation step is precisely \(1/q\); the modulation step is precisely \(1\). The bounds are in the convention
\[
A_q\|f\|_2^2\le\sum_{m,k\in\mathbb Z}|\langle f,e^{2\pi i m\cdot}g(\cdot-k/q)\rangle|^2\le B_q\|f\|_2^2.
\]
The asymptotics hold for each fixed integer \(q\ge2\), not uniformly as \(q\to\infty\) with \(n\). For a real argument \(u\), write \((u)_+=\max\{u,0\}\) and \(\{u\}=u-\lfloor u\rfloor\).

## Proof

**1. Exact fiber multiplier.** Define the unitary Zak transform
\[
Zf(t,\omega)=\sum_{k\in\mathbb Z}f(t+k)e^{-2\pi i k\omega},\qquad 0\le t,\omega<1.
\]
Integer-modulation orthogonality and the usual periodization calculation give
\[
S_qf(x)=\sum_{\ell\in\mathbb Z}f(x-\ell)
\sum_{k\in\mathbb Z}g(x-k/q)g(x-\ell-k/q).
\]
Initially this identity holds on a dense class and extends by boundedness. Since two copies of \(g\) can overlap at integer separation only for \(\ell=0,\pm1\), the Zak transform diagonalizes \(S_q\):
\[
Z(S_qf)(t,\omega)=\Phi_q(t,\omega)Zf(t,\omega),\quad
\Phi_q=q-2c_q(t)+2c_q(t)\cos(2\pi\omega),
\]
where
\[
\begin{split}
u_j(t)&=\{t+j/q\},\qquad
c_q(t)=\sum_{j=0}^{q-1}u_j(t)(1-u_j(t)),\\
x(t)&=\frac{\{qt\}}q,\qquad
c_q(t)=\frac{q^2-1}{6q}+x(t)-qx(t)^2\\
&=\frac{2q^2+1}{12q}-q\left(x(t)-\frac1{2q}\right)^2.
\end{split}
\]
Each of the \(q\) distinct strict maxima of \(c_q\) in \([0,1)\) is attained at \(t_j=(j+1/2)/q\), and its value is \(c_q^*\). For any \(t\), the minimum over \(\omega\) is \(q-4c_q(t)\) and the maximum is \(q\). Thus the sharp lower/upper bounds are as stated; in particular, \(S_q\) is invertible.

**2. Exact canonical-dual Fourier coefficients.** For almost every \(t\), set
\[
\Delta_q(t)=\sqrt{q(q-4c_q(t))},\qquad
r_q(t)=\frac{q-\Delta_q(t)}{q+\Delta_q(t)}.
\]
For \(q\ge2\) these are real with \(\Delta_q>0\), \(0<r_q<1\). The geometric Poisson-kernel expansion yields the absolutely convergent Fourier series
\[
\Phi_q(t,\omega)^{-1}=
\sum_{k\in\mathbb Z}\frac{(-r_q(t))^{|k|}}{\Delta_q(t)}
e^{-2\pi i k\omega}.
\]
For \(0\le t<1\), the original window satisfies
\[
Zg(t,\omega)=(1-t)+t e^{2\pi i\omega}.
\]
Hence \(Z\gamma_q=Zg/\Phi_q\), so comparison of Fourier coefficients gives for every integer \(n\ge0\)
\[
\boxed{\gamma_q(t+n)=\frac{(-r_q(t))^n}{\Delta_q(t)}
\left[1-t(1+r_q(t))\right]},
\]
and, for \(m\ge1\),
\[
\gamma_q(t-m)=\frac{(-r_q(t))^{m-1}}{\Delta_q(t)}
\left[t-(1-t)r_q(t)\right].
\]
These are identities almost everywhere and provide a direct reconstruction of the canonical dual. They also prove \(\gamma_q\) is not compactly supported.

**3. Sharp one-cell asymptotic.** The function \(r_q(t)\) increases strictly with \(c_q(t)\), so its only maxima in a unit cell are the \(q\) nondegenerate points \(t_j\). Write \(d_q^*=\Delta_q(t_j)\), \(R_q=r_q(t_j)\), and \(c_q^*=c_q(t_j)\). Direct differentiation gives
\[
\frac{d}{dc}\log\frac{q-\sqrt{q(q-4c)}}{q+\sqrt{q(q-4c)}}=
\frac{q}{c\sqrt{q(q-4c)}}.
\]
Near any \(t_j\), therefore,
\[
\log r_q(t)=\log R_q-\frac{q^2}{c_q^*d_q^*}(t-t_j)^2
+O_q((t-t_j)^4).
\]
The exact positive-cell identity above implies
\[
I_{q,n}:=\int_n^{n+1}|\gamma_q(x)|^2\,dx
=\int_0^1r_q(t)^{2n}
\frac{[1-t(1+r_q(t))]^2}{\Delta_q(t)^2}\,dt.
\]
Outside fixed small neighborhoods of the \(t_j\), the maximum of \(r_q\) is strictly below \(R_q\). Inside each neighborhood, a Gaussian change of variables and dominated convergence yield
\[
I_{q,n}\sim\frac{R_q^{2n}}{\sqrt n}
\frac1{(d_q^*)^2}\sqrt{\frac{\pi c_q^*d_q^*}{2q^2}}
\sum_{j=0}^{q-1}[1-(1+R_q)t_j]^2,
\]
which is the claimed constant \(E_q\). The sum is strictly positive: its affine summand cannot vanish at all \(q\ge2\) distinct \(t_j\). No uniform-in-\(q\) remainder is claimed.

**4. Symmetric tails and limiting rate.** Reflection \(Rf(x)=f(-x)\) preserves \(g\) and permutes its lattice shifts up to harmless phases, so \(RS_q=S_qR\). Thus \(\gamma_q\) is even. Since \(I_{q,n}\sim E_qR_q^{2n}/\sqrt n\) and \(0<R_q<1\), a geometric-tail comparison gives
\[
\sum_{n\ge N}I_{q,n}\sim\frac{E_q}{1-R_q^2}\frac{R_q^{2N}}{\sqrt N}.
\]
Doubling proves the symmetric-tail formula. Finally,
\[
R_q=\frac{1-\sqrt{(1-q^{-2})/3}}{1+\sqrt{(1-q^{-2})/3}},
\]
which is strictly decreasing for integer \(q\ge2\) and has the stated endpoint values.

## Verification

The accompanying standalone `checker.py` uses only the Python standard library. It compares the multiplier against direct sums of shifted Zak windows, numerically evaluates the Fourier coefficients of its inverse and compares them with the closed formula, checks evenness and exact extrema, and compares numerical cell integrals to the analytical Laplace constants over several \(q\) and large \(n\). It prints the number of assertions on successful completion. These numerical computations supplement the proof; no experiment is used to justify an infinite limit.

For reference, the leading cell-mass constants are \(E_2\approx0.170554451324415\) and \(E_3\approx0.108413745541773\). The claims may be reproduced by running `python3 checker.py` from the directory containing this document.

## Relationship to prior work

The focal work of Ghosh and Selvan [1] concerns frame regions for B-splines and other generators; their subsequent preprint [2] investigates obstructions. Atindehou and coauthors [3] construct explicit compactly supported dual windows in regions of the second-order B-spline frame set, but those need not be the canonical dual. Bölcskei and Janssen [4] establish general inheritance of decay and qualitative restrictions on canonical dual windows; a qualitative exponential-decay conclusion does not yield the exact parameter-dependent exponential rate and \(n^{-1/2}\) prefactor of the spatial-tail law. The precise sharp frame bounds for this lattice and related Zak-fiber spectral statistics are established elsewhere and are not claimed new here.

Janssen's 1996 paper [5] explicitly studies frame bounds and minimal duals at integer redundancy and is an important possible antecedent. Its abstract was accessible, and the publicly listed author-hosted copy could not be read; consequently there is residual priority uncertainty about overlap with the explicit dual formula. The exact spatial \(L^2\) tail and truncation constants, rather than the general Zak method or frame bounds, are the central claim.

## Limitations

The result is for the unnormalized hat window, the exact rectangular lattice with modulation step \(1\), and integer redundancies \(q\ge2\). It is a fixed-\(q\), large-spatial-truncation theorem; neither a double scaling limit nor an arbitrary lattice theorem is proved. The stated asymptotic is an \(L^2\)-cell-mass and symmetric-tail law, not a pointwise uniform limit in space. An earlier inaccessible paper may contain equivalent specialized formulas; historical originality is therefore provisional pending comparison. Independent validation has not been performed.

## References

[1] R. Ghosh and A. A. Selvan, *On Gabor frames generated by B-splines, totally positive functions, and Hermite functions*, arXiv:2304.11322, first public 22 April 2023, https://arxiv.org/abs/2304.11322.

[2] R. Ghosh and A. A. Selvan, *Obstructions for Gabor frames of second order B-spline*, arXiv:2310.01141, 2023, https://arxiv.org/abs/2310.01141.

[3] A. G. D. Atindehou, C. Frederick, Y. B. Kouagou, and K. A. Okoudjou, *On the frame set of the second-order B-spline*, arXiv:1806.05614, https://arxiv.org/abs/1806.05614.

[4] H. Bölcskei and A. J. E. M. Janssen, *Gabor Frames, Unimodularity, and Window Decay*, Journal of Fourier Analysis and Applications 6 (2000), 255–276, https://www.mins.ee.ethz.ch/pubs/files/gabor99.pdf.

[5] A. J. E. M. Janssen, *Some Weyl-Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, doi:10.1016/0019-3577(96)85088-9.
