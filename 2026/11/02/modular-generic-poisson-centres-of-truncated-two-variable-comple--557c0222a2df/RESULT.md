# Modular generic Poisson centres of truncated two-variable complete intersections

## Finding
For every field \(k\) and integers \(m,n\ge 2\), let \(A=k[x,y]/(x^m,y^n)\). An alternating Poisson bracket on the *fixed, labelled* commutative algebra \(A\) is determined by \(f=\{x,y\}\). Write \(p=\operatorname{char}k\), with \(p=0\) allowed, and let \(a\) be \(0\) if \(p>0\) divides \(m\), and \(1\) otherwise; define \(b\) analogously from \(n\). The entire Poisson-bracket parameter space is the affine vector space \((x^a y^b)\subseteq A\), of dimension
\[
 d=(m-a)(n-b).
\]
Thus there are exactly \(q^d\) labelled Poisson brackets over every finite field \(\mathbb F_q\).

Define \(P_t=\{i:0\le i<t,\ i=0\text{ if }p=0,\text{ or }p\mid i\text{ if }p>0\}\), and put \(u=|P_m|\), \(v=|P_n|\). Set \(\delta_m=1\) when \(p>0\) divides \(m-1\), and zero otherwise; define \(\delta_n\) analogously. Then the minimum possible dimension of the Poisson centre among *all* these brackets is
\[
 z_{\min}=uv+b\delta_n(m-u)+a\delta_m(n-v)+ab(1-\delta_m)(1-\delta_n).
\]
It is attained throughout the nonempty dense open set where the coefficient of \(x^a y^b\) in \(f\) is nonzero. On this open set the Poisson centre has the **same explicit monomial basis**:
\[
 \{x^i y^j:0\le i<m,\ 0\le j<n,\ (j\in P_n\text{ or }(a=1\text{ and }i=m-1)),\ (i\in P_m\text{ or }(b=1\text{ and }j=n-1))\}.
\]
Over \(\mathbb F_q\), exactly \((q-1)q^{d-1}\) brackets lie in this displayed open set (the formula does not assert that these are the only brackets with minimal centre). Every **nonzero** bracket has centre dimension at most \(mn-2\), with equality attained by \(\{x,y\}=x^{m-1}y^{n-1}\). Hence both extremal dimensions are sharp.

A bracket with \(\{x,y\}\) invertible exists exactly when \(p>0\) divides both \(m\) and \(n\). In that case the Poisson centre of every such bracket is \(k[x^p,y^p]\subseteq A\), of dimension \(\lceil m/p\rceil\lceil n/p\rceil\). For example, the generic centre dimension is \(2\) in characteristic zero, \(6\) for \(m=n=3\) in characteristic \(2\), and \(1\) for \(m=n=3\) in characteristic \(3\).

## Assumptions and scope
A Poisson bracket means a \(k\)-bilinear alternating Lie bracket satisfying the Leibniz rule in each argument. The result applies also in characteristic \(2\), with alternation explicitly required; no identification modulo algebra automorphisms is taken. The parameter space and centre statements concern the resulting reduced algebraic sets. The field \(k\) need not be perfect or algebraically closed. In characteristic zero, membership in \(P_t\) means the exponent equals zero.

## Proof
**1. All brackets.** For any alternating biderivation let \(f=\{x,y\}\). The quotient relations give
\[
0=\{x^m,y\}=m x^{m-1}f,\qquad 0=\{x,y^n\}=n y^{n-1}f.
\]
When the first scalar is nonzero in \(k\), multiplication by \(x^{m-1}\) kills exactly the ideal \((x)\); when it vanishes there is no restriction. The analogous statement applies to \(y\). Thus these two relations are equivalent to \(f\in(x^a y^b)\). Conversely, each such \(f\) defines, on canonical polynomial representatives,
\[
 \{g,h\}=f(\partial_x g\,\partial_y h-\partial_y g\,\partial_x h)\pmod{(x^m,y^n)}.
\]
The displayed relations make this well-defined independently of representatives. It is alternating and a biderivation. Its Jacobiator is an alternating triderivation: it vanishes on triples from the two algebra generators (also with repeated generators in characteristic two) and hence everywhere. There are no additional Jacobi equations. The monomials \(x^i y^j\) with \(a\le i<m\) and \(b\le j<n\) constitute a basis of the bracket parameter space, giving dimension \(d\) and the count \(q^d\).

**2. Lower bound and generic equality.** Write \(f=x^a y^b g\) in \(A\). An element \(h\in A\) is Poisson-central precisely when \(f\partial_x h=f\partial_y h=0\) (computed with canonical representatives). Therefore the central kernel for \(f\) contains that for \(f_0=x^a y^b\). If the coefficient of \(x^a y^b\) in \(f\) is nonzero, choose \(g\) with that nonzero constant coefficient; it is a unit in \(A\), so the two central kernels agree. Such parameters form the complement of one coordinate hyperplane, establishing density and their exact finite-field number.

**3. Explicit generic centre.** For a basis monomial \(h=x^i y^j\), the expression \(f_0\partial_y h\) vanishes exactly if either \(j\in P_n\), or \(a=1\) and \(i=m-1\). Similarly \(f_0\partial_x h=0\) exactly if either \(i\in P_m\), or \(b=1\) and \(j=n-1\). The surviving monomial images have distinct exponents for distinct inputs wherever nonzero, so no cancellation between different monomial inputs occurs. The intersection of the two conditions is precisely the displayed monomial basis. Partition the exponent pairs according as each exponent belongs to its corresponding \(P_t\). The four disjoint contributions are respectively
\[
 uv,\quad b\delta_n(m-u),\quad a\delta_m(n-v),\quad ab(1-\delta_m)(1-\delta_n),
\]
which proves the formula for \(z_{\min}\).

**4. Maximum for nonzero brackets.** The linear map \(h\mapsto(\{h,x\},\{h,y\})\) has kernel the Poisson centre. When \(f\ne0\), its values on \(x\) and \(y\) are linearly independent, so its rank is at least \(2\). Thus \(\dim Z_P(A)\le mn-2\). For \(f=x^{m-1}y^{n-1}\), all basis monomials except \(x\) and \(y\) are in the kernel, so equality holds.

**5. Invertible values.** The permitted ideal \((x^a y^b)\) contains a unit if and only if \(a=b=0\), equivalent to \(p>0\) dividing both truncation exponents. For invertible \(f\), the centre is the simultaneous kernel of \(\partial_x\) and \(\partial_y\), which is exactly the span, indeed the subalgebra, of monomials with both exponents divisible by \(p\). This gives the asserted \(p\)-power centre.

## Verification
Run `python3 verify.py` using Python 3 and no third-party dependencies. The script constructs the truncated algebra and brackets directly from basis multiplication, obtains centres by finite-field Gaussian elimination, checks the Jacobi identity on basis triples, and compares the results with the claimed dimensions and counts. It uses complete enumeration for \((m,n,q)=(2,2,2),(2,2,3),(2,3,2),(2,3,3),(3,3,2),(3,4,2),(3,3,4)\) and reproducible samples in three larger cases. The \(q=4\) arithmetic is performed in a polynomial-basis representation of \(\mathbb F_4\). The final marker is `TRUNCATED_POISSON_CENTRE_OK`. These finite tests corroborate rather than prove the arbitrary-field theorem.

## Relationship to prior work
Launois and Richard, arXiv:0805.4694v1 (30 May 2008), study Poisson (co)homology of the **specified** log-canonical bracket \(\{x,y\}=xy\) over \(\mathbb C\); in Proposition 2.1 they compute its two-dimensional Poisson centre. That known complex-field special case is neither asserted to be new nor used to claim universal priority. Bao, Ye and Zhang, arXiv:1607.05958v1 (20 July 2016), Example 7.4, study a constant symplectic bracket on a \(p\)-truncated Poisson algebra, with an additional restricted \(p\)-operation. This already supplies an example of the unit-valued case, not a classification of all labelled brackets or the modular congruence-dependent generic centre. The present combined result concerns the entire affine bracket family, sharp generic/maximal centre dimensions, and the parity/residue-dependent finite-field populations. It does not classify Poisson isomorphism classes or Poisson cohomology beyond degree zero.

## Limitations
Absolute priority has not been independently established; a broader Poisson-classification theorem not identified in the consulted literature could imply portions of this result. The formula counts brackets on a fixed labelled algebra, not brackets up to isomorphism. It does not determine the full distribution of centre dimensions outside the generic open set or any nonreduced deformation functors. Centre dimensions are algebraic, not analytic Poisson ranks of a smooth manifold.

## References
- S. Launois and L. Richard, *Poisson (co)homology of truncated polynomial algebras in two variables*, arXiv:0805.4694v1, 30 May 2008, especially pp. 1–3 and Proposition 2.1. https://arxiv.org/abs/0805.4694
- Y.-H. Bao, Y. Ye and J. J. Zhang, *Restricted Poisson algebras*, arXiv:1607.05958v1, 20 July 2016, especially Example 7.4. https://arxiv.org/abs/1607.05958
