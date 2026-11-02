# Exact dihedral-order spectrum of Miyamoto involutions in finite-field spin factors

## Finding

Let \(q\) be an odd prime power and let \((V,B)\) be a nondegenerate symmetric bilinear space of dimension \(m\ge3\) over \(k=\mathbb F_q\). Suppose \(Q(x)=B(x,x)\) represents \(1\). Consider the spin-factor Jordan algebra \(J=k\mathbf1\oplus V\), whose product is
\[
(a\mathbf1+x)\circ(b\mathbf1+y)=(ab+B(x,y))\mathbf1+ay+bx.
\]
Its nontrivial primitive idempotents are exactly \(e_u=(\mathbf1+u)/2\) for \(Q(u)=1\). The corresponding Miyamoto involution \(\tau_u\) fixes \(\mathbf1\) and restricts to \(T_u(x)=2B(u,x)u-x\) on \(V\). In particular \(\tau_u=\tau_{-u}\) and these are the only coincidences.

Let \(p\) be the characteristic, \(\chi:k\rightarrow\{-1,0,1\}\) the quadratic character, \(n=m-1\), and \(\Delta\) the determinant square-class of a Gram matrix of \(B\). Set
\[
\epsilon=\chi\!\left((-1)^{\lfloor n/2\rfloor}\Delta\right),\qquad h_-=(q-1)/2,\qquad h_+=(q+1)/2.
\]
Define \(Z,C_{\rm s},C_{\rm ns}\) as follows. If \(n\) is even,
\[
Z=q^{n-1}+(q-1)\epsilon q^{n/2-1},\qquad
C_{\rm s}=C_{\rm ns}=q^{n-1}-\epsilon q^{n/2-1}.
\]
If \(n\) is odd,
\[
Z=q^{n-1},\qquad
C_{\rm s}=q^{n-1}+\epsilon\chi(-1)q^{(n-1)/2},\qquad
C_{\rm ns}=q^{n-1}-\epsilon\chi(-1)q^{(n-1)/2}.
\]
For fixed \(u\) of norm \(1\), put \(A_d=|\{v\in V:Q(v)=1,\ \operatorname{ord}(\tau_u\tau_v)=d\}|\). Then, **for every positive integer \(d\)**,
\[
A_d=\begin{cases}
2,&d=1,\\
2(Z-1),&d=p,\\
\varphi(d)C_{\rm s},&d>1\text{ and }d\mid h_-,\\
\varphi(d)C_{\rm ns},&d>1\text{ and }d\mid h_+,\\
0,&\text{otherwise}.
\end{cases}
\]
These cases are disjoint, since \(\gcd(h_-,h_+)=1\) and \(p\nmid h_-h_+\). Thus the order support and every exact multiplicity are explicit, including characteristic-dependent unipotent products.

The size of the unit sphere \(S=|\{v:Q(v)=1\}|\) is
\[
S=\begin{cases}
q^{m-1}-\chi((-1)^{m/2}\Delta)q^{(m-2)/2},&m\text{ even},\\
q^{m-1}+\chi((-1)^{(m-1)/2}\Delta)q^{(m-1)/2},&m\text{ odd}.
\end{cases}
\]
There are \(S A_d\) ordered pairs of primitive axes with order \(d\), and \(S A_d/4\) ordered pairs drawn from the set of **distinct involutions** (repetition allowed) with product order \(d\). Each pair generates a dihedral group of order \(2d\), including the order-two case \(d=1\).

**Sharp boundary.** The full set of \(S/2\) Miyamoto involutions forms a set of \(3\)-transpositions if and only if either \(q=3\), or \(q=5\), \(m=3\), and the binary space \(u^\perp\) is anisotropic. For \(q=5\) this is equivalently \(\chi(\Delta)=-1\). The condition does not depend on the selected unit vector.

## Assumptions and scope

The field has odd cardinality; the form is nondegenerate and represents \(1\); the dimension is at least three. The claim includes all primitive axes of this spin factor, not a specially chosen generating subset. The product order is computed in the actual automorphism group of \(J\), not merely on a projective quotient. All eigenvalue and power arguments below are valid also when \(q\) is a proper prime power. The determinant enters only through its square-class, so choice of Gram basis does not affect the answer.

## Proof

**1. Axis and involution description.** Expanding \((a\mathbf1+x)^2=a\mathbf1+x\) shows that nontrivial idempotents satisfy \(a=1/2\) and \(Q(x)=1/4\), hence have the asserted form. Relative to \(e_u\), the Peirce spaces have eigenvalues \(1\), \(0\), and \(1/2\), on \(ke_u\), \(ke_{-u}\), and \(u^\perp\), respectively. The fusion-rule involution acts as \(+1\) on the first two and \(-1\) on the third; this is exactly \(T_u(x)=2B(u,x)u-x\). Its \(+1\)-eigenspace on \(V\) is the line \(ku\), hence \(T_u=T_v\) with both norms one implies \(v=\pm u\).

**2. Reduction to one norm equation.** Fix a unit vector \(u\), and write each unit vector uniquely as \(v=tu+w\) where \(t=B(u,v)\in k\), \(w\in u^\perp\), and \(Q(w)=1-t^2\). The restriction \(B|_{u^\perp}\) is nondegenerate and has determinant square-class \(\Delta\) because \(Q(u)=1\).

**3. Nondegenerate pairs.** Suppose \(t^2\ne1\). Then the plane \(ku+kv\) is nondegenerate. The product \(T_uT_v\) acts identically on its orthogonal complement; on this plane it has determinant \(1\), trace \(4t^2-2\), and reciprocal eigenvalues
\[
\lambda=(t+s)^2,\qquad \lambda^{-1}=(t-s)^2,\qquad s^2=t^2-1.
\]
When \(t^2-1\) is a nonzero square, \(t+s\in k^\times\), so \(\lambda\) is in the square subgroup of \(k^\times\) of order \(h_-\). When it is a nonsquare, take \(s\in\mathbb F_{q^2}\) with \(s^q=-s\); then \((t+s)(t-s)=1\), so \(t+s\) belongs to the norm-one torus of order \(q+1\), and \(\lambda\) belongs to its square subgroup of order \(h_+\). The two resulting cyclic groups are each parametrized by all admissible \(t\) values. For every \(d>1\) dividing the corresponding half-torus order, exactly \(\varphi(d)\) distinct \(t\) values produce eigenvalues of exact order \(d\): each inverse pair of eigenvalues determines two opposite \(t\) values; the self-inverse case \(\lambda=-1\) corresponds to the single value \(t=0\). The product is semisimple even at \(t=0\), since it equals minus the identity on the two-plane.

**4. Unipotent and identity pairs.** If \(t=1\) or \(t=-1\), the perpendicular component satisfies \(Q(w)=0\). For \(w=0\), \(v=\pm u\) and the product is the identity. For \(w\ne0\), the product is a nonidentity unipotent transformation. Direct substitution of the reflection formula shows that its nilpotent deviation \(N=T_uT_v-I\) satisfies \(N^3=0\): \(\operatorname{im}N\subseteq\operatorname{span}(u,w)\), on which \(N^2=0\). In odd characteristic its order is exactly \(p\), including \(p=3\). Hence the identity multiplicity is \(2\), and the unipotent multiplicity is \(2(Z-1)\), with \(Z\) the number of zeros of \(Q\) on \(u^\perp\).

**5. Quadratic-shell calculation.** For a nondegenerate quadratic form on an \(n\)-space with determinant \(\delta\), standard diagonalization and the quadratic-character Gauss sum give, for \(n\) even, \(N(0)=q^{n-1}+(q-1)\chi((-1)^{n/2}\delta)q^{n/2-1}\) and \(N(a)=q^{n-1}-\chi((-1)^{n/2}\delta)q^{n/2-1}\) if \(a\ne0\). For odd \(n\), \(N(0)=q^{n-1}\) and \(N(a)=q^{n-1}+\chi((-1)^{(n-1)/2}\delta)\chi(a)q^{(n-1)/2}\) for nonzero \(a\). These formulas follow, for example, by writing the character indicator \(q^{-1}\sum_{z\in k}\psi(z(Q(w)-a))\), multiplying the one-dimensional quadratic Gauss sums and using \(G(\chi,\psi)^2=\chi(-1)q\). Substituting \(a=0\), or \(a=1-t^2\) with \(\chi(t^2-1)=+1\) or \(-1\), proves the displayed \(Z,C_{\rm s},C_{\rm ns}\). The same formula in dimension \(m\), at \(a=1\), gives \(S\). This completes all order and pair multiplicities.

**6. The three-transposition threshold.** Both \(C_{\rm s}\) and \(C_{\rm ns}\) are strictly positive for \(n\ge2\). For \(q\ge7\) one of \(h_-\), \(h_+\) is at least four, so an order exceeding three occurs. For \(q=3\), both half-tori have order at most two, while any unipotent has order three; hence the condition always holds. For \(q=5\), the half-tori have orders two and three, so the condition is equivalent to absence of nonzero isotropic vectors in \(u^\perp\). A nondegenerate quadratic space of dimension at least three over a finite field always has such a vector (also immediate from the formula for \(Z\)), while a binary space is anisotropic exactly when its zero set has size one. For \(n=2\), \(Z=q+(q-1)\epsilon\), hence \(Z=1\) precisely when \(\epsilon=-1\), equivalent to \(\chi(\Delta)=-1\) for \(q=5\). This proves the stated classification.

## Verification

Standalone exact-arithmetic programs enumerate all unit vectors and compute actual products and multiplicative orders of their \(m\)-dimensional matrices. The prime-field program checks sixteen complete cases for \(q=3,5,7,11\), dimensions three and four and two quadratic-form square classes; the extension-field program checks three cases over \(\mathbb F_9\), including dimension four. Every observed histogram agrees with the closed formula. The scripts require Python 3 and the standard library only. Finite enumeration is a corroboration of, not a substitute for, the general proof.

## Relationship to prior work

Hall–Rehren–Shpectorov (2014, preprint version 1) introduced and investigated the axial-algebra framework and two-generated Jordan-type algebras. Hall–Segev–Shpectorov (2016, especially §5 and §7) explicitly identify the Miyamoto action on Jordan algebras of Clifford type with the negative orthogonal reflection, and explain that product orders match reflection product orders. These facts are used here, not claimed as new. The classification of quadratic forms and the quadratic-shell count are also classical. Later studies of solid subalgebras in Jordan-type axial algebras and Jordan factors of Matsuo algebras address structural aspects of these algebras but do not give the uniform finite-field order-by-order multiplicity formula in the inspected material. The claimed contribution is the completed numerical distribution for **all** axes, its uniform characteristic-dependent count, and the sharp all-axis three-transposition threshold. Since existing finite orthogonal association-scheme theory may imply some formulas indirectly, independent publication-priority review remains warranted.

## Limitations

The theorem excludes characteristic two, degenerate forms, quadratic spaces of dimension below three and forms not representing one. It concerns the full set of axes, which is generally different from a prescribed small generating subset. It does not classify the full Miyamoto group or all simultaneous-conjugacy classes of pairs. The statements are mathematically checked here but have not undergone independent expert audit; complete historical priority is not asserted.

## References

1. J. I. Hall, F. Rehren, S. Shpectorov, *Primitive axial algebras of Jordan type*, arXiv:1403.1898v1 (first publicly posted 2014-03-07), https://arxiv.org/abs/1403.1898.
2. J. I. Hall, Y. Segev, S. Shpectorov, *Miyamoto involutions in axial algebras of Jordan type half*, arXiv:1610.01307v1 (2016-10-05), §5 and §7, https://arxiv.org/abs/1610.01307.
3. I. Gorshkov, S. Shpectorov, A. Staroletov, *Solid subalgebras in algebras of Jordan type half*, arXiv:2401.16218v1 (2024-01-29), https://arxiv.org/abs/2401.16218.
4. I. Gorshkov, A. Mamontov, A. Staroletov, *On Jordan algebras that are factors of Matsuo algebras*, arXiv:2305.10958 (first version 2023-05-18), https://arxiv.org/abs/2305.10958.
