# Universal critical relaxation amplitudes for uniform-susceptibility multistage epidemics

## Finding
Consider a continuously replenished susceptible population coupled to arbitrarily many non-susceptible stages through a nonnegative, rank-one incidence term. At the exact basic reproduction threshold \(\mathcal R_0=1\), every initial condition having any potentially transmitting population exhibits an explicit algebraic profile:
\[
\begin{aligned}
\lim_{t\to\infty}t x(t)&=\mu S_*^2d q,\\
\lim_{t\to\infty}t[S_*-S(t)]&=S_*^2d,\\
\lim_{t\to\infty}t\lambda(t)&=\mu S_*d,\\
\lim_{T\to\infty}\frac{\int_0^T S(t)\lambda(t)\,dt}{\log T}&=\mu S_*^2d.
\end{aligned}
\]
Here \(\lambda(t)=\beta^{\mathsf T}x(t)\), \(q=M^{-1}P\), and \(d=\beta^{\mathsf T}M^{-2}P>0\). These coefficients are independent of the initial condition, and the last limit shows logarithmically divergent cumulative incidence despite vanishing prevalence. Precisely the initial states with \(\ell^{\mathsf T}x(0)=0\), where \(\ell^{\mathsf T}=\beta^{\mathsf T}M^{-1}\), exhibit no transmission and decay exponentially instead. The dichotomy allows reducible stage-transfer networks.

## Assumptions and scope
Fix an integer \(n\ge1\). Assume recruitment \(\nu>0\), susceptible per-capita removal \(\mu>0\), a nonnegative probability vector \(P\in\mathbb R^n\) with \(\sum_jP_j=1\), and a nonzero nonnegative transmission vector \(\beta\in\mathbb R^n\). Let \(M\in\mathbb R^{n\times n}\) have nonpositive off-diagonal entries and a strictly positive sum in every column, denoted by \(\mu_j>0\). In particular \(-M\) is a Metzler generator with strict loss from each stage; no irreducibility or graph reachability is needed.

For arbitrary \(S(0)\ge0\), \(x(0)\in[0,\infty)^n\), consider
\[
\dot S=\nu-\mu S-S\lambda,\qquad
\dot x=SP\lambda-Mx,\qquad \lambda=\beta^{\mathsf T}x.
\]
Set \(S_*=\nu/\mu\) and impose the **exact criticality** \(S_*\beta^{\mathsf T}M^{-1}P=1\). Define
\[
q=M^{-1}P,\quad \ell^{\mathsf T}=\beta^{\mathsf T}M^{-1},\quad
d=\ell^{\mathsf T}q=\beta^{\mathsf T}M^{-2}P.
\]
The nonnegative inverse ensures \(q\ge0\) and \(\ell\ge0\). Criticality guarantees \(\beta^{\mathsf T}q=1/S_*>0\) and \(d>0\). Limits of vectors are componentwise; the formula permits \(q_j=0\) (then the corresponding scaled component converges to zero). The logarithmic-incidence statement uses \(T>1\).

## Proof
**Positive global dynamics and attraction.** The semigroup \(e^{-Mt}\) is entrywise nonnegative. As each column sum of \(M\) is \(\mu_j>0\), a comparison of \(N=S+\mathbf1^{\mathsf T}x\) gives \(\dot N\le\nu-mN\), where \(m=\min(\mu,\mu_1,\ldots,\mu_n)>0\). Thus solutions are global and bounded in the nonnegative cone. Moreover \(S(t)>0\) for every \(t>0\).

At criticality put \(w=\ell^{\mathsf T}x\). Since \(\ell^{\mathsf T}M=\beta^{\mathsf T}\) and \(\ell^{\mathsf T}P=1/S_*\),
\[
\dot w=(S/S_*-1)\lambda.
\]
On the positive-susceptible region, the nonnegative function
\[
\mathcal V(S,x)=S-S_*-S_*\log(S/S_*)+S_*w
\]
has the *exact* derivative
\[
\dot{\mathcal V}=-\mu (S-S_*)^2/S.
\]
Every omega-limit set lies in \(S=S_*\). A full trajectory contained in that set has \(\lambda\equiv0\) from the equation for \(S\); the residual stage dynamics is \(\dot x=-Mx\), whose only bounded complete trajectory is the origin. LaSalle's principle yields \(S(t)\to S_*\) and \(x(t)\to0\). The initial case \(S(0)=0\) is handled by starting the argument at an arbitrary positive time.

**Only one center direction.** The infected-block linearization at the critical disease-free equilibrium is
\[
A=S_*P\beta^{\mathsf T}-M.
\]
Its right and left zero eigenvectors are \(q\) and \(\ell\): \(Aq=0\), \(\ell^{\mathsf T}A=0\), \(\ell^{\mathsf T}q=d>0\). The matrix \(M\) is a nonsingular \(M\)-matrix since its column sums are positive, so the spectrum of \(-M\) lies in the open left half-plane. Every eigenvalue \(z\) of \(A\) with \(\operatorname{Re}z\ge0\) must satisfy the rank-one resolvent identity
\[
1=S_*\beta^{\mathsf T}(M+zI)^{-1}P
=S_*\int_0^\infty e^{-zt}\,\beta^{\mathsf T}e^{-Mt}P\,dt.
\]
The integrand's kernel is nonnegative, continuous, and positive on some nonempty interval, with integral \(1/S_*\). Strict modulus contraction excludes all \(z\ne0\) in the closed right half-plane. Differentiating the scalar characteristic factor at zero gives the strictly positive derivative \(S_*d\), proving algebraic simplicity of zero. The complementary spectral subspace therefore decays exponentially. The spectral projector at zero is \(\Pi=q\ell^{\mathsf T}/d\).

**Asymptotic shape.** For every \(j\) with \(\beta_j>0\), the diagonal of \(M^{-1}\) is positive, so \(\ell_j\ge\beta_j(M^{-1})_{jj}>0\). Thus on the nonnegative cone there exists \(C>0\) with \(0\le\lambda\le Cw\). If \(w(0)>0\), the equation for \(w\) implies \(w(t)>0\) and \((\log w)'=(S/S_*-1)\lambda/w\to0\).

Write \(x=(q/d)w+y\), with \(\ell^{\mathsf T}y=0\), and let \(s=S-S_*\). Then
\[
\dot y=Ay+s(I-\Pi)P\lambda.
\]
The semigroup of \(A\) restricted to \(\ell^{\mathsf T}y=0\) decays exponentially. Variation of constants, \(s(t)\to0\), and the slow-variation estimate \(w(t-v)/w(t)\le e^{\varepsilon v}\) for all sufficiently late times and every fixed small \(\varepsilon>0\), imply \(y(t)/w(t)\to0\) by dominated convergence. Consequently
\[
\frac{x}{w}\longrightarrow\frac qd,
\qquad \frac{\lambda}{w}\longrightarrow\frac1{S_*d}.
\]
Finally \(\dot s=-\mu s-S\lambda\). The same exponential-convolution argument gives \(s/w\to-1/(\mu d)\). Therefore
\[
\frac{\dot w}{w^2}=
\frac1{S_*}\frac{s}{w}\frac{\lambda}{w}
\longrightarrow-\frac1{\mu S_*^2d^2}.
\]
Integrating the derivative of \(1/w\) and dividing by \(t\) proves \(t w(t)\to\mu S_*^2d^2\), and substitution yields the first three limits. As \(tS(t)\lambda(t)\to\mu S_*^2d\), elementary integral comparison with \(1/t\) yields the cumulative-incidence limit.

**The silent face.** If \(w(0)=0\), then the inequality \(\lambda\le Cw\) and the scalar equation for \(w\) show \(w(t)\equiv0\) and \(\lambda(t)\equiv0\). Hence \(x(t)=e^{-Mt}x(0)\) decays exponentially and \(S(t)=S_*+[S(0)-S_*]e^{-\mu t}\) exactly. No initial states outside these two cases exist.

## Verification
The supplementary finite diagnostics in `verify.py` check the eigenvector and spectral identities, the critical Lyapunov derivative at sample states, the asymptotic amplitudes for one-, two-, and three-stage models through physical time \(T=200000\), and the silent-stage case. The required Python packages are NumPy and SciPy; run `python3 verify.py`. Each tested transmitting component and susceptible/infectivity amplitude agrees with its proved limit to within the stated numerical tolerance. Numerical tests do not certify the infinite-dimensional parameter family; the proof above supplies the global quantifiers.

## Relationship to prior work
Earn and McCluskey (2025, equations (2)–(7) and the Methods) introduced and globally analyzed the general uniform-susceptibility stage system, including the reproduction-number formula and threshold attraction. Their published theorem is foundational and is *not* claimed as new here. The present contribution is the explicit universal critical-time amplitude, its dependence on the second inverse transfer moment \(d\), the logarithmic cumulative-incidence law, and the exact transmission/silent-face alternative, including transfer networks lacking source accessibility.

Guo, Li, and Shuai (2012) had established global threshold stability for a related multistage disease class, using graph-theoretic Lyapunov methods, but the inspected principal theorems do not provide the above explicit general critical amplitudes. Standard center-manifold analysis predicts a \(1/t\) decay in generic transcritical systems; it does not by itself supply these coefficient formulas or the reducible-network initial-data dichotomy. This is a claim about the inspected literature, not a proof that all earlier mathematical writing lacks an equivalent result.

## Limitations
The formula requires exact threshold equality, bilinear incidence, constant susceptible recruitment and linear stage-transfer losses with positive column sums. The coefficient is not asserted for nonlinear incidence, vital recruitment proportional to total population, delays, multiple susceptible strata, or the supercritical regime. If a component of \(q\) vanishes, the theorem only gives the corresponding vanishing scaled limit, not that component's best exponential/algebraic subleading term. Existing general bifurcation or renewal theory might already imply an equivalent coefficient without using this notation; additional bibliographic inspection could alter the novelty assessment. Only self-review has been performed; no independent audit is claimed.

## References
1. David J. D. Earn and C. Connell McCluskey, *Global stability of epidemic models with uniform susceptibility*, Proceedings of the National Academy of Sciences 122 (2025), e2510156122. Published December 2, 2025. DOI: 10.1073/pnas.2510156122. Open author manuscript: https://arxiv.org/pdf/2512.11003.
2. Hongbin Guo, Michael Y. Li, and Zhisheng Shuai, *Global dynamics of a general class of multistage models for infectious diseases*, SIAM Journal on Applied Mathematics 72 (2012), 261–279. DOI: 10.1137/110827028. Author-hosted full text: https://sites.ualberta.ca/~myli/research/ps_files/multistage_2012.pdf.
