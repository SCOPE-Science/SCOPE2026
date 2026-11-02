# Smith normal form of the reduced divisor-indexed Ramanujan matrix for every modulus

## Finding

For every integer \(n\ge 2\), let \(\mathcal D_n=\{d:d\mid n,\ d>1\}\), and put \(r=\tau(n)-1\). Let \(c_d(e)\) denote the ordinary Ramanujan sum and consider the \(r\)-by-\(r\) integer matrix
\[
 B_n=\bigl(c_d(e)\bigr)_{d,e\in\mathcal D_n}.
\]
Its **complete integral Smith normal form** is specified by the following primewise recipe. For each prime \(\ell\mid n\varphi(n)\), define a multiset \(E_\ell\) of positive integers.

* If \(\ell\nmid n\), take the singleton \(\{\nu_\ell(\varphi(n))\}\) if that valuation is positive; otherwise take the empty multiset.
* If \(\ell\mid n\), write \(n=\ell^a m\), \(\ell\nmid m\), and set \(T=\tau(m)\) and \(h=\nu_\ell(\varphi(m))\). Start with exactly \(T\) copies of each exponent \(1,2,\ldots,a\). Remove one copy of \(1\). If \(h>0\), increase one remaining copy of \(a\) to \(a+h\). (In this last case \(m>1\), hence \(T\ge2\), so that copy exists.)

Sort each multiset nondecreasingly and pad it on the **left** with zeroes to length \(r\), obtaining exponents \(e_{\ell,1}\le\cdots\le e_{\ell,r}\). Then the positive Smith invariant factors are
\[
\boxed{s_j=\prod_{\ell\mid n\varphi(n)}\ell^{e_{\ell,j}}\quad (1\le j\le r),\qquad s_j\mid s_{j+1}.}
\]
In particular the finite abelian cokernel is \(\bigoplus_{j=1}^r\mathbb Z/s_j\mathbb Z\). Its determinant and all finite-field ranks are
\[
\boxed{\det B_n=\frac{\varphi(n)}{n}\prod_{\substack{d\mid n\\d>1}}d>0,}
\]
\[
\boxed{\operatorname{rank}_{\mathbb F_\ell}(B_n)=
\begin{cases}
\tau(n/\ell^{\nu_\ell(n)}),&\ell\mid n,\\
\tau(n)-2,&\ell\nmid n\text{ and }\ell\mid\varphi(n),\\
\tau(n)-1,&\ell\nmid n\varphi(n).
\end{cases}}
\]
For example, at \(n=12\) the complete Smith list is \((1,1,2,12,24)\); at \(n=36\) it is \((1,1,1,6,6,36,36,72)\).

## Assumptions and scope

The sole hypothesis is an integer \(n\ge2\). The matrix indices are **all divisors greater than one on both axes**; the result is not a claim about a matrix indexed by all divisors, a circulant on residues, or arbitrary finite-ring Ramanujan analogues. We use \(\tau(n)\) for the number of positive divisors, \(\varphi(n)\) for Euler's totient, \(\mu(n)\) for Möbius's function, and \(\nu_\ell(n)\) for the exponent of the rational prime \(\ell\) in a positive integer. The convention \(\varphi(1)=1\) is used. Factors equal to \(1\) are retained in the Smith list. Invariant factors are determined up to signs and are taken positive.

## Proof

**1. An integral rank-one diagonalization.** Index every matrix by \(\mathcal D_n\), in any common divisor-compatible order. Let \(E\) be the divisibility incidence matrix \(E_{d,t}={\bf1}_{t\mid d}\) and \(D=\operatorname{diag}(d:d\in\mathcal D_n)\). The matrix \(E\) is integral unimodular, with inverse \((E^{-1})_{d,t}=\mu(d/t){\bf1}_{t\mid d}\). By the ordinary Ramanujan identity,
\[
c_d(e)=\sum_{t\mid\gcd(d,e)}t\mu(d/t),
\]
we have \(B_n=E^{-1}DE^{\mathsf T}+u\mathbf1^{\mathsf T}\), with \(u_d=\mu(d)\). The divisor identity \(\sum_{t\mid d}\mu(t)=0\) for \(d>1\) gives \(Eu=-\mathbf1\) and \(E^{-1}\mathbf1=-u\). Therefore integral unimodular operations transform \(B_n\) to
\[
K=EB_nE^{-\mathsf T}=D-\mathbf1 b^{\mathsf T},\qquad b_d=-\mu(d).
\]
The determinant lemma over \(\mathbb Q\) gives
\[
\det B_n=\left(\prod_{d\in\mathcal D_n}d\right)
\left(1-\sum_{d\in\mathcal D_n}\frac{b_d}{d}\right)
=\left(\prod_{d\in\mathcal D_n}d\right)\sum_{d\mid n}\frac{\mu(d)}d
=\left(\prod_{d\in\mathcal D_n}d\right)\frac{\varphi(n)}n.
\]
This also proves that the Smith form has no zero diagonal factors. The determinant calculation alone is not the asserted new Smith classification.

**2. Reduction to local module presentations.** Fix any rational prime \(\ell\). Smith elementary divisors at \(\ell\) describe the \(\ell\)-primary component of the cokernel of \(K^{\mathsf T}\) over the discrete valuation ring \(\mathbb Z_{(\ell)}\) (equivalently \(\mathbb Z_\ell\)). Introduce one generator \(x_d\) for each \(d\in\mathcal D_n\), and put \(w=\sum_{d\in\mathcal D_n}b_dx_d\). The column relations of \(K^{\mathsf T}\) are exactly
\[
d x_d=w\qquad(d\in\mathcal D_n).
\]
All changes of generators and eliminations below have unit coefficients in the local ring, so preserve the claimed elementary divisors.

**3. Primes outside the modulus.** Suppose \(\ell\nmid n\). Then every \(d\in\mathcal D_n\) is a unit in \(\mathbb Z_{(\ell)}\). The relations imply \(x_d=w/d\), while their defining equation gives
\[
\left(1-\sum_{d\in\mathcal D_n}\frac{b_d}d\right)w
=\frac{\varphi(n)}n w=0.
\]
The element \(w\) generates the entire local cokernel, and no additional relation remains. Hence the cokernel is cyclic of order \(\ell^{\nu_\ell(\varphi(n))}\), interpreted as trivial at valuation zero. This establishes the singleton rule.

**4. Primes dividing the modulus: eliminate unit-divisor generators.** Write \(n=\ell^a m\), with \(a\ge1\) and \(\ell\nmid m\). Put \(T=\tau(m)\), \(h=\nu_\ell(\varphi(m))\), and \(\alpha=\varphi(m)/m\). The relation indexed by \(d=\ell\) says \(w=\ell x_\ell\). For each \(t\mid m\), \(t>1\), its unit-indexed relation gives
\[
x_t=\frac\ell t x_\ell.
\]
For every \(t\mid m\) write \(x_{\ell t}=t^{-1}x_\ell+y_t\), with \(y_1=0\); then \(\ell y_t=0\). For \(j=2,\ldots,a\) and \(t\mid m\), put \(z_{j,t}=t x_{\ell^j t}\), so that \(\ell^j z_{j,t}=\ell x_\ell\). As \(b_d=-\mu(d)\), the definition of \(w\) reduces **exactly** to
\[
(1-\ell)\alpha x_\ell+\sum_{\substack{t\mid m\\t>1}}\mu(t)y_t=0.
\]
All higher powers of \(\ell\) have zero Möbius coefficient, so this is the only remaining relation beyond the displayed torsion relations.

If \(m=1\), then \(\alpha=1\) and \(1-\ell\) is an \(\ell\)-adic unit. Thus \(x_\ell=0\). The remaining generators are the one \(z_{j,1}\) of order \(\ell^j\) for each \(2\le j\le a\). This is exactly the recipe with \(T=1\), \(h=0\), including \(a=1\).

If \(m>1\), select a rational prime \(q\mid m\). Since \(\mu(q)=-1\) is a unit, the last displayed equation eliminates \(y_q\). Combining it with \(\ell y_q=0\) leaves precisely
\[
\ell(1-\ell)\alpha x_\ell=0,
\qquad\text{equivalently}\qquad
\ell^{h+1}x_\ell=0
\]
up to multiplication by a local unit. The remaining \(T-2\) generators \(y_t\) are independent and each has relation \(\ell y_t=0\).

If \(a=1\), there are no \(z\)-generators. We have exactly \(T-2\) factors of size \(\ell\) and one factor \(\ell^{h+1}\). This is the recipe: start with \(T\) copies of exponent \(1\), delete one, and increase another by \(h\).

Finally let \(a\ge2\), choose one \(z_*=z_{a,1}\), and introduce
\[
v=x_\ell-\ell^{a-1}z_*,\qquad
z'_{j,t}=z_{j,t}-\ell^{a-j}z_*
\quad\text{for }(j,t)\ne(a,1).
\]
The new coordinate transformations are integral triangular with unit diagonal. The relations become
\[
\ell v=0,\qquad \ell^j z'_{j,t}=0,
\qquad \ell^{a+h}z_*=0.
\]
Indeed \(\ell^a z_*=\ell x_\ell\), and substituting \(x_\ell=v+\ell^{a-1}z_*\) into \(\ell^{h+1}x_\ell=0\) gives the final relation, because \(\ell v=0\). Together with the \(T-2\) surviving \(y_t\), this yields \(T-1\) factors of exponent one; \(T\) factors of each exponent \(2,\ldots,a-1\); \(T-1\) factors of exponent \(a\); and one factor of exponent \(a+h\). At \(h=0\), the latter is another exponent-\(a\) factor. This is the stipulated recipe for \(m>1\).

**5. Global assembly and ranks.** For each prime \(\ell\), the preceding local presentation determines all positive \(\ell\)-adic elementary-divisor exponents, with no unrecorded unit-factor multiplicity. By the classification of finite abelian groups, align each prime's sorted exponents by adding leading zeros to the common length \(r\); their products are the unique global positive invariant factors. For \(\ell\mid n\), the recipe contains exactly \(aT-1\) positive exponents, leaving rank \(r-(aT-1)=T\) modulo \(\ell\). For \(\ell\nmid n\), there is one positive exponent precisely when \(\ell\mid\varphi(n)\). These are the stated finite-field ranks, completing the proof.

## Verification

The accompanying dependency-free program `verify.py` evaluates Ramanujan sums using the independent formula
\[
c_d(e)=\mu\bigl(d/\gcd(d,e)\bigr)\,\varphi(d)/\varphi\bigl(d/\gcd(d,e)\bigr).
\]
For every modulus \(2\le n\le30\), it computes **all determinantal divisors** by exhaustive exact-integer enumeration of every square minor, recovering every invariant factor without using the proof's local presentation. For every \(2\le n\le150\), it independently computes the exact determinant by fraction-free elimination and checks the determinant formula. It also checks \(1192\) finite-field ranks over eight small primes. The actual replay result is:

`VERIFY_OK: 29 complete determinantal-divisor Smith checks; 149 exact determinants; 1192 modular ranks.`

These finite checks corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work

Fowler, Garcia and Karaali's 2012 supercharacter formulation supplies an established matrix viewpoint for Ramanujan sums and classical arithmetic identities. Schlage-Puchta's 2021 paper computes the determinant of a **full divisor-indexed matrix**, establishing rational nonsingularity, but a determinant does not determine an integral Smith form. Shareshian and Sundaram (2023 preprint) use a full Ramanujan divisor table and its orthogonality in symmetric-function representation theory. These sources are relevant background; the classified object here is the principal submatrix deleting the unit divisor on **both** indices.

The squarefree-modulus specialization of the reduced matrix was previously identified; this theorem does **not** claim the squarefree case as new. Its further statement is the full classification for arbitrary prime powers and their products, including the boosted exponent \(a+\nu_\ell(\varphi(m))\) when \(n=\ell^a m\). No claim of literature-wide uniqueness is made.

## Limitations

The theorem addresses ordinary Ramanujan sums on divisor indices, not generalized finite-ring Ramanujan matrices, Fourier submatrices on primitive residues, or arbitrary principal submatrices. Its modular ranks follow from the finer Smith classification. An equivalent specialization of a broader integer-matrix theorem in unlocated literature is a residual originality risk. No independent mathematical validation has been performed.

## References

1. C. F. Fowler, S. R. Garcia, G. Karaali, *Ramanujan sums as supercharacters*, first arXiv version dated 2012-01-05, arXiv:1201.1060.
2. J.-C. Schlage-Puchta, *A determinant involving Ramanujan sums and So's conjecture*, Archiv der Mathematik 117 (2021), 379–384. DOI:10.1007/s00013-021-01643-8.
3. J. Shareshian, S. Sundaram, *Ramanujan sums and rectangular power sums*, arXiv:2305.12007 (2023).
