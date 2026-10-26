# Three-segment limit law for one-point types over staircase interval orders

## Finding
Let \(n\geq1\). Define the staircase height-two poset \(P_n\) on the \(2n\) named points \(a_1,\ldots,a_n,b_1,\ldots,b_n\) by
\[
a_i<b_j\quad\Longleftrightarrow\quad i\leq j,
\]
with no other strict comparisons. Regard \(P_n\) as an induced, individually named parameter subposet of the countable universal homogeneous poset. Every nonalgebraic complete one-type \(p\) has a lower set \(L_p=\{c\in P_n:c<x\in p\}\) and upper set \(U_p=\{c\in P_n:x<c\in p\}\). Define the bivariate type polynomial
\[
T_n(u,v)=\sum_{p\text{ nonalgebraic}}u^{|L_p|}v^{|U_p|}.
\]
Write
\[
I_n(z)=(1+z)^{n-1}\sum_{i=0}^{n-1}z^i+z^n(1+z)^n.
\]
Then the **exact joint type-profile identity** is
\[
\boxed{T_n(u,v)=I_n(u)+I_n(v)-1+\sum_{j=1}^{n}v(1+v)^{n-j}\big((1+u)^j-1\big).}
\]
In particular, for the scalar nonalgebraic type count,
\[
\boxed{T_n(1,1)=(2n+1)2^n,}
\]
and exactly \((n-1)2^n+1\) types have both a nonempty lower set and a nonempty upper set.

Select one of these \(T_n(1,1)\) types uniformly, and define \(X_n=|L_p|/n\), \(Y_n=|U_p|/n\). Let \(Z\) be uniform on \([0,1]\), independent of a categorical choice \(C\) with probabilities \(1/4,1/4,1/2\). Set
\[
(X,Y)=\begin{cases}
(1/2+Z,0)&C=1,\\
(0,1/2+Z)&C=2,\\
(Z/2,(1-Z)/2)&C=3.
\end{cases}
\]
Then the law of \((X_n,Y_n)\) converges to that of \((X,Y)\). More quantitatively, for the Wasserstein distance \(W_1\) induced by the \(\ell^1\) distance on \(\mathbb R^2\),
\[
\boxed{W_1\bigl(\mathcal L(X_n,Y_n),\mathcal L(X,Y)\bigr)=O(n^{-1/2}).}
\]
The limiting measure has mass \(1/4\) on each of two one-sided line segments and mass \(1/2\) on the diagonal segment. Its covariance, marginal variance and Pearson correlation are
\[
\boxed{\operatorname{Cov}(X,Y)=-\frac{23}{192},\qquad
\operatorname{Var}(X)=\operatorname{Var}(Y)=\frac{11}{64},\qquad
\operatorname{Corr}(X,Y)=-\frac{23}{33}.}
\]
In particular, \(\operatorname{Corr}(X_n,Y_n)\to-23/33\).

## Assumptions and scope
A one-type is counted once for each distinct complete relation pattern over the **individually named** \(2n\) parameters. Algebraic equality types are excluded. The ambient structure is the Fraïssé limit of **all finite partial orders**, so each consistent one-point extension of \(P_n\) is realized and determined uniquely up to automorphism fixing the parameters. The variables \(u,v\) are formal markers for the numbers of named elements strictly below and strictly above the new point. All limits keep the staircase shape while \(n\to\infty\); they are not assertions about arbitrary interval orders or arbitrary finite parameter posets.

## Proof
**1. Complete-type criterion.** A relation profile is a pair \((L,U)\) where \(L\) is an ideal, \(U\) is a filter, and \(l<u\) for every \(l\in L\), \(u\in U\). Necessity follows from transitivity of \(l<x<u\). Conversely, adjoining a new element strictly above exactly \(L\), strictly below exactly \(U\), and incomparable with the remaining parameters defines a finite poset precisely under these conditions. Universality realizes this finite extension, and ultrahomogeneity equates two realizations with the same profile. This standard criterion is used, not claimed as a new result.

**2. One-sided profiles.** An ideal \(L\) in \(P_n\) either contains every \(a_i\), in which case any subset of the \(b_j\) may be selected, contributing \(u^n(1+u)^n\), or has a first missing lower element \(a_i\). In the latter case, \(a_1,\ldots,a_{i-1}\) are required, \(a_i\) is missing, the remaining \(n-i\) lower elements are optional, and precisely the upper elements \(b_1,\ldots,b_{i-1}\) are optional. The weight is \(u^{i-1}(1+u)^{n-1}\). Summation gives \(I_n(u)\). The order-reversing involution \(a_i\leftrightarrow b_{n+1-i}\) gives the same filter enumerator \(I_n(v)\). Adding the ideal-only and filter-only patterns double-counts the empty–empty profile exactly once, hence their contribution is \(I_n(u)+I_n(v)-1\).

**3. Two-sided profiles.** Suppose \(L\) and \(U\) are both nonempty. No maximal element \(b_j\) can belong to \(L\), because an element of \(U\) would then be strictly above \(b_j\); dually no minimal \(a_i\) can belong to \(U\). Thus \(L\subseteq\{a_i\}\) and \(U\subseteq\{b_j\}\). Let \(j\) be the least index of a selected upper element \(b_j\). For all comparabilities \(l<u\) to hold, \(L\) must be a nonempty subset of \(\{a_1,\ldots,a_j\}\), and the remaining selected upper elements can be any subset of \(\{b_{j+1},\ldots,b_n\}\). This yields exactly \(v(1+v)^{n-j}((1+u)^j-1)\), with unique \(j\), proving the polynomial.

Setting \(u=v=1\), we have \(I_n(1)=(n+2)2^{n-1}\), and the mixed sum equals \(\sum_{j=1}^n(2^n-2^{n-j})=(n-1)2^n+1\). Consequently \(T_n(1,1)=(2n+1)2^n\).

**4. The limiting law.** There are \(I_n(1)-1\) lower-only profiles and the same number of upper-only profiles, plus \((n-1)2^n+1\) mixed profiles. Dividing by \((2n+1)2^n\) gives class probabilities tending to \(1/4,1/4,1/2\) with errors \(O(1/n)\). The empty–empty profile has vanishing mass.

For an ideal with a first missing \(a_i\), each of the \(n\) possible indices contributes exactly \(2^{n-1}\) profiles, so the index is uniform. Conditioned on it, the ideal size is distributed as \((i-1)+\operatorname{Bin}(n-1,1/2)\): the \(n-i\) remaining lower elements and \(i-1\) eligible upper elements are independent fair choices. The exceptional all-lower-selected family has relative ideal mass \(2/(n+2)\). Therefore the normalized lower-only size couples to \(1/2+Z\) with expected absolute error \(O(n^{-1/2})\); the upper-only family follows by duality.

For a mixed profile with first selected upper index \(j\), the number of profiles is \(w_j=2^n-2^{n-j}\). Since \(\sum_jw_j=(n-1)2^n+1\), the distribution of \(j\) differs in total variation by \(O(1/n)\) from the discrete uniform distribution on \(\{1,\ldots,n\}\). Conditional on \(j\), \(|L|\) has the \(\operatorname{Bin}(j,1/2)\) law conditioned to be nonzero, and \(|U|=1+\operatorname{Bin}(n-j,1/2)\), independently. The conditioning perturbation contributes \(O(1/n)\) on average (bound the unconditioned zero probability by \(2^{-j}\) and sum over \(j\)); binomial standard deviations divided by \(n\) are \(O(n^{-1/2})\). Coupling the discrete uniform index to \(Z\) completes the stated \(W_1\) rate. The bounds apply in both coordinates on the compact square \([0,2]^2\).

**5. Moments.** The limiting mixture gives
\[
\mathbb EX=\mathbb EY=\frac38,\quad
\mathbb EX^2=\mathbb EY^2=\frac5{16},\quad
\mathbb E(XY)=\frac1{48}.
\]
Subtracting the squared means yields the displayed covariance and variance and thus the correlation \(-23/33\). Since \((X_n,Y_n)\in[0,2]^2\), convergence in \(W_1\) gives convergence of all displayed moments; the limiting variance is positive, so the Pearson correlations converge as well.

## Verification
The standalone file `verify.py` directly enumerates all ternary comparison patterns for \(n=1,\ldots,5\), constructs each enlarged strict relation and checks transitivity without using the ideal/filter counting argument. Its independent binomial-coefficient implementation of the polynomial agrees coefficient-by-coefficient for all five sizes (578 nonalgebraic profiles in total); it checks the exact mixed-profile and scalar counts and rational moment identities. Additional exact finite distributions at \(n=10,30,100\) display convergence toward the asserted correlation. Execute with `python3 verify.py`; the recorded output is in `verification_output.txt`.

## Relationship to prior work
The random poset and its one-point extension mechanism are classical. In particular, earlier scalar height-two poset counts expressed through bipartite independent-set polynomials already imply the unrefined number of one-types after specializing to a staircase graph; **the scalar total is not presented as independently novel**. Dolinka and Mašulović (2010 preprint, 2012 journal) discuss generic posets and explicit downset/upset data in poset one-point extensions. A published published-finding corpus record, “Finite-parameter 1-type counting in the random poset is #P-complete” (2026), gives the general ideal/filter classification and the complexity of scalar counting. That broad classification supplies the **starting point** here but does not give the displayed bivariate polynomial for the staircase family, its three-segment limiting measure, its quantitative rate, or the limiting correlation.

Kitaev and Remmel (2010) and Dukes, Kitaev, Remmel and Steingrímsson (2010) develop enumerative theory of the \((2+2)\)-free/interval-order class to which these staircase posets belong, focusing on poset isomorphism classes, ascent sequences, and downset statistics. Their full accessible arXiv texts do not identify a one-point type-profile limit over individually named staircase parameters. This distinction is about statements and their implications, not a claim that earlier papers could not be used to derive the result.

## Limitations
The general ideal/filter correspondence and the classical interval-order characterization are existing results. The novelty claim is limited to the **exact joint profile and its derived asymptotic law** for the explicitly specified staircase family, not arbitrary posets. An equivalent derivation might exist in uncatalogued type-profile, Ferrers-poset, or probabilistic combinatorics literature. Finite enumerations corroborate but do not prove the all-\(n\) identity or its limit. No independent scientific audit is asserted.

## References
1. Sergey Kitaev and Jeffrey Remmel, “Enumerating \((2+2)\)-free posets by the number of minimal elements and other statistics,” arXiv:1004.3220, initially public 19 April 2010. https://arxiv.org/abs/1004.3220
2. Mark Dukes, Sergey Kitaev, Jeffrey Remmel, and Einar Steingrímsson, “Enumerating \((2+2)\)-free posets by indistinguishable elements,” arXiv:1006.2696, initially public 14 June 2010. https://arxiv.org/abs/1006.2696
3. Igor Dolinka and Dragan Mašulović, “A universality result for endomorphism monoids of some ultrahomogeneous structures,” arXiv:1009.2892, initially public 15 September 2010; Proceedings of the Edinburgh Mathematical Society 55 (2012), 635–656. https://arxiv.org/abs/1009.2892
4. “Finite-parameter 1-type counting in the random poset is #P-complete,” published published-finding corpus mathematical record, 4 October 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1
