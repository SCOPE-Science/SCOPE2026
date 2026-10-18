# Cyclic Plücker complete intersections: an exact smoothness criterion and low-dimensional models

## Finding
Fix an integer \(n\ge4\) and an algebraically closed field \(k\) of any characteristic. Write \(p_{ij}\) for the Plücker coordinates on \(\operatorname{Gr}(2,n)\), and use cyclic indices modulo \(n\). Define the **scheme**
\[
X_n=\operatorname{Gr}(2,n)\cap V(p_{12},p_{23},\ldots,p_{n-1,n},p_{n1}).
\]
Then \(X_n\) is reduced, pure of dimension \(n-4\), and a local complete intersection (hence Gorenstein). Its dualizing sheaf and degree are
\[
\omega_{X_n}\simeq\mathcal O_{X_n},\qquad
\deg X_n=\frac{1}{n-1}\binom{2n-4}{n-2}.
\]
The irreducible components are indexed by cyclic independent sets \(T\subseteq\{1,\ldots,n\}\) of size at least two; in particular their number is \(L_n-n-1\), where \(L_n\) is the Lucas number, normalized by \(L_0=2,L_1=1\). **The component-indexing portion is a deduction from the established binomial-edge-ideal decomposition and is not asserted to be new.**

The additional geometric result is an exact **pointwise smoothness criterion**. Represent \(W\in X_n\) by a rank-two \(2\times n\) matrix with column vectors \(v_1,\ldots,v_n\in k^2\), and define \(Z(W)=\{i:v_i=0\}\). Then
\[
W\in (X_n)_{\mathrm{sm}}
\quad\Longleftrightarrow\quad
\begin{cases}
\text{no two cyclic neighbors belong to }Z(W),\\
\det(v_{i-1},v_{i+1})\ne0\text{ for every }i\in Z(W).
\end{cases}
\]
The condition is invariant under the choice of frame. Thus its negation describes the entire reduced singular support set-theoretically in every characteristic.

For \(n\ge5\), at a point with exactly the zero columns \(v_1,v_2,v_4\), with \(v_3\) and \(v_5\) independent, and all remaining columns nonzero, the completed local ring is
\[
\widehat{\mathcal O}_{X_n,W}\simeq
k[[t_1,\ldots,t_{n-5},s,t]]/(st).
\]
For \(n=5\), the scheme is a nodal pentagon of five projective lines. For \(n=6\), its eleven components are eight linearly embedded projective planes and three copies of the Segre quadric \(\mathbb P^1\times\mathbb P^1\); their total Plücker degree is \(8+3\cdot2=14\).

## Assumptions and scope
The base field is algebraically closed but its characteristic is unrestricted. This theorem addresses the scheme-theoretic linear section \(X_n\), not the full affine binomial-edge-ideal variety (which has an additional rank-one component). A "zero column" refers to any rank-two representative matrix; since left multiplication by \(\operatorname{GL}_2\) preserves zero vectors and linear dependence, the criterion depends only on the Grassmannian point. The term "smooth" is scheme-theoretic smoothness over \(k\), not smoothness of a selected irreducible component. Reduced singular support is characterized; no claim is made about the nonreduced singular subscheme.

## Proof
**1. A reduced Grassmannian section.** Let \(\mathcal F\subset\operatorname{Mat}_{2\times n}\) be the rank-two open locus. It maps smoothly and surjectively onto \(\operatorname{Gr}(2,n)\) as the principal \(\operatorname{GL}_2\)-bundle of frames. Pulling back the stated Plücker hyperplanes gives the equations
\[
f_i=\det(v_i,v_{i+1})=0\qquad(i\bmod n).
\]
Their ideal in the ambient polynomial ring is the binomial edge ideal of the cycle \(C_n\). Herzog–Hibi–Hreinsdóttir–Kahle–Rauh prove this ideal radical, with minimal primes indexed by the empty set and by all cyclic independent vertex sets \(T\) of size at least two (the corresponding prime sets the \(v_i\) for \(i\in T\) to zero and makes columns proportional on every remaining consecutive run). The empty-set prime imposes rank at most one and is disjoint from \(\mathcal F\). Therefore the pullback of \(X_n\) is reduced; faithful flatness of the frame bundle proves that \(X_n\) is reduced. This application of the established radicality and prime decomposition is explicitly prior work.

**2. Dimension, purity and number of components.** If \(T\) is cyclic independent of cardinality \(z\ge2\), its complement consists of \(z\) nonempty paths (runs) with total \(n-z\) columns. On the dense locus with every column outside \(T\) nonzero and the \(z\) run directions spanning \(k^2\), a run of length \(r\) contributes \(r+1\) free parameters (one common direction, up to scalar, and \(r\) scalars). Thus the frame locus has dimension \((n-z)+z=n\). Quotienting by the free four-dimensional frame action gives component dimension \(n-4\). The primes for distinct \(T\) remain distinct on the rank-two open set, so the components are exactly these. The number of independent \(z\)-subsets of the labeled \(n\)-cycle is
\[
\frac n{n-z}\binom{n-z}{z}\quad(0\le z\le\lfloor n/2\rfloor),
\]
whose sum over all \(z\) is \(L_n\). Removing the empty set and \(n\) singletons gives \(L_n-n-1\). The Grassmannian is smooth of dimension \(2n-4\), and \(X_n\) has pure codimension \(n\), cut by exactly \(n\) hyperplanes; in each regular local ring these generators form a regular sequence. Hence \(X_n\) is a local complete intersection. By adjunction and \(\omega_{\operatorname{Gr}(2,n)}=\mathcal O(-n)\), one gets \(\omega_{X_n}=\mathcal O_{X_n}\). The Plücker intersection degree equals \(\deg\operatorname{Gr}(2,n)\), the displayed Catalan number.

**3. Complete tangent-rank calculation.** Every rank-two solution has at least two zero columns: with zero or only one zero column, the nonzero columns form a connected path and all become proportional, contradicting rank two. Write \(Z=Z(W)\), of cardinality \(z\). If two consecutive columns vanish, their edge equation has zero differential. Since \(X_n\) has local codimension \(n\), the Jacobian criterion shows \(W\) singular.

Now suppose the zeros are cyclically isolated. The nonzero columns form exactly \(z\) runs of lengths \(r_1,\ldots,r_z\) with \(\sum_jr_j=n-z\). Each run is nonzero and proportional, and its \(r_j-1\) internal-edge differential rows are independent; altogether these supply \(n-2z\) rows. The two equations incident to an isolated zero column \(v_i\) have derivatives supported only in the two coordinates of \(v_i\), forming a block of rank \(\operatorname{rank}(v_{i-1},v_{i+1})\) (one or two). Blocks from different zero columns are disjoint and independent of the run-internal blocks. Consequently,
\[
\operatorname{rank}(df_1,\ldots,df_n)_W
=n-2z+\sum_{i\in Z}\operatorname{rank}(v_{i-1},v_{i+1}).
\]
This equals \(n\) precisely when every indicated neighbor pair is independent. The same Jacobian rank is obtained before and after the smooth frame-bundle quotient. This proves the exact smoothness criterion, including its characteristic independence.

**4. Explicit crossing germ.** Near a point with exactly \(Z=\{1,2,4\}\) and \(p_{35}\ne0\), use the frame action to set \(v_3=e_1\) and \(v_5=e_2\). The equations around the zero columns force \(v_4=0\) and \(v_2=s e_1\). The consecutive equations from \(5\) through \(n\) make the nonzero \(v_5,\ldots,v_n\) proportional to \(e_2\); the remaining cyclic equation forces \(v_1=t e_2\). The only remaining equation is \(f_1=\det(t e_2,s e_1)=-st=0\). The \(n-5\) other nonzero-column ratios are free near the chosen point. Completion yields exactly the claimed node times a smooth factor. (For \(n=5\) the string of other columns is empty.)

**5. First two positive-dimensional cases.** At \(n=5\) all independent sets of size at least two are the five nonadjacent vertex pairs. Each corresponding prime forces two zero columns and proportionality in the only length-two surviving run; the associated Grassmannian locus is a projective line. Two such lines meet exactly when their sets have a common vertex and the two surviving coordinate columns can have rank two. Each line meets precisely two others, no three share a point, and the explicit chart in step 4 makes each of the five intersections an ordinary node. Thus \(X_5\) is a cycle of five lines. At \(n=6\) there are six independent pairs at cyclic separation two, three opposite pairs, and two independent triples. The six separation-two pairs yield linear planes, each opposite pair gives a Segre \(\mathbb P^1\times\mathbb P^1\) of degree two, and each alternating triple gives \(\operatorname{Gr}(2,3)=\mathbb P^2\). These are all eleven distinct components. Their degree sum is fourteen, matching the Grassmannian intersection degree.

## Verification
The included standalone `verify_cycle.py` enumerates row-reduced rank-two frames over \(\mathbb F_2\) for \(n=4,5,6,7\), and over \(\mathbb F_3\) for \(n=4,5,6\). For each frame satisfying all cycle equations it directly ranks the exact Jacobian matrix, evaluates the proposed zero-column criterion, and confirms membership in at least one explicit prime component. It also verifies cycle-independent-set counts. The extracted code returned `VERIFY_OK`, with counts respectively \((2,2),(10,5),(38,11),(126,21)\) and \((2,2),(15,10),(89,44)\), where each pair means total finite-field points and smooth finite-field points. These checks are finite corroboration and not the proof of the theorem over all \(n\) or arbitrary characteristic.

## Relationship to prior work
The cycle binomial-edge ideal is radical, and its entire affine minimal-prime classification, **including the independent-set indexing**, is explicitly given by Herzog–Hibi–Hreinsdóttir–Kahle–Rauh (arXiv:0909.4717, Corollary 2.2 and the cycle paragraph following Corollary 3.9); Rauh (arXiv:1210.7960, Theorem 7) generalizes the same component framework. These imply the basic component decomposition after restricting to rank-two frames, so this is not claimed as new. Damadi–Rahmati (Mathematics 2016, 4(2), 37, Corollary 4) establish that cycle graphs with at least five vertices are edge singular in their stated sense, but do not give the displayed **point-by-point smoothness criterion for the Grassmannian scheme**, its crossing chart, or the explicit \(n=5,6\) scheme geometry. The adjunction and degree calculations are standard once the complete-intersection statement is established. The proposed incremental contribution is precisely the uniform all-point criterion, nodal local model, and geometric interpretation of these cyclic Plücker sections as reduced Gorenstein varieties with trivial dualizing sheaf.

## Limitations
The nonreduced Jacobian singular subscheme, individual higher-dimensional component normality, all nongeneric completed singular germs, global deformation behavior, and any Calabi–Yau property stronger than triviality of the dualizing sheaf are not asserted. Although source and published-finding corpus searches did not locate the same pointwise criterion, undiscovered equivalent formulations remain a genuine originality risk. For \(n=4\), \(X_n\) is a disconnected pair of reduced points, so no connectedness claim is made. This work has not undergone an independent audit.

## References
1. J. Herzog, T. Hibi, F. Hreinsdóttir, T. Kahle, J. Rauh, *Binomial edge ideals and conditional independence statements*, arXiv:0909.4717 (first posted 2009-09-25), especially Corollary 2.2, Theorem 3.2 and the cycle example after Corollary 3.9.
2. J. Rauh, *Generalized Binomial Edge Ideals*, arXiv:1210.7960 (first posted 2012-10-30), especially Corollary 4, Lemma 5 and Theorem 7.
3. H. Damadi, F. Rahmati, *Smoothness in Binomial Edge Ideals*, Mathematics 4(2) (2016), article 37, DOI: 10.3390/math4020037, especially Theorem 3 and Corollary 4.
