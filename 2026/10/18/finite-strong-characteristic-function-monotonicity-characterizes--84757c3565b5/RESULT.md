# Finite strong characteristic-function monotonicity characterizes Bernoulli sums

## Finding
Let \(X\) be any integer-valued random variable with **finite, nonempty support**. As in Aamand–Alon–Houen–Thorup, call \(X\) *monotone* if the modulus of its characteristic function is nonincreasing on \([0,\pi]\), and *strongly monotone* if every exponential tilt is monotone. The following conditions are equivalent:

1. \(X\) is strongly monotone.
2. After extracting the smallest-support integer power, the probability-generating polynomial of \(X\) has only strictly negative real zeros (the constant case is allowed).
3. There are independent Bernoulli variables \(B_1,\ldots,B_m\), with success probabilities strictly between zero and one, such that \(X\) has the same law as \(a+\sum_{j=1}^{m}B_j\), where \(a=\min\operatorname{supp}X\) and \(m=\max\operatorname{supp}X-a\).

Thus among finitely supported integer laws the strong-monotonicity hypothesis is **exactly** a shifted Poisson-binomial condition; there are no additional bounded-support examples. If \(m\ge1\), the characteristic-function modulus of every exponential tilt is strictly decreasing on \((0,\pi)\).

Ordinary monotonicity is genuinely weaker. For a three-atom law with strictly positive masses \((p_0,p_1,p_2)\) on consecutive integers, ordinary monotonicity holds exactly when
\[
p_1(p_0+p_2)\ge4p_0p_2,
\]
whereas strong monotonicity holds exactly when
\[
p_1^2\ge4p_0p_2.
\]
In particular, the probabilities \((8,7,2)/17\) give an ordinarily monotone but not strongly monotone law.

## Assumptions and scope
The support is a finite subset of \(\mathbb Z\); no initial consecutiveness or strict positivity of intermediate masses is assumed. Put \(a=\min\operatorname{supp}X\), \(m=\max\operatorname{supp}X-a\), and
\[
H(z)=\sum_{k=0}^{m}\Pr(X=a+k)z^k.
\]
Then \(H(1)=1\), its leading and constant coefficients are positive, and all its coefficients are nonnegative. An exponential tilt with parameter \(\theta\in\mathbb R\) has masses proportional to \(e^{\theta x}\Pr(X=x)\). Finite support ensures that every real tilt is defined. The case \(m=0\) means a point mass, a vacuous product of Bernoulli variables, and a constant polynomial with no zeros.

## Proof
For \(r=e^\theta>0\), the characteristic function of the tilted law is
\[
\varphi_\theta(t)=e^{iat}\frac{H(re^{it})}{H(r)}.
\]
Since \(H(r)>0\), strong monotonicity is equivalent to: for **every** \(r>0\), the function \(t\mapsto|H(re^{it})|\) is nonincreasing on \([0,\pi]\).

Suppose that \(H\) has a nonreal zero \(\zeta\) in the open upper half-plane. Write \(\zeta=re^{it_0}\) with \(r>0\) and \(0<t_0<\pi\). On that circle the modulus is zero at \(t_0\). Since the modulus is nonnegative and hypothesized nonincreasing, it must be identically zero for every \(t\in[t_0,\pi]\). This gives infinitely many distinct zeros of the nonzero polynomial \(H\), a contradiction. Real coefficients pair nonreal zeros by conjugation, so all zeros are real. As \(H(s)>0\) for every \(s\ge0\), all zeros are strictly negative. This proves (1) implies (2), including the possibility that some intermediate probability masses vanish (which the conclusion automatically excludes unless \(m=0\)).

If \(m\ge1\), write the roots as \(-\lambda_1,\ldots,-\lambda_m\), with every \(\lambda_j>0\). The normalization at \(z=1\) gives
\[
H(z)=\prod_{j=1}^{m}\frac{\lambda_j+z}{1+\lambda_j}
=\prod_{j=1}^{m}((1-q_j)+q_j z),
\qquad q_j=(1+\lambda_j)^{-1}\in(0,1).
\]
This is the generating polynomial of a sum of independent Bernoulli variables, establishing (2) implies (3). Conversely, under tilt \(r\), each Bernoulli parameter becomes
\[
q_j(r)=\frac{r q_j}{1-q_j+r q_j}\in(0,1).
\]
For \(0<t<\pi\),
\[
\frac{d}{dt}\big|1-q_j(r)+q_j(r)e^{it}\big|^2
=-2q_j(r)(1-q_j(r))\sin t<0.
\]
Each modulus is positive on the open interval; their product is therefore strictly decreasing there. Thus (3) implies (1), and the strictness assertion follows. The point-mass case is constant and satisfies all three conditions.

For the three-atom distinction, let the masses be \(p_0,p_1,p_2>0\), summing to one, and set \(u=\cos t\). Direct multiplication gives
\[
|p_0+p_1e^{it}+p_2e^{2it}|^2
=p_0^2+p_1^2+p_2^2-2p_0p_2+2p_1(p_0+p_2)u+4p_0p_2u^2.
\]
The derivative with respect to \(u\) is \(2p_1(p_0+p_2)+8p_0p_2u\), increasing in \(u\) and minimized on \([-1,1]\) at \(u=-1\). As \(u=\cos t\) decreases along \([0,\pi]\), the squared modulus is nonincreasing in \(t\) exactly when \(p_1(p_0+p_2)\ge4p_0p_2\). (This also handles zeros of the modulus without differentiating its square root.) The quadratic generating polynomial has two real roots exactly when its discriminant \(p_1^2-4p_0p_2\) is nonnegative, giving the strong criterion by the established equivalence.

For masses \((8,7,2)/17\), the weak inequality has integer margin \(7(8+2)-4\cdot8\cdot2=6>0\), but the quadratic discriminant numerator is \(7^2-4\cdot8\cdot2=-15\). Indeed, tilt by \(r=2\) gives the polynomial \((4+7z+4z^2)/15\), which vanishes at \(z=(-7+i\sqrt{15})/8\) on the upper unit circle; at \(z=-1\) its value is \(1/15\). Hence the tilted modulus falls to zero before \(\pi\) and then rises, explicitly violating monotonicity.

## Verification
All logical implications are symbolic and apply to arbitrary finite support and real probabilities. The included standalone script `check.py` verifies the exact rational three-point margins, the quadratic discriminant, and the nonreal-root witness in \(\mathbb Q(i\sqrt{15})\), as well as a Bernoulli-product illustration. The script is illustrative; the infinite family is certified by the preceding polynomial-root argument, not by enumerated cases. Run with `python3 check.py` using only the Python standard library.

## Relationship to prior work
Aamand, Alon, Houen and Thorup (arXiv:2104.03721, published in *Electronic Communications in Probability* 27, 2022) introduce the two monotonicity notions, prove sufficiency for Bernoulli, geometric and Poisson variables (Lemma 3.1), and apply strong monotonicity to tilted local estimates (Theorem 3.2). Their accessible paper does not give the converse classification for finite support, or the separating three-atom boundary. The classical Aissen–Schoenberg–Whitney real-rootedness/Poisson-binomial equivalence is recorded in Tang and Tang's 2019 survey (Theorem 4.1). The novelty assessed here is the missing **necessity** from the all-tilts Fourier condition, together with the exact distinction from weak monotonicity; neither the standard factorization theorem alone nor the cited sufficiency lemma implies that necessity.

## Limitations
This is a finite-support theorem. It does not characterize strongly monotone laws with infinite support (including the geometric and Poisson laws already known to be examples). Strong monotonicity under every real tilt is essential: a single untilted modulus condition admits non-real-rooted counterexamples. The connection to classical real-rooted polynomials is elementary and may have appeared elsewhere under different terminology; the literature comparison is not an absolute uniqueness certificate.

## References
1. A. Aamand, N. Alon, J. B. T. Houen and M. Thorup, *On Sums of Monotone Random Integer Variables*, *Electronic Communications in Probability* 27 (2022), doi:10.1214/22-ECP500. First public preprint: arXiv:2104.03721 (8 April 2021). Accessible author manuscript: https://web.math.princeton.edu/~nalon/PDFS/sumofmon1.pdf.
2. W. Tang and F. Tang, *The Poisson Binomial Distribution—Old & New*, arXiv:1908.10024 (2019), especially Section 4, Theorem 4.1, giving the Aissen–Schoenberg–Whitney/Edrei characterization.
3. M. Aissen, I. J. Schoenberg and A. M. Whitney, *On the generating functions of totally positive sequences. I*, *Journal d'Analyse Mathématique* 2 (1952), 93–103, doi:10.1007/BF02786970 (classical root-factorization background).
