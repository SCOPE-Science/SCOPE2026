# Exact rank-refined two-involution fibers of homogeneous signed-unipotent matrices over odd finite fields

## Finding

Let \(q\) be an odd prime power, \(n\ge 2\), and \(m\ge 1\). Put \(d=nm\), let \(J\) be the direct sum of \(m\) unipotent Jordan blocks of size \(n\), and put \(g_{\varepsilon}=\varepsilon J\) for \(\varepsilon\in\{1,-1\}\). An *involution* means \(s^2=I\), including the identity.

For \(0\le r\le m\), define
\[
N_r=\begin{cases}
{m\brack r}_q\,q^{k m^2+r(m-r)},&n=2k+1,\\
{m\brack r}_q\,q^{k m^2-r(m-r)},&n=2k,
\end{cases}
\qquad
 a_r=\begin{cases}km+r,&n=2k+1,\\km,&n=2k.\end{cases}
\]
Here \({m\brack r}_q\) is the Gaussian binomial coefficient. For a factorization \(st=g_\varepsilon\), define its *residual positive rank* \(r\) to be the dimension of the \(+1\)-eigenspace of \(s\) on \(V/(g_\varepsilon-\varepsilon I)V\). This quotient has dimension \(m\), and \(s\) preserves the defining subspace because it conjugates \(g_\varepsilon\) to its inverse.

The **exact** three-variable prescribed-product fiber enumerator is
\[
\boxed{\ \sum_{\substack{s^2=t^2=I\\st=g_\varepsilon}}
 u^{r(s)}z^{\dim\ker(s-I)}w^{\dim\ker(t-I)}
 =\sum_{r=0}^{m}N_r u^r z^{a_r}w^{b_{\varepsilon,r}}\ },
\qquad
b_{1,r}=a_r,\quad b_{-1,r}=d-a_r.
\]
Thus for positive unipotent products the two factors always have the same positive eigenspace dimension; for negative unipotent products their positive eigenspace dimensions are complementary. When \(n\) is even, the ranks of the two factors are constant but the residual rank distinguishes \(m+1\) strata with the nonconstant coefficients \(N_r\).

For example, when \(q=3\), \(n=2\), and \(m=2\), the residual-rank polynomial is \(81+108u+81u^2\), yielding \(270\) ordered factorizations, all with two-dimensional positive eigenspaces. When \(q=3\), \(n=3\), and \(m=2\), the strata have multiplicities \(81,972,81\), with positive eigenspace dimensions \(2,3,4\).

## Assumptions and scope

The field has odd characteristic, and all matrices act on \(\mathbb F_q^d\). The Jordan blocks in \(g_\varepsilon\) all have the *same* size; mixtures of distinct block sizes are not claimed. Factors satisfy \(s^2=t^2=I\), rather than requiring exact order two. The target matrix is **fixed**, not merely specified up to similarity. All cardinalities count ordered matrix pairs, not simultaneous-conjugacy orbits.

The primary MSC2020 code is 15A23. The motivating public source is de Seguins Pazzis's 2023 study of the existence of products of two involutions; the pointwise fiber sizes proved here are a quantitative problem distinct from existence.

## Proof

**1. Involutions reversing a fixed product.** If \(st=g_\varepsilon\) and \(s^2=t^2=I\), then \(sg_\varepsilon s=g_\varepsilon^{-1}\); conversely any such \(s\) determines the unique involution \(t=sg_\varepsilon\). Since the scalar sign cancels under conjugation, the reversing involutions of \(g_\varepsilon\) are precisely those of \(J\).

**2. Semilinear realization.** Set \(R=\mathbb F_q[x]/(x^n)\), write \(V=R^m\), and let \(J\) act by multiplication by \(1+x\). The automorphism
\[
\sigma:R\longrightarrow R,\qquad \sigma(x)=(1+x)^{-1}-1=-x+x^2-\cdots+(-1)^{n-1}x^{n-1}
\]
satisfies \(\sigma^2=1\). The relation \(sJs=J^{-1}\) means \(s\) is \(\sigma\)-semilinear, uniquely of the form \(s=A\sigma\), with \(A\in\mathrm{GL}_m(R)\). The involution equation is \(A\sigma(A)=I\). Reduction modulo \(x\) produces an involution \(A_0\in\mathrm{GL}_m(\mathbb F_q)\), with \(+1\)-eigenspace dimension \(r\). As \(q\) is odd, \(A_0\) is conjugate to \(S=\operatorname{diag}(I_r,-I_{m-r})\).

**3. Uniqueness of the lifting orbit.** A constant conjugation permits \(A\equiv S\pmod{x}\). Suppose by induction that \(A\equiv S\pmod{x^j}\) for \(1\le j<n\). Write \(A\equiv S+x^jD\pmod{x^{j+1}}\). The involution equation gives
\[
DS+(-1)^jSD=0.
\]
Conjugating the semilinear operator by \(U=I+x^jY\) changes the order-\(j\) coefficient to \(D+YS-(-1)^jSY\). Taking \(Y=-DS/2\) makes this coefficient zero, by the preceding equation. Induction yields a conjugacy to \(S\sigma\). Conversely the residue signature \(r\) is invariant. Hence precisely one orbit of reversing involutions occurs for each \(r\in\{0,\ldots,m\}\), under conjugation by \(\mathrm{GL}_m(R)\), the centralizer of \(J\).

**4. Exact stabilizer cardinalities.** Put \(h=m-r\) and \(D_{\mathrm{even}}=r^2+h^2\), \(D_{\mathrm{odd}}=2rh\). The stabilizer of \(S\sigma\) in \(\mathrm{GL}_m(R)\) consists exactly of \(U=S\sigma(U)S\). Reduction modulo \(x\) maps this group onto \(\mathrm{GL}_r(\mathbb F_q)\times\mathrm{GL}_h(\mathbb F_q)\) (constant matrices give a section). On the \(j\)-th congruence layer, \(1\le j<n\), the involution acts as \(Y\mapsto(-1)^jSYS\). Its fixed dimension is \(D_{\mathrm{even}}\) for even \(j\) and \(D_{\mathrm{odd}}\) for odd \(j\). These layer dimensions contribute independently: any invariant lift of an invariant reduction exists, by averaging an arbitrary lift \(U\) with its image \(S\sigma(U)S\), which is valid because \(2\) is invertible and both have the same invertible reduction. If \(E\) and \(O\) count even and odd integers in \(\{1,\ldots,n-1\}\), the stabilizer order is
\[
|\mathrm{GL}_r(q)|\,|\mathrm{GL}_{h}(q)|\,q^{E D_{\mathrm{even}}+O D_{\mathrm{odd}}}.
\]
Meanwhile \(|\mathrm{GL}_m(R)|=q^{(n-1)m^2}|\mathrm{GL}_m(q)|\) and
\[
\frac{|\mathrm{GL}_m(q)|}{|\mathrm{GL}_r(q)|\,|\mathrm{GL}_{h}(q)|}=q^{rh}{m\brack r}_q.
\]
If \(n=2k+1\), then \(E=O=k\), giving orbit cardinality \(q^{km^2+rh}{m\brack r}_q\). If \(n=2k\), then \(E=k-1\) and \(O=k\), giving \(q^{km^2-rh}{m\brack r}_q\). These are exactly the coefficients \(N_r\), with no other possible residual signatures.

**5. The two factor ranks.** On the associated graded layer \(x^jR^m/x^{j+1}R^m\), the representative \(S\sigma\) acts as \((-1)^jS\), so
\[
\operatorname{tr}(s)=(2r-m)\sum_{j=0}^{n-1}(-1)^j.
\]
Every involution is diagonalizable in odd characteristic, hence \(\dim\ker(s-I)=(d+\operatorname{tr}(s))/2=a_r\). Since \(J=1+x\) induces identity on each graded layer, \(sJ\) has the same trace as \(s\). Thus \(t=sg_1=sJ\) has positive dimension \(a_r\). For \(g_{-1}=-J\), we have \(t=-sJ\), so its positive dimension is \(d-a_r\). Combining the strata gives the displayed exact polynomial. Every step applies over an arbitrary finite field of odd characteristic.

## Verification

The accompanying standalone Python file `checker.py` enumerates all polynomial coefficient matrices \(A\), tests \(A\sigma(A)=I\) exactly, computes the residual signature \(r\) and the matrix rank of \(s-I\) over prime fields, and compares the entire coefficient table with the formula. It reports `ALL_EXACT_CHECKS_PASSED 13` for thirteen configurations over \(\mathbb F_3\) and \(\mathbb F_5\), including nontrivial multiplicities \(m=2\), odd and even lengths, and separate residue strata. It computes finite checks, not an infinite-field certificate; the general assertion follows from the preceding proof. No external libraries are required. Run `python checker.py` with Python 3.

## Relationship to prior work

The classical theorem on products of two involutions characterizes products by similarity to their inverses. De Seguins Pazzis (arXiv:2303.00820, 2023), in particular, gives a short qualitative existence treatment, not the finite-field pointwise factor count.

Marques de Sá (preprint 16-04, 2016), Sections 5–6 and Theorems 6.1–6.2, already classifies simultaneous-similarity orbits and determines which **pairs of involution similarity classes** are possible for fixed products, including unipotent products. We do not claim those orbit classifications or rank-support conditions. The exact finite-field sizes of the residual-signature strata, the explicit two-factor rank enumerator and its even/odd exponent transition are quantitative refinements; the cited orbit-count theorem itself counts orbits rather than members in a prescribed-product fiber.

Related work by Praeger and Seress on reversing involutions focuses on regular semisimple elements in finite general linear groups, not homogeneous nonsemisimple unipotent targets. An equivalent numerical enumeration in unindexed finite-group or matrix literature cannot be ruled out by the searches performed.

## Limitations

The theorem is proved only in odd characteristic and for homogeneous Jordan-block type. No claim is made for arbitrary mixtures of sizes, characteristic two, or for factorization counts modulo simultaneous conjugation beyond the residual-orbit classification used in the proof. The source comparison does not establish absolute historical priority. Independent mathematical review has not yet occurred.

## References

1. Clément de Seguins Pazzis, *A note on bireflectional elements of an algebra*, arXiv:2303.00820v1, publicly submitted 2023-03-01. https://arxiv.org/abs/2303.00820
2. Eduardo Marques de Sá, *Canonical Forms for Simultaneous Similarity of Pairs of Involutions*, University of Coimbra preprint 16-04, 2016, especially Sections 5–6. https://www.mat.uc.pt/preprints/ps/p1604.pdf
3. C. E. Praeger and Á. Seress, *Regular semisimple elements and involutions in finite general linear groups of odd characteristic*, 2012/2013, sections on reversing involutions of regular semisimple elements.
4. K. Gongopadhyay, T. Lohan, and C. Maity, *Strongly reversible classes in* \(\mathrm{SL}(n,\mathbb C)\), arXiv:2307.07967, Sections 1 and 3.1; reversing symmetries over the complex field.
