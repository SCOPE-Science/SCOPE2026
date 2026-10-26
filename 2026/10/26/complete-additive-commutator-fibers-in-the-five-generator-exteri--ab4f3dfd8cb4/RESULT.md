# Complete additive-commutator fibers in the five-generator exterior algebra

## Finding
Let \(q\) be any odd prime power, \(V\) a five-dimensional vector space over \(\mathbb F_q\), and \(E=\bigwedge V\) its unital, thirty-two-dimensional associative exterior algebra. For \(C\in E\), put
\[
F(C)=\#\{(x,y)\in E\times E:xy-yx=C\}.
\]
The following gives every fiber. If \(C\notin\bigwedge^2V\oplus\bigwedge^4V\), then \(F(C)=0\). For every other target write \(C=\alpha+\beta\), with \(\alpha\in\bigwedge^2V\) and \(\beta\in\bigwedge^4V\), and put
\[
H=\frac{q^5-1}{q-1},\qquad K=\frac{q^4-1}{q-1}.
\]
Then
\[
F(C)=\begin{cases}
q^{54}+H(q^2-1)q^{50}, &\alpha=0,\ \beta=0,\\
K(q^2-1)q^{50}, &\alpha=0,\ \beta\ne0,\\
(q^2-1)q^{50}, &\alpha\ne0\text{ is decomposable},\ \beta\in\bigwedge^4V,\\
0, &\text{otherwise}.
\end{cases}
\]
In the last case, “otherwise” includes any nonzero component of \(C\) outside degrees two and four and every nondecomposable bivector \(\alpha\). Since the characteristic is odd, a bivector is decomposable (or zero) precisely when \(\alpha\wedge\alpha=0\). Thus the commutator image is the product of the affine Plücker cone and the five-dimensional fourth exterior power:
\[
\{xy-yx:x,y\in E\}=\{\alpha\in\bigwedge^2V:\alpha\wedge\alpha=0\}+\bigwedge^4V.
\]
The image size and the number of commuting ordered pairs consequently are
\[
\#\{xy-yx:x,y\in E\}=q^{12}+q^{10}-q^7,
\]
\[
F(0)=q^{56}+q^{55}+q^{54}-q^{51}-q^{50}.
\]
The zero-fiber count is a previously available consistency check, not a new priority claim. The distinct nonzero-target multiplicities and full target-by-target classification are the asserted refinement.

## Assumptions and scope
The field is finite of odd characteristic, with no additional restriction on \(q\), and \(E\) is the associative, unital exterior algebra, not a Clifford algebra and not the graded-Lie supercommutator algebra. Pairs are ordered and labeled. The bracket is the ordinary associative additive commutator. Degree projections are those of the canonical exterior grading. In characteristic two the ordinary bracket vanishes identically, which is why the assumption that \(q\) is odd is essential. No assertion is made for exterior algebras with more or fewer generators.

## Proof
**1. Reduction to odd parts.** Write \(x=x_{\rm ev}+a+A+a_5\) and \(y=y_{\rm ev}+b+B+b_5\), with \(a,b\in V\), \(A,B\in\bigwedge^3V\), and \(a_5,b_5\in\bigwedge^5V\). Even elements commute with everything, odd elements anticommute, and any product involving an odd degree-five term has degree exceeding five. Thus
\[
[x,y]=2(a\wedge b)+2(a\wedge B+A\wedge b).
\]
The arbitrary even parts of both inputs contribute \(q^{32}\) choices, and the two top-degree odd parts contribute \(q^2\). Therefore every target fiber equals \(q^{34}\) times the number of quadruples \((a,b,A,B)\in V^2\times(\bigwedge^3V)^2\) with the prescribed two components, after division by two.

**2. The linear map at fixed vectors.** For fixed \(a,b\in V\), the fourth-degree component is the value of the linear map
\[
T_{a,b}:(\bigwedge^3V)^2\to\bigwedge^4V,\qquad(A,B)\mapsto a\wedge B+A\wedge b.
\]
If \(a,b\) are independent, every exterior basis four-vector contains at least one of these two basis directions because there are only three other directions. Hence the map is surjective, of rank five, and has \(q^{15}\) solutions for every fourth-degree target. If \(a,b\) span a nonzero line \(L\), the image is exactly \(L\wedge\bigwedge^3V\), of dimension four, and each attainable target has \(q^{16}\) preimages. If both vectors vanish, the map is zero and has \(q^{20}\) preimages at the zero target.

**3. Nonzero two-form.** A prescribed nonzero decomposable \(\alpha/2\) uniquely determines its supporting two-plane. The ordered pairs \((a,b)\) with \(a\wedge b=\alpha/2\) form a torsor for \(\mathrm{SL}_2(\mathbb F_q)\) and therefore number \(q(q^2-1)\). Every such pair is independent. Multiplying by \(q^{15}\) and then by \(q^{34}\) yields \((q^2-1)q^{50}\) for every fourth-degree target. A nondecomposable two-form cannot be a single wedge of two vectors.

**4. Vanishing two-form.** The equation \(a\wedge b=0\) says that \(a,b\) are linearly dependent. Apart from the zero pair, they span a unique line \(L\). There are \(H\) lines in \(V\) and \(q^2-1\) nonzero ordered pairs on each. The zero fourth-degree target is attained for all such lines, giving \(H(q^2-1)q^{16}+q^{20}\) quadruples. For \(\beta\ne0\), the fourth-degree condition is equivalent to \(L\subseteq\ker(v\mapsto v\wedge\beta)\). The pairing \(V\times\bigwedge^4V\to\bigwedge^5V\) is perfect; its kernel at a nonzero \(\beta\) is four-dimensional, with exactly \(K\) lines. Therefore the quadruple count is \(K(q^2-1)q^{16}\). Restoring the factor \(q^{34}\) proves all remaining cases.

**5. Image cardinality and conservation.** The number of nonzero decomposable bivectors equals
\[
(q-1){5\brack2}_q=(q^5-1)(q^2+1).
\]
Every such bivector, as well as zero, occurs with each of the \(q^5\) fourth forms. Therefore the image size is \(q^5[1+(q^5-1)(q^2+1)]=q^{12}+q^{10}-q^7\). Summing all fiber sizes gives the independent check
\[
\begin{aligned}
&q^{54}+(q^2-1)q^{50}\Big(H+(q^5-1)K+q^5(q^5-1)(q^2+1)\Big)=q^{64},
\end{aligned}
\]
which is the total number of ordered pairs in the thirty-two-dimensional algebra. Expanding the zero fiber gives the stated commuting count. This finishes the proof.

## Verification
The standalone standard-library script `verify.py` checks actual wedge signs, the degree-two and degree-four coefficients of random full algebra products, and fiber dimensions by row elimination. It exhaustively enumerates all \(3^{10}=59049\) ordered degree-one pairs over \(\mathbb F_3\) and compares the four representative target fibers with the formulas; it also examines \(18750\) selected degree-one pairs over \(\mathbb F_5\), tests random full products over both fields, and checks the global conservation identity for field orders three, five, seven, and nine. The required success marker is `VERIFY_OK_EXTERIOR5_COMMUTATOR_FIBERS`. The script is finite corroboration; the preceding argument proves the result for every odd prime power. The \(q=9\) check is algebraic conservation, not a field-of-order-nine exhaustive enumeration.

## Relationship to prior work
Domokos and Zubor (first arXiv public version, 2014) prove structural results about commuting subalgebras and odd square-zero subspaces of exterior algebras; their Section 2 establishes graded-odd anticommutativity and their Example 8.6 identifies decomposable bivectors using the Plücker relations. Those facts are inputs here. Their results do not provide the fourth-degree target stratification or the exact nonzero-target commutator fibers. MacDougall's 1981 paper counts bivectors over finite fields by decomposable length; this supplies background for counting possible degree-two parts but does not classify the additional degree-four fibers. Bentin and Mota (2012) discuss the Grassmann algebra's PI-algebra construction and parity decomposition, without targetwise counting. A previously available calculation gives the five-generator exterior-algebra zero-fiber count; the formula for \(F(0)\) above agrees exactly and is not claimed as novel. This work concerns the joint target fibers, not just the decomposability locus or the zero fiber.

## Limitations
The result does not apply to characteristic two, higher-generator exterior algebras, graded supercommutators, or more than one commutator summed together. It is a self-review without independent audit. Historical priority remains subject to fuller comparison with older finite-field bivector literature and possible implicit results in noncommutative algebra or additive probability. The full text of MacDougall's two-page original was not examined; its accessible abstract specifies bivector length counts, so this is a residual rather than a decisive overlap risk.

## References
1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916v2 (2014), especially Section 2 and Example 8.6. https://arxiv.org/html/1403.2916v2
2. R. M. Bentin and S. Mota, *Building Grassmann Numbers from PI-Algebras*, arXiv:1204.1471v1 (6 April 2012). https://arxiv.org/html/1204.1471v1
3. J. A. MacDougall, *Bivectors over a finite field*, Canadian Mathematical Bulletin 24 (1981), 489–490. DOI:10.4153/CMB-1981-073-8. Accessible abstract: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/bivectors-over-a-finite-field/A29EFACE611429A3BA265DE48E2A528F
