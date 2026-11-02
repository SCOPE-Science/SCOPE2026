# All-noise-strength mixing-entropy concavity for a fourth-Hermite Fokker–Planck relaxation

## Finding

For the positive, genuinely non-Gaussian fourth-Hermite density \(p_a(x)=\phi(x)[1+a\operatorname{He}_4(x)]\), with \(0<a\le 1/100\), arbitrary Ornstein–Uhlenbeck smoothing \(0<q\le1\), and independent copies \(X_q,Y_q\), the mixing entropy
\[
F_{a,q}(t)=h\!\left(\sqrt{1-t}\,X_q+\sqrt t\,Y_q\right)
\]
obeys the explicit **strict uniform curvature bound**
\[
\boxed{F_{a,q}''(t)\le -7a^2q^4<0}\qquad(0<t<1).
\]
Here \(X_q=\sqrt q\,X+\sqrt{1-q}\,Z\), \(Y_q\) is formed independently, \(X,Y\) are independent with law \(p_a\), and \(Z\) is independent standard Gaussian. This includes the **unsmoothed endpoint** \(q=1\) and every noise strength; a prior explicit result for this same family treated only \(0<q\le5/8\). No assertion is made for general symmetric non-Gaussian laws.

## Assumptions and scope

The reference density is \(\phi(x)=(2\pi)^{-1/2}\exp(-x^2/2)\). The probabilists' Hermite polynomials are \(A(x)=\operatorname{He}_4(x)=x^4-6x^2+3\) and \(B(x)=\operatorname{He}_8(x)=x^8-28x^6+210x^4-420x^2+105\). Since \(A\ge-6\), every \(0<a\le1/100\) defines a positive probability density. Orthogonality gives mean zero and unit variance. The two OU noise copies must be independent. The proof is valid for all real \(t\) with \(0<t<1\), and includes \(q=1\) without taking a noisy limit. Entropy is differential Shannon entropy with natural logarithms.

The dynamics has a direct nonequilibrium statistical-mechanics interpretation: \(q=e^{-2\tau}\) is the Hermite-mode attenuation parameter for a unit-rate one-dimensional OU/Fokker–Planck heat bath at elapsed time \(\tau\ge0\). The bound holds uniformly over all bath times, including \(\tau=0\).

## Proof

**Hermite reduction.** Write \(\epsilon=aq^2\) and \(z=t(1-t)\), \(S=1-2z\). Then \(0<\epsilon\le1/100\), \(0<z\le1/4\), and \(1/2\le S<1\). Multiplication of the two Gaussian-characteristic-function/Hermite generating functions gives the *exact* density \(\phi R\), where
\[
R=1+w,\quad w=\epsilon SA+\epsilon^2z^2B.
\]
Equivalently, this follows by expanding the independent Gaussian fourth-chaos perturbations: the two fourth-order contributions combine with coefficient \(\epsilon[(1-t)^2+t^2]=\epsilon S\), and their product creates precisely the eighth-order term \(\epsilon^2[t(1-t)]^2B\). The independent factors are each at least \(1-6\epsilon\), and the output is their conditional Gaussian projection, hence
\[
R(x)\ge m:=(1-6\epsilon)^2\ge(47/50)^2>0.
\]
This positivity is pointwise, not merely an integrated estimate. The output has unit variance; its entropy is \(h(\phi)-D(z)\), where \(D(z)=\mathbb E_\phi[R\log R]\).

**Exact differential identities.** With \(w_z=-2\epsilon A+2\epsilon^2zB\) and \(w_{zz}=2\epsilon^2B\), and Gaussian expectation denoted by \(\mathbb E\), differentiation under the integral (valid from polynomial tails and \(R\ge m\)) gives
\[
D_z=\mathbb E[w_z\log(1+w)],\qquad
D_{zz}=\mathbb E\!\left[\frac{w_z^2}{R}\right]+2\epsilon^2\mathbb E[B\log R].
\]
Since \(z_t=1-2t\) and \(z_{tt}=-2\),
\[
F_{tt}=2D_z-(1-4z)D_{zz}.
\]
It therefore suffices to prove \(D_z\le-7\epsilon^2S\) and \(D_{zz}>0\).

**Exact moments and strict Cauchy ceilings.** Direct Gaussian moment evaluation gives
\[
\begin{gathered}
\mathbb EA^2=24,\quad \mathbb EA^3=1728,\quad \mathbb EA^4=368064,\quad
\mathbb EB^2=40320,\\
\mathbb EB^4=3507873984921600,\quad \mathbb EAB=0,\quad
\mathbb EA^2B=40320,\quad \mathbb EA^2B^2=10115159040.
\end{gathered}
\]
By Cauchy–Schwarz these yield the following *strict* integer ceilings:
\[
\begin{aligned}
\mathbb E|A|^3&<2973, & \mathbb EA^2|B|&<121821,\\
\mathbb E|A|B^2&<20195129, & \mathbb E|B|^3&<11892749013.
\end{aligned}
\]
All moment integers and strict square-root comparisons are re-evaluated exactly by the accompanying standard-library Python script; they do not depend on numerical quadrature.

**Negative first derivative.** Since \(R\ge m\), the scalar Taylor bound \(|\log(1+w)-w|\le w^2/(2m)\) holds for every \(w>-1\) with \(1+w\ge m\) (integrate \(s/(1+s)\)). Orthogonality gives
\[
\mathbb E[ww_z]=-48\epsilon^2S+80640\epsilon^4z^3.
\]
Writing the four absolute-moment ceilings as \(C_{30},C_{21},C_{12},C_{03}\) in their displayed order, expansion of \(w_z w^2\) yields
\[
\left|D_z-\mathbb E[ww_z]\right|
\le\frac{\epsilon^3}{m}\bigl[S^2C_{30}+\epsilon(zS^2+2Sz^2)C_{21}
+\epsilon^2(2Sz^3+z^4)C_{12}+\epsilon^3 z^5C_{03}\bigr].
\]
The elementary interval bounds \(S^2\le S\), \(zS^2+2Sz^2\le3S/8\), \(2Sz^3+z^4\le5S/128\), and \(z^5\le S/512\) imply, at the worst case \(\epsilon=1/100\),
\[
\frac{|D_z-\mathbb E[ww_z]|}{\epsilon^2S}
\le \frac{(1/100)}{(47/50)^2}
\left[2973+\frac{3(1/100)}8\,121821
+\frac{5(1/100)^2}{128}\,20195129
+\frac{(1/100)^3}{512}\,11892749013\right]
=\frac{1808355327013}{45240320000}<40.
\]
This upper bound is monotone in \(\epsilon\in(0,1/100]\). Further \(80640\epsilon^2z^3/S\le63/250\), whence
\[
\boxed{D_z/\epsilon^2S<-48+40+63/250<-7.}
\]

**Positive second derivative.** Weighted Cauchy–Schwarz and \(\mathbb E[w_zA]=-48\epsilon\) give
\[
\mathbb E\left[\frac{w_z^2}{R}\right]
\ge \frac{(48\epsilon)^2}{\mathbb E[RA^2]}
=\frac{96\epsilon^2}{1+72\epsilon S+1680\epsilon^2z^2}.
\]
Because \(\mathbb E[Bw]=40320\epsilon^2z^2\ge0\), applying the same logarithmic remainder bound to \(\mathbb E[B\log R]\) yields
\[
\frac{D_{zz}}{\epsilon^2}\ge
\frac{96}{1+72\epsilon S+1680\epsilon^2z^2}
-\frac{\epsilon^2}{m}\left[S^2C_{21}+2\epsilon Sz^2C_{12}+\epsilon^2z^4C_{03}\right].
\]
The first term is \(>3840/73\), while the magnitude of the second is at most
\[
\frac{(1/100)^2}{(47/50)^2}
\left[121821+\frac{(1/100)}8\,20195129
+\frac{(1/100)^2}{256}\,11892749013\right]
=\frac{388378921813}{22620160000}<18.
\]
Therefore \(D_{zz}/\epsilon^2>3840/73-18>34>0\). As \(1-4z\ge0\), combine the identities:
\[
F_{tt}=2D_z-(1-4z)D_{zz}<-14\epsilon^2S\le-7\epsilon^2.
\]
Substituting \(\epsilon=aq^2\) proves the theorem, including the endpoints \(q=1\) and \(t=1/2\) (the curvature in \(t\) is assessed at interior \(t\), not at \(t=0,1\)).

## Verification

Run `python verify.py` using Python's standard library. It reconstructs the probabilists' Hermite polynomials, evaluates all eight Gaussian moments by exact integer arithmetic, validates the four Cauchy ceilings, and checks the two rational global curvature certificates using exact fractions. The analytic step bounding logarithmic remainders and the Hermite convolution identity are stated and proved above; a finite script does not replace their universal proof.

## Relationship to prior work

Abu-Ajamieh, arXiv:2610.22386v1 (submitted 2026-10-12), Section 8, establishes strict concavity for this same positive fourth-Hermite family only in the strong smoothing range \(0<q\le5/8\), with bound \(F''\le-(aq^2)^2/10\). The new bound applies up to effective Hermite amplitude \(\epsilon=aq^2=1/100\), including the unsmoothed endpoint. **Implication check:** the source's result, although written for \(q\le5/8\), already extends by reparametrization to every effective amplitude \(\epsilon\le(5/8)^2/100=1/256\), even when the displayed noise parameter is \(q=1\): the resulting mixed density depends only on \(\epsilon\). The genuinely new range is therefore \(1/256<\epsilon\le1/100\), including unsmoothed inputs of amplitude greater than \(1/256\). This is a new *amplitude* region rather than novelty for every parameter point with \(q>5/8\). The original theorem for \(q\le5/8\) is prior art, not a new discovery. The Ball–Nayar–Tkocz conjecture is broader and remains open in general; Luo's 2026 related counterexamples address different families. General Gaussian-scale-mixture entropy concavity (Eskenazis–Gavalakis) does not cover this density: the Hermite-eight coefficient of the input is zero whereas the Hermite-four coefficient is positive, which is incompatible with a nonconstant Gaussian variance mixture. No claim of literature-wide priority certification or general symmetry-class resolution is made.

## Limitations

Only the explicitly defined positive fourth-Hermite perturbations with \(0<a\le1/100\) are covered, for independent copies and standard Gaussian smoothing. The constant \(7\) and amplitude limit \(1/100\) are conservative, not claimed optimal; no claim is made for negative perturbations, arbitrary symmetric densities, non-Gaussian baths, other entropy functionals, or dependent copies. The proof gives a uniform analytic curvature certificate, without claiming an optimal constant.

## References

1. F. Abu-Ajamieh, *Noise-Induced Restoration of Entropy Concavity Near Gaussian Equilibrium*, arXiv:2610.22386v1 (first public 2026-10-12), particularly Section 8, https://arxiv.org/abs/2610.22386.
2. K. Ball, P. Nayar, T. Tkocz, *A reverse entropy power inequality for log-concave random vectors*, arXiv:1509.05926, https://arxiv.org/abs/1509.05926.
3. C. Luo, work on entropy concavity for weighted sums of symmetric variables, arXiv:2609.11418 (2026), https://arxiv.org/abs/2609.11418.
4. A. Eskenazis and L. Gavalakis, *Entropy power inequalities for Gaussian mixtures*, arXiv:2308.15997, https://arxiv.org/abs/2308.15997.
