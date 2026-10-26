# Two sixteen-point genus-two curves over \(\mathbf F_7\)

## Finding

**Theorem.** Among smooth, projective, geometrically connected genus-two curves \(C/\mathbf F_7\), precisely two \(\mathbf F_7\)-isomorphism classes have \(\#C(\mathbf F_7)=16\). Representatives, their six-point Weierstrass branch-divisor Frobenius partitions, and their Weil polynomials are:

| Representative | Branch-degree partition | \(\#C(\mathbf F_{49})\) | Weil polynomial \(W_C(T)\) | Rational automorphisms |
| --- | --- | ---: | --- | ---: |
| \(y^2=x^6+1\) | \((2,2,2)\) | 46 | \((T^2+4T+7)^2\) | 24 |
| \(y^2=x^6+3x^4+3x^2+4\) | \((6)\) | 44 | \((T^2+3T+7)(T^2+5T+7)\) | 4 |

In particular their Jacobians lie in different \(\mathbf F_7\)-isogeny classes. The 16-point bound and its attainability are known; the claim here is the **complete isomorphism classification together with the arithmetic branch, Weil, and automorphism refinement**. With fixed source coordinate and an equation \(y^2=F(X,Z)\), precisely 588 squarefree binary sextics have all eight rational fibers split; the above classes account for 84 and 504 sextics respectively, including square-multiplied models.

## Assumptions and scope

All rational points, automorphisms, orbits, and isomorphisms are defined over \(\mathbf F_7\) unless an extension is explicitly displayed. A genus-two curve is smooth, projective and geometrically connected. Every genus-two curve is hyperelliptic; its canonical involution is defined over the ground field, and the genus-zero quotient is \(\mathbf P^1\) because every genus-zero curve over a finite field has a rational point. Thus the quotient induces a double cover \(C\to\mathbf P^1\). In characteristic seven the cover can be written \(y^2=F(X,Z)\) for a homogeneous sextic. An equation for a curve whose all rational fibers split has \(F(P)\in\{1,2,4\}\) for all eight rational base points, using the standard representatives \((t,1)\), \(t\in\mathbf F_7\), and \((1,0)\). In particular its leading coefficient is nonzero and the degree-six affine polynomial is squarefree. Conversely any such squarefree sextic defines a smooth genus-two curve with 16 rational points.

## Proof

**The fiber bound and equality criterion.** There are eight rational points on \(\mathbf P^1(\mathbf F_7)\); a degree-two cover has at most two rational points over each, so \(\#C(\mathbf F_7)\le 16\). Equality requires all eight fibers to consist of two distinct rational points. In a model \(y^2=F(X,Z)\) with char \(\ne2\), this is equivalent to \(F(P)\) being one of the three nonzero squares \(S=\{1,2,4\}\) at each rational point \(P\). The equality criterion also excludes branch points above rational base points and ensures the leading coefficient of \(F\) is nonzero.

**An eight-coordinate hyperplane.** Write \(F(X,Z)=\sum_{i=0}^{6} a_i X^iZ^{6-i}\) and \(f(x)=F(x,1)\). The evaluation vector is \(v(F)=(f(0),f(1),\ldots,f(6),a_6)\in\mathbf F_7^8\). The finite-field identities \(\sum_{x\in\mathbf F_7}x^i=0\) for \(0\le i<6\), and \(\sum_{x\in\mathbf F_7}x^6=-1\), give \(\sum_{j=0}^{7}v_j(F)=0\). Evaluation at the seven finite points is an isomorphism from polynomials of degree at most six to \(\mathbf F_7^7\), by Lagrange interpolation. Therefore the evaluation map on binary sextics is bijective onto this seven-dimensional hyperplane. Consequently, the exact set of models with eight split fibers is
\[
\mathcal V=\{v\in S^8:\sum_{j=0}^{7}v_j=0\pmod7\}.
\]
Counting all 45 possible multiplicity triples \((n_1,n_2,n_4)\) with sum eight, retaining those satisfying \(n_1+2n_2+4n_4\equiv0\pmod7\), and weighting them by the corresponding multinomial coefficients gives \(\#\mathcal V=924\). The full coefficient-level enumeration independently confirms this number.

**Geometric smoothness.** Each vector determines a unique sextic \(f\) with nonzero leading coefficient. Its associated hyperelliptic curve is geometrically smooth precisely when \(\gcd(f,f')=1\) in \(\mathbf F_7[x]\); equivalently the six geometric branch points are distinct. Applying the Euclidean algorithm to every one of the 924 interpolated polynomials gives exactly 588 squarefree models. The separate C++ enumeration iterates all \(7^7=823543\) coefficient vectors without using the interpolation algorithm; it independently obtains 924 split models and 588 smooth ones. Both exact algorithms and their outputs are embedded in the package.

**Arithmetic isomorphisms and the two orbits.** Any isomorphism between two genus-two curves descends through the unique hyperelliptic involution to an automorphism of \(\mathbf P^1\). Conversely a projective change of variable \(g\in\operatorname{PGL}_2(\mathbf F_7)\) lifts to an isomorphism of the double covers precisely when the transformed sextics differ by a nonzero square scalar. Projective matrices are taken up to scalar, and for this degree six over \(\mathbf F_7\) the scalar normalization introduces no ambiguity because \(\lambda^6=1\) for all \(\lambda\in\mathbf F_7^\times\). The action on the eight evaluations is therefore simply a permutation induced by \(g\), followed by common multiplication by one of \(S\). Since \(\#\operatorname{PGL}_2(\mathbf F_7)=7(7^2-1)=336\), this action has 1008 elements. Exhaustively applying all 336 projective transformations and all three square multipliers to the 588 smooth evaluation vectors yields **exactly two orbits**, of sizes **84** and **504**, whose union is the whole smooth set. Their representatives interpolate to the two sextics in the theorem. The coefficient-level C++ implementation rederives the orbit union without referencing the first enumeration's result.

**Automorphisms.** The stabilizers of the two representatives under the 1008-element action have orders \(1008/84=12\) and \(1008/504=2\). Each stabilizing projective transformation has exactly two distinct lifts to the double cover, differing by the hyperelliptic involution. Thus the full rational automorphism-group orders are \(24\) and \(4\).

**Branch spectra.** For the first curve, \(x^6+1=(x^2+1)(x^2+2)(x^2+4)\) in \(\mathbf F_7[x]\); all three quadratics are irreducible because their negatives are nonsquares. Hence Frobenius has three orbits of size two. The second sextic is irreducible over \(\mathbf F_7\): the embedded program verifies \(x^{7^6}\equiv x\pmod f\) and \(\gcd(x^{7^2}-x,f)=\gcd(x^{7^3}-x,f)=1\), which is the exact degree-six Rabin irreducibility criterion. Its branch partition is \((6)\).

**Weil polynomials.** Enumerating squares in \(\mathbf F_{49}=\mathbf F_7[u]/(u^2-3)\), with \(3\) nonsquare in \(\mathbf F_7\), gives \(\#C_1(\mathbf F_{49})=46\) and \(\#C_2(\mathbf F_{49})=44\). Each has 16 rational points over \(\mathbf F_7\), so \(\sum\alpha_i=7+1-16=-8\), while \(\sum\alpha_i^2=49+1-\#C(\mathbf F_{49})\). Newton's identity gives the middle Weil coefficient
\[
e_2=\frac{(-8)^2-(50-\#C(\mathbf F_{49}))}{2}=\frac{14+\#C(\mathbf F_{49})}{2},
\]
namely 30 or 29. The functional equation gives leading, cubic, linear and constant coefficients \(1,8,56,49\); factoring the resulting quartics yields the stated distinct Weil polynomials. By the finite-field isogeny classification, their Jacobian isogeny types are respectively an elliptic trace-\(-4\) square and a product of elliptic trace-\(-3\) and trace-\(-5\) isogeny classes.

## Verification

The package includes `code/check_values.py` and `data/check_values_output.json`, which enumerate the 924 evaluation vectors, test smoothness, construct all 336 projective transformations, form all equivalence orbits, and derive the extension-field point counts. Independently, `code/check_coefficients.cpp` and `data/check_coefficients_output.txt` exhaust 823543 sextic coefficient vectors and independently obtain the two full orbits. `code/verify_models.py` and `data/verify_models_output.txt` compute extension-field points using independent quadratic arithmetic, factor the first sextic, and prove irreducibility of the second by the finite-field polynomial criterion. Every program was executed and its output compared with the included reference file. These are finite exhaustive certificates for this one field and genus, not statements for general finite fields or genera.

## Relationship to prior work

The 16-point bound for genus-two curves over \(\mathbf F_7\), and the existence of curves attaining it, have long been known; neither is claimed as a new result. Faber–Grantham–Howe (2022) frame sharp finite-field curve-point bounds through gonality. Zobernig (2021) discusses characteristic-dependent genus-two moduli and stratifications. Rökaeus (2011) explicitly performed a broad computational census of genus-two curves over small fields (including \(\mathbf F_7\)) as input to constructing higher-genus covers, but the inspected paper presents higher-genus constructions rather than a complete tabulation of the two sixteen-point arithmetic isomorphism classes with the branch/Weil/automorphism refinement. Classical general mass formulas, arithmetic orbit tables, or unpublished computational tables may implicitly contain this result; the class-level publication priority is not certified. This contribution is exactly the stated complete **extremal** arithmetic classification and its structural distinctions, not a general all-genus-two census.

## Limitations

Only the field \(\mathbf F_7\) and genus two are addressed. Class counts are over \(\mathbf F_7\) rather than over an algebraic closure. The fixed-coordinate sextic counts 84 and 504 include square scalar multiples and are not numbers of distinct curves. Computations are exhaustive because they cover all 823543 sextic coefficients and all 336 projective classes; no assertion about an unbounded family is inferred from these counts. Earlier inaccessible or unindexed detailed genus-two databases could establish the same narrow classification, so publication priority retains that residual risk. No independent external audit has been carried out.

## References

1. X. Faber, J. Grantham and E. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307 (initial public version 2022-07-28), https://arxiv.org/abs/2207.14307.
2. M. Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270 (2021), https://arxiv.org/abs/2111.07270.
3. K. Rökaeus, *Computer Search for Curves with Many Points among Abelian Covers of Genus 2 Curves*, arXiv:1106.5176 (2011), https://arxiv.org/abs/1106.5176.
4. G. Cardona, *On the Number of Curves of Genus 2 over a Finite Field* (2003); general arithmetic genus-two counting framework.
