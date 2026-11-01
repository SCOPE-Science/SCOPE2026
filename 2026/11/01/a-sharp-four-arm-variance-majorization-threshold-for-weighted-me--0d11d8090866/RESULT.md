# A sharp four-arm variance-majorization threshold for weighted metric stars

## Finding

Let a compact metric star have \(m\ge2\) arms of strictly positive lengths \(\ell_1,\ldots,\ell_m\), all meeting only at a common hub. Put \(T=\sum_i\ell_i\), \(p_i=\ell_i/T\), and \(S_j=\sum_i p_i^j\). Sample \(X,Y\) independently from normalized arclength on the complete network, and let \(D=d(X,Y)\) be their intrinsic shortest-path distance. Then
\[
\frac{\mathbb E D}{T}=S_2-\frac23S_3,\qquad
\frac{\mathbb E D^2}{T^2}=\frac23S_3+\frac12S_2^2-S_4,\qquad
\frac{\operatorname{Var}(D)}{T^2}=\frac23S_3+\frac12S_2^2-S_4-\left(S_2-\frac23S_3\right)^2.
\]
With \(m\) and \(T\) fixed, the two raw moments are strictly Schur-convex functions of the positive arm-length vector for every \(m\ge3\). The variance is strictly Schur-convex for \(m=3\), but **neither Schur-convex nor Schur-concave for every \(m\ge4\)**. When \(m=2\), the network is an interval, and all three moments are independent of the subdivision into arms. Therefore four arms constitute the exact threshold for failure of variance majorization.

An explicit strictly positive four-arm witness is
\[
p=\left(\frac9{20},\frac9{20},\frac9{100},\frac1{100}\right),\qquad
q=\left(\frac9{20},\frac9{20},\frac{19}{200},\frac1{200}\right).
\]
Although \(q\) strictly majorizes \(p\), the normalized variance *decreases* by exactly
\[
\frac{\operatorname{Var}_q(D)-\operatorname{Var}_p(D)}{T^2}=-\frac{203133}{8000000000}<0.
\]
For the same transfer the normalized mean and raw second moment increase by \(153/200000\) and \(1683/4000000\), respectively. These comparisons are exact.

## Assumptions and scope

Every arm is an ordinary closed interval \([0,\ell_i]\), with the zero endpoints identified at one hub. No other endpoints are identified; in particular, the space is a tree, not a flower made of cycles. Lengths are positive real numbers, \(m\) is an integer at least two, and the sampling distribution on each arm has density \(1/T\) with respect to arclength. Ordered independent sampling includes same-arm pairs; their diagonal has probability zero. Distances between positions \(x\) and \(y\) on the same arm equal \(|x-y|\), and on distinct arms equal \(x+y\).

For vectors \(p,q\) with the same positive coordinate sum, \(q\) *majorizes* \(p\) when the sums of the \(k\) largest coordinates of \(q\) are at least those for \(p\) for each \(1\le k<m\). Strict Schur-convexity means \(F(q)>F(p)\) whenever \(q\) majorizes \(p\) and the vectors are not permutations. All comparisons in this finding use a fixed number of arms and fixed total network length, not a fixed individual edge length.

## Proof

**Exact moments.** On one arm of length \(a\), integration over the ordered square yields
\[
\int_0^a\!\int_0^a |x-y|\,dx\,dy=\frac{a^3}{3},\qquad
\int_0^a\!\int_0^a |x-y|^2\,dx\,dy=\frac{a^4}{6}.
\]
For two *distinct* arms of lengths \(a,b\), direct integration gives
\[
\int_0^a\!\int_0^b(x+y)\,dy\,dx=\frac{a^2b+ab^2}{2},
\]
\[
\int_0^a\!\int_0^b(x+y)^2\,dy\,dx=\frac{a^3b+ab^3}{3}+\frac{a^2b^2}{2}.
\]
Summing the same-arm and ordered distinct-arm contributions, dividing by the square of the total length, and finally normalizing each distance by \(T\), gives precisely the first two displayed moment identities. Subtraction of the squared mean gives the variance identity. No approximations or infinite enumeration are used.

**Strict Schur-convexity of the two raw moments.** Write \(\mu=S_2-2S_3/3\) and \(M_2=2S_3/3+S_2^2/2-S_4\). For two distinct coordinates \(x=p_i\), \(y=p_j\) and \(R_2=\sum_{k\ne i,j}p_k^2\), differentiation in the unconstrained ambient coordinate space and the identity \(\sum p_k=1\) yield
\[
\frac{\partial_i\mu-\partial_j\mu}{x-y}=2(1-x-y),
\quad
\frac{\partial_i M_2-\partial_j M_2}{x-y}
=2\bigl((x+y)(1-x-y)+R_2\bigr).
\]
Both expressions are strictly positive when \(m\ge3\), since every remaining arm has positive length. Each is the differential criterion for a symmetric function to be strictly Schur-convex: any nontrivial majorization can be decomposed into finitely many pairwise averaging transfers. For \(m=2\), both quotients vanish because the geometric object is one interval of length \(T\).

**Three arms: variance remains strictly Schur-convex.** Let \(m=3\), and label the coordinates \(x,y,z>0\) with \(x+y+z=1\). Differentiating \(V=M_2-\mu^2\) and factoring exactly gives
\[
\frac{\partial_x V-\partial_y V}{x-y}=\frac{2z}{3}\bigl(1+12xyz\bigr)>0.
\]
The same formula holds for each pair by symmetry. The differential majorization criterion proves strict Schur-convexity for all positive three-arm vectors.

**Four arms: an exact reversal.** The displayed four-arm vectors \(p,q\) have equal sum one, and \(q\) is obtained by shifting \(1/200\) from the smaller fourth arm to the larger third arm. Consequently \(q\) strictly majorizes \(p\). Substitution into the proved moment identities gives
\[
\mu(q)-\mu(p)=\frac{153}{200000},\quad
M_2(q)-M_2(p)=\frac{1683}{4000000},\quad
V(q)-V(p)=-\frac{203133}{8000000000}.
\]
This disproves Schur-convexity of \(V\) for four arms.

**Every larger number of arms inherits the reversal.** Fix \(m>4\) and \(0<\eta<1\). Replace the first four components of each witness by \((1-\eta)p\) or \((1-\eta)q\), respectively, and append \(m-4\) identical positive coordinates \(\eta/(m-4)\). The resulting vectors have positive coordinates and unit sum, and the second is still obtained from the first by one transfer towards greater inequality. Since \(V\) is polynomial in the coordinates, its negative witness difference at \(\eta=0\) persists for all sufficiently small positive \(\eta\). Therefore \(V\) is not Schur-convex for any \(m\ge4\).

**Variance is not Schur-concave for \(m\ge4\).** At the uniform vector \(u=(1/m,\ldots,1/m)\), the pair-transfer derivative quotient of \(V\), interpreted continuously at equal coordinates, equals
\[
\left.\frac{\partial_i V-\partial_j V}{p_i-p_j}\right|_{p=u}
=\frac{2(m-2)(3m+4)}{3m^3}>0.
\]
This identity follows by substituting \(p_i=1/m\) into the two quotient formulas above, and applying \((\partial_i V-\partial_j V)/(p_i-p_j)=(\partial_iM_2-\partial_jM_2)/(p_i-p_j)-2\mu(\partial_i\mu-\partial_j\mu)/(p_i-p_j)\). Thus the variation \((1/m+\varepsilon,1/m-\varepsilon,1/m,\ldots)\), which strictly majorizes \(u\) for \(0<\varepsilon<1/m\), raises \(V\) for sufficiently small positive \(\varepsilon\). This disproves Schur-concavity for all \(m\ge4\), completing the sharp classification.

## Verification

The accompanying `verify.py` evaluates the independent same-arm/distinct-arm double-integral formulas using exact rational arithmetic, checks the symbolic pair-transfer polynomial identities, and reproduces the rational four-arm witness and its positive-length extensions. It uses Python 3 with SymPy. Running `python verify.py` produced `PASS 237 exact algebra/integral/majorization checks`. The formal proof for every positive length and every dimension of the parameter simplex is the algebra and majorization argument above; finite examples are independent checks, not an exhaustive proof.

## Relationship to prior work

Dahl's 2007 study of majorization and distances in trees is about *vertex-to-vertex distance vectors measured from a specified vertex*, not centered moments of the random distance between two arclength-uniform points on a weighted tree. Garijo, Márquez and Silveira's arXiv paper (first publicly posted in 2021) gives continuous-network **mean-distance** methods, including for weighted trees; its full text explicitly focuses on first moments and algorithms, rather than the centered second moment and its Schur-majorization phase transition. Mălin and Rovența (2015) study convex functions and majorization in \(K\)-spiders as nonpositively curved metric spaces, particularly Jensen–Popoviciu inequalities and extrema of convex flow functions; their accessible full text does not compute pairwise arclength-distance variance. Earlier classical mean-distance work on graph-shaped domains similarly motivates the observable but does not supply this four-arm classification in the accessible descriptions.

A related prior calculation for metric **flowers of circles** reports a four-petal variance-majorization threshold, but each petal in that topology is a circle with two routes between points. A metric star is instead a tree with a unique path between points; the exact moment expressions here differ and do not follow by inserting parameters into the flower expressions. Results about mean distance and stochastic extremality for **equilateral** metric trees concern changing tree topology at fixed unit edges, whereas the present theorem holds one star topology fixed and changes its strictly positive edge lengths. Searches of relevant mathematical research records did not identify a statement equivalent to the moment formulas *plus* sharp variance majorization classification. Failure to find one does not prove worldwide priority.

## Limitations

No global extrema of \(V\) for \(m\ge4\) are asserted, and a negative Schur-convexity witness does not imply that balanced lengths fail to be globally optimal. The result does not cover cycles, arbitrary trees beyond a one-hub star, nonuniform sampling, or any property of vertex-only sampling. The full text of Dahl's article was not accessible in the materials inspected, and older classical mean-distance sources were not fully inspected; an independently discovered historical equivalent would affect the originality assessment. The general first-moment weighted-tree algorithm may recover the mean formula, which is stated here as background to the new joint classification, not as an independent priority claim.

## References

1. G. Dahl, *Majorization and distances in trees*, Networks 50 (2007), 251–257. DOI: https://doi.org/10.1002/net.20202. First publicly published 2007-09-04. Abstract and publication metadata consulted; complete text not accessible.
2. D. Garijo, A. Márquez and R. I. Silveira, *Continuous mean distance of a weighted graph*, arXiv:2103.11676v1, first posted 2021-03-22; https://arxiv.org/abs/2103.11676. Full open-access preprint inspected, especially Introduction and Sections 3–4.
3. M. Mălin and I. Rovența, *Some Remarks on Convex Network Flows for K-Spiders*, Mathematical Problems in Engineering (2015), article 710516. DOI: https://doi.org/10.1155/2015/710516. Open-access full text inspected.
4. D. Garijo, A. Márquez and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, Results in Mathematics 78 (2023), article 139. DOI: https://doi.org/10.1007/s00025-023-01902-w. Later open-access publication of reference 2.
