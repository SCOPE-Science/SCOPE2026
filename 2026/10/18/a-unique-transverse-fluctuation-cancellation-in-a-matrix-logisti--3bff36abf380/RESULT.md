# A unique transverse fluctuation cancellation in a matrix logistic map

## Finding
For the two-by-two Hermitian matrix logistic map of Pawela and Życzkowski, let
\[
F_b(H)=D_b H(I-H)D_b,\qquad D_b=\operatorname{diag}(2,b),\qquad 1<b<\sqrt3.
\]
Set \(c_b=1-b^{-2}\). The invariant diagonal curve \(H=\operatorname{diag}(x,c_b)\), \(0\le x\le1\), carries the full logistic map \(f(x)=4x(1-x)\) and its stationary arcsine probability \(d\mu(x)=dx/[\pi\sqrt{x(1-x)}]\). Infinitesimal complex off-diagonal perturbations evolve by the scalar multiplier \(2b(1-c_b-x)\).

For \(x_0\) distributed according to \(\mu\), define \(x_j=f^j(x_0)\) and the logarithmic transverse derivative magnitude
\[
L_n(x_0)=\sum_{j=0}^{n-1}\log|2b(1-c_b-x_j)|.
\]
All logarithms here are finite outside a \(\mu\)-null set. For every \(1<b<\sqrt3\):
\[
\frac{L_n}{n}\longrightarrow\log(b/2)\quad\text{almost surely},\qquad
\frac{L_n-n\log(b/2)}{\sqrt n}\Longrightarrow N(0,\sigma_b^2).
\]
Let \(\beta_b=\arccos(2c_b-1)\). The asymptotic variance is the absolutely convergent explicit series
\[
\boxed{\displaystyle\sigma_b^2=2\sum_{\substack{q\ge1\\q\ \mathrm{odd}}}\frac{1}{q^2}\left[\sum_{j=0}^{\infty}2^{-j}\cos(2^jq\beta_b)\right]^2.}
\]
In this entire parameter interval, \(\sigma_b^2=0\) **if and only if** \(b=\sqrt2\). At that unique value, the centered sums are exact \(L^2\)-bounded coboundaries. By contrast, the explicitly evaluable parameter \(b=2/\sqrt3\) has
\[
\boxed{\sigma_{2/\sqrt3}^2=\pi^2/3.}
\]
Thus normal transverse contraction has the same simple Lyapunov formula for the whole family, but its finite-time logarithmic fluctuations have a unique degeneracy in the stable-fixed-channel regime.

## Assumptions and scope
The phase space is the compact Hermitian order interval \(\{H=H^*:0\preceq H\preceq I\}\); here \(b\) is a real scalar satisfying \(1<b<\sqrt3\). The theorem concerns the linearized off-diagonal complex coordinate along the invariant diagonal curve and stationary initial \(x_0\sim\mu\); the real and imaginary off-diagonal directions have the same multiplier. It does **not** claim a central limit theorem for an arbitrary non-diagonal initial matrix, nor does it assert globally attracting nonlinear synchronization. For the diagonal orbit, the other two real tangent exponents are \(\log2\) and \(\log|2-b^2|\), with the latter \(-\infty\) at \(b=\sqrt2\). The two transverse real exponents are both \(\log(b/2)\).

## Proof
**1. Invariant curve and exact normal cocycle.** Write \(H=\left(\begin{smallmatrix}x&z\\\overline z&y\end{smallmatrix}\right)\). Matrix multiplication gives
\[
x'=4\bigl(x(1-x)-|z|^2\bigr),\quad
y'=b^2\bigl(y(1-y)-|z|^2\bigr),\quad
z'=2b(1-x-y)z.
\]
For \(y=c_b=1-b^{-2}\) and \(z=0\) the second coordinate is fixed and the first is \(f(x)=4x(1-x)\). Since \(b\le2\), the original map preserves the Hermitian order interval: \(0\preceq H(I-H)\preceq I/4\) and \(D_b^2\preceq4I\). Differentiation at \(z=0\) proves the asserted scalar normal multiplier and tangent splitting.

**2. Circle conjugacy and exact mean.** Under \(x=(1-\cos\theta)/2\) with normalized Haar measure \(d\theta/(2\pi)\), the logistic map is the doubling endomorphism \(T\theta=2\theta\pmod{2\pi}\). Put \(\beta=\beta_b\); then \(2c_b-1=\cos\beta\) and the normal multiplier is \(b(\cos\theta-\cos\beta)\). The Fourier identity
\[
\log|\cos\theta-\cos\beta|+\log2
=-2\sum_{k\ge1}\frac{\cos(k\beta)}{k}\cos(k\theta)
\quad\text{in }L^2(d\theta/2\pi)
\]
follows by adding the classical expansions of \(\log|2\sin((\theta\pm\beta)/2)|\). It gives the mean \(\log(b/2)\). The doubling map is ergodic, so Birkhoff's theorem yields almost-sure convergence of \(L_n/n\).

**3. Martingale approximation and explicit variance.** Denote the centered logarithmic observable by \(\psi_\beta\) and let \(P\) be the transfer operator dual to composition with \(T\) on Haar \(L^2\). The elementary Fourier action is \(P\cos(k\theta)=\cos((k/2)\theta)\) for even \(k\), and zero for odd \(k\). The preceding series implies \(\|P^j\psi_\beta\|_2\le C2^{-j}\). Thus \(h=\sum_{j\ge1}P^j\psi_\beta\in L^2\) and
\[
m=\psi_\beta+h-h\circ T,\qquad Pm=0.
\]
The process \(m\circ T^j\) is a stationary reverse-martingale difference sequence. The ergodic martingale central limit theorem applies; the coboundary \(h\circ T^n-h\) has bounded \(L^2\)-norm and does not affect the normalized sums. Only odd Fourier frequencies remain in \(m\); for each positive odd \(q\), its cosine coefficient is
\[
-\frac2q\sum_{j\ge0}2^{-j}\cos(2^jq\beta).
\]
Orthogonality of the cosine basis gives exactly the displayed series for \(\|m\|_2^2=\sigma_b^2\). The series converges absolutely because the bracket has magnitude at most two. This also establishes \(n^{-1}\operatorname{Var}(L_n)\to\sigma_b^2\).

**4. Classification of all zero-variance parameters within the stated interval.** Define a finite even measure on the circle by
\[
\eta_\beta=\frac12\sum_{j\ge0}2^{-j}
(\delta_{2^j\beta}+\delta_{-2^j\beta}).
\]
Its \(q\)-th Fourier coefficient is the inner bracket in the variance series. Since the series is a sum of nonnegative terms, \(\sigma_b^2=0\) precisely when every odd Fourier coefficient of \(\eta_\beta\) vanishes. Fourier uniqueness for finite measures makes this equivalent to \(\eta_\beta\) being invariant under rotation by \(\pi\). The level-zero pair of atoms \(A=\{\beta,-\beta\}\) has total mass one, and all higher levels together have total mass one.

If \(\beta\ne\pi/2\) and \(0<\beta<\pi\), the sets \(A\) and \(A+\pi\) are disjoint. Rotation invariance would force mass at least one on \(A+\pi\), hence **every** higher-level atom lies there. In particular, \(2\beta\equiv\beta+\pi\) or \(2\beta\equiv-\beta+\pi\pmod{2\pi}\); within \(0<\beta<\pi\) the only possibility is \(\beta=\pi/3\). But the present range \(0<c_b<2/3\) gives \(\arccos(1/3)<\beta<\pi\), excluding \(\pi/3\). For \(\beta=\pi/2\), the first-level Fourier factor is zero for odd \(q\), the second contributes \(-1/2\), and the remaining geometric tail contributes \(+1/2\), so the variance vanishes. This is \(c_b=1/2\), equivalently \(b=\sqrt2\), completing the classification.

**5. Exact coboundary and a nonzero variance witness.** At \(b=\sqrt2\), the normal factor is \(b\cos\theta\) and the product identity \(\prod_{j=0}^{n-1}2\cos(2^j\theta)=\sin(2^n\theta)/\sin\theta\) gives
\[
L_n-n\log(b/2)=\log|\sin(2^n\theta)|-\log|\sin\theta|.
\]
These differences are uniformly bounded in \(L^2\) under Haar measure. At \(b=2/\sqrt3\), one has \(\beta=2\pi/3\): the inner bracket equals two for odd \(q\) divisible by three and minus one for the remaining odd \(q\). Consequently
\[
\sigma_b^2=2\left(4\frac{\pi^2}{72}+\frac{\pi^2}{9}\right)=\frac{\pi^2}{3}.
\]

## Verification
Run the accompanying standard-library-only `verify.py` with `python3 verify.py`. It checks the matrix-coordinate identity for rational samples, the invariant fixed channel, the exact resonance cosine sums, bounded partial sums of the variance series and the finite-iterate telescoping identity. On the packaged version, **4,199 assertions passed**. These finite checks are supplementary; the infinite-time limit laws and uniqueness classification follow from the foregoing proof, not the script.

## Relationship to prior work
Pawela and Życzkowski introduced the matrix logistic map, its diagonal two-node specialization, invariant spectral distributions and numerical transfer-of-chaos examples (arXiv:2303.06176, first public version 10 March 2023; especially Eq. (6) and Appendix A). Their diagonal-matrix calculations concern steady-state scalar spectral distributions; they do not provide the off-diagonal normal cocycle's Gaussian fluctuation law or its unique cohomological cancellation parameter. The general martingale-coboundary method is standard (Gordin and subsequent refinements); the present contribution is the exact model-dependent variance series and zero-variance classification. Investigations of different coupled *scalar* logistic maps do not imply these Hermitian off-diagonal statements.

## Limitations
The statement is stationary and linearized: an arcsine-distributed initial point on the diagonal invariant curve and the corresponding infinitesimal normal derivative. It does not classify finite-amplitude non-diagonal orbits or global attraction basins. The logarithm is singular at isolated phase values; the exceptional countable preimage set has zero arcsine measure. The variance series is explicit and absolutely convergent, not claimed to admit an elementary closed form at general parameter values. Priority is assessed relative to the inspected primary paper, related standard theory and targeted literature searches; complete historical uniqueness is not certified.

## References
1. Ł. Pawela and K. Życzkowski, *Matrix logistic map: fractal spectral distributions and transfer of chaos*, arXiv:2303.06176v1 (public 10 March 2023), https://arxiv.org/abs/2303.06176. See the Hermitian map, graph-coupled Eq. (6), and Appendix A.
2. M. Gordin and M. Peligrad, *On the functional central limit theorem via martingale approximation*, arXiv:0910.3448 (2009), https://arxiv.org/abs/0910.3448 (general martingale approximation, not the present model-specific variance).
