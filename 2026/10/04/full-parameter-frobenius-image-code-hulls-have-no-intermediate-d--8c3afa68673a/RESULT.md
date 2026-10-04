# Full-parameter Frobenius image-code hulls have no intermediate dimensions
## Finding

Let \(q\) be a prime power, \(m\ge2\), \(1\le k<m\), and
\[
d=\gcd(k,m).
\]
For every projective parameter
\[
(\lambda:\mu)\in\mathbb P^1(\mathbb F_{q^m}),
\]
consider
\[
\phi_{\lambda,\mu}(x)=\lambda x+\mu x^{q^k},
\qquad
C_{\lambda,\mu}=\operatorname{im}\phi_{\lambda,\mu}\subseteq\mathbb F_{q^m},
\]
with the trace inner product used in the cited source. Then
\[
\dim_{\mathbb F_q}\operatorname{Hull}(C_{\lambda,\mu})\in\{0,d\}.
\]
In particular, there are no intermediate hull dimensions on the full parameter line. Every non-LCD member has hull dimension exactly \(d\).

## Assumptions and scope

The trace pairing is
\[
\langle x,y\rangle=\operatorname{Tr}_{\mathbb F_{q^m}/\mathbb F_q}(xy).
\]
The source proves that the adjoint of \(\phi_{\lambda,\mu}\) is
\[
\phi_{\lambda,\mu}^{\dagger}(y)
=\lambda y+\mu^{q^{m-k}}y^{q^{m-k}},
\]
and that
\[
\operatorname{Hull}(C_{\lambda,\mu})
=\operatorname{im}\phi_{\lambda,\mu}\cap\ker\phi_{\lambda,\mu}^{\dagger}.
\]
No restriction such as \(\gcd(m,\operatorname{char}\mathbb F_q)=1\) is needed for the dichotomy proved here.

## Proof

Put
\[
K=\mathbb F_{q^d}.
\]
Because \(d\mid k\) and \(d\mid(m-k)\), every \(a\in K\) satisfies
\[
a^{q^k}=a^{q^{m-k}}=a.
\]
Hence both operators are \(K\)-linear:
\[
\phi_{\lambda,\mu}(ax)=a\phi_{\lambda,\mu}(x),
\qquad
\phi_{\lambda,\mu}^{\dagger}(ay)=a\phi_{\lambda,\mu}^{\dagger}(y).
\]
Therefore \(\operatorname{im}\phi_{\lambda,\mu}\), \(\ker\phi_{\lambda,\mu}^{\dagger}\), and their intersection are \(K\)-subspaces.

It remains to bound the \(K\)-dimension of the adjoint kernel. If either coefficient of
\[
\phi_{\lambda,\mu}^{\dagger}(y)=\lambda y+\mu^{q^{m-k}}y^{q^{m-k}}
\]
vanishes, then the nonzero projective parameter makes the map a nonzero scalar multiple of either the identity or a Frobenius automorphism, so its kernel is zero.

Assume now \(\lambda\mu\ne0\). If the adjoint kernel is nonzero and \(u,v\) are two nonzero kernel elements, then
\[
\lambda u=-\mu^{q^{m-k}}u^{q^{m-k}},
\qquad
\lambda v=-\mu^{q^{m-k}}v^{q^{m-k}}.
\]
Dividing the two equations gives
\[
\left(\frac uv\right)^{q^{m-k}}=\frac uv.
\]
The fixed field of the \(q^{m-k}\)-Frobenius on \(\mathbb F_{q^m}\) is
\[
\mathbb F_{q^{\gcd(m-k,m)}}=\mathbb F_{q^d}=K.
\]
Thus \(u/v\in K\). Since the kernel is already a \(K\)-subspace, any nonzero kernel is exactly one-dimensional over \(K\).

Consequently
\[
\ker\phi_{\lambda,\mu}^{\dagger}
\]
is either \(0\) or a one-dimensional \(K\)-space. Its intersection with the \(K\)-subspace \(\operatorname{im}\phi_{\lambda,\mu}\) is therefore either \(0\) or the whole kernel. Converting \(K\)-dimension back to \(\mathbb F_q\)-dimension gives precisely
\[
\dim_{\mathbb F_q}\operatorname{Hull}(C_{\lambda,\mu})\in\{0,d\}.
\]

The source already characterizes when the extremal value \(d\) occurs by a trace-isotropy condition. Since no positive intermediate value can occur, that condition becomes a complete criterion for non-LCD behavior on the residual singular locus.

## Verification

`artifacts/verify.py` performs exact finite stress tests over binary extension fields. For every projective parameter in the listed cases, it constructs \(\phi_{\lambda,\mu}\) and its trace adjoint as binary linear maps, computes \(\operatorname{im}\phi_{\lambda,\mu}\cap\ker\phi_{\lambda,\mu}^{\dagger}\), and checks that the hull dimension is always \(0\) or \(d\). The resulting distributions agree with `artifacts/certificate.json`.

These finite computations are not used as an infinite proof. The theorem for all prime powers follows from the fixed-subfield argument above.

## Relationship to prior work

Bartoli, Grimaldi, and Stănică develop the image-code hull framework and prove the adjoint intersection formula over the full parameter space. For the Frobenius twist they show that a nonzero kernel is an \(\mathbb F_{q^d}\)-line. Nevertheless, their current abstract describes the full-parameter singular hull dimension only as lying between \(0\) and \(d\), and their self-adjoint theorem likewise leaves a parameter \(\delta\) with
\[
0\le\delta\le d,
\]
characterizing only the extremal case \(\delta=d\).

The additional observation is that the image is also automatically \(\mathbb F_{q^d}\)-linear. Intersecting an \(\mathbb F_{q^d}\)-subspace with an \(\mathbb F_{q^d}\)-line cannot produce an intermediate \(\mathbb F_q\)-dimension. This closes the remaining interval in the full-parameter Frobenius classification.

Searches for an exact full-parameter dichotomy, for hull dimensions that are multiples of \(d\), and for the \(\mathbb F_{q^d}\)-linearity argument found no prior statement of this conclusion. The closest indexed hull result located concerns generalized Roth--Lempel Galois hulls and is a different code family.

## Limitations

The result is specific to the binomial Frobenius family \(\lambda X+\mu X^{q^k}\). It does not assert a corresponding dichotomy for general linearized polynomials with three or more Frobenius terms, whose kernels may have larger dimension over proper subfields. The proof determines the only possible hull dimensions but does not replace the source's trace-isotropy criterion for deciding which singular parameters have hull dimension \(d\).

## References

1. Daniele Bartoli, Giovanni Giuseppe Grimaldi, and Pantelimon Stănică, *On the hull of linearized polynomial codes*, arXiv:2604.23097v1, first public version 2026-04-25; Advances in Mathematics of Communications, DOI 10.3934/amc.2026.101087.
2. Rudolf Lidl and Harald Niederreiter, *Finite Fields*, 2nd ed., Cambridge University Press, 1997.
