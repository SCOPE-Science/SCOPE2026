# Exact Euclidean Banach--Mazur distance of the two-dimensional \(p=3\) Cesàro space
## Finding
Let \(X=\mathrm{ces}_3^{(2)}\) be \(\mathbb R^2\) with \(\|(x,y)\|=\left(|x|^3+\left((|x|+|y|)/2\right)^3\right)^{1/3}\). Let \(\tau>0\) be the unique solution of \(3^{4/3}(1+\tau)^2=\tau\left((1+\tau)^2+8\right)\). Then \[d_{\mathrm{BM}}(X,\ell_2^2)^2=\frac{\left(8+(1+\tau)^3\right)^{2/3}}{3^{4/3}+\tau^2},\]so \(d_{\mathrm{BM}}(X,\ell_2^2)^2\approx1.29958204360103898476\) and \(d_{\mathrm{BM}}(X,\ell_2^2)\approx1.13999212435921634518\). An optimal Euclidean pullback, up to positive scaling, is \(|(x,y)|_*^2=x^2+3^{-4/3}y^2\).

## Assumptions and scope
The space is real and two-dimensional. The norm is
\[
\|(x,y)\|=\left(|x|^3+\left(\frac{|x|+|y|}2\right)^3\right)^{1/3}.
\]
The Banach--Mazur distance is taken over all invertible real linear maps from \(X\) to the Euclidean plane. No claim is made here for \(\mathrm{ces}_p^{(2)}\) at exponents other than \(p=3\).

## Proof
For a positive-definite quadratic form \(q\), write
\[
\Delta(q)=\frac{\sup_{v\ne0}\|v\|^2/q(v)}{\inf_{v\ne0}\|v\|^2/q(v)}.
\]
Then \(d_{\mathrm{BM}}(X,\ell_2^2)^2=\inf_q\Delta(q)\).

The norm is invariant under the two coordinate sign changes. If
\[
m\,q(v)\le \|v\|^2\le M\,q(v)
\]
holds for all \(v\), averaging \(q\) over those sign changes preserves both inequalities and removes the mixed term. Hence an optimal distortion is attained within diagonal forms. After a positive rescaling, it is enough to consider
\[
q_r(x,y)=x^2+r y^2,\qquad r>0.
\]

By homogeneity and absoluteness, put \(t=|y|/|x|\) and define
\[
F_r(t)=\frac{\|(1,t)\|^2}{1+r t^2}
=\frac{\left((8+(1+t)^3)/8\right)^{2/3}}{1+r t^2},
\qquad 0\le t<\infty.
\]
Its logarithmic derivative vanishes exactly when
\[
r=R(t):=\frac{(1+t)^2}{t\left((1+t)^2+8\right)}.
\]
Moreover
\[
R'(t)=-
\frac{(t+1)\left(t^3+3t^2-5t+9\right)}{t^2(t^2+2t+9)^2}<0,
\]
because
\[
t^3+3t^2-5t+9=t(t-1)^2+5\left(t-\frac35\right)^2+\frac{36}5>0.
\]
Thus each \(F_r\) has one interior critical point, and it is the global maximum; the minimum is at one of the two endpoints.

The endpoint values are
\[
F_r(0)=\left(\frac98\right)^{2/3}=\frac{3^{4/3}}4,
\qquad
\lim_{t\to\infty}F_r(t)=\frac1{4r}.
\]
Set
\[
r_0=3^{-4/3},
\]
so these endpoint values coincide. Let \(\tau\) be the unique positive number with \(R(\tau)=r_0\), equivalently
\[
3^{4/3}(1+\tau)^2=\tau\left((1+\tau)^2+8\right).
\]

For \(r\le r_0\), the endpoint minimum is at most \(F_r(0)\), while \(F_r(\tau)\) decreases as \(r\) increases. Therefore
\[
\Delta(q_r)\ge \frac{F_r(\tau)}{F_r(0)}
\ge \frac{F_{r_0}(\tau)}{F_{r_0}(0)}.
\]
For \(r\ge r_0\), the endpoint minimum is at most \(1/(4r)\), and
\[
4rF_r(\tau)
\]
is increasing in \(r\). Hence again
\[
\Delta(q_r)\ge
4rF_r(\tau)\ge
4r_0F_{r_0}(\tau)
=\frac{F_{r_0}(\tau)}{F_{r_0}(0)}.
\]
At \(r=r_0\), the two endpoints are equal minima and \(\tau\) is the unique maximum, so equality holds. Simplifying the quotient gives
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2
=
\frac{\left(8+(1+\tau)^3\right)^{2/3}}{3^{4/3}+\tau^2}.
\]

## Verification
The bundled `verify.py` independently bisects the defining equation for \(\tau\), checks the endpoint equalization for \(r_0=3^{-4/3}\), and evaluates the displayed exact formula numerically. The replay gives
\[
\tau\approx2.76673988007870113907,
\]
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2\approx1.29958204360103898476,
\]
and
\[
d_{\mathrm{BM}}(X,\ell_2^2)\approx1.13999212435921634518.
\]
The exact proof does not depend on the numerical approximation.

## Relationship to prior work
Zuo's 2012 paper defines the two-dimensional Cesàro norm for general \(1<p<\infty\), develops exact Ptolemy-constant methods for absolute normalized norms, and gives the exact Ptolemy constant of \(\mathrm{ces}_2^{(2)}\). The inspected article does not state a Banach--Mazur distance formula for \(\mathrm{ces}_3^{(2)}\), and text search of the full article found no Banach--Mazur discussion. Targeted searches for the exact \(p=3\) Euclidean distortion and for a John/Löwner-ellipsoid formulation did not locate a published statement implying the formula above.

## Limitations
This result concerns only the real two-dimensional \(p=3\) Cesàro norm. The proof reduces the Banach--Mazur optimization to diagonal quadratic forms by sign symmetry; it does not classify all optimal linear maps. Literature searches cannot prove nonexistence of an obscure earlier equivalent formulation, so an older result under different convex-geometry terminology remains a residual bibliographic risk.

## References
Z. Zuo, *The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\)*, Journal of Inequalities and Applications 2012, Article 107, DOI `10.1186/1029-242X-2012-107`, published 17 May 2012.

J. S. Shue, *On the Cesàro sequence spaces*, Tamkang Journal of Mathematics 1 (1970), 143--150.
