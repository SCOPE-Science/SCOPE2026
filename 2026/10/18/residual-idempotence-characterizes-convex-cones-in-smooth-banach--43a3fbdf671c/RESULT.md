# Residual idempotence characterizes convex cones in smooth Banach spaces

## Finding
Let \(X\) be a real Banach space whose norm is Gâteaux differentiable away from zero. Let \(K\subseteq X\) be a nonempty, closed, convex Chebyshev set (each \(x\in X\) admits a unique nearest point \(P_Kx\in K\)). Define the nonlinear residual map \(R=I-P_K\). Then
\[
R\circ R=R\quad\Longleftrightarrow\quad K\text{ is a convex cone with vertex }0.
\]
Here *cone* means \(tK\subseteq K\) for all real \(t\geq0\); pointedness and nonempty interior are not required. Thus the classification applies, for example, to every nonempty closed convex subset of any real uniformly convex, uniformly smooth Banach space, including \(\ell_p\) for \(1<p<\infty\), when a unique nearest point exists.

There is also an exact pointwise test. If \(0\in K\), set \(p=P_Kx\), \(r=x-p\), and let \(J:X\to X^*\) be the normalized duality map, \(J(v)=D(\|\cdot\|^2/2)(v)\) for \(v\ne0\) and \(J(0)=0\). Then
\[
P_K(r)=0\quad\Longleftrightarrow\quad \langle J(r),p\rangle=0.
\]
In particular, idempotence of \(I-P_K\) can be tested by a scalar duality pairing at every \(x\).

## Assumptions and scope
The space is real, not necessarily Hilbert, reflexive, strictly convex, or finite-dimensional. Smoothness means Gâteaux differentiability of the norm at every nonzero vector; this makes \(J\) single-valued. The Chebyshev hypothesis independently guarantees existence and uniqueness of the projection and is deliberately retained: these properties do not follow from smoothness alone. Convexity and closedness are assumed throughout. The zero set \(K=\{0\}\) and the whole space \(K=X\) are included, as are closed linear subspaces and non-pointed cones. Composition \(R\circ R\) refers to the nonlinear mapping, not multiplication of bounded linear operators.

## Proof
**Variational fact.** Given \(z\in X\) and \(q\in K\), the following are equivalent:
\[
q=P_Kz\quad\Longleftrightarrow\quad
\langle J(z-q),k-q\rangle\leq0\quad\text{for all }k\in K.\tag{1}
\]
Indeed, for fixed \(k\in K\), the convex differentiable function \(t\mapsto\frac12\|z-q-t(k-q)\|^2\) on \([0,1]\) has its minimum at \(t=0\) if \(q=P_Kz\); its right derivative is \(-\langle J(z-q),k-q\rangle\), proving necessity. Conversely, convexity of the squared norm and the subgradient inequality give
\[
\frac12\|z-k\|^2\geq\frac12\|z-q\|^2-\langle J(z-q),k-q\rangle\geq\frac12\|z-q\|^2.
\]
Hence \(q\) is the unique nearest point. The case \(z=q\) follows from \(J(0)=0\). No continuity of \(P_K\) is used.

**Pointwise criterion.** Suppose \(0\in K\), and write \(p=P_Kx\), \(r=x-p\). Applying (1) to \(x,p\) and \(k=0\) gives \(\langle J(r),p\rangle\geq0\). If \(P_Kr=0\), applying (1) to \(r,0\) at \(k=p\) gives \(\langle J(r),p\rangle\leq0\); equality follows. In the opposite direction, if this pairing is zero, (1) at \(x,p\) gives, for every \(k\in K\),
\[
\langle J(r),k\rangle\leq\langle J(r),p\rangle=0.
\]
As \(0\in K\), (1) at \(r,0\) gives \(P_Kr=0\). This proves the exact pointwise equivalence.

**Necessity of conicity.** Assume \(R\circ R=R\). Take any \(y\in K\). Since \(P_Ky=y\), we have \(Ry=0\), hence \(R0=R(Ry)=Ry=0\). Thus \(P_K0=0\) and \(0\in K\). We already know that \(K\) is convex, so \(ty\in K\) for \(0\leq t\leq1\). For any \(t>1\), write \(x=ty\), \(p=P_Kx\), \(r=ty-p\). Idempotence gives \(P_Kr=0\), so the pointwise criterion yields \(\langle J(r),p\rangle=0\). The variational inequality (1) at \(x,p\) with \(k=y\) yields \(\langle J(r),y\rangle\leq0\). Consequently,
\[
\|r\|^2=\langle J(r),r\rangle
=t\langle J(r),y\rangle-\langle J(r),p\rangle\leq0.
\]
Thus \(r=0\), so \(ty=p\in K\). This holds for every \(y\in K\) and every \(t>1\). Together with \(0\leq t\leq1\), it proves \(tK\subseteq K\) for all \(t\geq0\).

**Sufficiency of conicity.** Conversely, assume \(K\) is a nonempty convex cone. Then \(0\in K\). For arbitrary \(x\), put \(p=P_Kx\), \(r=x-p\). Both \(0\) and \(2p\) belong to \(K\). Apply (1) first with \(k=0\) and then with \(k=2p\):
\[
\langle J(r),p\rangle\geq0\quad\text{and}\quad
\langle J(r),p\rangle\leq0.
\]
Therefore the pairing vanishes and the pointwise criterion gives \(P_Kr=0\). Hence \(R(Rx)=r-P_Kr=r=Rx\) for every \(x\), establishing idempotence.

## Verification
The derivation uses only (i) the first-order variational inequality (1), derived directly from differentiability and convexity, (ii) the normalization \(\langle J(r),r\rangle=\|r\|^2\), and (iii) the inclusion \(0,p,2p\in K\) for cones. Necessity uses the test input \(x=ty\) for every \(y\in K\) and every real \(t>1\); thus no finite sample, bounded set of parameters, or numerical experiment substitutes for the global argument. Boundary cases \(r=0\), \(K=\{0\}\), and \(K=X\) satisfy the same proof.

## Relationship to prior work
Kumar, Bin Abu Baker, and Botelho (2026) introduce nonlinear bi-potent maps and study necessary conditions for idempotence of \(I-P_K\), without presenting this full cone-versus-idempotence equivalence in the smooth Chebyshev convex setting. Domokos and Marsh (2018), notably Proposition 1.9(c) and Proposition 1.12, establish the standard duality variational inequalities and projection properties for sets already known to be cones, under stronger geometric assumptions than those used here. Those inequalities are the explicitly acknowledged foundation of the argument; the converse classification is the proposed contribution. Németh (2026) treats polarity and order-theoretic features of already-conical projection sets. Hilbert-space cases are related to classical Moreau decomposition, so the statement is not presented as a new construction of Moreau decomposition.

## Limitations
The classification is **not** established here for arbitrary nonsmooth norms or nonconvex Chebyshev sets; neither assumption may silently be dropped. Smoothness alone does not imply that every closed convex set is Chebyshev. The statement characterizes exact, globally quantified residual idempotence only, not approximate idempotence, continuity, or Lipschitz bounds. Its elementary proof means that unnoticed coverage by general variational inequality, proximal-resolvent, or Moreau-type literature is a meaningful publication-priority risk. No independent audit or external certification is claimed.

## References
1. H. Kumar, A. Bin Abu Baker, and F. Botelho, *On Nonlinear Idempotents and Metric Projections in Normed Spaces*, arXiv:2607.14649v1 (first posted 2026-07-16), https://arxiv.org/abs/2607.14649.
2. A. Domokos and M. M. Marsh, *Projections onto cones in Banach spaces*, Fixed Point Theory 19 (2018), 167–178, https://webpages.csus.edu/mmarsh/domokos%26marsh-projections%20to%20cones.pdf.
3. S. Z. Németh, study of subdual cones (2026), arXiv:2608.21005, https://arxiv.org/abs/2608.21005.
4. *Dual and generalized dual cones in Banach spaces*, Optimization Letters (2024), https://link.springer.com/article/10.1007/s11590-024-02126-9 (duality-projection variational characterization).
