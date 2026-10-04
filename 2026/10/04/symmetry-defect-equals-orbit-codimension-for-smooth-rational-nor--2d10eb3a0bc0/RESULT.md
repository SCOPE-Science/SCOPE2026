# Symmetry defect equals orbit codimension for smooth rational normal scrolls
## Finding
Let \(k\ge2\) and \(d\ge k\). A smooth rational normal scroll of dimension \(k\) and degree \(d\) has the form
\[
S( a_1,\ldots,a_k)=\mathbb P(E)\subset \mathbb P^{d+k-1},\qquad E=\bigoplus_{i=1}^k\mathcal O_{\mathbb P^1}(a_i),
\]
with \(1\le a_1\le\cdots\le a_k\) and \(\sum_i a_i=d\). Its projective automorphism group satisfies
\[
\dim \operatorname{Aut}_{\mathbb P}(S)
=k^2+2+h^1(\mathbb P^1,\operatorname{End}E)
=k^2+2+\sum_{i>j}\max\{a_i-a_j-1,0\}.
\]

Let \(\mathcal R_{d,k}\) denote the locus of smooth rational normal scrolls of dimension \(k\) and degree \(d\), modulo no projective equivalence, inside the corresponding Hilbert scheme. Each splitting type is a single \(\operatorname{PGL}_{d+k}\)-orbit, and the balanced type is dense in \(\mathcal R_{d,k}\). Therefore
\[
\operatorname{codim}_{\mathcal R_{d,k}}\bigl(\operatorname{PGL}_{d+k}\cdot S(a_1,\ldots,a_k)\bigr)
=h^1(\mathbb P^1,\operatorname{End}E).
\]
Thus the excess symmetry above the balanced value is exactly the orbit codimension in the scroll locus.

Writing \(d=qk+s\) with \(0\le s<k\), the unique balanced type is
\[
(q,\ldots,q,q+1,\ldots,q+1),
\]
with \(k-s\) copies of \(q\) and \(s\) copies of \(q+1\). It is the unique open orbit and has projective automorphism dimension \(k^2+2\). If \(d\ge k+1\), the unique least-balanced type
\[
(1,\ldots,1,d-k+1)
\]
has
\[
h^1(\mathbb P^1,\operatorname{End}E)=(k-1)(d-k-1),
\qquad
\dim \operatorname{Aut}_{\mathbb P}(S)=(k-1)d+3,
\]
and is the unique orbit of maximal codimension among smooth scrolls with fixed \(d,k\).

## Assumptions and scope
The ground field is \(\mathbb C\). Only smooth rational normal scrolls are considered, so every \(a_i\) is positive. The automorphism dimension means the dimension of the algebraic group of automorphisms induced by projective transformations of the tautological embedding. Finite extra components, such as the ruling swap of a balanced quadric surface, do not change the dimension. The codimension statement is inside the smooth-scroll locus \(\mathcal R_{d,k}\), not inside the full Hilbert scheme of all schemes with the same Hilbert polynomial.

## Proof
For the tautological projective bundle \(S=\mathbb P(E)\), projective automorphisms in the identity component fit dimension-wise into the standard projective-bundle sequence
\[
1\longrightarrow \operatorname{Aut}_{\mathbb P^1}(E)/\mathbb G_m
\longrightarrow \operatorname{Aut}_{\mathbb P}(S)
\longrightarrow \operatorname{PGL}_2
\longrightarrow 1.
\]
Surjectivity on the base follows because every automorphism of \(\mathbb P^1\) pulls each \(\mathcal O(a_i)\) back to an isomorphic line bundle. The kernel is the bundle-automorphism group modulo scalar homotheties. Since \(\operatorname{Aut}(E)\) is a Zariski-open subset of \(H^0(\operatorname{End}E)\),
\[
\dim \operatorname{Aut}_{\mathbb P}(S)=h^0(\operatorname{End}E)-1+3=h^0(\operatorname{End}E)+2.
\]

Now \(\operatorname{End}E\) has rank \(k^2\) and degree zero on \(\mathbb P^1\). Riemann--Roch gives
\[
h^0(\operatorname{End}E)-h^1(\operatorname{End}E)=k^2.
\]
Using \(H^1(\mathbb P^1,\mathcal O(m))\) of dimension \(\max\{-m-1,0\}\), the splitting of \(\operatorname{End}E\) yields
\[
h^1(\operatorname{End}E)=\sum_{i>j}\max\{a_i-a_j-1,0\}.
\]
This proves the automorphism formula. The defect vanishes exactly when no two \(a_i\) differ by at least two, which is exactly the balanced condition.

Harris's degeneration theorem for rational normal scrolls orders splitting types by balance: the balanced scroll degenerates to every less-balanced splitting type of the same dimension and degree. Since the splitting type determines the projective-equivalence class, the balanced projective orbit is dense in the scroll locus. Hence the codimension of the orbit of \(S(a_1,\ldots,a_k)\) is the drop in orbit dimension from the balanced orbit. Because
\[
\dim(\operatorname{PGL}_{d+k}\cdot S)=(d+k)^2-1-\dim \operatorname{Aut}_{\mathbb P}(S),
\]
that drop is exactly \(h^1(\operatorname{End}E)\).

For the sharp upper bound, put \(b_i=a_i-1\ge0\) and \(e=d-k=\sum_i b_i\). When \(e\ge1\),
\[
\begin{aligned}
\sum_{i>j}\max\{b_i-b_j-1,0\}
&\le \sum_i(i-1)(b_i-1)_+\\
&\le (k-1)\sum_i(b_i-1)_+\\
&\le (k-1)(e-1).
\end{aligned}
\]
Equality in the last inequality forces exactly one positive \(b_i\); sortedness then forces \(b_k=e\), and equality holds throughout. Thus the unique maximizer is \(a=(1,\ldots,1,d-k+1)\), with defect \((k-1)(d-k-1)\). Adding the balanced baseline \(k^2+2\) gives \((k-1)d+3\).

## Verification
The standalone script `verify_scroll_aut.py` independently enumerates every positive nondecreasing splitting type for \(2\le k\le6\) and \(k\le d\le22\), totaling 2212 types. For each type it compares the direct \(H^0(\operatorname{End}E)\) sum with the cohomological defect formula, identifies the unique balanced minimizer and least-balanced maximizer, and checks the closed-form extremal dimensions. It also checks all 1225 surface types with \(1\le a\le b<50\) against the published surface formula \(6\) for \(a=b\) and \(b-a+5\) for \(a<b\). The replay output is stored in `verification_output.txt`.

The finite computation is only a consistency check. The formulas and uniqueness statements for all \(k,d\) follow from the proof above.

## Relationship to prior work
Ma gives the projective-bundle automorphism exact sequence explicitly for the rank-three bundles used to realize three-dimensional rational normal scrolls; the first arXiv version is dated 14 February 2013. Harris's classical degeneration theorem orders rational normal scrolls by balance, and Ramkumar gives a modern statement of that theorem and identifies the unique least-balanced degeneration. Ferapontov and Kruglikov compute the full projective symmetry algebra for rational normal scroll surfaces \(S_{a,b}\), giving dimension \(6\) for \(a=b\) and \(b-a+5\) for \(a<b\), which is exactly the \(k=2\) specialization of the formula above.

The statement here combines these ingredients into an all-dimensional fixed-\((d,k)\) theorem: the symmetry excess is identified with the exact projective-orbit codimension, and both extremal splitting types and their sharp dimensions/codimensions are determined. Searches of the cited scroll literature and a research-result database did not locate this cohomological orbit-codimension formula or the all-dimensional sharp extremal statement.

## Limitations
The result does not classify disconnected components of the projective automorphism group, singular scrolls with zero summands, or non-scroll points in the ambient Hilbert component. The codimension is a set-theoretic orbit codimension inside the smooth-scroll locus; no assertion is made here about scheme-theoretic multiplicities or normality of orbit closures. General projective-bundle deformation theory makes the appearance of \(h^1(\operatorname{End}E)\) natural, so the remaining originality risk is that an equivalent all-dimensional codimension statement may exist under different terminology even though it was not found in the checked sources.

## References
1. S. Ma, *Rationality of some tetragonal loci*, arXiv:1302.3367v1 (14 February 2013); Algebraic Geometry 1 (2014), 52--76, doi:10.14231/AG-2014-014.
2. J. Harris, *A bound on the geometric genus of projective varieties*, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 8 (1981), 35--68, Section 3'.
3. R. Ramkumar, *On Rees algebras of 2-determinantal ideals*, J. London Math. Soc. 109 (2024), e12821, doi:10.1112/jlms.12821.
4. E. V. Ferapontov and B. Kruglikov, *Involutive Scroll Structures on Solutions of 4D Dispersionless Integrable Hierarchies*, Commun. Math. Phys. 406 (2025), Article 222, doi:10.1007/s00220-025-05479-z.
