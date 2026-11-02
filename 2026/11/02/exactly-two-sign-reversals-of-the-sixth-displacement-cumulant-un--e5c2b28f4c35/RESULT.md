# Exactly two sign reversals of the sixth displacement cumulant under orientational resetting

## Finding

For a freely translating planar active Brownian particle with Poissonian resetting of **orientation only**, the long-time sixth cumulant rate of displacement parallel to the resetting direction has **exactly two, simple, positive sign-reversal thresholds** as the resetting rate is varied. This gives a reentrant positive–negative–positive classification, while independent isotropic translational Brownian noise leaves both thresholds unchanged.

Let the angular diffusivity be \(d>0\), reset rate \(r>0\), propulsion speed \(v>0\), and independent translational diffusivity \(D_T\ge0\). Put \(q=r/d\) and let \(\kappa_6(X_t)\) denote the sixth ordinary cumulant of longitudinal displacement. Then the limit exists and equals

\[
\lim_{t\to\infty}\frac{\kappa_6(X_t)}t
=\frac{4320v^6}{d^5}\,
\frac{P(q)}{(q+1)^{11}(q+4)^5(q+9)^4(q+16)^3(q+25)^2(q+36)},
\]

where \(P(q)=\sum_{j=0}^{15}c_jq^j\), with the following integer coefficients **in ascending order**:

```text
j : c_j
 0 : 20782448640000
 1 : 181236700108800
 2 : 54861583665024
 3 : -2573265668397984
 4 : -6219315460897056
 5 : -3549159799788784
 6 : 790599382490714
 7 : 1743348986439210
 8 : 891840550099254
 9 : 249919114303995
10 : 43934398967304
11 : 5036657759205
12 : 375256499910
13 : 17440408989
14 : 456634850
15 : 5106569
```

The polynomial has exactly two positive roots \(q_-<q_+\), both simple, in the exact rational isolating intervals

\[
\frac14<q_-<\frac{13}{50},\qquad \frac{29}{20}<q_+<\frac32.
\]

Numerically they are \(q_-=0.2525378162813238\ldots\) and \(q_+=1.4515226679631110\ldots\). The sixth-cumulant rate is strictly positive for \(0<q<q_-\), strictly negative for \(q_-<q<q_+\), and strictly positive for \(q>q_+\), with zeros only at these two thresholds. All statements hold at any finite \(D_T\ge0\).

## Assumptions and scope

Consider an angle \(\Theta_t\in\mathbb R/(2\pi\mathbb Z)\) undergoing rotational Brownian diffusion \(d\Theta_t=\sqrt{2d}\,dW_t\) between independent Poisson events of rate \(r\), at which it is instantly set to angle zero. The position is **not reset**. Let

\[
X_t=v\int_0^t\cos\Theta_s\,ds+\sqrt{2D_T}\,B_t,
\]

where \(B\) and \(W\) are independent standard Brownian motions, independent of the reset clock. The result concerns the long-time cumulant growth rate, not finite-time cumulant signs. The initial angular law may be stationary or arbitrary: the simple principal eigenvalue gives the same limiting growth rate.

The first-public source is Baouche, Franosch, Meiners, and Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769v1, publicly dated 2024-05-10. The present result uses that physical model, but not a claimed novelty in defining orientation-only resetting, its renewal representation, or its previously computed first through fourth displacement moments.

## Proof

**1. Principal eigenvalue and cumulant growth.** After scaling time by \(d\), the angular generator, tilted by longitudinal propulsion, is

\[
(\mathcal L_z f)(\theta)=f''(\theta)+q[f(0)-f(\theta)]+z\cos\theta\,f(\theta).
\]

At \(z=0\) the Markov generator has a simple zero eigenvalue and a spectral gap. Bounded analytic perturbation therefore gives a simple analytic principal eigenvalue \(\phi_q(z)\) near zero, with \(\phi_q(0)=0\). Feynman–Kac and spectral isolation imply, uniformly in a small complex neighborhood of zero, that the longitudinal scaled cumulant-generating function is

\[
\lim_{t\to\infty}\frac1t\log\mathbb E[e^{kX_t}]
=D_Tk^2+d\,\phi_q(vk/d).
\]

The same analytic spectral expansion justifies differentiation through the long-time limit up to the sixth order. In particular, because independent Gaussian displacement contributes only a quadratic term,

\[
\lim_{t\to\infty}\frac{\kappa_6(X_t)}t
=\frac{v^6}{d^5}\,\phi_q^{(6)}(0),
\]

independently of \(D_T\).

**2. Exact six-mode finite recursion.** Normalize the positive left principal eigenmeasure to total mass one, and let \(a_n(z)\) denote its \(n\)th complex angular Fourier moment. Reflection symmetry makes \(a_{-n}(z)=a_n(z)\), and \(a_0(z)=1\). Taking Fourier test functions in the adjoint eigenvalue equation gives

\[
\phi_q(z)=za_1(z),\qquad
(q+n^2+\phi_q(z))a_n(z)
=q+\frac z2\bigl(a_{n-1}(z)+a_{n+1}(z)\bigr)\quad(n\ge1).
\]

Write \(a_n(z)=\sum_{j\ge0}a_{n,j}z^j\), \(\phi_q(z)=\sum_{j\ge1}b_jz^j\), with

\[
a_{0,0}=1,\quad a_{0,j}=0\ (j>0),\quad
 a_{n,0}=\frac{q}{q+n^2}\ (n\ge1),\quad b_j=a_{1,j-1}.
\]

For \(n,j\ge1\), coefficient comparison yields the purely rational recurrence

\[
a_{n,j}=\frac{\frac12(a_{n-1,j-1}+a_{n+1,j-1})
-\sum_{p=1}^{j}b_p a_{n,j-p}}{q+n^2}.
\]

To obtain \(b_6=a_{1,5}\), this recurrence uses only the finite triangular array \(n+j\le6\). It is therefore an **exact finite computation of an infinite-dimensional perturbative coefficient**, not an uncontrolled Fourier cutoff. Simplifying \(6!b_6\) using rational polynomial arithmetic gives exactly \(4320P(q)\) divided by the stated positive denominator. The attached `verify.py` reconstructs the full rational function and checks symbolic identity. As a low-order normalization check, it also recovers

\[
\phi_q''(0)=\frac{10q+4}{(q+1)^3(q+4)},
\]

in agreement with the diffusion coefficient obtained from the previously known second moment. The zero-reset limit of the sixth coefficient is \(145\), again providing a useful independent parameter-boundary check.

**3. Complete positive-root certificate.** The descending coefficient sequence of \(P\) has exactly two sign changes: one when passing from the positive high-degree terms to three consecutive negative coefficients, and a second when passing back to the three positive low-degree coefficients. Descartes' rule of signs gives at most two positive roots, **counted with multiplicity**. Direct exact integer/rational evaluations give

\[
P(1/4)>0,\quad P(13/50)<0,\qquad
P(29/20)<0,\quad P(3/2)>0.
\]

The intermediate value theorem supplies a positive root in each disjoint interval. The Descartes upper bound forces these to be the only positive roots, and forces both to be simple. Since the denominator is strictly positive for \(q>0\), continuity and these sign certificates prove the complete positive–negative–positive classification.

## Verification

From this directory, install the dependencies in `requirements.txt` and run `python verify.py`. The script reconstructs every coefficient needed for the sixth scaled cumulant with exact SymPy rational arithmetic and verifies equality with the reported polynomial. It checks the exact Descartes sign count, four rational bracket inequalities, and the exact zero-reset limit. It also independently diagonalizes a finite Fourier approximation of the tilted operator at five positive reset-rate ratios and evaluates its sixth analytic Taylor coefficient through a complex Cauchy integral. All five comparisons agree to the stated finite numerical tolerance. **Finite-dimensional spectral calculations are diagnostic only; the exact finite-mode coefficient recursion and Descartes argument supply the proof.** No random seed or third-party paper text is required.

## Relationship to prior work

Baouche et al. (2024) analyze precisely the orientation-only resetting model by renewal equations and the intermediate scattering function; their presented explicit time-dependent moment formulas stop at fourth order, with attention to variance, skewness, and non-Gaussianity. Their general transform can provide an alternative starting point, but it does not state or directly establish a sixth-cumulant global sign count. Kumar, Sadekar, and Basu (2020) earlier analyze orientation-only resetting, focusing on short-time distributions and lower moments; the long-time sixth-cumulant transition is not in their studied claims. Chaki, Olsen, and Löwen (2024) investigate *passive* shape-anisotropic Brownian particles under orientation resetting, with a different displacement mechanism and effective diffusion tensor. General additive-functional and spectral-tilting theories justify parts of the method but do not by themselves give this explicit model-specific polynomial and its exactly-two-positive-root classification.

## Limitations

The observation is a long-time single-particle cumulant rate. Its sign is not a density-positivity criterion, a finite-time sign assertion, or a claim about the transverse displacement cumulant. Experimental cumulant estimates may be noisy, especially at high order. The theorem assumes fixed-speed propulsion, isotropic independent translational diffusion, angular Brownian motion, instantaneous complete orientation resetting, and Poissonian reset times. Neither random resetting angles nor general waiting-time laws are addressed. The exact threshold positions are not asserted to be novel under every alternative mathematical representation; broader unindexed spectral/renewal literature could contain equivalent expressions and warrants independent priority verification.

## References

1. Y. Baouche, T. Franosch, M. Meiners, C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769v1 (2024-05-10), https://arxiv.org/html/2405.06769v1 .
2. V. Kumar, O. Sadekar, U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294v1 (2020-08-07), https://arxiv.org/html/2008.03294v1 .
3. S. Chaki, K. S. Olsen, H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v1 (2024-06-25), https://arxiv.org/html/2406.17550v1 .
4. F. den Hollander, S. N. Majumdar, J. M. Meylahn, H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909 (2018), https://arxiv.org/abs/1801.09909 .
