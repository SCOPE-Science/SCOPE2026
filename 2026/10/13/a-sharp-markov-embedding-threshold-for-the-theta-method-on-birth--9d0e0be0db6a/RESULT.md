# A sharp Markov-embedding threshold for the \(\theta\)-method on birth–death chains

## Finding

Let \(n\ge2\), and let \(Q\) be the row generator of a finite irreducible birth–death chain on the ordered states \(1,\ldots,n\): \(Q_{i,i+1}>0\) and \(Q_{i+1,i}>0\) whenever these entries exist, all other off-diagonal entries are zero, and \(Q\mathbf1=0\). For \(\theta\ge0\) and \(h>0\), define the one-step rational transition approximation
\[
P_{\theta,h}=(I-\theta hQ)^{-1}(I+(1-\theta)hQ).
\]
A real matrix \(P\) is *Markov-embeddable* if \(P=\exp B\) for some finite-state continuous-time Markov generator \(B\) (nonnegative off-diagonal entries, zero row sums). The following classification holds.

**Theorem (sharp dimension and implicitness thresholds).** If \(n\ge3\):

1. For every \(0\le\theta\le\frac12\) and **every** \(h>0\), \(P_{\theta,h}\) is not Markov-embeddable. When \(0<\theta\le\frac12\), the matrix nevertheless is strictly positive and stochastic for all sufficiently small positive \(h\).
2. For each \(\theta>\frac12\), \(P_{\theta,h}\) is Markov-embeddable for every sufficiently small positive \(h\). Its **unique** real matrix logarithm \(B=\log P_{\theta,h}\) has strictly positive entries in every off-diagonal position.
3. For every \(\theta\ge1\) and **every** \(h>0\), in the birth–death setting the unique real logarithm is a generator with strictly positive off-diagonal entries. More generally, the **existence of an explicit strictly positive Markov generator** extends to every finite irreducible continuous-time Markov generator, without the birth–death restriction; **uniqueness is not asserted in that generalization**.

For \(n=2\), write \(\Lambda=-\operatorname{tr}Q>0\). Then \(P_{\theta,h}\) is embeddable precisely when
\[
1-(1-\theta)h\Lambda>0;
\]
this condition holds automatically for every \(h>0\) if \(\theta\ge1\). When it holds, its unique embedding generator is \(B=(-\log r/\Lambda)Q\), with
\[
r=\frac{1-(1-\theta)h\Lambda}{1+\theta h\Lambda}\in(0,1).
\]
Thus **three states are minimal** for the absolute obstruction in part 1, and \(\theta=\frac12\) is its sharp implicitness boundary.

For the symmetric three-state unit-rate path,
\[
Q=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix},
\quad \theta=\frac12,\quad h=\frac12,
\]
one obtains the **strictly positive stochastic matrix**
\[
P=\frac1{35}\begin{pmatrix}23&10&2\\10&15&10\\2&10&23\end{pmatrix},
\quad \operatorname{spec}P=\left\{1,\frac35,\frac17\right\},
\]
yet its unique real logarithm satisfies
\[
(\log P)_{13}=\frac16\log\left(\frac{125}{189}\right)<0.
\]
Consequently even this positive, reversible, real-positive-spectrum Crank–Nicolson step cannot be a homogeneous continuous-time Markov transition.

## Assumptions and scope

All matrices and rates are real and finite-dimensional. The birth–death rates are strictly positive in both directions on every adjacent edge, ensuring irreducibility. The numerical matrix is defined for all \(h>0\) because \(I-\theta hQ\) is invertible for \(\theta\ge0\). It always has row sums one, but is not necessarily entrywise nonnegative at large steps. Embeddability is stronger than being stochastic: it requires a *time-homogeneous* continuous-time generator on the same state space, not a time-dependent generator, a hidden-state realization, or a factorization into multiple stochastic matrices.

## Proof

**1. Real simple spectrum and the logarithm criterion.** Every irreducible birth–death generator is diagonally similar to a real symmetric Jacobi matrix with positive neighboring off-diagonals. The latter has simple eigenvalues. Since the generator is irreducible, they are
\[
0,-\lambda_2,\ldots,-\lambda_n,
\qquad 0<\lambda_2<\cdots<\lambda_n=\Lambda.
\]
The scalar eigenvalue map of the step is
\[
g_{\theta,h}(\lambda)=\frac{1-(1-\theta)h\lambda}{1+\theta h\lambda},
\qquad g'_{\theta,h}(\lambda)=-\frac{h}{(1+\theta h\lambda)^2}<0.
\]
Hence the eigenvalues of \(P_{\theta,h}\) are real and distinct. An embeddable real matrix has no zero eigenvalue and no simple negative eigenvalue (a negative eigenvalue of a real exponential has even algebraic multiplicity). When all eigenvalues are positive, the *principal* logarithm is the **only real logarithm**: every logarithm commutes with its exponential, hence with \(P\), preserves each one-dimensional real eigenspace, and must take the unique real scalar logarithm on it. Consequently, with positive spectrum, embeddability is equivalent to nonnegative off-diagonal entries of \(B=\log P\), since \(B\mathbf1=0\). This is the specialized simple-spectrum version of the classical Markov embedding criterion.

**2. A sign lemma for tridiagonal generators.** Fix neighboring-distance-two states \(i\) and \(i+2\). For every integer \(k\ge2\),
\[
(-1)^k(Q^k)_{i,i+2}>0.
\]
Indeed, a nonzero length-\(k\) matrix-product path from \(i\) to \(i+2\) uses an even number of actual nearest-neighbor jumps; every remaining factor is a strictly negative diagonal entry. All terms therefore have sign \((-1)^k\), and at least one term is nonzero (two forward jumps with \(k-2\) diagonal stays). The identical assertion holds in the reverse direction. More generally, for distinct states at distance \(d\), \((Q^k)_{ij}=0\) for \(k<d\) and \((Q^d)_{ij}>0\).

**3. The obstruction at and below Crank–Nicolson.** Suppose \(0\le\theta\le\frac12\). If \(\theta<1\) and \(h\ge[(1-\theta)\Lambda]^{-1}\), the smallest step eigenvalue is zero or negative and simple, so the step has no real logarithm. It remains to handle
\[
0<h<\frac1{(1-\theta)\Lambda},
\]
where all step eigenvalues are positive. The two matrix logarithms below have convergent operator power series, because \((1-\theta)h\Lambda<1\) and \(\theta h\Lambda<1\):
\[
\begin{aligned}
B&=\log(I+(1-\theta)hQ)-\log(I-\theta hQ)\\
&=\sum_{k\ge1}c_kh^kQ^k,
\qquad c_k=\frac{\theta^k+(-1)^{k+1}(1-\theta)^k}{k}.
\end{aligned}
\]
For every odd \(k\), \(c_k>0\); for every even \(k\), \(c_k\le0\). At any distance-two entry, the terms for \(k<2\) vanish, while by step 2 every term for \(k\ge2\) is nonpositive. At least one term is strictly negative: for \(\theta<\frac12\) take \(k=2\); for \(\theta=\frac12\) take \(k=3\). Thus \(B_{i,i+2}<0\), contradicting the generator condition. This proves part 1 for all steps.

For \(0<\theta\le\frac12\), the identity
\[
P_{\theta,h}=\theta^{-1}(I-\theta hQ)^{-1}-\frac{1-\theta}{\theta}I
\]
shows every off-diagonal entry is strictly positive, since the resolvent of an irreducible generator is strictly positive. Its diagonal entries approach one as \(h\downarrow0\), hence the entire step is strictly positive and row-stochastic for sufficiently small \(h\).

**4. Embedding above the sharp boundary.** For any \(\theta>\frac12\) and sufficiently small \(h>0\), the preceding logarithmic series converges, now with
\[
c_k>0\qquad(k\ge1),
\]
because for even \(k\) one has \(\theta^k>(1-\theta)^k\), and odd coefficients are positive. For states \(i\ne j\) separated by graph distance \(d\), the first nonzero series term is
\[
B_{ij}=c_dh^d(Q^d)_{ij}+O(h^{d+1})>0
\quad(h\downarrow0).
\]
As there are finitely many entries, a common step threshold makes every off-diagonal entry positive. Furthermore, \(P\mathbf1=\mathbf1\) implies \(B\mathbf1=0\). Thus \(B\) is a genuine irreducible Markov generator, proving part 2.

**5. Unconditional embedding for \(\theta\ge1\).** Here both factors of \(P\) have positive real spectrum and
\[
B=\log(I-(\theta-1)hQ)-\log(I-\theta hQ)
=\int_{\theta-1}^{\theta}hQ(I-shQ)^{-1}\,ds.
\]
For \(s>0\) put \(R_s=(I-shQ)^{-1}\). It has the stochastic-resolvent representation
\[
R_s=\int_0^\infty e^{-u}e^{shQu}\,du,
\]
so every off-diagonal entry of \(R_s\) is strictly positive for irreducible \(Q\), and its row sums are one. Also
\[
hQ R_s=\frac{R_s-I}{s},
\]
whose off-diagonal entries are strictly positive and whose row sums vanish. The integrand extends continuously to \(s=0\), with limit \(hQ\). Integrating over an interval of positive length gives \(B\mathbf1=0\) and strictly positive off-diagonal entries. Thus \(P=e^B\) for all \(h>0\). This existence argument does not use the birth–death condition; its uniqueness conclusion relies on the birth–death simple real spectrum and is not asserted for arbitrary irreducible generators.

**6. The two-state exception.** In dimension two, \(Q\) has eigenvalues \(0\) and \(-\Lambda\), and \(P\) has eigenvalues \(1\) and \(r=g_{\theta,h}(\Lambda)\), which are distinct. If \(r\le0\), there is no real logarithm. If \(r>0\), then \(0<r<1\) and \(B=(-\log r/\Lambda)Q\) is a Markov generator with \(e^B=P\). This is the unique real logarithm, completing the theorem.

**7. Explicit positive three-state witness.** With the displayed symmetric path generator, the spectral projectors for eigenvalues \(0,-1,-3\) are respectively
\[
E_0=\frac13\mathbf1\mathbf1^{\mathsf T},\quad
E_1=\frac12(1,0,-1)^{\mathsf T}(1,0,-1),\quad
E_3=\frac16(1,-2,1)^{\mathsf T}(1,-2,1).
\]
The step is \(P=E_0+(3/5)E_1+(1/7)E_3\), giving the rational matrix above, and
\[
(\log P)_{13}=-\frac12\log\frac35+\frac16\log\frac17
=\frac16\log\frac{125}{189}<0.
\]
This finishes the explicit counterexample.

## Verification

The self-contained Python 3 file `artifacts/verify_embedding.py` checks the three-state matrix and its spectral projectors with exact fractions; tests the path-parity lemma on heterogeneous four- and five-state generators through degree fifteen; checks 114 coefficient signs through degree nineteen for all implicitness regimes; verifies positive stochastic resolvents and the exact resolvent identity at four rational parameters; and checks the two-state eigenvalue formula on 24 rational configurations. Run with `python3 artifacts/verify_embedding.py` from the package root. Its observed output was `VERIFY_OK exact checks: 336`. These finite checks verify necessary algebraic instances, **not** the all-dimension theorem; that theorem is proved analytically in the numbered steps above.

## Relationship to prior work

Classical Markov-embedding criteria, including the negative-eigenvalue obstruction and a principal-logarithm generator test for real simple-spectrum stochastic matrices, are **not** new (Davies 2010; Casanellas, Fernández-Sánchez and Roca-Lacostena 2020; Baake, Baake and Sumner 2025). The 2025 reversible-embedding study also gives the classical transitivity obstruction for strictly tridiagonal discrete transition matrices in dimensions at least three; thus the \(\theta=0\) endpoint is prior-covered. The finding applies these criteria to the entire family of \(\theta\)-method steps on irreducible birth–death generators, and supplies the **positive-step** sharp implicitness/dimension boundary, including all strictly positive Crank–Nicolson steps, and an all-step overimplicit embedding theorem, neither of which is stated in the inspected primary papers.

Zappavigna, Colaneri, Kirkland and Shorten (2012) analyze loss of entrywise positivity and Lyapunov stability for Padé approximations; this differs from a step that is already strictly positive but still cannot lie on *any* homogeneous Markov semigroup. Separate work on Crank–Nicolson positivity and order-cone preservation for Markov diffusion steps addresses different conditions; those properties do not imply embeddability. Existing work on the positivity of backward-Euler-filtered Crank–Nicolson and on the minimal state dimension for loss of positivity of the \([2/2]\) Padé map likewise does not settle this logarithmic-embedding distinction. The original texts and stated implications were compared rather than inferring originality from titles alone.

## Limitations

The theorem does **not** classify the entire intermediate stepsize window for \(\frac12<\theta<1\): it proves embedding for all sufficiently small steps and nonembedding whenever the scalar step multiplier has a nonpositive simple eigenvalue. It does not make assertions for reducible tridiagonal chains in parts 1–2, non-birth–death generators at \(\theta\le1\), nonlinear integrators, time-inhomogeneous continuous-time embeddings, or time-dependent controls. The positive off-diagonal effective generator for \(\theta>\frac12\) is generally *dense*, not a birth–death generator. All results are exact mathematics, not claims about floating-point stochasticity or simulation efficiency. Although targeted original-source and literature comparisons revealed no dominating theorem in this family, equivalently phrased specialized results in older numerical semigroup literature cannot be excluded absolutely.

## References

1. E. B. Davies, “Embeddable Markov Matrices,” arXiv:1001.1693v1 (public 11 January 2010). https://arxiv.org/abs/1001.1693
2. M. Casanellas, J. Fernández-Sánchez, J. Roca-Lacostena, “The embedding problem for Markov matrices,” arXiv:2005.00818v2, particularly Corollary 2.8. https://arxiv.org/abs/2005.00818
3. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442. Author version https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf ; DOI https://doi.org/10.1016/j.laa.2011.12.021
4. E. Baake, M. Baake, J. Sumner, “Embedding of reversible Markov matrices,” arXiv:2511.22800v1 (2025), especially Example 3.4, Fact 2.5 and Theorem 3.16. https://arxiv.org/abs/2511.22800
5. I. Higueras, T. Roldán, “A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation,” arXiv:2301.01066 (2023). https://arxiv.org/abs/2301.01066
6. Published mathematical notes, “Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson,” https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac
7. Published mathematical notes, “Eight-state barrier for Markov positivity of the [2/2] Padé map,” https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
