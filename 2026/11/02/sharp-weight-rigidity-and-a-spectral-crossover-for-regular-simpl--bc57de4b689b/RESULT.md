# Sharp weight rigidity and a spectral crossover for regular-simplex midpoint frames

## Finding
Let \(m\ge4\) be an integer. The \(N=m(m+1)/2\) normalized edge-midpoint vectors of a regular simplex in real Euclidean \(m\)-space form the Parseval frame \(V_m=(v_e)\) described below. Set \(G_m=(|\langle v_e,v_f\rangle|)_{e,f}\). Its complete spectrum, including multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\Lambda_m=\dfrac{4(m-2)}{m+1}&1\\[2mm]
\Theta_m=\dfrac{(m-3)(m-5)}{m^2-1}&m\\[2mm]
\Nu_m=\dfrac8{m^2-1}&N-m-1.
\end{array}
\]
At \(m=7\), the last two eigenvalues coincide; their multiplicities must then be combined. The top eigenvalue is simple for all \(m\ge4\). For any nonnegative weights \(t_e\) with \(\sum_e t_e^2=1\), the following **global sharp stability inequality** holds:
\[
\boxed{\Lambda_m-\sum_{e,f}t_et_f|\langle v_e,v_f\rangle|
\ \ge\ \gamma_m\left(1-\frac{(\sum_e t_e)^2}{N}\right),\qquad
\gamma_m=\begin{cases}
\dfrac{4m(m-3)}{m^2-1},&4\le m\le7,\\[2mm]
\dfrac{3m-7}{m-1},&m\ge8.
\end{cases}}
\]
The coefficient \(\gamma_m\) cannot be increased, even when all weights are strictly positive. Equality at the maximal projection-frame value \(\Lambda_m\) occurs only at the uniform weights \(t_e=N^{-1/2}\). The identity of the least-stable perturbation changes from the \(-2\) eigenspace of the triangular-graph adjacency operator to its \(m-3\) eigenspace between dimensions seven and eight. For \(m=7\), the displayed inequality is an equality for **every** admissible weight vector.

## Assumptions and scope
Take \(n=m+1\) unit regular-simplex vertices \(w_1,\ldots,w_n\in\mathbb R^m\) satisfying \(\sum_iw_i=0\) and \(\langle w_i,w_j\rangle=-1/m\) for distinct indices. Let \(\mathcal E=\{\{i,j\}:1\le i<j\le n\}\), so \(|\mathcal E|=N\). Define the real Parseval edge-midpoint frame by
\[
v_{\{i,j\}}=\sqrt{\frac{m}{N}}\,\frac{w_i+w_j}{\sqrt{2(m-1)/m}}.
\]
All norms and inner products of the frame vectors in the statement are Euclidean, and \(t\) is any member of the nonnegative Euclidean unit sphere in \(\mathbb R^N\). The scalar function on the left is the frame-weight objective appearing in the standard extremal characterization of relative projection constants; for this frame, its supremum is \(\Lambda_m\) [1]. The estimate does **not** claim that this frame maximizes the projection constant among all frames in dimension \(m\).

## Proof
**Step 1: Gram entries and Parseval normalization.** For every edge, \(\|w_i+w_j\|^2=2(m-1)/m\). For two distinct edges sharing one vertex, the unnormalized midpoint inner product equals \(1-3/m\); for disjoint edges, it equals \(-4/m\). Thus the entries of the absolute Gram matrix \(G_m\) have exactly three values:
\[
a=\frac2{m+1}\quad\text{(same edge)},\qquad
b=\frac{m-3}{m^2-1}\quad\text{(one common vertex)},\qquad
c=\frac4{m^2-1}\quad\text{(disjoint)}.
\]
Since \(\sum_i w_iw_i^\top=(m+1)I/m\), we have
\[
\sum_{i<j}(w_i+w_j)(w_i+w_j)^\top
=(m-1)\sum_i w_iw_i^\top.
\]
The displayed normalization therefore gives \(\sum_e v_ev_e^\top=I\): this is a Parseval frame.

**Step 2: the triangular-graph spectrum.** Write \(A\) for the adjacency matrix of the line graph of the complete graph on \(n\) vertices (two edges adjacent when they share exactly one vertex) and \(J\) for the \(N\times N\) all-ones matrix. Directly from Step 1,
\[
G_m=(a-c)I+(b-c)A+cJ.
\]
Let \(Q\) be the unsigned \(n\times N\) vertex-edge incidence matrix. Then \(Q^\top Q=2I+A\), while \(QQ^\top=(n-2)I+J_n\). Since \(n\ge5\), the latter matrix has eigenvalues \(2(n-1)\) once and \(n-2\) with multiplicity \(n-1\), and has full rank \(n\). It follows that \(A\) has eigenvalues \(2(n-2)\) on the constant vector, \(n-4\) with multiplicity \(n-1\), and \(-2\) with multiplicity \(N-n\). Since \(J\) vanishes on the orthogonal complement of the constant vector, substitution gives exactly \(\Lambda_m,\Theta_m,\Nu_m\) with the stated multiplicities.

**Step 3: compute the sharp gap.** A direct subtraction yields
\[
\Lambda_m-\Theta_m=\frac{3m-7}{m-1}>0,\quad
\Lambda_m-\Nu_m=\frac{4m(m-3)}{m^2-1}>0,\quad
\Theta_m-\Nu_m=\frac{m-7}{m+1}.
\]
Consequently the largest nonprincipal eigenvalue is \(\Mu_m=\max\{\Theta_m,\Nu_m\}\), and \(\gamma_m=\Lambda_m-\Mu_m\), giving the piecewise formula. The top eigenspace is precisely the one-dimensional span of the all-ones vector.

**Step 4: a global inequality, including sharpness and equality cases.** Put \(u=N^{-1/2}\mathbf1\), and decompose any admissible weight vector as \(t=hu+z\), where \(h=\langle t,u\rangle=(\sum_e t_e)/\sqrt N\), \(z\perp u\), and \(h^2+\|z\|_2^2=1\). By Step 3,
\[
t^\top G_mt=\Lambda_mh^2+z^\top G_mz
\le\Lambda_mh^2+\Mu_m\|z\|_2^2
=\Lambda_m-\gamma_m(1-h^2),
\]
which proves the inequality. If \(t\) attains \(\Lambda_m\), then \(z=0\); the nonnegative condition forces \(t=u\).

To show \(\gamma_m\) is the **best** coefficient within the nonnegative cone, take any nonzero real eigenvector \(z\perp u\) corresponding to \(\Mu_m\). For every sufficiently small nonzero \(\varepsilon\), all entries of \(u+\varepsilon z\) remain strictly positive. The normalized vector \(t_\varepsilon=(u+\varepsilon z)/\|u+\varepsilon z\|_2\) makes the spectral inequality an equality, with a strictly positive angular defect. When \(m\le7\), such an eigenvector can be chosen as an alternating four-edge cycle (the signed cycle lies in \(\ker Q\)); when \(m\ge8\), take \(z=Q^\top(e_1-e_2)\). At \(m=7\) all nonconstant eigenvalues coincide, so every weight vector attains equality in the stability inequality (though only the uniform vector maximizes the frame objective).

## Verification
The accompanying dependency-free `checker.py` constructs the exact integer-scaled Gram matrices \((m^2-1)G_m\) from edge incidences for every \(4\le m\le18\). It checks the two incidence identities, constant row sums, the first two trace moments of the claimed spectrum, strict top-eigenvalue separation, the dimension-seven crossover, and explicit nonnegative equality witnesses. In dimensions \(4\le m\le11\), it also checks the exact annihilating polynomial of degree three. Run `python3 checker.py`; the observed output was `PASS: 262333 exact-integer assertions, m=4,...,18`. The proof for **all** integers \(m\ge4\) is Step 2's general incidence argument, not this finite computation.

## Relationship to prior work
Deregowska and Lewandowska [1, Example 2.1 and Corollary 2.1] introduced the Parseval edge-midpoint configuration in this projection-constant setting, verified the biangular Gram entries, and proved the **unperturbed** value \(\Lambda_m=4(m-2)/(m+1)\). Their Lemma 2.1 establishes equality of the relative and equal-weight frame values for biangular tight frames. The present theorem adds the entire absolute-Gram spectral decomposition and the **globally optimal quantitative loss** for every nonuniform weight, including the change of least-stable eigenspace at dimension seven. It does not re-claim the known optimal value itself. Kumar, Mohar, Mojallal, and Pragada [2] prove stabilization of the *ambient-dimension sequence* of maximal projection constants, which is a different stability assertion and gives no coefficient for weight perturbations of this fixed frame. Graph eigenvalue bounds related to projection constants [3] have different quantified objects. Standard triangular-graph eigenvalues are used transparently in Step 2, but they do not by themselves state the sharp frame-weight stability theorem.

## Limitations
This is a statement about the **fixed regular-simplex midpoint Parseval frame** rather than all optimal frames or all Banach-space projections. No stability estimate is asserted when the frame vectors themselves are perturbed. The excluded case \(m=3\) has a repeated top absolute-Gram eigenvalue and does not have positive rigidity gap. The result does not resolve the conjectured global maximal projection constants in dimensions six and eight [1]. Although the relevant primary statements were compared, an older equivalent formulation via triangular graphs, spectral optimization, or frame perturbation remains a publication-priority risk. Independent audit has not been performed.

## References
[1] B. Deregowska and B. Lewandowska, *Maximal Projection Constants and Extremal Vector Configurations: Some Conjectures and Examples*, arXiv:2608.08695 (first public version, 9 August 2026), especially §2, Example 2.1 and Lemma 2.1; https://arxiv.org/html/2608.08695.

[2] H. Kumar, B. Mohar, S. A. Mojallal, and S. Pragada, *Stability of maximal relative projection constants*, arXiv:2609.03200 (2 September 2026); https://arxiv.org/abs/2609.03200.

[3] V. Sivashankar, Q. Tang, and T. Wakhare, *Graph Eigenvalues and Projection Constants*, arXiv:2608.02429 (3 August 2026); https://arxiv.org/abs/2608.02429. Its available abstract and summaries concern extremal graph-eigenvalue and projection-constant bounds, not fixed-frame weight stability.
