# Three missing tangent points of Sziklai-optimal curves and the quartic Frobenius-bitangent spectrum

## Finding
Let \(q\ge5\) be a prime power. Every plane curve of degree \(q-1\) over \(\mathbf F_q\) attaining the Sziklai count \((q-1)^2\) without a rational line component has a completely determined *rational tangent-incidence profile*: the tangent lines at its rational points comprise \((q-1)^2\) distinct rational lines, and the numbers of these lines through rational points of the plane are
\[
0^{\times3},\qquad(q-2)^{\times(q-1)^2},\qquad(q-1)^{\times3(q-1)}.
\]
Consequently **every such curve misses exactly three rational points with its rational tangents**. It cannot be tangent-filling, despite attaining the maximal rational-point count in its degree.

For the unique projective class over \(\mathbf F_5\), given by \(C_5:X^4+Y^4+3Z^4=0\), the \(28\) geometric even-contact lines (ordinary bitangents including hyperflexes) have arithmetic Frobenius permutation type
\[
2^2 4^6.
\]
There are \(16\) ordinary bitangents and \(12\) hyperflex lines; the numbers defined over \(\mathbf F_5\), \(\mathbf F_{25}\), and \(\mathbf F_{625}\) are respectively \(0,4,28\). The extension of degree four is minimal for splitting the full bitangent configuration.

## Assumptions and scope
An *optimal degree-\(q-1\) curve* here means a plane curve over \(\mathbf F_q\) without \(\mathbf F_q\)-linear components satisfying \(\#C(\mathbf F_q)=(q-1)^2\). Ferreira–Speziali's classification [1] identifies every such curve up to an \(\mathbf F_q\)-projectivity with
\[
C_{\alpha,\beta,\gamma}:\quad \alpha X^{q-1}+\beta Y^{q-1}+\gamma Z^{q-1}=0,
\quad \alpha,\beta,\gamma\in\mathbf F_q^\times,\quad\alpha+\beta+\gamma=0.
\]
This model is smooth: the three partial derivatives have no simultaneous projective zero because \(q-1\) is invertible in characteristic \(p\). A *rational tangent* means tangent at an \(\mathbf F_q\)-point of this smooth curve. A *geometric even-contact line* on the quartic is a geometric line whose intersection divisor is twice an effective divisor of degree two; this includes fourth-order contact at one point. For smooth plane quartics in odd characteristic these lines correspond to effective odd theta characteristics. Frobenius acts on their coefficient triples modulo projective scaling.

## Proof
**Universal tangent incidence.** A nonzero element of \(\mathbf F_q\) has \((q-1)\)-st power equal to one. Since the coefficients are nonzero and sum to zero, the rational points of the diagonal curve are exactly the \((q-1)^2\) torus points \([x:y:1]\) with \(x,y\in\mathbf F_q^\times\). Any point having exactly two nonzero coordinates gives a sum of two coefficients, which is the negative of the third and hence nonzero; any coordinate vertex also fails the equation.

The Gauss tangent map sends a rational torus point to the dual line with coefficient triple
\[
[\alpha x^{q-2}:\beta y^{q-2}:\gamma]
=[\alpha/x:\beta/y:\gamma].
\]
As the point ranges over \((\mathbf F_q^\times)^2\), these triples range bijectively over all rational dual-torus points \([A:B:1]\) with \(A,B\in\mathbf F_q^\times\). Thus the set of rational tangents is precisely the set of all rational lines whose three coefficients are nonzero, regardless of the admissible \(\alpha,\beta,\gamma\).

For a rational point with all three coordinates nonzero, solving \(Ax+By+z=0\) for nonzero \(A,B\) gives exactly \(q-2\) solutions: for each nonzero \(A\) there is a unique \(B\), except for precisely one excluded choice giving \(B=0\). For a point with exactly two nonzero coordinates, the equation imposes one relation on the two nonzero line coefficients, giving \(q-1\) solutions. A coordinate vertex lies on no line having all three coefficients nonzero. The three strata have respective sizes \((q-1)^2\), \(3(q-1)\), and \(3\), proving the incidence profile and the three-point covering deficit. Projectivities preserve this incidence statement.

**Specialization to the unique optimal quartic.** Homma's projective-class count [2], also recalled in [1], gives \(\nu_5=(5+1)/6=1\). Choose \(C_5:X^4+Y^4+3Z^4=0\); its partial derivatives are scalar multiples of \(X^3,Y^3,Z^3\) and cannot vanish simultaneously at a projective point.

A line with all three nonzero coefficients can be normalized to \(X+uY+vZ=0\), \(uv\ne0\). Its restricted quartic is
\[
(uY+vZ)^4+Y^4+3Z^4.
\]
If this is a scalar square of a homogeneous quadratic, comparison of the \(Y^3Z\), \(YZ^3\), \(Y^4\), \(Z^4\), and \(Y^2Z^2\) coefficients gives \(v^4=3u^4\) and \(3u^4+2=0\), hence \(u^4=1\), \(v^4=3\) in characteristic five. More explicitly, writing the putative square as \(k(rY^2+sYZ+tZ^2)^2\), its two odd-degree mixed coefficients force \(r,s,t\ne0\), \(t/r=v^2/u^2\). The leading/trailing coefficients then force \(v^4=3u^4\); the middle coefficient reduces to \(3u^4+2=0\). Conversely, for these two root conditions one has the exact identity
\[
(uY+vZ)^4+Y^4+3Z^4
=2\bigl(u^2Y^2+uvYZ+v^2Z^2\bigr)^2.
\]
The quadratic discriminant is \(-3u^2v^2\ne0\), so these are the \(16\) ordinary bitangents meeting the quartic doubly at two distinct geometric points.

The remaining even-contact lines have exactly two nonzero coefficients. In suitable labels they are \(X=sY\), \(X=sZ\), or \(Y=sZ\), with respectively \(s^4=4\), \(s^4=2\), and \(s^4=2\). Each is a hyperflex line: its restriction is a nonzero fourth power of the single remaining coordinate. Four roots per family give \(12\) hyperflex lines. A line having just one nonzero coefficient is a coordinate line and restricts to a nontrivial diagonal binary quartic with two nonzero fourth-power monomials; it cannot be a quadratic square in characteristic five. This exhausts all three coefficient-support sizes, proving the \(28\)-line list without relying on an external bitangent census.

Let \(\theta^4=3\) in an algebraic closure of \(\mathbf F_5\). The polynomial \(T^4-3\) is irreducible over \(\mathbf F_5\), since \(3\) has order four whereas every fourth power in \(\mathbf F_{25}^{\times}\) has order dividing six. Thus \(\theta\) has degree four and \(\theta^5=3\theta\). The roots of \(u^4=1\) are already in \(\mathbf F_5\); the roots of \(v^4=3\) form \(\theta\mathbf F_5^\times\) and each has Frobenius orbit length four. Roots of \(s^4=4\) lie in \(\theta^2\mathbf F_5^\times\) and have Frobenius orbit length two; roots of \(s^4=2\) lie in \(\theta^3\mathbf F_5^\times\) and have orbit length four. Therefore the \(16\) ordinary lines contribute four four-cycles, the \(12\) hyperflex lines contribute two two-cycles and two further four-cycles, altogether \(2^2 4^6\). A projective normalization does not shorten these cycles because the relevant nonzero coefficients are fixed by setting the first (or second) one equal to one.

## Verification
The accompanying pure-Python program `verify.py` performs exact arithmetic in \(\mathbf F_{625}=\mathbf F_5[T]/(T^4-3)\), enumerates all rational projective points and Gauss tangents, verifies the ordinary-bitangent square identities for all sixteen lines, constructs the twelve hyperflex lines, and computes Frobenius orbits of all \(28\). It prints `ALL_CHECKS_PASS`. A separate independently written program `verify_prime_fields.py` enumerates all rational projective points and Gauss lines for \(q=5,7,11,13\), reproducing the universal profile in those test cases. These finite computations check the formulas but are not substituted for the proof for all prime powers.

## Relationship to prior work
Ferreira–Speziali [1, Theorem 4.4 and Proposition 4.1] prove the complete Sziklai-optimal diagonal classification; Homma [2, Theorem 1.3] determines the number of projective equivalence classes. Both facts are used as **prior theorems, not claimed here as new**. Asgarli–Ghioca [3, Section 1] define tangent-filling curves and construct examples of degree \(q-1\), but do not identify the exact three-point deficit, dual-torus Gauss bijection, or the pointwise rational-tangent profile for *Sziklai-optimal* curves. Bethea–Brazelton [4, Sections 3–4] classify automorphism-group actions on geometric bitangents of complex symmetric quartics; their equivariant complex-geometric orbits are distinct from arithmetic Frobenius cycles of the displayed finite-field twist. Classical formulas for Fermat quartic bitangents may imply portions of the specialized quartic computation; the independent arithmetic descent and combined incidence conclusion are the subject here.

## Limitations
The degree-\(q-1\) classification is assumed from [1]; no new proof of it is claimed. The universal incidence theorem applies only to curves meeting exactly the Sziklai bound and excludes no examples by imposing hidden smoothness assumptions. The explicit even-contact calculation is confined to \(\mathbf F_5\) and does not assert a general Frobenius spectrum for all \(q\). The exact arithmetic calculations are reproducible; neither a worldwide uniqueness-of-priority assertion nor an independent external audit is claimed. Classical explicit Fermat bitangent formulas and unindexed finite-field specializations pose residual priority uncertainty.

## References
[1] W. de Paula Ferreira and P. Speziali, *Optimal plane curves of degree q-1 over a finite field*, arXiv:2211.14288 (first public version 2022-11-25), https://arxiv.org/html/2211.14288v1.

[2] M. Homma, *On maximal plane curves of degree 3 over F4, and Sziklai's example of degree q-1 over Fq*, arXiv:2105.04784 (first public version 2021-05-11), https://arxiv.org/abs/2105.04784.

[3] S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first public version 2023-02-26), https://arxiv.org/html/2302.13420v2.

[4] T. Bethea and M. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242 (first public version 2024-10-11), https://arxiv.org/html/2410.09242v1.
