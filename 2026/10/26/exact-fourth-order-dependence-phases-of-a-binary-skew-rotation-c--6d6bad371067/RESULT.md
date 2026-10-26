# Exact fourth-order dependence phases of a binary skew-rotation coding

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\), let \(\alpha\in\mathbb R\), and give \(\mathbb T^2\) Haar probability measure. Define the affine skew rotation
\[
T_\alpha(x,y)=(x+y,y+\alpha)\pmod 1,
\]
and the stationary binary sign process \(Z_n=s(\pi_1T_\alpha^n(x,y))\), where \(s(u)=1\) on \([0,1/2)\) and \(s(u)=-1\) on \([1/2,1)\).

Every collection of at most three **distinct-time** observations \(Z_{n_1},Z_{n_2},Z_{n_3}\) is a family of independent fair signs, for every real \(\alpha\). For four consecutive times the entire joint law is
\[
\Pr(Z_0=e_0,\ldots,Z_3=e_3)
=\frac{1+C(\alpha)e_0e_1e_2e_3}{16}
\quad(e_j\in\{-1,1\}),
\]
where \(d(\alpha)=\operatorname{dist}(\alpha,\tfrac12\mathbb Z)\in[0,1/4]\) and
\[
\boxed{C(\alpha)=\frac13-16d(\alpha)^2
+48\bigl(d(\alpha)-\tfrac16\bigr)_+^2.}
\]
The four consecutive signs are independent and fair **if and only if**
\[
\boxed{\alpha\equiv\pm\sqrt3/12\pmod{1/2}.}
\]
These exceptional parameters are irrational. The process has measure-theoretic entropy zero for every \(\alpha\), including the exceptional parameters. The fourth-order correlation takes every value in \([-1/3,1/3]\), with maxima at \(\alpha\in\tfrac12\mathbb Z\) and minima at \(\alpha\in\tfrac14+\tfrac12\mathbb Z\).

## Assumptions and scope
The probability is Haar measure on the two-torus, rather than the orbit law of a prescribed starting point. The transformation is invertible and preserves Haar measure. The single-observation coordinate is the **first** coordinate of \(T_\alpha^n\), and the coding threshold is exactly one half. The independence statement allows arbitrary distinct integer observation times, whereas the explicit fourth-order law concerns four **consecutive** times. No conclusion about arbitrary quadruples or independence of all finite-dimensional distributions is claimed.

The identity
\[
\pi_1T_\alpha^n(x,y)=x+ny+\tbinom n2\alpha\pmod1
\]
holds for all integers \(n\), including negative integers by invertibility.

## Proof
**I. Complete independence for up to three observation times.** The Fourier coefficients of the half-circle sign \(s\) vanish at frequency zero and at all even frequencies. Approximate \(s\) by its bounded Fejér trigonometric approximations in \(L^1(\mathbb T)\). A nonzero Fourier summand in a product of \(m\) observations has \(m\) nonzero **odd** integer frequencies \(k_j\). Integration over the independent Haar variables \(x,y\) requires
\[
\sum_j k_j=0,\qquad \sum_j n_jk_j=0.
\]
For \(m=1\) the first equation is impossible. For \(m=2\) at distinct times the two equations force both frequencies zero. For \(m=3\), a sum of three odd integers cannot vanish. All nonempty Walsh moments of any collection of at most three distinct times consequently vanish. Fourier approximation is justified because the approximants are uniformly bounded and converge in \(L^1\); hence the corresponding finite products converge in \(L^1\). Vanishing of these Walsh moments is equivalent to the uniform product distribution.

**II. Reduction of the consecutive four-word law.** Fourier/Walsh inversion of the four signs uses the vanishing just proved: only the empty subset and the full four-element subset remain. Define
\[
C(\alpha)=\int_0^1\!\int_0^1\prod_{j=0}^3 s\bigl(x+jy+\tbinom j2\alpha\bigr)\,dx\,dy.
\]
Translation of \(\alpha\) by \(1/2\) flips the two factors with \(j=2,3\) and leaves their product unchanged. Simultaneous negation of \(x,y,\alpha\), using \(s(-u)=-s(u)\) almost everywhere, leaves a product of four signs unchanged. These operations prove that \(C\) is periodic with period \(1/2\) and even. It remains to compute it for \(a\in[0,1/4]\).

**III. Exact polyhedral evaluation.** Regard \((x,y,a)\) as ranging over \([0,1]^2\times[0,1/4]\). The only discontinuity hyperplanes of the integrand are
\[
 x+jy+\tbinom j2 a=\ell/2
\quad(j=0,1,2,3;\ \ell\in\mathbb Z),
\]
plus the boundaries of the square in \(x,y\). Only finitely many levels \(\ell\) meet this bounded prism. Every change in the planar polygonal subdivision as \(a\) varies must occur at a triple intersection of these planes (including square boundary planes), unless coincident/parallel planes persist; those do not change the subdivision. Exact three-by-three determinant enumeration of all such intersections inside the prism gives only \(a=0,1/6,1/4\). On either open interval \((0,1/6)\) or \((1/6,1/4)\), every cell has a constant sign and affine-in-\(a\) vertices; the signed sum of its polygonal areas is therefore a polynomial of degree at most two in \(a\).

The provided self-contained `verify.py` implements two independent finite constructions: (1) exact determinant enumeration of every possible critical parameter, and (2) for any rational parameter, exact integration by splitting \(y\) at every crossing of two \(x\)-discontinuity points and at every wraparound. Between such crossings the \(x\)-averaged sign product is affine in \(y\), so the rational midpoint quadrature on each interval is **exact**, not a numerical approximation. Exact evaluations at three distinct rational points in each parameter interval and at every endpoint yield
\[
C(a)=
\begin{cases}
\frac13-16a^2,&0\le a\le\frac16,\\
\frac13-16a^2+48(a-\frac16)^2,&\frac16\le a\le\frac14.
\end{cases}
\]
Since both expressions are quadratic and the possible knot set is exhaustive, these finitely checked rational identities establish the formula for **all real** parameters, not just sampled values. The determinant and rational-integration algorithms and their completeness arguments are printed explicitly in the verifier, so the calculation does not depend on opaque numerical evidence.

**IV. Exceptional parameters, extrema and entropy.** On \([0,1/6]\), the formula has precisely one zero, \(a=\sqrt3/12\). On \([1/6,1/4]\), it decreases from \(-1/9\) to \(-1/3\), so there are no more zeros. Its derivative is negative on \((0,1/4)\), except at the right endpoint, giving the stated extrema. By the four-word formula, vanishing of \(C\) is exactly four-block independence.

Finally \(T_\alpha^n(x,y)=(x+ny+\tbinom n2\alpha,y+n\alpha)\). Its Bowen balls for fixed precision have covering number \(O_\varepsilon(n)\): using cells of width \(O(\varepsilon)\) in \(x\) and \(O(\varepsilon/n)\) in \(y\) controls the first \(n\) iterates. Thus its topological entropy is zero; the Haar measure entropy and entropy of every symbolic factor are also zero. This argument applies equally at rational and irrational \(\alpha\).

## Verification
Run `python3 verify.py` with the Python standard library. It proves that the only possible parameter subdivision knots are exactly `0,1/6,1/4`, checks six interior rational evaluations (three per interval), checks all three boundary evaluations, and confirms the candidate formula by exact rational arithmetic. It reports `VERIFY_OK`. There are no random samples, floating-point tolerances, external solvers, finite-orbit extrapolations or unpublished external data in the certificate. The analytic Fourier argument and quadratic-cell argument are essential parts of the proof and are not replaceable by the checker alone.

## Relationship to prior work
Host and Kra, *Analysis of two step nilsequences* (first arXiv version 20 September 2007), Section 2.3, explicitly discusses the underlying affine two-torus skew transformation and quadratic orbit observables. Bergelson, Host, Kra and Ruzsa, *Multiple recurrence and nilsequences* (manuscript dated 4 May 2004), Sections 1 and 4, treats higher-order correlations in broad measure-preserving systems. Those general frameworks do not state the exact half-circle sign coding law, its unique quadratic knot, or its isolated irrational four-block independence phases. The earlier same-topic computation for a **four-dimensional**, rather than two-dimensional, unipotent toral sign coding establishes a different consecutive-block uniformity statement and does not imply the present four-point phase formula. The classical parity/Fourier argument for lower-order independence is used here, not claimed as independently novel; the claimed finding is its combination with the exact four-point law and phase classification.

## Limitations
Only the particular half-circle binary coding and four consecutive observations are analyzed explicitly. All parameter values are allowed, but no claim is made that a four-block-independent stationary process is Bernoulli; indeed its entropy is zero. The new formula is proved with an exact finite rational certificate plus mathematical completeness arguments, not an independent formal proof assistant. An earlier equivalent closed formula outside the inspected indexed literature remains a residual historical-priority risk. No independent scientific audit has been performed.

## References
1. B. Host and B. Kra, *Analysis of two step nilsequences*, arXiv:0709.3241v1, first submitted 2007-09-20, Section 2.3, https://arxiv.org/html/0709.3241v1.
2. V. Bergelson, B. Host and B. Kra, with an appendix by I. Ruzsa, *Multiple recurrence and nilsequences*, manuscript dated 2004-05-04, https://sites.math.northwestern.edu/~kra/papers/synd.pdf; published in *Inventiones Mathematicae* 160 (2005), 261–303, DOI:10.1007/s00222-004-0428-6.
