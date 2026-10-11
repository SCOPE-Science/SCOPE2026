# Exponential-alphabet crossover for Zipf-normalized expanding maps

## Finding
Fix a retained-length fraction \(0<\lambda<1\). For each \(q>1\), let \(p_n(q)=n^{-q}/\zeta(q)\) and \(c(q)=\lambda/\zeta(q)\). Consider the countable, piecewise-affine expanding map defined in the next section, with inverse contraction ratios \(r_n(q)=c(q)n^{-q}\). Write \(s_N(q)\) for the Hausdorff dimension of its survivor with symbols restricted to \(\{1,\ldots,N\}\), \(N\ge2\), and \(s_\infty(q)\) for the full countable-symbol survivor.

**Exact dimensions.** The dimensions are uniquely specified by
\[
\sum_{n=1}^N r_n(q)^{s_N(q)}=1,\qquad
\bigl(c(q)\bigr)^{s_\infty(q)}\zeta(qs_\infty(q))=1.
\]
In particular \(0<s_N(q)<s_\infty(q)<1\) and \(1/q<s_\infty(q)\).

**Exponential cutoff crossover.** Set \(q=1+\varepsilon\), and for every fixed \(\tau>0\) put \(N_\varepsilon=\lfloor\exp(\tau/\varepsilon)\rfloor\). There is exactly one \(a_\lambda(\tau)>0\) solving
\[
\lambda\int_0^\tau\exp\!\bigl((a_\lambda(\tau)-1)t\bigr)\,dt=1.
\]
As \(\varepsilon\downarrow0\),
\[
\boxed{\displaystyle
s_{N_\varepsilon}(1+\varepsilon)
=1-\varepsilon a_\lambda(\tau)
+O_{\lambda,\tau}\bigl(\varepsilon^2|\log\varepsilon|\bigr),\qquad
s_\infty(1+\varepsilon)
=1-(1-\lambda)\varepsilon
+O_\lambda\bigl(\varepsilon^2|\log\varepsilon|\bigr).}
\]
These error bounds are uniform when \(\lambda\) and \(\tau\) range over fixed compact subintervals of \((0,1)\) and \((0,\infty)\), respectively. The continuum phase is strictly decreasing in \(\tau\), has \(a_\lambda(\tau)>1-\lambda\) at every finite \(\tau\), and decreases to \(1-\lambda\) as \(\tau\to\infty\). Moreover,
\[
\boxed{\quad a_\lambda(\tau)\gtrless 1\quad\Longleftrightarrow\quad\tau\lessgtr1/\lambda.\quad}
\]
Consequently for each fixed \(\tau\ne1/\lambda\), all sufficiently small \(\varepsilon>0\) satisfy
\[
\operatorname{sgn}\!\left(s_{N_\varepsilon}(1+\varepsilon)-\frac1{1+\varepsilon}\right)
=\operatorname{sgn}(\lambda\tau-1).
\]
At the threshold \(\tau=1/\lambda\), only the leading crossover equality is asserted. For each fixed \(N\ge2\), \(s_N(1+\varepsilon)\to0\), whereas \(s_\infty(1+\varepsilon)\to1\). Thus the two orders of the alphabet-size and critical-exponent limits disagree. At every finite \(\tau>0\), the dimension gap has a strictly positive, explicit first-order coefficient:
\[
\lim_{\varepsilon\downarrow0}
\frac{s_\infty(1+\varepsilon)-s_{N_\varepsilon}(1+\varepsilon)}{\varepsilon}
=a_\lambda(\tau)-(1-\lambda)>0.
\]

## Assumptions and scope
For every \(q>1\), define \(P_n=\sum_{k=1}^np_k(q)\), \(P_0=0\), and closed intervals
\[
I_n=[P_n-\lambda p_n(q),P_n]\subset[0,1],\quad n\ge1.
\]
Their lengths are \(r_n(q)=\lambda p_n(q)\), and the positive gap between successive intervals is \((1-\lambda)p_n(q)\) for \(n\ge2\). The leftmost interval is separated from zero by \((1-\lambda)p_1(q)\); the intervals accumulate at one. Define the expanding branch map \(T_q:\bigcup_{n\ge1}I_n\to[0,1]\) by
\[
T_q(x)=\frac{x-[P_n-\lambda p_n(q)]}{\lambda p_n(q)}\quad(x\in I_n).
\]
Each inverse branch is the similarity \(\psi_n(x)=P_n-\lambda p_n(q)+r_n(q)x\). The *full survivor* is the set of points with infinite valid \(T_q\)-itineraries, equivalently the image of all sequences in \(\mathbb N^{\mathbb N}\) under the contraction coding. The *finite survivor* restricts the itineraries to \(\{1,\ldots,N\}^{\mathbb N}\). Hausdorff dimension is computed in the ordinary Euclidean metric. These are separated similarities with no distortion; the alphabet truncation changes the allowed itineraries, not the branch lengths or the normalizing denominator.

All asymptotic assertions keep \(\lambda\) and \(\tau\) fixed while \(\varepsilon\to0^+\). No claim is made about the first correction exactly at \(\tau=1/\lambda\), nor about perturbations that renormalize the truncated weights.

## Proof
**1. Geometric coding and pressure roots.** The first-level interval images are disjoint, because \(P_n-\lambda p_n-P_{n-1}=(1-\lambda)p_n>0\) for \(n\ge2\); their total length is \(\lambda<1\). Their derivatives are the positive constants \(r_n=c(q)n^{-q}\), all below \(\lambda<1\), so infinite compositions converge. For a finite alphabet, the open set condition and elementary similarity dimension theorem identify the Hausdorff dimension with the unique zero of \(\sum_{n\le N}r_n^s-1\). (Equivalently: the level-\(k\) cylinder intervals give the upper bound, and the finite Bernoulli self-similar measure with weights \(r_n^{s_N}\), together with the positive finite-alphabet separation, gives the matching Frostman lower bound.) At \(s=0\) the sum is \(N>1\), and at \(s=1\) it is at most \(\lambda<1\), proving uniqueness in \((0,1)\).

For the full alphabet, \(\sum_{n\ge1}r_n^s=c(q)^s\zeta(qs)\) is finite precisely for \(s>1/q\), diverges as \(s\downarrow1/q\), and equals \(\lambda<1\) at \(s=1\). It therefore has a unique root \(s_\infty\in(1/q,1)\). For every \(s>s_\infty\), the level-\(k\) cylinders cover the infinite-coded set with total \(s\)-volume \((\sum_n r_n^s)^k\to0\), proving \(\dim_H\Lambda_\infty\le s_\infty\). On the other hand, the finite roots increase to \(s_\infty\), by monotonicity and uniform convergence of \(\sum_n r_n^s\) on any compact subinterval of \((1/q,\infty)\). Since every finite-coded limit set is included in the infinite-coded set, its Hausdorff dimension is at least \(\sup_Ns_N=s_\infty\). Strictly \(s_N<s_\infty\), because a finite sum at the infinite root is strictly below one.

**2. Uniform harmonic-sum limit.** Write \(q=1+\varepsilon\) and test a bounded parameter \(a\) through \(s=1-a\varepsilon\). For \(a\) in any fixed bounded interval, the normalization satisfies
\[
\zeta(1+\varepsilon)=\varepsilon^{-1}+O(1),\qquad
c(1+\varepsilon)^{1-a\varepsilon}=\lambda\varepsilon\bigl(1+O(\varepsilon|\log\varepsilon|)\bigr).
\]
Also \(qs=1+\varepsilon(1-a-a\varepsilon)\). Put \(u=1-a-a\varepsilon\). For bounded \(u\) and fixed \(\tau>0\), the decreasing-function integral comparison (valid for small \(\varepsilon\) since \(1+u\varepsilon>0\)) gives
\[
\left|\sum_{n=1}^{N_\varepsilon}n^{-1-u\varepsilon}
-\int_1^{N_\varepsilon}x^{-1-u\varepsilon}\,dx\right|\le1.
\]
Making the substitution \(t=\varepsilon\log x\) shows, uniformly for bounded \(u\),
\[
\varepsilon\sum_{n=1}^{N_\varepsilon}n^{-1-u\varepsilon}
=\int_0^{\tau}e^{-ut}\,dt+O(\varepsilon),
\]
where \(\varepsilon\log N_\varepsilon=\tau+O(\varepsilon e^{-\tau/\varepsilon})\). Consequently the finite pressure sum at \(s=1-a\varepsilon\) equals
\[
\lambda\int_0^\tau e^{(a-1)t}\,dt+O_{\lambda,\tau}(\varepsilon|\log\varepsilon|).
\]
The continuum expression is strictly increasing in \(a\), with derivative \(\lambda\int_0^\tau t e^{(a-1)t}\,dt>0\). Its value at \(a=0\) is \(\lambda(1-e^{-\tau})<1\), while it diverges as \(a\to\infty\). Its unique positive root \(a_\lambda(\tau)\) can thus be bracketed by two fixed bounded values. Uniform convergence and the derivative lower bound on this bracket show that the *finite* pressure root has parameter \(a_\varepsilon=a_\lambda(\tau)+O(\varepsilon|\log\varepsilon|)\). Multiplying by \(\varepsilon\) proves the asserted finite-dimension expansion.

**3. Infinite-alphabet limit.** In a fixed neighborhood of \(a=1-\lambda\), put \(u=1-a-a\varepsilon>0\). Since \(\zeta(1+u\varepsilon)=(u\varepsilon)^{-1}+O(1)\) uniformly there, the infinite pressure at \(s=1-a\varepsilon\) is
\[
\frac{\lambda}{1-a}+O_\lambda(\varepsilon|\log\varepsilon|).
\]
Its leading value crosses one uniquely and transversely at \(a=1-\lambda\). Monotonicity of the exact pressure as a function of \(s\), together with a fixed bracket around this point, proves \(1-s_\infty=(1-\lambda)\varepsilon+O_\lambda(\varepsilon^2|\log\varepsilon|)\).

**4. Threshold, gap and noncommuting limits.** For fixed \(\tau\), the phase integral increases strictly with \(a\) and \(\tau\). At \(a=1\) its value is \(\lambda\tau\), proving the phase threshold. At \(a=1-\lambda\) it is \(1-e^{-\lambda\tau}<1\), so the phase root lies strictly above \(1-\lambda\) for finite \(\tau\). Its strict monotonicity and monotone convergence of the integral imply \(a_\lambda(\tau)\downarrow1-\lambda\). The difference from the natural convergence exponent \(1/q=1-\varepsilon+O(\varepsilon^2)\) has first-order sign \(1-a_\lambda(\tau)\), proving the threshold away from equality. Finally, for every fixed finite \(N\) and fixed \(s>0\), each ratio \(r_n(1+\varepsilon)=\lambda n^{-1-\varepsilon}/\zeta(1+\varepsilon)\to0\); hence \(\sum_{n\le N}r_n^s\to0\) and \(s_N(1+\varepsilon)\to0\). The full-alphabet asymptotic gives its contrasting limit one and the claimed first-order dimension gap.

## Verification
The standalone script `verify_crossover.py` checks exact affine-interval gaps, finite-dimensional pressure roots using Hurwitz zeta subtraction for extremely large \(N\), infinite pressure roots, and the strict sides of the phase threshold. It completed 87 numerical diagnostics with arbitrary-precision arithmetic. These finite numerical checks test the identities but do not constitute the proof of limits or novelty. To reproduce, install `mpmath` (tested with version 1.3.0) and run `python verify_crossover.py` from the extracted package directory. The proof above, not this computation, covers all real \(\lambda\), \(q\), \(\tau\), and all sufficiently small \(\varepsilon\) in the stated quantifiers.

## Relationship to prior work
The broad conformal-IFS pressure formula and its finite-subsystem connection are classical: Mauldin and Urbański (1996) establish dimension through pressure for infinite conformal systems. Thus the two implicit pressure equations above are **not** claimed as new general principles. Das and Simmons (2022) analyze Hausdorff dimension spectra of subsystems, but not this normalized harmonic-singularity/exponential-cutoff asymptotic. Cunha, Novaes and Ponce (2026) study countably branched expanding maps, giving general dimension bounds and in Appendix B.1 a different affine construction with geometrically blocked contraction ratios. Their hypotheses motivate examining a power-law branch-size family at the borderline \(q\downarrow1\). The present result concerns the explicit exponential truncation scale, its phase integral, a sharp crossing of the convergence exponent, and the first-order truncation bias; these are not supplied as stated by the source theorems. They require the separate uniform near-pole asymptotic above. No assertion of exhaustive literature priority is made.

## Limitations
This is an exactly solvable similarity model; its asymptotics are not asserted for general nonlinear expanding maps, variable distortion, arbitrary slowly varying branch-size factors, or cutoff-dependent renormalization. The error constant depends on fixed compact parameter ranges, and no boundary sign is claimed when \(\tau=1/\lambda\). Full-space Hausdorff dimension is considered, not box dimension or convergence rates of invariant measures. An equivalent uniform double-scaling analysis in other literature remains a residual originality risk. Numerical tests are finite diagnostics only.

## References
1. M. G. C. Cunha, D. D. Novaes and G. Ponce, *Infinite-Piecewise Expanding Maps: Chaos, Ergodicity and Invariant-Set Complexity*, arXiv:2608.00398v1 (first public version, 2026-08-01), particularly Theorem A, Section 2, and Appendix B.1. https://arxiv.org/abs/2608.00398
2. R. D. Mauldin and M. Urbański, *Dimensions and Measures in Infinite Iterated Function Systems*, Proc. Lond. Math. Soc. 73 (1996), 105–154, DOI:10.1112/plms/s3-73.1.105. Author-hosted manuscript: https://www.urbanskimath.com/wp-content/uploads/2014/01/34_Urbanski.pdf
3. T. Das and D. Simmons, *On the dimension spectra of infinite conformal iterated function systems*, J. Fractal Geom. 9 (2022), 73–87, DOI:10.4171/JFG/112. https://arxiv.org/abs/1910.10259
