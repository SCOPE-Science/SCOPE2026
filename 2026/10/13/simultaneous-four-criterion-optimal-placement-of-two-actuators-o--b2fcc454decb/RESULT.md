# Simultaneous four-criterion optimal placement of two actuators on a damped directed ring

## Finding
For every integer \(n\ge3\), every \(0<r<1\), and every horizon \(H\in n\mathbb N\) with \(H\ge n\), or \(H=\infty\), two independently controlled coordinate actuators in the damped directed ring \(A=rS\) simultaneously maximize the smallest controllability-Gramian eigenvalue and determinant and minimize its inverse trace and spectral condition number **if and only if** the two cyclic inter-actuator gaps differ by at most one. For every fixed \(n,r,H\), all nonbalanced choices are strictly inferior on every one of these four criteria. The same placements therefore work at every full-cycle finite horizon and at the infinite horizon.

Specifically, index the vertices by \(0,\ldots,n-1\), let \(Se_j=e_{j+1\bmod n}\), and choose distinct \(p,q\) with \(B=[e_p,e_q]\). Write their cyclic gaps as \(a,b\ge1\), \(a+b=n\), and arrange \(a\le b\). Set \(t=r^2\) and
\[
 F_H=\begin{cases}(1-t^H)/(1-t^n),&H<\infty,\\(1-t^n)^{-1},&H=\infty.\end{cases}
\]
Then the \(n\) eigenvalues of \(W_H=\sum_{k=0}^{H-1}A^kBB^{\mathsf T}(A^k)^{\mathsf T}\) (with the convergent series interpretation at infinity) are precisely the multiset
\[
 F_H\{(1+t^b)t^j:0\le j<a\}\ \cup\ F_H\{(1+t^a)t^j:0\le j<b\}.
\]
Consequently,
\[
 \lambda_{\min}(W_H)=F_H(t^{b-1}+t^{n-1}),\qquad
 \lambda_{\max}(W_H)=F_H(1+t^a),\qquad
 \kappa_2(W_H)=t^{-(b-1)},
\]
\[
 \det W_H=F_H^n t^{[a(a-1)+b(b-1)]/2}(1+t^b)^a(1+t^a)^b,
\]
\[
 \operatorname{tr}(W_H^{-1})=F_H^{-1}\left(\frac{\sum_{j=0}^{a-1}t^{-j}}{1+t^b}+\frac{\sum_{j=0}^{b-1}t^{-j}}{1+t^a}\right).
\]
In contrast, \(\operatorname{tr}W_H=2\sum_{k=0}^{H-1}t^k\), interpreted as \(2/(1-t)\) for infinite horizon, is independent of placement and cannot distinguish good and bad locations.

## Assumptions and scope
The state is real, \(x_{k+1}=rSx_k+Bu_k\), with two independent scalar control channels, each acting on one **distinct** state coordinate. Their amplitudes are not jointly renormalized; the input columns have unit Euclidean norm individually. The ring is directed and \(S\) is an orthogonal cyclic permutation, not a symmetric graph Laplacian. The damping satisfies strictly \(0<r<1\). A finite horizon is restricted to a positive integer multiple of \(n\), including the minimal full-cycle horizon; the infinite-horizon formula is legitimate because \(A\) is Schur stable. The result does not optimize freely oriented input vectors or differently weighted actuators.

All these Gramians are positive definite, so all four criteria are well defined. Balanced placements mean \(\{a,b\}=\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\). Cyclic translations and interchange of the two actuators generate equivalent choices; these are all the maximizers/minimizers.

## Proof
**1. Exact phase decomposition.** Relabel \(p=0,q=a\). Each summand is diagonal because \(S^ke_j=e_{j+k\bmod n}\). If \(H=mn\), every residue class of \(k\) occurs \(m\) times, with geometric multiplier \(F_H=\sum_{\ell=0}^{m-1}t^{\ell n}\). At infinity the analogous multiplier is \(\sum_{\ell\ge0}t^{\ell n}\). Thus at vertex \(j\),
\[
 (W_H)_{jj}=F_H\big(t^{j}+t^{(j-a\bmod n)}\big).
\]
For \(0\le j<a\), the second exponent is \(b+j\), giving \(F_H(1+t^b)t^j\). For \(a\le j<n\), put \(j=a+k\), \(0\le k<b\); the first exponent is \(a+k\), giving \(F_H(1+t^a)t^k\). This proves the spectrum and positivity. Its largest member is \(F_H(1+t^a)\) because \(a\le b\); its smallest member is the last of the longer block, \(F_Ht^{b-1}(1+t^a)=F_H(t^{b-1}+t^{n-1})\). Division, multiplication, and reciprocal summation produce the other displayed formulas. Since two coordinates are actuated at every time, trace sums to \(2\sum_{k=0}^{H-1}t^k\).

**2. Extreme eigenvalues and conditioning.** Holding \(n,t,H\) fixed, the shorter gap \(a\) ranges over integers \(1\le a\le\lfloor n/2\rfloor\), while \(b=n-a\). Since \(t\in(0,1)\), both \(t^{b-1}\) and \(t^{-(b-1)}\) vary strictly in the favorable direction as \(a\) increases: the smallest eigenvalue strictly increases and the condition number strictly decreases. This characterizes their shared optimum and handles the odd case automatically.

**3. Determinant.** Put \(y=-\log t>0\), \(c=y/2\). The elementary identity \(1+e^{-ys}=2e^{-ys/2}\cosh(cs)\), together with \(a+b=n\), transforms the displayed determinant into
\[
 \log\det W_H=n\log(2F_H)-\frac{yn(n-1)}2+a\log\cosh(cb)+b\log\cosh(ca).
\]
Define for \(x>0\)
\[
 f(x)=\frac{\log\cosh(cx)}{x}=\int_0^c\tanh(sx)\,ds.
\]
For each \(s>0\), \(\tanh(sx)\) is strictly increasing and strictly concave in \(x>0\): its first derivative is positive and second is \(-2s^2\tanh(sx)\operatorname{sech}^2(sx)<0\). Therefore \(f\) is strictly increasing and strictly concave. The placement-dependent determinant term equals \(ab[f(a)+f(b)]\). When \(a\) increases toward \(n/2\), the factor \(ab=a(n-a)>0\) strictly increases, and so does \(f(a)+f(n-a)\), since its derivative is \(f'(a)-f'(n-a)>0\) for \(a<n/2\) by strict concavity. Both factors are positive. Hence the determinant strictly increases toward balanced gaps. A continuous monotonicity proof also gives strict monotonicity on the admissible integer gaps.

**4. Inverse trace.** For any positive integer \(m\),
\[
 \sum_{j=0}^{m-1}t^{-j}=\frac{t(t^{-m}-1)}{1-t}.
\]
Let \(T=t^{-n}\) and \(h(x)=(1+t^{-x})^{-1}=(1+e^{yx})^{-1}\). Elementary simplification of the inverse-trace expression gives
\[
 \operatorname{tr}(W_H^{-1})=\frac{t}{F_H(1-t)}\left((1+T)[h(a)+h(b)]-2\right).
\]
Its multiplier is positive. For \(x>0\),
\[
 h''(x)=\frac{y^2e^{yx}(e^{yx}-1)}{(1+e^{yx})^3}>0.
\]
Thus \(h\) is strictly convex, and for fixed \(a+b=n\), the sum \(h(a)+h(b)\) strictly decreases when the smaller argument approaches \(n/2\). Its minimum over integer gaps occurs precisely at balanced gaps, and all unbalanced choices are strictly worse. Together with Steps 2–3 this proves simultaneous sharp optimality for all four criteria.

## Verification
The analytical proof applies to every stated dimension, damping, and horizon; no numerical enumeration is used as an infinite proof. The standalone pure-Python script `verify.py` checks the exact phase construction and all five formulas by rational arithmetic, including all possible two-coordinate gaps for dimensions \(3\le n\le12\), four rational damping squares, one, two, and three full-cycle horizons, and infinite horizon; it also checks all four strict optimality comparisons. The script executes 2,210 exact-rational comparisons, including additional direct time-index summations. Invoke `python3 verify.py` from the directory containing the extracted script; the expected output is `VERIFY_OK 2210 exact rational comparisons and finite-time direct sums`. This finite evidence checks the algebra and implementation but does not replace the continuous inequalities in the proof.

For example, for an eight-vertex ring with \(r=1/2\), adjacent actuators yield \(\kappa_2=4096\), whereas opposite actuators yield \(\kappa_2=64\). The formula makes this comparison independent of the admissible horizon.

## Relationship to prior work
Summers–Lygeros (2013) established general properties of Gramian-trace actuator selection, which explain why a trace objective can fail to discriminate positions here, but not the present multimetric exact solution. Cortesi–Summers–Lygeros (2014) established submodular structure for several Gramian objectives and general selection methods, not the explicit equal-gap theorem. Enyioha–Rahimian–Pappas–Jadbabaie (2014) considered closely related directed rings, minimum controllability-Gramian eigenvalues, and the benefit of spreading leaders, especially as network size grows; the precise finite-size equal-gap criterion is consistent with that work, but the examined material gives neither this joint four-criterion optimizer classification nor the determinant, inverse-trace, and exact condition formulas. Fitch–Leonard (2016) solved different leader-placement questions for undirected continuous-time Laplacian dynamics, so their ring geometry cannot be substituted for the damped one-way shift analyzed here. A distinct single freely oriented input problem also differs from two independently controlled coordinate channels.

## Limitations
No claim is made about arbitrary horizons not divisible by \(n\), nonidentical actuator powers, correlated or constrained control signals, undirected Laplacian dynamics, or more than two independently actuated coordinates. This is a finite-dimensional deterministic placement result, not a robustness or control-effort optimization under input constraints. The original literature contains qualitative equal-spacing principles; the distinct proposed contribution is the simultaneous sharp exact classification and its formulas. The possibility that a specialized exact equivalent has appeared elsewhere is not eliminated. No independent scientific audit has been performed.

## References
1. T. H. Summers and J. Lygeros, *Optimal Sensor and Actuator Placement in Complex Dynamical Networks*, arXiv:1306.2491, first posted 2013-06-11. https://arxiv.org/abs/1306.2491
2. F. L. Cortesi, T. H. Summers, and J. Lygeros, *Submodularity of Energy Related Controllability Metrics*, arXiv:1403.6351, first posted 2014-03-25. https://arxiv.org/abs/1403.6351
3. C. Enyioha, M. A. Rahimian, G. J. Pappas, and A. Jadbabaie, *Controllability and Fraction of Leaders in Infinite Network*, arXiv:1410.1830, first posted 2014-10-06. https://arxiv.org/abs/1410.1830
4. K. E. Fitch and N. E. Leonard, *Optimal Leader Selection for Controllability and Robustness in Multi-agent Networks*, European Control Conference (2016), doi:10.1109/ECC.2016.7810511. https://doi.org/10.1109/ECC.2016.7810511
