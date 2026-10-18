# Sharp Haar-section oracle efficiency and the one-dimensional barrier

## Finding

Let \(n\ge2\) and \(1\le d\le n\) be integers. Let \(P\in\mathbb R^{d\times n}\) be Haar-distributed among matrices with orthonormal rows. For any distinct unit vectors \(u,v\in\mathbb R^n\), define the boundary-ball random-section Frank–Wolfe efficiency

\[
\Gamma(P;u,v)=\frac{\|Pu\|_2\|Pv\|_2-\langle Pu,Pv\rangle}{1-\langle u,v\rangle}.
\]

**The sharp universal expectation is**

\[
\boxed{\inf_{u,v\in\mathbb S^{n-1},\ u\ne v}\mathbb E\Gamma(P;u,v)=\frac{d-1}{n-1}.}
\]

For every \(u\ne v\),

\[
\frac{d-1}{n-1}\le\mathbb E\Gamma(P;u,v)\le\frac dn.
\]

The lower constant is approached along any sequence \(u\to v\) of distinct unit vectors. It is positive exactly when \(d\ge2\). For \(d=n\) the efficiency equals one identically.

**Exact rank-one-section law.** If \(d=1\) and \(\phi=\arccos\langle u,v\rangle\in(0,\pi]\), then

\[
\boxed{\Pr\{\Gamma(P;u,v)>0\}=\frac\phi\pi},\qquad
\boxed{\mathbb E\Gamma(P;u,v)=\frac{2}{\pi n}\,\frac{\sin\phi-\phi\cos\phi}{1-\cos\phi}}.
\]

In particular, \(\mathbb E\Gamma(P;u,v)\sim4\phi/(3\pi n)\) as \(\phi\downarrow0\). Consider minimizing the linear function \(f(x)=-\langle u,x\rangle\) over the Euclidean unit ball, from the boundary point \(x=v\), by exactly minimizing over each independent Haar-random line through the incumbent and accepting the section minimizer. Before the first strictly improving step the incumbent remains \(v\); its waiting time is geometric with success probability \(\phi/\pi\) and mean \(\pi/\phi\). If \(g=1-\cos\phi\) is the objective gap, the exact conditional one-step expected decrease is

\[
\boxed{\mathbb E[g-g^+\mid x=v]=\frac{2}{\pi n}(\sin\phi-\phi\cos\phi)
\sim\frac{4\sqrt2}{3\pi n}\,g^{3/2}.}
\]

Hence no fixed strictly positive relative expected-improvement constant is valid near the minimizer for single-line sections, even on a Euclidean ball with a linear objective.

## Assumptions and scope

All statements concern real Euclidean space, Haar-uniform linear subspaces (orthonormal-row \(P\)), fixed distinct unit vectors \(u,v\), and exact linear section minimization. The expectation is over \(P\) alone. We include the endpoint \(d=n\) and every ambient dimension \(n\ge2\). The one-dimensional waiting time assumes independent fresh Haar lines and no additional movement on zero-improvement iterations. The theorem concerns the boundary-ball efficiency of the section linear minimization oracle; it is not an automatic rate theorem on arbitrary strongly convex constraint sets.

## Proof

**1. A norm-increment identity.** Set \(\rho=\langle u,v\rangle<1\). Elementary polarization gives

\[
2\bigl(\|Pu\|\|Pv\|-\langle Pu,Pv\rangle\bigr)
=\|P(u-v)\|^2-(\|Pu\|-\|Pv\|)^2.
\]

Haar invariance gives \(\mathbb E(P^{\mathsf T}P)=(d/n)I\). Consequently,

\[
\mathbb E\Gamma(P;u,v)=\frac dn-\frac{\mathbb E(\|Pu\|-\|Pv\|)^2}{2(1-\rho)}. \tag{1}
\]

This identity appears in the motivating literature; the sharp bound below is the additional step.

**2. The circular Fourier chord inequality.** For any real, \(2\pi\)-periodic Lipschitz function \(h\), any \(t\in\mathbb R\), and \(\phi\in[0,\pi]\), Fourier expansion and Parseval give

\[
\frac1{2\pi}\int_0^{2\pi}|h(t+\phi)-h(t)|^2dt
\le 2(1-\cos\phi)\frac1{2\pi}\int_0^{2\pi}|h'(t)|^2dt. \tag{2}
\]

Indeed, if \(c_k\) are its Fourier coefficients, the two sides have expansions \(\sum_{k\in\mathbb Z}|c_k|^2|e^{ik\phi}-1|^2\) and \(|e^{i\phi}-1|^2\sum_{k\in\mathbb Z} k^2|c_k|^2\). The comparison follows from \(|e^{ik\phi}-1|\le |k|\,|e^{i\phi}-1|\), first for positive integers by a geometric sum and then for negative integers by symmetry. Lipschitz regularity guarantees that \(h\) belongs to the periodic Sobolev space \(H^1\), so this Parseval calculation is valid even at nondifferentiable points.

Choose a unit vector \(w\perp v\), write \(u=\cos\phi\,v+\sin\phi\,w\), and apply (2) to

\[
h_P(t)=\|P(\cos t\,v+\sin t\,w)\|.
\]

Haar rotational invariance makes the distribution of each shifted pair of norms independent of the base angle. Therefore,

\[
\mathbb E(\|Pu\|-\|Pv\|)^2
\le 2(1-\cos\phi)\,\mathbb E\bigl[h_P'(0)^2\bigr]. \tag{3}
\]

**3. Exact directional derivative energy.** Let \(\Pi=P^{\mathsf T}P\) and \(S=\|Pv\|^2\). Almost surely \(S>0\), and

\[
h_P'(0)=\frac{\langle Pv,Pw\rangle}{\|Pv\|}
=\frac{\langle\Pi v,w\rangle}{\sqrt S}.
\]

Because \(\Pi\) is an orthogonal projector, \(\langle \Pi v,v\rangle=\|\Pi v\|^2=S\). Decomposing \(\Pi v=Sv+b\) with \(b\perp v\) gives \(\|b\|^2=S(1-S)\). Conditional on \(S\), rotational invariance under all orthogonal maps fixing \(v\) makes the direction of \(b\) uniform in \(v^\perp\). Thus for unit \(w\perp v\),

\[
\mathbb E\left[h_P'(0)^2\mid S\right]=\frac{1-S}{n-1}.
\]

Since \(\mathbb E S=d/n\),

\[
\boxed{\mathbb E h_P'(0)^2=\frac{n-d}{n(n-1)}.} \tag{4}
\]

The argument includes \(d=1\). For \(d=n\), \(S=1\) and the derivative vanishes. For \(d<n\), the event \(S=0\) has probability zero.

**4. Uniform inequality.** Substitute (4) into (3), then into (1):

\[
\mathbb E\Gamma(P;u,v)\ge\frac dn-\frac{n-d}{n(n-1)}=\frac{d-1}{n-1}.
\]

The upper bound follows directly from (1). Nonnegativity is also immediate by Cauchy–Schwarz.

**5. Sharpness at near alignment.** With \(u_\phi=\cos\phi\,v+\sin\phi\,w\), the path \(t\mapsto h_P(t)\) is differentiable at \(t=0\) almost surely. The projection norm is \(1\)-Lipschitz as a function of the unit-vector argument, so the squared difference quotient is bounded by one. Dominated convergence and (4) imply

\[
\lim_{\phi\downarrow0}\frac{\mathbb E(\|Pu_\phi\|-\|Pv\|)^2}{2(1-\cos\phi)}
=\frac{n-d}{n(n-1)}.
\]

Equation (1) gives the asserted limiting efficiency \((d-1)/(n-1)\), proving optimality of the constant for all permitted \(n,d\).

**6. Exact single-line law.** For \(d=1\), write \(P=p^{\mathsf T}\), where \(p\) is uniform on \(\mathbb S^{n-1}\). Then

\[
\Gamma(P;u,v)=\frac{2[-(p\cdot u)(p\cdot v)]_+}{1-\cos\phi}.
\]

On the plane spanned by \(u,v\), write the projection of \(p\) as \(R(\cos\alpha,\sin\alpha)\). Its angle \(\alpha\) is uniform on \([0,2\pi)\), independent of \(R\), and \(\mathbb E R^2=2/n\); for \(n=2\), \(R=1\). With \(p\cdot u=R\cos\alpha\) and \(p\cdot v=R\cos(\alpha-\phi)\), the two cosine factors have opposing signs on arcs of total angular length \(2\phi\). Thus the positive-efficiency probability is \(\phi/\pi\). Elementary integration over those arcs gives

\[
\frac1{2\pi}\int_0^{2\pi}[-\cos\alpha\cos(\alpha-\phi)]_+\,d\alpha
=\frac{\sin\phi-\phi\cos\phi}{2\pi}.
\]

Taking expectations proves the exact mean formula. The series \(\sin\phi-\phi\cos\phi=\phi^3/3+O(\phi^5)\), together with \(1-\cos\phi=\phi^2/2+O(\phi^4)\), proves the asymptotic. For the linear-objective ball problem, a sampled line through \(v\) meets the boundary again at \(v-2(p\cdot v)p\). Exact minimization chooses that point precisely when \((p\cdot u)(p\cdot v)<0\), and otherwise returns \(v\). Therefore the preceding probability is the exact first-move success probability and the preceding normalized expectation is the exact relative objective decrease. Independence gives the geometric waiting time. No claim about the complete multi-step trajectory is required.

## Verification

The standalone file `verify.py` (Python 3 standard library only) replays rational-dimensional identities, deterministic angular quadratures, finite random Haar-frame comparisons of both bounds, and discretized circle-Fourier energy inequalities. With the specified seed, it completed 433582 finite checks: 1302 rational identities, 40 angular quadratures, 432000 random-projector tests, and 240 Fourier shift checks. The analytic proof, not the finite tests, establishes the all-dimension, all-angle and sharp-infimum statements. Execute with `python3 verify.py`.

## Relationship to prior work

Poirion, Pokutta, and Takeda (2026), *Random-Subspace Frank–Wolfe over Strongly Convex Sets*, introduce the boundary-ball efficiency \(\Gamma\) and derive identity (1). Their Proposition 1 establishes the lower bound \(d/n-4(n-d)/(n(n-1))\) for \(d\ge3\); their Proposition 7 gives the positive but smaller bound \((d-1)/(96(n-1))\) for \(d\ge2\). Neither quoted bound identifies the exact infimum. The present sharp \((d-1)/(n-1)\) coefficient eliminates the factor-four loss in the Proposition 1 correction, strengthens the positive lower bound by a factor of 96, covers \(d=2\) optimally, and identifies the genuine \(d=1\) failure with an exact probability and gap law. The original efficiency identity, Fourier/Parseval inequality, and Haar second-moment identities are credited mathematical ingredients, not individually claimed as novel. A related published result on Haar stochastic-subspace descent concerns objective-side random updates, rather than constrained section LMOs, and does not imply this exact infimum.

## Limitations

Only the exact expected boundary-ball oracle ratio is classified. Applications to a general convex body need the geometric comparison assumptions and constants of the chosen optimization method; a new uniform convergence theorem for arbitrary strongly convex bodies is not asserted. The first-move waiting law concerns a fixed linear objective on a ball with independent full line minimizations and is not a multi-step distribution theorem. Arithmetic, oracle error, approximate sampling, and implementation costs are outside scope. Equivalence to a result in unindexed literature remains possible; no independent audit has been performed.

## References

1. P.-L. Poirion, S. Pokutta, and A. Takeda, *Random-Subspace Frank–Wolfe over Strongly Convex Sets*, arXiv:2605.24819v1, first public release 2026-05-24. https://arxiv.org/html/2605.24819v1 (especially Sections 2–3 and Appendix C).
2. *Exact Haar moments remove sampling-dimension restrictions in sparse stochastic subspace descent*, published mathematical research record dated 2026-09-18; mathematical comparison used solely for distinguishing objective-side descent from section-oracle gaps. https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-exact-haar-moments-sparse-ssd--d9ecf263b248
