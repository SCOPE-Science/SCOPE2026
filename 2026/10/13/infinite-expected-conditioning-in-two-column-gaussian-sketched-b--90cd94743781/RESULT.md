# Infinite expected conditioning in two-column Gaussian-sketched biorthogonalization

## Finding

There are two-column inputs whose columns are orthonormal within each matrix and whose ordinary cross-Gram matrix has condition number only \(\sqrt2\), but whose Gaussian-sketched two-sided Gram–Schmidt output has infinite expected spectral condition number at every fixed finite sketch size \(s\ge2\). Specifically, fix \(n\ge3\) and
\[
X=[e_1,e_3],\qquad Y=[(e_1+e_2)/\sqrt2,e_3]\in\mathbb R^{n\times 2}.
\]
For the output \(Q\) under the signed real normalization defined below, there are constants \(C_s>0\) and \(t_s<\infty\) such that
\[
\mathbb P\{\kappa_2(Q)>t\}\ge C_s/t\quad(t\ge t_s),\qquad
\mathbb E\kappa_2(Q)^r=+\infty\quad(r\ge1).
\]
The corresponding nonsketched output has condition number \(2^{1/4}\). The probabilities are unconditional; the statement neither estimates typical conditioning nor asserts an exact tail asymptotic.

## Assumptions and scope

The entries of \(\Omega\in\mathbb R^{s\times n}\) are independent \(N(0,1/s)\) variables. Use the oblique projections of Algorithm 3.1 of Grigori–Piccinini–Simunec in exact arithmetic. For a nonzero pivot \(d=(\Omega\widetilde q)^{\mathsf T}(\Omega\widetilde p)\), define
\[
q=\widetilde q/\sqrt{|d|},\qquad p=\operatorname{sign}(d)\widetilde p/\sqrt{|d|}.
\]
Thus \((\Omega q)^{\mathsf T}(\Omega p)=1\) for either sign. The condition number is the ratio of the largest and smallest singular values of the full-column-rank output. There is no rejection, safeguard, or conditioning on a successful embedding event.

## Proof

Write \(y_1=(e_1+e_2)/\sqrt2\), \(a=\Omega e_1\), \(b=\Omega y_1\), and \(g=\Omega e_3\). Let
\[
z=a^{\mathsf T}b,\quad h=b^{\mathsf T}g,\quad k=a^{\mathsf T}g,\quad v=g^{\mathsf T}g.
\]
The joint Gaussian density of \((a,b,g)\) is nondegenerate since their three input vectors are linearly independent. The projections following the first normalization produce
\[
\widetilde q_2=e_3-(h/z)e_1,\quad
\widetilde p_2=e_3-(k/z)y_1,\quad
d=(\Omega\widetilde q_2)^{\mathsf T}(\Omega\widetilde p_2)=v-hk/z.
\]
Indeed the projectors on the two sides subtract \(q_1(\Omega p_1)^{\mathsf T}\Omega e_3\) and \(p_1(\Omega q_1)^{\mathsf T}\Omega e_3\), respectively. Both \(z\) and \(zd=zv-hk\) are nonzero almost surely: they are nonzero polynomials, as is seen at the sketch-space point \((a,b,g)=(e_1,e_1,e_2)\).

In the physical orthonormal frame \([e_1,e_3]\), the output is represented by
\[
M=\begin{pmatrix}|z|^{-1/2}&-h/(z\sqrt{|d|})\\0&|d|^{-1/2}\end{pmatrix}.
\]
The singular-value product is \(|\det M|=|zd|^{-1/2}\), and the leading column gives \(\sigma_{\max}(M)\ge |z|^{-1/2}\). Hence
\[
\kappa_2(Q)=\sigma_{\max}(M)^2\sqrt{|zd|}\ge\sqrt{|d|/|z|}.
\]

In sketch space use the point \((a,b,g)=(e_1,e_2,e_1+e_2)\), where \(z=0\), \(h=k=1\), and \(v=2\). In a small bounded neighborhood, \(h,k\ge1/2\), \(v\le10\), and the first coordinate \(a_1\) is at least \(1/2\). For \(0<|z|<1/80\),
\[
|d|\ge 1/(4|z|)-10\ge1/(8|z|),\qquad \kappa_2(Q)\ge1/(\sqrt8|z|).
\]
Replacing \(b_1\) by \(z\) defines a local coordinate change with Jacobian determinant in absolute value \(a_1\). In the transformed neighborhood choose a compact product box containing the base point in its interior. The transformed density is continuous and bounded below by a positive constant on that box. Integrating there over \(0<|z|<\epsilon\) and the other fixed-width coordinates gives probability at least \(c_s\epsilon\) for all sufficiently small \(\epsilon>0\). Taking \(\epsilon=1/(\sqrt8 t)\) gives the asserted lower bound. For \(r\ge1\), integrating \(r t^{r-1}\mathbb P(\kappa_2(Q)>t)\) over large \(t\) diverges.

The ordinary cross-Gram matrix is \(\operatorname{diag}(1/\sqrt2,1)\). The two nonsketched pivots are \(1/\sqrt2\) and \(1\), with no second-column projection corrections, so the ordinary output is \([2^{1/4}e_1,e_3]\).

## Relationship to prior work

Grigori–Piccinini–Simunec introduce the underlying randomized process. Their Proposition 4.1 gives an upper small-ball bound for one sketched inner product. Such an upper bound does not imply an unconditional lower tail for the output condition number. Even a first column with a finite expected norm does not exclude the phenomenon here: the second pivot contains \(hk/z\), which makes the singular-value ratio grow on the order of at least \(1/|z|\) on the transverse neighborhood in the proof.

For context, the single-pivot density and moment cutoffs are consequences of established distributional formulas, not separate findings. For unit vectors with correlation \(c\) and \(|c|<1\), Gaunt's Eq. (2.3) for the average of correlated Gaussian products gives, after the gamma duplication identity,
\[
f_{(\Omega x)^{\mathsf T}\Omega y}(0)
=\frac{s\Gamma(s-1)}{2^{s-1}\Gamma(s/2)^2}(1-c^2)^{(s-2)/2}\quad(s\ge2).
\]
The resulting positive, finite density gives a first-vector norm moment cutoff \(r<2\) for \(r>0\). At \(|c|=1\), the absolute pivot is \(\chi_s^2/s\), giving the cutoff \(r<s\). These scalar facts alone do not control the condition number of the two-column output.

## Verification and limitations

The standard-library script `verify.py` checks rational Schur-complement and triangular-output identities and rational near-breakdown examples. Its density quadratures pertain to the established scalar background. The lower probability tail and the all-\(s\) and all-\(r\) assertions follow from the proof, not from these finite tests. The result neither treats safeguard or embedding-conditioned variants nor classifies moments of the condition number below order one. Even when \(s>n\) the finite-sample conclusion holds, without implying that badly conditioned outputs occur frequently.

## References

1. L. Grigori, L. Piccinini, and I. Simunec, *Randomized biorthogonalization through a two-sided Gram–Schmidt process*, arXiv:2509.04386v1, Algorithm 3.1 and Proposition 4.1. https://arxiv.org/abs/2509.04386v1
2. R. E. Gaunt, *The basic distributional theory for the product of zero mean correlated normal random variables*, Statistica Neerlandica 76 (2022), 450–470, Eq. (2.3). https://arxiv.org/abs/2106.02897v2
