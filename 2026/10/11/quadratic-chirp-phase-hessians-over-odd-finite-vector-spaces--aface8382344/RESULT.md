# Quadratic chirp phase Hessians over odd finite vector spaces

## Finding
Let \(p\) be an odd prime, \(d\ge1\), \(V=\mathbb F_p^d\), and \(N=p^d\). Let \(Q:V\to\mathbb F_p\) be a nondegenerate homogeneous quadratic form with polar form \(B(h,x)=Q(h+x)-Q(h)-Q(x)\). Define the unimodular quadratic chirp \(u_Q(x)=\exp(2\pi iQ(x)/p)\) and its real phase-autocorrelation energy
\[
\mathcal E_Q(\theta)=\sum_{h\in V\setminus\{0\}}\left|\sum_{x\in V}u_Q(x+h)\overline{u_Q(x)}\,e^{i(\theta(x+h)-\theta(x))}\right|^2,
\qquad\theta\in\mathbb R^V.
\]
The chirp has zero off-origin autocorrelation, hence its normalized finite Fourier transform is also unimodular. The real Hessian \(\nabla^2\mathcal E_Q(0)\), for the ordinary Euclidean inner product on \(\mathbb R^V\), is diagonal in the Fourier-character basis indexed by \(h\in V\) using the pairing \(B\), with **exact eigenvalues**
\[
\boxed{\lambda_h=8N\sin^2\!\left(\frac{2\pi Q(h)}p\right),\qquad h\in V.}
\]
In particular, its nullspace is exactly the Fourier span of \(\{h:Q(h)=0\}\), with real dimension
\[
\boxed{Z(Q)=\begin{cases}p^{d-1},&d\text{ odd},\\[2mm]p^{d-1}+(p-1)p^{d/2-1}\,\chi_p((-1)^{d/2}\det M),&d\text{ even},\end{cases}}
\]
where \(Q(x)=x^{\mathsf T}Mx\), \(M\) is invertible symmetric over \(\mathbb F_p\), and \(\chi_p\) is the quadratic character on \(\mathbb F_p^\times\).

The quadratic chirp is **locally isolated among constant-amplitude zero-autocorrelation functions modulo global phase if and only if \(Q\) is anisotropic**; equivalently, either \(d=1\), or \(d=2\) with \(\chi_p(-\det M)=-1\). In that case, for sufficiently small mean-zero real \(\theta\),
\[
\mathcal E_Q(\theta)\ge 2N\sin^2(\pi/p)\,\|\theta\|_2^2.
\]
If \(s\ne0\) and \(Q(s)=0\), then every real function \(f:\mathbb F_p\to\mathbb R\) yields an **exact** zero-autocorrelation family
\[
\boxed{u_{Q,f,s}(x)=u_Q(x)\exp\bigl(i f(B(s,x))\bigr).}
\]
Modulo constant phases this is a smooth \((p-1)\)-torus. Tangent spaces to these families, as \(s\) ranges over projective isotropic lines, span the entire Hessian nullspace. This does **not** assert that arbitrary sums of the line deformations are themselves exact solutions or that these families exhaust all solutions near an isotropic chirp.

## Assumptions and scope
The group is the *elementary abelian additive group* of \(V\), not the cyclic group of order \(p^d\). The quadratic form is homogeneous, nondegenerate, and defined over an odd prime field; \(d\) is arbitrary. Unimodularity refers to modulus one in both the original coordinates and the unitary Fourier transform \(N^{-1/2}\sum_xu(x)\overline{\gamma(x)}\). All phase parameters are real and considered locally modulo \(2\pi\mathbb Z\) on each coordinate. The theorem gives the exact Hessian, its nullity, a local-isolation criterion, and individual exact flat families; it does not give a global classification of perfect sequences.

## Proof
**1. Chirp correlation.** Put \(e_p(t)=e^{2\pi it/p}\). Quadratic polarization gives
\[
u_Q(x+h)\overline{u_Q(x)}=e_p(Q(h))e_p(B(h,x)).
\]
For nonzero \(h\), the linear character \(x\mapsto e_p(B(h,x))\) is nontrivial because \(B\) is nondegenerate, so its sum vanishes. Fourier autocorrelation therefore implies that the unitary Fourier transform has modulus one everywhere.

**2. First variation.** For real \(\varphi\), write \(C_h(t)\) for the \(h\)-autocorrelation of \(u_Qe^{it\varphi}\). Direct differentiation, changing variables in the translated term, gives
\[
C_h'(0)=i e_p(Q(h))\bigl(e_p(-B(h,h))-1\bigr)
\sum_xe_p(B(h,x))\varphi(x).
\]
As \(B(h,h)=2Q(h)\), and with the \(B\)-Fourier normalization \(\widehat\varphi(h)=N^{-1}\sum_x\varphi(x)e_p(-B(h,x))\), reality of \(\varphi\) gives
\[
\mathcal E_Q(t\varphi)
=4N^2t^2\sum_{h\ne0}\sin^2\!\left(\frac{2\pi Q(h)}p\right)|\widehat\varphi(h)|^2+O_\varphi(t^3).
\]
Consequently
\[
D^2\mathcal E_Q(0)[\varphi,\varphi]
=8N^2\sum_{h\in V}\sin^2\!\left(\frac{2\pi Q(h)}p\right)|\widehat\varphi(h)|^2.
\]
Parseval reads \(\|\varphi\|_2^2=N\sum_h|\widehat\varphi(h)|^2\). The multiplier is even under \(h\mapsto-h\), so the stated spectral eigenvalues apply to the real cosine/sine character basis as well. Because \(p\) is odd, \(\sin(2\pi Q(h)/p)=0\) exactly when \(Q(h)=0\). The zero-frequency constant direction is among these.

**3. Exact nullity.** Diagonalize \(Q\) over \(\mathbb F_p\). By character orthogonality,
\[
Z(Q)=p^{-1}\sum_{t\in\mathbb F_p}\sum_{x\in V}e_p(tQ(x)).
\]
For \(t\ne0\), each diagonal Gauss sum contributes a quadratic-character factor; its square is \(\chi_p(-1)p\). If \(d\) is odd, the sum over nonzero \(t\) cancels. If \(d=2m\), it equals \((p-1)p^m\chi_p((-1)^m\det M)\). Dividing by \(p\) proves the displayed formula. A nondegenerate quadratic form over \(\mathbb F_p\) is anisotropic precisely in dimension one and in nonsplit dimension two: for \(d\ge3\), the formula gives \(Z(Q)>1\), while in dimension two \(Z(Q)=1\) exactly for \(\chi_p(-\det M)=-1\).

**4. Exact flat directions.** Fix a nonzero isotropic \(s\). The new phase depends only on \(B(s,x)\). For a shift \(h\) not proportional to \(s\), the restriction of \(x\mapsto B(h,x)\) to \(\ker B(s,\cdot)\) is nontrivial, hence the correlation sum cancels over each fiber of \(B(s,\cdot)\). If \(h=ts\), then \(B(s,h)=2tQ(s)=0\); the new phase quotient under that shift is identically one, and the original nontrivial-character correlation cancels. All nonzero shifts vanish. The map \(B(s,\cdot)\) is onto \(\mathbb F_p\), so these arbitrary coordinate phases form a \(p\)-torus, or \((p-1)\)-torus modulo global phase. Their tangents contain the complete real Fourier support on the line \(\mathbb F_ps\). Every nonzero isotropic label lies on exactly one such line, so their combined tangent spans precisely \(\ker\nabla^2\mathcal E_Q(0)\).

**5. Local isolation.** In the anisotropic case the only Hessian zero mode is the constant vector. For every nonconstant Fourier label, \(\sin^2(2\pi Q(h)/p)\ge\sin^2(\pi/p)\). The real analytic function \(\mathcal E_Q\) is invariant under global phase; its Taylor expansion on mean-zero phases therefore has the positive quadratic lower bound displayed above after shrinking the neighborhood. Thus the only nearby zero-energy functions differ by global phase. In the isotropic case the explicit nonconstant \((p-1)\)-torus of exact solutions supplies arbitrarily small counterexamples to isolation. This proves both implications.

## Verification
Run `python3 verify.py` from the directory containing this result's accompanying checker. The standard-library script independently enumerates \(140\) diagonal nondegenerate quadratic forms over odd prime fields and checks the zero-count formula, compares the predicted Hessian to centered finite differences for \(10\) distinct examples, and checks \(7\) exact phase families by direct correlation sums. Observed output was:

`VERIFY_OK quadratic_zero_counts=140 hessian_directional=10 flat_families=7 maximum_relative_hessian_error=1.794e-10`

Finite checks use floating arithmetic and do not prove the theorem in general; the preceding character and Gauss-sum arguments establish the all-prime, all-rank statements.

## Relationship to prior work
Feichtinger–Kozek–Luef study finite-abelian signal and time-frequency theory, supplying the multi-dimensional Fourier framework but not this local phase-energy Hessian. Gilbert–Rzeszotnik establish the role of biunimodular functions among finite Fourier extremizers and discuss cyclic examples with isolated versus continuous families. Führ–Rzeszotnik analyze biunimodular vectors for general unitary matrices and cyclic zero-autocorrelation examples. Their inspected statements do not identify an odd-field quadratic-form isotropic cone with the entire phase-energy Hessian kernel, nor the exact all-rank nullity and local-isolation dichotomy. Banica’s generalized-Fourier-matrix defect concerns a full \(N\times N\) Hadamard matrix, not the \(N\)-dimensional phase-autocorrelation energy of a fixed chirp; the paper leaves the circulant case as an explicit unsolved tangent system. The explicit split-form phase families have antecedents in bent-function constructions; originality is claimed for the combined spectral and local-rigidity classification, not for the existence of arbitrary-function bent deformations in isolation. In particular, the cyclic group of order \(p^2\) is not interchangeable with \(\mathbb F_p^2\), whose split and nonsplit forms have different Hessian nullities.

## Limitations
Only real phase perturbations of quadratic chirps are analyzed. A Hessian-null direction need not integrate jointly with unrelated null directions; there is no assertion of a smooth complete local moduli space in the isotropic case. Nor is there a classification of nonquadratic, global, or even-characteristic solutions. The isolated case supplies a local, not globally optimal, stability radius. Although primary texts and a published-results index were compared, equivalent formulations in the older bent-function or circulant-Hadamard defect literature remain an originality risk.

## References
1. H. G. Feichtinger, W. Kozek and F. Luef, *Gabor analysis over finite Abelian groups*, arXiv:math/0703228, first public preprint 2007-03-08, https://arxiv.org/abs/math/0703228.
2. J. Gilbert and Z. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Ann. Inst. Fourier 60 (2010), 1317–1346, DOI:10.5802/aif.2556; printed primary MSC 42C40, https://www.numdam.org/item/AIF_2010__60_4_1317_0/.
3. H. Führ and Z. Rzeszotnik, *On biunimodular vectors for unitary matrices*, arXiv:1506.06738, first public preprint 2015-06-19, https://arxiv.org/abs/1506.06738.
4. T. Banica, *The defect of generalized Fourier matrices*, arXiv:1210.2556, first public preprint 2012-10-09, https://arxiv.org/abs/1210.2556.
