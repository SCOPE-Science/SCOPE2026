# Exact spectral doublets of a Stieltjes–Volterra operator with one midpoint atom

## Finding

For any real \(a>0\), put \(\mu_a=dt+a\,\delta_{1/2}\) on \([0,1]\), let \(H_a=L^2([0,1],\mu_a;\mathbb C)\), and define the **strict Stieltjes–Volterra integration operator**
\[
(V_af)(t)=\int_{[0,t)}f(s)\,d\mu_a(s),\qquad t\in[0,1].
\]
For every integer \(m\ge0\), there exist exactly two numbers \(\kappa_{m,+}<\kappa_{m,-}\) in \((2\pi m,2\pi(m+1))\), uniquely determined by
\[
\cot(\kappa_{m,+}/2)=a\kappa_{m,+}+1,\qquad
\cot(\kappa_{m,-}/2)=a\kappa_{m,-}-1.
\]
**Complete singular-spectrum theorem.** Every nonzero singular value of \(V_a\) is simple, and in decreasing order they are precisely
\[
 s_{2m+1}(V_a)=\kappa_{m,+}^{-1},\qquad
 s_{2m+2}(V_a)=\kappa_{m,-}^{-1}\qquad(m=0,1,2,\dots).
\]
The high-frequency singular spectrum forms unusually close *doublets*:
\[
\boxed{\lim_{m\to\infty}m^4\bigl(s_{2m+1}(V_a)-s_{2m+2}(V_a)\bigr)
       =\frac{1}{4\pi^4a^2}.}
\]
By contrast the full singular sequence has \(\lim_{n\to\infty}n\,s_n(V_a)=1/\pi\). The Hilbert–Schmidt trace and critical logarithmic trace are
\[
\sum_{m=0}^{\infty}\bigl(\kappa_{m,+}^{-2}+\kappa_{m,-}^{-2}\bigr)
 =\|V_a\|_{\mathcal S_2}^2=\frac12+a,
\qquad
\lim_{N\to\infty}\frac{\sum_{n=1}^{N}s_n(V_a)}{\log N}=\frac1\pi.
\]
Consequently \(V_a\in\mathcal S_p\) exactly for \(p>1\).

## Assumptions and scope

The scalar field is complex (identical conclusions hold over the reals); the atom has fixed positive mass \(a\) and is at the geometric midpoint. Integration over \([0,t)\), rather than \([0,t]\), is intentional: at the atom, the state is the **left limit**, while the value immediately to the right has an impulsive increment \(a f(1/2)\). Singular values are the eigenvalues of \(|V_a|\), counted with their usual multiplicities. No result for other atom locations, several atoms, or arbitrary singular measures is claimed. The limit \(a\to0\) is not uniform in high singular-value rank.

The midpoint is not chosen as an arbitrary numerical slice: it is the symmetric minimal mixed-clock model, where the continuous halves have equal lengths. This symmetry is precisely responsible for spectral pairing and the quartic intra-pair spacing. The issue is a quantitative operator-ideal refinement of mixed continuous/atomic Stieltjes compactness, not a claim about the full Aubin–Lions three-space projection.

## Proof

**1. Compactness and the precise integration convention.** The operator has kernel \(K(t,s)=\mathbf1_{\{s<t\}}\) on \(H_a\). Since \(\mu_a\) is finite, this kernel belongs to \(L^2(\mu_a\otimes\mu_a)\); thus \(V_a\) is Hilbert–Schmidt and compact. The two continuous portions of the strictly ordered square give area \(1/2\), and the atom interacts with Lebesgue mass \(1/2\) on either side, giving total \(a\). The atom cannot interact with itself because the inequality is strict. Hence
\[
\|V_a\|_{\mathcal S_2}^2=\iint_{s<t}d\mu_a(s)d\mu_a(t)=\frac12+a.
\]
The kernel is nonzero on every suitable triangular subregion of each continuous half, so the operator has infinite rank.

**2. Energy-space equivalence, including the atomic coordinate.** Put \(c=1/2\). A vector \(u=V_af\), identified with its two continuous representatives and its atomic value, consists of functions \(u_-\in H^1(0,c)\), \(u_+\in H^1(c,1)\), with \(u_-(0)=0\) and **atomic evaluation** \(u(c)=u_-(c)\). There is no imposed continuity at the atom. Conversely every such pair arises uniquely from a function \(f\in H_a\) by setting \(f=u_-'\) on the first half, \(f=u_+'\) on the second half, and
\[
 f(c)=\frac{u_+(c)-u_-(c)}a.
\]
Indeed, the strict integral accumulates the continuous derivative before \(c\) and includes the atomic increment exactly for \(t>c\). Consequently \(V_a\) identifies \(H_a\) isometrically with the Hilbert energy space \(\mathcal X_a\) having form
\[
 E(u,v)=\int_0^c u_-'\overline{v_-'}dt+\int_c^1u_+'\overline{v_+'}dt
  +\frac{[u]\overline{[v]}}a,
 \qquad [u]=u_+(c)-u_-(c),
\]
whereas its embedding in \(H_a\) has inner product
\[
 N(u,v)=\int_0^c u_-\overline{v_-}dt+\int_c^1u_+\overline{v_+}dt
    +a\,u_-(c)\overline{v_-(c)}.
\]
The energy is strictly positive away from zero because \(u_-(0)=0\). Compactness of the inclusion \(\mathcal X_a\hookrightarrow H_a\) follows from compact \(H^1\) embeddings on both halves and compactness of the one-dimensional evaluation coordinate. By the compact-operator singular-value variational principle, positive reciprocals \(\kappa=1/s(V_a)\) are precisely the positive square roots of generalized eigenvalues \(E(u,v)=\kappa^2N(u,v)\) for all \(v\in\mathcal X_a\).

**3. The exact transmission eigenproblem.** Interior test functions yield \(-u_\pm''=\kappa^2u_\pm\) on their respective open halves. Integrating by parts and varying the two interface traces independently gives
\[
 u_-'(c)=u_+'(c)+a\kappa^2u_-(c),\qquad
 u_+'(c)=\frac{u_+(c)-u_-(c)}a.
\]
At the free right endpoint, \(u_+'(1)=0\). At the left endpoint, \(u_-(0)=0\). Every positive eigenfunction therefore has the form
\[
 u_-(t)=A\sin(\kappa t),\qquad
 u_+(t)=B\cos(\kappa(1-t)),
\]
and its two interface equations, after division by \(\kappa>0\), are
\[
 \begin{pmatrix}
 \sin(\kappa/2)&-\cos(\kappa/2)+a\kappa\sin(\kappa/2)\\
 \cos(\kappa/2)-a\kappa\sin(\kappa/2)&-\sin(\kappa/2)
 \end{pmatrix}
 \begin{pmatrix}A\\B\end{pmatrix}=0.
\]
Taking the determinant produces, up to a nonzero sign, the characteristic function
\[
 F_a(\kappa)=\cos\kappa-a\kappa\sin\kappa
   +a^2\kappa^2\sin^2(\kappa/2)
  =\bigl(\cos(\kappa/2)-(a\kappa+1)\sin(\kappa/2)\bigr)
   \bigl(\cos(\kappa/2)-(a\kappa-1)\sin(\kappa/2)\bigr).
\]
At \(\sin(\kappa/2)=0\) this determinant equals \(1\), so no root has a vanishing denominator when the two displayed cotangent equations are obtained. Conversely each positive root gives a nonzero pair \((A,B)\) satisfying the interface equations and hence a genuine singular eigenvector; no boundary solution is lost in elimination.

**4. Exhaustion, strict ordering and simplicity.** For every integer \(m\ge0\), the function \(\kappa\mapsto\cot(\kappa/2)-a\kappa\) decreases strictly from \(+\infty\) to \(-\infty\) on the interval \((2\pi m,2\pi(m+1))\), because its derivative is \(-\tfrac12\csc^2(\kappa/2)-a<0\). Consequently the equations with right sides \(+1\) and \(-1\) have exactly one solution each on that interval, and the first solution is smaller. The intervals are disjoint and exhaust the positive axis up to excluded endpoints; hence every positive generalized eigenvalue is listed. The interface matrix has rank exactly one at each root because its sine entries do not vanish. Thus every eigenspace has dimension one; the generalized problem is compact and self-adjoint, so all the positive eigenvalues and the associated singular values are simple. Their reciprocals appear in the asserted decreasing order.

**5. Pair spacing, the Weyl law and the operator ideals.** Fix \(a>0\), put \(K_m=2\pi m\), and write \(\kappa_{m,\pm}=K_m+\varepsilon_{m,\pm}\). For \(m\to\infty\) the cotangent equations force \(\varepsilon_{m,\pm}\to0^+\) and
\[
 \cot(\varepsilon/2)=\frac2\varepsilon+O(\varepsilon).
\]
Solving the two equations through the next term, uniformly for fixed \(a\), yields
\[
 \varepsilon_{m,+}=\frac{2}{aK_m}-\frac{2}{a^2K_m^2}+O_a(K_m^{-3}),
 \qquad
 \varepsilon_{m,-}=\frac{2}{aK_m}+\frac{2}{a^2K_m^2}+O_a(K_m^{-3}).
\]
It follows that \(\kappa_{m,-}-\kappa_{m,+}=4/(a^2K_m^2)+O_a(K_m^{-3})\), whence
\[
 s_{2m+1}-s_{2m+2}=
 \frac{\kappa_{m,-}-\kappa_{m,+}}{\kappa_{m,+}\kappa_{m,-}}
 =\frac4{a^2(2\pi m)^4}+O_a(m^{-5}),
\]
which proves the boxed quartic limit. The same expansion shows \(s_n\sim(\pi n)^{-1}\) with the natural paired indexing. Hence \(\sum_n s_n^p<\infty\) exactly for \(p>1\), and comparison of harmonic sums gives \(\sum_{n\le N}s_n\sim\pi^{-1}\log N\). The Hilbert–Schmidt identity from Step 1 completes the exact root sum rule.

## Verification

The accompanying `verify_atom.py` independently evaluates the two monotone cotangent equations, tests the algebraically unexpanded transmission determinant, compares exact root predictions to a separate finite weighted-kernel singular-value discretization for several masses, checks the direct kernel Hilbert–Schmidt trace, and tests the predicted fourth-power splitting at growing indices. Run `python verify_atom.py` after installing `numpy` from `requirements.txt`. The finite matrix comparisons are diagnostic, not exhaustive; all claims about infinitely many singular values follow from Steps 1–5.

## Relationship to prior work

Fernández, *Aubin–Lions Compactness for Stieltjes–Bochner Evolution Graphs* (arXiv:2609.10064v1, publicly available 9 September 2026), develops the mixed atomic/continuous Stieltjes graph and a compact state projection. Its full text gives neither the spectrum of the strict integration operator considered here nor paired singular-value asymptotics. The present claim concerns the complete singular spectrum and a sharp intra-doublet fourth-power law, not a restatement of compactness.

Classical singular values for the ordinary Lebesgue Volterra operator, transfer-matrix spectral methods, and general singular-value asymptotics for smooth Volterra kernels predate this result. In the atom-free case the exact singular values are \((\pi(n-\tfrac12))^{-1}\); that fact is not claimed as new. Bird–Ngai–Teplyaev (2003) study measure-defined interval Laplacians under **continuous-measure** hypotheses, which do not cover a positive interior atom or the present jump-energy form. Tuan–Gorenflo (1996) study general singular-value asymptotics of Volterra kernels, not the atomic transmission doublet.

Two close published operator-theory comparisons were inspected in full: *Radial singular-value majorization for reflection-symmetric weighted integration* treats smooth positive weights on Lebesgue \(L^2\) and rank-one-corrected integration, whereas *An entire characteristic determinant for the singular spectrum of the Hardy–Volterra commutator* treats the distinct analytic kernel \((1-t/x)\mathbf 1_{t<x}\). Neither hypothesis yields the one-atom metric or the two cotangent branches and quartic splitting. General string/point-interaction transfer methods may supply alternative equivalent proofs of the characteristic equation; the novel component asserted is the explicitly quantified mixed-measure singular doublet, subject to independent bibliographic confirmation.

## Limitations

The mass \(a\) must be strictly positive and fixed before taking the high-rank limit. The midpoint and strict half-open integration convention are essential to the statement. The result does not cover the full spectrum of other Stieltjes graph embeddings, nor prove uniformity over arbitrary atom positions, multiple atoms, or mass tending to zero. Determinant factorization, coupled-string interface methods and general singular asymptotics are established techniques, not new methods. Although directly matching references were not found in the recorded searches and close records were compared by implication, independent priority verification is not yet performed; potentially unindexed point-mass string theorems could overlap with portions of the claim.

## References

1. F. J. Fernández, *Aubin–Lions Compactness for Stieltjes–Bochner Evolution Graphs*, arXiv:2609.10064v1, first public 9 September 2026. https://arxiv.org/abs/2609.10064.
2. E. J. Bird, S.-M. Ngai and A. Teplyaev, *Fractal Laplacians on the Unit Interval*, Annales des Sciences Mathématiques du Québec **27** (2003), 1–34. https://digitalcommons.georgiasouthern.edu/math-sci-facpubs/604/.
3. V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numer. Funct. Anal. Optim. **17** (1996), 453–461, DOI:10.1080/01630569608816704.
4. *Radial singular-value majorization for reflection-symmetric weighted integration*, public mathematics result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-radial-singular-value-majorization-for-reflection-symmetric-weig--2b376b3b891a.
5. *An entire characteristic determinant for the singular spectrum of the Hardy–Volterra commutator*, public mathematics result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-entire-characteristic-determinant-for-the-singular-spectrum-o--2a37cf33f373.
