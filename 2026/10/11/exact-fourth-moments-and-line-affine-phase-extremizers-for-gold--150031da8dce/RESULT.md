# Exact fourth moments and line-affine phase extremizers for Gold graphs

## Finding

For integers \(m\geq1\) and \(k\geq1\), write \(q=2^m\), \(d=\gcd(m,k)\), \(s=2^d\), and \(F=\mathbb F_q\). On the polynomial graph \(\Gamma_{m,k}=\{(t,t^{2^k+1}):t\in F\}\subset F^2\), consider the unnormalized extension operator
\[
T f(\xi,\eta)=\sum_{t\in F}f(t)\psi(\xi t+\eta t^{2^k+1}),
\]
with a nontrivial additive character \(\psi:F\to\mathbb C\), counting measure on the input, and uniform probability measure on the output \(F^2\). Then its exact sharp fourth power norm is
\[
\boxed{\|T\|_{\ell^2(F)\to L^4(F^2)}^4=1+s(1-q^{-1}).}
\]

Every nonzero maximizer is exactly of the form \(f(t)=c(-1)^{g(t)}\), with \(c\in\mathbb C^\times\) and \(g:F\to\mathbb F_2\), where the restriction of \(g\) to **every affine \(\mathbb F_s\)-line of \(F\)** is affine as a map of additive \(\mathbb F_2\)-vector spaces. More explicitly, for each \(a\ne0\) and \(x\in F\), the function \(u\mapsto g(x+ua)\) on \(\mathbb F_s\) must equal a constant plus an \(\mathbb F_2\)-linear functional (depending on \(x,a\)). This necessary-and-sufficient condition gives all complex-valued equality cases, not just example families.

When \(d=1\), every sign assignment is allowed, giving exactly \(2^{q-1}\) distinct maximizers modulo nonzero complex scalars. When \(d=m\), only affine \(\mathbb F_2\)-valued functions occur, giving exactly \(q\) projective maximizers. When \(1<d<m\), the extremizer class contains genuinely nonadditive sign patterns described explicitly in the proof. The exact nonnegative deficit identity below quantitatively separates amplitude, squared-phase, and fiber-product obstructions.

## Assumptions and scope

The additive character is any fixed nontrivial character of \(F\); its sign convention does not affect the norm. A norm without subscript on the output means the \(q^{-2}\)-normalized counting integral. All input vectors are complex-valued; there is no reality or positivity assumption. The polynomial exponent and extension-field degree are arbitrary positive integers, including \(k\) divisible by \(m\). Finite-field addition has characteristic two. The phrase projectively distinct identifies \(f\) and \(cf\) for \(c\in\mathbb C^\times\).

## Proof

Write \(P(t)=t^{2^k+1}\), \(B=\sum_{t\in F}|f(t)|^2\), and define the derivative fiber
\[
A_{a,b}=\{x\in F:P(x)+P(x+a)=b\}.
\]
By additive character orthogonality, applied to the square of the synthesis operator,
\[
\mathcal E(f):=\|Tf\|_{L^4(F^2)}^4
=\sum_{a,b\in F}\left|\sum_{x\in A_{a,b}}f(x)f(x+a)\right|^2.
\]
For \(a=0\), the sole nonempty fiber is \(A_{0,0}=F\), contributing \(\left|\sum_x f(x)^2\right|^2\). The square on \(f\) is essential: in characteristic two this term is **not** identically \(B^2\) for complex inputs.

For \(a\ne0\), the Gold derivative is
\[
P(x+a)+P(x)=a^{2^k}x+ax^{2^k}+a^{2^k+1}.
\]
Substitute \(x=au\). Its linear part is \(a^{2^k+1}(u+u^{2^k})\). Fixed points of the automorphism \(u\mapsto u^{2^k}\) of \(\mathbb F_{2^m}\) constitute precisely \(\mathbb F_{2^d}\). Consequently every nonempty \(A_{a,b}\) is an additive coset \(x+a\mathbb F_s\) of size \(s\), and for fixed \(a\ne0\) exactly \(q/s\) values of \(b\) occur.

Cauchy--Schwarz on each nonempty derivative fiber gives
\[
\left|\sum_{x\in A_{a,b}}f(x)f(x+a)\right|^2
\le s\sum_{x\in A_{a,b}}|f(x)|^2|f(x+a)|^2.
\]
Summing over all nonzero \(a\), and using \(\sum_{a\ne0,x}|f(x)|^2|f(x+a)|^2=B^2-\sum_x|f(x)|^4\), yields
\[
\mathcal E(f)\le B^2+s\left(B^2-\sum_x|f(x)|^4\right)
\le\bigl(1+s-s/q\bigr)B^2.
\]
The constant function \(f=1\) attains both inequalities: its zero fiber contributes \(q^2\); for each \(a\ne0\), there are \(q/s\) fibers, each contributing \(s^2\), for a total of \(q^2+s(q^2-q)\). Thus the bound is sharp.

For completeness, define \(H_{a,b}=\sum_{x\in A_{a,b}}f(x)f(x+a)\). There is an **exact** deficit decomposition
\[
\begin{aligned}
&(1+s-s/q)B^2-\mathcal E(f)\\
&=\left(B^2-\left|\sum_x f(x)^2\right|^2\right)
+s\left(\sum_x|f(x)|^4-B^2/q\right)\\
&\quad+\sum_{a\ne0}\sum_{b\in F}\left(s\sum_{x\in A_{a,b}}|f(x)f(x+a)|^2-|H_{a,b}|^2\right).
\end{aligned}
\]
Every summand or bracket on the right is nonnegative by the triangle inequality or Cauchy--Schwarz. When \(f\ne0\), equality in the middle term forces all \(|f(x)|\) to coincide and be nonzero, and equality in the first term forces all \(f(x)^2\) to have identical argument. Hence \(f(x)=c\varepsilon(x)\), where \(\varepsilon:F\to\{\pm1\}\). Let \(\varepsilon(x)=(-1)^{g(x)}\). The remaining fiberwise equality means that for every \(a\ne0\), \(g(x)+g(x+a)\) is constant as \(x\) ranges over any coset of \(a\mathbb F_s\). Requiring this for all nonzero directions \(a\) is equivalent to each affine \(\mathbb F_s\)-line restriction of \(g\) being \(\mathbb F_2\)-affine, because a function on an additive group is affine exactly when all its directional finite differences are constant. This proves necessity and sufficiency of the full equality classification.

If \(d=1\), lines over \(\mathbb F_2\) have two points, so every sign function qualifies; quotienting by the global sign leaves \(2^{q-1}\) classes. If \(d=m\), the only \(\mathbb F_s\)-line is all of \(F\), hence \(g\) must be globally affine over \(\mathbb F_2\); there are \(q\) distinct projective additive characters.

For \(1<d<m\), write \(F\cong\mathbb F_s^{L}\) as a vector space with \(L=m/d\ge2\), and use coordinates \(y_1,\ldots,y_L\). Every sign function arising from
\[
g(y)=\operatorname{Tr}_{\mathbb F_s/\mathbb F_2}\!\left(\sum_{i<j}c_{ij}y_i y_j\right)+\ell(y)+b,
\]
where \(c_{ij}\in\mathbb F_s\), \(\ell\) is an arbitrary \(\mathbb F_2\)-linear form, and \(b\in\mathbb F_2\), satisfies the line-affinity condition: on \(y+ua\), the argument inside the trace is a polynomial in \(u\) with terms of degree at most two; both \(u\mapsto u\) and \(u\mapsto u^2\) are \(\mathbb F_2\)-linear. If some \(c_{ij}\ne0\), the cross-coordinate polar form is nonzero by nondegeneracy of the field trace pairing, so the corresponding \(g\) need not be globally affine. In fact these constructions give at least \(2^{m+d\binom L2}\) projectively distinct sign extremizers, because their distinct mixed polar forms remain distinct modulo affine terms. No assertion that this constructed subfamily exhausts the line-affine class is needed: the preceding necessary-and-sufficient geometric condition already classifies every extremizer.

## Verification

The standalone pure-Python checker at `artifacts/verify.py` uses polynomial-basis arithmetic for \(\mathbb F_{2^m}\), \(1\le m\le6\). For all \(21\) tested pairs \((m,k)\) with \(1\le k\le m\), it constructs every derivative fiber and independently checks that every nonempty fiber has size \(2^{\gcd(m,k)}\). It also computes all ordered convolution sums for constant functions, additive-character signs, arbitrary sample signs in the APN case, and explicit nonaffine quadratic signs in four nontrivial subfield cases. Eight explicit nonextremizer tests have strict deficit. Four cases use direct Fourier sums over all \(q^2\) output characters, verifying the normalization as well as the combinatorial moment identity. Successful replay prints `VERIFY_OK exact_Gold_cases=21 nonaffine_quadratic_extremizer_cases=4 nonextremizer_tests=8 Fourier_orthogonality_checks=4`.

These calculations are finite corroboration only. The theorem for unbounded extension degree and exponent is proved by the derivative-kernel argument above.

## Relationship to prior work

Mockenhaupt and Tao [1] established the finite-field restriction framework and even-moment method; their paper mainly treats fields of odd characteristic and cones/paraboloids, rather than this binary Gold family. Carlet, Gong, and Tan [2, Sections 2--5] analyze differential uniformity and Walsh spectra of quadratic maps and related graphs; their derivative-fiber theory supplies relevant context but their stated results do not determine the sharp arbitrary-weight Gold-graph \(\ell^2\)-to-\(L^4\) norm and its line-affine complex equality conditions. González-Riquelme and Oliveira e Silva [3, Theorems 1.1--1.5] give sharp finite-field extension inequalities on other geometric surfaces, with distinct dimensions and characteristics. Fraser and Rakhmonov [4, Section 5.1] prove exponent-range restriction estimates for large Sidon sets, not this exact Gold-graph norm or equality geometry. The Gold exponents and their differential behavior are classical; **their discovery is not claimed**. The specific sharp synthesis/equality/deficit statement here has not been located in the inspected sources. A differently phrased earlier result in coding-theoretic or additive-combinatorial literature remains possible.

## Limitations

Only the fourth moment is addressed, with counting input and probability output normalization. The exact extremizer condition is geometric; except in the cases \(d=1\) and \(d=m\), no closed total count of all line-affine Boolean maps is asserted. The displayed quadratic trace family is a proved subfamily, not claimed exhaustive. The result does not imply optimality at other exponents, an independent originality guarantee, or any certification beyond the reproducible proof and checks.

## References

1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first public 18 April 2002, especially Sections 2--5. https://arxiv.org/abs/math/0204234
2. C. Carlet, G. Gong, and Y. Tan, *Quadratic Zero-Difference Balanced Functions, APN Functions and Strongly Regular Graphs*, arXiv:1410.2903v2, first public 10 October 2014, Sections 2--5. https://arxiv.org/html/1410.2903v2
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v2 (2024), Theorems 1.1--1.5. https://arxiv.org/html/2405.16647v2
4. J. M. Fraser and F. Rakhmonov, *An improved \(L^2\) restriction theorem in finite fields*, arXiv:2505.09293v1 (2025), Section 5.1. https://arxiv.org/html/2505.09293v1
