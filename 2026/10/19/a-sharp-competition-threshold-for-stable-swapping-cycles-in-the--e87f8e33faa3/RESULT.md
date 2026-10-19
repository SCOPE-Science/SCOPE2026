# A sharp competition threshold for stable swapping cycles in the symmetric Ricker map

## Finding

For the exchange-symmetric two-species Ricker map
\[
F_{R,k}(x,y)=(Rxe^{-x-ky},\;Rye^{-y-kx}),\qquad R>0,\quad k\ge0,
\]
acting on strictly positive states, a **swapping two-cycle** means two distinct states \((x,y)\) and \((y,x)\), with \(x>y>0\), mapped into each other.

**Existence and uniqueness.** For each \((R,k)\), such a cycle exists, uniquely up to exchanging coordinates, if and only if
\[
0\le k<1,\qquad \log R>\frac{2(1+k)}{1-k}.
\]
Every such cycle has the following exact one-parameter representation, with \(0<\delta<1\):
\[
u(\delta)=\frac{\operatorname{artanh}\delta}{\delta},\quad
v(\delta)=(1-\delta^2)u(\delta),\quad
S=\frac{4u(\delta)}{1-k},\quad
\log R=\frac{2(1+k)}{1-k}u(\delta),\quad
(x,y)=\frac S2(1+\delta,1-\delta).
\]

**Exact sharp stability threshold.** Let \(\delta_*\in(0,1)\) be the unique root of
\[
(1-\delta_*^2)\frac{\operatorname{artanh}\delta_*}{\delta_*}=\delta_*^2
\]
and set
\[
k_* =\frac{1-\delta_*^2}{1+\delta_*^2}\approx0.277839040264.
\]
For \(0<k<1\), define \(\delta_-(k)\) and \(\delta_+(k)\) uniquely by
\[
v(\delta_-(k))=\frac{1-k}{1+k},\qquad
\frac{4u(\delta_+(k))}{1-k}\left[1-(1+k)v(\delta_+(k))\right]=2,
\]
and set \(\delta_-(0)=0\). The swapping two-cycle is **linearly asymptotically stable** (both multipliers of the two-step map strictly inside the unit disk) exactly when
\[
0\le k<k_*,\qquad\delta_-(k)<\delta<\delta_+(k).
\]
Thus \(k_*\) is the sharp largest cross-competition intensity permitting a linearly attracting swapping cycle, although swapping cycles exist for \(k_*\le k<1\) when the intrinsic growth rate is sufficiently large. At equality in either strict stability inequality, at least one multiplier has unit modulus; strict linear asymptotic stability is not claimed there.

For example, at \(k=0.03\) the attracting swapping cycles occupy approximately \(8.915749064<R<14.760100029\). These are parameter bounds, not a statement about attraction from every initial state.

## Assumptions and scope

The parameters are fixed with \(R>0\) and \(k\ge0\); both populations must be strictly positive. No stochastic forcing, unequal growth factors or unequal cross-competition coefficients are allowed. The theorem classifies only cycles whose second state is the coordinate swap of the first. It does **not** classify all period-two orbits, other attracting sets, basins, or stochastic transitions. Stability means the strict spectral-radius criterion for the derivative of the second iterate.

## Proof

**1. Exact parametrization.** Suppose \(F_{R,k}(x,y)=(y,x)\) and \(x>y>0\). Dividing each coordinate equation by its original coordinate and taking logarithms gives
\[
\log(y/x)=\log R-x-ky,\qquad
\log(x/y)=\log R-y-kx.
\]
Their sum yields \(S=x+y=2\log R/(1+k)\). Their difference yields
\[
2\log(x/y)=(1-k)(x-y).
\]
With \(\delta=(x-y)/(x+y)\) this becomes \(4\operatorname{artanh}\delta=(1-k)S\delta\). The left side is positive, so \(k<1\). Solving the two identities gives the displayed expressions for \(S\) and \(\log R\). Conversely these expressions substituted into the two logarithmic equations establish the exact swap, so there are no omitted algebraic branches. The function \(u\) increases strictly from \(1\) to infinity on \((0,1)\), because \(\operatorname{artanh}\delta<\delta/(1-\delta^2)\). Hence the stated growth threshold is necessary and sufficient and \(\delta\) is unique.

**2. Floquet reduction.** Let \(P\) exchange coordinates. Exchange symmetry gives \(DF(y,x)=P\,DF(x,y)\,P\), so the two-step Jacobian at \((x,y)\) is \((P\,DF(x,y))^2\). Since \(F(x,y)=(y,x)\), direct differentiation gives
\[
B=P\,DF(x,y)=\begin{pmatrix}
-kx & \frac xy(1-y)\\[3pt]
\frac yx(1-x)&-ky
\end{pmatrix}.
\]
Thus \(F^2\) has both multipliers strictly inside the unit circle exactly when both eigenvalues of the real matrix \(B\) do. Write
\[
\operatorname{tr}B=-kS,\quad
D_k(\delta)=\det B=S-1-(1-k^2)xy
=\frac{4u(\delta)}{1-k}\bigl[1-(1+k)v(\delta)\bigr]-1.
\]
The strict real quadratic Schur criterion says that the eigenvalues of \(B\) are inside the unit disk exactly when
\[
1+\operatorname{tr}B+\det B>0,\quad
1-\operatorname{tr}B+\det B>0,\quad
1-\det B>0.
\]
The two first expressions factor, **without approximation**, as
\[
1+\operatorname{tr}B+\det B=(1-k)\bigl[S-(1+k)xy\bigr],\quad
1-\operatorname{tr}B+\det B=(1+k)\bigl[S-(1-k)xy\bigr].
\]
Since \(xy=S^2(1-\delta^2)/4\), these conditions are respectively \(v(\delta)<(1-k)/(1+k)\) and \(v(\delta)<1\). The second holds automatically for \(0<\delta<1\).

**3. Unique crossing points.** The function \(v\) strictly decreases from \(1\) to \(0\): indeed
\[
v'(\delta)=\frac1\delta-\frac{1+\delta^2}{\delta^2}\operatorname{artanh}\delta<0.
\]
Therefore the first condition is \(\delta>\delta_-(k)\), with \(\delta_-(0)=0\). On the other hand \(S(\delta)\) increases strictly, whereas
\[
xy=\frac{4u(\delta)^2(1-\delta^2)}{(1-k)^2}
\]
decreases strictly: the derivative of its logarithm has the sign of \(\delta-\operatorname{artanh}\delta<0\). Consequently \(D_k(\delta)=S-1-(1-k^2)xy\) increases strictly for every \(k<1\). At \(\delta\downarrow0\), \(D_k\to-1-4k/(1-k)<1\); at \(\delta\uparrow1\), \(D_k\to+\infty\). This proves that \(\delta_+(k)\) exists uniquely and that the final Schur condition is \(\delta<\delta_+(k)\).

**4. Sharp disappearance of the stable window.** At \(\delta=\delta_-(k)\), write \(v=v(\delta)=(1-k)/(1+k)\). Then \(k=(1-v)/(1+v)\), and direct substitution gives the exact comparison
\[
1-D_k(\delta_-(k))=
\frac{2\left[v(\delta_-(k))-\delta_-(k)^2\right]}{1-\delta_-(k)^2}.
\]
Thus the two strict inequalities can hold simultaneously exactly when \(v(\delta_-(k))>\delta_-(k)^2\). The strictly decreasing function \(v(\delta)\) crosses strictly increasing \(\delta^2\) once; denote their intersection by \(\delta_*\). Since \(\delta_-(k)\) increases with \(k\), the window is nonempty exactly for \(k<k_*=(1-\delta_*^2)/(1+\delta_*^2)\). The case \(k=0\) follows directly from \(\delta_-(0)=0\) and \(D_0\) being increasing. Every assertion follows.

## Verification

The bundled stand-alone file `verify.py` uses the Python standard library only. Run `python3 verify.py`. It checks all four factorizations with exact rational arithmetic, reconstructs swaps and two-step Floquet matrices independently at sampled parameters, evaluates the strict Schur inequalities against their asserted parameter window, and checks monotonicity on finite grids. One replay produced `VERIFY_OK` after **13,062** assertions. This is a consistency test; the proof above supplies all-parameter validity. The source's numerical onset estimate at cross-coupling \(0.03\) is near the exact lower boundary but is not used as proof.

## Relationship to prior work

Ryashko, Otman and Bashkirtseva (2025) studied **this same symmetric competitive Ricker model**, including numerically observed non-diagonal antiphase two-cycles and coexistence with in-phase attractors; their reported lower transition near \(R=8.927\) at \(k=0.03\) is acknowledged. Their inspected model, bifurcation plots, stability descriptions and stochastic sections do not state an exact global coupling cutoff for linearly stable swap cycles or a complete analytic stability interval.

Goldar, Hassan, Pati, Mohsen and Izadi (2026) study a more general two-population Ricker map and give the generic Jacobian and Schur stability test for a period-two orbit; their general test is prior art. Substituting a **swapping orbit** into that test and proving existence, uniqueness, the monotonic crossing and sharp all-growth competition cutoff produces the present classification. Earlier published analyses of synchronous cycles of row-regular Ricker models concern diagonal trajectories, not the off-diagonal swapping cycles considered here. No claim of unique priority against every possible earlier specialization is made.

## Limitations

The conclusion is local, linear asymptotic stability, not a global basin theorem. For \(k=k_*\) or other strict-boundary parameters, nonlinear attraction or higher-order bifurcation type is unproved. Stable nonswapping two-cycles or higher-period attractors are not excluded above \(k_*\). At \(k=0\), the populations decouple and the swapping orbit is a product of scalar two-cycle states; the formula remains valid. Possible equivalence to an earlier analytic result in dispersed ecological dynamics literature remains a priority risk. No independent scientific audit has been performed.

## References

1. L. Ryashko, A. Otman, I. Bashkirtseva, “Multirhythmicity, Synchronization, and Noise-Induced Dynamic Diversity in a Discrete Population Model with Competition,” *Mathematics* **13** (2025), 857. First public publication 2025-03-05. DOI: `10.3390/math13050857`.
2. S. Goldar, S. S. Hassan, R. Pati, A. A. Mohsen, M. Izadi, “Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth,” *Discrete Dynamics in Nature and Society* **2026** (2026), 7255117. Published 2026-09-16. DOI: `10.1155/ddns/7255117`.
