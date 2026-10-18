# Quadratic vanishing of the unfoliated core in an integrable piecewise-affine square map

## Finding

For the nine-piece, area-preserving square homeomorphism \(F_\theta\) constructed by Ostrovski [1], let \(\theta_K\), for every integer \(K\geq3\), be the distinguished parameter defined in [1, Lemma 5.2], and let \(\Gamma_K^0\) be the innermost boundary of the explicitly foliated outer annulus in [1, Corollary 5.4]. Put \(\varepsilon_K=\pi/4-\theta_K\). Denote by \(U_K\) the bounded Jordan domain enclosed by \(\Gamma_K^0\), and by \(I_K=[0,1]^2\setminus\overline{U_K}\) the open outer annulus.

The **exact normalized-area law** is
\[
\operatorname{area}(U_K)=\sin(2\varepsilon_K)-2K(1-\sin(2\varepsilon_K))\sin^2\varepsilon_K.
\]
Its sharp accumulation law is
\[
\varepsilon_K=K^{-1}+\tfrac13K^{-2}+O(K^{-3}),\qquad
\operatorname{area}(U_K)=\tfrac{10}{3}K^{-2}+O(K^{-3}).
\]
Consequently the region guaranteed by [1] to be foliated by invariant polygonal circles has area
\[
\operatorname{area}(I_K)=1-\tfrac{10}{3}K^{-2}+O(K^{-3}).
\]
These statements quantify the protected integrable region only: they do **not** assert chaoticity, ergodicity, or nonintegrability anywhere in \(U_K\).

## Assumptions and scope

Use precisely the geometric map in [1, Sections 2–3]. Set \(t=\sin^2\theta\), \(s=\sin\theta\cos\theta\), and let \(z=(1/2,1/2)\). One corner piece is given by
\[
B=\frac1{t-s}
\begin{pmatrix}
 t^2-(1-s)^2 &(1-2s)t\\
 (2s-1)t &(2t-1)t
\end{pmatrix}.
\]
Let \(v_0=(t,1-s)\) and \(v_K=(s,t)\). The parameter \(\theta_K\in(0,\pi/4)\) is the unique one in [1, Lemma 5.2] satisfying \(B^Kv_0=v_K\), with each intermediate iterate in the appropriate corner piece. Since \(v_K=R(v_0)\) for the quarter-turn \(R(x,y)=(1-y,x)\), the polygonal Jordan curve \(\Gamma_K^0\) has vertices \(R^i B^jv_0\) in their dynamical order, for \(i=0,1,2,3\) and \(j=0,\ldots,K-1\). The Jordan property and complete invariant-circle foliation of the annulus are established in [1]; this result does not reprove them.

Areas are ordinary Euclidean (Lebesgue) areas, with the entire square normalized to area one. The integer \(K\) is at least three throughout; no statement is made for generic \(\theta\).

## Proof

**Exact shoelace calculation.** Define \(v_j=B^jv_0\) for \(0\le j\le K\). Because \(\det B=1\), the oriented cross-products are constant:
\[
\det(v_j,v_{j+1})=\det(v_0,Bv_0)=-t(1-2s).
\]
The last equality follows by substituting the displayed matrix and using \(s^2=t-t^2\). After recentering at \(z\), telescope the cross-products:
\[
\sum_{j=0}^{K-1}\det(v_j-z,v_{j+1}-z)
=K\det(v_0,Bv_0)-\det(z,v_K-v_0).
\]
Here \(v_K-v_0=(s-t,t+s-1)\), so \(\det(z,v_K-v_0)=t-1/2\). Rotating this quarter-boundary by \(R\) four times preserves all centered determinants, and the shoelace formula therefore gives the **signed** enclosed area \(2[-Kt(1-2s)-(t-1/2)]\). Its positive orientation follows from the cyclic vertex order and the positive rotation number \(1/(4K)\) of the Jordan curve established in [1, Theorem 5.1]. Thus
\[
\operatorname{area}(U_K)=1-2t-2Kt(1-2s).
\]
Write \(\varepsilon=\pi/4-\theta\). Using \(2t=1-\sin2\varepsilon\) and \(1-2s=1-\cos2\varepsilon=2\sin^2\varepsilon\) yields the asserted exact formula.

**Parameter law.** The corner matrix has positive eigenvalues \(e^{\mu}\) and \(e^{-\mu}\), with
\[
\cosh\mu=\frac12\operatorname{tr}B
=1+\frac{(1-2s)^2}{2(s-t)}
=1+\frac{2\sin^3\varepsilon}{\cos\varepsilon-\sin\varepsilon}.
\]
It preserves the indefinite quadratic form \(Q(x,y)=t(x^2+y^2)-xy\) [1, Eq. (3.2)]. Polarization, combined with \(v_K=B^Kv_0\), gives
\[
\cosh(K\mu)=\frac{\langle v_0,v_K\rangle_Q}{Q(v_0)}=\frac1{2t}
=\frac1{1-\sin2\varepsilon}.
\]
Both inverse hyperbolic cosines are positive. Hence the exact return parameter obeys
\[
K=\frac{\operatorname{arcosh}((1-\sin2\varepsilon)^{-1})}{
\operatorname{arcosh}(1+2\sin^3\varepsilon/(\cos\varepsilon-\sin\varepsilon))}.
\]
As \(\varepsilon\downarrow0\), Taylor expansion at the positive branch gives
\[
\operatorname{arcosh}((1-\sin2\varepsilon)^{-1})
=2\sqrt{\varepsilon}\,[1+\tfrac56\varepsilon+O(\varepsilon^2)],
\]
\[
\operatorname{arcosh}(1+2\sin^3\varepsilon/(\cos\varepsilon-\sin\varepsilon))
=2\varepsilon^{3/2}[1+\tfrac12\varepsilon+O(\varepsilon^2)].
\]
Therefore \(K=\varepsilon^{-1}+1/3+O(\varepsilon)\), and inversion gives \(\varepsilon_K=K^{-1}+(1/3)K^{-2}+O(K^{-3})\).

Finally,
\[
2K(1-\sin2\varepsilon)\sin^2\varepsilon
=2\varepsilon-\tfrac{10}{3}\varepsilon^2+O(\varepsilon^3),
\]
while \(\sin2\varepsilon=2\varepsilon+O(\varepsilon^3)\). The order-\(\varepsilon\) terms cancel, leaving
\(\operatorname{area}(U_K)=\frac{10}{3}\varepsilon_K^2+O(\varepsilon_K^3)=\frac{10}{3K^2}+O(K^{-3})\).

## Verification

Run the bundled `verify.py` with Python and the `sympy`, `mpmath` and `numpy` packages. It checks the matrix determinant, its preserved quadratic form, the key signed-area algebra modulo \(s^2=t-t^2\), and the analytic formula against direct polygon shoelace areas at \(K=3,4,8,12\). It also checks the large-\(K\) asymptotic numerically. The proof above is independent of these finitely many tests.

## Relationship to prior work

Ostrovski [1] defines the nine-piece map, proves existence and uniqueness of the special sequence \(\theta_K\), constructs \(\Gamma_K^0\), and proves complete foliation of the outer annulus; these qualitative results are **assumed, not rediscovered**. The present statement identifies its exact Lebesgue area and an unexpected quadratic, rather than linear, rate of exhaustion of the square. The source provides eigenvalue and endpoint data but does not state the area identity or the coefficient \(10/3\). Related literature on piecewise-linear area-preserving maps [2,3] addresses other maps and invariant circles without this specific area law.

## Limitations

The result measures one explicitly certified integrable annulus; it does not classify the dynamics of the interior, establish that the annulus is maximal, or characterize typical parameter values. The estimate is asymptotic only along the countable exceptional parameter sequence. Originality is assessed against accessible prior sources, not independently certified; an undiscovered equivalent geometric area formula remains possible.

## References

[1] G. Ostrovski, *Dynamics of a Continuous Piecewise Affine Map of the Square*, arXiv:1305.4282v1 (first public posting 2013-05-18), Sections 2–6 and Appendix; published in *Physica D* 271 (2014), 1–9. https://arxiv.org/html/1305.4282v1

[2] S. Bullett, *Invariant circles for the piecewise linear standard map* (1986), referenced and compared in [1, Section 4].

[3] H. Reeve-Black and F. Vivaldi, *Near-integrable behaviour in a family of discretized rotations*, *Nonlinearity* 26 (2013), 1227–1270, referenced in [1].
