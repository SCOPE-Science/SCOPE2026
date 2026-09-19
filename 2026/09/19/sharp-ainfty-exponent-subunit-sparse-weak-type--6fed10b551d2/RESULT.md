# Sharp \(A_\infty\) growth at the weak \(L^1\) endpoint for subunit sparse powers

## Result

Let \(\mathscr D\) be the standard dyadic lattice on \(\mathbb R\), and for a finite sparse family \(\mathcal S\subset\mathscr D\) and \(r>0\) write
\[
\mathcal A_{\mathcal S}^{r}f(x)
=
\left(\sum_{Q\in\mathcal S}\langle |f|\rangle_Q^r\,\mathbf 1_Q(x)\right)^{1/r}.
\]
For dyadic weights \(\omega,v\), use
\[
[\omega,v]_{A_1}
=
\left\|\frac{M_{\mathscr D}\omega}{v}\right\|_{L^\infty}
\]
and the dyadic Fujii--Wilson characteristic
\[
[\omega]_{A_\infty}
=
\sup_{Q\in\mathscr D}
\frac{1}{\omega(Q)}
\int_Q M_{\mathscr D}(\mathbf 1_Q\omega).
\]

**Theorem.** Fix \(0<r<1\). There are \(1/2\)-sparse families \(\mathcal S_m\) and weight pairs \((\omega_m,v_m)\), \(m\ge2\), such that
\[
[\omega_m,v_m]_{A_1}=1,\qquad
[\omega_m]_{A_\infty}\asymp m,
\]
and
\[
\|\mathcal A_{\mathcal S_m}^{r}\|_{L^1(v_m)\to L^{1,\infty}(\omega_m)}
\gtrsim m^{1/r-1}.
\]
Consequently,
\[
\|\mathcal A_{\mathcal S}^{r}\|_{L^1(v)\to L^{1,\infty}(\omega)}
\lesssim_r
[\omega,v]_{A_1}[\omega]_{A_\infty}^{\,1/r-1}
\]
has the optimal power of the Fujii--Wilson \(A_\infty\) characteristic, already on the one-dimensional dyadic lattice and even with the mixed \(A_1\) characteristic fixed exactly at \(1\). More generally, no uniform replacement
\[
[\omega]_{A_\infty}^{\,1/r-1}\longmapsto \Phi([\omega]_{A_\infty})
\]
is possible when \(\Phi(t)=o(t^{1/r-1})\).

This supplies the sharpness counterpart for the \(0<r<1\) endpoint factor in Theorem B(ii) of Gonçalves--Lorist, arXiv:2609.20531.

## Construction

For \(j\in\mathbb Z\), put
\[
I_j=[0,2^{-j}),
\qquad
\mathcal S_m=\{I_0,I_1,\dots,I_m\}.
\]
The family is \(1/2\)-sparse: for \(j<m\) take
\[
E_j=I_j\setminus I_{j+1},
\]
and take \(E_m=I_m\).

Set
\[
\omega_m=1+(2^m-1)\mathbf 1_{I_m},
\qquad
v_m=M_{\mathscr D}\omega_m,
\qquad
e_m=1-2^{-m}.
\]
Then, by definition,
\[
[\omega_m,v_m]_{A_1}=1.
\]

## Exact maximal-function profile

For \(0\le j<m\) and \(x\in I_j\setminus I_{j+1}\),
\[
v_m(x)=1+e_m2^j,
\]
while \(v_m=2^m\) on \(I_m\). Hence
\[
V_m:=\|\mathbf 1_{I_0}\|_{L^1(v_m)}
=
2+\frac m2-\left(1+\frac m2\right)2^{-m}.
\]
In particular,
\[
V_m\le 2+\frac m2\le\frac{3m}{2},
\qquad m\ge2.
\]

The same nested geometry gives the Fujii--Wilson characteristic explicitly. A dyadic interval is either disjoint from \(I_m\), contained in \(I_m\), or is the unique ancestor \(I_k\) of \(I_m\) for some \(k\le m\). In the first two cases the local Fujii--Wilson ratio equals \(1\). For \(Q=I_k\),
\[
\omega_m(I_k)=2^{-k}+e_m
\]
and
\[
\int_{I_k}M_{\mathscr D}(\mathbf 1_{I_k}\omega_m)
=
\omega_m(I_k)+\frac{m-k}{2}e_m.
\]
Therefore
\[
[\omega_m]_{A_\infty}
=
\sup_{k\le m}
\left(
1+
\frac{(m-k)e_m}{2(2^{-k}+e_m)}
\right).
\]
For \(m\ge2\), choosing \(k=1\) and using \(e_m\ge3/4\) gives
\[
[\omega_m]_{A_\infty}\ge \frac m4.
\]
On the other hand, if \(0\le k\le m\), the extra term is at most \((m-k)/2\). If \(k=-\ell<0\), then
\[
\frac{(m+\ell)e_m}{2(2^\ell+e_m)}
\le
\frac{m+\ell}{2^{\ell+1}}
\le\frac m2.
\]
Thus
\[
\frac m4\le[\omega_m]_{A_\infty}\le1+\frac m2\le m.
\]

## Weak-type lower bound

Let
\[
f_m=\mathbf 1_{I_0}.
\]
For every \(x\in I_m\), all \(m+1\) averages over the members of \(\mathcal S_m\) are equal to \(1\). Hence
\[
\mathcal A_{\mathcal S_m}^{r}f_m(x)
=(m+1)^{1/r},
\qquad x\in I_m.
\]
Moreover,
\[
\omega_m(I_m)=2^m|I_m|=1.
\]
Using levels tending upward to \((m+1)^{1/r}\) if the weak norm is defined with strict superlevel sets,
\[
\|\mathcal A_{\mathcal S_m}^{r}f_m\|_{L^{1,\infty}(\omega_m)}
\ge (m+1)^{1/r}.
\]
Therefore
\[
\|\mathcal A_{\mathcal S_m}^{r}\|_{L^1(v_m)\to L^{1,\infty}(\omega_m)}
\ge
\frac{(m+1)^{1/r}}{V_m}
\ge
\frac23\,m^{1/r-1}.
\]
Since \([\omega_m]_{A_\infty}\le m\),
\[
\|\mathcal A_{\mathcal S_m}^{r}\|_{L^1(v_m)\to L^{1,\infty}(\omega_m)}
\ge
\frac23\,[\omega_m]_{A_\infty}^{\,1/r-1}.
\]
Because \([\omega_m]_{A_\infty}\ge m/4\to\infty\), every proposed power \(\theta<1/r-1\), and more generally every \(o(t^{1/r-1})\) factor, fails uniformly.

## Context

Gonçalves and Lorist prove in arXiv:2609.20531 that for \(0<r<1\)
\[
\|\mathcal A_{\mathcal S}^{r}\|_{L^1(v)\to L^{1,\infty}(\omega)}
\lesssim_{r,\eta}
[\omega,v]_{A_1}[\omega]_{A_\infty}^{1/r-1}.
\]
They note that this endpoint estimate is new even for the classical dyadic filtration and resolves the \(q<1\) question raised by Nieraeth and Stockdale after Corollary C of arXiv:2409.08921. Their discussion separately records known sharpness at the logarithmic \(r=1\) endpoint and sharp weighted consequences for square functions, but does not give a sharpness example for the new \(0<r<1\) \(A_\infty\) power.

The earlier Hytönen--Li mixed weak bound, arXiv:1509.00273, treats \(p>1\) and contains the analogous exponent \((1/r-1/p)_+\); the \(p=1\), \(r<1\) endpoint was outside that theorem.

## Limitations

The result is a sharpness theorem for the sparse model itself. It proves optimality of the \(A_\infty\) exponent in the general endpoint sparse bound, but it does not by itself prove matching lower bounds for every concrete operator admitting sparse domination. It does not optimize the numerical constant, address the logarithmic \(r=1\) endpoint, determine sharp dependence on the mixed \(A_1\) factor, or give a new upper bound. The example is one-dimensional and dyadic, which is sufficient for impossibility of improving the general exponent.

Originality is asserted only to the best of our knowledge.

## References

1. F. Gonçalves and E. Lorist, *Sharp mixed \(A_p\)-\(A_\infty\) estimates for sparse operators on filtered and nonhomogeneous measure spaces*, arXiv:2609.20531 (2026). https://arxiv.org/abs/2609.20531
2. Z. Nieraeth and C. B. Stockdale, *Endpoint weak-type bounds beyond Calderón--Zygmund theory*, arXiv:2409.08921; Potential Analysis 65, Article 15 (2026). https://arxiv.org/abs/2409.08921
3. T. P. Hytönen and K. Li, *Weak and strong \(A_p\)-\(A_\infty\) estimates for square functions and related operators*, Proc. Amer. Math. Soc. 146 (2018), 2497--2507. https://arxiv.org/abs/1509.00273
