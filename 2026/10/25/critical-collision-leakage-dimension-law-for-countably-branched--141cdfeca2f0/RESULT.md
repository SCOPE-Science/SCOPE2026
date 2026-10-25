# Critical collision–leakage dimension law for countably branched expanding maps

## Finding

For the explicit family below, let \(t(q,\eta)\) be the Hausdorff dimension of the unrestricted invariant set, and let \(d(q,\eta)\) be the dimension of the invariant subset whose successive branch labels are never equal. Both dimensions are characterized by scalar equations, and the *dimension penalty for forbidding immediate returns to the same branch* is asymptotically independent of the geometric leakage rate.

Write \(\zeta\) for the Riemann zeta function, \(q>1\), \(0<\eta<1\), and
\[
p_j(q)=\frac{j^{-q}}{\zeta(q)},\qquad r_j(q,\eta)=(1-\eta)p_j(q),\qquad S_2(q)=\sum_{j\ge1}p_j(q)^2=\frac{\zeta(2q)}{\zeta(q)^2}.
\]
The dimensions are the unique roots in \((1/q,1)\) of
\[
\sum_{j\ge1}r_j^{t}=1,\qquad
\sum_{j\ge1}\frac{r_j^{d}}{1+r_j^{d}}=1,
\]
respectively. In particular, \(1/q<d(q,\eta)<t(q,\eta)<1\).

**Critical additive law.** For *every* function \(\eta=\eta(q)\) satisfying \(0<\eta(q)<1\) and \(\eta(q)\to0\) as \(q\downarrow1\), one has simultaneously
\[
\boxed{\displaystyle
1-t(q,\eta)\sim(q-1)\eta,\qquad
 t(q,\eta)-d(q,\eta)\sim(q-1)S_2(q),}
\]
and consequently
\[
\boxed{\displaystyle 1-d(q,\eta)\sim(q-1)\bigl(\eta+S_2(q)\bigr).}
\]
The assertions remain valid with arbitrarily irregular dependence of \(\eta\) on \(q\). As \(S_2(q)\sim\zeta(2)(q-1)^2\), the no-repeat penalty has the universal cubic asymptotic
\[
\boxed{\displaystyle\lim_{q\downarrow1}\frac{t(q,\eta(q))-d(q,\eta(q))}{(q-1)^3}=\zeta(2)=\frac{\pi^2}{6}.}
\]
If \(\eta(q)/S_2(q)\to\kappa\in[0,\infty)\), the total dimension deficit has coefficient \((1+\kappa)\zeta(2)\) at cubic order. This locates the crossover between geometric holes and symbolic immediate-repeat exclusions at \(\eta\asymp(q-1)^2\).

## Assumptions and scope

Let \(g_j=\eta 2^{-j}\). Partition \([0,1)\), in order, into an initial gap of length \(g_1\), an interval \(J_1\) of length \(r_1\), a gap of length \(g_2\), an interval \(J_2\) of length \(r_2\), and so on. Explicitly,
\[
a_j=g_j+\sum_{k<j}(g_k+r_k),\qquad J_j=[a_j,a_j+r_j].
\]
Because \(\sum_j(g_j+r_j)=1\), the intervals are nonoverlapping, isolated, and accumulate only at \(1\). Set \(\psi_j(x)=a_j+r_jx\) on \([0,1]\), and define \(T|_{J_j}=\psi_j^{-1}\). Every branch of \(T\) is affine, onto \([0,1]\), and expanding, with infinitely many isolated domains and polynomially decaying inverse slopes. These are one-dimensional expanding interval maps with a countable Markov partition.

For a sequence \(\omega=(\omega_1,\omega_2,\ldots)\in\mathbb N^{\mathbb N}\), set \(\Pi(\omega)=\lim_{n\to\infty}\psi_{\omega_1}\circ\cdots\circ\psi_{\omega_n}(0)\). Define
\[
\Lambda_{q,\eta}=\Pi(\mathbb N^{\mathbb N}),\qquad
K_{q,\eta}=\Pi\{\omega:\omega_n\ne\omega_{n+1}\text{ for every }n\ge1\}.
\]
The positive gaps guarantee unique branch labels. The claim concerns Hausdorff dimension of these (possibly nonclosed) symbolic limit sets. It does **not** assert the same dimension for their closures, nor does it classify arbitrary smooth non-affine perturbations.

## Proof

**1. Exact unrestricted dimension.** For \(s>1/q\), write \(w_j=r_j^s\). Then \(\sum_jw_j<\infty\), and the \(s\)-sum of lengths of all level-\(n\) cylinders is \((\sum_jw_j)^n\). A cylinder-cover argument gives \(\dim_H\Lambda\le t\) whenever \(\sum_jr_j^s<1\). Conversely, for each finite alphabet \(\{1,\ldots,N\}\), the isolated affine branches form a strongly separated finite similarity system, whose dimension is the root of \(\sum_{j\le N}r_j^s=1\). These roots increase to the infinite-sum root, so \(\dim_H\Lambda=t\). Strict monotonicity and divergence as \(s\downarrow1/q\) imply the stated uniqueness.

**2. Exact no-repeat dimension.** At exponent \(s>1/q\), the weighted adjacency matrix for \(\omega_n\ne\omega_{n+1}\) is \(B_{ij}=w_j\) when \(i\ne j\), and \(B_{ii}=0\). For each \(\lambda>0\), put \(v_i=(\lambda+w_i)^{-1}\). Directly,
\[
(Bv)_i-\lambda v_i
=\sum_j\frac{w_j}{\lambda+w_j}-1,
\]
independently of \(i\). Thus \(Bv=\lambda v\) precisely when \(\sum_jw_j/(\lambda+w_j)=1\). In particular, the pressure vanishes at the unique \(d\) solving \(\sum_jr_j^d/(1+r_j^d)=1\).

For completeness, this also yields a dimension proof avoiding any unverified infinite-matrix spectral assertion. If \(s>d\), the unique solution \(\lambda(s)\) is less than \(1\); the positive eigenvector \(v\) is bounded above and below, and \(\sum_jw_jv_j<\infty\). Consequently the \(s\)-sums of all length-\(n\) admissible cylinders decay at least geometrically like \(\lambda(s)^{n-1}\), establishing \(\dim_H K\le d\). If \(s<d\) and \(s>1/q\), a sufficiently large finite alphabet satisfies \(\sum_{j\le N}r_j^s/(1+r_j^s)>1\). Its irreducible finite graph-directed similarity set has pressure zero at an exponent greater than \(s\), and strong separation gives dimension greater than \(s\). Letting \(s\uparrow d\) proves \(\dim_H K\ge d\). The inequalities \(1/q<d<t<1\) follow because \(\sum_jw_j/(1+w_j)<\sum_jw_j\), and both series diverge at their convergence endpoint.

**3. Uniform singular derivative near \(q=1\).** Put \(\delta=q-1\), \(Z=\zeta(q)\), \(c=(1-\eta)/Z\), and
\[
U_q(s)=\sum_{j\ge1}r_j^s=c^s\zeta(qs),\qquad
V_q(s)=\sum_{j\ge1}\frac{r_j^s}{1+r_j^s}.
\]
As \(\delta\downarrow0\), \(Z\sim1/\delta\) and \(c\sim\delta\). For any fixed \(0<b<1\), the point \(s_b=1-b\delta\) satisfies \(q s_b-1\sim(1-b)\delta\), hence \(U_q(s_b)\to1/(1-b)>1\). Moreover, \(0\le U_q(s_b)-V_q(s_b)\le\sum_jr_j^{2s_b}=O(\delta^2)\). Therefore both roots lie between \(s_b\) and \(1\) for all small \(\delta\), for every fixed \(b\):
\[
1-t=o(\delta),\qquad 1-d=o(\delta).
\]
Uniformly for \(s\in[d,1]\), we have \(qs-1=\delta(1+o(1))\), and
\[
-\frac{d}{ds}U_q(s)
=c^s\left[q\bigl(-\zeta'(qs)\bigr)-\log(c)\zeta(qs)\right]
\sim\frac1\delta.
\]
Here \(-\zeta'(1+h)\sim h^{-2}\), while the logarithmic term has lower order \(O(\log(1/\delta))\). The derivative difference is bounded by
\[
0\le V_q'(s)-U_q'(s)
\le 2\sum_jr_j^{2s}|\log r_j|
=O\bigl(\delta^2\log(1/\delta)\bigr),
\]
where the displayed nonnegative difference follows by differentiating \(x/(1+x)\). Thus \(-V_q'(s)\sim1/\delta\) uniformly on \([d,1]\).

**4. Separate geometric and symbolic deficits.** Since \(U_q(t)=1\) and \(U_q(1)=1-\eta\), the mean-value theorem and Step 3 give
\[
1-t=\frac{\eta}{-U_q'(\xi_q)}\sim\delta\eta
\]
for some \(\xi_q\in[t,1]\). At \(s=t\), the exact spectral defect is
\[
1-V_q(t)=\sum_j\frac{r_j^{2t}}{1+r_j^t}.
\]
Because \(t=1-o(\delta)\), one has \(c^t\sim\delta\), \(qt=1+\delta(1+o(1))\), and
\[
\sum_j\frac{r_j^{2t}}{1+r_j^t}
=\sum_jr_j^{2t}+O\Bigl(\sum_jr_j^{3t}\Bigr)
\sim c^{2t}\zeta(2qt)\sim\frac{\zeta(2q)}{\zeta(q)^2}=S_2(q).
\]
The mean-value theorem applied to \(V_q(d)=1\) and \(V_q(t)=1-S_2(q)(1+o(1))\), together with the uniform derivative asymptotic, gives
\[
t-d\sim\delta S_2(q).
\]
Adding the two positive deficits proves the asserted uniform additive law. Finally \(S_2(q)\sim\zeta(2)\delta^2\), proving the cubic constant and leakage-versus-collision crossover. No finite computation or numerical extrapolation enters these deductions.

## Verification

The file `checker.py` (standard Python 3) checks the finite-alphabet Perron-vector identity exactly using rational arithmetic. It also approximates the Riemann zeta sums via Euler–Maclaurin expansion and calculates unrestricted and no-repeat dimensions at five decreasing values of \(q-1\), with a matched gap mass \(\eta=S_2/(1+S_2)\). The recorded file `checker_output.txt` ends with `NUMERICAL_DIAGNOSTICS_PASS`. These finite and floating-point checks corroborate the formulas but are **not** a computer-assisted proof of infinite-alphabet dimension or asymptotics; those are established in the preceding analytic argument.

## Relationship to prior work

Cunha, Novaes and Ponce (2026) study infinitely many isolated expanding branches with polynomially decaying inverse slopes, establishing coding and geometric properties for their invariant sets. The present family lies in that branch framework, but studies a new nearest-neighbor forbidden-return survivor with an exact root and a singular dimension comparison. The underlying finite-graph-directed dimension principle is classical and also appears in the conformal-IFS framework of Ghenciu and Pavlov, while the general restricted-digit setting has been studied for Lüroth expansions by van Golden, Kalle, Kombrink and Samuel. These broad frameworks are not claimed as new. The contribution is the **quantitative joint asymptotic** distinguishing leakage and an immediate-repeat exclusion, particularly its independent cubic collision coefficient. A pre-existing general perturbative pressure theorem may imply the asymptotic after specialization; identifying such a theorem remains a priority risk.

## Limitations

The result concerns a specified affine countable-branch family and nearest-neighbor exclusion. It does not cover all conformal countable Markov systems, arbitrary adjacency graphs, or fixed nonvanishing hole mass. The limit is taken as \(q\downarrow1\) with \(\eta(q)\downarrow0\), not at \(q=1\), where the Zipf probabilities cease to be normalizable. Hausdorff dimensions of closures are not asserted, and the numerical diagnostics are not certified infinite computations.

## References

1. M. G. C. Cunha, D. D. Novaes and G. Ponce, *Infinite-Piecewise Expanding Maps: Chaos, Ergodicity and Invariant-Set Complexity*, arXiv:2608.00398, first submitted 2026-08-01. https://arxiv.org/abs/2608.00398
2. A. E. Ghenciu and R. Pavlov, *The extended Hausdorff dimension spectrum of a conformal iterated function system is maximal*, arXiv:2308.15189, first submitted 2023-08-29. https://arxiv.org/html/2308.15189v1
3. S. van Golden, C. Kalle, S. Kombrink and T. Samuel, *Dimensions of infinitely generated self-affine sets and restricted digit sets for signed Lüroth expansions*, arXiv:2404.10749, first submitted 2024-04-16. https://arxiv.org/html/2404.10749v1
4. R. D. Mauldin and M. Urbański, *Dimensions and measures in infinite iterated function systems*, Proceedings of the London Mathematical Society 73 (1996), 105–154.
