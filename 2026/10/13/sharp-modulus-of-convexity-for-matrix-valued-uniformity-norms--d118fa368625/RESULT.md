# Sharp modulus of convexity for matrix-valued uniformity norms
## Finding
Let \(G\) be a finite group, let \(N\ge2\), and let \(k\ge2\). Put \(q=2^k\), and equip the space of functions \(F:G\to M_N(\mathbb C)\) with the matrix-valued uniformity norm \(\|\cdot\|_{U^k(G)}\) used by Jamneshan and Ünal [1]. Write
\[
X_{G,N,k}=\bigl(M_N(\mathbb C)^G,\|\cdot\|_{U^k(G)}\bigr).
\]
With the usual modulus-of-convexity convention
\[
\delta_X(\varepsilon)=\inf\left\{1-\left\|\frac{x+y}{2}\right\|:\ \|x\|=\|y\|=1,\ \|x-y\|\ge\varepsilon\right\},
\]
the exact modulus is
\[
\boxed{
\delta_{X_{G,N,k}}(\varepsilon)
=1-\left(1-\left(\frac{\varepsilon}2\right)^q\right)^{1/q},
\qquad 0<\varepsilon\le2.
}
\]
In particular, the lower bound proved in Corollary 4.2 of [1] is sharp for every finite \(G\), every \(N\ge2\), and every \(k\ge2\). No geometry of \(G\) is needed to attain equality: constant matrix-valued functions already do so.

## Assumptions and scope
The norm and normalized matrix trace are exactly those of [1]. The proof uses only the defining iterated multiplicative derivatives and the source's Hanner inequality. The matrix size restriction \(N\ge2\) is needed only to place the two-coordinate extremizing diagonal matrices. This includes the quantum-information setting of [1], where \(N=p^n\) with \(p\) prime and \(n\ge1\).

The statement is about the full matrix-valued space \(X_{G,N,k}\). Although [1] obtains quantum uniformity norms by restricting along the Weyl-orbit embedding, the present proof does not show that the quantum subspace has the same exact modulus.

## Proof
For a constant function \(F_A(x)=A\), the first multiplicative derivative is constant:
\[
(\Delta_hF_A)(x)=AA^*.
\]
Applying another derivative squares this positive matrix, and induction gives
\[
(\Delta_{h_k}\cdots\Delta_{h_1}F_A)(x)
=(AA^*)^{2^{k-1}}.
\]
The defining average is therefore independent of \(x,h_1,\ldots,h_k\). Since [1] uses normalized trace, one obtains
\[
\|F_A\|_{U^k(G)}^{2^k}
=\frac1N\operatorname{Tr}(AA^*)^{2^{k-1}}
=\frac1N\operatorname{Tr}|A|^q.
\]
Thus the constant-function subspace is an isometric copy of the normalized Schatten \(q\)-class on \(M_N(\mathbb C)\).

Fix \(0<\varepsilon\le2\), and set
\[
b=\frac{\varepsilon}2,
\qquad
a=(1-b^q)^{1/q}.
\]
Define
\[
A_+=N^{1/q}\operatorname{diag}(a,b,0,\ldots,0),
\qquad
A_-=N^{1/q}\operatorname{diag}(a,-b,0,\ldots,0).
\]
The constant-function formula gives
\[
\|F_{A_+}\|_{U^k}^q
=\|F_{A_-}\|_{U^k}^q
=a^q+b^q=1.
\]
It also gives
\[
\|F_{A_+}-F_{A_-}\|_{U^k}=2b=\varepsilon,
\qquad
\left\|\frac{F_{A_+}+F_{A_-}}2\right\|_{U^k}=a.
\]
Hence
\[
\delta_{X_{G,N,k}}(\varepsilon)
\le1-a
=1-\left(1-\left(\frac{\varepsilon}2\right)^q\right)^{1/q}.
\]
Corollary 4.2 of [1], derived there from the \(q\)-Hanner inequality, proves the reverse inequality. Equality follows.

## Verification
The proof is algebraic and covers every finite \(G\), every \(N\ge2\), and every \(k\ge2\). The accompanying `artifacts/verify.py` checks the constant-function recursion exponent, the normalized Schatten formula, and the extremizing identities for representative matrix sizes, uniformity orders, and separations. Those finite checks are corroborative only; the infinite family is proved by the displayed identities and the source's all-parameter Hanner bound.

## Relationship to prior work
Jamneshan and Ünal [1] prove a \(q\)-Hanner inequality for matrix-valued uniformity norms and infer the lower bound
\[
\delta(\varepsilon)\ge1-\left(1-\left(\frac{\varepsilon}2\right)^q\right)^{1/q}.
\]
The inspected version states this as a lower bound and does not state sharpness or an exact modulus. The present result supplies a matching family of extremizers.

Hatami [2] develops the geometry of scalar hypergraph/Gowers-type norms, including Hanner inequalities and modulus-of-convexity considerations, and records the classical Schatten-class Hanner theory. Those results motivate the shape of the modulus but do not identify the exact modulus of the matrix-valued uniformity space introduced in the later work [1]. Jamneshan and Thom [3] develop matrix-valued Gowers norms and inverse theory; the inspected material establishes Gowers--Cauchy--Schwarz, monotonicity, and norm properties but does not give this sharp modulus statement.

The sharpness mechanism is specifically the isometric normalized Schatten \(q\)-subspace formed by constant functions. It shows that no improvement of the global modulus can come from the noncommutative cube structure or from the finite group.

## Limitations
The result does not classify all extremizing pairs. It does not determine the exact modulus of the Weyl-orbit quantum-uniformity subspace, which may have additional constraints. It also does not claim a new Hanner inequality for Schatten classes; that ingredient is classical. Originality is limited to the exact sharpness conclusion for the newly studied matrix-valued uniformity spaces, and very recent literature may still be incompletely indexed.

## References
1. A. Jamneshan and B. Ünal, *Quantum uniformity norms are pullbacks of matrix-valued uniformity norms*, arXiv:2606.16862v2 (v1 first public 2026-06-15), especially Theorem 4.1 and Corollary 4.2.
2. H. Hatami, *On generalizations of Gowers norms and their geometry*, arXiv:0903.3237; Israel J. Math. 175 (2010), 175--206.
3. A. Jamneshan and A. Thom, *Quadratic maps between non-abelian groups*, Math. Proc. Cambridge Philos. Soc. (2026), doi:10.1017/S0305004126101911.
