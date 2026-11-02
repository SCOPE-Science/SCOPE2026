# Sharp symmetry breaking at six draws in three-colour expiring coupon flux

## Finding

Consider a stationary iid three-symbol sequence whose symbol probabilities are \(p=(p_1,p_2,p_3)\), and let \(\mu_M(p)\) be the probability that the newest length-\(M\) window contains all three symbols while its predecessor does not. For every integer \(M\ge3\), the following exact sharp transition holds:

1. For \(M=3,4,5\), the unique maximizing probability vector is \((1/3,1/3,1/3)\).
2. For **every** integer \(M\ge6\), the uniform vector is a strict local minimum of \(\mu_M\) relative to the two-dimensional probability simplex. In particular, it is not a maximizer.
3. At the first broken-symmetry length \(M=6\), the *complete set* of global maximizers consists of the three permutations of \((a_*,a_*,1-2a_*)\), where \(a_*\) is the unique root in \((1/5,1/4)\) of
   \[
   42a^4-40a^3+35a^2-15a+2=0.
   \]
   Numerically \(a_*=0.240860803475815\ldots\), and the maximum flux is \(0.084298746260378\ldots\), strictly above the uniform flux \(20/243\).

The optimization concerns **stationary new-entry frequency**, not the distribution or mean of the first completion time starting from an empty collection.

## Assumptions and scope

Let \((X_t)_{t\in\mathbb Z}\) be iid on \(\{1,2,3\}\), with \(p_i=\Pr(X_t=i)\ge0\) and \(\sum_i p_i=1\). For an integer \(M\ge3\), define \(W_t=(X_{t-M+1},\ldots,X_t)\), and \(A_M\) as the event that \(W_t\) contains all three symbols. Define
\[
\mu_M(p)=\Pr(W_{t-1}\notin A_M,\ W_t\in A_M).
\]
All derivative claims refer to the relative interior of the closed simplex; the boundary has zero entry flux. Put \(e_2=p_1p_2+p_1p_3+p_2p_3\) and \(e_3=p_1p_2p_3\).

## Proof

**1. Exact entry identity.** A new complete window after an incomplete predecessor requires a unique missing symbol \(i\) in the common block of length \(M-1\); the entering symbol must be \(i\) and the departing symbol must differ from \(i\). With \(\{i,j,k\}=\{1,2,3\}\), independence and inclusion-exclusion give
\[
\mu_M(p)=\sum_{i=1}^3 p_i(1-p_i)\left[(1-p_i)^{M-1}-p_j^{M-1}-p_k^{M-1}\right]. \tag{1}
\]
This identity extends continuously to the closed simplex. In particular, it vanishes on every face \(p_i=0\). The first four useful symmetric-polynomial reductions, valid since \(\sum p_i=1\), are
\[
\begin{aligned}
\mu_3&=4e_3,\\
\mu_4&=6e_3(1-e_2),\\
\mu_5&=2e_3(4-7e_2-3e_3),\\
\mu_6&=5e_3(2e_2^2-5e_2-3e_3+2). \tag{2}
\end{aligned}
\]

**2. Global uniform optimum for lengths three through five.** For a symmetric differentiable function \(F(e_2,e_3)\) on the simplex, along a transfer between coordinates \(x\) and \(y\), with third coordinate \(z\),
\[
\frac{\partial F}{\partial x}-\frac{\partial F}{\partial y}=-(x-y)(F_{e_2}+zF_{e_3}). \tag{3}
\]
For \(M=3\), the bracket is \(4z\). For \(M=4\), it is \(6z[1-e_2-xy]\), strictly positive when \(x,y,z>0\): indeed \(e_2+xy=z(1-z)+2xy\le 1/4+1/2<1\). For \(M=5\), it is
\[
2z[4-7(e_2+xy)-6e_3]
=2z[4-7z(1-z)-(14+6z)xy].
\]
As \(xy\le(1-z)^2/4\), the inner bracket is at least
\[
\frac{1-3z+13z^2-3z^3}{2}
\ge\frac{1-3z+10z^2}{2}>0 \qquad (0\le z\le1),
\]
where the final quadratic is strictly positive because its discriminant is negative. Equation (3) therefore satisfies the strict Schur-concavity criterion at each of the three lengths. Every nonuniform positive vector is strictly improved by finite pairwise balancing transfers; the boundary has zero flux. The unique global maximum is uniform.

**3. Universal local instability for lengths at least six.** Write \(u=(1/3,1/3,1/3)\). For any real tangent vector \(h\) with \(\sum_i h_i=0\), Taylor expansion of (1) at \(u\) gives
\[
\mu_M(u+th)=\mu_M(u)+\frac{Q_M}{2\cdot3^M}\,t^2\sum_i h_i^2+O_{M,h}(t^3),
\quad Q_M=3\cdot2^{M-2}M(M-5)-12M^2+42M-18. \tag{4}
\]
The linear term vanishes by symmetry. Direct calculation gives \(Q_6=90>0\), and
\[
Q_{M+1}-2Q_M=3\cdot2^M(M-2)+12M^2-66M+48>0\qquad(M\ge6).
\]
Thus \(Q_M>0\) for every integer \(M\ge6\). The uniform vector is a strict local minimum on the simplex for all such lengths, in every nonzero tangent direction.

**4. Complete first asymmetric optimum at length six.** By (2), write \(F(e_2,e_3)=5e_3(2e_2^2-5e_2-3e_3+2)\). On the open simplex,
\[
F_{e_2}=5e_3(4e_2-5)<0,
\]
since \(e_2\le1/3\). At an interior critical point with all three coordinates distinct, applying (3) to every pair would require \(F_{e_2}+p_iF_{e_3}=0\) for each \(i\), whence \(F_{e_2}=F_{e_3}=0\), a contradiction. Therefore any nonuniform maximizer has two equal coordinates.

Write \(p=(a,a,1-2a)\) for \(0<a<1/2\). Its flux and derivative factor as
\[
\begin{aligned}
G(a)&=-10a^2(2a-1)(9a^4-9a^3+10a^2-5a+1),\\
G'(a)&=-10a(3a-1)Q(a),\\
Q(a)&=42a^4-40a^3+35a^2-15a+2. \tag{5}
\end{aligned}
\]
Here \(Q''(a)=2(252a^2-120a+35)>0\) for every real \(a\). The exact signs \(Q(0)>0\), \(Q(1/3)<0\), \(Q(1/2)>0\) yield exactly two simple roots on \((0,1/2)\): \(a_*\in(1/5,1/4)\) and \(a_+\in(1/3,3/8)\). Thus the only interior stationary possibilities, up to permutation, are these two and the uniform vector.

The root \(a_+\) is not a local maximum on the full simplex. Indeed, perturb \((a,a,b)\) to \((a+t,a-t,b)\), with \(b=1-2a\). To second order, \(e_2\) decreases by \(t^2\) and \(e_3\) by \(bt^2\), so
\[
F(a+t,a-t,b)-F(a,a,b)=-(F_{e_2}+bF_{e_3})t^2+O(t^4).
\]
At \(b=1-2a\), the bracket equals
\[
10(1-2a)R(a),\qquad R(a)=3a^4-2a^3+6a^2-5a+1.
\]
Because \(R''(a)=12(3a^2-a+1)>0\) and \(R(1/3)=-1/27\), \(R(1/2)=-1/16\), convexity puts \(R<0\) throughout \([1/3,1/2]\). Hence the displayed perturbation increases the flux at \(a_+\). The uniform point is a strict local minimum by step 3. On the compact simplex a positive global maximum exists in the interior; its only remaining possible form is a permutation of \((a_*,a_*,1-2a_*)\). These three points are therefore all and only the global maxima.

## Verification

The standalone `verify.py` uses exact symbolic algebra and an independent enumeration of all three-colour words of lengths \(M+1\) for \(M=3,4,5,6\). It checks the entry identity against the word enumeration, the four symmetric reductions, exchange derivatives, the uniform-Hessian formula at thirteen different lengths, the induction algebra, and the quartic stationary-point reductions. Run `python verify.py` with Python 3.10+ and SymPy 1.12+. The provided `verification_output.txt` is the recorded output. The infinite-length local-instability result is proved by the analytic induction above, not inferred from those finite checks.

## Relationship to prior work

Long's 2026 expiring-coupon work derives stationary entry flux for **uniform** coupon probabilities and asymptotic hitting laws; the event characterization in its Theorem 3.1 motivates (1), but it does not state the finite-horizon optimization over nonuniform probability vectors. An earlier fixed-alphabet asymptotic nonuniform-flux analysis gives the large-window scale but does not imply the exact first window of symmetry breaking or classify the finite-six optimizer. Classical nonuniform coupon-collector and structured-covering studies predominantly treat monotone first-coverage statistics, not the stationary new-entry event studied here.

## Limitations

This is a fixed three-type theorem. Global maximizers are classified for \(M=3,4,5,6\), but not for arbitrary \(M\ge7\); only the strict local failure of uniform sampling is proved for the latter lengths. The entry frequency need not equal the reciprocal of the expected hitting time from an empty start at finite dimension. Historical priority outside inspected and indexed literature is not independently certified. Numerical values are illustrative and are not a substitute for the algebraic proof.

## References

1. C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1 (first posted 2026-04-29), https://arxiv.org/abs/2604.26298.
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511 (2026), https://arxiv.org/abs/2605.14511.
3. N. B. Shank and H. Yang, *Coupon Collector Problem for Non-Uniform Coupons and Random Quotas*, Electronic Journal of Combinatorics 20 (2013), #P33, https://doi.org/10.37236/3348.
4. *Speed and concentration of the covering time for structured coupon collectors*, Advances in Applied Probability 52 (2020), 433–462, https://doi.org/10.1017/apr.2020.5.
