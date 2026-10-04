# A minimal characteristic-two obstruction to Lie closure of algebraic reflexive hulls
## Finding
Let \(k\) be any field of characteristic \(2\), let \(V=k^2\), and define
\[
E=\left\{M(s,t)=\begin{pmatrix}s+t&s\\ t&s\end{pmatrix}:s,t\in k\right\}\subseteq \operatorname{End}_k(V).
\]
Then \(E\) is a two-dimensional Lie subalgebra under the commutator, while
\[
\operatorname{Ref}_a(E)=\left\{\begin{pmatrix}a&b\\ c&b\end{pmatrix}:a,b,c\in k\right\}
\]
is not a Lie subalgebra. Thus Lie closure of algebraic reflexive hulls, proved recently over \(\mathbb C\), is not a characteristic-free phenomenon. Dimension \(2\) is minimal for such a counterexample.

## Assumptions and scope
The field \(k\) is arbitrary subject only to \(\operatorname{char}k=2\). The algebraic reflexive hull of a linear subspace \(F\subseteq\operatorname{End}_k(V)\) is
\[
\operatorname{Ref}_a(F)=\{T\in\operatorname{End}_k(V):T(v)\in F(v)\text{ for every }v\in V\},
\]
where \(F(v)=\{S(v):S\in F\}\). No finiteness or algebraic-closedness assumption on \(k\) is used.

## Proof
Write
\[
B=M(1,0)=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
C=M(0,1)=\begin{pmatrix}1&0\\1&0\end{pmatrix}.
\]
Then \(E=kB+kC\). In characteristic \(2\), direct multiplication gives \([B,C]=B\), while \([B,B]=[C,C]=0\). Bilinearity of the commutator therefore shows \([E,E]\subseteq E\), so \(E\) is a Lie subalgebra.

It remains to compute the reflexive hull. For \(v=(x,y)^{\mathsf T}\),
\[
M(s,t)v=\begin{pmatrix}s(x+y)+tx\\ sy+tx\end{pmatrix}.
\]
As a linear map from the parameter pair \((s,t)\) to \(E(v)\), its coefficient matrix is
\[
\begin{pmatrix}x+y&x\\ y&x\end{pmatrix},
\]
whose determinant is \(x^2\). Hence, whenever \(x\ne0\), one has \(E(v)=k^2\), so the reflexivity condition imposes no restriction at that vector. When \(x=0\) and \(y\ne0\), one has
\[
E(v)=k(1,1)^{\mathsf T}.
\]
Therefore a matrix \(T=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) lies in \(\operatorname{Ref}_a(E)\) exactly when \(T(0,1)^{\mathsf T}=(b,d)^{\mathsf T}\) lies on that diagonal line, equivalently \(b=d\). This proves the displayed formula for \(\operatorname{Ref}_a(E)\).

Finally, the two matrices
\[
X=\begin{pmatrix}0&1\\0&1\end{pmatrix},\qquad
Y=\begin{pmatrix}0&0\\1&0\end{pmatrix}
\]
belong to \(\operatorname{Ref}_a(E)\), but
\[
[X,Y]=\begin{pmatrix}1&0\\1&1\end{pmatrix}
\]
does not, because its upper-right and lower-right entries are different. Thus \(\operatorname{Ref}_a(E)\) is not Lie closed.

For \(\dim_kV=1\), every commutator in \(\operatorname{End}_k(V)\) is zero, so every linear subspace and every algebraic reflexive hull is automatically a Lie subalgebra. Therefore dimension \(2\) is minimal.

## Verification
Every step is symbolic. Lie closure of \(E\) reduces to the single basis commutator \([B,C]=B\). The reflexive-hull computation reduces to the determinant \(x^2\) and the single exceptional projective direction \(x=0\). The two displayed hull elements give an explicit failed commutator. No finite enumeration is used in the proof.

## Relationship to prior work
Hao and Chen prove over finite-dimensional complex vector spaces that if \(E\subseteq\operatorname{End}(V)\) is a Lie subalgebra, then \(\operatorname{Ref}_a(E)\) is also a Lie subalgebra. Their argument passes through matrix exponentials and differentiation of conjugation curves, and the paper explicitly sets its ambient field to \(\mathbb C\). The example above shows that the statement itself cannot simply be transferred to arbitrary characteristic: characteristic \(2\) fails already in dimension \(2\).

Searches for the same two-dimensional family, the same hull equation, and characteristic-two failures of Lie closure did not locate an equivalent published statement. The nearest material concerns algebraic reflexivity in characteristic zero or unrelated characteristic-two exceptions.

## Limitations
The result is a boundary theorem for the general reflexive-hull statement. It does not assert that local derivations of a specific algebra fail to form a Lie algebra in characteristic \(2\), because the displayed subalgebra \(E\) is not identified here as the full derivation algebra of an algebra. No claim is made about odd positive characteristic.

## References
1. Z. Hao and L. Chen, “Local derivations is a Lie algebra,” arXiv:2609.09198v1, 2026. In particular, Definition 2.1, Lemma 2.6, and Theorem 2.7.
