# An exact continuum envelope for the full-rank fixed-spectrum entanglement no-go

## Finding

Let \(\lambda=(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\) be an ordered full-rank two-qubit spectrum,
\[
\lambda_1\ge \lambda_2\ge \lambda_3\ge \lambda_4>0,\qquad
\sum_{i=1}^4\lambda_i=1,
\]
and assume
\[
2\lambda_2+\lambda_3<\lambda_1.
\]
Let \(\rho_\lambda\) be the Verstraete--Audenaert--De Moor fixed-spectrum MEMS and let \(\sigma_\lambda\) be the isospectral Bell-diagonal state, in the conventions of Camacho and de Vicente. A necessary condition for a non-entangling channel \(\Lambda\) with \(\Lambda(\rho_\lambda)=\sigma_\lambda\) is
\[
\lambda_2\le
\frac{1-\lambda_1}{2}
+\frac12\left(\frac{\lambda_3^2}{4\lambda_2}-\lambda_4\right)_+,
\]
where \((t)_+=\max(t,0)\).

Consequently, whenever the displayed inequality fails, no maximally entangled state exists in the set of two-qubit states with spectrum \(\lambda\). Equivalently, under the same assumptions, the new analytic no-go region is
\[
\begin{cases}
\lambda_2>\lambda_3+\lambda_4,
& \lambda_3^2\le 4\lambda_2\lambda_4,\\[4pt]
\displaystyle\frac{\lambda_2}{\lambda_3}>
\frac{1+\sqrt2}{2},
& \lambda_3^2>4\lambda_2\lambda_4.
\end{cases}
\]
This region contains all three rank-four regions in Theorem 8 of Camacho and de Vicente and is strictly larger. For example,
\[
\lambda=\left(\frac{63}{100},\frac15,\frac3{20},\frac1{50}\right)
\]
lies outside all three of their analytic regions but is excluded by the continuum envelope, with
\[
\frac{1-\lambda_1}{2}
+\frac12\left(\frac{\lambda_3^2}{4\lambda_2}-\lambda_4\right)
=\frac{121}{640}
<\frac15.
\]

## Assumptions and scope

The fixed-spectrum MEMS is
\[
\rho_\lambda
=\lambda_1\Phi_1+\lambda_2|01\rangle\langle01|
+\lambda_3\Phi_2+\lambda_4|10\rangle\langle10|,
\]
and the Bell-diagonal target is
\[
\sigma_\lambda=\sum_{j=1}^4\lambda_j\Phi_j.
\]
Here \(\Phi_j\) are Bell-basis projectors in the convention of the cited source.

The hypothesis \(2\lambda_2+\lambda_3<\lambda_1\) implies \(\lambda_1>1/2\). Indeed, if \(\lambda_1\le1/2\), then
\[
2\lambda_2+\lambda_3
\ge \lambda_2+\lambda_3+\lambda_4
=1-\lambda_1\ge\lambda_1,
\]
because \(\lambda_2\ge\lambda_4\), a contradiction. Thus the Bell-diagonal target is entangled. The MEMS is also entangled because
\[
\lambda_3+2\sqrt{\lambda_2\lambda_4}
\le \lambda_2+\lambda_3+\lambda_4
=1-\lambda_1<\lambda_1.
\]

The result is a necessary-condition obstruction for the specific MEMS-to-Bell-diagonal conversion used in the source. It does not classify all full-rank spectra and does not assert that the envelope is sufficient for a non-entangling conversion.

## Proof

Assume that a non-entangling channel \(\Lambda\) maps \(\rho_\lambda\) to \(\sigma_\lambda\). Following Camacho and de Vicente, set
\[
F_{ij}=\operatorname{tr}\!\left(\Phi_i\Lambda(\xi_j)\right),
\]
where
\[
\xi_1=\Phi_1,\quad
\xi_2=|01\rangle\langle01|,\quad
\xi_3=\Phi_2,\quad
\xi_4=|10\rangle\langle10|.
\]
Their necessary conditions include
\[
\sum_{j=1}^4\lambda_jF_{ij}=\lambda_i,\qquad
\sum_{i=1}^4F_{ij}=1,\qquad F_{ij}\ge0,
\]
and, for every \(a\in[0,1]\),
\[
2a(1-a)F_{i3}+a^2F_{i2}+(1-a)^2F_{i4}\le\frac12.
\]

Under \(2\lambda_2+\lambda_3<\lambda_1\), the rank-four proof in the source first forces
\[
F_{12}=F_{14}=0,\qquad F_{11}=1,\qquad F_{13}=0,
\]
and hence
\[
F_{21}=F_{31}=F_{41}=0.
\]
For the second row define
\[
x=F_{22},\qquad y=F_{23},\qquad z=F_{24}.
\]
The continuum constraint becomes
\[
a^2x+2a(1-a)y+(1-a)^2z\le\frac12
\qquad\text{for every }a\in[0,1].
\]
Put
\[
u=\frac12-x,\qquad v=\frac12-z.
\]
The endpoint cases imply \(u,v\ge0\). The continuum inequality is equivalent to
\[
y\le\frac12+\sqrt{uv}.
\]
Indeed, its deficit is
\[
a^2u+2a(1-a)\left(\frac12-y\right)+(1-a)^2v.
\]
By homogeneity, testing \(a\in[0,1]\) is the same as testing the corresponding quadratic on all nonnegative pairs \((r,s)\neq(0,0)\). For \(u,v\ge0\), the quadratic \(ur^2+2wrs+vs^2\) is nonnegative for all \(r,s\ge0\) exactly when \(w+\sqrt{uv}\ge0\). Sufficiency follows from
\[
ur^2+vs^2\ge2\sqrt{uv}\,rs,
\]
and necessity follows by taking \(r/s=\sqrt{v/u}\) when \(u,v>0\), with boundary cases immediate. Taking \(w=1/2-y\) gives the claimed bound.

The second-row eigenvalue equation is
\[
\lambda_2=\lambda_2x+\lambda_3y+\lambda_4z.
\]
Hence
\[
\lambda_2
\le
\frac{1-\lambda_1}{2}
-\lambda_2u-\lambda_4v+\lambda_3\sqrt{uv}.
\]
Writing \(r=\sqrt u\) and \(s=\sqrt v\), with
\[
0\le r,s\le\frac1{\sqrt2},
\]
we maximize
\[
H(r,s)=-\lambda_2r^2-\lambda_4s^2+\lambda_3rs.
\]
For fixed \(s\), the maximizer
\[
r_*=\frac{\lambda_3}{2\lambda_2}s
\]
lies in the interval because \(\lambda_3\le\lambda_2\). Thus
\[
\max_r H(r,s)
=s^2\left(\frac{\lambda_3^2}{4\lambda_2}-\lambda_4\right).
\]
Maximizing over \(0\le s^2\le1/2\) yields
\[
\max H=
\frac12\left(\frac{\lambda_3^2}{4\lambda_2}-\lambda_4\right)_+,
\]
which proves the envelope.

If \(\lambda_3^2\le4\lambda_2\lambda_4\), violation is exactly \(\lambda_2>\lambda_3+\lambda_4\). If \(\lambda_3^2>4\lambda_2\lambda_4\), violation is equivalent to
\[
4\lambda_2^2>4\lambda_2\lambda_3+\lambda_3^2,
\]
hence
\[
\frac{\lambda_2}{\lambda_3}>\frac{1+\sqrt2}{2}.
\]

The source's region A has \(\lambda_2>2\lambda_3+\lambda_4\), so one of these branches excludes it. In region B, \(\lambda_3\le2\lambda_4\) and \(\lambda_2>\lambda_3+\lambda_4\), which gives \(\lambda_3^2\le4\lambda_2\lambda_4\) and invokes the first branch. In region C, \(\lambda_3>2\lambda_4\) and \(\lambda_2>3\lambda_3/2\); the first branch applies when the discriminant is nonpositive, and otherwise the second branch applies because
\[
\frac32>\frac{1+\sqrt2}{2}.
\]
The rational spectrum in the finding satisfies none of A, B, or C and yields a strict extension.

## Verification

The proof is analytic. The source premises were checked directly in the full preprint: Eq. (39) gives the all-\(a\) continuum, and Theorem 8 derives the first-row reduction before splitting into three coarser full-rank regions.

The accompanying checker uses exact rational arithmetic for the strict-extension spectrum. It verifies ordering, full rank, normalization, the first-row hypothesis, failure of all three source regions, the positive-discriminant branch, and the exact envelope value \(121/640\) with gap \(7/640\). It also compares the analytic quadratic maximum with a finite grid as a corroborative sanity check. The finite grid is not part of the proof.

## Relationship to prior work

Verstraete, Audenaert, De Bie, and De Moor characterized fixed-spectrum two-qubit states that simultaneously maximize entanglement of formation, negativity, and relative entropy of entanglement. De Vicente later proved that such a state need not be a universal fixed-spectrum resource by finding rank-two spectra for which a non-entangling conversion to a suitable isospectral target is impossible.

Camacho and de Vicente extended the obstruction to all rank-two and rank-three spectra and a large full-rank region. Their full-rank analysis introduces the exact continuum inequalities used here, discretizes them for numerical feasibility tests, and proves analytic infeasibility only on regions A, B, and C. They explicitly state that their analytic region is strictly contained in the numerically infeasible region.

The present result optimizes one of their exact continuum row constraints instead of retaining only coarse endpoint and midpoint consequences. It gives a closed-form necessary envelope strictly containing A, B, and C. Targeted searches for the source title, arXiv identifier, the square-root threshold, the discriminant \(\lambda_3^2-4\lambda_2\lambda_4\), and equivalent fixed-spectrum/non-entangling formulations found no published statement of this envelope.

## Limitations

The theorem applies only to ordered full-rank two-qubit spectra satisfying \(2\lambda_2+\lambda_3<\lambda_1\). It proves nonexistence when the envelope is violated; it does not prove existence of a non-entangling channel when the envelope holds. It therefore does not close the remaining full-rank feasibility problem or prove that the new boundary is the exact continuum feasibility boundary.

The originality comparison is literature-based rather than an exhaustive proof that no equivalent formula has appeared under different notation. The closest residual risk is an unlocated equivalent optimization in later or differently indexed work on non-entangling conversions.

## References

1. G. Camacho and J. I. de Vicente, “Nonexistence of maximally entangled mixed states for a fixed spectrum,” arXiv:2511.08285v1 (2025); Phys. Rev. A 113, 022416 (2026), DOI 10.1103/2m8l-kfnm.
2. J. I. de Vicente, “Maximally entangled mixed states for a fixed spectrum do not always exist,” arXiv:2402.05673 (2024); Phys. Rev. Lett. 133, 050202 (2024).
3. F. Verstraete, K. Audenaert, T. De Bie, and B. De Moor, “Maximally entangled mixed states of two qubits,” arXiv:quant-ph/0011110; Phys. Rev. A 64, 012316 (2001).
