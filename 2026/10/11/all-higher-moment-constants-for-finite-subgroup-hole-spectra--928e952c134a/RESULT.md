# All higher-moment constants for finite subgroup-hole spectra
## Finding
Let \(G\) be a finite abelian group of order \(N\), let \(K\le\widehat G\) be a proper subgroup of order \(k\), put \(H=K^\perp\), and write \(m=|H|=N/k\ge2\). Set \(\Lambda=\widehat G\setminus K\). For every real \(p>4\), with normalized counting measure on \(G\),
\[
\left\|\sum_{\chi\in\Lambda}a_\chi\chi\right\|_p
\le K_p(\Lambda)\left(\sum_{\chi\in\Lambda}|a_\chi|^2\right)^{1/2},
\]
and the exact sharp constant is
\[
K_p(\Lambda)^p
=\frac{k^{p/2-1}}{m}
\left((m-1)^{p/2}+(m-1)^{1-p/2}\right).
\]
Every nonzero extremizer is exactly
\[
a_\chi=A\,\overline{\chi(y)}\qquad(\chi\in\Lambda)
\]
for some \(A\ne0\) and \(y\in G\). Equivalently, in physical space every extremizer is
\[
f(x)=Ak\left(m\mathbf 1_{\{y\}}(x)-\mathbf 1_{y+H}(x)\right).
\]

## Assumptions and scope
Characters are normalized to have \(L^2(G)\)-norm one, and \(L^p(G)\) uses normalized counting measure. The theorem is for every finite abelian group, every proper dual subgroup, and every finite real exponent \(p>4\). The endpoint \(p=4\) follows from the same fourth-moment estimate but has extra equality issues in low-dimensional degeneracies, so the complete equality statement above is deliberately restricted to \(p>4\). Exponents below four are not covered.

The annihilator relation \(H=K^\perp\) implies \(|H||K|=N\). A function has Fourier support in \(\Lambda\) exactly when its sum on every coset of \(H\) is zero.

## Proof
First prove a sharp zero-sum lemma. Let \(z_1,\ldots,z_m\in\mathbb C\) satisfy \(\sum_j z_j=0\), and normalize \(\sum_j|z_j|^2=1\). Put \(y_j=|z_j|^2\). Then \(\sum_jy_j=1\). For every index \(i\),
\[
|z_i|=\left|\sum_{j\ne i}z_j\right|
\le\sqrt{(m-1)(1-|z_i|^2)},
\]
so
\[
0\le y_i\le M:=\frac{m-1}{m}.
\]

We also need the exact fourth-moment bound
\[
\sum_j y_j^2\le B:=\frac{m^2-3m+3}{m(m-1)}.
\]
For \(m=2\) this is immediate. Assume \(m\ge3\), let \(t=\max_jy_j\), and relabel so \(y_1=t\). If \(t\le1/2\), then \(\sum_jy_j^2\le t\le1/2\le B\). If \(t\ge1/2\), zero-sum closure gives
\[
\sqrt t\le\sum_{j>1}\sqrt{y_j}.
\]
After squaring and applying Cauchy--Schwarz to the \(\binom{m-1}2\) pair products,
\[
\sum_{2\le i<j\le m}y_i y_j
\ge\frac{(2t-1)^2}{2(m-1)(m-2)}.
\]
Consequently
\[
\sum_jy_j^2
\le t^2+(1-t)^2-\frac{(2t-1)^2}{(m-1)(m-2)}=:U_m(t).
\]
On \([1/2,M]\), \(U_m\) is nondecreasing; for \(m=3\) it is constant. Direct substitution gives \(U_m(M)=B\), proving the claim.

If \(m=2\), the zero-sum relation forces \(z_2=-z_1\), so the desired local bound and equality class are immediate. Hence assume \(m\ge3\). Now put \(q=p/2>2\) and
\[
r:=\frac1{m(m-1)}.
\]
Let \(Q\) be the quadratic Hermite interpolant to \(t^q\) with a double contact at \(r\) and a simple contact at \(M\):
\[
Q(r)=r^q,\qquad Q'(r)=q r^{q-1},\qquad Q(M)=M^q.
\]
In Newton form,
\[
Q(t)=r^q+q r^{q-1}(t-r)+a(t-r)^2,
\]
where \(a=[r,r,M](t^q)>0\). Because the second derivative of \(t^q\) is strictly increasing for \(q>2\), the Hermite error has the sign of \((t-r)^2(t-M)\). Hence
\[
t^q\le Q(t)\qquad(0\le t\le M),
\]
with equality only at \(t=r\) or \(t=M\). For \(2<q<3\), the statement at \(t=0\) follows by continuity from positive \(t\).

Therefore
\[
\sum_j y_j^q
\le a\sum_jy_j^2+b\sum_jy_j+mc
\le aB+b+mc
=Q(M)+(m-1)Q(r),
\]
where \(Q(t)=at^2+bt+c\). Since
\[
M+(m-1)r=1,\qquad M^2+(m-1)r^2=B,
\]
we obtain
\[
\sum_j|z_j|^p
\le A_{m,p}\left(\sum_j|z_j|^2\right)^{p/2},
\qquad
A_{m,p}=m^{-p/2}\left((m-1)^{p/2}+(m-1)^{1-p/2}\right).
\]
For \(m>2\), equality in the strict Hermite majorant forces exactly one \(y_j=M\) and the other \(m-1\) values to equal \(r\). Equality in the closing triangle inequality then forces all small coordinates to have a common phase opposite the large coordinate. The case \(m=2\) is the forced antipodal pair. Thus the local equality class is complete.

Return to \(G\). For each coset \(C\) of \(H\), put
\[
S_C=\sum_{x\in C}|f(x)|^2.
\]
The zero-sum lemma gives
\[
\sum_{x\in C}|f(x)|^p\le A_{m,p}S_C^{p/2}.
\]
Summing over the \(k\) cosets and using \(p/2>1\),
\[
\|f\|_p^p
\le A_{m,p}N^{p/2-1}\|f\|_2^p.
\]
Since \(N=km\), this is exactly the displayed formula for \(K_p(\Lambda)^p\).

Equality in the coset convexity step forces all \(L^2\)-mass onto one coset. The local equality classification then gives, for some \(B\ne0\) and \(y\in G\),
\[
f=B\left(m\mathbf 1_{\{y\}}-\mathbf 1_{y+H}\right).
\]
Fourier inversion gives \(\widehat f(\chi)=(B/k)\overline{\chi(y)}\) for every \(\chi\notin K\), and zero on \(K\). Renaming \(B/k\) as \(A\) proves the stated coefficient equality class and sharpness.

## Verification
The bundled `verify.py` was replayed from the package directory. It returned:

`VERIFY_OK`

`hermite_majorant_checks=224224 max_signed_excess=2.220e-16`

`random_zero_sum_checks=16560 max_excess=1.665e-16`

`equality_checks=288`

`p4_p6_specialization_checks=1248`

`cyclic_fourier_extremizer_checks=216`

These computations are regression checks only. The proof of the continuum statement is the analytic zero-sum/Hermite argument above. The specialization checks confirm that the formula reduces algebraically to the fourth- and sixth-moment subgroup-hole formulas, and the cyclic checks independently evaluate the claimed extremizers on explicit finite groups.

## Relationship to prior work
Michels gives the standard \(\Lambda(p)\) framework and the constant \(K_p(\Lambda)\) for character sets, but the inspected paper concerns infinite character sets and operator-ideal limit orders rather than exact constants for finite complements of subgroups. Gilbert and Rzeszotnik determine full Fourier-transform operator norms on finite abelian groups and characterize their extremals; their theorem is for the unrestricted transform between full \(L^p\) spaces, not for the spectral subspace obtained by deleting a dual subgroup. Their subgroup wave packets therefore do not imply the subgroup-hole constant proved here.

The new mechanism is the sharp all-real-\(p\) norm of the complex zero-sum hyperplane, obtained from a fourth-moment constraint plus a Hermite quadratic majorant. This simultaneously yields the finite harmonic-analysis theorem for every real \(p>4\), rather than for isolated even moments.

## Limitations
The theorem does not treat \(2<p<4\), where the one-large-coordinate extremal pattern can fail. The complete equality statement is asserted only for \(p>4\). The literature search cannot exclude an older equivalent zero-sum-hyperplane inequality hidden under matrix-norm, centered-sequence, or convexity terminology; no decisive unresolved source was found.

## References
1. C. Michels, *Lambda(p)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first submitted 1999-04-30.
2. J. Gilbert and Z. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Annales de l'Institut Fourier 60 (2010), 1317--1346, DOI 10.5802/aif.2556.
