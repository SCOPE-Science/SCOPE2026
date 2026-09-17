# Harmonic-resonance obstructions for weighted critical Hardy--Rellich inequalities

## Statement

Let \(N\ge2\), \(a\in\mathbb R\), and for \(u\in C_c^\infty(\mathbb R^N\setminus\{0\})\) set
\[
\mathcal I_a[u]:=\int_{\mathbb R^N}\left|\nabla\!\left(\frac{u(x)}{|x|}\right)\right|^N |x|^a\,dx.
\]
Consider the Hessian and Laplacian estimates
\[
\tag{H_a}\mathcal I_a[u]\le C\int_{\mathbb R^N}|D^2u|^N|x|^a\,dx,
\]
\[
\tag{L_a}\mathcal I_a[u]\le C\int_{\mathbb R^N}|\Delta u|^N|x|^a\,dx.
\]

Two conclusions follow.

### 1. Correct sharp weight set for the Hessian formulation

For \(N\ge2\), \((H_a)\) holds for all test functions if and only if
\[
\boxed{a\notin\{0,N\}.}
\]
For \(a\notin\{0,N\}\), the estimates in Sections 3.3--3.5 of Majdoub (arXiv:2606.15668v1) already prove \((H_a)\), with the explicit admissible constant
\[
2^{N/2-1}\left[\left(\frac{N}{|a|}\right)^N+\left(\frac{N}{|N-a|}\right)^N\right].
\]
The two excluded weights are genuinely singular. The obstruction at \(a=N\) is also exhibited in Majdoub. At \(a=0\), logarithmic cutoffs of the affine harmonic function \(x_1\) make the left side grow while the weighted Hessian norm tends to zero.

Thus the June 2026 claim that \(a=N\) is the unique critical Hessian weight requires correction. This is consistent with Castro's revised arXiv:2511.16537v4 (2 July 2026), which explicitly removes \(a=0\) and gives a linear-function counterexample to the unweighted Laplacian version.

### 2. An infinite harmonic-resonance obstruction for the Laplacian formulation

Let \(Y_m\not\equiv0\) be a spherical harmonic of degree \(m\ge0\), so
\[
-\Delta_{\mathbb S^{N-1}}Y_m=m(m+N-2)Y_m.
\]
If \(\beta\) is either homogeneity of the associated harmonic mode,
\[
\beta=m\qquad\text{or}\qquad \beta=-(m+N-2),
\]
with the duplicated \(N=2,m=0\) root counted only once, then \((L_a)\) fails at
\[
\boxed{a=N(1-\beta).}
\]
Equivalently, for \(N\ge3\) the failure set contains
\[
\boxed{\{N(1-m):m\ge0\}\ \cup\ \{N(m+N-1):m\ge0\},}
\]
while for \(N=2\) it contains
\[
\boxed{\{2(1-m):m\ge0\}\ \cup\ \{2(m+1):m\ge1\}=2\mathbb Z.}
\]

In particular:

- \(a=0\) fails, from the linear harmonic mode \(m=1\); this agrees with Castro v4 and shows that Corollary 1.6 of Majdoub v1 cannot include the unweighted point.
- \(a=-N\) fails, from any degree-two harmonic polynomial.
- \(a=N(N-1)\) fails: for \(N\ge3\) use the fundamental harmonic homogeneity \(\beta=2-N\); for \(N=2\) this endpoint equals \(a=N=2\), already supplied by the constant mode.

Hence both boundary points of the Muckenhoupt interval
\[
-N<a<N(N-1)
\]
are true failure points for the critical Laplacian Hardy--Rellich inequality, not merely limitations of the weighted Calderon--Zygmund proof. This gives a negative answer at both endpoints to the boundary question raised in Remark 5.4 of Majdoub v1.

Inside the Muckenhoupt interval, Majdoub's valid Hessian estimates combined with weighted Calderon--Zygmund theory give \((L_a)\) for
\[
-N<a<N(N-1),\qquad a\notin\{0,N\},
\]
and the resonant counterexamples above show that the exclusions that lie in the interval are necessary. Thus this is the exact corrected validity set *within* the Muckenhoupt interval. No claim is made here that the displayed discrete resonance set is the complete failure set outside that interval.

## Proof of the harmonic-resonance obstruction

Fix \(\eta\in C_c^\infty(\mathbb R)\) such that \(\eta=1\) on \([-1,1]\) and \(\operatorname{supp}\eta\subset[-2,2]\). Put
\[
h(r,\omega)=r^\beta Y_m(\omega),\qquad
u_L(r,\omega)=h(r,\omega)\,\eta\!\left(\frac{\log r}{L}\right),\qquad L\ge1.
\]
Every \(u_L\) is smooth and compactly supported in an annulus contained in \(\mathbb R^N\setminus\{0\}\). Since
\[
\beta(\beta+N-2)=m(m+N-2),
\]
\(h\) is harmonic away from the origin.

Writing \(t=\log r\), a direct polar-coordinate computation gives
\[
\Delta u_L
=r^{\beta-2}Y_m(\omega)
\left[
\frac{2\beta+N-2}{L}\eta'\!\left(\frac tL\right)
+\frac1{L^2}\eta''\!\left(\frac tL\right)
\right].
\]
At the resonant weight \(a=N(1-\beta)\), the radial power in both critical integrals cancels exactly:
\[
r^{N(\beta-2)}r^a r^{N-1}\,dr=\frac{dr}{r}=dt.
\]
The Laplacian is supported only in the two transition regions, whose total \(t\)-length is \(O(L)\), and its bracket is \(O(L^{-1})\). Hence
\[
\int_{\mathbb R^N}|\Delta u_L|^N|x|^a\,dx\le C L^{1-N}.
\]

On the plateau \(|t|\le L\), \(u_L=h\), so
\[
\nabla\!\left(\frac{u_L}{r}\right)=\nabla\!\left(r^{\beta-1}Y_m\right).
\]
This homogeneous gradient is not identically zero: otherwise \(r^{\beta-1}Y_m\) would be constant, forcing \(h\) to be a nonzero multiple of \(r\), which is not harmonic in dimension \(N\ge2\). Therefore its spherical \(L^N\) norm is positive, and the same radial cancellation gives
\[
\mathcal I_a[u_L]\ge cL.
\]
Consequently
\[
\frac{\mathcal I_a[u_L]}{\int |\Delta u_L|^N|x|^a\,dx}\ge c' L^N\longrightarrow\infty,
\]
which proves failure of \((L_a)\) at every resonant weight.

## The two Hessian resonances

The same construction gives the two Hessian counterexamples without invoking the Laplacian estimate. Take either
\[
h(x)=1,\quad (\beta,a)=(0,N),
\]
or
\[
h(x)=x_1,\quad (\beta,a)=(1,0).
\]
Both are affine, hence \(D^2h=0\). In the transition annuli, differentiating the logarithmic cutoff gives
\[
|D^2u_L(x)|\le C r^{\beta-2}(L^{-1}+L^{-2}).
\]
At \(a=N(1-\beta)\) this implies
\[
\int |D^2u_L|^N|x|^a\,dx\le C L^{1-N},
\]
while exactly as above \(\mathcal I_a[u_L]\ge cL\). Thus \((H_a)\) fails at \(a=N\) and \(a=0\). Together with Majdoub's direct estimates for \(a\notin\{0,N\}\), this yields the stated iff classification.

## Context and limitations

Majdoub v1 predates Castro's July 2026 revision. Its proof itself identifies separate one-dimensional degeneracies at \(a=N\) in the radial estimate and \(a=0\) in the angular estimate, but it then fills \(a=0\) by citing the earlier unweighted theorem. Castro v4 now explicitly states that the unweighted conjecture is false and excludes \(a=0\).

The logarithmic-cutoff construction is a standard weighted-elliptic idea, and classical work such as McOwen (1979) studies the Laplacian on weighted Sobolev spaces with exceptional weights related to harmonic modes. The full text of McOwen (1979) was not inspected here, so this record does not claim that the abstract resonance mechanism is new in weighted elliptic theory. The claim of originality is narrower: no source found in the targeted search states this resonance obstruction for the present critical Hardy--Rellich functional, its correction of the June 2026 sharp Hessian range, or its endpoint consequences for Remark 5.4.

The record does not characterize \((L_a)\) at all nonresonant weights outside the Muckenhoupt interval. Such a characterization would require additional weighted elliptic analysis beyond the counterexample argument above.

## References

1. H. Castro, *A critical Hardy--Rellich inequality*, arXiv:2511.16537v4 (2 July 2026). https://arxiv.org/abs/2511.16537
2. M. Majdoub, *An extension of a critical Hardy--Rellich inequality: explicit constants and the sharp weight range*, arXiv:2606.15668v1 (14 June 2026). https://arxiv.org/abs/2606.15668
3. R. C. McOwen, *The behavior of the Laplacian on weighted Sobolev spaces*, Comm. Pure Appl. Math. 32 (1979), 783--795. https://doi.org/10.1002/cpa.3160320604
