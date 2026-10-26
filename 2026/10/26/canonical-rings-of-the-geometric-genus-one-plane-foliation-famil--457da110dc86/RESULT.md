# Canonical rings of the geometric-genus-one plane-foliation family

## Finding
For each integer \(n\ge 2\), consider the reduced-model surface \(S_n\) in Example 7.1 of Guo–Hu–Lü, arXiv:2610.19788v1, and its induced foliation \(\mathcal F_n\). The complete graded foliated canonical ring
\[
R_n=\bigoplus_{m\ge 0}H^0(S_n,\mathcal O_{S_n}(mK_{\mathcal F_n}))
\]
is the normal three-dimensional graded semigroup algebra
\[
R_n\cong\mathbb C[U,T_0,\ldots,T_{n-1}]/I_2\!
\begin{pmatrix}T_0&T_1&\cdots&T_{n-2}\\T_1&T_2&\cdots&T_{n-1}\end{pmatrix},
\quad\deg U=1,\quad\deg T_j=j+2.
\]
Here \(I_2\) denotes the ideal of all two-by-two minors, empty when \(n=2\). Explicitly the generators are represented by homogeneous plane sections \(U=Y\) and \(T_j=X^jYZ\).

The complete plurigenera and Hilbert series are
\[
h^0(S_n,mK_{\mathcal F_n})=
\#\{(a,b,c)\in\mathbb Z_{\ge0}^3:a+b+c=m,\ b\ge c,\ 0\le a\le(n-1)c\},
\]
\[
\sum_{m\ge0}h^0(S_n,mK_{\mathcal F_n})t^m
=\frac{1+t^3+t^4+\cdots+t^n}{(1-t)(1-t^2)(1-t^{n+1})},
\]
with the numerator interpreted as \(1\) for \(n=2\). In particular the canonical-model surface defined as \(\operatorname{Proj}R_2\) is \(\mathbb P(1,2,3)\); the equality-volume example has a polynomial canonical ring with three generators in degrees \(1,2,3\). For every \(n\), \(\operatorname{Proj}R_n\) is a normal projective toric surface with an explicit weighted determinantal presentation.

## Assumptions and scope
Work over \(\mathbb C\). Fix an integer \(n\ge2\) and an irrational real number \(\alpha\) with \(1<\alpha<n/(n-1)\). Guo–Hu–Lü define a degree-two foliation on the plane with affine vector field
\[
V=x(1-nx+\alpha y)\partial_x+y(2-(n-1)x+y)\partial_y.
\]
The reduced surface \(S_n\to\mathbb P^2\) comes from two point blowups above \(O=[0:0:1]\) and \(n\) point blowups above \(B=[1:0:0]\). Write \(H\) for the pullback of a line, and \(e_2\) and \(f_n\) for the total-transform exceptional basis elements at the final respective centers. The source establishes
\[
K_{\mathcal F_n}\sim H-e_2-f_n.
\]
The calculations below use the actual infinitely-near centers specified by the two linearizable local singularities, rather than treating the last exceptional valuations as ordinary multiplicities. No assertion is made for arbitrary foliated surfaces of volume \(1/6\).

## Proof
**1. Determine both divisorial valuations.** On the chart \(Z=1\) at \(O\), use \(x=X/Z\) and \(y=Y/Z\). The linearized vector field has eigenvalues \((1,2)\), with the coordinate branch \(y=0\) followed by the reduction. Its first two point blowups have local chart transformations \(y=xs\), then \(s=xw\), whence \(y=x^2w\). The last exceptional divisor therefore has \(v_{e_2}(x)=1\) and \(v_{e_2}(y)=2\). In particular
\[
v_{e_2}(X^aY^bZ^c)=a+2b
\]
for a nonzero homogeneous monomial viewed as a local function after trivializing \(\mathcal O_{\mathbb P^2}(m)\) by \(Z^m\).

At \(B=[1:0:0]\), put \(p=Y/X\) and \(q=Z/X\). Restricting the defining homogeneous one-form to \(X=1\) shows its lowest part is \(nq\,dp-p\,dq\); the tangent vector has weights \((1,n)\) on \((p,q)\). The non-reduced center follows the \(q=0\) separatrix. Indeed the blowup chart \(q=ps\) lowers the second weight from \(n\) to \(n-1\) and leaves the same configuration, so after \(n\) blowups the final exceptional valuation has \(v_{f_n}(p)=1\), \(v_{f_n}(q)=n\). The source's strict-transform class \(H-e_1-e_2-f_1\) for \(Y=0\) independently confirms that this branch meets only the first exceptional center above \(B\), not the later centers. Thus
\[
v_{f_n}(X^aY^bZ^c)=b+nc.
\]

**2. Identify the complete section spaces.** Since \(e_2\) and \(f_n\) are effective exceptional divisors on \(S_n\), every section of \(m(H-e_2-f_n)\) comes from a homogeneous degree-\(m\) plane polynomial whose pullback has divisorial valuation at least \(m\) at both final exceptional divisors. For a monomial with \(a+b+c=m\), the two conditions are
\[
a+2b\ge m,\qquad b+nc\ge m,
\]
equivalently \(b\ge c\) and \(a\le(n-1)c\). Distinct degree-\(m\) plane monomials have distinct local monomial initial forms for each monomial valuation. Hence no cancellation can remove a term whose weight is below the threshold; the admissible monomials form a basis in every degree, not just a spanning set.

**3. Determine generators and relations.** Let \(U=Y\) and \(T_j=X^jYZ\) for \(0\le j\le n-1\). For an admissible monomial \(X^aY^bZ^c\), express \(a\) as a sum of \(c\) integers \(j_1,\ldots,j_c\in[0,n-1]\), which is possible precisely because \(0\le a\le(n-1)c\). Then
\[
X^aY^bZ^c=U^{b-c}\prod_{i=1}^c T_{j_i}.
\]
There are no further relations involving \(U\), since \(Y\) and \(YZ\) are algebraically independent and the ratios of consecutive \(T_j\) recover the independent coordinate \(X\) on the fraction field. The kernel of the monomial map \(\mathbb C[T_0,\dots,T_{n-1}]\to\mathbb C[X,YZ]\), with \(T_j\mapsto X^jYZ\), is the classical prime ideal of two-by-two minors of the rational-normal-curve catalecticant. One direct proof is to sort a product of \(T\)'s by repeatedly applying \(T_iT_{j+1}=T_{i+1}T_j\): modulo these relations, its class is determined uniquely by the number of factors and their total index. Those are exactly the exponents of \(YZ\) and \(X\) in the image, so the displayed relations generate the full kernel. Saturation of the integer cone defined by \(b\ge c\ge0\) and \(0\le a\le(n-1)c\) proves normality.

**4. Compute the Hilbert series.** The monomial basis gives
\[
\begin{aligned}
H_n(t)&=\sum_{c\ge0}\sum_{a=0}^{(n-1)c}\sum_{b=c}^{\infty}t^{a+b+c}\\
&=\frac1{(1-t)^2}\left(\frac1{1-t^2}-\frac{t}{1-t^{n+1}}\right)\\
&=\frac{1+t^3+\cdots+t^n}{(1-t)(1-t^2)(1-t^{n+1})}.
\end{aligned}
\]
The pole at \(t=1\) has leading coefficient \((n-1)/(2(n+1))\). Thus the section-growth volume is \((n-1)/(2(n+1))\), agreeing independently with the source's Zariski-decomposition computation. At \(n=2\), there are no determinantal relations and the three generator degrees are \(1,2,3\); hence \(\operatorname{Proj}R_2\cong\mathbb P(1,2,3)\).

## Verification
Run the standalone exact-integer script `python3 verify_plurigenera.py`. It enumerates all admissible monomials and compares them with the rational generating-function coefficients for every \(2\le n\le10\) and \(0\le m\le55\), a total of 504 parameter-degree instances. Each enumerated monomial receives an explicit generator factorization. The script also verifies the degree-two equality example against independent weighted-partition counts. Its finite checks corroborate the symbolic proof; they are not substituted for its universal quantifiers.

## Relationship to prior work
Guo–Hu–Lü [1], Example 7.1 and Theorem 1.1, construct these foliations and determine their geometric genus and volumes, including the sharp equality example. They do not give the graded ring, all plurigenera, the minimal weighted generating system, or the determinantal equations of its Proj. They identify the more general higher-plurigenus question as future work. Hacon–Langer [2] give general birational boundedness, invariance and growth results for foliation pluricanonical systems, not this family-specific presentation. Lü [3] studies general foliated canonical-map bounds, not these single-section canonical maps. Xu [4] treats universal pluri-index bounds, not this family. The rational-normal-curve minor ideal and monomial valuation techniques are standard; their explicit connection here to the reduced-model canonical rings is the asserted specific finding.

## Limitations
The calculation applies only to the indicated complex family, its specified reduced surface and the standard canonical line bundle representative; no claim is made about all geometric-genus-one foliations, arbitrary birational singular models, or a moduli classification. The canonical-model assertion means \(\operatorname{Proj}\) of this graded ring, without asserting a complete foliation singularity classification there. The numerical checks are finite; the general theorem is algebraic. Scientific novelty is evaluated against inspected and searchable prior literature, not independently certified, and earlier implicit computations may exist.

## References
[1] Z. Guo, B. Hu and X. Lü, *The volume of foliated surfaces with geometric genus one*, arXiv:2610.19788v1 (first public 2026-10-14), Example 7.1 and Theorem 1.1. https://arxiv.org/html/2610.19788v1

[2] C. D. Hacon and A. Langer, *On birational boundedness of foliated surfaces*, arXiv:1910.07709, Introduction and Theorem 0.5. https://arxiv.org/abs/1910.07709

[3] X. Lü, *The canonical map of a foliated surface of general type*, arXiv:2410.08465, Introduction and §§3–4. https://arxiv.org/abs/2410.08465

[4] S. Xu, *Birational Automorphism Bounds for General-Type Foliations on Surfaces via Pluricanonical Indices*, arXiv:2608.29900, Introduction. https://arxiv.org/abs/2608.29900
