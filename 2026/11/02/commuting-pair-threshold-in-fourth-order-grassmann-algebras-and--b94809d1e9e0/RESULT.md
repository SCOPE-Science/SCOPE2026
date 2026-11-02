# Commuting-pair threshold in fourth-order Grassmann algebras and the five-generator centralizer spectrum

## Finding

Let \(q\) be an odd prime power, let \(V=\mathbb F_q^n\) with \(n\ge 1\), and let \(J=\bigoplus_{i\ge1}\bigwedge^i V\) be the augmentation ideal of the exterior algebra. Put \(A_n=\bigwedge V/J^5\), so that products of exterior degree at least five vanish. Write \(c_n=\binom{n-1}{3}\), with the convention that a binomial coefficient is zero when its lower argument exceeds its nonnegative upper argument. Then the exact probability that two uniformly and independently chosen elements of \(A_n\) commute in the **ordinary associative-algebra sense** is

\[
\operatorname{cp}(A_n)=q^{-2n}\left(1+(q^n-1)(q+1)q^{-c_n}\right).
\]

More precisely, among all ordered commuting pairs, the ratio of those in which at least one element has nonzero exterior-degree-one part to those in which both degree-one parts vanish is

\[
R_n(q)=(q^n-1)(q+1)q^{-c_n}.
\]

For **every** odd prime power \(q\), this ratio is strictly greater than one for \(1\le n\le5\) and strictly smaller than one for \(n\ge6\). Thus a strict majority of commuting pairs has nonzero degree-one support through five generators, whereas a strict majority has both degree-one components zero from six generators onward. The same dichotomy persists asymptotically as \(q\to\infty\), and zero-degree-one-pair dominance becomes overwhelming when \(q\) is fixed and \(n\to\infty\).

At the first rank where cubic odd terms have two distinct nonzero wedge ranks, there is also a complete element-centralizer census for the **untruncated** exterior algebra \(E_5=\bigwedge(\mathbb F_q^5)\). Define

\[
N_2(q)=(q-1){5\brack2}_q,\qquad
N_4(q)={5\brack1}_q q^2(q-1)(q^3-1),
\]

where \({a\brack b}_q\) is the Gaussian binomial coefficient. If \(C_{E_5}(x)=\{y\in E_5:xy=yx\}\), then the complete centralizer-dimension enumerator is

\[
\sum_{x\in E_5}z^{\dim_{\mathbb F_q}C_{E_5}(x)}
=q^{17}z^{32}+q^{17}N_2(q)z^{30}+q^{17}N_4(q)z^{28}
+(q^5-1)q^{27}z^{24}.
\]

In particular, precisely four centralizer dimensions occur, and the number of ordered commuting pairs in \(E_5\) is

\[
q^{54}+(q^5-1)(q+1)q^{50}.
\]

## Assumptions and scope

All algebras here are unital associative algebras over the indicated finite field. Commutation is \(xy=yx\), not graded or super commutation. The odd-characteristic hypothesis is essential: in characteristic two every exterior algebra is ordinarily commutative, so the displayed odd-characteristic formulas do not apply. The filtration quotient \(A_n\) is canonical for the augmentation ideal, not an arbitrary choice of monomials. For \(n\le4\), \(A_n\) is the full exterior algebra. For \(n=5\), \(E_5\) differs from \(A_5\) by its central one-dimensional top-degree space, allowing the separate full-algebra centralizer refinement.

## Proof

**1. Reduce ordinary commutation to an odd wedge equation.** The exterior algebra is supercommutative. Write an element of \(A_n\) as \(a_0+a_1\), with its even and odd exterior-degree components. The even component commutes with everything; two odd components anticommute. Since the characteristic is odd,

\[
[a_0+a_1,b_0+b_1]=2a_1b_1.
\]

Set \(h=\binom n3\) and \(e=1+\binom n2+\binom n4\). The even component has dimension \(e\) and the odd one is \(V\oplus\bigwedge^3 V\), of dimension \(n+h\). Write two odd components as \(v+u\) and \(w+t\), with \(v,w\in V\) and \(u,t\in\bigwedge^3V\). Their product vanishes exactly when both homogeneous equations hold:

\[
v\wedge w=0,\qquad v\wedge t+u\wedge w=0.
\]

There are no additional equations because products of exterior degree at least five vanish.

**2. Count disjoint degree-one strata.** Put \(r=\binom{n-1}{3}\). For each nonzero \(v\in V\), the linear map \(L_v:\bigwedge^3V\to\bigwedge^4V\), \(u\mapsto v\wedge u\), has rank exactly \(r\): extend \(v\) to a basis and identify the image with \(v\wedge\bigwedge^3(V/\langle v\rangle)\). If \(v=w=0\), all \(q^{2h}\) pairs \((u,t)\) commute. If \(v\ne0\), the first equation forces \(w=\lambda v\), with \(q\) choices for \(\lambda\), and the second becomes \(v\wedge(t-\lambda u)=0\). Thus each \((v,\lambda)\) permits \(q^{2h-r}\) pairs \((u,t)\), for a total of \((q^n-1)q^{2h-r+1}\). Finally, if \(v=0,w\ne0\), the condition is \(u\wedge w=0\); it gives \((q^n-1)q^{2h-r}\) pairs. These cases are disjoint and exhaustive. Hence the number of commuting odd-component pairs is

\[
q^{2h}+(q^n-1)(q+1)q^{2h-r}.
\]

Even components are arbitrary and contribute \(q^{2e}\). Dividing by \(|A_n|^2=q^{2(e+n+h)}\) proves the probability formula and the stated ratio.

**3. Prove the uniform six-generator threshold.** For \(1\le n\le5\), one has \(r\le n-1\). Hence for every \(q\ge3\),

\[
R_n(q)>(q^n-1)q^{1-r}\ge(q^n-1)q^{2-n}=q^2-q^{2-n}>1.
\]

For \(n\ge6\), one has \(r\ge n+4\): it holds at \(n=6\) with \(r=10\), and \(\binom n3-\binom{n-1}{3}=\binom{n-1}{2}\ge10\) for subsequent increments while \(n+4\) grows only by one. Therefore

\[
R_n(q)<q^n(q+1)q^{-(n+4)}=\frac{q+1}{q^4}\le\frac4{81}<1
\]

for every odd prime power \(q\ge3\). These inequalities prove the strict majority statement in every odd characteristic. For fixed \(n\), the ratio is asymptotic to \(q^{n+1-r}\) as \(q\to\infty\); for fixed \(q\), it tends to zero as \(n\to\infty\) since \(r\) grows cubically.

**4. Classify all element centralizers in the full five-generator algebra.** In \(E_5\), the even part has dimension \(16\), and the odd part is \(V\oplus\bigwedge^3 V\oplus\bigwedge^5V\), also of dimension \(16\). The top-degree part is central. For a fixed element whose odd part is \(v+u+s\), the commutator map on a general odd element \(w+t+s'\) has the two components \(v\wedge w\in\bigwedge^2V\) and \(v\wedge t+u\wedge w\in\bigwedge^4V\).

If \(v\ne0\), the first component forces \(w\) into the one-dimensional span of \(v\), contributing rank \(4\). Conditional on that, the second component has rank \(\binom43=4\) on the freely varying \(t\). The whole commutator map therefore has rank \(8\), so the centralizer has dimension \(32-8=24\). The number of elements in this stratum is \((q^5-1)q^{10+1+16}=(q^5-1)q^{27}\).

If \(v=0\), the commutator rank is the rank of \(T_u:V\to\bigwedge^4V\), \(w\mapsto u\wedge w\). The canonical identification \(\bigwedge^3 V\cong\bigwedge^2V^*\otimes\bigwedge^5V\) identifies this map (up to an invertible change of coordinates and a nonzero scalar) with the contraction map of an alternating bilinear form on the five-dimensional space \(V\). Its rank is \(0\), \(2\), or \(4\); rank zero occurs exactly when \(u=0\). A rank-two alternating form is specified by its three-dimensional radical and a nonzero alternating form on the two-dimensional quotient. Consequently, there are \((q-1){5\brack2}_q\) such \(u\). A rank-four alternating form is specified by its one-dimensional radical and a nondegenerate alternating form on the four-dimensional quotient. The latter are counted by

\[
\frac{|\operatorname{GL}_4(q)|}{|\operatorname{Sp}_4(q)|}
=q^2(q-1)(q^3-1).
\]

Hence there are \({5\brack1}_q q^2(q-1)(q^3-1)\) rank-four \(u\). For each \(u\), the even component and the top-degree odd component are arbitrary, supplying \(q^{16+1}=q^{17}\) elements. Their centralizer dimensions are \(32\), \(30\), or \(28\), respectively. These are all elements, and adding their \(q^{\dim C(x)}\) centralizer sizes proves the enumerator and the commuting-pair formula. The latter also agrees with the general formula for \(A_5\), multiplied by \(q^2\) for the two independent top-degree coordinates in \(E_5\).

## Verification

The accompanying standard-library program `verify.py` constructs wedge multiplication from oriented subset masks, calculates finite-field matrix ranks by Gaussian elimination, and compares raw centralizer-fiber counts with the formulas. It exhaustively checks every odd element for \((n,q)=(2,3),(3,3),(3,5),(4,3)\). It also exhaustively enumerates all \(q^{10}\) cubic forms for \(n=5\) and \(q=2,3\), confirming that their wedge-map ranks are exactly \(0,2,4\) with the asserted frequencies. It independently samples nonzero-linear-part centralizer ranks at \(n=5,6,7\) over fields of orders \(3,5\), and builds direct \(32\times32\) associative commutator matrices for forced and random elements of the full five-generator algebra over \(\mathbb F_3\) and \(\mathbb F_5\) and checks both pair-count expressions at three odd field orders. The output ends in `VERIFY_OK` when all checks pass.

The exhaustive computations concern only their stated finite parameter ranges; the arbitrary-rank and arbitrary-field assertions are proved algebraically above.

## Relationship to prior work

Domokos and Zubor (2014, published 2015) established the connection between commutative subalgebras of Grassmann algebras and square-zero subspaces of the odd part, and determined maximal commutative-subalgebra dimensions. Bovdi and Leung (arXiv first public 2018-03-09) further constructed maximal commutative Grassmann subalgebras using intersecting set systems. The graded commutation reduction is classical and is **not** claimed as new here. Neither of those inspected primary texts presents a finite-field commuting-pair formula for the fourth radical truncation or the complete five-generator element-centralizer dimension spectrum. Fulman and Guralnick (2018) give finite-field commuting-pair formulas for classical matrix, unitary and symplectic Lie algebras, not these exterior-algebra quotients. General results on commuting probabilities for finite rings also do not by themselves compute the two explicit invariants here. The new claim is the exact parameter-wide counts and the induced rank-six dominance boundary, not the supercommutativity or alternating-form classification used in the proof.

## Limitations

The commuting-pair formula is for the fourth-order augmentation quotient, not for the full Grassmann algebra in arbitrary rank. The full-algebra centralizer distribution is established only at five generators. Characteristic two is excluded from these formulas because ordinary commutation then becomes automatic. No formula for all dimensions of maximal commutative subalgebras is claimed. Although the named primary texts and semantic research records were compared by statements and implications, unindexed or inaccessible sources might contain equivalent point-count formulas; no global priority certificate is asserted. The finite checks are corroboration rather than a proof of the infinite family.

## References

1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916, first posted 2014-03-12. https://arxiv.org/abs/1403.2916
2. V. A. Bovdi and H.-H. Leung, *Maximal commutative subalgebras of a Grassmann algebra*, arXiv:1803.03457, first posted 2018-03-09. https://arxiv.org/abs/1803.03457
3. J. Fulman and R. Guralnick, *Enumeration of commuting pairs in Lie algebras over finite fields*, arXiv:1611.05499, Annals of Combinatorics 22 (2018), 295–316. https://arxiv.org/abs/1611.05499
4. S. M. Buckley and D. MacHale, *Commuting probability for subrings and quotient rings*, Journal of Algebra, Combinatorics, Discrete Structures and Applications 4 (2017), 189–196. https://www.acarindex.com/journal-of-algebra-combinatorics-discrete-structures-and-applications/commuting-probability-for-subrings-and-quotient-rings-1196332
