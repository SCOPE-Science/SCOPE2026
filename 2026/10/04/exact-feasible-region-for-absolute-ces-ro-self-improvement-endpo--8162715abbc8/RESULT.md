# Exact feasible region for absolute Cesàro self-improvement endpoints
## Finding
Fix \(1\le p<\infty\). For a \(p\)-absolutely Cesàro bounded operator \(T\), write \(C_{{p,\mathrm{{ac}}}}(T)\) for the least constant in
\[
\frac1N\sum_{{k=0}}^{{N-1}}\lVert T^k x\rVert^p\le C_{{p,\mathrm{{ac}}}}(T)\lVert x\rVert^p
\]
and define
\[
q_*(T)=\sup\{{q\ge p:T\text{{ is }}q\text{{-absolutely Cesàro bounded}}\}.
\]
Then the exact feasible region of the pair \(\bigl(C_{{p,\mathrm{{ac}}}}(T),q_*(T)\bigr)\) is:

- if \(C_{{p,\mathrm{{ac}}}}(T)=1\), then \(q_*(T)=\infty\);
- if \(K>1\) and \(C_{{p,\mathrm{{ac}}}}(T)=K\), then necessarily \(q_*(T)\ge pK/(K-1)\);
- conversely, for every \(K>1\) and every \(Q\in[pK/(K-1),\infty]\), there is a positive operator \(T\) on \(\ell^p(\mathbb N)\) such that
\[
C_{{p,\mathrm{{ac}}}}(T)=K,\qquad q_*(T)=Q.
\]
Thus the universal lower endpoint from the focal self-improvement theorem is the only restriction: at fixed optimal Cesàro constant, every larger finite endpoint and the infinite endpoint occur already for positive operators on a classical sequence space.

## Assumptions and scope
All spaces and operators are real or complex as appropriate for the positive sequence-space models. The exponent satisfies \(1\le p<\infty\). The quantity \(q_*(T)\) records the supremal strong absolute-Cesàro exponent; endpoint membership itself is not encoded by the supremum. In the constructed finite-endpoint examples the endpoint \(Q\) is not attained.

The focal source proves that if \(C_{{p,\mathrm{{ac}}}}(T)=K>1\), then \(T\) is \(q\)-absolutely Cesàro bounded for every \(q<pK/(K-1)\), and it exhibits one positive weighted shift attaining that minimal possible supremum. It also exhibits a square-zero example with the same \(p\)-constant and infinite supremal exponent. The statement above classifies all intermediate feasible supremal exponents.

## Proof
If \(C_{{p,\mathrm{{ac}}}}(T)=1\), the focal theorem shows that \(T\) is a contraction. Hence \(\lVert T^k x\rVert\le\lVert x\rVert\) for every \(k\), so \(T\) is \(q\)-absolutely Cesàro bounded for every finite \(q\), and therefore \(q_*(T)=\infty\).

Now let \(K>1\). The focal self-improvement theorem immediately gives the necessary inequality
\[
q_*(T)\ge Q_0:=\frac{{pK}}{{K-1}}.
\]
It remains to realize every \(Q\in[Q_0,\infty]\).

First suppose \(Q<\infty\), and put
\[
\alpha=\frac1Q,\qquad \beta=\alpha p=\frac pQ,\qquad K_Q=\frac1{{1-\beta}}=\frac Q{{Q-p}}.
\]
Since \(Q\ge Q_0\), the decreasing function \(Q\mapsto Q/(Q-p)\) gives \(K_Q\le K\). On \(\ell^p(\mathbb N)\), define the positive weighted backward shift
\[
W_Qe_1=0,\qquad W_Qe_j=\left(\frac j{{j-1}}\right)^{{1/Q}}e_{{j-1}}\quad(j\ge2).
\]
The weighted-shift characterization used in the focal source gives
\[
C_{{p,\mathrm{{ac}}}}(W_Q)
=\sup_{{j\ge1}}j^{{\beta-1}}\sum_{{\ell=1}}^j\ell^{{-\beta}}
=\frac1{{1-\beta}}=K_Q.
\]
Applying the focal self-improvement theorem to \(W_Q\) yields \(q\)-absolute Cesàro boundedness for every \(q<Q\). At the endpoint, for the basis vector \(e_j\),
\[
\frac1j\sum_{{k=0}}^{{j-1}}\lVert W_Q^ke_j\rVert_p^Q
=\sum_{{\ell=1}}^j\frac1\ell\longrightarrow\infty.
\]
Thus \(W_Q\) is not \(Q\)-absolutely Cesàro bounded. By monotonicity in the exponent, it is not \(q\)-absolutely Cesàro bounded for any \(q\ge Q\), so \(q_*(W_Q)=Q\).

On two coordinates define the positive square-zero operator
\[
S_K(x_1,x_2)=((2K-1)^{{1/p}}x_2,0).
\]
Since \(S_K^2=0\), for every \(N\ge2\) only the first two orbit terms can contribute. The worst case is \(N=2\), and
\[
C_{{p,\mathrm{{ac}}}}(S_K)=\frac{{1+\lVert S_K\rVert^p}}2
=\frac{{1+(2K-1)}}2=K.
\]
Being nilpotent, \(S_K\) is \(q\)-absolutely Cesàro bounded for every finite \(q\), so \(q_*(S_K)=\infty\).

Let \(T=S_K\oplus W_Q\) on the \(\ell^p\)-sum of the two spaces, identified isometrically with \(\ell^p(\mathbb N)\). Because \(p\)-th powers add across an \(\ell^p\)-sum,
\[
C_{{p,\mathrm{{ac}}}}(T)=\max\{C_{{p,\mathrm{{ac}}}}(S_K),C_{{p,\mathrm{{ac}}}}(W_Q)\}=K.
\]
For every finite \(q\ge p\),
\[
(a^p+b^p)^{{q/p}}\le 2^{{q/p-1}}(a^q+b^q),
\]
so a finite direct sum of two \(q\)-absolutely Cesàro bounded operators is again \(q\)-absolutely Cesàro bounded. Hence \(T\) is \(q\)-absolutely Cesàro bounded for all \(q<Q\). Conversely, the invariant \(W_Q\)-summand shows that \(T\) fails \(Q\)-absolute Cesàro boundedness. Therefore \(q_*(T)=Q\).

For \(Q=\infty\), take \(S_K\) on the first two coordinates and zero on the remaining coordinates. This positive operator has optimal \(p\)-Cesàro constant \(K\) and is \(q\)-absolutely Cesàro bounded for every finite \(q\).

## Verification
The argument is symbolic. The lower boundary is exactly the published self-improvement threshold. The finite-endpoint construction uses the same weighted-shift family as the focal source but with parameter \(\beta=p/Q\); the endpoint failure is the divergent harmonic sum displayed above. The exact \(p\)-constant of the direct sum follows from additivity of \(p\)-th powers. The passage of \(q\)-absolute Cesàro boundedness through the two-summand direct sum is justified by the explicit finite-dimensional inequality above. No finite experiment is used to infer an infinite statement.

## Relationship to prior work
Arnold's 2026 focal paper proves the universal lower bound \(q_*(T)\ge pK/(K-1)\) and, in its discussion of \(q_*(T)\), gives two operators with the same \(p\)-Cesàro constant \(K\): an extremal weighted shift with \(q_*=pK/(K-1)\) and a square-zero operator with \(q_*=\infty\). The result here closes the gap between those two examples by determining the full attainable set at each fixed \(K\).

Abbar, Arnold and Coine characterize \(q\)-absolute Cesàro boundedness for weighted backward shifts and supply the weighted-shift calculation used by the focal paper. Their stated results do not classify the joint feasible region of the optimal \(p\)-Cesàro constant and the supremal self-improvement exponent. Earlier work of Cohen, Cuny, Eisner and Lin develops \(p\)-absolute Cesàro boundedness and power-growth estimates, but does not give this two-invariant realization classification.

## Limitations
The classification concerns the supremal exponent \(q_*(T)\), not whether absolute Cesàro boundedness holds at that endpoint. The finite-endpoint constructions deliberately fail at \(Q\). The realization uses direct sums of a nilpotent block and a weighted shift; it does not classify irreducible, invertible, or other restricted operator subclasses. An older equivalent realization observation under different notation remains a literature risk.

## References
1. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1, first public 24 September 2026.
2. A. Abbar, L. Arnold and C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1, first public 21 September 2026.
3. G. Cohen, C. Cuny, T. Eisner and M. Lin, *Resolvent conditions and growth of powers of operators*, Journal of Mathematical Analysis and Applications 487 (2020), Article 124035, DOI:10.1016/j.jmaa.2020.124035.
