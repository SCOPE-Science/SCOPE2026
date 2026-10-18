# Five categories are the sharp threshold for positive richness–missing-mass covariance after two draws

## Finding

Let \(X_1,X_2\) be independent draws from a discrete probability law having precisely \(d\) atoms of positive masses \(p_1,\ldots,p_d\). Write
\[
K_2=\#\{X_1,X_2\},\qquad
M_2=\sum_{i:p_i\text{ is unobserved}}p_i,
\qquad s_j=\sum_{i=1}^d p_i^j.
\]
The missing mass \(M_2\) is the conditional chance that the third draw has a category not observed in the first two. The exact covariance is
\[
\operatorname{Cov}(K_2,M_2)=(1+s_2)s_3-2s_2^2. \tag{1}
\]
The **sharp support threshold** is five:

* With one atom, the covariance is zero. With two, three, or four positive atoms, the covariance is strictly negative for *every* choice of probabilities.
* With five positive atoms, it can be positive: for \(p=(4/5,1/20,1/20,1/20,1/20)\), the covariance is exactly \(1/1600\).
* For every \(d\ge5\), there are fully supported laws with positive covariance and others with negative covariance. For the uniform \(d\)-atom law the covariance is \(-(d-1)/d^3\).

This is a classification of whether a positive covariance is *possible* at a given support size, not a claim that every five-atom law has positive covariance. The two-draw horizon is the first at which sample richness is random.

## Assumptions and scope

All probabilities are real and strictly positive and sum to one; \(d\) is finite. The sample size is exactly two. The missing mass is a population-probability-weighted sum of unseen-category indicators, not the *number* of unseen categories, and \(K_2\) counts distinct categories rather than the number of singletons. The covariance is taken under the fixed two-draw multinomial model, not an independently Poissonized sample size. No distributional asymptotics are required.

## Proof

**1. Exact reduction to power sums.** Let \(I=\mathbf1\{X_1=X_2\}\). Then \(K_2=2-I\) and \(\mathbb EI=s_2\). An atom \(i\) remains unseen precisely when both draws avoid it, giving
\[
\mathbb EM_2=\sum_i p_i(1-p_i)^2=1-2s_2+s_3.
\]
On the event \(I=1\), both draws land in one atom \(i\), leaving missing mass \(1-p_i\). Therefore
\[
\mathbb E(IM_2)=\sum_i p_i^2(1-p_i)=s_2-s_3.
\]
It follows that
\[
\operatorname{Cov}(K_2,M_2)=-\operatorname{Cov}(I,M_2)
=s_2(1-2s_2+s_3)-(s_2-s_3),
\]
which is (1).

**2. Extremal shape at prescribed concentration.** Fix \(m\ge2\), a feasible quadratic power sum \(t\in[1/m,1]\), and maximize \(s_3\) on the compact set of \(m\)-component nonnegative probability vectors satisfying \(s_2=t\). At a maximizer, restrict to its positive support, of size \(r\le m\). If the positive masses are all equal, keep that as the uniform case. Otherwise the gradients of the constraints \(\sum p_i=1\) and \(\sum p_i^2=t\) are independent. The Lagrange equations
\[
3p_i^2=\lambda+2\mu p_i
\]
show that at most two different positive masses occur; call them \(a>b>0\). Subtracting the equations yields \(2\mu=3(a+b)\).

If two coordinates both equal \(a\), the vector adding \(\varepsilon\) to one and subtracting it from the other lies in the tangent space of both constraints. The Hessian of the constrained objective \(s_3-\lambda(\sum p_i-1)-\mu(s_2-t)\) along this tangent vector equals
\[
2(6a-2\mu)=6(a-b)>0.
\]
The second-order necessary condition for a constrained maximum demands a nonpositive Hessian on every tangent vector. This contradiction shows that a nonuniform maximizer has exactly **one** largest mass, with all remaining positive masses equal. Zero entries merely reduce the support size. Thus, at each fixed \(s_2\), the largest possible covariance in (1) is attained either by a uniform-support vector or by a vector \((1-(r-1)b,b,\ldots,b)\) with \(r\le m\) and \(0<b<1/r\) (including equality for the uniform endpoint). We emphasize that the extremizer may lie on a smaller-support boundary.

**3. Universal negativity with at most four atoms.** For a vector having one large mass and \(r-1\) equal smaller masses, substitution into (1) and algebraic factorization yield
\[
\begin{array}{rcl}
r=2:&\quad&-2b^2(1-b)^2,\\
r=3:&\quad&-2b^2(18b^3-12b^2+1),\\
r=4:&\quad&-6b^3(48b^2-30b+5).
\end{array}\tag{2}
\]
Here \(0<b\le1/r\). The factors are strictly negative: for \(r=3\) the bracket decreases on \([0,1/3]\) but remains at least \(1/3\); for \(r=4\) the quadratic has positive leading coefficient and negative discriminant \(-60\). For a uniform \(r\)-atom vector, (1) equals \(-(r-1)/r^3<0\), which is also covered by (2) for \(r\le4\). Since \(1+s_2>0\), maximizing \(s_3\) with fixed \(s_2\) also maximizes (1). Every nondegenerate law with at most four atoms therefore has strictly negative covariance. For the one-atom boundary, both statistics are constant and their covariance is zero.

**4. Sharpness and both signs above the threshold.** With \(p=(4/5,1/20,1/20,1/20,1/20)\), one has \(s_2=13/20\), \(s_3=41/80\), and (1) gives \(1/1600>0\). For any \(d>5\), fix a sufficiently small \(\varepsilon>0\), multiply these five masses by \(1-\varepsilon\), and append \(d-5\) masses each equal to \(\varepsilon/(d-5)\). Continuity of (1) preserves positivity. Every uniform \(d\)-atom law, on the other hand, has negative covariance \(-(d-1)/d^3\). Thus five is the sharp minimal support and both signs are possible for each larger support size.

## Verification

`verify.py` uses only the Python standard library and exact rational arithmetic. It computes \(K_2\) and \(M_2\) directly for every ordered sample pair and independently compares the resulting covariance with (1), throughout all positive integer-composition laws with one through six atoms and moderate denominators. It checks strict signs at supports two through four, the five-atom rational witness, fully supported positive witnesses through twenty atoms, the uniform formula through fifty atoms, and the three factorized expressions in (2) on rational grids. The program must print `PASS exact checks: 10730`. The symbolic second-order extremal argument and the universal inequalities in (2) are analytic proofs; finite rational tests are corroboration, not substitutes for these proofs.

## Relationship to prior work

Chebunin and Zuyev (arXiv:1906.10949, first public 2019-06-26) study fluctuations of occupancy and missing-mass processes, including their covariance functions, in infinite urn schemes with regular variation and Poissonization. Their analysis emphasizes functional limits, not the exact support-size boundary for fixed two observations. Indeed, under independent Poissonization, the occupancy indicators of different categories become independent, implying \(\operatorname{Cov}(K,M)=-\sum_i p_i\operatorname{Var}(\mathbf1_{\{N_i>0\}})\le0\); thus fixed sample-size conditioning is important to the positive example here.

Lee and Böhme (arXiv:2402.05835, first submitted 2024-02-08; extended ICLR 2025 version, Appendix D.3) give general multinomial covariance component formulas between occupancy-frequency statistics and missing mass. Those formulas encompass an exact covariance calculation such as (1); **the elementary identity (1) is not claimed as a novel stand-alone contribution**. The specific claimed contribution is the sharp five-category *possibility threshold*, proved using a fixed-concentration third-power-sum extremal argument and a complete one-through-four support exclusion.

Related published mathematical notes on adjacent discovery indicators and on richness against occupancy frequency counts or unbiased diversity estimates study different pairings. They do not, as inspected, yield the support-five statement by implication. The strongest residual originality uncertainty is an equivalent threshold hidden in classical sample-coverage, symmetric-power-sum, or occupancy literature.

## Limitations

This result does not classify the entire positive-covariance region of the \(d\)-simplex when \(d\ge5\), quantify the largest attainable covariance for each \(d\), or address three or more draws. It does not assert a new general covariance identity: general component formulas already exist. The proof is for a finite, fully supported population law. A positive example says nothing about the typical law on an alphabet of size five. Independent historical-priority review has not been performed.

## References

1. M. Chebunin and S. Zuyev, “Functional central limit theorems for occupancies and missing mass process in infinite urn models,” arXiv:1906.10949 (first posted 2019-06-26), https://arxiv.org/abs/1906.10949; *Journal of Theoretical Probability* 35 (2022), 1–19, https://doi.org/10.1007/s10959-020-01053-6.
2. S. Lee and M. Böhme, “How Much is Unseen Depends Chiefly on Information About the Seen,” arXiv:2402.05835 (first posted 2024-02-08), https://arxiv.org/abs/2402.05835; ICLR 2025, Appendix D.3, https://proceedings.iclr.cc/paper_files/paper/2025/file/1324202edd7b5e2235aa19fec340d045-Paper-Conference.pdf.
3. A. Ben-Hamou, S. Boucheron and M. I. Ohannessian, “Concentration Inequalities in the Infinite Urn Scheme for Occupancy Counts and the Missing Mass, with Applications,” arXiv:1412.8652 (2014), https://arxiv.org/abs/1412.8652.
4. M. Skorski, “On Missing Mass Variance,” arXiv:2104.07028 (2021), https://arxiv.org/abs/2104.07028.
