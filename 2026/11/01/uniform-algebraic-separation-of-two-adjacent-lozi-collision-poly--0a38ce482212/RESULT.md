# Uniform algebraic separation of two adjacent Lozi collision polynomials

## Finding

For the orientation-preserving Lozi family of Ou [1], consider the two canonical periodic-word collision equations associated with the adjacent sign words \((+,-,-,+,+,+)\) and \((+,-,-,-,+,+,+)\), of lengths six and seven. Let \(P_4(a,b)\) and \(P_5(a,b)\) be the explicit integer polynomials given below, and define the univariate Sylvester resultant \(R(b)=\operatorname{Res}_a(P_4,P_5)\), with the standard determinant convention.

**Theorem.** For every real \(b\in[0,1]\),

\[
\boxed{R(b)\le -\frac{5252318}{6322725}<0.}
\]

Consequently, for every such \(b\), the pair of formal collision equations \(P_4(a,b)=P_5(a,b)=0\) has **no common complex solution \(a\)**. This is a uniform algebraic statement: it concerns every root of the collision equations, not just real, sign-admissible periodic orbits. In particular, two genuine Lozi border collisions from these words cannot occur at the same parameter, even if their analytic formal continuations are considered.

## Assumptions and scope

The Lozi map is

\[
\Lambda_{a,b}(x,y)=\bigl(-a|x|-by+(a-b-1),\,x\bigr),
\qquad a>b+1,\quad0\le b\le1.
\]

For a word \(s=(s_0,\ldots,s_{N-1})\) with each \(s_j\in\{-1,1\}\), define the *formal periodic point* by cyclically applying the affine branches

\[
\Lambda_{s_j}(x,y)=(-s_j ax-by+a-b-1,x).
\]

A formal periodic point need not respect every prescribed sign. It is **collision-formal** when its last listed first coordinate, \(x_{N-1}\), is zero. At this point the final symbol can be taken with either sign, so the condition includes every physical border collision for that word. The two words above are \(\iota_{+,m,2}\) with \(m=4,5\) in [1]; their last zero-coordinate condition is the collision condition in [1, Proposition 3.5 and Theorem 6.6]. The present theorem strengthens admissible real-locus separation to separation of the **entire complex algebraic** equations, with a quantitative, \(b\)-uniform resultant gap.

Define the explicit polynomials

\[
\begin{aligned}
P_4(a,b)={}&a^5-(b+1)a^4+(b^2-1)a^3\\
&+(b^3-b^2+b-1)a^2+(b^4+b^2+1)a\\
&-b^5+b^4-b^3-b^2+b-1,\\[3pt]
P_5(a,b)={}&a^6-(b+1)a^5+(b^2-b-1)a^4\\
&+(b^3+2b-1)a^3+(b^4-b^3+b-1)a^2\\
&+(b^5+b^3-b^2+1)a\\
&-b^6+b^5-b^4+b^3-b^2+b-1.
\end{aligned}
\]

No assertion is made that every algebraic zero is sign-admissible, or that the true physical collision locus exists for all \(b\in[0,1]\). The theorem is an identity and inequality for the **formal collision equations** on the entire parameter strip. The nondegenerate case \(b>0\) is orientation-preserving; \(b=0\) is its degenerate tent-map boundary.

## Proof

**1. Affine recurrence and uniqueness.** Put \(C=a-b-1>0\), and for \(\sigma\in\{\pm1\}\) define

\[
Q_\sigma=\begin{pmatrix}-\sigma a&-b\\1&0\end{pmatrix},\qquad u=(C,0)^{\mathsf T}.
\]

For a sign word of length \(N\), successive affine compositions give \(z_N=M z_0+v\), where \(M=Q_{s_{N-1}}\cdots Q_{s_0}\) and \(v=\sum_{j=0}^{N-1}Q_{s_{N-1}}\cdots Q_{s_{j+1}}u\). If \(b>0\), the cone \(\lvert z_1\rvert\ge\lvert z_2\rvert\) is strictly expanded and preserved under every forward \(Q_\sigma\), since \(a-b>1\). The complementary strict cone \(\lvert z_2\rvert>\lvert z_1\rvert\) is strictly expanded and preserved under each backward \(Q_\sigma^{-1}\), since \((a-1)/b>1\). Thus no nonzero vector is fixed by \(M\) (either its forward or its backward orbit grows), and \(I-M\) is invertible. At \(b=0\), the eigenvalues of \(M\) are \(0\) and \(\pm a^N\), so \(I-M\) is again invertible. Consequently the formal periodic point exists uniquely and satisfies \(z_0=(I-M)^{-1}v\).

**2. The two collision polynomials.** Reading the second coordinate of \(z_0\), which is \(x_{N-1}\) by periodicity, gives

\[
x_{N-1}=\frac{e_2^{\mathsf T}\operatorname{adj}(I-M)v}{\det(I-M)}
=-\frac{C\,P_m(a,b)}{\det(I-M)},\qquad m=4,5.
\]

Ordinary exact multiplication and cancellation produce the displayed \(P_4,P_5\). The standalone program `verify_lozi.py` reconstructs both matrix products, checks exact divisibility by \(C\), and verifies both coefficient lists. Because \(C\ne0\) and \(I-M\) is invertible in the physical domain, every actual collision for either word satisfies its corresponding \(P_m=0\).

**3. Exact resultant certificate.** Compute the Sylvester determinant

\[
R(b)=\operatorname{Res}_a(P_4,P_5).
\]

An exact integer-polynomial calculation gives

\[
-R(b)=\sum_{k=0}^{30}c_k\,b^k(1-b)^{30-k},
\]

where the complete ordered coefficient vector \((c_0,\ldots,c_{30})\) is

\[
\begin{gathered}
(5,133,1698,13910,82399,376725,1384117,4197642,\\
10704416,23257071,43465817,70393416,99410297,\\
123226487,135272275,133373291,120803314,\\
103699756,86971606,72046909,57843940,\\
43349490,29180938,17091469,8475190,\\
3457434,1117524,269891,43711,3641,13).
\end{gathered}
\]

The identity is verified by exact symbolic polynomial operations, without floating-point evaluation, by the supplied code. In particular, all \(31\) coefficients are **strictly positive**. More quantitatively, direct exact rational comparison shows

\[
\min_{0\le k\le30}\frac{c_k}{\binom{30}{k}}
=\frac{5252318}{6322725},
\]

attained at \(k=16\). Since

\[
\sum_{k=0}^{30}\binom{30}{k}b^k(1-b)^{30-k}=1
\]

and every summand is nonnegative for \(0\le b\le1\), the bound on \(R\) follows, with both endpoints included. A shared complex root of \(P_4(\cdot,b)\) and \(P_5(\cdot,b)\) would force their resultant to vanish; the uniform strict inequality excludes this for every real \(b\) in the entire interval. \(\square\)

## Verification

Run `python verify_lozi.py` with a compatible SymPy installation. The script independently builds the affine-word matrices, checks both polynomial identities by exact division, recomputes the degree-30 resultant, obtains the full 31-term positive-coefficient certificate, and checks the exact rational bound. During preparation, every check completed successfully. These exact identities constitute a finite algebraic proof certificate, not a numerical sample of the interval. The cone argument independently verifies uniqueness of formal periodic points on the stipulated dynamical parameter domain.

## Relationship to prior work

Ou [1] defines the Lozi parameterization, formal itineraries, analytic continuations, and their border-collision condition. Its Introduction, Figure 2, and accompanying discussion already **observe** that the sign-admissible curves for fixed \(n\) and distinct \(m\) do not intersect. Such admissible-real-curve separation is **not** claimed here as an original result. The new assertion is the considerably stronger, quantitative **nonvanishing of the entire algebraic resultant**, for all real \(b\in[0,1]\) and all complex candidate values of \(a\). A geometrical assertion for admissible real curves cannot imply this polynomial statement: excluded formal roots can intersect outside the admissible real locus, including at complex \(a\). The result provides a global exact continuation/separation certificate for the adjacent length-six and length-seven words; it does not prove a general fixed-\(n\) theorem for every word length.

Sushko, Avrutin, and Gardini [2] study analytically represented stability-region boundaries for Lozi maps and the two-dimensional border-collision normal form. The accessible abstract concerns cycles with rotation number \(1/n\) near center bifurcations; its full text was not available in the inspected access routes, so possible equivalent formal-algebraic assertions there cannot be completely excluded. A search of related records did not reveal the explicit resultant or this uniform certificate. These searches are not a proof of publication priority.

## Limitations

The assertion is about two specific natural symbolic words and one real parameter interval. No all-word disjointness theorem, maximal parameter continuation, ordering of all physical bifurcation curves, or independence from all prior publications is asserted. The source already noted nonintersection of relevant **physical** curves graphically; our new object is their complete **formal algebraic** separation and uniform resultant bound. An independently obtained exact algebraic certificate in inaccessible or unindexed literature remains possible. A separate independent mathematical audit has not been performed.

## References

[1] D.-S. Ou, *Critical points in higher dimensions, I: Reverse order of periodic orbit creations in the Lozi family*, arXiv:2203.02326, first posted 2022-03-04, https://arxiv.org/abs/2203.02326. Sections 1, 2, 3, 4, 6 and Appendices A–B were inspected in the accessible full text.

[2] I. Sushko, V. Avrutin and L. Gardini, *Lozi map embedded into the 2D border collision normal form*, *Journal of Difference Equations and Applications* 29 (2023), 965–981, DOI:10.1080/10236198.2023.2205960. Abstract and classification information inspected; full text unavailable via the accessible route.
