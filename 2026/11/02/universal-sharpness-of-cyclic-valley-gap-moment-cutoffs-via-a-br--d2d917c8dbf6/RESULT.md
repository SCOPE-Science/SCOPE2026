# Universal sharpness of cyclic valley-gap moment cutoffs via a Brownian-bridge trace

## Finding

For every pair of positive integers \(i,j\), the exact-linear moment thresholds for the number \(D_{i,K}\) of successive valleys separated by \(i+1\) sites in a uniformly random cyclic permutation are **optimal without exceptions**. Specifically, put
\[
a_i=\frac{i\,2^{i+1}}{i!\,(i+1)(i+2)(i+4)},\qquad K_0=i+j+6.
\]
Then
\[
\boxed{\mathbb E D_{i,i+3}=(i+4)a_i>(i+3)a_i.}
\]
Let \(c_{ij}\) denote the exact covariance slope for \(K\ge i+j+7\) as given in Matijasevick (2026), Proposition 3.1. Introduce the symmetric integral kernels on \([0,1]^2\)
\[
A_i(s,t)=\frac{(s+t)^i-|s-t|^i}{2i!},\qquad
B(s,t)=\min(s,t)-st.
\]
Writing \(A_i\) and \(B\) also for their operators on \(L^2([0,1])\), the exact first subthreshold covariance correction is
\[
\boxed{\frac{\operatorname{Cov}(D_{i,K_0},D_{j,K_0})}{K_0}-c_{ij}
=\operatorname{tr}(A_i B A_j B)>0.}
\]
In particular the variance slope \(b_i=c_{ii}\) fails at \(K=2i+6\) for **every** \(i\ge1\); the mean fails at \(K=i+3\); and the mixed covariance fails at \(K=i+j+6\) for every \(i,j\ge1\). Hence the proven thresholds \(i+4\), \(2i+7\), \(i+j+7\) for exact linearity cannot be reduced in any parameter.

## Assumptions and scope

Take \(K\ge3\) independent continuously distributed priorities at cyclic sites \(0,\ldots,K-1\), with cyclic subscripts. A site is a **valley** when its priority is strictly less than those of both neighbors. Let \(D_{i,K}\) count cyclically successive pairs of distinct valleys at positive clockwise distance \(i+1\), including the wrap-around gap; set it to zero when there is only one valley. Only positive integers \(i,j\) are considered. This priority model is the root-set representation of uniform ballistic deposition established in Matijasevick (2026), Lemmas 2.1–2.2. Its probability law is unchanged by any common continuous increasing transform of the priorities.

The slope \(c_{ij}\) is **not** claimed as new. For an independent infinite sequence, put \(g=i+1\), \(h=j+1\), and define \(Y_x^{(g)}\) as the indicator that \(x\) and \(x+g\) are successive valleys. Write \(u(s)=s\) and \(M(s,t)=\min(s,t)\). With the integral-operator convention \((Af)(s)=\int_0^1A(s,t)f(t)dt\), the source constants have the precise representation
\[
a_i=\langle u,A_i u\rangle,\quad
u_{ij}=\langle u,A_i A_j u\rangle,\quad
v_{ij}=\langle u,A_i M A_j u\rangle,
\]
\[
c_{ij}=\mathbf1_{\{i=j\}}a_i+2\nu_{ij}+2v_{ij}-(i+j+7)a_i a_j.
\]
All integral operators are bounded Hilbert–Schmidt operators, so the indicated fourth-order products are trace-class.

## Proof

**1. Excursion and outside-neighbor kernels.** Conditional on endpoint priorities \(1-s\) and \(1-t\), the probability that the \(i\) interior priorities form the required single increasing-then-decreasing excursion is \(A_i(s,t)\). This is the excursion-kernel identity proved in Matijasevick (2026), Lemma 4.2; alternatively it follows by choosing the peak and assigning each remaining interior value to its allowed side. When the two immediate outside neighbors are distinct, independent uniform priorities, the additional probability that the endpoints are valleys is \(st\). For a gap with a **shared** outside neighbor, that probability becomes \(\min(s,t)\).

At \(K=i+3\), the outside neighbors of the length-\(i+1\) gap are the same cyclic site. Therefore
\[
\mathbb E D_{i,i+3}=(i+3)\int_0^1\!\int_0^1 A_i(s,t)M(s,t)\,ds\,dt.
\]
Subtract the usual \((i+3)a_i\) and use \(B=M-u\otimes u\). Because \(A_i\) and \(B\) are symmetric and \(B(s,t)=s(1-t)\) on \(0<s<t<1\), substituting \(s=tz\) gives
\[
\begin{aligned}
\int_0^1\!\int_0^1 A_i(s,t)B(s,t)\,ds\,dt
&=\frac{1}{i!(i+3)(i+4)}
\int_0^1 z\big((1+z)^i-(1-z)^i\big)dz\\
&=\frac{i\,2^{i+1}}{i!(i+1)(i+2)(i+3)(i+4)}
=\frac{a_i}{i+3}.
\end{aligned}
\]
Hence \(\mathbb E D_{i,i+3}=(i+4)a_i\). The correction equals \(a_i>0\) in the unnormalized mean.

**2. The unique collision of the two covariance boundary offsets.** Fix \(i,j\ge1\), write \(g=i+1\), \(h=j+1\), \(K_0=g+h+4\), and set
\[
q_{ij}=\operatorname{tr}(A_i M A_j M).
\]
Since \(K_0\ge i+4,j+4\), every single-gap indicator has the ordinary expectation \(a_i\) or \(a_j\). For a fixed initial length-\(g\) gap beginning at zero, another length-\(h\) gap can overlap without contradicting the valley condition only at the following offsets modulo \(K_0\):

- \(h_0=0\) if \(i=j\), giving probability \(a_i\);
- \(h_0=g\) or \(h_0=-h\), when the long gaps are consecutive, each giving \(\nu_{ij}\);
- \(h_0=g+2=-h-2\pmod {K_0}\), where the two long gaps are separated by *two* distinct length-two gaps, giving \(q_{ij}\).

This list is exhaustive: no two valleys are adjacent; an extra valley cannot lie strictly inside either selected gap; and the two indicator windows have total size \(K_0+2\), so they cannot be disjoint. The wrapped configuration in the last case consists cyclically of gap lengths \(g,2,h,2\). Each length-two gap has excursion kernel \(M(s,t)\), yielding the trace formula for \(q_{ij}\) by four endpoint integrations.

Translation invariance thus gives
\[
\frac{\operatorname{Cov}(D_{i,K_0},D_{j,K_0})}{K_0}
=\mathbf1_{\{i=j\}}a_i+2\nu_{ij}+q_{ij}-K_0a_i a_j.
\]
Comparing with the displayed established formula for \(c_{ij}\), where \(i+j+7=K_0+1\), gives
\[
\frac{\operatorname{Cov}(D_{i,K_0},D_{j,K_0})}{K_0}-c_{ij}
=q_{ij}-2v_{ij}+a_i a_j.
\]
As \(B=M-u\otimes u\), cyclic invariance of trace and symmetry of \(A_i,A_j,M\) imply exactly
\[
q_{ij}-2v_{ij}+a_i a_j=\operatorname{tr}(A_i B A_j B).
\]

**3. Strict positivity for every pair.** For \(s,t\in(0,1)\), \(A_i(s,t)>0\) because \(s+t>|s-t|\), and \(B(s,t)=\min(s,t)(1-\max(s,t))>0\). Thus the kernel of \(A_iB\) is strictly positive throughout \((0,1)^2\); likewise for \(A_jB\). The trace identity
\[
\operatorname{tr}(A_i B A_j B)
=\int_0^1\!\int_0^1 (A_iB)(s,t)(A_jB)(t,s)\,dt\,ds>0
\]
is valid for these Hilbert–Schmidt products. This completes the universal proof, including the diagonal \(i=j\) case. For the diagonal, it is also the squared Hilbert–Schmidt norm of \(B^{1/2}A_iB^{1/2}\).

## Verification

The standalone `verify.py` exhaustively enumerates all permutations through ten sites at selected boundary instances and compares **exact fractions** with the published slopes and the predicted anomalies. It also evaluates the trace by 200-node Gaussian quadrature, independently checking four small pairs. Run with `python verify.py` from a directory containing `verify.py` and, for the quadrature checks, NumPy. The attached `verification_output.txt` records 26 passed finite equality/positivity/quadrature assertions. These finite tests are supplementary and do not replace the quantified all-integer proof above.

In particular, the exact covariance discrepancies per site are
\[
\begin{array}{c|c}
(i,j)&\operatorname{Cov}(D_{i,K_0},D_{j,K_0})/K_0-c_{ij}\\\hline
(1,1)&29/28350\\
(1,2)&2/2835\\
(1,3)&47/155925\\
(2,2)&1/2025
\end{array}
\]
with the respective boundary sizes \(8,9,10,10\). The expectation formula was independently checked for \(i=1,2,3,4\). All fractions refer to probabilities of finite random permutations and are exact.

## Relationship to prior work

Matijasevick (2026), Proposition 3.1, proves exact linearity for \(K\ge i+4\) in the mean and \(K\ge i+j+7\) in covariance; Remark 3.2 reports empirical sharpness only over the parameters reached by exhaustive enumeration. The present result proves optimality **uniformly for every pair of positive indices**, and evaluates the entire first subthreshold discrepancy as a strictly positive Brownian-bridge trace. It does not claim the slope formulas, the excursion kernel, or the random-priority representation as new.

Mansour–Rastegar–Roitershtein (2019) supplies the underlying deposition model and particular small-gap formulas. Earlier enumerations of peak sets and classical linear-run covariances are relevant antecedents, but do not in the inspected material establish this precise all-index cyclic boundary correction. General pattern-overlap methodology may provide alternative derivations; full historical priority should be independently assessed.

## Limitations

The theorem concerns uniform cyclic-deposition priorities / uniform random cyclic permutations, only exact first and second moments, and the **single** cycle size just below each known exact-linear threshold. It does not give formulas at every smaller size, a nonuniform-deposition extension, a new central limit theorem, or a claim of full bibliographic uniqueness. Numerical quadrature is not used to prove strict positivity, which follows directly from the kernels. Independent external mathematical validation has not been performed.

## References

1. Mateo Matijasevick, *Gaps between roots in ballistic deposition on a strip: linear variance, Gaussian limits and a Poisson regime* (first posted 2026-10-15), arXiv:2610.21094v1. https://arxiv.org/abs/2610.21094 . Particularly Proposition 3.1, Remark 3.2, Lemma 4.2, and Theorem 4.5.
2. Toufik Mansour, Reza Rastegar, Alexander Roitershtein, *On ballistic deposition process on a strip* (2019), arXiv:1903.12548v2. https://arxiv.org/abs/1903.12548 .
3. Howard Levene and Jacob Wolfowitz, *The covariance matrix of runs up and down* (1944), *Annals of Mathematical Statistics* 15. Historical context; no priority assertion is based on an inspection of its complete text.
