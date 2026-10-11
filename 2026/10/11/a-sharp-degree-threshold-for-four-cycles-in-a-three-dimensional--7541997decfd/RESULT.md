# A sharp degree threshold for four-cycles in a three-dimensional nilpotent-Jacobian family

## Finding
The first genuine period-four orbit in the polynomial family below can occur already with a quadratic defining polynomial, whereas it is impossible when that polynomial is affine. Precisely, for arbitrary real \(\alpha\ne0\), \(\nu\), and nonconstant affine \(P\), the map \(N_{P,\alpha,\nu}\) has only its fixed point among points fixed by its fourth iterate. There is an explicitly constructed quadratic \(P\) for which \(N_{P,1,0}\) has four pairwise distinct points cyclically permuted by the map. The minimum degree of the **univariate defining polynomial** \(P\) for a primitive four-cycle is therefore two; it is *not* a statement about the total degree of the three-dimensional map.

## Assumptions and scope
Throughout, coordinates are real, iteration is in discrete time, and \(P\in\mathbb R[u]\). For any \(\alpha\ne0\) and \(\nu\in\mathbb R\), set \(U=P(y+\alpha x^2)\) and
\[
N_{P,\alpha,\nu}(x,y,z)=\bigl(U,\ z-2\alpha xU,\ \alpha U^2+\nu\bigr).
\]
This is a standard subfamily of the three-dimensional nilpotent-Jacobian polynomial systems considered by Castañeda and Rebollo-Perdomo. “Period four” means **least positive period exactly four**; fixed points of the fourth iterate are also investigated to establish the exclusion.

The differential of \(N\) is pointwise nilpotent, not merely nilpotent at its fixed point. Writing \(q=P'(y+\alpha x^2)\), its Jacobian is
\[
DN=\begin{pmatrix}
2\alpha xq&q&0\\
-2\alpha U-4\alpha^2x^2q&-2\alpha xq&1\\
4\alpha^2xUq&2\alpha Uq&0
\end{pmatrix}.
\]
Its trace, sum of principal two-minors, and determinant all vanish identically, so \(\det(sI-DN)=s^3\); Cayley–Hamilton gives \((DN)^3=0\) at every point.

## Proof
**Step 1: an explicit conjugacy.** Define the polynomial coordinate automorphism
\[
\Phi(x,y,z)=\bigl(x-P(Y),\ Y,\ z-2\alpha xP(Y)+\alpha P(Y)^2\bigr),\qquad Y=y+\alpha x^2.
\]
Its polynomial inverse sends \((X,Y,Z)\) to
\[
\bigl(X+P(Y),\ Y-\alpha(X+P(Y))^2,\ Z+2\alpha(X+P(Y))P(Y)-\alpha P(Y)^2\bigr).
\]
Direct substitution, without a time reparametrization, yields
\[
\Phi\circ N\circ\Phi^{-1}=G,\qquad
G(X,Y,Z)=\bigl(P(Y)-P(Z),\ Z,\ \alpha(P(Y)-P(Z))^2+\nu\bigr).
\]
This conjugacy preserves all *least periods*. Although \(N\) has a nilpotent Jacobian, no claim of pointwise Jacobian nilpotence is made for the nonlinearly conjugate map \(G\).

**Step 2: an affine defining polynomial excludes fourth-period points.** Let \(P(u)=pu+q_0\) with \(p\ne0\), and \(\lambda=\alpha p^2\ne0\). Introduce \(r=\lambda(Y-\nu)\) and \(s=\lambda(Z-\nu)\). The last two equations of \(G\) become the universal planar map
\[
(r,s)\longmapsto\bigl(s,(r-s)^2\bigr).
\]
For a point fixed under four planar iterates, write its periodic scalar sequence as \(a,b,c,d,a,b,\ldots\). Then
\[
c=(a-b)^2,\quad d=(b-c)^2,\quad a=(c-d)^2,\quad b=(d-a)^2.
\]
Put \(A=a-c\), \(B=b-d\), and \(S=a+c-b-d\). Taking differences of these four equalities gives the **exact** algebraic identities
\[
A=S(B-A),\qquad B=S(A+B),\qquad S=-2AB.
\]
If \(A=B=0\), the four recurrence equations force \(a=b=c=d=0\). Otherwise the two homogeneous linear equations in \(A,B\) have a nonzero solution, so their determinant must vanish:
\[
(1+S)(1-S)-S^2=0,\qquad S^2=\tfrac12.
\]
But \(1+S>0\), whereas their first equation and \(S=-2AB\) give
\[
(1+S)A^2=SAB=-\tfrac12 S^2=-\tfrac14<0,
\]
a contradiction. Hence the planar fourth iterate has only the origin as a fixed point. Every fixed point of \(G^4\) must therefore have \(Y=Z=\nu\), and its first coordinate is then forced to be \(X=P(Y)-P(Z)=0\). Thus the only fixed point of \(G^4\) is \((0,\nu,\nu)\), already fixed by \(G\). The same holds for \(N^4\) by conjugacy. (For constant \(P\), which is outside the nonconstant source family, the conclusion is even more immediate.)

**Step 3: a quadratic defining polynomial creates a primitive four-cycle.** Let \(t\in(1,2)\) be the unique root of
\[
t^3-t^2-2=0,\qquad\text{equivalently }t^2(t-1)=2.
\]
Uniqueness in \((1,2)\) follows because the cubic changes sign and is strictly increasing on that interval. Set
\[
\sigma=t^2+(t-1)^2,\qquad
P(u)=\frac{t^2}{4}u(\sigma-u),\qquad \alpha=1,\quad\nu=0.
\]
The displayed cubic identity directly implies
\[
P(0)=0,\qquad P(1)=t,\qquad
P\bigl(t^2\bigr)=P\bigl((t-1)^2\bigr)=1.
\]
For these parameters \(G(X,Y,Z)=(P(Y)-P(Z),Z,(P(Y)-P(Z))^2)\), and substituting these four polynomial evaluations gives the exact orbit
\[
(0,(t-1)^2,0)\longmapsto (1,0,1)
\longmapsto (-t,1,t^2)
\longmapsto (t-1,t^2,(t-1)^2)
\longmapsto (0,(t-1)^2,0).
\]
The four third-coordinate values \(0,1,t^2,(t-1)^2\) are pairwise distinct for \(1<t<2\), proving that the period is *exactly* four. Applying the inverse \(\Phi^{-1}\) to these four points produces a primitive four-cycle of the original pointwise nilpotent-Jacobian polynomial map. Combined with Step 2, this proves the sharp degree threshold.

## Verification
The included `CHECK.py` uses only the Python standard library and exact rational arithmetic in the quotient \(\mathbb Q[t]/(t^3-t^2-2)\). It verifies the polynomial evaluations and all four map transitions without floating-point rounding. Independently, a symbolic calculation of the characteristic polynomial for an arbitrary generic quadratic defining polynomial yields \(s^3\), and explicit symbolic substitution verifies the conjugacy. These checks support, but do not replace, the all-parameter algebraic argument in Step 2 and the general Jacobian computation above. Run `python3 CHECK.py` from the extracted artifact directory.

## Relationship to prior work
Castañeda and Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields* (arXiv:2209.06986v1, 2022), introduce the encompassing family, prove uniqueness of fixed points and absence of two-cycles, establish a three-cycle, and note a five-cycle when the univariate polynomial is linear (their Remark 3.2). Their concluding section explicitly poses the analytic existence question for periods at least four. Chamberland, *Dynamics of Maps with Nilpotent Jacobians* (2006), studies an earlier special family and proves results about two- and three-cycles; his paper's introductory four-cycle concerns a different rational planar map. Neither of these inspected primary texts derives the affine no-four theorem or exhibits the quadratic four-cycle above. The 2024 journal version of the first paper was accessible through bibliographic metadata and abstract but not full-text inspection, so changes between versions remain a priority risk.

## Limitations
The result establishes neither a complete count of primitive four-cycles for quadratic \(P\) nor a classification of every period for higher-degree \(P\). It applies to the stated subfamily; it does not claim that every polynomial map in three dimensions with a nilpotent Jacobian obeys the affine obstruction. The explicit quadratic example has real algebraic coefficients; no assertion about the existence of rational-coefficient examples is made.

## References
1. Á. Castañeda and S. Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1, publicly posted 15 September 2022; subsequently *Archiv der Mathematik*, DOI: 10.1007/s00013-024-02085-8. Source text: https://arxiv.org/pdf/2209.06986
2. M. Chamberland, *Dynamics of Maps with Nilpotent Jacobians*, *Journal of Difference Equations and Applications* 12 (2006), 49–56. DOI: 10.1080/10236190500267970. Lawful author-hosted manuscript: https://chamberland.math.grinnell.edu/papers/nilpotent.pdf
