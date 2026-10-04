# Cubic grid-phase law for a sampled bang switch in a controlled qubit

## Finding

Consider the one-control two-level system in Bloch coordinates
\[
\dot X=(\Delta M_z+u M_x)X,\qquad |u|\le 1,
\]
for transfer from the north pole \(X(0)=(0,0,1)\) to the south pole \((0,0,-1)\), with \(0<\Delta<1\). Write
\[
\Omega=\sqrt{1+\Delta^2},\qquad
\tau=\frac{2\pi}{\Omega},\qquad
\alpha=\frac{\pi-\arccos(\Delta^2)}{2\pi}.
\]
The continuous time-optimal bang-bang trajectory switches from \(u=-1\) to \(u=+1\) at time \(\alpha\tau\).

For \(N\) equal sample intervals, let
\[
k_N=\lfloor N\alpha\rfloor,\qquad r_N=N\alpha-k_N.
\]
Study the three-block sampled endpoint branch reported in the source: \(k_N\) samples with amplitude \(-1\), one sample with an interior amplitude \(u_N\), and the remaining \(N-k_N-1\) samples with amplitude \(+1\). If \(r_N\) remains in a compact subset of \((0,1)\), the unique endpoint-solving branch near the continuous bang-bang trajectory obeys
\[
t_N=\tau+\frac{r_N(1-r_N)}{3}\left(\frac{\tau}{N}\right)^3+O(N^{-4})
\]
and
\[
u_N=1-2r_N-
\frac{\Delta^2r_N(1-r_N)}{\sqrt{1-\Delta^2}}
\frac{\tau}{N}+O(N^{-2}).
\]
Equivalently,
\[
\frac{t_N}{\tau}-1
=\frac{r_N(1-r_N)\tau^2}{3N^3}+O(N^{-4}).
\]
At exact grid alignment, \(r_N=0\), the continuous bang-bang protocol is represented exactly and \(t_N=\tau\).

This identifies a cubic grid-phase law for the observed one-interior-sample branch. In particular, a single exponential fit does not describe the branch asymptotically: its leading coefficient oscillates with the fractional switch position \(r_N\).

## Assumptions and scope

Use
\[
M_x=\begin{pmatrix}0&0&0\\0&0&-1\\0&1&0\end{pmatrix},
\qquad
M_z=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}.
\]
The result assumes \(0<\Delta<1\) and concerns the local three-block endpoint branch near the continuous bang-bang solution. The stated remainder is uniform when \(r_N\) stays in a fixed compact subset of \((0,1)\). It does not establish that this branch is the global sampled-data minimum for every \(N\).

The source's earliest public version is arXiv:2211.09167v1, dated 2022-11-16. Its subject is quantum control, corresponding to MSC 81Q93.

## Proof

Set
\[
A_-=\Delta M_z-M_x,\qquad A_+=\Delta M_z+M_x,
\]
and let \(s=\alpha\tau\). The continuous switch state is
\[
X_s=e^{sA_-}(0,0,1)^\top
=(-\Delta,\sqrt{1-\Delta^2},0)^\top.
\]
Let \(h=\tau/N\), write \(r=r_N\), and seek
\[
t_N=\tau+c h^3+O(h^4),\qquad
u_N=1-2r+u_1h+O(h^2).
\]
Factoring the discrete propagator by the exact continuous propagation before and after the switch reduces the local defect to
\[
B_h=
e^{(-(1-r)h+c(1-\alpha)h^3)A_+}
e^{h(\Delta M_z+(1-2r+u_1h+O(h^2))M_x)}
e^{(-rh+c\alpha h^3)A_-}.
\]
A direct Taylor expansion of \(B_hX_s-X_s\) gives no first-order term. With
\[
g=\sqrt{1-\Delta^2},
\]
the second-order term is
\[
h^2(0,0,\Delta^2r(1-r)+g u_1)^\top.
\]
Hence exact endpoint matching forces
\[
u_1=-\frac{\Delta^2r(1-r)}{g}.
\]
After this substitution, the independent tangential component at third order is proportional to
\[
r(1-r)-3c.
\]
More explicitly, the first two coordinates of the third-order coefficient are
\[
\frac{\Delta g}{3}\bigl(r(1-r)-3c\bigr),
\qquad
\frac{\Delta^2}{3}\bigl(r(1-r)-3c\bigr).
\]
Since \(0<\Delta<1\), endpoint matching yields
\[
c=\frac{r(1-r)}{3}.
\]
The next coefficient in \(u_N\) absorbs the remaining third-order component. The endpoint equations are analytic, and the leading derivatives with respect to the scaled control correction and scaled time correction are nonzero: the second-order vertical equation has derivative \(g>0\) with respect to \(u_1\), while the third-order independent tangent equation has nonzero derivative with respect to \(c\). The implicit-function theorem therefore gives a unique nearby endpoint branch with the stated expansions, uniformly for \(r\) in compact subsets of \((0,1)\).

If \(r_N=0\), then \(N\alpha\) is an integer. Choosing \(-1\) until that grid point and \(+1\) afterwards reproduces the continuous bang-bang trajectory exactly, proving \(t_N=\tau\).

## Verification

The accompanying `verify.py` uses only the Python standard library. It composes exact Rodrigues rotations for the three constant-control pieces, solves the two endpoint equations by Newton iteration for \(\Delta=1/2\), and compares the recovered coefficient
\[
\frac{t_N-\tau}{(\tau/N)^3}
\]
against \(r_N(1-r_N)/3\) for several \(N\). It also checks an exact-alignment example with \(\Delta^2=1/2\), for which \(\alpha=1/3\). The replay prints `VERIFY_OK`.

## Relationship to prior work

Dionis and Sugny derive sampled-data Pontryagin conditions for this qubit problem and report that, for most \(N\), their numerical optimum has exactly three constant parts \(-1,\omega_0,+1\), with \(\omega_0\) used for one sampling interval. They describe the one-control convergence plot as approximately exponential, while also noting a cloud of numerical points. The cubic coefficient and its dependence on the fractional switch position are not stated there.

Bourdin and Trélat provide a general Pontryagin maximum principle for nonlinear sampled-data optimal control, but do not give this qubit-specific switch-quantization asymptotic. Scarinci and Veliov prove higher-order error estimates for a different discretization of linear-quadratic bang-bang problems; their method and objective do not imply the coefficient above.

Semantic searches for the qubit, sampled bang switch, grid phase, and cubic convergence returned no statement with the same objects and implication. The closest grid-phase record found concerns an unrelated statistical quantization problem.

## Limitations

The theorem is local to the three-block endpoint branch. It does not prove global sampled-data optimality for every \(N\), nor does it rule out other branches with smaller time. The expansion excludes phases approaching \(0\) or \(1\) except for the separately treated exact-alignment case. No claim is made for \(\Delta=0\), \(\Delta=1\), multiple switches, or the two-control model.

A residual originality risk is that an equivalent switching-time quantization theorem may exist in general bang-bang discretization literature under different terminology. The inspected closest general papers do not contain this coefficient or this qubit endpoint statement.

## References

1. E. Dionis and D. Sugny, “Time-optimal control of two-level quantum systems by piecewise constant pulses,” arXiv:2211.09167v1 (2022); *Physical Review A* **107**, 032613 (2023), DOI: 10.1103/PhysRevA.107.032613.
2. L. Bourdin and E. Trélat, “Optimal sampled-data control, and generalizations on time scales,” *Mathematical Control and Related Fields* **6** (2016), 53–94, DOI: 10.3934/mcrf.2016.6.53.
3. T. Scarinci and V. M. Veliov, “Higher-order numerical scheme for linear quadratic problems with bang-bang controls,” *Computational Optimization and Applications* **69** (2018), 403–422, DOI: 10.1007/s10589-017-9948-z.
