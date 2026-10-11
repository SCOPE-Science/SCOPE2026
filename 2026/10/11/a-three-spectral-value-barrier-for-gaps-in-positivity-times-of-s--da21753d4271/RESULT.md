# A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups

## Finding
Let \(I\) be a finite or countably infinite index set, and consider the coordinatewise ordered real Hilbert space \(H=\ell^2(I;\mathbb R)\). For a bounded self-adjoint operator \(A\) on \(H\), put \(\mathcal P(A)=\{t\ge0:e^{tA}\text{ maps }H_+\text{ into }H_+\}\). Assume that the largest spectral value \(\lambda_1\) is simple, with normalized eigenvector \(v\) for which every coordinate \(v_i\) is strictly positive.

**Spectral-cardinality theorem.** If \(A\) has at most three distinct spectral values, then
\[
\mathcal P(A)=\{0\}\cup[\tau,\infty),\qquad \tau\in[0,\infty],
\]
where \([\infty,\infty)\) here means the empty set. Thus positivity cannot disappear at a later positive time once it has appeared. All finite cutoffs occur already in dimension three; a bounded three-spectral-value operator on a countable infinite-dimensional space can have \(\tau=\infty\). Four spectral values suffice to break this no-gap conclusion: an explicit symmetric matrix generator has \(\mathcal P(A)=\{0,1\}\cup[2,\infty)\).

## Assumptions and scope
The matrix of a positive operator relative to the standard basis is entrywise nonnegative, a condition equivalent to cone preservation even for countably infinite \(I\). Self-adjointness, a simple largest eigenvalue, and strictly positive coordinates of its eigenvector are essential hypotheses of the barrier theorem; no compactness of \(A\) or of its resolvent is assumed. The exponentials are bounded operators and form a norm-continuous semigroup. The theorem concerns operator positivity, not individual eventual positivity of positive initial vectors. All statements use the real, coordinatewise order.

## Proof
**1. Three spectral values.** Write \(\lambda_1>\lambda_2>\lambda_3\), and let \(P_1,P_2,P_3\) be the mutually orthogonal spectral projections, so \(P_1=vv^T\), \(P_1+P_2+P_3=I\), and
\[
e^{tA}=e^{\lambda_3t}I+(e^{\lambda_1t}-e^{\lambda_3t})P_1+(e^{\lambda_2t}-e^{\lambda_3t})P_2.\]
For distinct coordinates \(i,j\), define \(a_{ij}=v_iv_j>0\), \(b_{ij}=\langle P_2e_j,e_i\rangle\), \(\alpha=\lambda_2-\lambda_3\), and \(\beta=\lambda_1-\lambda_3\), where \(0<\alpha<\beta\). Then for \(t>0\),
\[
\langle e^{tA}e_j,e_i\rangle=(e^{\lambda_1t}-e^{\lambda_3t})[a_{ij}+b_{ij}R(t)],\quad R(t)=\frac{e^{\alpha t}-1}{e^{\beta t}-1}.
\]
The function \(R\) decreases strictly from \(r_0=\alpha/\beta\) to zero as \(t\) increases from zero to infinity. Indeed, its logarithmic derivative is \(\alpha/(1-e^{-\alpha t})-\beta/(1-e^{-\beta t})<0\), since the function \(x\mapsto x/(1-e^{-xt})\) increases strictly for \(x>0\): differentiating reduces this to \(e^{xt}>1+xt\). If \(b_{ij}\ge0\), the entry is positive at every \(t>0\). If \(b_{ij}<0\), the bracket increases strictly with \(t\); it is already positive for every \(t>0\) when \(a_{ij}+b_{ij}r_0\ge0\), and otherwise has one zero at the unique \(\tau_{ij}>0\) satisfying \(R(\tau_{ij})=-a_{ij}/b_{ij}\). Accordingly the nonnegative time set of each off-diagonal entry is either \((0,\infty)\) or \([\tau_{ij},\infty)\). Every diagonal entry is positive at every positive time because \(\langle e^{tA}e_i,e_i\rangle=\sum_{k=1}^3 e^{\lambda_k t}\|P_ke_i\|^2>0\). Hence the intersection over all pairs gives \(\mathcal P(A)=\{0\}\cup[\sup_{i\ne j}\tau_{ij},\infty)\), with the understood empty tail if this supremum is infinite. For a finite index set this supremum is finite.

If there are precisely two spectral values, \(e^{tA}=e^{\lambda_2t}I+(e^{\lambda_1t}-e^{\lambda_2t})P_1\). Its off-diagonal entries are strictly positive for all \(t>0\), so \(\tau=0\). The one-dimensional case is immediate.

**2. Realization of finite nonzero cutoffs.** Consider
\[
A_*=\frac1{22}\begin{pmatrix}-29&-7&12\\-7&-29&12\\12&12&-8\end{pmatrix}.
\]
An orthonormal eigenbasis consists of \(v=(1,1,3)/\sqrt{11}\), \(w=(1,-1,0)/\sqrt2\), and \(u=(3,3,-2)/\sqrt{22}\), with eigenvalues \(0,-1,-2\), respectively. The only potentially negative off-diagonal entry is the first-second pair: its spectral coefficients are \(a_{12}=1/11\) and \(b_{12}=-1/2\), while the first-third and second-third entries are positive for all \(t>0\). For these eigenvalues, \(R(t)=1/(1+e^t)\); consequently,
\[
\mathcal P(A_*)=\{0\}\cup[\log(9/2),\infty).
\]
Multiplying \(A_*\) by the positive scalar \(\log(9/2)/T\) realizes every prescribed cutoff \(T>0\). For \(T=0\), the tridiagonal path generator \(\begin{psmallmatrix}0&1&0\\1&0&1\\0&1&0\end{psmallmatrix}\) has three distinct eigenvalues and a strictly positive top eigenvector; its exponential is positive for every \(t\ge0\) by the nonnegative power series.

**3. Infinite cutoff with three spectral values.** On \(\ell^2(\mathbb N;\mathbb R)\), set \(c_k=\sqrt{3/2}\,2^{-k}\) and \(v_{2k-1}=v_{2k}=c_k\), so \(\|v\|_2=1\). Put \(P_1=vv^T\), and let \(P_2\) project orthogonally onto the closed span of \((e_{2k-1}-e_{2k})/\sqrt2\), for \(k\ge1\); these two projections are mutually orthogonal. Set \(P_3=I-P_1-P_2\) and \(A_\infty=-P_2-2P_3\). The three eigenvalues \(0,-1,-2\) all occur, and the simple dominant eigenvector \(v\) is strictly positive. For the pair \((2k-1,2k)\), the spectral coefficients are \(a=c_k^2\) and \(b=-1/2\), whence
\[
\langle e^{tA_\infty}e_{2k},e_{2k-1}\rangle=(1-e^{-2t})\left(c_k^2-\frac1{2(1+e^t)}\right).
\]
At every fixed \(t>0\), this expression is negative for all sufficiently large \(k\), since \(c_k\to0\). Thus \(\mathcal P(A_\infty)=\{0\}\) and \(\tau=\infty\). Each fixed pair nevertheless has its own finite eventual positivity cutoff, as follows from part 1.

**4. Four spectral values admit a positivity-time hole.** Let \(J\) be the adjacency matrix of the four-vertex path, set \(B=I_4+J/4\), and let \(A_4=\log B\) by symmetric functional calculus. Since the eigenvalues of \(J\) are \(2\cos(k\pi/5)\), \(k=1,2,3,4\), the matrix \(B\) is positive definite with four distinct eigenvalues. It is entrywise nonnegative and irreducible, so the dominant eigenvector of \(A_4\) is strictly positive. Now \(e^{tA_4}=B^t\). For \(0<t<1\), its entry in positions \((1,3)\) is strictly negative: the even part \(g_t(z)=((1+\sqrt z/4)^t+(1-\sqrt z/4)^t)/2\) of the functional calculus is a decreasing function of \(z\) on the two positive eigenvalues of the odd-block restriction \(J^2|_{\operatorname{span}(e_1,e_3)}=\begin{psmallmatrix}1&1\\1&2\end{psmallmatrix}\), since \(g'_t(z)<0\) for \(0<t<1\). For \(1<t<2\), its entry \((1,4)\) is strictly negative: polynomial interpolation of \(x^t\) on the four positive, distinct eigenvalues of \(B\) has cubic coefficient equal to the third divided difference \(f_t[\xi_1,\xi_2,\xi_3,\xi_4]\), which is strictly negative because \(\frac{d^3}{dx^3}(x^t)=t(t-1)(t-2)x^{t-3}<0\). The lower-degree terms give zero in entry \((1,4)\), while \((B^3)_{1,4}=1/64\), establishing negativity. At integer times \(0,1,2\) positivity follows from \(I\), \(B\), and \(B^2\), and positivity for all \(t\ge2\) follows from the published sharp critical-exponent theorem for powers of \(4\times4\) doubly nonnegative matrices [4]. Thus \(\mathcal P(A_4)=\{0,1\}\cup[2,\infty)\). This last component uses the published critical-exponent theorem rather than claiming it as a new statement.

## Verification
All critical steps are analytic and cover infinitely many coordinate pairs, not extrapolations from finite enumeration. The accompanying standard-library script `verify_spectral_times.py` checks the exact eigenvector decompositions and cutoff identities, supplies rational arithmetic checks on the four-vertex path, and independently tests sample matrix powers as consistency checks. The sharp four-eigenvalue construction additionally invokes the established dimension-four critical-exponent theorem. Its use is stated explicitly, rather than being presented as a self-contained new proof of that published theorem.

## Relationship to prior work
Daners, Glück and Kennedy [1] developed eventual positivity criteria and finite-dimensional semigroup examples; these do not specify the entire positivity-time set by spectral cardinality on countable coordinate Hilbert spaces. Arnold [2] proves a growth-bound equality for individually eventually positive semigroups on \(L^p\), a different statement. Dobrick [3] gives a compact-resolvent self-adjoint example whose operators fail to be positive at arbitrarily late times; its generator uses a richer spectral structure, while the bounded three-level example above has an explicit coordinatewise obstruction at every positive time. Guillot, Khare and Rajaratnam [4] establish the critical exponent for all doubly nonnegative matrices, used as a cited result in the four-point witness. In finite dimension their theorem also supplies general eventual positivity once a matrix power is entrywise nonnegative; it does not by itself characterize the exact positivity-time set for bounded self-adjoint semigroups with three spectral values in arbitrary countable dimension.

## Limitations
The no-gap theorem requires a strictly positive simple dominant eigenvector, self-adjointness, and a spectrum of cardinality at most three. It does not claim that arbitrary eventually positive semigroups are eventually positive as operators. The infinite-dimensional example has a bounded generator but not compact resolvent. The four-level counterexample is a specific matrix, not a classification of all four-level positivity-time sets. Two highly relevant 2026 manuscripts [2,3] were accessible only through verified abstracts; their complete texts were not inspected, so independent priority checks against those full texts remain advisable. Independent scientific review has not been performed.

## References
[1] D. Daners, J. Glück, J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, arXiv:1511.09020 (2015), especially Sections 5–6; https://arxiv.org/abs/1511.09020 .

[2] L. Arnold, *Stability of Individually Eventually Positive Semigroups on \(L^p\)-Spaces*, arXiv:2608.15038 (first posted 2026-08-15); https://arxiv.org/abs/2608.15038 .

[3] A. Dobrick, *Individual and Uniform Eventual Positivity of Self-Adjoint Semigroups*, arXiv:2609.00425 (2026); https://arxiv.org/abs/2609.00425 .

[4] D. Guillot, A. Khare, B. Rajaratnam, *The critical exponent conjecture for powers of doubly nonnegative matrices*, arXiv:1303.4701 (2013); https://arxiv.org/abs/1303.4701 .
