# Exact divisibility law for Ritt powers
## Finding
Let \(X\) be a complex Banach space and let \(T\in\mathcal B(X)\). Suppose that \(T^N\) is a Ritt operator for at least one integer \(N\ge1\). Define
\[
E=\sigma(T)\cap\mathbb T.
\]
If \(E=\varnothing\), put \(d=1\). Otherwise put
\[
d=\operatorname{lcm}\{\operatorname{ord}(\lambda):\lambda\in E\}.
\]
Then for every integer \(n\ge1\),
\[
T^n\text{ is Ritt}\quad\Longleftrightarrow\quad d\mid n.
\]
Consequently the Ritt exponents of \(T\) form the exact divisibility ray \(d\mathbb N_{\ge1}\). In particular, \(d\) is the unique least positive Ritt exponent, and if \(T^m\) and \(T^n\) are Ritt then \(T^{\gcd(m,n)}\) is Ritt.

## Assumptions and scope
The space is complex, \(T\) is bounded, and at least one positive power of \(T\) is Ritt. A Ritt operator is used in the standard power-bounded discrete-derivative sense: \(A\) is power bounded and
\[
\sup_{k\ge1} k\,\lVert A^k-A^{k-1}\rVert<\infty.
\]
This characterization is equivalent to the usual Ritt resolvent condition. No compactness, reflexivity, positivity, contractivity, or geometric assumption on \(X\) is required.

## Proof
Choose \(N\ge1\) such that \(T^N\) is Ritt. Since \(T^N\) is power bounded, \(T\) is power bounded: writing \(k=qN+r\) with \(0\le r<N\),
\[
\lVert T^k\rVert\le \Bigl(\max_{0\le r<N}\lVert T^r\rVert\Bigr)\sup_{q\ge0}\lVert (T^N)^q\rVert.
\]
Hence \(\sigma(T)\subseteq\overline{\mathbb D}\). If \(\lambda\in E\), spectral mapping gives \(\lambda^N\in\sigma(T^N)\cap\mathbb T\). A Ritt operator has no peripheral spectral point other than \(1\), so \(\lambda^N=1\). Thus \(E\) is a finite set of roots of unity and \(d\mid N\).

Necessity is immediate. If \(T^n\) is Ritt and \(\lambda\in E\), then \(\lambda^n\in\sigma(T^n)\cap\mathbb T=\{1\}\). Therefore every \(\operatorname{ord}(\lambda)\) divides \(n\), so \(d\mid n\).

For sufficiency, first prove that \(T^d\) is Ritt. Put \(S=T^d\) and \(a=N/d\). Then \(S\) is power bounded and \(S^a=T^N\) is Ritt. Moreover \(\sigma(S)\cap\mathbb T\subseteq\{1\}\): if \(\mu\in\sigma(S)\cap\mathbb T\), polynomial spectral mapping gives \(\mu=\lambda^d\) for some \(\lambda\in\sigma(T)\); since \(|\mu|=1\) and \(\sigma(T)\subseteq\overline{\mathbb D}\), necessarily \(\lambda\in E\), hence \(\lambda^d=1\).

Let
\[
Q_a(z)=1+z+\cdots+z^{a-1}.
\]
Its zeros are precisely the nontrivial \(a\)-th roots of unity, so none lies in \(\sigma(S)\). Hence \(Q_a(S)\) is invertible. Since
\[
I-S^a=(I-S)Q_a(S),
\]
we have
\[
I-S=(I-S^a)Q_a(S)^{-1}.
\]
Write \(n-1=aj+r\) with \(0\le r<a\). If \(M=\sup_{k\ge0}\lVert S^k\rVert\) and
\[
C=\sup_{j\ge0}(j+1)\,\lVert (S^a)^{j+1}-(S^a)^j\rVert,
\]
then
\[
\begin{aligned}
n\,\lVert S^{n-1}(I-S)\rVert
&\le n\,\lVert S^r\rVert\,\lVert (S^a)^j-(S^a)^{j+1}\rVert\,\lVert Q_a(S)^{-1}\rVert\\
&\le aMC\,\lVert Q_a(S)^{-1}\rVert,
\end{aligned}
\]
because \(n\le a(j+1)\). The discrete-derivative characterization therefore makes \(S=T^d\) Ritt.

Finally, every positive power of a Ritt operator is Ritt. Indeed, if \(A\) is Ritt and \(k\ge1\), then
\[
A^{kj}-A^{k(j-1)}=\sum_{r=0}^{k-1}A^{k(j-1)+r}(A-I),
\]
and the Ritt derivative bound for \(A\) gives a uniform bound for \(j\lVert (A^k)^j-(A^k)^{j-1}\rVert\). Thus, whenever \(d\mid n\), the operator \(T^n\) is a positive power of the Ritt operator \(T^d\), and is itself Ritt.

## Verification
The proof uses only spectral mapping, elementary polynomial functional calculus, and the standard power-bounded discrete-derivative characterization of Ritt operators. The key root step was checked at the level of the actual polynomial \(Q_a\): all of its zeros lie on \(\mathbb T\setminus\{1\}\), while \(\sigma(T^d)\cap\mathbb T\subseteq\{1\}\), so \(Q_a(T^d)\) is invertible. The empty-peripheral-spectrum case is included by the convention \(d=1\).

## Relationship to prior work
Badea's 2026 paper proves that displacement bounds can force a finite peripheral spectrum of roots of unity and that an explicitly chosen universal power is Ritt; in the uniformly convex setting it also characterizes existence of odd Ritt powers. The present statement is different: once any Ritt power exists for a fixed operator, it classifies every Ritt exponent exactly and identifies the operator-specific minimum from the peripheral spectrum. Bouabdillah and Le Merdy's finite-peripheral-spectrum theory supplies the broader Ritt\(_E\) framework and the standard discrete-derivative characterization, but the inspected theorem statements do not give this divisibility classification.

## Limitations
The result assumes existence of at least one Ritt power and does not supply a criterion for that existence. It is stated for complex Banach spaces, because the proof uses the complex spectrum. The argument gives an explicit bound involving \(\lVert Q_a(T^d)^{-1}\rVert\), but it does not optimize quantitative Ritt constants. A residual literature risk remains that the same fixed-operator divisibility classification may have appeared under older power-root or finite-peripheral-spectrum terminology.

## References
1. C. Badea, *Iterates of Ritt operators close to the identity*, arXiv:2609.27458v1 (2026).
2. O. Bouabdillah and C. Le Merdy, *Polygonal functional calculus for operators with finite peripheral spectrum*, arXiv:2203.05373v2; DOI 10.1007/s11856-024-2632-y.
