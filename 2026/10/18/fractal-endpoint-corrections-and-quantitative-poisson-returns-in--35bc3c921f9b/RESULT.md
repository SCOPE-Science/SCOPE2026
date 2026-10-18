# Fractal endpoint corrections and quantitative Poisson returns in a Zipf expanding map

## Finding
For the reflected Zipf-normalized countable-branch affine expanding map defined below, the invariant conformal probability has a **sharp two-scale distribution law at its branch-accumulation point**. Its leading local dimension is not the Hausdorff dimension of the repeller, and its first nonzero correction is a nonconstant profile that retains the full singular distribution function. The same local law yields a quantitative Poisson limit for visits to shrinking neighborhoods of that point.

Fix real \(q>1\) and \(0<\lambda<1\). Define \(Z=\zeta(q)\), \(c=\lambda/Z\), and the unique \(s\in(1/q,1)\) satisfying
\[
 c^s\zeta(qs)=1.
\]
Set
\[
 d=\frac{qs-1}{q-1},\qquad H=\frac{1}{(q-1)Z},\qquad
 K=\frac{c^s}{qs-1}H^{-d}.
\]
The exponent satisfies \(0<d<s<1\). For the invariant probability \(\mu\), as \(x\downarrow0\),
\[
 \boxed{\mu([0,x])=Kx^d+O_{q,\lambda}\bigl(x^{d+1/(q-1)}\bigr).}
\]
The correction exponent is optimal. Its entire phase profile is described next.

For \(n\ge2\) and \(0\le a\le1\), define
\[
 b_n=Z^{-1}\sum_{j>n}j^{-q},\qquad
 x_n(a)=b_n+\frac{a}{Zn^q},
\]
and let \(F(x)=\mu([0,x])\) for \(x\in[0,1]\), with
\[
 Q_\lambda(a)=
 \begin{cases}
 F(a/\lambda),&0\le a\le\lambda,\\
 1,&\lambda\le a\le1.
 \end{cases}
\]
Then the **uniform fractal correction law** is
\[
 \boxed{\sup_{0\le a\le1}
 \left|n^{qs}\bigl(F(x_n(a))-Kx_n(a)^d\bigr)
 -c^s\bigl(Q_\lambda(a)-a\bigr)\right|=O_{q,\lambda}(n^{-1}).}
\]
The continuous function \(Q_\lambda(a)-a\) is nonconstant: it vanishes at \(a=0,1\), while its value at \(a=\lambda\) is \(1-\lambda>0\). In particular,
\[
 \lim_{n\to\infty}n^{qs}\bigl(F(x_n(\lambda))-Kx_n(\lambda)^d\bigr)
 =c^s(1-\lambda)>0.
\]
The first correction therefore cannot be replaced by a smaller uniform order.

For \(X_0\sim\mu\), \(X_k=T^k(X_0)\), \(t\ge0\), and integer \(m\ge1\), put
\[
 N_m(t)=\sum_{k=0}^{m-1}{\bf1}\{X_k\le t\,m^{-1/d}\}.
\]
For each fixed \(t>0\), its distribution satisfies the **quantitative rare-return theorem**
\[
 \boxed{d_{\rm TV}\left(\mathcal L(N_m(t)),
 \operatorname{Poisson}(Kt^d)\right)
 =O_{q,\lambda,t}\left(m^{-\eta}\right),\qquad
 \eta=\min\left\{1,\frac1{qs-1}\right\}.}
\]
At \(t=0\) the count is identically zero. Consequently, for every \(t\ge0\),
\[
 \boxed{\lim_{m\to\infty}
 \mu\left\{m^{1/d}\min_{0\le k<m}T^k(X_0)>t\right\}
 =e^{-Kt^d}.}
\]
The limiting extremal index is one. This concerns the singular conformal measure, not Lebesgue-distributed initial conditions.

## Assumptions and scope
The inverse similarities on \([0,1]\) are
\[
 S_n(x)=b_n+cn^{-q}x,\quad
 b_n=Z^{-1}\sum_{j>n}j^{-q},\quad n\ge1.
\]
Their branch intervals \(I_n=S_n([0,1])\) are disjoint, with the gap from \(I_n\) to \(I_{n-1}\) of length \((1-\lambda)n^{-q}/Z\) for \(n\ge2\). The intervals accumulate only at \(0\). The map \(T:\bigcup_{n\ge1}I_n\to[0,1]\) is \(T|_{I_n}=S_n^{-1}\). Its survivor \(\Lambda\) contains points with infinite admissible itineraries and has Hausdorff dimension \(s\).

The probability \(\mu\) is the push-forward of the independent-symbol law \(\mathbb P(J=n)=c^s n^{-qs}\) under the coding map \((J_1,J_2,\ldots)\mapsto\lim_{k\to\infty}S_{J_1}\circ\cdots\circ S_{J_k}(0)\). Its non-atomicity, \(T\)-invariance, and ergodicity follow directly from the coding. This is the standard \(s\)-conformal measure for the separated affine system.

Reflection \(x\mapsto1-x\) identifies these branches with the Zipf-normalized family \([P_n-\lambda p_n,P_n]\), \(p_n=n^{-q}/Z\), \(P_n=\sum_{j\le n}p_j\), already studied in the literature. Neither that family, the pressure equation for \(s\), nor the existence of a conformal invariant measure is claimed as new.

All estimates fix \(q,\lambda\) strictly inside the displayed ranges. The term \(O(n^{-1})\) is uniform in \(a\) but not asserted uniform as \(q\downarrow1\) or \(\lambda\) approaches its endpoints.

## Proof
**1. Coding and dimension.** Each inverse derivative is the constant \(r_n=cn^{-q}\), and \(\sum_n r_n=\lambda<1\). The separated full shift coding exists and is injective. The function \(u\mapsto\sum_n r_n^u\) decreases continuously from infinity at \(u\downarrow1/q\) to \(\lambda\) at \(u=1\). This gives the unique pressure root \(s\). At depth \(k\), the cylinder intervals have total \(s\)-power length exactly one and maximal diameter at most \(c^k\), giving the Hausdorff upper bound. Finite-alphabet subsystems have similarity dimensions increasing to \(s\) under the open set condition, proving the reverse bound. The Bernoulli probabilities sum to one, and deleting the first symbol implements \(T\), proving invariance and ergodicity. All atoms have mass zero because the maximal single-symbol probability is strictly less than one.

Since \(s<1\), one has \(qs-1<s(q-1)\), so \(0<d<s\).

**2. An exact local-mass identity.** For every \(n\ge2\) and \(a\in[0,1]\), the point \(x_n(a)\) lies in \(I_n\) if \(a\le\lambda\) and in the subsequent empty gap if \(a\ge\lambda\). All higher-index intervals lie below it and all lower-index intervals lie above it. By conditional coding on the first symbol,
\[
 F(x_n(a))=c^s\sum_{j>n}j^{-qs}+c^sn^{-qs}Q_\lambda(a).
 \tag{1}
\]
This is an exact equality, with no smoothing or finite-branch approximation. It holds at the interval endpoints because \(\mu\) has no atoms.

**3. Uniform two-term expansion.** The integral/Euler--Maclaurin estimate, valid for each fixed \(v>1\), is
\[
 \sum_{j>n}j^{-v}=\frac{n^{1-v}}{v-1}
 -\frac12n^{-v}+O_v(n^{-v-1}).
 \tag{2}
\]
Applying (2) at \(v=q\) gives, uniformly in \(a\in[0,1]\),
\[
 x_n(a)=Hn^{1-q}+\frac{a-1/2}{Z}n^{-q}+O_q(n^{-q-1}).
\]
Taylor expansion of \(Kx_n(a)^d\) and the identities \(d(q-1)=qs-1\) and \(HZ(q-1)=1\) give
\[
 Kx_n(a)^d=\frac{c^s}{qs-1}n^{1-qs}
 +c^s(a-1/2)n^{-qs}+O_{q,\lambda}(n^{-qs-1}).
 \tag{3}
\]
Expanding the tail in (1) at \(v=qs\) and subtracting (3),
\[
 F(x_n(a))-Kx_n(a)^d
 =c^s\bigl(Q_\lambda(a)-a\bigr)n^{-qs}
 +O_{q,\lambda}(n^{-qs-1}),
\]
uniformly over the entire branch-plus-gap cell. Each sufficiently small positive \(x\) belongs to a cell \([b_n,b_{n-1}]\), and there \(x\asymp n^{1-q}\); this proves the global bound \(O(x^{qs/(q-1)})\). The displayed positive limit at \(a=\lambda\) proves its optimality.

**4. Quantitative Poisson coupling.** Let \(u=t m^{-1/d}\) with fixed \(t>0\), and choose the unique large index \(n=n(u)\) with \(b_n\le u<b_{n-1}\). Along the stationary trajectory, the first-symbol process \((J_{k+1})_{k\ge0}\) is independent with probabilities \(w_j=c^sj^{-qs}\). Every symbol \(j>n\) guarantees \(X_k\le u\); every symbol \(j<n\) forbids it. Only occurrences of the one boundary symbol \(j=n\) can cause disagreement. Thus, on the same coding space, \(N_m(t)\) differs from a \(\operatorname{Binomial}(m,p_m)\) variable, where \(p_m=\sum_{j>n}w_j\), with probability at most \(mw_n\).

As \(u\downarrow0\), \(n\asymp u^{-1/(q-1)}\) and \(w_n=O(u^{qs/(q-1)})\). The proven local distribution bound and \(0\le F(u)-p_m\le w_n\) imply
\[
 mw_n=O(m^{-1/(qs-1)}),\qquad
 mp_m=Kt^d+O(m^{-1/(qs-1)}).
\]
The elementary binomial-to-Poisson total-variation bound is at most \(mp_m^2=O(m^{-1})\); changing the Poisson mean contributes at most \(|mp_m-Kt^d|\). Adding these three bounds proves the asserted total-variation rate. A zero visit count is equivalent to the minimum being greater than \(u\); taking the zero probability of the limiting Poisson variable gives the Weibull survival law.

## Verification
The accompanying independent arithmetic checks are in `verify_endpoint.py`; reproduce using Python 3 and `mpmath` 1.3 or later with `python verify_endpoint.py`. The script reconstructs the pressure root, exact branch-cell distribution from a recursive coding formula, sharp endpoint-profile values at six cell positions for four increasing branch indices, and first-order shrinking-threshold mass in two distinct parameter pairs. Its numerical tests passed for \((q,\lambda)=(2,0.4)\) and \((3,0.7)\). The argument above, not those tests, proves the infinitely many branch and time statements for all admissible real parameters.

## Relationship to prior work
Cunha--Novaes--Ponce establish the countably expanding branch framework, a shift conjugacy, dimensional information, and existence of an invariant conformal law, but do not derive this singular-endpoint mass correction or rare-return rate. The public result *Exponential-alphabet crossover for Zipf-normalized expanding maps* supplies exactly the reflected branch family and its pressure/dimension equations; its proved statements concern finite-alphabet dimension under the joint limit of alphabet cutoff and \(q\downarrow1\), not the present fixed-parameter local distribution or its first fractal correction. These geometries and pressure identities are explicitly treated as prior work.

Mauldin--Urbański give the general conformal-IFS pressure and measure foundations; Banaji--Fraser study Assouad spectra rather than conformal-distribution corrections. Reeve studies Hausdorff dimension of exponentially shrinking-target sets for countable Markov maps, not stationary near-accumulation Poisson statistics. Freitas--Freitas--Todd develop broad extreme-value and return laws, including Poisson limits under mixing conditions; the Poisson family is therefore not itself new. The present quantitative coupling and its exact constants are consequences of the separately proved sharp singular-mass law, and no universal Poisson theorem is claimed.

## Limitations
The model is affine, has independently coded branches, and uses the distinguished conformal probability. Nothing here establishes the same constants, sharp profile, or rate for nonlinear sliding-Shilnikov return maps, arbitrary countable IFSs, or Lebesgue initial distributions. The second-order profile is specified through the self-similar distribution \(F\), not a finite elementary expression. The total-variation exponent is an upper bound, not asserted optimal. Generic conformal-measure or return-time literature might contain an equivalent specialized instance; bibliographic priority is not independently certified.

## References
1. M. G. C. Cunha, D. D. Novaes, G. Ponce, *Infinite-Piecewise Expanding Maps: Chaos, Ergodicity and Invariant-Set Complexity*, arXiv:2608.00398v1 (first public 2026-08-01), Theorem A and Appendix B. https://arxiv.org/abs/2608.00398
2. *Exponential-alphabet crossover for Zipf-normalized expanding maps*, published research record, full `RESULT.md` inspected. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exponential-alphabet-crossover-for-zipf-normalized-expanding-map--9738a052e9b1
3. R. D. Mauldin, M. Urbański, *Dimensions and Measures in Infinite Iterated Function Systems*, Proc. London Math. Soc. 73 (1996), 105--154. DOI:10.1112/plms/s3-73.1.105.
4. A. Banaji, J. M. Fraser, *Assouad type dimensions of infinitely generated self-conformal sets*, Nonlinearity 37 (2024), 045004. https://arxiv.org/html/2207.11611v2
5. H. W. J. Reeve, *Shrinking Targets for Countable Markov Maps*, 2011. https://arxiv.org/abs/1107.4736
6. A. C. M. Freitas, J. M. Freitas, M. Todd, *Hitting Time Statistics and Extreme Value Theory*, Probab. Theory Relat. Fields 147 (2010), 675--710. https://arxiv.org/abs/0804.2887
