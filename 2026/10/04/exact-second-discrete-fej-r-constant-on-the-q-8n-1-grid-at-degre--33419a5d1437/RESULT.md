# Exact second discrete Fejér constant on the \(q=8n+1\) grid at degree two
## Finding
For every integer \(n\ge 2\), set \(q=8n+1\). In Ivanov's second discrete Fejér problem with \(p=3\) and \(\nu=1\), consider even trigonometric polynomials
\[
t(y)=1+2a_1\cos(2\pi y/q)+2a_2\cos(4\pi y/q)
\]
that are nonnegative for every \(y\in\mathbb Z_q\). Then
\[
\lambda(1,3,q)=
\frac{2\cos(\pi/4-\pi/(4q))\cos(\pi/q)}
{1+\sin(\pi/(2q))+\cos(2\pi/q)}.
\]
Writing \(\theta=2\pi/q\), \(r=3n\), \(s=3n+1\), \(c_r=\cos(r\theta)\), and \(c_s=\cos(s\theta)\), the same value is
\[
\lambda(1,3,q)=-\frac{c_r+c_s}{1+2c_rc_s}.
\]
An extremizer is
\[
t_*(y)=
\frac{(\cos(\theta y)-c_r)(\cos(\theta y)-c_s)}
{1/2+c_rc_s}.
\]
Its only zeros on the half-grid \(0\le y\le(q-1)/2\) are \(r=3n\) and \(s=3n+1\).

Ivanov's reduction then gives, for every \(2/q<h\le 3/q\),
\[
A_{\mathbb T}(1/q,h)=\lambda(1,3,q).
\]

## Assumptions and scope
The normalization is the one used for the second discrete Fejér problem: the constant Fourier coefficient is \(a_0=1\), and the objective is the first cosine coefficient \(a_1\). The claim is restricted to \(n\ge2\). The case \(n=1\), hence \(q=9\), is already contained in Ivanov's solved \(q=2p+1\) family and is used only as a consistency check.

## Proof
Put \(\theta=2\pi/q\), \(r=3n\), and \(s=3n+1\). Because \(q=8n+1\), the values \(\cos(\theta y)\) decrease strictly for integers \(0\le y\le4n\). The two roots \(r\) and \(s\) are adjacent grid points. Therefore
\[
\tau(y)=(\cos(\theta y)-c_r)(\cos(\theta y)-c_s)
\]
is nonnegative on the whole grid \(\mathbb Z_q\), by evenness.

Expanding \(\tau\) in the basis \(1,\cos(\theta y),\cos(2\theta y)\) gives
\[
\tau(y)=\tau_0+2\tau_1\cos(\theta y)+2\tau_2\cos(2\theta y),
\]
where
\[
\tau_0=\frac12+c_rc_s,\qquad
\tau_1=-\frac{c_r+c_s}2,\qquad
\tau_2=\frac14.
\]
Both \(c_r\) and \(c_s\) are negative, hence \(\tau_0>0\), so \(t_*=\tau/\tau_0\) is feasible and has first coefficient \(\tau_1/\tau_0\).

It remains to prove optimality. Let
\[
d_r=\cos(2r\theta),\qquad d_s=\cos(2s\theta).
\]
The relation \(q=8n+1\) gives
\[
d_r=-\sin(3\pi/(2q))<0,\qquad
d_s=\sin(5\pi/(2q))>0.
\]
Set
\[
D=c_sd_r-c_rd_s>0,\qquad
\gamma_r=\frac{d_s}{2D},\qquad
\gamma_s=-\frac{d_r}{2D},\qquad
\gamma_0=\gamma_r+\gamma_s.
\]
Thus \(\gamma_r,\gamma_s>0\). Direct coefficient comparison yields, for every even trigonometric polynomial of degree at most two,
\[
\gamma_0a_0-a_1=\gamma_rt(r)+\gamma_st(s).
\]
Indeed,
\[
2(\gamma_rc_r+\gamma_sc_s)=-1,\qquad
2(\gamma_rd_r+\gamma_sd_s)=0.
\]
For every feasible polynomial with \(a_0=1\), nonnegativity at \(r\) and \(s\) therefore implies \(a_1\le\gamma_0\). For \(\tau\), both sampled values vanish, so \(\gamma_0\tau_0=\tau_1\). Hence \(t_*\) attains the upper bound and
\[
\lambda(1,3,q)=\frac{\tau_1}{\tau_0}
=-\frac{c_r+c_s}{1+2c_rc_s}.
\]

Finally, elementary sum-to-product identities and \(q=8n+1\) give
\[
-(c_r+c_s)=2\cos(\pi/4-\pi/(4q))\cos(\pi/q)
\]
and
\[
1+2c_rc_s=1+\sin(\pi/(2q))+\cos(2\pi/q),
\]
which is the stated closed form.

## Verification
The accompanying `verify.py` numerically checks the grid nonnegativity, positivity of the quadrature weights, the coefficient identity, and equality of the two closed forms for \(1\le n\le100\). It prints `VERIFY_OK`. These finite checks are sanity tests only; the proof above is analytic and covers every integer \(n\ge2\).

For the first new member, \(n=2\) and \(q=17\),
\[
\lambda(1,3,17)\approx0.7175495863997976,
\]
with grid zeros \(6\) and \(7\).

## Relationship to prior work
V. I. Ivanov's 2018 paper defines this discrete Fejér problem and proves a quadrature criterion for exactness. It solves several parameter families, including the \(q=2p+1\) family that contains \(\lambda(1,3,9)\). In its conclusion, it explicitly identifies the family \(q=2(p+1)n+1\) as a priority for further computation and predicts the zero pattern
\[
\{\,n(2k+1):1\le k\le p-1\,\}.
\]
For \(p=3\), that family is exactly \(q=8n+1\), and the predicted zeros are \(3n\) and \(5n\), the latter being congruent up to grid symmetry to \(3n+1\). The theorem above proves the entire \(p=3\) subfamily for \(n\ge2\).

Krenedits and Révész provide the broader Carathéodory–Fejér/positive-definite framework on locally compact Abelian groups, but the inspected material does not give this exact \(p=3\), \(q=8n+1\) constant.

## Limitations
The theorem does not address \(p>3\), other residue classes of \(q\), or uniqueness of the extremizer. The literature comparison covered the primary 2018 source, the general 2015 framework, targeted exact-form searches, and a semantic database search; non-indexed literature remains a residual originality risk.

## References
1. V. I. Ivanov, "Pointwise Turán problem for periodic positive definite functions," *Trudy Instituta Matematiki i Mekhaniki UrO RAN* 24(4) (2018), 156–175. DOI: 10.21538/0134-4889-2018-24-4-156-175.
2. S. Krenedits and Sz. Gy. Révész, "Carathéodory–Fejér type extremal problems on locally compact Abelian groups," *Journal of Approximation Theory* 194 (2015), 108–131. DOI: 10.1016/j.jat.2015.02.001.
