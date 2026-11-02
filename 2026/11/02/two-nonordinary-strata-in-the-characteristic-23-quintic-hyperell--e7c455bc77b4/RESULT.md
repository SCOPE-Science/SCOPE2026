# Two nonordinary strata in the characteristic-23 quintic hyperelliptic pencil

## Finding
For \(k=\overline{\mathbb F}_{23}\), consider the quintic hyperelliptic pencil
\[
C_t:\quad y^2=x^5+x+t,\qquad t\in k,\quad t^4\ne1.
\]
The complete geometric \(23\)-rank and Jacobian \(a\)-number classification is
\[
(f_{23}(C_t),a(C_t))=\begin{cases}
(0,2),&t=0,\\
(1,1),&t^4=-2,\\
(2,0),&t\notin\{0\}\text{ and }t^4\notin\{-2,1\}.
\end{cases}
\]
The central curve is superspecial. The nonordinary parameter scheme has defining polynomial \(2t^4(t^4+2)\), so its central point has multiplicity four and its four nonzero points are reduced. The four nonzero parameters belong to \(\mathbb F_{23^2}\setminus\mathbb F_{23}\) and form one geometric isomorphism orbit; thus precisely two isomorphism classes occur among nonordinary fibers of this pencil. Over \(\mathbb F_{23}\), only the smooth fiber at \(t=0\) is nonordinary.

## Assumptions and scope
All geometric statements are over an algebraic closure \(k\) of \(\mathbb F_{23}\). The word \(23\)-rank means the geometric \(p\)-rank of the Jacobian, the dimension of its etale \(23\)-torsion. The \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_p,\operatorname{Jac}(C_t)[p])\). For a smooth genus-two hyperelliptic curve, the latter equals \(2\) minus the rank of its one-step Hasse–Witt matrix. The geometrically superspecial condition is equivalent here to vanishing of that matrix. Nothing is asserted about singular fibers \(t^4=1\) or other characteristics.

## Proof
**Smoothness and genus.** With \(f_t(x)=x^5+x+t\), a repeated root must satisfy \(5x^4+1=0\) and \(x^5+x+t=0\). The resultant is \(3125t^4+256\), congruent to \(3(1-t^4)\) modulo \(23\). Hence the specified fibers are smooth of genus two.

**The one-step matrix.** Let \(c_j(t)=[x^j]f_t(x)^{11}\). With respect to the standard hyperelliptic basis, the coefficient matrix \(M=(c_{23i-j})_{1\le i,j\le2}\) is the transpose of a Hasse–Witt matrix. Direct multinomial expansion modulo \(23\) yields
\[
M_t=\begin{pmatrix}
7t^5+9t&10t^6-3t^2\\
9t^2&0
\end{pmatrix},
\qquad \det M_t=2t^4(t^4+2).
\]
At \(t=0\) the entire matrix vanishes, giving \(a=2\) and stable Frobenius rank zero. At any root \(t^4=-2\), the matrix simplifies to
\[
M_t=\begin{pmatrix}-5t&0\\9t^2&0\end{pmatrix}
\]
and has rank one; elsewhere on the smooth locus it has rank two. This proves all stated \(a\)-numbers and ordinarity off the five nonordinary parameters.

**Stable Frobenius, not merely one-step rank.** Every solution of \(t^4=-2\) belongs to \(\mathbb F_{23^2}\): for \(t\ne0\), \(t^{23^2-1}=(t^4)^{132}=(-2)^{132}=1\). Write \(H_t=M_t^{\mathsf T}\) for the Frobenius coefficient matrix. At these four parameters \(H_t\) has rank one, and \(H_t^{(23)}H_t\) has one nonzero eigenvalue
\[
(-5t)^{24}=(-5)^2(t^4)^6=25\cdot(-2)^6=13\pmod{23}.
\]
Because the coefficients are fixed by the \(23^2\)-power Frobenius, successive two-step semilinear iterates preserve this nonzero one-dimensional image. The stable Frobenius rank, hence the geometric \(23\)-rank, is one. At the central fiber it is zero, and at all invertible fibers it is two. In genus two, vanishing one-step Hasse–Witt matrix makes \(C_0\) superspecial.

**Parameters and isomorphisms.** The factor \(t^4+2\) is separable and coprime to \(t\) and \(t^4-1\); it has precisely four geometric roots. Since \(-2\) is not a quadratic residue modulo \(23\), none is in \(\mathbb F_{23}\). For \(s^8=1\), the change \(x=s^2X\), \(y=s^5Y\) sends \(C_t\) isomorphically to \(C_{s^{-2}t}\). Its four possible scalars \(s^{-2}\) permute the four nonzero exceptional parameters transitively. Their \(23\)-rank differs from that of \(C_0\), so the two exceptional types cannot be isomorphic. The determinant has order four at zero and simple zeros at the remaining four points.

## Verification
Run `python3 verify_katz23.py`, using only the Python standard library. The program independently computes the four relevant coefficients in \((x^5+x+t)^{11}\) by both iterative multiplication and multinomial coefficients. It exhausts the \(529\) elements of \(\mathbb F_{23}[i]/(i^2+1)\), verifying the four rank-one parameters and four singular parameters, the Frobenius eigenvalue \(13\), and the transitive fourth-root scaling orbit. Successful execution prints `VERIFY_OK`. These finite computations check exact finite identities; the geometric classification and infinite iteration argument are proved above, not extrapolated from enumeration.

## Relationship to prior work
Zhu, *Construction of Generically Ordinary Families of Hyperelliptic Curves* (arXiv:2606.31783, first public 2026-06-30), proves generic ordinarity of \(y^2=x^d+\alpha x+t\) for suitable characteristics and gives a universal coefficient formula for its Hasse–Witt polynomial, but does not classify all geometric \(23\)-ranks, exceptional fibers, or isomorphism orbits in this characteristic. The central superspecial curve is not claimed as a new discovery: the classical \(y^2=x^5-x\) is superspecial when \(p\equiv5,7\pmod8\) (and is geometrically isomorphic to the corresponding \(y^2=x^5+x\) model). The contribution here is the complete mixed \(p\)-rank stratification, including the nonreduced Hasse divisor and the unique nonzero exceptional isomorphism orbit. General results on strata in hyperelliptic moduli do not determine this individual pencil's parameter divisor. Priority for an equivalent formula in older curve tables is not independently certified.

## Limitations
The calculation applies only in characteristic \(23\) to the indicated pencil and determines \(p\)-rank and one-step \(a\)-number, not complete isogeny classes, Newton polygons of every nonordinary fiber beyond what its \(p\)-rank forces, integral endomorphism rings, or arithmetic twists. The four exceptional parameter values count presentations, not four distinct geometric curves. A published general coefficient formula makes the determinant calculation accessible; the additional semilinear stability and scheme/orbit classification are the substantive distinctions from generic ordinarity alone. Independent mathematical validation has not been performed.

## References
1. Hui June Zhu, *Construction of Generically Ordinary Families of Hyperelliptic Curves*, arXiv:2606.31783 (first submitted 2026-06-30), especially Sections 3–4, https://arxiv.org/abs/2606.31783.
2. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: A warning and a request*, Contemporary Mathematics 722 (2019), https://arxiv.org/abs/1710.10726.
3. J. D. Achter and R. Pries, *The \(p\)-rank strata of the moduli space of hyperelliptic curves*, Advances in Mathematics 227 (2011), arXiv:0902.4637.
4. *Hash functions from superspecial genus-2 curves using Richelot isogenies*, Journal of Mathematical Cryptology, DOI:10.1515/jmc-2019-0021 (previously known superspecial \(x^5-x\) model).
