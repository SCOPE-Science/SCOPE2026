# Sharp negative type of three-subspace Grassmann graph metrics

## Finding

Let \(q\ge2\) be a prime power, \(n\ge6\) an integer, and \(\mathcal G_q(n,3)\) the set of all three-dimensional linear subspaces of \(\mathbb F_q^n\). Give \(\mathcal G_q(n,3)\) the Grassmann graph metric
\[
 d(U,V)=3-\dim(U\cap V).
\]
Put \([r]_q=(q^r-1)/(q-1)\), \(X=[n-5]_q\), and
\[
 F_{q,n}(p)=q^3X\{1-(q+1)2^p+q3^p\}-(q+1)+q2^p.
\]
There is a unique number \(p_{q,n}\in(0,1)\) such that \(F_{q,n}(p_{q,n})=0\). For every real \(p\ge0\), with the convention \(d(U,U)^p=0\) (also at \(p=0\)), the following are equivalent:

1. \(0\le p\le p_{q,n}\).
2. The powered distance matrix \((d(U,V)^p)_{U,V}\) is conditionally negative semidefinite.
3. For every \(t>0\), the Gaussian-type kernel \((\exp(-t\,d(U,V)^p))_{U,V}\) is positive semidefinite.

For every admissible \(p\) and each fixed \(t>0\), the last matrix is actually **strictly** positive definite. The powered distance matrix is strictly conditionally negative definite for \(0\le p<p_{q,n}\). At \(p=p_{q,n}\), the zero-sum nullspace has dimension
\[
 M_2=\begin{bmatrix}n\\2\end{bmatrix}_q-\begin{bmatrix}n\\1\end{bmatrix}_q,
\]
where the bracket denotes a Gaussian binomial coefficient. Consequently, the smallest Euclidean dimension of a realization with squared distances \(d(U,V)^{p_{q,n}}\) is precisely
\[
 \begin{bmatrix}n\\3\end{bmatrix}_q-1-M_2.
\]
For fixed \(q\) and \(n\to\infty\), put \(L_q=q\log3-(q+1)\log2>0\). Then
\[
 p_{q,n}=\frac{1}{q^3[n-5]_q L_q}+O_q([n-5]_q^{-2})
 \sim\frac{q-1}{q^{n-2}L_q}.
\]
For example, \(p_{2,6}=0.270530819610\ldots\), and the critical Euclidean dimension is \(806\) for the \(1395\) binary three-subspaces of dimension six.

## Assumptions and scope

The field order is a prime power, and the ambient dimension is at least six so that the graph diameter is exactly three. The theorem does not claim an analogous formula for subspace rank four or greater, or for infinite-dimensional Grassmannians. At \(p=0\), all off-diagonal entries of the powered distance are one. Negative type is the inequality \(\sum_{U,V}a_Ua_Vd(U,V)^p\le0\) for every real coefficient family with \(\sum_Ua_U=0\). A squared-Euclidean embedding means that the displayed powered distances, not their square roots, are squared Euclidean separations.

## Proof

**(1) Distance-regular decomposition from subspace incidence.** Fix \(U,V\) with \(d(U,V)=i\), where \(0\le i\le3\). A neighbor \(W\) of \(V\) is obtained by choosing a two-dimensional subspace \(T=W\cap V\), then a one-dimensional complement modulo \(T\). Counting those that decrease or increase their distance from \(U\) gives
\[
 c_i=[i]_q^2,\qquad b_i=q^{2i+1}[3-i]_q[n-3-i]_q,
\]
with \(c_0=b_3=0\). Indeed, to decrease the distance, \(T\) contains \(U\cap V\): there are \([i]_q\) choices of \(T\) and another \([i]_q\) choices for the new line inside \((U+T)/T\). To increase it, \(T\) meets \(U\cap V\) in codimension one: there are \(q^i[3-i]_q\) choices of \(T\), and \(q^{i+1}[n-3-i]_q\) choices for a new line outside \((U+T)/T\). Thus the intersection array is established without enumerating graph vertices. Write \(v=b_0=q[3]_q[n-3]_q\) and \(a_i=v-b_i-c_i\).

Let \(A_i\) be the indicator matrix of pairs at distance \(i\), with \(A_0=I\). These commute. Their joint eigenspaces are \(E_j\), \(0\le j\le3\), with dimensions
\[
 m_j=\begin{bmatrix}n\\j\end{bmatrix}_q-\begin{bmatrix}n\\j-1\end{bmatrix}_q
\]
(the second Gaussian coefficient is zero for \(j=0\)). The eigenvalues of \(A_1\), obtained from the finite Grassmann-scheme incidence decomposition, are
\[
 \theta_j=v-[j]_q[n-j+1]_q.
\]
These standard scheme facts may alternatively be reconstructed by the three-step inclusion up/down operator; they are recorded in the cited Grassmann-scheme reference. Let \(P_i(j)\) be the eigenvalue of \(A_i\) on \(E_j\). The intersection array gives an explicit, fully checkable recurrence
\[
 P_0(j)=1,\quad P_1(j)=\theta_j,\quad
 P_{i+1}(j)=\frac{(\theta_j-a_i)P_i(j)-b_{i-1}P_{i-1}(j)}{c_{i+1}}
 \quad(1\le i\le2).
\]
Since \(A_0+A_1+A_2+A_3\) is the all-one matrix, \(\sum_{i=1}^3P_i(j)=-1\) for \(j=1,2,3\).

**(2) The three nonconstant eigenvalue branches.** Set \(H=qX+1\) and \(R=[3]_q=q^2+q+1\). Substitution in the recurrence yields the following triples \((P_1(j),P_2(j),P_3(j))\):
\[
\begin{aligned}
 j=1:\quad &\left(q^3(q+1)X+q^3+q^2-1,\ \frac{q^2H(q^4X-q^2-2q-1)}{q+1},\ -\frac{q^6XH}{q+1}\right);\\[3pt]
 j=2:\quad &\left(q^3X-(q+1),\ q-q^3(q+1)X,\ q^4X\right);\\[3pt]
 j=3:\quad &\left(-R,\ qR,\ -q^3\right).
\end{aligned}
\]
For the powered metric \(D_p=A_1+2^pA_2+3^pA_3\), let \(\lambda_j(p)=P_1(j)+2^pP_2(j)+3^pP_3(j)\). The \(j=2\) branch is exactly \(\lambda_2(p)=F_{q,n}(p)\).

**(3) Only the middle harmonic can obstruct negative type before exponent one.** For \(j=1\), \(P_2(1)>0\) because \(X\ge1\) and \(q^4-q^2-2q-1>0\) for \(q\ge2\). Moreover
\[
 -P_3(1)-P_2(1)=q^2(q+1)H>0.
\]
Hence \(\lambda_1'(p)<0\) for \(p\ge0\); since \(\lambda_1(0)=-1\), this branch is always strictly negative.

For \(j=3\), \(\lambda_3(p)=-R+qR2^p-q^33^p\). If \(q\ge3\), then \(qR/q^3\le13/9<\log3/\log2\), so \(\lambda_3'(p)<0\) for \(p\ge0\), and \(\lambda_3(0)=-1\). At \(q=2\), concavity of \(s\mapsto s^p\) for \(0\le p\le1\) gives \(3^p\ge(2^p+4^p)/2\). Writing \(z=2^p\), we therefore obtain
\[
 \lambda_3(p)=-7+14z-8\,3^p\le-7+10z-4z^2\le-\frac34<0.
\]
Thus \(\lambda_3(p)<0\) throughout \([0,1]\) for all field orders.

Finally, the bracket \(1-(q+1)2^p+q3^p\) has strictly positive derivative for \(p\ge0\): its derivative is at least \(2^p\{q\log3-(q+1)\log2\}>0\), because \(q\ge2\) and \(2\log(3/2)>\log2\). The remaining term \(-(q+1)+q2^p\) also increases strictly. Consequently \(F_{q,n}\) increases strictly on \([0,\infty)\), with
\[
 F_{q,n}(0)=-1,\qquad F_{q,n}(1)=(q-1)(q^3X+1)>0.
\]
There is precisely one root in \((0,1)\). All nonconstant branches are nonpositive exactly for \(0\le p\le p_{q,n}\), and only \(E_2\) vanishes at the endpoint. As \(E_0\) is the constants and the other summands span the zero-sum subspace, this proves the complete conditional-negative-type criterion and its nullity.

**(4) Gaussian positivity, sharpness, and embedding rank.** Schoenberg's finite-metric criterion represents a zero-diagonal conditionally negative semidefinite \(D_p\) as the matrix of squared Euclidean distances of finite vectors \(z_U\). Distinct subspaces have positive distance, so their vectors are distinct; \(\exp(-t\lVert z_U-z_V\rVert^2)\) is strictly positive definite for every \(t>0\), for example by the Gaussian Fourier integral. Conversely, if \(p>p_{q,n}\), choose nonzero \(a\in E_2\). Then \(\sum_Ua_U=0\) and \(a^{\mathsf T}D_pa=\lambda_2(p)\lVert a\rVert^2>0\). The expansion \(a^{\mathsf T}(e^{-tD_p})a=-t\,a^{\mathsf T}D_pa+O(t^2)<0\) as \(t\downarrow0\) disproves universal positive semidefiniteness. Here the exponential is entrywise, not a matrix exponential. Double centering a squared-distance matrix shows that the minimal Euclidean embedding dimension equals its negative-type form rank on the zero-sum subspace, giving the stated formula.

**(5) Exponential decay of the threshold.** With \(L_q=q\log3-(q+1)\log2\), Taylor expansion at zero yields \(F_{q,n}(p)=-1+(q^3XL_q+q\log2)p+O_q(Xp^2+p^2)\). The monotone root therefore satisfies \(p_{q,n}=(q^3XL_q)^{-1}+O_q(X^{-2})\), giving the claimed limit using \(X=[n-5]_q\).

## Verification

The accompanying standalone file `verify_grassmann.py` uses Python's standard library. It reconstructs the Grassmann intersection-array recurrence exactly as fractions, checks the three closed eigenvalue triples over 37 \((q,n)\) parameter pairs (including nonprime prime powers), verifies eigenmultiplicity sums and sign regimes, and independently enumerates all \(1395\) three-spaces in \(\mathbb F_2^6\) via reduced-row-echelon forms. For the latter, it reconstructs the \(68355\) graph edges from intersections, checks distance shells, verifies shortest-path distances by breadth-first search, tests intersection numbers, and confirms the adjacency minimal polynomial on independent integer vectors. It prints `ALL_CHECKS_OK` when all checks pass. The finite tests support, but do not replace, the universal proof.

Reproduction: run `python3 verify_grassmann.py` from the directory holding the attached files. No dependencies or external data are needed.

## Relationship to prior work

The eigenstructure of the finite Grassmann scheme, especially the known incidence-operator decomposition, is prior art; Srinivasan (2013) provides a constructive exposition. Schoenberg-type negative-type and strictness principles are classical; Li and Weston (2009) analyze strict negative type. Vallentin (2005) studies minimum-distortion Euclidean embeddings of distance-regular graphs using association schemes, a related but different optimization problem. The present statement classifies exact distance **powers** admitting universal Gaussian positive definiteness for rank-three finite-field Grassmannians, selects the decisive middle harmonic for every field/dimension, and identifies the exact endpoint rank and exponential scale. These conclusions are not stated in the cited treatments. The Johnson-subset case is not interchangeable with a finite-field Grassmann graph: its intersection numbers and its distance-power harmonic eigenvalues differ.

## Limitations

This is a mathematical proof with supporting finite checks, not an independent external validation or historical uniqueness guarantee. No assertion is made for Grassmann graphs of diameter at least four. Searches of specialized pre-2016 literature may be incomplete, and a different formulation of this particular sharp negative-type exponent in association-scheme literature remains possible. The numeric example is approximate; the defining equation, rank and sign classification are exact.

## References

1. F. Vallentin, *Optimal Embeddings of Distance Regular Graphs into Euclidean Spaces*, arXiv:math/0509716v1, publicly posted 2005-09-30. https://arxiv.org/abs/math/0509716
2. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695v1, publicly posted 2009-01-06. https://arxiv.org/abs/0901.0695
3. M. K. Srinivasan, *The Goldman-Rota identity and the Grassmann scheme*, arXiv:1304.6244v1, publicly posted 2013-04-23. https://arxiv.org/abs/1304.6244
