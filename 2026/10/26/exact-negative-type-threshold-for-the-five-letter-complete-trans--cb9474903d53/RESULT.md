# Exact negative-type threshold for the five-letter complete transposition metric

## Finding

Let \(G=S_5\), and give it the canonical all-transposition Cayley distance
\[
 d(\sigma,\tau)=5-c(\sigma^{-1}\tau),
\]
where \(c(g)\) counts cycles of \(g\), including fixed points. There is a unique \(p_*\in(0,8/25)\) satisfying
\[
 -10+35\,2^{p_*}-50\,3^{p_*}+24\,4^{p_*}=0,
 \qquad p_*=0.3131601640555839044\ldots .
\]
For **every real \(p>0\)**, the powered distance \(d^p\) is conditionally negative semidefinite if and only if \(0<p\le p_*\). The conditional inequality is strict for every \(0<p<p_*\). At \(p=p_*\), the real zero-sum nullspace is exactly the one-dimensional sign-character direction.

Consequently, the smallest dimension of a real Euclidean space into which the \(120\) permutations embed with **squared distances equal to \(d^p\)** is \(119\) for \(0<p<p_*\) and \(118\) for \(p=p_*\). The kernels \(K_{t,p}(\sigma,\tau)=\exp[-t d(\sigma,\tau)^p]\) are positive semidefinite for *every* \(t>0\) exactly when \(0<p\le p_*\), and they are strictly positive definite at every such \(t\). For \(p>p_*\), they fail positive semidefiniteness for all sufficiently small positive \(t\) but are strictly positive definite for sufficiently large \(t\).

## Assumptions and scope

This is the finite group of all permutations of five labels and **all ten transpositions** as generators, not the adjacent-transposition (Kendall) metric, Hamming metric, or principal-rotation-angle metric. The domain of \(p\) is \((0,\infty)\). Conditional negative semidefiniteness means that for every real vector \((a_g)_{g\in G}\) with \(\sum_g a_g=0\),
\[
 \sum_{g,h\in G}a_ga_h\,d(g,h)^p\le0.
\]
Euclidean embeddings use the distance convention \(\|v_g-v_h\|^2=d(g,h)^p\), without any unstated normalization.

## Proof

**1. Metric and central Fourier reduction.** A transposition changes the number of cycles by exactly one, and a permutation with \(c(g)\) cycles can be written as exactly \(5-c(g)\) transpositions, giving the asserted Cayley distance. For each real \(p>0\), let \(D_p\) be the \(120\)-by-\(120\) matrix with entries \(d(g,h)^p\). The function \(g\mapsto(5-c(g))^p\) is constant on conjugacy classes, so Schur's lemma decomposes \(D_p\) into irreducible blocks. The scalar on the block indexed by partition \(\lambda\vdash5\) is
\[
 \theta_\lambda(p)=\frac{1}{\dim V_\lambda}\sum_{g\in S_5}(5-c(g))^p\chi_\lambda(g).
\]
In the regular representation this scalar appears \((\dim V_\lambda)^2\) times. The zero-sum subspace consists of all blocks except the trivial representation, so conditional negativity is equivalent to nonpositivity of all six nontrivial scalars.

The conjugacy classes at distances \(0,1,2,3,4\) have sizes \(1,10,35,50,24\). More precisely, the cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\) have sizes \(1,10,15,20,20,30,24\). Their irreducible characters follow from the standard representation \(V\) with \(\chi_V(g)=\#\operatorname{Fix}(g)-1\); the two-subset permutation character \(\chi_{\mathrm{pairs}}\) with \(\chi_{(3,2)}=\chi_{\mathrm{pairs}}-1-\chi_V\); the exterior square \(\chi_{(3,1,1)}(g)=(\chi_V(g)^2-\chi_V(g^2))/2\); and sign twists for the conjugate partitions. Substitution yields the **complete nontrivial multiplier list**, with \(a=2^p\) and \(b=3^p\):
\[
\begin{aligned}
\theta_{(4,1)}&=5+5a-5b-6a^2,\\
\theta_{(3,2)}&=2-a-2b,\\
\theta_{(3,1,1)}&=-5a+4a^2,\\
\theta_{(2,2,1)}&=-2-a+2b,\\
\theta_{(2,1,1,1)}&=-5+5a+5b-6a^2,\\
\theta_{(1^5)}&=-10+35a-50b+24a^2.
\end{aligned}
\]
Their dimensions are respectively \(4,5,6,5,4,1\). In particular the last multiplier is the quadratic form in the sign-character vector divided by \(120\).

**2. Uniqueness and location of the sign obstruction.** Let
\[
 F(p)=-10+35\,2^p-50\,3^p+24\,4^p.
\]
Write \(L=\log2\), \(H=\log(3/2)\), and \(M=\log3=L+H\). Then
\[
 F'(p)=2^p g(p),\qquad
 g(p)=35L+48L\,2^p-50M(3/2)^p.
\]
Direct differentiation gives
\[
 g''(p)=48L^3\,2^p-50MH^2(3/2)^p.
\]
For \(p\ge0\), \(2^p\ge(3/2)^p\) and \(48L^3>50MH^2\), so \(g''(p)>0\). Also \(g'(0)=48L^2-50MH>0\) and \(g(0)=83L-50M>0\). All three logarithmic comparisons are certified by the elementary convergent series
\[
 \log x=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,\quad
 z=\frac{x-1}{x+1},\quad
 0<R_N<\frac{2z^{2N+1}}{(2N+1)(1-z^2)}
\]
with \(N=12\) for \(x\in\{2,3,3/2\}\), using rational arithmetic. Therefore \(F'(p)>0\) for every \(p\ge0\). As \(F(0)=-1\) and \(F(8/25)>0\), there is exactly one positive zero, lying in \((0,8/25)\). The positive endpoint sign is certified using rational lower and upper bounds for \(2^{8/25},3^{8/25},4^{8/25}\): each bound is obtained from an exact integer comparison of its twenty-fifth power with the appropriate eighth power. The accompanying checker reproduces this certificate without floating-point decisions. It also verifies \(2^{8/25}<5/4\) using integers alone.

**3. The other irreducible blocks at and below the root.** For \(0<p\le p_*<8/25<1/3\), one has \(1<a<5/4\), \(a\le b\le a^2\), and \(b<3^{1/3}<3/2\). Consequently,
\[
\begin{aligned}
\theta_{(4,1)}&\le5-6a^2<0,\\
\theta_{(3,2)}&<0,\\
\theta_{(3,1,1)}&=a(4a-5)<0,\\
\theta_{(2,2,1)}&<-2-1+3=0,\\
\theta_{(2,1,1,1)}&\le-5+5a-a^2<0.
\end{aligned}
\]
For the last strict inequality the concave quadratic is increasing on \([1,5/4]\), with value \(-5/16\) at \(5/4\). The sign scalar \(F(p)\) is negative for \(0<p<p_*\) and zero at \(p_*\), so all asserted conditional-negative-type statements follow. For \(p>p_*\) the sign scalar is strictly positive, giving a concrete obstruction to conditional negative semidefiniteness.

**4. Dimension and covariance.** The centered Gram matrix \(-\tfrac12 JD_pJ\), where \(J=I-\mathbf1\mathbf1^{\mathsf T}/120\), is positive semidefinite exactly in the established range. Its rank is the number of negative eigenvalues of \(D_p\) on the zero-sum subspace. This is \(119\) below \(p_*\) and \(118\) at \(p_*\), since the sign representation has dimension one and all other nontrivial blocks stay strictly negative. This Gram matrix realizes the minimum Euclidean embedding dimension. Schoenberg's exponential criterion gives the every-bandwidth covariance equivalence. Distinct permutations have positive distance, so the induced Hilbert embedding is injective; the Gaussian of injective Euclidean points is strictly positive definite. For \(p>p_*\), the sign Fourier scalar of \(e^{-tD_p}\) equals \(-tF(p)+O(t^2)<0\) as \(t\downarrow0\). For sufficiently large \(t\), all off-diagonal entries are bounded by \(e^{-t}\), so \(119e^{-t}<1\) proves strict diagonal dominance and positive definiteness.

## Verification

Running the included `check.py` with Python 3 (and `mpmath` for supplementary high-precision endpoint evaluations) reproduces: enumeration of all \(120\) group elements; all seven conjugacy-class sizes; the six complete Fourier multipliers via independent permutation-character formulas; exact character orthogonality; the all-rational twenty-fifth-root test \(F(8/25)>0\); the exact logarithm-series inequalities needed for strict monotonicity; and numerical endpoint values. The universal inequalities are proved above; the numerical endpoint computation is corroboration, not the proof.

## Relationship to prior work

Sánchez, *On the supremal p-negative type of a finite metric space* (arXiv:1108.0451v1, 2011), gives a general criterion via distance matrices and the interval property, including complete bipartite examples. Ganesan, *Automorphism group of the complete transposition graph* (arXiv:1404.7363v1, 2014), studies this precise family of Cayley graphs, proving automorphism results rather than the present powered-distance Fourier threshold. Lafont and Prassidis, *Roundness properties of groups* (arXiv:math/0412219v1, 2004), study group and Cayley-graph roundness generally, without the \(S_5\) all-transposition exponent or endpoint rank statement in the inspected text. The present exact spectral classification is not implied by those stated results alone. This is a bounded literature comparison, not a claim of exhaustive priority.

## Limitations

The classification is for \(S_5\) with all transpositions, **not** every \(S_n\), every permutation metric, or individual admissible bandwidths when \(p>p_*\). It does not assert a stable quantitative embedding distortion, a closed algebraic expression for \(p_*\), or uniqueness against unindexed literature. The available literature inspection is bounded. Independent validation has not been performed.

## References

1. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (public 2011-08-02), https://arxiv.org/abs/1108.0451.
2. A. Ganesan, *Automorphism group of the complete transposition graph*, arXiv:1404.7363v1 (public 2014-04-27), https://arxiv.org/abs/1404.7363.
3. J.-F. Lafont and S. Prassidis, *Roundness properties of groups*, arXiv:math/0412219v1 (public 2004-12-10), https://arxiv.org/abs/math/0412219.
