# A sharp gain-two limit to stability rescue by symmetric sampling jitter

## Finding
For the scalar sampled-data feedback plant defined below, independent, equiprobable perturbation of every sample interval about a prescribed mean can restore mean-square stability even when *periodic sampling at that same mean* is unstable. **Such a rescue is possible if and only if the fixed feedback gain satisfies \(1<k<2\).** At and above gain \(k=2\), no amplitude of positive, symmetric two-point timing jitter can restore mean-square stability once the periodic sampling interval reaches its instability boundary. This is a precise distinction between stochastic sampling and worst-case robust sampling.

More explicitly, let
\[
 h_{\mathrm{per}}(k)=\log\frac{k+1}{k-1},\qquad k>1.
\]
For \(0<d<h\), choose independent intervals \(H_j=h+d\) or \(h-d\), each with probability \(1/2\). Put \(q=e^{-h}\) and \(c=\cosh d\). At the sampling instants, the exact mean-square factor is
\[
 V(k,h,d)=k^2-2k(k+1)qc+(k+1)^2q^2(2c^2-1).
\]
Mean-square exponential decay occurs exactly when \(V<1\); at \(V=1\) the second moment is constant, and at \(V>1\) it grows geometrically for nonzero initial condition. Thus the **complete parameter criterion** is the explicit strict quadratic inequality
\[
 (k+1)^2(2c^2-1)q^2-2k(k+1)cq+k^2-1<0,
 \qquad 0<d<h,\ k>1.
\]
The rescue statement is
\[
 \bigl[\exists h>h_{\mathrm{per}}(k),\ 0<d<h:\ V(k,h,d)<1\bigr]
 \quad\Longleftrightarrow\quad 1<k<2.
\]
The periodic comparator is strictly unstable for every \(h>h_{\mathrm{per}}(k)\), not merely marginal.

As a fully exact witness, choose \(k=3/2\), \(h=\log(100/19)\), and \(d=\operatorname{arcosh}(6/5)\). Then \(0<d<h\) and \(h>\log5=h_{\mathrm{per}}(3/2)\), while
\[
 V=\frac{38567}{40000}<1,
 \qquad \bigl((k+1)e^{-h}-k\bigr)^2=\frac{1681}{1600}>1.
\]
Thus *the same mean interval* (and hence the same asymptotic sampling rate), with independently randomized positive intervals, changes an unstable periodic sampled recursion into a mean-square geometrically convergent sampled recursion.

## Assumptions and scope
The continuous plant is \(\dot x(t)=-x(t)+u(t)\) with scalar real state and zero-order-hold static feedback \(u(t)=-k x(t_j)\) for \(t_j\le t<t_{j+1}\), where \(k>1\), \(t_0=0\), and \(t_{j+1}-t_j=H_j\). The intervals are independent and identically distributed, equiprobable on the two *positive* values \(h-d\) and \(h+d\), with \(h>d>0\), and independent of the initial state. The gain \(k\) is fixed, not retuned with each realized interval. All conclusions concern mean-square stability **indexed by the sample count** \(j\) at the random times \(t_j\), with deterministic, nonzero initial state. They do not assert a per-unit-physical-time exponent or an arbitrarily distributed jitter law.

## Proof
**1. Exact sample-to-sample multiplier.** Solving the forced scalar differential equation over one held interval gives
\[
 x(t_j+\tau)=\bigl[(k+1)e^{-\tau}-k\bigr]x(t_j),\qquad 0\le\tau\le H_j.
\]
Consequently \(X_{j+1}=M_k(H_j)X_j\), where \(X_j=x(t_j)\) and \(M_k(s)=(k+1)e^{-s}-k\). Independence implies
\[
 \mathbb E(X_j^2)=X_0^2\bigl(\mathbb E M_k(H)^2\bigr)^j=X_0^2V^j.
\]
Using \(\mathbb E e^{-H}=q\cosh d=qc\) and \(\mathbb E e^{-2H}=q^2\cosh(2d)=q^2(2c^2-1)\) yields the displayed exact expression for \(V\). This proves its exhaustive mean-square classification, including equality.

**2. Periodic stability and gain-dependent local jitter effect.** For \(k>1\), \(M_k(h)<1\) at every positive \(h\); the other strict Schur inequality \(M_k(h)>-1\) is equivalent to \(h<h_{\mathrm{per}}(k)\). Put \(q_0=(k-1)/(k+1)\). Direct factorization at the periodic frontier gives
\[
 V(k,h_{\mathrm{per}},d)-1
 =2(k-1)(c-1)\bigl((k-1)c-1\bigr).
\]
If \(1<k<2\), choose \(d>0\) sufficiently small to satisfy both \(d<h_{\mathrm{per}}\) and \(1<c<1/(k-1)\). The right side is strictly negative. By continuity, the *same* \(d\) has \(V<1\) for all \(h>h_{\mathrm{per}}\) in a small nonempty right-neighborhood of the boundary, with \(d<h\). The corresponding periodic steps are unstable.

**3. Sharp universal non-rescue at gains \(k\ge2\).** Suppose, aiming for a contradiction, that \(k\ge2\), \(h\ge h_{\mathrm{per}}(k)\), and \(V<1\). Define positive numbers
\[
 A=(k+1)e^{-(h+d)},\quad B=(k+1)e^{-(h-d)},\quad u=A-k,\quad v=B-k.
\]
Then \(u^2+v^2=2V<2\). With \(s=u+v\), Cauchy--Schwarz gives \(-2<s<2\), and
\[
 uv=\frac{s^2-u^2-v^2}{2}>\frac{s^2-2}{2}.
\]
It follows that
\[
 AB=k^2+ks+uv>k^2-1+ks+\frac{s^2}{2}.
\]
The final quantity exceeds \((k-1)^2\), since its difference is exactly
\[
 \frac{(s+2)(2k+s-2)}{2}>0
 \qquad (k\ge2,\ -2<s<2).
\]
But \(AB=(k+1)^2e^{-2h}\le(k-1)^2\), by the assumed lower bound on \(h\). Contradiction. Hence \(V\ge1\) for every admissible two-point jitter at and beyond the periodic boundary when \(k\ge2\). This includes \(k=2\) and proves sharpness of the cutoff.

**4. Optional explicit root chart.** Set \(\Delta=(k^2-1)-(k^2-2)c^2\). When \(\Delta>0\), define
\[
 q_\pm=\frac{kc\pm\sqrt\Delta}{(k+1)(2c^2-1)}.
\]
For \(k>1\) these are positive and the complete stability region is \(q_-<e^{-h}<q_+\), subject also to \(h>d>0\). When \(\Delta\le0\), the quadratic is nonnegative for all \(q\), so no strict mean-square stability is possible for that chosen jitter magnitude. The roots follow from the quadratic formula; their product is positive and sum is positive. Equality at a root gives neutral second moment.

## Verification
`verify.py` uses SymPy to verify symbolically the exponential-moment identity, the discriminant, the periodic-boundary factorization and the non-rescue algebraic certificate. It checks the exact rational witness and additionally evaluates 42,000 rational parameter points at and beyond the periodic boundary for \(k\ge2\). To reproduce, install the package listed in `requirements.txt` and execute `python verify.py` from the extracted directory. The analytical sign proof in Step 3 and continuity proof in Step 2, not the finite test grid, establish the quantified theorem.

## Relationship to prior work
Jin, Wang and Wang's 2022 study of enhancing the average sampling interval by mixing shorter and longer periods establishes the broad practical motivation; its accessible abstract describes sufficient stability conditions, not the exact symmetric iid mean-preserving scalar gain-two necessity-and-sufficiency frontier proved here. Li, Zhang, Zhang and Cai's 2013 open-access paper analyzes random periods through finite-state Markov chains, delay-dependent feedback and Lyapunov matrix inequalities; its Theorems 6 and 8 cover implicit general stability tests, not this sharp elementary fixed-gain mean-rescue classification. Mustafa and Chen's 2013 work develops robust stability across *all* allowed intervals using output-feedback LMIs, a logically different quantifier from mean-square stability under iid equal probabilities. Wang and Zhu's 2023 paper considers stochastic sampled control through Poisson-counter timing and optimal control, rather than this binary equal-mean comparison.

## Limitations
The threshold \(k=2\) belongs to this *specific* plant normalization, fixed sample-and-hold feedback, equiprobable symmetric **two-point** interval law and sample-indexed mean-square criterion; it is not invariant under arbitrary plant scalings without renormalization, unequal probabilities or general sampling laws. The theorem does not claim uniform robust stability across interval realizations: the short and long multipliers need not both be contractive. The existence half gives an open interval beyond the periodic boundary but does not optimize the achievable extra mean interval, physical-time decay or control cost. Inaccessible full texts of closely related 2022 and 2023 studies leave a specialized prior-publication risk; no independent validation is asserted.

## References
1. C.-L. Jin, Q.-G. Wang and R. Wang, *Exponential stability of sampled-data control systems with enhanced average sampling interval*, International Journal of Control 96 (2023), 1744–1753; first available online May 3, 2022. https://doi.org/10.1080/00207179.2022.2069051.
2. Y. Li, Q. Zhang, S. Zhang and M. Cai, *Stabilization for Networked Control Systems with Random Sampling Periods*, Journal of Applied Mathematics (2013), article 252679. https://doi.org/10.1155/2013/252679.
3. G. Mustafa and T. Chen, *Stabilisation of non-uniformly sampled systems via dynamic output-feedback control*, IET Control Theory & Applications 7 (2013), 228–233. https://doi.org/10.1049/iet-cta.2012.0355.
4. G. Wang and Z. Zhu, *Optimal control of sampled-data systems based on an optimized stochastic sampling*, International Journal of Robust and Nonlinear Control 33 (2023), 4304–4325; first published January 20, 2023. https://doi.org/10.1002/rnc.6609.
5. B. Tang, Q.-J. Zeng, D.-F. He and Y. Zhang, *Random Stabilization of Sampled-data Control Systems with Nonuniform Sampling*, International Journal of Automation and Computing 9 (2012), 492–500. https://doi.org/10.1007/s11633-012-0672-y.
