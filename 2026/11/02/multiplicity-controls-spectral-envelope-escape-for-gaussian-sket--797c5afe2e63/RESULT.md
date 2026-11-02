# Multiplicity controls spectral-envelope escape for Gaussian-sketched Rayleigh quotients

## Finding

**Theorem (exact escape law, sharp multiplicity regime, and overshoot tails).** Let \(p,q,k\) be positive integers. Let \(A\) be any real symmetric matrix on \(\mathbb R^{p+q}\) whose only eigenvalues are \(a<b\), with multiplicities \(p\) and \(q\), respectively. Independently draw a unit vector \(v\) uniformly from the sphere and a \(k\)-by-\((p+q)\) matrix \(S\) of independent standard normal entries. Define the one-dimensional sketched Rayleigh–Ritz estimate and its **spectral-envelope overshoot** by

\[
\widehat\lambda=\frac{(Sv)^{\mathsf T}(SAv)}{\|Sv\|_2^2},\qquad
H=(a-\widehat\lambda)_++(\widehat\lambda-b)_+,\qquad \Delta=b-a>0.
\]

The denominator is nonzero almost surely. Put \(\alpha=q/2\), \(\beta=p/2\), and let \(I_t(\alpha,\beta)\) denote the regularized incomplete beta function. For an independent \(T_k\sim\operatorname{Beta}(1/2,k/2)\), the **exact unconditional escape probability** is

\[
P_{p,q,k}:=\Pr\{H>0\}
=\frac12\mathbb E\left[I_{T_k}(\alpha,\beta)+I_{T_k}(\beta,\alpha)\right].
\]

In particular \(P_{p,q,1}=1/2\) for **every** pair of multiplicities. Let \(r=\min\{p,q\}\), let \(m=2\) if \(p=q\), and \(m=1\) otherwise, and set

\[
B_{p,q}=B(p/2,q/2),\qquad M_j=\mathbb E|Z|^j
=\frac{2^{j/2}\Gamma((j+1)/2)}{\sqrt\pi},\quad Z\sim N(0,1).
\]

For fixed multiplicities \(p,q\), as the number of Gaussian sketch rows \(k\) tends to infinity,

\[
\boxed{P_{p,q,k}\sim \frac{mM_r}{rB_{p,q}}\,k^{-r/2}},\qquad
\boxed{\mathbb EH\sim\frac{m\Delta M_{r+2}}{B_{p,q}(r+1)(r+2)}\,k^{-(r/2+1)}}.
\]

Thus the multiplicity of the smaller extreme eigenspace, rather than the total ambient dimension, governs the rare spectral-escape exponent. For the mean size of a violation,

\[
\boxed{\mathbb E[H\mid H>0]\sim\frac{r}{r+2}\frac{\Delta}{k}}.
\]

For **every fixed** \(k\ge1\), the large-overshoot tail has a sharp positive constant:

\[
\lim_{t\to\infty}(t/\Delta)^k\Pr\{H>t\}
=D_{p,q,k}:=\frac{2\Gamma((k+1)/2)}{k\sqrt\pi\,\Gamma(k/2)}
\frac{B((p+k)/2,(q+k)/2)}{B(p/2,q/2)}.
\]

Therefore, for every \(s>0\),

\[
\mathbb EH^s<\infty\quad\Longleftrightarrow\quad 0<s<k.
\]

In particular, one sketch row gives infinite expected overshoot, while two rows give finite mean overshoot but infinite second moment. This last moment classification concerns the sketched **eigenvalue estimate**, not the reciprocal coefficient of a sketched linear-system solver.

For the planar case \(p=q=1\), write \(U_k=Z/R_k\) with independent \(Z\sim N(0,1)\) and \(R_k\sim\chi_k\). Then

\[
P_{1,1,k}=\frac2\pi\mathbb E[\arctan|U_k|],\qquad
\frac{\mathbb EH}{\Delta}=\frac1\pi\mathbb E[|U_k|-\arctan|U_k|]\quad(k>1).
\]

Consequently \(P_{1,1,2}=1-2/\pi\), \(\mathbb EH/\Delta=2/\pi-1/2\) at \(k=2\), and the large-sketch laws specialize to

\[
P_{1,1,k}\sim \frac{2\sqrt2}{\pi^{3/2}\sqrt k},\qquad
\mathbb EH\sim\frac{2\sqrt2\Delta}{3\pi^{3/2}k^{3/2}}.
\]

## Assumptions and scope

All randomness is real and independent: the trial direction is exactly Haar-uniform and the sketch has independent centered Gaussian entries of a common positive variance (the variance cancels from the quotient). The symmetric operator has **exactly two distinct spectral values** with positive integer multiplicities. The sketch dimension \(k\) may be smaller or larger than the ambient dimension; the limit \(k\to\infty\) holds at fixed \(p,q\), not in a joint high-dimensional limit. All expectations refer to exact arithmetic, with no conditioning on a successful subspace embedding.

A standard unsketched Rayleigh quotient always lies in \([a,b]\). Here the sketch uses a Petrov–Galerkin inner product and can escape that interval even though \(A\) is symmetric and positive definite when \(a>0\).

## Proof

**1. Gaussian quotient representation.** Orthogonal diagonalization and rotational invariance reduce the orientation of \(v\) to the single scalar

\[
W=\|\Pi_b v\|_2^2\sim\operatorname{Beta}(q/2,p/2).
\]

Here \(\Pi_b\) projects onto the eigenspace of \(b\). With probability one \(0<W<1\), and the usual Rayleigh quotient and orthogonal residual satisfy

\[
\rho=v^{\mathsf T}Av=a+\Delta W,\qquad
Av=\rho v+\Delta\sqrt{W(1-W)}\,u,
\]

for a unit vector \(u\) perpendicular to \(v\). Conditional on \(v\), the Gaussian vectors \(Sv\) and \(Su\) are independent standard Gaussian vectors. Consequently

\[
\widehat\lambda=a+\Delta\left(W+\sqrt{W(1-W)}U_k\right),
\quad U_k=Z/R_k,
\]

where \(Z\sim N(0,1)\), \(R_k\sim\chi_k\), and \(U_k\) is independent of \(W\). The well-known Student ratio has density

\[
f_{U_k}(x)=\frac{\Gamma((k+1)/2)}{\sqrt\pi\,\Gamma(k/2)}(1+x^2)^{-(k+1)/2}.
\]

**2. Exact beta escape law.** The estimate falls below \(a\) exactly when \(U_k< -\sqrt{W/(1-W)}\), and exceeds \(b\) exactly when \(U_k>\sqrt{(1-W)/W}\). Conditional on \(|U_k|=u\), the negative and positive signs have probability \(1/2\) each. Set \(T=u^2/(1+u^2)\). The below-\(a\) event is \(W<T\); the above-\(b\) event is \(1-W<T\). Independent chi-squared identities give \(T=T_k\sim\operatorname{Beta}(1/2,k/2)\). Integrating the two beta cumulative probabilities proves the exact displayed law. For \(k=1\), the distribution of \(T\) is symmetric \(\operatorname{Beta}(1/2,1/2)\); alternatively the conditional Cauchy-tail identity gives escape probability \(1/2\) for every \(W\), yielding \(P_{p,q,1}=1/2\).

**3. Sharp escape asymptotics.** For fixed \(\alpha,\beta>0\), as \(t\downarrow0\),

\[
I_t(\alpha,\beta)=\frac{t^\alpha}{\alpha B(\alpha,\beta)}(1+O(t)).
\]

The exact beta moment formula gives

\[
\mathbb ET_k^\alpha=\frac{\Gamma(\alpha+1/2)\Gamma((k+1)/2)}{\sqrt\pi\,\Gamma((k+1)/2+\alpha)}
\sim M_{2\alpha}k^{-\alpha}.
\]

The beta asymptotic can be integrated because the ratio of the incomplete beta function to \(t^\alpha\) is bounded on \([0,1]\), and \(T_k\to0\) in probability. The lower and upper edges therefore contribute \(M_q/(qB_{p,q})k^{-q/2}\) and \(M_p/(pB_{p,q})k^{-p/2}\), respectively, as their own leading terms. Keeping the dominant edge, or adding equal-multiplicity edges, yields the first boxed asymptotic.

**4. Sharp mean overshoot.** For \(u=|U_k|\), the normalized contribution from the lower edge before averaging the sign is

\[
L_{\alpha,\beta}(u)=\frac{1}{B(\alpha,\beta)}
\int_0^{u^2/(1+u^2)}
\left(u\sqrt{w(1-w)}-w\right)w^{\alpha-1}(1-w)^{\beta-1}\,dw.
\]

The corresponding upper-edge function is \(L_{\beta,\alpha}(u)\). Thus

\[
\mathbb EH/\Delta=\frac12\mathbb E\left[L_{\alpha,\beta}(|U_k|)+L_{\beta,\alpha}(|U_k|)\right].
\]

Set \(r=2\alpha\). Scaling \(w=u^2z\) in the first integral gives the sharp local limit

\[
L_{\alpha,\beta}(u)
\sim\frac{2u^{r+2}}{B(\alpha,\beta)(r+1)(r+2)}
\qquad(u\downarrow0).
\]

The endpoint integral also gives a uniform estimate \(0\le L_{\alpha,\beta}(u)\le C u^{r+2}\) for \(0\le u\le1\), with \(r=2\alpha\). For \(u>1\), \(L_{\alpha,\beta}(u)\le u\,\mathbb E\sqrt{W(1-W)}\). For any fixed \(s>r+2\), once \(k>s\), \(\mathbb E|U_k|^s=O(k^{-s/2})\), so the region \(u>1\) is negligible at the target scale. The small-\(u\) estimate, convergence of \(\sqrt{k}U_k\) to a standard normal, and uniform inverse-chi moments justify integrating the local asymptotic. In particular,

\[
\mathbb E|U_k|^{r+2}
=M_{r+2}\,2^{-(r+2)/2}
\frac{\Gamma((k-r-2)/2)}{\Gamma(k/2)}
\sim M_{r+2}k^{-(r+2)/2}.
\]

Combining the two edges yields the second boxed asymptotic. Dividing it by the escape probability and using \(M_{r+2}=(r+1)M_r\) proves the conditional-overshoot law.

**5. Exact fixed-row tail and moments.** For any fixed \(k\), the Student ratio has the one-sided limit

\[
\Pr\{U_k>x\}\sim
\frac{\Gamma((k+1)/2)}{k\sqrt\pi\,\Gamma(k/2)}\,x^{-k}.
\]

Conditioning on \(W\), an overshoot greater than \(t\) requires a positive or negative \(U_k\) exceeding a threshold equal to \(t/[\Delta\sqrt{W(1-W)}]\) plus a nonnegative edge correction. Regular variation and a uniform bound by a multiple of \(x^{-k}\) permit dominated convergence. The two signs contribute equally to leading order, and

\[
\mathbb E[W(1-W)]^{k/2}
=\frac{B((p+k)/2,(q+k)/2)}{B(p/2,q/2)}.
\]

This establishes the sharp constant \(D_{p,q,k}\). Tail integration, including the logarithmically divergent boundary case, proves \(\mathbb EH^s<\infty\) exactly when \(s<k\).

**6. Two-dimensional closed forms.** For \(p=q=1\), write \(W=\sin^2\theta\) with \(\theta\) uniform on \((0,\pi/2)\). Conditional on \(|U_k|=u\), the total angular length of the two escape intervals equals \(\arctan u\), once the random sign is averaged. This gives \(P_{1,1,k}=2\mathbb E\arctan|U_k|/\pi\). Integrating the positive overshoot after the change \(\theta\leftrightarrow\pi/2-\theta\) uses the exact identity

\[
\int_0^{\arctan u}\sin\theta\cos\theta\,(u-\tan\theta)\,d\theta
=\frac{u-\arctan u}{2}.
\]

It yields the planar mean formula. The \(k=2\) constants follow from elementary cosine integrals. The large-\(k\) constants are the already-proved general multiplicity laws at \(p=q=1\).

## Verification

A standalone computational checker, `verify.py`, reconstructs symbolic matrix and angular identities; compares the exact beta-function laws with direct Gaussian sketches in both a planar example and a five-dimensional two-level example; independently evaluates moment integrals, asymptotic constants, and fixed-row tail coefficients; and checks specific finite-row closed forms. Run `python verify.py` with NumPy, SciPy, and SymPy installed. These finite tests are diagnostics. The infinite limits and moment boundaries follow from the analytic argument above, not sampling.

## Relationship to prior work

Nakatsukasa and Tropp introduced sketched Rayleigh–Ritz and analyzed its approximation accuracy; their discussion of symmetric problems notes that sketched projection need not inherit the Hermitian structure. Balabanov and Grigori developed randomized block Krylov and Rayleigh–Ritz methods and explicitly defined the sketched Rayleigh quotient in their supplementary analysis. The Gaussian ratio representation and beta moments are classical, and fixed-direction Student-ratio behavior is not claimed as new. The distinct target here is the **joint Haar trial-direction and Gaussian-sketch law**: its exact spectral-envelope escape probability, sharp extreme-eigenspace-multiplicity exponents, conditional overshoot rate, and fixed-row overshoot-tail constant. Embedding-conditional deterministic guarantees do not specify these unconditional laws. No claim of independent priority certification is made.

## Limitations

The operator has precisely two distinct real eigenvalues, the input is one Haar-uniform trial vector, and the sketch is Gaussian and independent. The results do not prove an analogous multiplicity rule for three or more spectral levels, a multivector Rayleigh–Ritz space, a non-Gaussian sketch, complex arithmetic, or finite-precision implementations. The constants are for the exact spectral interval \([a,b]\), not a confidence region or the residual of an eigenvector. The large-sketch limits hold with multiplicities fixed; at fixed ambient dimension the limit eventually has more sketch rows than ambient coordinates, so it should not be presented as a simultaneous large-scale compression asymptotic. Comparison with specialized unpublished or inaccessible results may alter publication priority.

## References

- Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113, first posted 29 October 2021; especially Section 6 and its symmetric-problem discussion. https://arxiv.org/abs/2111.00113
- O. Balabanov and L. Grigori, *Randomized block Gram-Schmidt process for solution of linear systems and eigenvalue problems*, arXiv:2111.14641, first posted 29 November 2021; especially Section 4.4 and the supplementary sketched-Rayleigh-quotient discussion. https://arxiv.org/abs/2111.14641
- Classical Courant–Fischer min–max principle and beta/chi-square and Student-ratio distribution identities, used as standard background rather than claimed as discoveries.
