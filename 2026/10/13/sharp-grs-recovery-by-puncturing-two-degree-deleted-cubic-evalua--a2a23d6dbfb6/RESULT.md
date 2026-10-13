# Sharp GRS recovery by puncturing two degree-deleted cubic evaluation families

## Finding

Let \(\mathbb F_q\) be any finite field. For \(r\in\{1,2\}\), let \(S\subseteq\mathbb F_q\) contain at least five distinct elements. Define the polynomial spaces \(V_1=\operatorname{span}_{\mathbb F_q}\{1,x,x^3\}\) and \(V_2=\operatorname{span}_{\mathbb F_q}\{1,x^2,x^3\}\), and the dimension-three evaluation codes
\[
C_r(S)=\left\{\bigl(f(t)\bigr)_{t\in S}: f\in V_r\right\}.
\]

For a finite set \(T\), write \(e_j(T)\) for the \(j\)-th elementary symmetric function of its elements; in particular \(e_1(T)=\sum_{t\in T}t\), and for \(|T|=6\), \(e_5(T)=\sum_{t\in T}\prod_{u\in T\setminus\{t\}}u\). Set \(E_1(T)=e_1(T)\) and \(E_2(T)=e_5(T)\) when \(|T|=6\). Assume the **arc condition**
\[
 e_r(\{a,b,c\})\ne0\qquad\text{for every three distinct }a,b,c\in S.
\]
Then every puncturing \(C_r(T)\), \(T\subseteq S\), with \(|T|\ge5\), is MDS, and is monomially equivalent over \(\mathbb F_q\) to a generalized Reed--Solomon code **if and only if**
\[
|T|=5\quad\text{or}\quad \bigl(|T|=6\ \text{and}\ e_{1}(T)=0\text{ when }r=1,\ \text{respectively }e_{5}(T)=0\text{ when }r=2\bigr).
\]
In particular, no puncturing retaining at least seven coordinates is GRS. For \(n=|S|\ge7\), let \(\delta_r(S)\) be the minimum number of deleted coordinates required to obtain a GRS puncturing. Then
\[
\delta_r(S)=\begin{cases}n-6,&\text{if some six-subset }T\subseteq S\text{ has }E_r(T)=0,\\n-5,&\text{otherwise.}\end{cases}
\]
Thus the minimum is exactly \(n-6\) or \(n-5\), never any other value. The minimum-deletion sets are exactly the complements of eligible six-subsets in the former case and all complements of five-subsets in the latter.

The eligible six-subsets form a *five-packing*: any five-subset of \(S\) lies in at most one eligible six-subset. Consequently, if \(B_r(S)\) is their number, then \(6B_r(S)\le\binom n5\). This is a complete characterization for these two families, not a claim about arbitrary MDS codes.

## Assumptions and scope

The monomial factors are initially all one, and coordinate permutation and nonzero coordinate scaling are allowed in the equivalence to GRS. The evaluation set consists of **distinct finite-field elements**; the result makes no claim about adjoining the evaluation point at infinity, repeated evaluation points, shortening, or extending the codes. The displayed arc condition is essential. It implies \(n\le q\). The statement is valid in every characteristic, including characteristic two.

## Proof

**1. Arc and MDS property.** Associate to \(t\in S\) the projective point \(P_r(t)=[1:t:t^3]\) for \(r=1\), respectively \(P_r(t)=[1:t^2:t^3]\) for \(r=2\). A direct determinant expansion gives, up to a global sign,
\[
\det\big(P_1(a),P_1(b),P_1(c)\big)=(b-a)(c-a)(c-b)(a+b+c),
\]
\[
\det\big(P_2(a),P_2(b),P_2(c)\big)=(b-a)(c-a)(c-b)(ab+ac+bc).
\]
All triples are therefore linearly independent by the arc condition, so each \(C_r(T)\) with at least three positions is an \([|T|,3,|T|-2]_q\) MDS code.

**2. The GRS criterion.** A three-dimensional MDS code is monomially equivalent to a generalized Reed--Solomon code precisely when its projective columns lie on a smooth plane conic over \(\mathbb F_q\). Indeed GRS columns have the form \([1:z:z^2]\), with the homogeneous point at infinity allowed. Conversely, a smooth plane conic having an \(\mathbb F_q\)-rational point is a split genus-zero conic, projectively equivalent to this Veronese conic; its parametrization and the coordinate rescalings yield a GRS generator. Any five points of a projective arc lie on a conic: the linear space of six quadratic forms has a nontrivial kernel on five points. That conic is smooth, for a singular plane conic cannot contain five distinct rational points with no three collinear (a pair of rational lines forces three collinear, and a nonsplit pair has at most one rational point). It is unique up to scalar: two distinct smooth conics cannot share five geometric points, by the degree-four intersection bound for conics. Hence all five-coordinate puncturings are GRS.

**3. The six-coordinate boundary.** Substitute \(P_1(t)\) into the six independent degree-two coordinate monomials \(X^2,XY,XZ,Y^2,YZ,Z^2\). The resulting monomial degrees in \(t\) are \(0,1,3,2,4,6\), i.e. every degree from zero through six **except degree five**. For \(P_2(t)\) the resulting degrees are \(0,2,3,4,5,6\), i.e. every such degree **except degree one**. Thus a conic through \(P_r(T)\), \(|T|=6\), exists precisely when a nonzero polynomial of degree at most six, with the designated missing coefficient zero, vanishes at all six distinct evaluation points. Such a polynomial must be a scalar multiple of
\[
H_T(z)=\prod_{t\in T}(z-t)=z^6-e_1(T)z^5+e_2(T)z^4-\cdots-e_5(T)z+e_6(T).
\]
Its coefficient of \(z^5\) is \(-e_1(T)\); that of \(z\) is \(-e_5(T)\). This proves the exact six-point criteria. The conic is automatically smooth by the arc argument in step 2.

**4. Seven or more coordinates.** Any conic vanishing on the columns yields a polynomial in \(t\) of degree at most six. The substitution of the six quadratic monomials is injective, since all the six exponents above are distinct. A nonzero such polynomial has at most six distinct roots in any field. No smooth conic, hence no GRS equivalence, is possible once \(|T|\ge7\). Steps 2--4 immediately prove the exact deletion threshold and identify all optimal deleted coordinate sets.

**5. The packing property.** Fix a five-subset \(U\subseteq S\). For \(r=1\), an eligible extension \(U\cup\{t\}\) must satisfy \(t=-e_1(U)\), leaving at most one choice. For \(r=2\), the required equation is
\[
 e_5(U\cup\{t\})=e_5(U)+t\,e_4(U)=0.
\]
The two coefficients \(e_4(U)\) and \(e_5(U)\) cannot both vanish: if \(0\notin U\), then \(e_5(U)=\prod_{u\in U}u\ne0\); if \(0\in U\), then the other four entries are nonzero and \(e_4(U)\) equals their nonzero product. Hence at most one extension exists also for \(r=2\). Each six-subset contains six five-subsets; counting their disjoint occurrences gives \(6B_r(S)\le\binom n5\).

## Verification

The accompanying standalone \(\texttt{verify.py}\) independently computes the modular ranks of the six-column quadratic-evaluation matrices; it does not merely recompute the displayed elementary symmetric functions. It checks every triple-column determinant, every retained subset of sizes five through seven in four explicit length-seven examples, and all MDS evaluation subsets of sizes five, six, seven over the prime fields of sizes 11 and 13. It checks the five-packing incidence property for each example.

For \(r=1\) on \(S=\{0,1,2,3,4,5,6\}\), modulo 19 exactly the six-subset \(\{0,1,3,4,5,6\}\) is GRS, so the required puncturing depth is one; modulo 23 no six-subset is GRS, so the depth is two. For the exceptional six-subset over \(\mathbb F_{19}\), the explicit smooth conic containing all six columns is \(XY+14XZ+18Y^2+4YZ+Z^2=0\), with \([X:Y:Z]=[1:t:t^3]\). The triple sums are all nonzero modulo 19, so this is an MDS code; the conic is smooth because the six points form an arc; directly, its symmetric matrix over \(\mathbb F_{19}\) is \(\left[\begin{smallmatrix}0&10&7\\10&18&2\\7&2&1\end{smallmatrix}\right]\), whose determinant is \(1\pmod{19}\). For \(r=2\), the set \(S=\{1,4,5,10,13,16,18\}\subseteq\mathbb F_{19}\) has exactly one eligible six-subset, whereas \(S=\{0,1,2,3,4,7,11\}\subseteq\mathbb F_{17}\) has none. All four seven-point codes satisfy their respective MDS hypotheses. These finite tests are sanity checks, not substitutes for the all-field proof.

To reproduce: run \(\texttt{python3 verify.py}\) with the bundled script; successful execution ends with \(\texttt{VERIFY_OK}\). No third-party packages are required.

## Relationship to prior work

Ning [1] defines the codimension-one subcodes \(\mathrm{GRS}_{k,r}\), proves their MDS tests via elementary symmetric polynomials, and studies self-duality, near-MDS behavior, and dual codes. Jin--Ma--Xing--Zhou [2], Proposition VI.1, establish the non-GRS obstruction with the strict condition \(n>2k\), which for \(k=3\) covers the **already known** retained-length-at-least-seven obstruction. Their Proposition V.1 also **asserts** non-GRS for the first deleted-degree family at the weaker boundary \(n\ge2k\); its equality case is contradicted by the directly verified six-point MDS conic above. The present result is the precise *unclassified six-coordinate boundary*: it classifies which GRS puncturings of length six actually occur, counts and constrains them, and computes the sharp puncturing-to-GRS threshold. The five-point GRS statement itself is classical.

Márquez-Corbella--Pellikaan [3], Section 3 and Appendix D, establish the geometric relationship between GRS codes and rational normal curves, used here for the three-dimensional conic criterion. Abdukhalikov--Ding--Verma [4], Section 3, Theorem 3.2, give the non-GRS conclusion with the **weak** inequality \(n\ge2k\). At its boundary \(n=2k=6\), their non-GRS assertion is contradicted by the explicit smooth-conic MDS example above; their MDS criterion itself remains valid. Jin--Ma--Xing--Zhou [2] Proposition VI.1 assumes the **strict** inequality \(n>2k\), and is consistent with this result, but their Proposition V.1 for the first family states non-GRS already at \(n\ge2k\) and has the same explicit equality-boundary counterexample. This is a genuine six-point boundary distinction, not a restatement or an extension of the older non-GRS conclusion. Generic GRS recognition supplies a tool, but the symmetric six-subset classification and exact puncturing depth are additional deductions.

## Limitations

The result applies only to the two specified degree-deleted cubic evaluation families under the arc/MDS assumption. It does not classify arbitrary non-GRS MDS codes, extensions, or additive/group automorphisms. It does not assert that every eligible six-subset exists: the two sharp thresholds both occur. The packing bound is a valid upper bound, not an assertion of equality. The disagreements with the weak-inequality non-GRS assertions of [2] and [4] are specific to the equality boundary, and do not challenge the separate MDS tests or strict longer-length results. The proof is mathematical and all-characteristic; the bundled finite-field calculations verify representative cases only. Literature search cannot exclude unindexed or unpublished overlaps, and no independent review has yet been performed.

## References

1. Y. Ning, *On subcodes of the generalized Reed--Solomon codes*, arXiv:2507.04689, first posted 7 July 2025, \(\texttt{https://arxiv.org/pdf/2507.04689}\). Sections 2, 4, 5. Published in *Designs, Codes and Cryptography* 94 (2026), article 154, DOI 10.1007/s10623-026-01893-z.
2. L. Jin, L. Ma, C. Xing, H. Zhou, *New families of non-Reed--Solomon MDS codes*, arXiv:2411.14779 (2024), \(\texttt{https://arxiv.org/pdf/2411.14779}\). Sections II, III and VI, notably Propositions V.1 and VI.1.
3. I. Márquez-Corbella, R. Pellikaan, *A characterization of MDS codes that have an error correcting pair*, arXiv:1508.02187 (2015), DOI 10.1016/j.ffa.2016.04.004. Section 3 and Appendix D.
4. K. Abdukhalikov, C. Ding, G. K. Verma, *Some constructions of non-generalized Reed--Solomon MDS codes*, arXiv:2506.04080 (2025), \(\texttt{https://arxiv.org/pdf/2506.04080}\). Sections 2--6.
