# Sharpness of the \(A_\infty\) endpoint power for sublinear sparse sums

## Result

Fix \(0<r<1\). For the usual dyadic filtration on \([0,1)\), there are \(1/2\)-sparse families
\(\mathcal S_N\) and pairs of weights \((\omega_N,v_N)\), \(N\ge 4\), such that

\[
[\omega_N,v_N]_{A_1}=1,\qquad
[\omega_N]_{A_\infty}\simeq N,
\]

while

\[
\|\mathcal A_{\mathcal S_N}^{r}\|_{L^1(v_N)\to L^{1,\infty}(\omega_N)}
\gtrsim_r N^{1/r-1}
\gtrsim_r [\omega_N]_{A_\infty}^{\,1/r-1}.
\]

Consequently, in a uniform mixed estimate of the form

\[
\|\mathcal A_{\mathcal S}^{r}\|_{L^1(v)\to L^{1,\infty}(\omega)}
\le C_r[\omega,v]_{A_1}[\omega]_{A_\infty}^{\gamma},
\]

the exponent necessarily satisfies

\[
\boxed{\gamma\ge \frac1r-1.}
\]

Thus the \(A_\infty^{1/r-1}\) factor in the new \(0<r<1\), \(p=1\) endpoint estimate of
Gonçalves--Lorist is quantitatively sharp even after the mixed \(A_1\) characteristic is
held identically equal to \(1\).

Here

\[
\mathcal A_{\mathcal S}^{r}f(x)
=
\left(\sum_{I\in\mathcal S}\langle |f|\rangle_I^r\mathbf 1_I(x)\right)^{1/r},
\]

\[
[\omega,v]_{A_1}=\left\|\frac{M_{\mathscr D}\omega}{v}\right\|_\infty,
\qquad
[\omega]_{A_\infty}
=
\sup_{Q\in\mathscr D}
\frac{1}{\omega(Q)}
\int_Q M_{\mathscr D}(\mathbf1_Q\omega).
\]

## Construction

Let

\[
I_j=[0,2^{-j}),\qquad 0\le j\le N,
\]

and take the finite nested sparse chain

\[
\mathcal S_N=\{I_0,I_1,\ldots,I_N\}.
\]

It is \(1/2\)-sparse: for \(j<N\) use \(E_j=I_j\setminus I_{j+1}\), and use
\(E_N=I_N\).

Define

\[
\omega_N=1+2^N\mathbf1_{I_N},
\qquad
v_N=M_{\mathscr D}\omega_N.
\]

Then, by definition,

\[
[\omega_N,v_N]_{A_1}=1.
\]

The point of the example is that \(v_N\) absorbs the maximal-function cost completely,
while the endpoint sparse sum still retains a polynomial dependence on the Fujii--Wilson
\(A_\infty\) characteristic.

## Exact \(A_\infty\) calculation

Every dyadic interval \(Q\subset[0,1)\) is either disjoint from \(I_N\), contained in
\(I_N\), or is one of the ancestors \(I_j\), \(0\le j<N\). In the first two cases the
Fujii--Wilson ratio is \(1\).

For \(Q=I_j\), the dyadic maximal function of \(\mathbf1_{I_j}\omega_N\) is explicit.
On \(I_N\) it equals \(1+2^N\), while on the shell
\(I_k\setminus I_{k+1}\), \(j\le k<N\), it equals the average over \(I_k\),

\[
1+2^k.
\]

Hence

\[
\begin{aligned}
\int_{I_j}M_{\mathscr D}(\mathbf1_{I_j}\omega_N)
&=(1+2^N)2^{-N}
 +\sum_{k=j}^{N-1}(1+2^k)2^{-k-1}\\
&=1+2^{-j}+\frac{N-j}{2}.
\end{aligned}
\]

Since

\[
\omega_N(I_j)=1+2^{-j},
\]

we obtain the exact formula

\[
\boxed{
[\omega_N]_{A_\infty}
=
\max_{0\le j\le N}
\left(1+\frac{N-j}{2(1+2^{-j})}\right).
}
\]

In particular, for \(N\ge2\),

\[
1+\frac{N-1}{3}
\le [\omega_N]_{A_\infty}
\le 1+\frac N2,
\]

so \([\omega_N]_{A_\infty}\simeq N\). More precisely, taking
\(j=\lfloor\log_2N\rfloor\) also gives

\[
[\omega_N]_{A_\infty}=\frac N2+O(\log N).
\]

The same calculation at \(j=0\) gives

\[
\int_0^1 v_N
=
\int_0^1M_{\mathscr D}\omega_N
=
2+\frac N2.
\]

## Weak endpoint lower bound

Take \(f=\mathbf1_{[0,1)}\). Every average of \(f\) over every interval in
\(\mathcal S_N\) is \(1\). Therefore, on \(I_N\),

\[
\mathcal A_{\mathcal S_N}^{r}f=(N+1)^{1/r}.
\]

For the threshold \(t=N^{1/r}\),

\[
I_N
\subset
\{x:\mathcal A_{\mathcal S_N}^{r}f(x)>t\}.
\]

Since

\[
\omega_N(I_N)
=(1+2^N)2^{-N}
=1+2^{-N},
\]

the weak \(L^1(\omega_N)\) quasi-norm obeys

\[
\|\mathcal A_{\mathcal S_N}^{r}f\|_{L^{1,\infty}(\omega_N)}
\ge
N^{1/r}(1+2^{-N}).
\]

On the other hand,

\[
\|f\|_{L^1(v_N)}
=
2+\frac N2.
\]

Thus

\[
\|\mathcal A_{\mathcal S_N}^{r}\|_{L^1(v_N)\to L^{1,\infty}(\omega_N)}
\ge
\frac{N^{1/r}(1+2^{-N})}{2+N/2}
\gtrsim N^{1/r-1}.
\]

Because \([\omega_N,v_N]_{A_1}=1\) and
\([\omega_N]_{A_\infty}\lesssim N\), no smaller exponent of
\([\omega]_{A_\infty}\) can hold uniformly.

## Context

Gonçalves and Lorist prove, for \(0<r<1\),

\[
\|\mathcal A_{\mathcal S}^{r}\|_{L^1(v)\to L^{1,\infty}(\omega)}
\lesssim_r
[\omega,v]_{A_1}
[\omega]_{A_\infty}^{1/r-1}.
\]

Their paper states that this \(r<1\) endpoint case is new even for the classical dyadic
filtration and resolves an open problem left by Nieraeth--Stockdale. In the same discussion
they identify sharpness results for the neighboring \(r=1\), \(p=r=2\), and Rubio de Francia
square-function cases, but do not provide a lower-bound example establishing sharpness of
the new \(p=1,\ r<1\) \(A_\infty\) power.

The construction above supplies that missing lower bound with the strongest possible
separation of the two displayed weight factors: the mixed \(A_1\) characteristic is exactly
one throughout the family.

## Limitations

This result concerns the mixed two-weight endpoint estimate for the positive sparse
operator. It does not assert that every operator admitting an \(\ell^r\)-sparse domination
must attain the same lower bound, and it does not address sharpness of constants depending
on \(r\) or on the sparseness parameter. The construction does not recover the logarithmic
sharpness at \(r=1\), which is a distinct phenomenon already known in the literature.

The source preprint is extremely recent, so an unindexed contemporaneous observation of
the same sharpness example remains the main originality risk.

## References

1. F. Gonçalves and E. Lorist, *Sharp mixed \(A_p\)-\(A_\infty\) estimates for sparse
   operators on filtered and nonhomogeneous measure spaces*, arXiv:2609.20531v1 (2026).
   https://arxiv.org/abs/2609.20531v1

2. Z. Nieraeth and C. B. Stockdale, *Endpoint weak-type bounds beyond
   Calderón--Zygmund theory*, Potential Analysis 65 (2026), Article 15.
   https://arxiv.org/abs/2409.08921

3. T. P. Hytönen and K. Li, *Weak and strong \(A_p\)-\(A_\infty\) estimates for square
   functions and related operators*, Proc. Amer. Math. Soc. 146 (2018), 2497--2507.
   https://arxiv.org/abs/1509.00273
