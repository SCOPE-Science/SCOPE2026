# Exact finite-field census of Heisenberg Rota–Baxter operators

## Finding

Let
\[
H_3(\mathbf F_q)=\langle c,e,f:[e,f]=c\rangle
\]
be the three-dimensional Heisenberg Lie algebra over the finite field \(\mathbf F_q\). A linear operator \(R\) has weight \(\lambda\) when
\[
[R(x),R(y)]+\lambda R([x,y])
=R([R(x),y]+[x,R(y)]).
\]

Every such operator has the form
\[
R=
\begin{pmatrix}
x&\alpha&\beta\\
0&y&u\\
0&v&z
\end{pmatrix}
\]
in the ordered basis \((c,e,f)\), and the seven parameters satisfy the single equation
\[
\boxed{(y-x)z=xy-\lambda x+uv.}
\]

Therefore
\[
\boxed{\#\operatorname{RB}_0(H_3(\mathbf F_q))=q^6}
\]
and, for every \(\lambda\ne0\),
\[
\boxed{\#\operatorname{RB}_\lambda(H_3(\mathbf F_q))=q^6+q^4.}
\]

On the Rota–Baxter hypersurface,
\[
\det R=x^2(y+z-\lambda).
\]
Hence the exact invertible counts are
\[
\boxed{q^3(q-1)(q^2-q-1)}
\]
for weight zero and
\[
\boxed{q^3(q^3-2q^2+2)}
\]
for every nonzero weight.

Thus changing from weight zero to a nonzero weight creates exactly \(q^4\) additional finite-field points. Invertible Rota–Baxter operators exist over every finite field at every weight.

## Assumptions and scope

The count is for linear Rota–Baxter operators on the three-dimensional Heisenberg Lie algebra, not modulo Lie-algebra automorphisms.

The formulas hold for every prime power \(q\), including characteristic two. No algebraic-closedness assumption is needed.

For nonzero weight, all weights have the same count because scaling \(R\mapsto \lambda^{-1}R\) is a bijection from weight \(\lambda\) operators to weight one operators, and it preserves invertibility.

## Proof

Write
\[
R(c)=x c+p e+r f,
\quad
R(e)=\alpha c+y e+v f,
\quad
R(f)=\beta c+u e+z f.
\]
Apply the Rota–Baxter identity first to \((c,e)\). Comparing the \(f\)-coordinate gives \(r^2=0\), hence \(r=0\). Applying it to \((c,f)\) then gives \(p^2=0\), hence \(p=0\). Thus \(R(c)=xc\).

For \((e,f)\), the central coordinate is
\[
yz-uv+\lambda x=x(y+z),
\]
which is equivalent to
\[
(y-x)z=xy-\lambda x+uv.
\]
The central parameters \(\alpha,\beta\) are free.

We first count the five parameters \((x,y,u,v,z)\). If \(y\ne x\), then \(z\) is uniquely determined, giving
\[
q(q-1)q^2=q^3(q-1)
\]
solutions.

If \(y=x\), the equation is
\[
uv=x(\lambda-x),
\]
and \(z\) is free. The number of pairs \((u,v)\) with \(uv=t\) is \(2q-1\) when \(t=0\) and \(q-1\) when \(t\ne0\).

For \(\lambda=0\), the sum over \(x\) is
\[
(2q-1)+(q-1)^2=q^2.
\]
Thus the diagonal slice contributes \(q^3\), the five-parameter total is \(q^4\), and the free \((\alpha,\beta)\) multiply this by \(q^2\), giving \(q^6\).

For \(\lambda\ne0\), exactly \(x=0,\lambda\) give zero product. Hence
\[
2(2q-1)+(q-2)(q-1)=q^2+q.
\]
The diagonal slice contributes \(q^3+q^2\), so the five-parameter total is \(q^4+q^2\), and the full count is \(q^6+q^4\).

For invertibility, eliminate \(uv\) using the defining equation:
\[
yz-uv=x(z+y-\lambda).
\]
Therefore
\[
\det R=x(yz-uv)=x^2(y+z-\lambda).
\]

At weight zero, fix \(x\ne0\) and require \(y+z\ne0\). Put
\[
r=yz-x(y+z).
\]
Among the \(q(q-1)\) pairs \((y,z)\) with \(y+z\ne0\), exactly \(q-2\) have \(r=0\): after writing \(Y=y-x\), \(Z=z-x\), the equation \(r=0\) is \(YZ=x^2\), and the unique pair with \(y+z=0\) is \(Y=Z=-x\). Thus for each nonzero \(x\), the number of \((y,z,u,v)\) is
\[
(q-2)(2q-1)+(q(q-1)-(q-2))(q-1)
=q(q^2-q-1).
\]
Multiplying by \(q-1\) choices of \(x\) and by the free \(q^2\) central parameters gives
\[
q^3(q-1)(q^2-q-1).
\]

For nonzero weight it is enough to take \(\lambda=1\). Fix \(x\ne0\) and require \(y+z\ne1\). The zero-product equation becomes
\[
(y-x)(z-x)=x(x-1).
\]
For \(x=1\), there are \(2q-3\) zero-product pairs with \(y+z\ne1\); for \(x\ne0,1\), there are \(q-3\). Weighting zero products by \(2q-1\) choices of \((u,v)\), nonzero products by \(q-1\), and summing over \(x\ne0\) yields
\[
q(q^3-2q^2+2)
\]
solutions in \((x,y,z,u,v)\). The free central parameters contribute \(q^2\), giving
\[
q^3(q^3-2q^2+2).
\]

## Verification

The included checker performs two independent tests.

For \(q=2,3\), it exhaustively enumerates all \(q^9\) linear maps and tests the Rota–Baxter identity directly on basis pairs for weights zero and one.

For \(q=2,3,5,7\), it enumerates the reduced seven-parameter hypersurface, checks every generated operator directly against the Rota–Baxter identity, and verifies both total and invertible formulas.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the formulas for arbitrary prime powers.

## Relationship to prior work

Ji and Hua classify weight-zero and weight-one Rota–Baxter operators on the three-dimensional Heisenberg Lie algebra over an algebraically closed field. Their proof reduces the operator identity to the same centrality conditions and one scalar equation used above. They do not count finite-field points or isolate the invertible locus.

Zhu and Wu independently study the classical Yang–Baxter, equivalently weight-zero Rota–Baxter, equation on the same Heisenberg algebra using a basis with the central vector last. Their equation is the transposed-coordinate version of the same hypersurface. Their paper lists solution families but does not give finite-field counts.

Focused searches under Heisenberg, finite field, Rota–Baxter, Yang–Baxter, invertible, census, and point-count formulations did not locate the formulas above.

## Limitations

The result counts operators, not automorphism-conjugacy classes.

The exact formulas are special to the three-dimensional Heisenberg algebra; no higher-dimensional Heisenberg count is claimed.

The classification equations are elementary once the basis is fixed, so an equivalent finite-field census may exist under different terminology.

Failed searches do not prove novelty.

## References

1. G. Ji and X. Hua, “Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra,” *Korean Journal of Mathematics* 26 (2018), 53–60, published 30 March 2018, DOI 10.11568/kjm.2018.26.1.53. MSC 2010: 17B05, 17B65.
2. K. X. Zhu and M. Z. Wu, “The Classical Yang-Baxter Operator on the Heisenberg Lie Algebra and Its Applications,” *Pure Mathematical Sciences* 7 (2018), 45–52, DOI 10.12988/pms.2018.81012.
