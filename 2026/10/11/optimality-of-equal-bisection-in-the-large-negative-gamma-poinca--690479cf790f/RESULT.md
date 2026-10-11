# Optimality of equal bisection in the large-negative-\(\gamma\) Poincaré recurrence
## Finding
Let \(p\in[1,\infty)\), \(\gamma<-p\), and
\[
\beta=1+\frac{\gamma}{p}<0.
\]
For the unit cube \(Q_0=(0,1)^N\), a measurable function \(g:Q_0\to\mathbb R\), and a nonzero step \(h\in(-1,1)^N\), set
\[
Q_{0,h}=\{x\in Q_0:x+h\in Q_0\},\qquad
\Delta_hg(x)=g(x+h)-g(x),
\]
and use the quantities from Section 4 of Dai--Yang--Yuan--Zhao:
\[
\mathcal F(h)=\int_{Q_{0,h}}\left(|\Delta_hg(x)|^p-|h|^{p+\gamma}\right)_+\,dx,
\]
\[
M(h)=\left|\left\{x\in Q_{0,h}:|\Delta_hg(x)|>|h|^\beta\right\}\right|.
\]
Then
\[
\mathcal F(h)\le (2^{-\gamma}-1)|h|^{p+\gamma}M(h)+2^p\mathcal F(h/2).
\]
This improves the coefficient \(2^{|\gamma|}=2^{-\gamma}\) in Lemma 4.4 of arXiv:2610.04259v1 by retaining the full-step threshold that is subtracted in the definition of \(\mathcal F(h)\).

There is also an exact subdivision statement. Let \(m\ge2\), let \(t_1,\ldots,t_m>0\) satisfy \(\sum_i t_i=1\), and decompose the increment \(h\) into consecutive proportional substeps \(t_i h\). The weighted-convexity proof produces the threshold-surplus coefficient
\[
B_\gamma(t_1,\ldots,t_m)=\sum_{i=1}^m t_i^{\gamma+1}-1.
\]
Among all finite proportional subdivisions,
\[
B_\gamma(t_1,\ldots,t_m)\ge 2^{-\gamma}-1,
\]
and equality holds exactly for \(m=2\) and \(t_1=t_2=1/2\). Thus equal bisection is the unique optimal proportional subdivision for this recurrence mechanism.

## Assumptions and scope
The statement concerns \(p\in[1,\infty)\) and \(\gamma<-p\), exactly the large-negative-parameter regime treated by the iterative Section 4 argument of arXiv:2610.04259v1. No regularity of \(g\) is required beyond measurability. A substep is called proportional when it is a positive scalar multiple \(t_i h\) of the original step and the positive scalars sum to one.

The optimization statement is deliberately method-specific. It covers every finite proportional subdivision combined with the standard weighted convexity inequality for \(|\cdot|^p\). It does not claim optimality among unrelated decompositions, probabilistic schemes, non-proportional vector splittings, or different proofs of the Poincaré inequality.

## Proof
Write
\[
H=|h|^{p+\gamma}.
\]
On the exceedance set
\[
E_h=\{x\in Q_{0,h}:|\Delta_hg(x)|>|h|^\beta\},
\]
the positive part disappears and
\[
\mathcal F(h)=\int_{E_h}\left(|\Delta_hg(x)|^p-H\right)\,dx.
\]
For equal bisection, put
\[
A=|\Delta_{h/2}g(x)|,\qquad
C=|\Delta_{h/2}g(x+h/2)|.
\]
The triangle inequality and convexity give
\[
|\Delta_hg(x)|^p\le 2^{p-1}(A^p+C^p).
\]
The half-step threshold is
\[
H_2=|h/2|^{p+\gamma}=2^{-(p+\gamma)}H.
\]
For every nonnegative \(a\),
\[
a\le (a-H_2)_++H_2.
\]
Applying this to \(A^p\) and \(C^p\), and then subtracting the full threshold \(H\), yields
\[
|\Delta_hg(x)|^p-H
\le 2^{p-1}\left[(A^p-H_2)_++(C^p-H_2)_+\right]
 +(2^pH_2-H).
\]
The last coefficient is exact:
\[
2^pH_2-H=(2^{-\gamma}-1)H.
\]
Integrating over \(E_h\), enlarging the two half-step integration domains to the domains defining \(\mathcal F(h/2)\), and using \(|E_h|=M(h)\) gives
\[
\mathcal F(h)\le (2^{-\gamma}-1)HM(h)+2^p\mathcal F(h/2).
\]

For the general subdivision, let
\[
s_0=0,\qquad s_i=\sum_{j=1}^i t_j,
\]
and define the consecutive increments
\[
v_i=g(x+s_i h)-g(x+s_{i-1}h).
\]
Weighted convexity gives
\[
\left|\sum_{i=1}^m v_i\right|^p
\le \sum_{i=1}^m t_i^{1-p}|v_i|^p.
\]
The threshold corresponding to substep \(t_i h\) is
\[
|t_i h|^{p+\gamma}=t_i^{p+\gamma}H.
\]
After the same positive-part replacement, its contribution to the threshold term is therefore
\[
t_i^{1-p}t_i^{p+\gamma}H=t_i^{\gamma+1}H.
\]
Subtracting the full-step threshold gives exactly
\[
B_\gamma(t_1,\ldots,t_m)H
=\left(\sum_{i=1}^m t_i^{\gamma+1}-1\right)H.
\]
Thus the corresponding recurrence is
\[
\mathcal F(h)\le B_\gamma(t_1,\ldots,t_m)HM(h)
+\sum_{i=1}^m t_i^{1-p}\mathcal F(t_i h),
\]
with shifted domains bounded by the defining substep domains exactly as in the bisection proof.

Since \(\gamma<-p\le-1\), one has \(\gamma+1<0\). Hence \(r\mapsto r^{\gamma+1}\) is strictly convex on \((0,\infty)\). For fixed \(m\), Jensen's inequality gives
\[
\sum_{i=1}^m t_i^{\gamma+1}
\ge m\left(\frac1m\right)^{\gamma+1}
=m^{-\gamma},
\]
with equality if and only if all \(t_i=1/m\). Because \(-\gamma>0\), the quantity \(m^{-\gamma}\) is strictly increasing for integers \(m\ge2\). Therefore
\[
B_\gamma(t_1,\ldots,t_m)
\ge m^{-\gamma}-1
\ge 2^{-\gamma}-1,
\]
and equality in the global bound occurs exactly at the equal bisection.

## Verification
Every step is symbolic and valid for all parameters in the stated range. The identity
\[
2^p|h/2|^{p+\gamma}-|h|^{p+\gamma}
=(2^{-\gamma}-1)|h|^{p+\gamma}
\]
checks the sharpened bisection coefficient directly. The general threshold coefficient follows from the exact exponent cancellation
\[
t_i^{1-p}t_i^{p+\gamma}=t_i^{\gamma+1}.
\]
Strict convexity follows from
\[
\frac{d^2}{dr^2}r^{\gamma+1}
=(\gamma+1)\gamma r^{\gamma-1}>0,
\]
because both \(\gamma+1\) and \(\gamma\) are negative. No finite experiment or numerical extrapolation is used as evidence for the quantified claim.

## Relationship to prior work
Dai, Yang, Yuan, and Zhao prove the large-negative-\(\gamma\) Poincaré inequality by successively halving increments. Their Lemma 4.4 states
\[
\mathcal F(h)\le 2^{|\gamma|}|h|^{p+\gamma}M(h)+2^p\mathcal F(h/2),
\]
and their Theorem 4.1 obtains a global upper constant of order \(8^{|\gamma|}\). Their Section 5.1 separately proves that the least Poincaré constant grows at least linearly in \(|\gamma|\). The sharpened local recurrence above is not stated there, nor is the optimization over finite proportional subdivisions.

Nguyen's 2025 survey and research article formulates the broader nonlocal Poincaré problem that motivated the 2026 theorem and develops the surrounding Sobolev/BV theory. The inspected Section 8 does not contain the large-negative-parameter halving recurrence or the proportional-subdivision optimization proved here.

Targeted publication-index searches for the exact coefficient, proportional subdivision, weighted-convexity recurrence, and equivalent threshold formulations located no statement implying the result. The strongest remaining originality risk is that the elementary coefficient optimization may have appeared implicitly in older inequality folklore under terminology not indexed by these searches.

## Limitations
The result is a sharp statement about the threshold-surplus term in a specific recurrence class. It does not prove that the least global Poincaré constant grows exponentially in \(|\gamma|\), and it does not close the gap between the source's linear lower bound and exponential upper bound. Indeed, the source proof contains other large-negative-\(\gamma\) losses, including a geometric factor involving \(r_0^{p+\gamma}\), so the coefficient improvement alone does not change the global asymptotic order established there.

No claim is made for infinite subdivisions, non-proportional vector decompositions, or a different proof architecture.

## References
1. Feng Dai, Dachun Yang, Wen Yuan, Yirui Zhao, *Sharp Poincaré Inequalities for Families of Nonlocal Nonconvex Functionals*, arXiv:2610.04259v1, 2026. In particular Section 4, Lemma 4.4 and Theorem 4.1, and Section 5.1.
2. Hoai-Minh Nguyen, *Characterizations of the Sobolev norms and the total variation via nonlocal functionals, and related problems*, arXiv:2507.00842v1, 2025.
