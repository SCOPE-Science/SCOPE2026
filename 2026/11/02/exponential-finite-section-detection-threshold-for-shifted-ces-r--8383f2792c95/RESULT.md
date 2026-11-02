# Exponential finite-section detection threshold for shifted Cesàro nonhyponormality

## Finding

Let \(C_\alpha\) be the order-one shifted Cesàro operator on complex \(\ell^2(\mathbb N_0)\), with \(\alpha>-1\), and let \(K_\alpha=C_\alpha^*C_\alpha-C_\alpha C_\alpha^*\). Write \(P_N\) for the orthogonal projection onto the first \(N\) coordinate vectors, with \(N\ge1\). The new quantitative question is: **how many leading coordinates are necessary and sufficient to detect the failure of hyponormality?** The answer is an exact scalar threshold, with an exponentially diverging critical dimension near \(\alpha=0\).

For \(-1<\alpha<0\) set \(\varepsilon=-\alpha\), \(z=N+\alpha>0\), and
\[
\mathcal S_N(\alpha)=\psi(N+\alpha+1)-\psi(\alpha+2)
 +\frac{1}{z^2\psi_1(z)-z},
\]
where \(\psi\) and \(\psi_1\) are the digamma and trigamma functions. The denominator is strictly positive. **For every positive integer \(N\)**,
\[
\boxed{\operatorname{ind}_-(P_N K_\alpha P_N)=
\begin{cases}1,&\varepsilon\mathcal S_N(\alpha)>1,\\0,&\varepsilon\mathcal S_N(\alpha)\le1.\end{cases}}
\]
At equality the finite section has one zero eigenvalue; below equality it is strictly positive. The scalar \(\mathcal S_N(\alpha)\) increases strictly with \(N\) and tends to infinity, so the **first negative principal-section size**
\[
N_*(\varepsilon)=\min\{N\ge1:\varepsilon\mathcal S_N(-\varepsilon)>1\}
\]
is finite and unambiguously defined for each \(0<\varepsilon<1\). It has the sharp essential-singularity asymptotic
\[
\boxed{\lim_{\varepsilon\downarrow0}N_*(\varepsilon)e^{-1/\varepsilon}=e^{-1-\gamma},}
\]
where \(\gamma\) is Euler's constant. Thus the smallest principal compression witnessing nonhyponormality grows exponentially, with an explicit prefactor. The full trace-class self-commutator has exactly one negative eigenvalue for every \(-1<\alpha<0\); it is positive for \(\alpha\ge0\).

For comparison with the explicit inverse-image witness used in Ma's nonhyponormality proof [1, Section 7], consider
\[
u_L=\sum_{i=0}^{L-1}(i+\alpha+1)(e_i-e_{i+1})
\]
and let \(L_*(\varepsilon)\) be the first positive integer \(L\) at which \(\langle K_{-\varepsilon}u_L,u_L\rangle<0\). Then
\[
\boxed{\lim_{\varepsilon\downarrow0}L_*(\varepsilon)e^{-1/\varepsilon}=e^{1-\gamma},
\qquad \lim_{\varepsilon\downarrow0}\frac{L_*(\varepsilon)}{N_*(\varepsilon)}=e^2.}
\]
Thus optimizing over the entire canonical coordinate section detects negativity by a sharp factor \(e^2\) earlier than that particular preselected witness. This comparison is new only as a quantitative finite-section optimization; the prior construction and qualitative nonhyponormality are expressly credited to [1].

This concerns **compressions of the full self-commutator**, not the self-commutator of a finite-section Cesàro matrix.

## Assumptions and scope

For every real \(\alpha>-1\) define the bounded operator
\[
(C_\alpha x)_n=\frac{1}{n+\alpha+1}\sum_{j=0}^{n}x_j,
\qquad n\in\mathbb N_0.
\]
Boundedness for this parameter range is established in Ma [1, Theorem 1.1]. Inner products use the standard complex Hilbert-space convention; signs of self-adjoint forms are independent of convention. The notation \(\operatorname{ind}_-\) counts strictly negative eigenvalues with multiplicity. The finite section \(P_NK_\alpha P_N\) is regarded as an operator on \(P_N\ell^2\), which has dimension \(N\). Define
\[
a_j=\frac1{j+\alpha+1},\quad
g_j=a_j-a_{j+1}=\frac1{(j+\alpha+1)(j+\alpha+2)},\quad
d_j=a_j^2-g_j=\frac1{(j+\alpha+1)^2(j+\alpha+2)}.
\]
All \(a_j,g_j,d_j\) are positive, \(a=(a_j)\in\ell^2\), and \(\sum_{j\ge0}(j+1)d_j<\infty\). A principal section always means the leading coordinate section, not an arbitrary selection of indices.

## Proof

**1. A positive trace-class operator minus one rank-one term.** Let \(v_k=e_0+\cdots+e_k\). Direct multiplication gives, for \(i,j\ge0\),
\[
(K_\alpha)_{ij}=\sum_{n\ge\max(i,j)}a_n^2-(\min(i,j)+1)a_i a_j.
\]
For \(i\le j\), the telescoping identity \(\sum_{n\ge j}g_n=a_j\) yields
\[
(K_\alpha)_{ij}
 =\sum_{n\ge j}(a_n^2-g_n)+\alpha a_i a_j
 =\sum_{n\ge j}d_n+\alpha a_i a_j.
\]
The same formula with \(\max(i,j)\) holds for every pair. Since the rank-one positive terms have summable traces, the operator identity is valid in trace norm:
\[
\boxed{K_\alpha=H_\alpha+\alpha aa^*,\qquad
H_\alpha=\sum_{k\ge0}d_k v_kv_k^*.}
\]
In particular, \(H_\alpha\ge0\) and \(K_\alpha\) is trace class. For \(\alpha\ge0\), positivity follows. For \(\alpha<0\), subtraction of one positive rank-one operator gives \(\operatorname{ind}_-(K_\alpha)\le1\) by the elementary codimension-one min-max argument.

**2. Exact finite-dimensional rank-one test.** Take \(x\in P_N\ell^2\). Its partial sums \(t_k=\sum_{i=0}^{k}x_i\) are independent of \(k\) for all \(k\ge N-1\), with common value \(c\). The telescoping identity \(\sum_{k\ge i}g_k=a_i\) also gives \(\langle a,x\rangle=\sum_{k\ge0}g_k t_k\). Put \(D_{N-1}=\sum_{k\ge N-1}d_k>0\). Then
\[
\langle H_\alpha x,x\rangle=
\sum_{k=0}^{N-2}d_k|t_k|^2+D_{N-1}|c|^2,
\]
\[
\langle a,x\rangle=
\sum_{k=0}^{N-2}g_k t_k+a_{N-1}c.
\]
The change of variables \(x\mapsto(t_0,\ldots,t_{N-2},c)\) is invertible, so the positive form is strictly positive on \(P_N\ell^2\). Weighted Cauchy–Schwarz, with equality at the inverse-diagonal-weight multiple of the displayed linear functional, gives its exact norm squared:
\[
\sup_{x\in P_N\ell^2\setminus\{0\}}
\frac{|\langle a,x\rangle|^2}{\langle H_\alpha x,x\rangle}
=\sum_{k=0}^{N-2}\frac{g_k^2}{d_k}+\frac{a_{N-1}^2}{D_{N-1}}
=\sum_{k=0}^{N-2}\frac1{k+\alpha+2}
+\frac{1}{(N+\alpha)^2 D_{N-1}}.
\]
Hence \(P_NK_\alpha P_N=P_NH_\alpha P_N-\varepsilon(P_Na)(P_Na)^*\) is positive definite, positive semidefinite with a one-dimensional nullspace, or has exactly one negative eigenvalue, according as \(\varepsilon\) times the last maximum is less than, equal to, or greater than one. This uses the exact full infinite tail of the positive form, not a truncated approximation.

**3. Identification by special functions.** Write \(z=N+\alpha>0\). The elementary partial fraction identity
\[
\frac1{u^2(u+1)}=\frac1{u^2}-\frac1u+\frac1{u+1}
\]
gives
\[
D_{N-1}=\sum_{k=0}^{\infty}\frac{1}{(z+k)^2(z+k+1)}
=\psi_1(z)-\frac1z>0.
\]
The recurrence \(\psi(w+1)-\psi(w)=1/w\) gives
\[
\sum_{k=0}^{N-2}\frac1{k+\alpha+2}
=\psi(N+\alpha+1)-\psi(\alpha+2).
\]
This proves the displayed formula for \(\mathcal S_N\) and the exact inertia criterion.

**4. Strict increase and attainment of the first cutoff.** The maximizing ratio in Step 2 is the squared dual norm of the linear functional \(x\mapsto\langle a,x\rangle\) for the positive form \(H_\alpha\), restricted to the nested coordinate spaces \(P_N\ell^2\). Hence \(\mathcal S_N\) is nondecreasing. It is strictly increasing because splitting the tail block \(\{k\ge N-1\}\) into its first coordinate and its remaining tail makes the weighted Cauchy–Schwarz bound strictly larger: equality in the unsplit tail would require the ratio \(g_k/d_k=k+\alpha+1\) to be constant throughout the tail, which is false. The harmonic term forces \(\mathcal S_N\to\infty\). For \(-1<\alpha<0\) there is a negative principal section and therefore \(\operatorname{ind}_-(K_\alpha)=1\); compactness from Step 1 guarantees this negative direction is an eigenvalue.

**5. Sharp singularity of the first detection size.** Put \(\alpha=-\varepsilon\). For \(\varepsilon\in(0,1/2)\) and \(N\to\infty\), the standard expansion of the trigamma series, uniformly in that parameter range, is
\[
\psi_1(N-\varepsilon)=\frac1{N-\varepsilon}
+\frac1{2(N-\varepsilon)^2}+O(N^{-3}).
\]
Thus the reciprocal tail term is \(2+O(N^{-1})\). The digamma expansion is \(\psi(N+1-\varepsilon)=\log N+O(N^{-1})\). Consequently,
\[
\mathcal S_N(-\varepsilon)
=\log N+2-\psi(2-\varepsilon)+O(N^{-1}),
\]
with an error uniform for \(0<\varepsilon<1/2\). Define \(N_*(\varepsilon)\) by the strict threshold. The harmonic growth shows \(N_*(\varepsilon)\to\infty\). Apply the previous expansion at \(N_*(\varepsilon)\) and at the preceding integer. Their threshold values straddle \(1/\varepsilon\); the difference between the corresponding scalar values tends to zero (indeed it is \(O(1/N_*)\)). Therefore
\[
\log N_*(\varepsilon)-\frac1\varepsilon
=\psi(2-\varepsilon)-2+o(1)
= -1-\gamma+o(1),
\]
using \(\psi(2)=1-\gamma\). Exponentiation proves the sharp limit. No finite numerics are used to infer it.

**6. Exact comparison with the known explicit witness.** The vector \(u_L\) displayed in the finding has cumulative-sum coordinates \(t_i=i+\alpha+1\) for \(0\le i<L\) and \(t_i=0\) afterward. Inserting them into the trace-norm rank-one decomposition gives exactly
\[
\langle K_\alpha u_L,u_L\rangle=B_L(\alpha)(1+\alpha B_L(\alpha)),
\quad B_L(\alpha)=\sum_{i=0}^{L-1}\frac1{i+\alpha+2}.
\]
Thus the first negative witness size is \(L_*(\varepsilon)=\min\{L:\varepsilon B_L(-\varepsilon)>1\}\). The digamma identity \(B_L(-\varepsilon)=\psi(L+2-\varepsilon)-\psi(2-\varepsilon)\) shows, by the same two-sided first-crossing argument, that \(\log L_*(\varepsilon)-1/\varepsilon\to\psi(2)=1-\gamma\). Comparing with Step 5 gives the asserted exact ratio \(e^2\). The difference is between a preselected sparse inverse-image witness and the optimal arbitrary vector in the first \(N\) coordinate space; it does not alter the source's theorem.

No finite numerics are used to infer either limit.

## Verification

The standalone file `checker.py` uses only Python's standard library and checks the exact finite-difference Gram identity in 294 rational cases, exact zero-total-vector quadratic forms in 144 cases, and six rigorous rational interval signs around three low-dimensional thresholds. It reports **444 finite exact-rational assertions**. For each finite sign test it encloses the entire positive infinite tail with a rational integral majorant, so no truncated sum is silently identified with the full tail. Reproduce using `python checker.py`.

The mathematical proof of the all-integer inertia criterion, unique negative index, and \(\varepsilon\downarrow0\) limit is Steps 1–5. The checker tests normalization and selected finite consequences only. Numerical diagonalizations and a few sample thresholds cannot establish these infinite assertions. Illustrative exact finite-cutoff outcomes are \(N_*(1/2)=2\) and \(N_*(1/4)=10\); their rigorous rational decisions are included in the checker.

## Relationship to prior work

Ma [1] proves hyponormality of the same operator family exactly for nonnegative shifts and proves failure for negative shifts by constructing finitely supported vectors. In its Section 7, the negative quadratic form is asymptotic to a negative multiple of \((\log N)^2\) for a particular witness; this is explicitly prior work, not a new claim. The result here instead determines the **least size of an arbitrary leading coordinate compression** with negative spectrum, including the nontrivial infinite-tail contribution, the exact digamma–trigamma threshold, and the prefactor in the exponential divergence of that minimal size. A sparse preselected witness need not give the earliest negative section; the optimization over the entire first \(N\) coordinates in Step 2 is essential.

The published finite Gram reduction for shifted Cesàro self-commutators [2] computes a different relative lower-bound optimization and identifies \(-\infty\) for its normalized negative-shift Rayleigh quotient; it does not compute the least negative principal compression. The published trace identity [3] determines trace-class membership and the shift-independent total trace, but does not imply a finite detection threshold. The known qualitative order-one and order-two literature [4] discusses hyponormality and posinormality without providing this finite-section critical scale in the materials inspected. The explicit witness in [1] is recovered exactly in Step 6, but its sharp onset is later by a factor tending to \(e^2\) than the fully optimized coordinate-section onset. No comprehensive guarantee against an unindexed classical equivalent is asserted.

## Limitations

The exact criterion is for the **order-one** generalized Cesàro matrix on \(\ell^2\), with leading coordinate compressions of the **full self-commutator**. It does not classify nonleading index sets, the commutator of a finite matrix compression, higher-order generalized Cesàro matrices, or the magnitude of the unique negative eigenvalue. The exponential prefactor applies only as the negative shift approaches zero. The existence and position of the full hyponormality boundary, the general defect method, and the particular large-support negativity witness belong to Ma [1]. Originality is a best-knowledge literature comparison; independent mathematical assessment and publication-priority verification have not been performed.

## References

1. Y. Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1 (first publicly submitted 2026-09-18), especially Sections 1, 2, and 7. https://arxiv.org/html/2610.00193v1
2. *Finite Gram reduction of sharp Cesàro self-commutator bounds at every order*, published-finding corpus published mathematical record, 2026-10-11, identifier `2026/10/11/SCOPE-finite-gram-reduction-of-sharp-ces-ro-self-commutator-bounds-at--2747cc29070a`.
3. *A shift-invariant harmonic trace for generalized Cesàro self-commutators*, published-finding corpus published mathematical record, 2026-10-11, identifier `2026/10/11/SCOPE-a-shift-invariant-harmonic-trace-for-generalized-ces-ro-self-com--b9745d36b9d7`.
4. H. C. Rhaly Jr., *Supraposinormality and hyponormality for the generalized Cesàro matrices of order two*, arXiv:1602.01408 (2016), and *Hyponormality-Preserving Finite Rank Perturbations of Terraced Matrices*, Journal of the Nigerian Mathematical Society (2013). These address different qualitative or perturbative questions; only the abstracts were accessed for these two sources.
