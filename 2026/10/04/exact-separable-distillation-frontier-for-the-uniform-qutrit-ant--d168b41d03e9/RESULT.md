# Exact separable-distillation frontier for the uniform qutrit antisymmetric state
## Finding
Let \(F\) be the swap operator on \(\mathbb C^3\otimes\mathbb C^3\), let \(P_-=(I-F)/2\), and put \(\tau_-=P_-/3\). For
\[
|\psi_\theta\rangle=\cos\theta\,|00\rangle+\sin\theta\,|11\rangle,
\qquad 0<\theta\le \pi/4,
\]
the largest probability of an exact one-copy conversion \(\tau_-\mapsto |\psi_\theta\rangle\langle\psi_\theta|\) by a bipartite separable instrument is
\[
p_{\mathrm{SEP}}(\theta)=\min\!\left\{1,\frac{1}{2\sin(2\theta)}\right\}.
\]
In particular, the symmetric antisymmetric-qutrit benchmark of Akibue, Miyazaki and Osaka has a closed-form optimum: their displayed achievable curve is exact, not merely numerically tight.

## Assumptions and scope
A separable instrument here means a collection of completely positive branches with product Kraus operators, including a failure branch, whose sum is trace preserving. The success branch is required to output exactly the pure target whenever it occurs. The statement concerns one copy of \(\tau_-\) and \(0<\theta\le\pi/4\); it does not assert an LOCC optimum, a PPT-preserving optimum, an asymptotic rate, or an approximate-conversion result.

For the benchmark in the motivating paper, \(\theta_1=\theta_2=\theta_3=\pi\) and \(q_1=q_2=q_3=1/3\). Its three source vectors are then the orthonormal antisymmetric basis vectors, so their mixture is exactly \(\tau_-=P_-/3\).

## Proof
Write \(c=\cos\theta\), \(s=\sin\theta\), and \(C=\sin(2\theta)=2cs\).

Consider a success product Kraus operator \(K=A\otimes B\), with \(A,B:\mathbb C^3\to\mathbb C^2\). Because the total success output is rank one and positive, every nonzero success branch maps the entire antisymmetric support into the target line. A contributing branch must therefore have \(\operatorname{rank}A=\operatorname{rank}B=2\). Moreover its one-dimensional kernels coincide. Indeed, if \(u\in\ker A\) but \(Bu\ne0\), choose \(v\) with \(Av\ne0\). Then
\[
(A\otimes B)\frac{|u\rangle|v\rangle-|v\rangle|u\rangle}{\sqrt2}
=-\frac{Av\otimes Bu}{\sqrt2},
\]
a nonzero product vector, which cannot lie in the entangled target line. Thus \(u\in\ker B\), and symmetry gives equality of the kernels.

Let \(P\) be the common two-dimensional support plane and let \(|a\rangle\) be its normalized antisymmetric vector. Then \(K\) annihilates the two antisymmetric directions involving the common kernel, while
\[
K|a\rangle=\alpha|\psi_\theta\rangle
\]
for some scalar \(\alpha\). Put \(X=A^\dagger A\) and \(Y=B^\dagger B\), restricted to \(P\). In an orthonormal basis of \(P\), \(|a\rangle\) has coefficient matrix \(J/\sqrt2\), where
\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Hence
\[
\frac1{\sqrt2}AJB^T=\alpha\begin{pmatrix}c&0\\0&s\end{pmatrix}.
\]
Two consequences are needed. First,
\[
|\alpha|^2=\langle a|X\otimes Y|a\rangle
=\frac12\left(\operatorname{Tr}X\,\operatorname{Tr}Y-\operatorname{Tr}(XY)\right).
\]
Second, Schatten Hölder gives
\[
\|AJB^T\|_1\le \|A\|_2\|B\|_2,
\]
so
\[
\operatorname{Tr}X\,\operatorname{Tr}Y
\ge 2|\alpha|^2(c+s)^2.
\]
Combining the two identities yields the branch inequality
\[
\operatorname{Tr}(XY)\ge 2C|\alpha|^2.
\]

Now sum over all success branches. Their effect is \(E=\sum_\ell X_\ell\otimes Y_\ell\). Since the failure branch of the full instrument is separable, \(R=I-E\) is a separable positive operator. The swap \(F\) is block-positive because
\[
\langle x\otimes y|F|x\otimes y\rangle=|\langle x|y\rangle|^2\ge0.
\]
Therefore \(\operatorname{Tr}(FR)\ge0\), and because \(\operatorname{Tr}F=3\),
\[
3\ge\operatorname{Tr}(FE)=\sum_\ell\operatorname{Tr}(X_\ell Y_\ell)
\ge2C\sum_\ell|\alpha_\ell|^2.
\]
On \(\tau_-=P_-/3\), branch \(\ell\) succeeds with probability \(|\alpha_\ell|^2/3\), so \(p=(1/3)\sum_\ell|\alpha_\ell|^2\). Thus
\[
p\le\frac1{2C}=\frac1{2\sin(2\theta)}.
\]
Together with \(p\le1\), this is the desired upper bound.

For completeness, the matching instrument can be written explicitly. Set
\[
p=\min\!\left\{1,\frac1{2C}\right\},\qquad \alpha=\sqrt{p/2}.
\]
For each ordered pair of distinct input labels \(i,j\in\{0,1,2\}\), define product Kraus operators by
\[
A_{ij}=\sqrt c\,|0\rangle\langle i|+\sqrt s\,|1\rangle\langle j|,
\]
\[
B_{ij}=\sqrt2\,\alpha\left(\sqrt c\,|0\rangle\langle j|-\sqrt s\,|1\rangle\langle i|\right).
\]
For \(|a_{ij}\rangle=(|ij\rangle-|ji\rangle)/\sqrt2\),
\[
(A_{ij}\otimes B_{ij})|a_{ij}\rangle=\alpha|\psi_\theta\rangle,
\]
and the branch annihilates the other two antisymmetric basis directions. Summing the six success effects gives the diagonal operator
\[
E=2pC\sum_i|ii\rangle\langle ii|+p\sum_{i\ne j}|ij\rangle\langle ij|.
\]
If \(C\ge1/2\), then \(p=1/(2C)\); if \(C\le1/2\), then \(p=1\). In both cases every diagonal coefficient of \(E\) is at most one, so \(I-E\) is a nonnegative diagonal sum of product projectors and is therefore a valid separable failure effect. The six success branches have total success probability \(p\), proving achievability.

## Verification
The proof was checked at the level of branch ranges, kernel dimensions, normalization, and the trace pairing with the swap witness. The explicit six-branch construction independently reproduces the achievable curve and verifies trace preservation by a separable diagonal failure effect. No finite sampling, numerical optimization, or unproved computational certificate is used for the universal claim.

Boundary checks agree with the formula: at \(\theta=\pi/4\), the optimum is \(1/2\); at \(\sin(2\theta)=1/2\), the two branches of the formula meet at probability one; and as \(\theta\downarrow0\), the optimum tends to one. The theorem itself keeps \(\theta>0\), so every target in the proof has Schmidt rank two.

## Relationship to prior work
Akibue, Miyazaki and Osaka construct a separable protocol with success probability \(\min\{1,1/(2\sin(2\theta))\}\) for a broader three-state family. For the symmetric parameters \(\theta_i=\pi\) and \(q_i=1/3\), they report that their numerical hierarchy indicates this protocol is optimal. The present result supplies the missing analytic upper bound for exactly that benchmark.

Chitambar and Duan proved deterministic separable distillation for a different \(3\otimes3\) rank-two mixture and a fixed pure target. Their construction motivates later protocols but does not imply the probability frontier for the rank-three uniform antisymmetric state. General PPT-distillation results concern a strictly larger operation class and likewise do not imply this exact separable-instrument optimum.

## Limitations
The result is specific to the uniform antisymmetric qutrit state and exact one-copy separable instruments. The upper bound uses separability of the failure effect; it should not be read as a bound for an isolated trace-nonincreasing success map with an unrestricted completion. No claim is made about LOCC attainability, multiple copies, catalysts, approximate targets, or the nonuniform and non-antisymmetric parameter choices of the broader source family.

## References
1. S. Akibue, J. Miyazaki, and H. Osaka, “Optimizing Entanglement Manipulation via Algebraic-Geometric Decompositions and Semidefinite Programming Hierarchies,” arXiv:2501.17394; Letters in Mathematical Physics 116, 110 (2026), DOI 10.1007/s11005-026-02138-9.
2. E. Chitambar and R. Duan, “Nonlocal Entanglement Transformations Achievable by Separable Operations,” arXiv:0811.3739; Physical Review Letters 103, 110502 (2009), DOI 10.1103/PhysRevLett.103.110502.
