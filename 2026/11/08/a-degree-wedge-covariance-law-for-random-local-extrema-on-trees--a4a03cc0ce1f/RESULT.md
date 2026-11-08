# A degree–wedge covariance law for random local extrema on trees

## Finding

Let \(T=(V,E)\) be an arbitrary fixed simple tree with \(|V|\ge 2\). Give its vertices independent identically distributed continuous real labels. Let \(M\) count vertices whose label exceeds those of all their neighbors, and let \(L\) count vertices whose label is below those of all their neighbors. Endpoints of a path are included as local extrema.

Write \(d_v\) for a vertex degree and, for positive integers \(a,b\), set
\[
F(a,b)=\frac{a+b+1}{ab(a+1)(b+1)}-\frac{1}{ab\binom{a+b}{a}} >0.
\]
Then the exact distribution-free, all-tree covariance identity is
\[
\boxed{\operatorname{Cov}(M,L)=
-\sum_{v\in V}\frac{1}{(d_v+1)^2}
+2\sum_{\{u,v\}\in E}F(d_u,d_v)
-2\sum_{\{u,v\}:\operatorname{dist}_T(u,v)=2}
\frac{F(d_u,d_v)}{d_u+d_v+1}.}
\]
In particular, for distinct vertices \(u,v\), the mixed indicator covariance is strictly positive at distance one, strictly negative at distance two, and zero at distances at least three. At distance two its magnitude is exactly \(F(d_u,d_v)/(d_u+d_v+1)\), independent of the intermediate vertex's degree.

For the path \(P_n\) with \(n\ge4\),
\[
\boxed{\operatorname{Cov}(M,L)=\frac{8n-37}{180}.}
\]
Thus its covariance changes sign between \(n=4\) and \(n=5\). For the star \(K_{1,n-1}\) with \(n\ge3\),
\[
\boxed{\operatorname{Cov}(M,L)=
-\frac{(n-2)(n^3+2n^2-9n-6)}{12n^2}<0.}
\]
The smallest fixed-tree order admitting positive mixed extrema covariance is five vertices; the path on five vertices gives \(1/60\).

## Assumptions and scope

The underlying tree is deterministic. The randomness lies **only** in independently assigned continuous vertex labels; equivalently, all \(|V|!\) relative label orders are equally likely. The labels need not be uniform, symmetric or bounded. A local maximum/minimum uses all adjacent neighbors, with no artificial boundary labels. A tree of order two is allowed and has covariance zero. No claim is made about independent random edge orientations, randomly sampled tree topology or non-tree graphs.

## Proof

Apply the common-label probability-integral transform: the relative order is unchanged by replacing the labels with independent \(U[0,1]\) variables \(X_v\). Write \(I_v^+=\mathbf1\{X_v>X_w\ \forall w\sim v\}\) and \(I_v^-=\mathbf1\{X_v<X_w\ \forall w\sim v\}\). Since the \(d_v+1\) values in a closed neighborhood are exchangeable and have no ties,
\[
\mathbb E I_v^+=\mathbb E I_v^-=\frac1{d_v+1}.
\]
Because \(d_v\ge1\), a vertex cannot be both a maximum and minimum. Therefore \(\operatorname{Cov}(I_v^+,I_v^-)=-1/(d_v+1)^2\).

Now fix different vertices \(u,v\), with \(a=d_u,b=d_v\). If \(\operatorname{dist}_T(u,v)\ge3\), the two closed neighborhoods do not intersect; their indicators are independent. If \(u,v\) are adjacent, condition on \(X_u=x,X_v=y\). Their other neighbor sets are disjoint (a tree has no triangles). The simultaneous maximum/minimum event requires \(y<x\); hence
\[
\begin{aligned}
\Pr(I_u^+=I_v^-=1)
&=\int_0^1\!\int_0^x x^{a-1}(1-y)^{b-1}\,dy\,dx\\
&=\frac1{ab}-\frac{(a-1)!(b-1)!}{(a+b)!}.
\end{aligned}
\]
Subtracting \(1/((a+1)(b+1))\) produces \(F(a,b)\), since the factorial quotient equals \(1/[ab\binom{a+b}{a}]\).

If \(\operatorname{dist}_T(u,v)=2\), denote their unique common neighbor by \(w\). Conditional on \(X_w=z\), the two remaining neighbor sets are disjoint, and the respective probabilities are \((1-z^a)/a\) and \((1-(1-z)^b)/b\). Thus
\[
\Pr(I_u^+=I_v^-=1)
=\frac1{ab}\int_0^1(1-z^a)(1-(1-z)^b)\,dz.
\]
Using \(\int_0^1z^a(1-z)^b\,dz=a!b!/(a+b+1)!\), subtract the product of the marginal means and simplify:
\[
\begin{aligned}
\operatorname{Cov}(I_u^+,I_v^-)
&=\frac1{ab}\left(\frac{a!b!}{(a+b+1)!}
-\frac1{(a+1)(b+1)}\right)\\
&=-\frac{F(a,b)}{a+b+1}.
\end{aligned}
\]
The result is symmetric in \(u,v\), so expanding \(\operatorname{Cov}(\sum_u I_u^+,\sum_v I_v^-)\) counts each unordered edge and each unordered distance-two pair twice. This proves the tree identity.

For strict positivity, note that \(\binom{a+b}{a}\ge a+b\) for integers \(a,b\ge1\), while
\[
\frac{a+b+1}{(a+1)(b+1)} >\frac1{a+b},
\]
because \((a+b)^2-ab>1\). The displayed formula for \(F\) therefore gives \(F(a,b)>0\). The signed pointwise dependence conclusions follow.

For a path with \(n\ge5\), its two leaves have degree one, and all remaining vertices have degree two. The needed kernel values are
\[
F(1,2)=\frac16,\qquad F(2,2)=\frac7{72}.
\]
There are two edges of degree type \((1,2)\), \(n-3\) edges of type \((2,2)\), two distance-two pairs of degree type \((1,2)\), and \(n-4\) of type \((2,2)\). Inserting them into the general formula gives
\[
-\frac12-\frac{n-2}{9}
+2\left(\frac13+\frac{7(n-3)}{72}\right)
-2\left(\frac1{12}+\frac{7(n-4)}{360}\right)
=\frac{8n-37}{180}.
\]
For \(n=4\), direct insertion of its two degree-\((1,2)\) distance-two pairs yields the same expression, \(-1/36\). For \(n=3\), the path covariance is \(-1/9\); for the two-vertex tree it is zero.

For a star, the central degree is \(n-1\), each leaf degree one, \(F(1,n-1)=1/(2n)\), and all \(\binom{n-1}{2}\) leaf pairs are at distance two with \(F(1,1)=1/4\). Hence
\[
\begin{aligned}
\operatorname{Cov}(M,L)
&=-\frac1{n^2}-\frac{n-1}{4}
+\frac{n-1}{n}-\frac{(n-1)(n-2)}{12}\\
&=-\frac{(n-2)(n^3+2n^2-9n-6)}{12n^2}.
\end{aligned}
\]
The numerator factor in parentheses is positive for \(n\ge3\): it equals twelve at \(n=3\) and increases thereafter. At orders two, three and four, all tree types are respectively the edge, three-vertex path, and either the four-vertex path or four-vertex star, each with nonpositive covariance. Since \(P_5\) has covariance \(1/60\), five is the minimal order with positive covariance. This completes the proof.

## Verification

The accompanying `verify.py` is standalone Python 3 code using only the standard library. Run `python verify.py`. It compares the theoretical all-tree formula against independent exhaustive permutation enumeration for every unlabeled-tree shape on two through seven vertices, and for paths and stars through eight vertices. It additionally checks the exact distance-two beta-function identity and kernel positivity for every integer degree pair between one and 39, and the path/star formulas with exact rational arithmetic. The run reported `PASS 3086 exact checks`; no floating-point fitting or simulation substitutes for the all-tree proof.

## Relationship to prior work

Baldi, Rinott and Stein study marginal counts and normal approximation for local extrema of iid random functions on fixed graphs; their accessible 1989 conference paper gives the marginal expectation and one-sided variance examples. Kitaev reviews peak/valley statistics and their marginal enumerators for one-line permutations. Clark treats local extrema along root paths when the **tree itself** is sampled uniformly and labels are fixed, a different ensemble. These sources motivate the question but the inspected statements do not supply the arbitrary-fixed-tree mixed extrema kernel or its distance-two sign identity.

Independently orienting edges on a tree gives a different source/sink probability law: neighboring orientations are independent there, whereas a ranking-induced orientation shares vertex labels and creates the nonzero distance-two term above. Accordingly, independent-orientation extrema-covariance formulas do not imply this identity. The path specialization should not be treated as independently established novelty absent a broader historical joint peak/valley comparison.

## Limitations

The proof concerns exact second moments only; it establishes no joint distribution, central limit theorem or extremum over all tree shapes. The availability of a longer 1989 book chapter was limited, so hidden historical derivations of an equivalent mixed moment remain a priority risk. The cited earlier random-tree and permutation results do not, by their titles or abstracts alone, prove the absence of equivalent results. The standalone finite enumeration is corroborative, not a proof for arbitrary order.

## References

- P. Baldi, Y. Rinott, C. Stein, *On the Distribution of the Number of Local Minima of a Random Function on a Graph*, Advances in Neural Information Processing Systems 2 (1989), pp. 727–732. https://papers.nips.cc/paper_files/paper/1989/file/d947bf06a885db0d477d707121934ff8-Paper.pdf
- P. Baldi, Y. Rinott, *Asymptotic Normality of Some Graph-Related Statistics*, Journal of Applied Probability 26 (1989), pp. 171–175. https://doi.org/10.2307/3214327
- L. Clark, *Local Extrema in Random Trees*, International Journal of Mathematics and Mathematical Sciences 2005 (2005), pp. 3867–3882. https://doi.org/10.1155/IJMMS.2005.3867
- S. Kitaev, *Introduction to Partially Ordered Patterns*, arXiv:math/0603122, submitted 2006-03-05. https://arxiv.org/abs/math/0603122
