# An exact global separatrix and water-filling convergence for a positive quadratic map

## Finding

The quadratic operator introduced by Shoyimardonov and Rozikov admits an explicit, uniformly approximable radial separator in **every finite dimension**, without parameter-order or nondegeneracy restrictions. Its normalized projective dynamics converge from every nonzero initial state to a uniquely determined water-filling equilibrium. Consequently, the entire nonnegative cone is partitioned into convergence to zero, convergence to a nonzero fixed point on the separator, and escape to infinity. Every invariant Borel probability is a convex combination of point masses at fixed points.

Precisely, for any integer \(n\ge2\), any \(\theta_1,\ldots,\theta_n>0\), and any initial \(x_0\in\mathbb R_{\ge0}^{n}\setminus\{0\}\), let \(s_0=\sum_i(x_0)_i>0\), \(p_0=x_0/s_0\), and define
\[
 a(p)=\sum_{i=1}^n\theta_i p_i(1-p_i/2),\qquad
 G_i(p)=\frac{\theta_i p_i(1-p_i/2)}{a(p)}.
\]
The continuous positive function
\[
 s_*(p)=\exp\!\left(-\sum_{j=0}^{\infty}2^{-j-1}\log a(G^j p)\right)
\]
on the closed probability simplex is the **exact** critical radius. For each orbit \(x_{m+1}=H(x_m)\), with \(H_i(x)=\theta_i x_i(\sum_k x_k-x_i/2)\),
\[
 \|x_m\|_1=s_*(G^m p_0)\left(\frac{s_0}{s_*(p_0)}\right)^{2^m}.
\]
The three cases \(s_0<s_*(p_0)\), \(s_0=s_*(p_0)\), and \(s_0>s_*(p_0)\) yield respectively \(x_m\to0\), convergence to a nonzero fixed point, and \(\|x_m\|_1\to\infty\). In the first and last cases the norm has a sharp doubly exponential logarithmic scale, with \(2^{-m}\log\|x_m\|_1\to\log(s_0/s_*(p_0))\).

## Assumptions and scope

The phase space is the nonnegative cone \(\mathbb R_{\ge0}^{n}\), including all coordinate faces and the origin; no assumption of distinct parameter values is made. Define the initial positive support \(S=\{i:(x_0)_i>0\}\). For every nonempty \(S\), there is a unique \(\lambda_S>0\) satisfying
\[
 \sum_{i\in S}2(1-\lambda_S/\theta_i)_+=1,
 \qquad (t)_+=\max\{t,0\}.
\]
The limit of the normalized orbit is
\[
 (p^S)_i=\begin{cases}2(1-\lambda_S/\theta_i)_+,&i\in S,\\0,&i\notin S.\end{cases}
\]
It satisfies \(a(p^S)=\lambda_S\). On the critical surface the limit of the full orbit is \(p^S/\lambda_S\), a nonzero fixed point; on either other side the direction still converges to \(p^S\). The origin is fixed separately. A face that initially has zero coordinates never acquires positive mass there.

## Proof

**1. Homogeneous decomposition.** Set \(s=\sum_i x_i\) and \(p=x/s\). The identity \(H_i(x)=s^2\theta_i p_i(1-p_i/2)\) gives the exact recursion
\[
 p_{m+1}=G(p_m),\qquad s_{m+1}=a(p_m)s_m^2.
\]
Because \(\sum_i p_i^2\le1\), for all probability vectors \(p\) and positive parameters,
\[
 \theta_{\min}/2\le a(p)\le\theta_{\max}.
\]
In particular the projective system is well defined on every face and all forward iterates remain positive on their original support.

**2. A strict ascent potential.** On the simplex define
\[
 \Phi(p)=\sum_i\left[p_i\log\theta_i+
 \int_0^{p_i}\log(1-u/2)\,du\right].
\]
Its gradient on the simplex is \(g_i(p)=\log[\theta_i(1-p_i/2)]\); its diagonal Hessian entries are \(-1/(2-p_i)\). The update is the multiplicative-gradient formula \(G_i(p)=p_i e^{g_i(p)}/\sum_j p_j e^{g_j(p)}\). On the relative interior of the initial support set let \(q=G(p)\) and \(\Delta=q-p\). The logarithmic update implies
\[
 g(p)\cdot\Delta=D_{\mathrm{KL}}(q\Vert p)+D_{\mathrm{KL}}(p\Vert q)
 \ge\|\Delta\|_1^2,
\]
where both Kullback–Leibler divergences are finite and the last estimate is twice Pinsker's inequality (each divergence is at least half the squared \(\ell^1\)-distance). Taylor's formula along the segment between \(p\) and \(q\) uses \(-1\le\partial_{ii}^2\Phi\le-1/2\), and yields
\[
 \Phi(q)-\Phi(p)\ge g(p)\cdot\Delta-\tfrac12\|\Delta\|_2^2
 \ge\tfrac12\|\Delta\|_1^2.
\]
The potential is bounded above on the compact face, so \(\|G(p_m)-p_m\|_1\to0\).

**3. Convergence and identification of direction.** Every accumulation point is fixed by continuity of \(G\). There are only finitely many fixed points of \(G\): for each nonempty positive support \(J\), its fixed point must obey \(\theta_i(1-p_i/2)=\lambda_J\) for \(i\in J\), hence
\[
 \lambda_J=\frac{|J|-1/2}{\sum_{i\in J}\theta_i^{-1}},\qquad
 p_i=2(1-\lambda_J/\theta_i),
\]
with positivity required; there is at most one point per \(J\). A compact asymptotically regular orbit whose accumulation set is finite must converge: otherwise it would make infinitely many steps across separated neighborhoods, while step lengths tend to zero, giving an additional accumulation point outside those neighborhoods.

Let \(p_m\to p^*\), with positive support \(J\subseteq S\) and common active fitness \(\lambda\). For each \(i\in S\setminus J\), if \(\theta_i>\lambda\), then \((p_{m+1})_i/(p_m)_i\to\theta_i/\lambda>1\), impossible because these positive coordinates converge to zero. Thus \(\theta_i\le\lambda\) at all vanished coordinates. These are exactly the Karush–Kuhn–Tucker conditions for maximizing the strictly concave \(\Phi\) over the simplex on \(S\). They uniquely select \(p^S\) and the water-filling \(\lambda_S\) above, including tie cases \(\theta_i=\lambda_S\). Moreover, summing the fixed-point equations gives \(a(p^S)=\lambda_S\).

**4. Exact radial separator.** Put \(p_j=G^j p\). The uniformly bounded logarithms of \(a(p_j)\) make the defining weighted series for \(s_*(p)\) uniformly convergent. Shifting its indices gives
\[
 s_*(Gp)=a(p)s_*(p)^2.
\]
Dividing the radial recurrence by this identity and iterating yields
\[
 \frac{s_m}{s_*(p_m)}=\left(\frac{s_0}{s_*(p_0)}\right)^{2^m}.
\]
The projective limit implies \(s_*(p_m)\to1/\lambda_S\), by uniform convergence of the series and continuity. Therefore all three asymptotic cases follow, with \(x_m=s_mp_m\) and the stated double-exponential exponent.

**5. Computability and stationary measures.** If \(s_{*,N}(p)\) truncates the defining sum after the indices \(0,\ldots,N-1\), then
\[
 |\log s_{*,N}(p)-\log s_*(p)|\le2^{-N}B,
 \quad B=\max\{|\log(\theta_{\min}/2)|,|\log\theta_{\max}|\}.
\]
This holds uniformly on the entire simplex. Each nonzero orbit either converges to a fixed point or escapes every compact set. Such an orbit is recurrent only if it is itself fixed. Poincaré recurrence for a finite invariant Borel probability on the cone therefore restricts its support to the finite fixed-point set, giving a convex combination of the Dirac masses there. Every such combination is invariant.

## Verification

The accompanying Python 3 standard-library program `verify.py` checks the exact mass-direction decomposition using rational arithmetic; tests monotone ascent, convergence to the water-filling profile and the critical-radius cocycle across representative dimensions and parameter choices; and checks the certified logarithmic tail bound against longer truncation. Run `python3 verify.py` from the unpacked package directory. Finite numerical checks are corroboration only; the infinite-dimensional and all-parameter quantifiers (for every finite \(n\)) are established by the proof.

## Relationship to prior work

Shoyimardonov and Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, arXiv:2409.13450 (first posted 2024-09-20), introduce exactly this operator and classify its fixed points. Their full 2025 journal treatment also proves several two-dimensional basin and invariant-curve results, partial higher-dimensional invariant-region statements, and the existence of a radial eigenvalue \(2\) at nonzero equilibria. These facts and the underlying system are prior work, not discoveries here.

The claim here is the **combined global all-dimensional** direction limit on every face, the exact critical-radius series with an a priori uniform truncation error, the resulting complete extinction/fixed-point/escape trichotomy, and the stationary-measure classification. The explicit radial series is a general device for degree-two homogeneous maps and is not claimed novel in isolation; its usefulness here relies on the separate proved convergence of the projective dynamics. Known lower-dimensional separators alone do not imply the theorem for arbitrary numbers of coordinates and unequal parameters.

## Limitations

This result applies only to the stated positive homogeneous quadratic family on the nonnegative cone; it does not address signed parameters, perturbations breaking homogeneity, or an arbitrary quadratic operator. The critical surface is specified by a convergent series with certified error rather than by an elementary closed formula. The proof establishes convergence but does not give a uniform rate of directional convergence over all positive parameter vectors, nor characterize the finer parameter-dependent behavior near a water-filling tie. Mathematical priority is subject to independently checking any equivalent unindexed projective-gradient convergence theorem.

## References

1. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, arXiv:2409.13450v1 (2024-09-20). https://arxiv.org/abs/2409.13450
2. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, *Russian Journal of Nonlinear Dynamics* 21 (2025), 399–418. DOI: 10.20537/nd250803. https://nd.ics.org.ru/upload/iblock/cc9/nd250803.pdf
3. Standard finite-alphabet Kullback–Leibler divergence/Pinsker inequality and Poincaré recurrence are used in their usual classical forms.
