# Sharp generalized roundness in diameter-three Kneser graphs

## Finding
For every integer \(k\geq 8\), let \(n=3k-2\), let \(X\) be the set of all \(k\)-subsets of \([n]\), and let \(d\) be the shortest-path metric on the Kneser graph joining disjoint members of \(X\). Define
\[
A_k=\binom{2k-4}{k-2},\qquad R_k=\frac{(k-2)^2}{k-1}-2.
\]
There is exactly one real \(p_k>0\) satisfying
\[
\boxed{A_k\left[R_k\big((3/2)^{p_k}-1\big)-\big(1-2^{-p_k}\big)\right]=1.}
\]
For every real \(p\geq0\), the powered-distance matrix \(D_p=(d(S,T)^p)_{S,T\in X}\) is conditionally negative semidefinite if and only if \(0\leq p\leq p_k\). Here the diagonal is zero also at \(p=0\), when all off-diagonal entries are one. It is strictly negative definite on the zero-sum subspace for \(0\leq p<p_k\). At \(p=p_k\), its zero-sum kernel is **exactly** the second Johnson harmonic, of dimension
\[
\boxed{\dim\ker(D_{p_k}|_{\mathbf1^\perp})=\binom n2-n=\frac{n(n-3)}2.}
\]
Consequently the smallest Euclidean dimension in which the squared distances \(d(S,T)^{p_k}\) are realized is
\[
\boxed{\binom nk-1-\left(\binom n2-n\right).}
\]
Moreover the sharp exponent has the asymptotic
\[
\boxed{p_k\sim\frac{16\sqrt\pi}{\log(3/2)}\frac{1}{4^k\sqrt{k}}\quad(k\to\infty).}
\]
In particular, for \(k=8\) the root is approximately \(0.001859222906440637\), and the endpoint Euclidean embedding dimension is \(319560\).

## Assumptions and scope
A Kneser graph has a vertex for each \(k\)-subset and joins two vertices exactly when they are disjoint. The restriction \(n=3k-2\) is the first diameter-three regime immediately below the common-neighbor threshold \(n=3k-1\). All distances are intrinsic unit-edge graph distances. Negative type means
\[
\sum_{S,T\in X}c_Sc_Td(S,T)^p\leq0
\quad\text{whenever }\sum_{S\in X}c_S=0,
\]
with real coefficients. The assertion is about the complete finite metric space, with no normalization of the distance matrix. It excludes \(k<8\) and Kneser parameters other than \(n=3k-2\).

## Proof
**1. Graph distances.** For two distinct \(k\)-sets put \(t=|S\cap T|\). When \(t=0\), they are adjacent. When \(t\geq2\), their union has size at most \(2k-2\), leaving at least \(k\) ground elements; a third \(k\)-set disjoint from both gives distance two. When \(t=1\), the complement of their union has only \(k-1\) elements, so a common neighbor is impossible. To construct a three-edge path, choose a \(k\)-set \(U\) disjoint from \(S\) that contains two elements of \(T\setminus S\), together with \(k-2\) elements outside \(S\cup T\). Then \(|U\cap T|=2\), so \(U\) and \(T\) have a common neighbor; the distance from \(S\) to \(T\) is three. Thus the distances at intersection sizes \(0,1,2,\ldots,k-1\) are respectively \(1,3,2,\ldots,2\).

**2. Johnson harmonic eigenvalues.** The standard multiplicity-free decomposition of functions on \(k\)-subsets under the permutation action of \(S_n\) has orthogonal components \(V_j\) for \(0\leq j\leq k\), with \(V_0\) the constants and
\[
\dim V_j=\binom nj-\binom n{j-1}.
\]
Let \(B_0\) be the matrix indicating disjoint distinct pairs and \(B_1\) the matrix indicating \(|S\cap T|=1\). The standard Johnson-scheme orbital eigenvalues on \(V_j\), for \(1\leq j\leq k\), are
\[
 a_j=(-1)^j\binom{2k-2-j}{k-j},\qquad
 b_j=a_j r_j,\qquad
 r_j=\frac{(k-j)^2}{k-1}-j.
\]
For completeness, the disjoint-pair eigenvalue is obtained by applying \(B_0\) to the signed basis function \(f_j(S)=\prod_{i=1}^j(\mathbf1_{u_i\in S}-\mathbf1_{v_i\in S})\), where the \(2j\) labels are distinct. For \(B_1\), the same count gives
\[
 b_j=(-1)^j(k-j)\binom{2k-2-j}{k-j-1}
       +(-1)^{j-1}j\binom{2k-2-j}{k-j}.
\]
Dividing by \(a_j\) yields \(r_j\), since the lower-to-upper binomial ratio is \((k-j)/(k-1)\). The \(S_n\)-translates of these functions span \(V_j\); equivalently, these are the Eberlein orbital eigenvalues in the Johnson association scheme. The quoted standard decomposition, including multiplicities, is also recorded in Aalipour et al., Theorem 3.9 (2015 arXiv preprint).

Write \(B_2\) for the sum of the orbitals with intersection between two and \(k-1\). Since \(J=I+B_0+B_1+B_2\), the distance-power matrix is
\[
 D_p=2^p(J-I)+(1-2^p)B_0+(3^p-2^p)B_1.
\]
For \(p>0\), set \(v=(3/2)^p-1>0\), \(w=1-2^{-p}>0\), and \(q=w/v\). On \(V_j\) with \(j\geq1\), the eigenvalue \(\lambda_j(p)\) therefore satisfies
\[
\boxed{\frac{\lambda_j(p)}{2^p}=a_j(r_jv-w)-1.}\tag{1}
\]

**3. The unique second-harmonic crossing.** For all \(p>0\), exponential bounds give
\[
0<q=\frac{1-2^{-p}}{(3/2)^p-1}
<\frac{\log 2}{\log(3/2)}<\frac74.
\]
The final strict inequality follows from \(2^{11}<3^7\). For \(k\geq8\), \(r_2\geq22/7\), hence \(r_2-q>0\). Define
\[
H_k(p)=A_k[r_2((3/2)^p-1)-(1-2^{-p})].
\]
It satisfies \(H_k(0)=0\), \(H_k'(0)=A_k[r_2\log(3/2)-\log2]>0\), and
\[
H_k''(p)=A_k\left[r_2\log^2(3/2)(3/2)^p+\log^2(2)2^{-p}\right]>0.
\]
It is therefore strictly increasing from zero to infinity, crossing one at a unique positive exponent \(p_k\). Equation (1) shows that \(\lambda_2(p)\) has precisely that zero and is positive for every \(p>p_k\).

**4. Every competing harmonic remains negative through the crossing.** For \(0<p\leq p_k\), we have
\[
0<A_kv(r_2-q)=H_k(p)\leq1.
\tag{2}
\]
The ratios \(|a_{j+1}|/|a_j|=(k-j)/(2k-2-j)\) are at most \(1/2\) for \(j\geq2\), and \(r_j\) decreases strictly with \(j\). For even \(j\geq4\), if \(r_jv-w\leq0\) then (1) is negative; otherwise \(0<a_j(r_jv-w)<A_k(r_2v-w)\leq1\), so (1) is still strictly negative.

For \(j=1\), \(a_1<0\) and \(r_1=k-2>q\), so (1) is below \(-1\). It remains to control all odd \(j\geq3\). Put \(h=j-3\geq0\). Since \(r_3\geq4/7\) and \(r_j-r_{j+1}<3\),
\[
(q-r_j)_+\leq\frac{33}{28}+3h,
\qquad |a_j|\leq\frac{A_k}{2^{h+1}}.
\]
The elementary maximum over integers \(h\geq0\) is
\[
\max_{h\geq0}\frac{33/28+3h}{2^{h+1}}=\frac{117}{112}.
\]
Meanwhile \(r_2-q>22/7-7/4=39/28\). Consequently
\[
|a_j|v(q-r_j)_+
\leq\frac{117}{112}A_kv
<\frac34A_kv(r_2-q)\leq\frac34.
\]
For odd \(j\geq3\), equation (1) is therefore at most \(-1/4\). Hence every nonconstant component except \(V_2\) remains strictly negative at and below \(p_k\). At \(p=0\), \(D_0=J-I\) has eigenvalue \(-1\) on every nonconstant component. Above \(p_k\), \(V_2\) supplies a positive quadratic direction. This proves the exact negative-type range and the sole equality space.

**5. Euclidean rank and asymptotics.** By the finite negative-type embedding criterion, the centered Gram matrix \(-\tfrac12 P D_{p_k}P\), with \(P=I-J/|X|\), is positive semidefinite and has rank \(|X|-1-\dim V_2\). Its rank is the least dimension for an exact squared-Euclidean-distance realization.

Convexity and the positive initial derivative give \(0<p_k\leq[A_k(r_2\log(3/2)-\log2)]^{-1}\), so \(p_k\to0\). Taylor expansion at zero and the fact that \(r_2\sim k\) yield
\[
p_k\sim\frac{1}{A_kk\log(3/2)}.
\]
Finally \(A_k=\binom{2k-4}{k-2}\sim4^{k-2}/\sqrt{\pi k}\), giving the asserted constant \(16\sqrt\pi/\log(3/2)\). This proves all claims.

## Verification
The included standalone standard-library script `check_kneser.py` independently constructs the relevant disjointness and one-intersection orbital matrices for \(k=3,4,5\), checks their action on explicit harmonic vectors, and checks graph distances by breadth-first search. It also verifies the rational comparison inequalities for each \(8\leq k\leq180\), and computes high-precision critical roots and all harmonic signs at selected degrees through \(k=32\). It reports `KNESER_DIAMETER_THREE_NEGATIVE_TYPE_CERTIFICATE_OK` on success. The full infinite-family assertion is proved above; finite calculations are supplementary and not an exhaustive proof.

## Relationship to prior work
The Johnson-scheme eigenvalues, multiplicities and general Kneser distance-spectrum machinery are standard, and are explicitly reported by Aalipour et al. (2015), Theorems 3.9–3.10. General negative-type criteria appear in Sánchez (2011), and vertex-transitive equality considerations appear in Murugan (2011). Scarabotti and Tolli (2007) provide a broader finite-homogeneous-space harmonic-analysis setting. Those ingredients are credited rather than claimed as new. The additional result here is the **uniform all-harmonic comparison** showing that, for every \(k\geq8\) in the diameter-three regime, precisely \(V_2\) determines the sharp nonlinear power threshold, together with its endpoint rank and asymptotic. No covering result was identified in the inspected material; related unpublished or differently formulated calculations remain possible.

## Limitations
The theorem is restricted to graph metrics with \(n=3k-2\) and \(k\geq8\), and does not classify the smaller cases or Kneser graphs of other diameters. The novelty assessment is literature-limited rather than a guarantee of priority. The proof and code have not received independent mathematical validation.

## References
1. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533, first submitted 2007-01-19, https://arxiv.org/abs/math/0701533.
2. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451, first submitted 2011-08-02, https://arxiv.org/abs/1108.0451.
3. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, first submitted 2011-12-23, https://arxiv.org/abs/1112.5657.
4. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196, first submitted 2015-09-03, https://arxiv.org/abs/1509.01196.
