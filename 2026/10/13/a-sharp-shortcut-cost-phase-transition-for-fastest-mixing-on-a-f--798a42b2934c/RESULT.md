# A sharp shortcut-cost phase transition for fastest mixing on a four-vertex cycle

## Finding

For a four-vertex cycle, assign nonnegative symmetric transition rates \(q,a,r,b\) to edges \((0,1),(1,2),(2,3),(3,0)\), respectively. Fix a relative cost \(t>0\) for edge \((0,1)\), while the other three edges have unit cost, and impose the budget \(tq+a+r+b=1\). Let \(L(q,a,r,b)\) be the weighted combinatorial Laplacian. Write \(\lambda_2(L)\) for its second-smallest eigenvalue, including multiplicity.

**Theorem.** The exact optimal mixing rate over all feasible rates is
\[
\max_{\substack{q,a,r,b\ge0\\tq+a+r+b=1}}\lambda_2(L)=
\begin{cases}
\displaystyle\frac{4}{t+2\sqrt t+5},&0<t\le9,\\[4pt]
\displaystyle\frac15,&t\ge9.
\end{cases}
\]
More precisely:

- If \(0<t<9\), put \(h=\sqrt t\) and \(D=h^2+2h+5\). The **unique** optimum is
\[
(q,a,r,b)=\left(\frac{h+1}{hD},\frac2D,\frac{h+1}{D},\frac2D\right).
\]
The optimum assigns positive rate to all four edges, and its spectral gap has multiplicity two.

- If \(t=9\), the complete set of optima is the nontrivial line segment
\[
(q,a,r,b)=\left(s,\frac3{10}-3s,\frac25-3s,\frac3{10}-3s\right),
\qquad 0\le s\le\frac1{15}.
\]
For \(s<1/15\) the spectral gap is simple; at \(s=1/15\) it is double.

- If \(t>9\), the **unique** optimum is
\[
(q,a,r,b)=\left(0,\frac3{10},\frac25,\frac3{10}\right).
\]
Thus the costly shortcut is unused exactly on the high-cost side of the transition. Its removal does not break connectivity, because the remaining three edges form a path.

## Assumptions and scope

The four vertices are labeled in cyclic order \(0,1,2,3\). Edge rates may vanish, but must be nonnegative and satisfy the displayed equality budget. The matrix \(L\) is real symmetric, with off-diagonal entry \(-w_{ij}\) for an edge and diagonal entry equal to the sum of incident rates. Its spectrum is ordered as \(0=\lambda_1(L)\le\lambda_2(L)\le\lambda_3(L)\le\lambda_4(L)\). The associated continuous-time symmetric Markov generator is \(-L\), so \(\lambda_2(L)\) controls its asymptotic relaxation rate when the positively weighted subgraph is connected. No claim is made about nonsymmetric chains, arbitrary cost vectors, or cycles of other lengths. The normalization of the budget to one is harmless by the common scaling of all rates.

## Proof

### A sharp upper bound when \(0<t\le9\)

Write \(h=\sqrt t\in(0,3]\). Consider the two nonconstant vectors
\[
u=(1,1,-1,-1)^{\mathsf T},\qquad
v=(h,-h,-1,1)^{\mathsf T}.
\]
Both are perpendicular to the constant vector, and \(u^{\mathsf T}v=0\). Their squared norms are \(4\) and \(2(h^2+1)\). By the edge-energy identity \(z^{\mathsf T}Lz=\sum_{ij}w_{ij}(z_i-z_j)^2\),
\[
u^{\mathsf T}Lu=4a+4b,
\qquad
v^{\mathsf T}Lv=4h^2q+(h-1)^2(a+b)+4r.
\]
Set
\[
\alpha=\frac{(3-h)(h+1)}{16}\ge0,
\qquad \beta=\frac14>0.
\]
For the four edges, the coefficients in \(\alpha u^{\mathsf T}Lu+\beta v^{\mathsf T}Lv\) are exactly \(h^2,1,1,1\), because \(4\alpha+(h-1)^2\beta=1\) and \(4\beta=1\). Consequently,
\[
\alpha u^{\mathsf T}Lu+\beta v^{\mathsf T}Lv
=h^2q+a+r+b=1.
\]
The variational definition of \(\lambda_2\) gives
\[
1\ge\lambda_2(L)\bigl(4\alpha+2(h^2+1)\beta\bigr)
=\lambda_2(L)\frac{h^2+2h+5}{4}.
\]
This is the asserted upper bound \(\lambda_2(L)\le4/D\), where \(D=h^2+2h+5\).

Now take
\[
q=\frac{h+1}{hD},\qquad a=b=\frac2D,\qquad r=\frac{h+1}{D}.
\]
They are positive and satisfy the cost budget because \(D=(h+1)^2+4\). Direct substitution into the four rows of \(L\) shows
\[
Lu=\frac4D u,\qquad Lv=\frac4D v.
\]
The remaining nonzero eigenvalue, obtained from the trace after accounting for the zero eigenvalue and the two copies of \(4/D\), is
\[
\lambda_4(L)=\frac{2(h+1)^2}{hD}>\frac4D.
\]
Thus the upper bound is attained, and the claimed spectral-gap multiplicity is correct.

If \(h<3\), both multipliers \(\alpha\) and \(\beta\) are strictly positive. Equality in the weighted sum of the two Rayleigh lower bounds forces **both** \(u\) and \(v\) to lie in the \(\lambda_2\)-eigenspace. The equation \(Lu=\lambda_2u\) first yields \(a=b=\lambda_2/2\). The equation \(Lv=\lambda_2v\) then yields \(q=\lambda_2(h+1)/(4h)\) and \(r=\lambda_2(h+1)/4\). Since \(\lambda_2=4/D\), these fix all four rates uniquely.

### The high-cost bound and equality cases

For every \(t\ge9\) use the fixed vector \(v_3=(3,-3,-1,1)^{\mathsf T}\), whose squared norm is \(20\). Its squared differences on the four edges, in the prescribed order, are \(36,4,4,4\). Every feasible rate vector therefore satisfies
\[
\lambda_2(L)\le\frac{v_3^{\mathsf T}Lv_3}{20}
=\frac{36q+4(a+r+b)}{20}
=\frac15-\frac{t-9}{5}q\le\frac15.
\]
For \(t>9\), equality requires \(q=0\) and, by the equality case of the Rayleigh principle, \(Lv_3=(1/5)v_3\). The vertex equations give \(a=b=3/10\) and \(r=2/5\). This feasible vector has eigenvalues \(0,1/5,3/5,6/5\), so it attains the bound and is uniquely optimal.

At \(t=9\), equality still requires \(Lv_3=(1/5)v_3\), but no longer requires \(q=0\). Solving the four vertex equations gives exactly
\[
a=b=\frac3{10}-3q,
\qquad r=\frac25-3q.
\]
The budget is then an identity. Its Laplacian has **exactly** the eigenvalues
\[
0,\quad\frac15,\quad\frac35-6q,\quad\frac65-10q.
\]
For the second-smallest eigenvalue to equal the upper bound \(1/5\), both final values must be at least \(1/5\). Together with nonnegative rates, this is equivalent to \(0\le q\le1/15\). This proves that the displayed line segment is the full optimal set, and identifies the spectral-gap multiplicities, completing the proof.

## Verification

The accompanying Python 3 file `proof_check.py` uses only the standard library and exact `fractions.Fraction` arithmetic. Run `python3 proof_check.py`; the expected final line begins `VERIFY_OK`. The program independently reconstructs each Laplacian, budget, two explicit eigenvectors, and their conditional weights for twelve rational interior/boundary parameters; it checks forty-one rational points on the critical optimal segment and five values in the exterior region. For each reconstructed Laplacian it also compares the complete characteristic polynomial at five distinct rational arguments against the proposed factorization. Because both sides are monic quartics, these five evaluations prove the **specific rational-instance** characteristic-polynomial identities exactly. They do not constitute a proof over every real parameter; that is supplied by the analytic argument above.

The proof relies only on the universal Rayleigh variational principle and explicit finite-dimensional algebra. In particular, positivity on all parameter regimes and the boundary equality conditions do not depend on floating-point eigenvalue estimates.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis formulate rate-budget Laplacian eigenvalue optimization as a semidefinite program, give a general spectral/geometry duality, and solve the arbitrary-cost path problem (Result 5, Section 5.2). Their cycle discussion (Section 5.3) solves the equal-cost cycle and proves that an optimal cycle embedding may be taken in two dimensions. It explicitly treats arbitrary-cost cycles as more complicated; the specific four-cycle cost-dependent phase law, unique rate allocations on both sides, and critical continuum are not stated there. The equal-cost point \(t=1\) of the present theorem is a special case of that earlier result and is not individually claimed as new.

Boyd, Ghosh, Prabhakar, and Shah develop an optimization formulation for asynchronous randomized gossip on graphs, involving a different discrete-time averaging process. Shakeri and coauthors derive budget transitions for variable **interlayer** weights between fixed network layers; their model does not optimize the four conductances subject to one heterogeneous edge price. These broader formulations motivate the question but do not themselves state this sharp one-parameter classification.

## Limitations

This is a complete answer only for the described four-vertex cycle and one distinguished edge-cost parameter. The general variational and SDP mechanisms are known prior work. The novelty claim is the explicit cost threshold, full optimizer set, and associated multiplicity transition, not a new algorithm for solving generic semidefinite programs. An overlooked specialized treatment of four-cycle costs could duplicate this statement; the searches and inspected literature cannot exclude that possibility absolutely. No independent mathematical audit has been performed.

## References

1. S. Boyd, A. Ghosh, B. Prabhakar, and D. Shah, *Analysis and Optimization of Randomized Gossip Algorithms*, 43rd IEEE Conference on Decision and Control, December 14–17, 2004. Conference PDF: https://web.stanford.edu/~boyd/papers/pdf/gossip_opt.pdf.
2. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, doi:10.1137/S0036144504443821. Author PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf. In particular §§ 1, 5.2, 5.3.
3. H. Shakeri, N. Albin, F. D. Sahneh, P. Poggi-Corradini, and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785, initial public submission 2015-10-22. https://arxiv.org/pdf/1510.06785.
