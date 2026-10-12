# Sharp metric-conditioning phase transition for a four-stage positive cascade

## Finding
A stable positive cascade may require a poorly conditioned diagonal quadratic Lyapunov metric to suppress its transient growth. For the first four-stage chain where an interior scaling allocation competes with two outer links, the complete optimal conditioning tradeoff has two exact phases.

Let
\[
G=-\gamma I_4+wN,\qquad \gamma>0,\quad w>0,
\]
where \(N\) is the nilpotent matrix with \(N_{12}=N_{23}=N_{34}=1\) and all other entries zero. Thus \(N^4=0\) and every eigenvalue of \(G\) is \(-\gamma\). The system \(\dot x=Gx\) is a positive, Hurwitz-stable cascade.

For a positive diagonal matrix \(P=\operatorname{diag}(p_1,p_2,p_3,p_4)\), put
\[
\|x\|_P=(x^{\mathsf T}Px)^{1/2},\qquad
\kappa_2(P)=\frac{\max_i p_i}{\min_i p_i},
\]
and let \(\mu_P(G)\) be the largest eigenvalue of the symmetric part of \(P^{1/2}GP^{-1/2}\). For every budget \(K\ge1\),
\[
\boxed{\min_{\kappa_2(P)\le K}\mu_P(G)=-\gamma+wR(K)}
\]
with
\[
\boxed{R(K)=\begin{cases}
\dfrac{K^{-1/2}+\sqrt{4+K^{-1}}}{4},&1\le K\le2,\\[2mm]
2^{-1/3}K^{-1/6},&K\ge2.
\end{cases}}
\]
The minimizer is unique up to overall positive scaling and is
\[
\boxed{P_*(K)\propto\begin{cases}
\operatorname{diag}(1,1,K,K),&1\le K\le2,\\[1mm]
\operatorname{diag}\bigl(1,(K/2)^{1/3},(2K^2)^{1/3},K\bigr),&K\ge2.
\end{cases}}
\]

This is a genuine phase transition in the optimal metric. Before \(K=2\), the permitted distortion is concentrated in a jump between two pairs of equal weights. Beyond \(K=2\), all three links become graded and the middle squared scaled coupling is exactly half of either outer squared coupling. Equal geometric steps are generally not optimal.

For \(c=\gamma/w\), the smallest budget allowing a nonexpansive weighted semigroup is exactly
\[
\boxed{K_{\mathrm{crit}}(c)=\begin{cases}
1,&c\ge(1+\sqrt5)/4,\\[1mm]
\left(2c-\dfrac{1}{2c}\right)^{-2},&1/\sqrt2\le c<(1+\sqrt5)/4,\\[1mm]
\dfrac1{4c^6},&0<c<1/\sqrt2.
\end{cases}}
\]
In particular the small-damping regime has a sharp sixth-power conditioning cost.

For the exact rational example \(G=-I_4+2N\), the threshold is \(K_{\mathrm{crit}}=16\). The optimal metric \(P=\operatorname{diag}(1,2,8,16)\) makes \(G^{\mathsf T}P+PG\) negative semidefinite, but every diagonal metric with condition number below \(16\) has positive logarithmic norm and therefore permits strictly positive short-time weighted-norm growth. The system itself remains asymptotically stable throughout.

## Assumptions and scope
All statements are in exact arithmetic. The system is the four-state real, upper-triangular, uniform-rate positive cascade stated above, with a strictly positive common damping rate and a strictly positive common coupling. The metric may be any positive diagonal quadratic form. No restriction beyond \(\kappa_2(P)\le K\) is imposed.

The norm \(\|e^{tG}\|_P\) is the operator norm induced by \(\|x\|_P\); it is not the ordinary Euclidean norm unless \(P\) is a scalar multiple of the identity. A nonexpansive semigroup means its induced norm is at most one for every nonnegative time, not just asymptotically small.

The optimizing Lyapunov exponent is the weighted Euclidean logarithmic norm, a stronger finite-time diagnostic than the Hurwitz property. The result does not optimize over nondiagonal metrics or over systems with nonuniform couplings, unequal diagonal damping, feedback, or time-varying matrices.

## Proof
**1. Similarity and reduction to three link ratios.** Set
\[
q_i=\frac{p_i}{p_{i+1}}>0\qquad(1\le i\le3).
\]
The symmetric part of \(P^{1/2}GP^{-1/2}\) equals
\[
-\gamma I_4+\frac w2 T(q_1,q_2,q_3),
\]
where \(T\) is the real symmetric tridiagonal matrix with zero diagonal and consecutive off-diagonal entries \(\sqrt{q_1},\sqrt{q_2},\sqrt{q_3}\). Thus
\[
\mu_P(G)=-\gamma+\frac w2\lambda_{\max}(T).
\]
The matrix \(T\) is nonnegative and irreducible. Its positive Perron eigenvalue is strictly increasing in each positive edge, by the Rayleigh quotient evaluated on its strictly positive Perron vector.

Multiplying \(P\) by a scalar changes neither ratios nor condition number. Normalize its smallest entry to one; all entries then lie in \([1,K]\). Replacing \(p_1\) by one and \(p_4\) by \(K\), keeping \(p_2,p_3\) unchanged, never increases \(q_1\) or \(q_3\). Hence an optimum may be sought with
\[
p_1=1,\qquad p_4=K,
\]
and for \(K>1\) every optimum must satisfy these endpoint equalities, by strict Perron monotonicity. When \(K=1\), all four entries necessarily coincide.

**2. The two outer links must balance.** Let
\[
s=\frac{p_3}{p_2}\in[1/K,K].
\]
Then
\[
q_2=\frac1s,\qquad q_1q_3=\frac sK.
\]
Direct expansion of the tridiagonal characteristic polynomial gives
\[
\det(\lambda I-T)=\lambda^4-(q_1+q_2+q_3)\lambda^2+q_1q_3.
\]
Its largest positive eigenvalue is
\[
\lambda_{\max}(T)=\left(\frac{S+\sqrt{S^2-4q_1q_3}}2\right)^{1/2},\qquad S=q_1+q_2+q_3.
\]
For fixed \(q_1q_3>0\) and fixed \(q_2\), this expression strictly increases with \(q_1+q_3\). The arithmetic-geometric mean inequality therefore forces
\[
q_1=q_3=\sqrt{s/K}.
\]
Equality is feasible: choose
\[
p_2=\sqrt{K/s},\qquad p_3=\sqrt{Ks},
\]
which both belong to \([1,K]\) for every admissible \(s\). Consequently **every** optimum, not merely a symmetry-restricted candidate, has balanced outer links.

Write
\[
r=q_1=q_3=\sqrt{s/K}\in[1/K,1],\qquad q_2=\frac1{Kr^2}.
\]
For these reflection-symmetric link weights the Perron eigenvalue becomes
\[
L_K(r)=\frac12\left(\frac1{\sqrt K\,r}+\sqrt{\frac1{Kr^2}+4r}\right).
\]

**3. Unique scalar optimum and phase boundary.** Direct differentiation yields the exact sign formula
\[
\frac{dL_K(r)}{dr}
=\frac{2Kr^3-1-\sqrt{4Kr^3+1}}{2\sqrt K\,r^2\sqrt{4Kr^3+1}}.
\]
The numerator is negative for \(Kr^3<2\), zero precisely at \(Kr^3=2\), and positive for \(Kr^3>2\): to see the sign, set \(u=Kr^3\). When \(u\le1/2\) the first term is nonpositive. When \(u>1/2\), the difference of the squares of \(2u-1\) and \(\sqrt{4u+1}\) is \(4u(u-2)\), yielding the claimed sign.

Thus the unique minimizer in the interval \([1/K,1]\) is
\[
r_*(K)=\begin{cases}
1,&1\le K\le2,\\
(2/K)^{1/3},&K\ge2.
\end{cases}
\]
For \(K\le2\), \(p_2=p_1=1\) and \(p_3=p_4=K\), and substitution gives
\[
\frac12L_K(r_*)=\frac{K^{-1/2}+\sqrt{4+K^{-1}}}{4}.
\]
For \(K\ge2\), one has
\[
p_2=(K/2)^{1/3},\quad p_3=(2K^2)^{1/3},
\]
which makes \(q_1=q_3=(2/K)^{1/3}\) and \(q_2=q_1/2\). Its Perron eigenvalue is \(L_K(r_*)=2^{2/3}K^{-1/6}\), giving
\[
\frac12L_K(r_*)=2^{-1/3}K^{-1/6}.
\]
Every optimization step has a unique equality case (apart from the irrelevant scaling of \(P\)). This proves the formula, uniqueness, and phase transition.

**4. Exact nonexpansion frontier.** For a time-independent matrix, the induced logarithmic norm obeys
\[
\|e^{tG}\|_P\le e^{t\mu_P(G)}\quad(t\ge0),
\]
and conversely its right derivative at the identity is \(\mu_P(G)\). Therefore
\[
\|e^{tG}\|_P\le1\ \text{for all }t\ge0
\quad\Longleftrightarrow\quad\mu_P(G)\le0.
\]
The function \(R(K)\) is continuous and strictly decreasing; its endpoint values are
\[
R(1)=\frac{1+\sqrt5}{4},\qquad R(2)=\frac1{\sqrt2}.
\]
A viable budget therefore satisfies \(R(K)\le c=\gamma/w\). If \(c\ge R(1)\), the least budget is one. In the intermediate regime, set \(y=K^{-1/2}\) and solve
\[
4c=y+\sqrt{4+y^2}
\quad\Longleftrightarrow\quad
y=2c-\frac1{2c}.
\]
For \(c<1/\sqrt2\), solve
\[
c=2^{-1/3}K^{-1/6}
\quad\Longleftrightarrow\quad K=\frac1{4c^6}.
\]
These are exactly the three displayed pieces. If \(K\) is below the threshold, the optimal logarithmic norm is positive, hence every admissible metric exhibits initial norm growth; at or above it, the explicitly stated optimal metric certifies nonexpansion for all times.

**5. Exact rational boundary.** For \(G=-I_4+2N\) one has \(c=1/2\), hence \(K_{\mathrm{crit}}=16\). The optimum \(P=\operatorname{diag}(1,2,8,16)\) yields a symmetric congruence of \(G^{\mathsf T}P+PG\) with eigenvalues \(0,-1,-3,-4\). Thus it is negative semidefinite and the boundary is attained. This construction proves that the sixth-power branch has a concrete stable positive-system realization.

## Verification
Run the standalone standard-library checker `verify.py`. It computes the Perron eigenvalue from the tridiagonal characteristic polynomial, checks the piecewise closed form at selected budgets, compares the optimizer against exhaustive deterministic four-weight samples, and verifies the exact \(K=16\) certificate using rational characteristic determinants. The output `VERIFY_OK` indicates that these finite and symbolic consistency checks passed.

No finite grid proves the global optimum. The global result, uniqueness, and all-budget necessity follow from strict Perron monotonicity, the fixed-product arithmetic-geometric mean argument, and the sign-controlled one-variable derivative given in the proof.

## Relationship to prior work
Diagonal quadratic Lyapunov functions for stable positive linear systems are classical. Kaszkurewicz and Bhaya treat robust stability and diagonal Liapunov functions, within primary MSC \(93D09\). Mason and Shorten prove existence criteria for a **common** diagonal quadratic Lyapunov function for a pair of positive linear systems. Their full text establishes Metzler preliminaries and matrix-pencil criteria, without a fixed spectral condition-number budget or a four-link rate tradeoff. Mason's full diagonal Riccati stability paper treats positive time-delay systems and different matrix inequalities.

Bhatia, Kahan, and Li prove norm pinching results for monotone diagonal similarities of triangular matrices; that is relevant general scaling background but does not state or imply the exact condition-budgeted symmetric-part eigenvalue optimization. The publicly inspected abstract is insufficient to assert that their complete paper excludes every specialization, and this remains an originality risk.

The new object is the **minimal positive cascade with three interacting links** and a fixed condition budget on diagonal metrics, rather than existence of some unrestricted metric. The result identifies a nongeometric optimum, a phase change at \(K=2\), and an exact sixth-power price for nonexpansive Lyapunov certification. Targeted searches for diagonal stability, diagonal similarity, logarithmic norms, Jordan cascades, fixed condition budgets, and equivalent Lyapunov inequalities found no implication-equivalent published statement. No claim is made that unrestricted diagonal stability itself is new.

## Limitations
The full characterization is for the specified four-state uniform-rate upper-triangular Metzler matrix. Distinct damping rates, nonuniform edge weights, larger chains, nondiagonal positive metrics, and robust perturbations are not included.

The optimal weighted logarithmic norm is a sharp **one-sided exponential certificate**, not the exact maximum Euclidean transient. A weighted norm with condition number \(K\) gives the Euclidean estimate \(\|e^{tG}\|_2\le\sqrt K\,e^{t\mu_P(G)}\), which need not be sharp for finite \(t\).

Positive \(\mu_P(G)\) implies short-time amplification in that weighted norm; it does not contradict Hurwitz stability or prove growth for every trajectory. At equality in the nonexpansion frontier, a zero logarithmic norm is allowed and strict exponential decrease with positive margin is not asserted.

The literature overlap assessment has residual risks from generic diagonal similarity theory and abstracts for inaccessible articles; independent verification has not been performed.

## References
1. E. Kaszkurewicz and A. Bhaya, “Robust Stability and Diagonal Liapunov Functions,” *SIAM Journal on Matrix Analysis and Applications* 14 (1993), 508–520. DOI 10.1137/0614036.
2. O. Mason and R. Shorten, “On the simultaneous diagonal stability of a pair of positive linear systems,” *Linear Algebra and its Applications* 413 (2006), 13–23. DOI 10.1016/j.laa.2005.07.019. Open manuscript: https://mural.maynoothuniversity.ie/id/eprint/1886/1/HamiltonSimultaneous.pdf.
3. O. Mason, “Diagonal Riccati Stability and Positive Time-Delay Systems,” *Systems & Control Letters* 61 (2012), 6–10. DOI 10.1016/j.sysconle.2011.09.022.
4. R. Bhatia, W. Kahan, and R.-C. Li, “Pinchings and Norms of Scaled Triangular Matrices,” *Linear and Multilinear Algebra* 50 (2002), 15–21. DOI 10.1080/03081080290011674.
