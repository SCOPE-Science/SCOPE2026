# A shift-invariant harmonic trace for generalized Cesàro self-commutators

## Finding

Let \(m\geq 1\) be an integer and \(\alpha>-1\) real. On \(\ell^2(\mathbb N_0)\), let \(M_{\alpha,m}\) be the generalized Cesàro matrix defined below and set its self-commutator \(D_{\alpha,m}=M_{\alpha,m}^*M_{\alpha,m}-M_{\alpha,m}M_{\alpha,m}^*\). Then \(D_{\alpha,m}\) is trace class for **every** such \(m\) and \(\alpha\), and

\[
\boxed{\operatorname{Tr}D_{\alpha,m}=\frac{m^2}{2m-1}\sum_{k=1}^{2m-1}\frac1k.}
\]

The trace is independent of \(\alpha\), even across the transition from hyponormality to nonhyponormality. Moreover, using the established hyponormality classification of Ma,

\[
\|D_{\alpha,m}\|_{\mathcal S_1}=\operatorname{Tr}D_{\alpha,m}\ \Longleftrightarrow\ \alpha\geq 0,
\]

and the trace norm is strictly larger than this displayed trace for \(-1<\alpha<0\). The common trace grows as \(\frac m2\log(2m)+O(m)\) as \(m\to\infty\).

## Assumptions and scope

Indices range over \(n,j\in\mathbb N_0\). For any \(z\) and nonnegative integer \(k\), write \((z)_k=\prod_{r=0}^{k-1}(z+r)\), with \((z)_0=1\). Fix an integer \(m\geq1\) and a real \(\alpha>-1\), and let

\[
(M_{\alpha,m})_{nj}=\begin{cases}\displaystyle\frac{m(n-j+1)_{m-1}}{(n+\alpha+1)_m},&0\leq j\leq n,\\[3pt]0,&j>n.\end{cases}
\]

All operators and traces are on complex \(\ell^2(\mathbb N_0)\), with its standard orthonormal basis. Boundedness for this complete range of parameters is established in Ma [1, Theorem 1.1]; alternatively the entries obey a uniform bound \(C_{\alpha,m}/(n+1)\) and the weighted Schur test applies. Trace class means membership in the Schatten ideal \(\mathcal S_1\). The positivity of the unshifted self-commutator comes from the diagonal interrupter identity of Le–Rhaly [2]. No positivity is assumed when \(\alpha<0\).

## Proof

**1. An existing positivity identity.** Put \(A=M_{0,m}\). Le–Rhaly [2, Theorem 2.1] proved the diagonal interrupter identity

\[
AA^*=A^*P_m A,\qquad P_m=\operatorname{diag}\left(\frac{(n+1)_m}{(n+m+1)_m}\right)_{n\geq0}.
\]

Every diagonal entry of \(P_m\) belongs to \((0,1)\). Therefore \(D_0=A^*A-AA^*=A^*(I-P_m)A\geq0\). The subscript \(0\) in this proof means \(\alpha=0\) with \(m\) fixed.

**2. Exact finite-compression flux.** Let \(E_N\) be the orthogonal projection onto the first \(N+1\) coordinate vectors. For every integer \(N\geq0\), boundedness of \(A\), triangularity, and finite cancellation give

\[
\operatorname{Tr}(E_ND_0E_N)=\sum_{j=0}^N\sum_{n=N+1}^{\infty}|A_{nj}|^2=:F_N.
\]

Indeed \(\sum_{j=0}^N\langle A^*Ae_j,e_j\rangle\) sums over all output indices \(n\geq j\), whereas \(\sum_{j=0}^N\langle AA^*e_j,e_j\rangle\) sums only the pairs \(0\leq j\leq N\), \(0\leq k\leq j\); the internal square entries coincide and cancel. The remaining sum is nonnegative. All its terms converge because each column of a bounded operator is square summable.

**3. Limiting boundary flux.** Fix \(R>1\). Uniformly when \(1\leq u\leq R\), \(0\leq v\leq1\), and integer \(n,j\) obey \(n/N\to u\), \(j/N\to v\), we have, for \(N\to\infty\),

\[
N A_{nj}\longrightarrow \frac{m}{u}\left(1-\frac vu\right)^{m-1}.
\]

The convergence is uniform on the compact rectangle, since the numerator and denominator are fixed-degree polynomial products with denominators uniformly bounded away from zero after scaling. Thus the portion of \(F_N\) with \(N<n\leq RN\) converges by two-dimensional Riemann sums to

\[
m^2\int_1^R\int_0^1\frac{(1-v/u)^{2m-2}}{u^2}\,dv\,du.
\]

For the omitted tail note that, for all \(n\geq1\) and \(0\leq j\leq n\), the entry has the bound \(0\leq A_{nj}\leq C_m/(n+1)\). Consequently,

\[
0\leq\sum_{n>RN}\sum_{j=0}^N|A_{nj}|^2\leq C_m^2(N+1)\sum_{n>RN}(n+1)^{-2}=O_m(R^{-1}),
\]

uniformly in \(N\geq1\) when \(R>1\). Passing first to the \(N\)-limit and then to \(R\to\infty\), followed by \(w=1/u\), shows

\[
\lim_{N\to\infty}F_N=m^2\int_0^1\int_0^1(1-vw)^{2m-2}\,dv\,dw.
\]

For each nonnegative integer \(p\), elementary integration yields

\[
\begin{aligned}
\int_0^1\int_0^1(1-vw)^p\,dv\,dw
&=\frac{1}{p+1}\int_0^1\frac{1-(1-w)^{p+1}}w\,dw\\
&=\frac{1}{p+1}\sum_{k=1}^{p+1}\frac1k.
\end{aligned}
\]

Substituting \(p=2m-2\) gives the claimed harmonic number. Since \(D_0\geq0\), finiteness of \(\lim_N\operatorname{Tr}(E_ND_0E_N)\) proves \(D_0\in\mathcal S_1\) and computes its trace by the standard characterization of trace-class positive operators through increasing finite-coordinate compressions. This is a genuine infinite-dimensional conclusion, not a finite truncation heuristic.

**4. Trace-class invariance under parameter shifts.** For a fixed \(\alpha>-1\) set \(K=M_{\alpha,m}-A\). For \(n\) sufficiently large, differentiation of the reciprocal product \(s\mapsto(n+s+1)_m^{-1}\) on the compact segment joining \(0\) to \(\alpha\) gives

\[
\left|\frac1{(n+\alpha+1)_m}-\frac1{(n+1)_m}\right|\leq C_{m,\alpha}(n+1)^{-m-1}.
\]

As \((n-j+1)_{m-1}\leq C_m(n+1)^{m-1}\), we obtain \(|K_{nj}|\leq C_{m,\alpha}(n+1)^{-2}\) for \(0\leq j\leq n\) and all sufficiently large \(n\); finitely many early rows cause no difficulty. Hence the row norms satisfy \(\|K^*e_n\|_2\leq C_{m,\alpha}(n+1)^{-3/2}\) in the tail, and

\[
\|K\|_{\mathcal S_1}\leq\sum_{n=0}^{\infty}\|K^*e_n\|_2<\infty.
\]

The inequality follows by expressing \(K\) as the trace-norm convergent sum of rank-one operators corresponding to its rows. Expand the difference of self-commutators:

\[
D_{\alpha,m}-D_0=A^*K+K^*A+K^*K-AK^*-KA^*-KK^*.
\]

Every term on the right is trace class. Cyclicity of the trace for a trace-class factor and a bounded factor gives \(\operatorname{Tr}(A^*K)=\operatorname{Tr}(KA^*)\), \(\operatorname{Tr}(K^*A)=\operatorname{Tr}(AK^*)\), and \(\operatorname{Tr}(K^*K)=\operatorname{Tr}(KK^*)\). Therefore \(D_{\alpha,m}\in\mathcal S_1\) and \(\operatorname{Tr}D_{\alpha,m}=\operatorname{Tr}D_0\).

**5. Trace-norm phase boundary.** Ma [1, Theorem 1.1] proved that \(D_{\alpha,m}\geq0\) exactly when \(\alpha\geq0\). For any self-adjoint trace-class operator \(D\), \(\|D\|_{\mathcal S_1}-\operatorname{Tr}D=2\operatorname{Tr}(D_-)\), where \(D_-\) is its negative part. Thus equality holds precisely for \(\alpha\geq0\) and the inequality is strict throughout \(-1<\alpha<0\). Finally, \(\sum_{k=1}^{2m-1}1/k=\log(2m)+O(1)\) and \(m^2/(2m-1)=m/2+O(1)\), proving the growth statement.

## Verification

Exact small-order cases are \(\operatorname{Tr}D_{\alpha,1}=1\), \(\operatorname{Tr}D_{\alpha,2}=22/9\), \(\operatorname{Tr}D_{\alpha,3}=411/100\), and \(\operatorname{Tr}D_{\alpha,4}=1452/245\), for every \(\alpha>-1\). These follow by direct rational evaluation of the harmonic formula. The finite-compression computation and tail bound are uniform in the cutoff, and the trace-class perturbation estimate handles each fixed shift without requiring positivity there.

For perspective, \(M_{\alpha,m}\) itself is not Hilbert–Schmidt: its squared row norm is asymptotic to \(m^2/((2m-1)n)\) as \(n\to\infty\), by the same Riemann-sum scaling, so the sum of all squared entries diverges. This emphasizes that trace-class regularity is a property of the self-commutator, not of the underlying matrix.

## Relationship to prior work

Ma [1] defines the same two-parameter family and proves the complete hyponormality boundary and quantitative lower bounds; it does not give a trace-class classification or the exact self-commutator trace. Le–Rhaly [2] supplies the all-order diagonal interrupter and positive unshifted defect used as an input here, without a harmonic trace formula or shifted trace invariance. Rhaly's earlier finite-order studies [3] focus on posinormality and hyponormality. A distinct published study of trace-class Mellin-semigroup product defects for Cesàro kernels concerns differences between compositions of operators, rather than the adjoint self-commutator of the present single matrix family. The present theorem computes a new natural operator-ideal invariant and locates its exact trace-norm equality boundary.

## Limitations

The result is specific to integer orders and the explicitly defined shifted generalized Cesàro matrices on \(\ell^2\); no extension to arbitrary fractional orders or other sequence-space norms is asserted. The exact trace norm for \(-1<\alpha<0\) is not computed, only shown strictly above the universal trace. No lower bound on the negative trace mass is claimed. The positivity classification is borrowed from [1], not reproved here; the diagonal identity is borrowed from [2]. The absence of a matching statement in surveyed literature is not proof against unindexed or implicit prior formulations.

## References

[1] Y. Ma, *Hyponormality of generalized Cesàro matrices of every positive integer order*, arXiv:2610.00193v1, first posted 2026-09-18. https://arxiv.org/html/2610.00193v1

[2] T. Le and H. C. Rhaly Jr., *Coposinormality of the Cesàro matrices*, Archiv der Mathematik 110 (2018), 167–173. DOI:10.1007/s00013-017-1128-y. Author-supplied full text: https://www.researchgate.net/publication/321673225_Coposinormality_of_the_Cesaro_matrices

[3] H. C. Rhaly Jr., *A conjecture on hyponormality for the Cesàro matrix of positive integer order*, arXiv:1701.00425 (2017). https://arxiv.org/abs/1701.00425
