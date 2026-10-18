# A golden-ratio phase transition for weighted five-cycle Schatten-fourth radii

## Finding

For a weighted cyclic shift \(W\) on \(\mathbb C^5\), define
\[
 W e_j=a_j e_{j+1\pmod 5},\qquad \sum_{j=0}^4|a_j|^2=1,
\]
and, for \(0\le t\le1\), the weighted Schatten-fourth numerical radius
\[
 \mathfrak w_{t,4}(W)=\sup_{\theta\in\mathbb R}
 \big\|t e^{i\theta}W+(1-t)e^{-i\theta}W^*\big\|_{\mathcal S_4}.
\]
Put \(A=t^4+(1-t)^4\), \(q=4t^2(1-t)^2/A\in[0,2]\), and \(\gamma=\sqrt5-1\). Then the exact normalized minimax law is
\[
 \boxed{\min_{\sum|a_j|^2=1}\mathfrak w_{t,4}(W)^4
 =A\begin{cases}
 (1+q)/5,&0\le q\le\gamma,\\
 (2+q)/(6+q),&\gamma\le q\le2.
 \end{cases}}
\]
The complete equality profiles, stated in terms of \(x_j=|a_j|^2\), are as follows. All complex weight phases are arbitrary.

* If \(0\le q<\gamma\), the unique profile is \(x_j=1/5\) for all \(j\).
* At \(q=\gamma\), the set of minimizing profiles is **exactly**
  \[
  x_j=\frac15+u\cos\frac{4\pi j}{5}+v\sin\frac{4\pi j}{5}\ge0
  \quad(0\le j<5),\qquad (u,v)\in\mathbb R^2.
  \]
  In particular, the uniform profile and nonuniform boundary profiles coexist in a two-dimensional family.
* If \(\gamma<q<2\), the only profiles are cyclic rotations of
  \[
  \left(\frac{2+q}{6+q},0,\frac2{6+q},\frac2{6+q},0\right).
  \]
  Thus **exactly three weights are nonzero** in every minimizer.
* At \(q=2\) (equivalently \(t=1/2\)), the profiles are precisely cyclic rotations of
  \[
  (1/2,0,s,1/2-s,0),\qquad 0\le s\le1/2.
  \]
  Some endpoint profiles have just two nonzero weights.

The transition parameter \(q=\gamma\) occurs at two reciprocal choices of \(t\), approximately \(t=0.370368206338183\) and \(t=0.629631793661817\).

## Assumptions and scope

The underlying scalar field is \(\mathbb C\), the space is standard Euclidean \(\mathbb C^5\), \(\mathcal S_4\) denotes the Schatten-four class with unnormalized trace, and \(0\le t\le1\). A weighted five-cycle includes matrices with zero weights; for nonzero complex weights their phases need not agree. The Hilbert–Schmidt norm normalization is \(\|W\|_{\mathcal S_2}=1\). These are all global minimizers without a positivity assumption on the complex weights.

The objective is a fourth power. For arbitrary nonzero \(W\), divide the squared moduli by \(\sum|a_j|^2\) and multiply the displayed minimum by \((\sum|a_j|^2)^2\). No assertion is made for other dimensions or other Schatten exponents.

## Proof

**1. Exact phase-free trace identity.** Let \(u=1-t\) and \(Z_\theta=t e^{i\theta}W+u e^{-i\theta}W^*\). Since \(\|Z_\theta\|_{\mathcal S_4}^4=\operatorname{tr}[(Z_\theta^*Z_\theta)^2]\), expand
\[
 Z_\theta^*Z_\theta
 =t^2W^*W+u^2WW^*+tu(e^{2i\theta}W^2+e^{-2i\theta}(W^*)^2).
\]
The first two summands together form a diagonal matrix; their cross trace with \(W^2\) or \((W^*)^2\) vanishes. For a five-cycle, \(\operatorname{tr}W^4=0\), while
\[
 \operatorname{tr}(W^*W)^2=\operatorname{tr}(WW^*)^2=\sum_jx_j^2,
 \qquad
 \operatorname{tr}(W^*W\,WW^*)=
 \operatorname{tr}(W^2(W^*)^2)=\sum_jx_jx_{j+1}.
\]
All indices in this proof are taken modulo five. Consequently the phase variable disappears **exactly**:
\[
 \boxed{\mathfrak w_{t,4}(W)^4
 =A\sum_{j=0}^4x_j^2+4t^2u^2\sum_{j=0}^4x_jx_{j+1}
 =A\,F_q(x),}
\]
where \(F_q(x)=\sum_jx_j^2+q\sum_jx_jx_{j+1}\) on the nonnegative probability simplex.

**2. The uniform phase and its entire critical face.** Let \(C\) be the real adjacency matrix of the ordinary five-cycle. Then \(F_q(x)=x^\top M_qx\) with \(M_q=I+(q/2)C\). Fourier diagonalization gives its eigenvalues
\[
 1+q\cos\frac{2\pi k}{5},\qquad 0\le k<5.
\]
The minimum eigenvalue is \(1-q\cos(\pi/5)\), and \(1/\cos(\pi/5)=\sqrt5-1=\gamma\). Thus \(M_q\) is positive definite for \(0\le q<\gamma\) and positive semidefinite at equality. Write \(x=(1/5)\mathbf1+y\), where \(\sum_jy_j=0\). Because the constant vector is an eigenvector,
\[
 F_q(x)=\frac{1+q}{5}+y^\top M_qy.
\]
This proves uniform uniqueness below the threshold. At the threshold the zero eigenspace is precisely the two-dimensional real Fourier mode spanned by \(\cos(4\pi j/5)\) and \(\sin(4\pi j/5)\); intersecting its affine translate with the simplex gives **all** critical minimizers.

**3. Support reduction above the threshold.** Suppose \(\gamma<q\le2\). If a putative minimizer has five positive entries, perturb it by a small multiple of the real zero-sum Fourier vector \(v_j=\cos(4\pi j/5)\). Its second variation is \(2v^\top M_qv<0\), so the point cannot be a local minimum. If exactly four entries are positive, they form an induced path on four vertices. Order them along that path and perturb by a small multiple of
\[
 v=(\sin(\pi/5),-\sin(2\pi/5),\sin(2\pi/5),-\sin(\pi/5)).
\]
This has coordinate sum zero and is an eigenvector of the path adjacency matrix with eigenvalue \(-2\cos(\pi/5)\). Its second variation is again strictly negative. Therefore every minimizer has support of cardinality at most three.

**4. Classify every remaining support.** Three vertices of a pentagon either induce a consecutive path of length two, or one edge plus an isolated vertex. For the first type, let \(y\) be the middle mass and \(x,z\) the endpoint masses, so \(x+z=1-y\). The elementary bound \(x^2+z^2\ge(1-y)^2/2\) gives
\[
 F_q\ge\tfrac12+(q-1)y+(\tfrac32-q)y^2\ge\tfrac12
 \quad(\gamma<q\le2,\;0\le y\le1).
\]
The last inequality follows directly for \(q\le3/2\); for \(3/2\le q\le2\), use \(y^2\le y\) with its nonpositive coefficient. Equality requires \(y=0\) and equal endpoint masses.

For the edge-plus-isolate type, denote the isolated mass by \(z\), the adjacent masses by \(a,b\), with \(a+b=1-z\). Then
\[
 F_q=z^2+\frac{2+q}{4}(1-z)^2+\frac{2-q}{4}(a-b)^2.
\]
If \(q<2\), equality in the last term forces \(a=b\), and scalar minimization gives
\[
 z=\frac{2+q}{6+q},\quad a=b=\frac2{6+q},\quad
 F_q=\frac{2+q}{6+q}.
\]
For \(\gamma<q<2\), this value is strictly below \(1/2\), excluding every other support type, including all supports of size one or two. At \(q=2\), the squared-difference coefficient vanishes. Its minimum is \(1/2\) precisely at \(z=1/2\) and \(a+b=1/2\), and it includes the minimizing nonadjacent pairs as endpoints. This gives the claimed complete equality classification at the endpoint.

**5. Compare regimes.** At \(q=\gamma\), the two formulas coincide because
\[
 \frac{2+q}{6+q}-\frac{1+q}{5}
 =\frac{4-2q-q^2}{5(6+q)}.
\]
This vanishes at \(q=\sqrt5-1\), is positive below it, and negative above it. Combining Steps 1–4 proves the complete theorem, including all parameter endpoints and phases.

## Verification

An optional standard-library-only diagnostic program, `verify_cycle5.py`, directly forms complex five-cycle matrices, evaluates \(\operatorname{tr}[(Z_\theta^*Z_\theta)^2]\) at several angles, and compares it with the exact quadratic trace identity. It also tests the predicted extrema and critical profiles against thousands of sampled simplex points. The script reports 7059 passing finite assertions. These computations do **not** prove the continuum minimum or equality classification; Steps 1–5 do so without computational assumptions.

## Relationship to prior work

Pal and Chandok (2026) define the weighted Schatten numerical radius and develop generalized-Aluthge operator inequalities, including a Schatten-fourth upper estimate. The new result solves an exact nonlinear minimax problem for cyclic five-by-five shifts rather than a general upper-bound problem. Earlier finite weighted-shift numerical-range calculations concern other operator norms or restricted weights. Separately available sharp results for nilpotent one-step shifts concern paths, not the closed five-cycle and its critical Fourier eigenspace. An exact four-cycle optimization concerns a different winding term: the trace of the fourth power of a four-cycle is nonzero, whereas it vanishes here. None of these comparisons claims that the literature search establishes unique priority.

## Limitations

This classification is restricted to five-cycle weighted matrices, the Schatten-fourth radius, and Hilbert–Schmidt normalization. Its proof does not imply the full phase diagram for longer odd cycles, or quantitative stability away from the minima. A complete independent priority check of all older graph-quadratic optimization literature has not been performed. The overlap search includes indexed result summaries whose underlying full manuscripts could not all be inspected, so an equivalent formulation outside the inspected sources remains a residual risk. Finite diagnostic checks are supplementary and are not independent mathematical validation.

## References

1. Kallal Pal and Sumit Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336, first posted 2026-10-08. https://arxiv.org/abs/2610.11336.
2. *On the numerical range of some weighted shift matrices and operators*, *Linear Algebra and its Applications* (2014), DOI:10.1016/j.laa.2014.02.018. Prior study of numerical radii for restricted weighted shifts, not of the weighted Schatten-fourth five-cycle minimax law.
3. T. S. Motzkin and E. G. Straus, *Maxima for graphs and a new proof of a theorem of Turán*, *Canadian Journal of Mathematics* 17 (1965), 533–540. Classical background for graph simplex quadratic forms; the proof above does not require their extremal theorem.
