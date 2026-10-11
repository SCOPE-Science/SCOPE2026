# Exact norms of Dirac-diagonal operators on real Lipschitz-free spaces

## Finding
Let \((M,d,o)\) be any pointed metric space with at least two points. The real Lipschitz-free space \(\mathcal F(M)\) is the completion of the span of point evaluations \(\delta_x\), with \(\delta_o=0\). Let \(\lambda_x\in\mathbb R\) for each \(x\in M\setminus\{o\}\), and define \(D_\lambda\delta_x=\lambda_x\delta_x\) on the algebraic span.

For distinct non-root points \(x,y\), write
\[
a=d(o,x),\qquad b=d(o,y),\qquad c=d(x,y)
\]
and define
\[
H_{xy}(\lambda)=\frac1c\max\Big\{
|a\lambda_x-b\lambda_y|,\;
|a\lambda_x-(a-c)\lambda_y|,\;
|(b-c)\lambda_x-b\lambda_y|
\Big\}.
\]
Then the following extended nonnegative quantity is precisely the norm of the formal diagonal map:
\[
\mathcal N(\lambda)=\max\left\{\sup_{x\ne o}|\lambda_x|,\;
\sup_{x\ne y,\ x,y\ne o}H_{xy}(\lambda)\right\}.
\]
An empty supremum is zero. **The map extends to a bounded operator on \(\mathcal F(M)\) if and only if \(\mathcal N(\lambda)<\infty\)**, in which case \(\|D_\lambda\|=\mathcal N(\lambda)\). No compactness, discreteness or cardinality restriction is assumed.

For a subset \(S\subseteq M\setminus\{o\}\), the coordinate selector \(P_S\delta_x=\mathbf1_S(x)\delta_x\) has norm zero if \(S=\varnothing\), and otherwise
\[
\|P_S\|=\max\left\{1,\;
\sup_{\substack{x\in S,\ y\notin S\\ y\ne o}}\frac{d(o,x)}{d(x,y)}\right\},
\]
where an infinite value means that the algebraic selector does not extend boundedly. For finite \(M\), the exact constants for the canonical Dirac basis are
\[
K_{\mathrm{supp}}=\max\left\{1,\sup_{x\ne y,\ x,y\ne o}\frac{\max\{d(o,x),d(o,y)\}}{d(x,y)}\right\},
\quad
K_{\pm}=\max\left\{1,\sup_{x\ne y,\ x,y\ne o}\frac{d(o,x)+d(o,y)}{d(x,y)}\right\}.
\]
Thus every coordinate projection is contractive exactly when \(d(x,y)\ge\max\{d(o,x),d(o,y)\}\) for all distinct non-root points; every sign change is contractive exactly when \(d(x,y)=d(o,x)+d(o,y)\) for all such pairs (the rooted-star metric).

## Assumptions and scope
All scalars and Lipschitz functions are real, the metric is genuine and positive off the diagonal, and the basepoint \(o\) is fixed. In an infinite metric space the Dirac family need not be a Schauder basis; the statement concerns algebraic diagonals and their bounded extensions, not a claimed infinite basis. The basis-constant language applies only to finite \(M\). Supremums may be infinite, and the theorem distinguishes these unbounded cases. In finite spaces the operator norms are computable from the distance matrix and the symbol in quadratic time.

## Proof
Finite Dirac families are algebraically independent: arbitrary real values prescribed on finitely many non-root points (and zero at the root) have a finite Lipschitz constant on that finite set and extend to all of \(M\) by McShane's theorem. Thus the displayed formal diagonal is unambiguously defined.

The Arens--Eells description says that the closed unit ball of \(\mathcal F(M)\) is the closed absolutely convex hull of normalized molecules \((\delta_x-\delta_y)/d(x,y)\). For any linear map on their algebraic span, a finite bound on the images of all these molecules therefore gives the same bound on the operator norm and yields a unique bounded extension. Conversely every bounded extension obeys each molecular bound. By duality with \(\operatorname{Lip}_0(M)\),
\[
\left\|D_\lambda\frac{\delta_x-\delta_y}{d(x,y)}\right\|=
\sup_{\substack{f(o)=0\\\operatorname{Lip}(f)\le1}}
\frac{|\lambda_x f(x)-\lambda_y f(y)|}{d(x,y)}.
\]
For a pair \((o,x)\), the supremum equals \(|\lambda_x|\), since \(|f(x)|\le d(o,x)\) and equality is achievable by a distance function.

For a non-root pair \((x,y)\), let \(u=f(x)\), \(v=f(y)\) and use the three distances \((a,b,c)\) defined above. The admissible value pairs are exactly
\[
\mathcal H_{a,b,c}=\{(u,v)\in\mathbb R^2:|u|\le a,\ |v|\le b,\ |u-v|\le c\}.
\]
Indeed the three inequalities make \(f(o)=0,f(x)=u,f(y)=v\) a \(1\)-Lipschitz function on those three points. McShane extension gives a \(1\)-Lipschitz extension to all of \(M\) with the same values, so no other points impose hidden restrictions. The triangle inequalities \(|a-b|\le c\le a+b\) show that the vertices of this centrally symmetric polygon are among, and collectively exactly comprise (with repetitions at degenerate triangles), the six points
\[
\pm(a,b),\qquad\pm(a,a-c),\qquad\pm(b-c,b).
\]
A linear functional attains the largest absolute value at one of these vertices; applying this to \(\lambda_xu-\lambda_yv\) yields precisely \(H_{xy}(\lambda)\). Taking the supremum over all molecules proves the norm formula and the if-and-only-if bounded extension statement, including infinite \(M\).

For \(P_S\), a pair with both endpoints in or both outside \(S\) has local contribution \(1\) or \(0\); when \(x\in S\) and \(y\notin S\), the hexagonal maximum is \(a/c\), because \(|b-c|\le a\). The spoke contribution is \(1\) when \(S\ne\varnothing\). Taking the supremum over cuts proves the projection formula and the suppression constant. For a diagonal with \(\lambda_x,\lambda_y\in\{-1,1\}\), equal signs contribute \(1\) and opposite signs contribute \((a+b)/c\): the other two vertex values cannot exceed \(a+b\) by the triangle inequalities. Every pair can be assigned opposite signs, proving the sign constant. The contractivity characterizations follow by considering both singleton orientations of each cut and by comparing \(c\le a+b\) with the condition \((a+b)/c\le1\).

## Verification
Run `python3 verification/dirac_multiplier_checker.py` using standard-library Python 3. It independently enumerates all intersections of the six boundary lines of the three-point Lipschitz polygon with exact rational arithmetic, testing \(7000\) combinations of integral metric triples and symbols; it also checks projection and opposite-sign identities. Its recorded output is `DIRAC_MULTIPLIER_LOCAL_EXACT_OK 7000`.

Optionally run `python3 verification/global_lp_stress.py` (Python 3 with SciPy). It optimizes the full global Lipschitz polytope for \(720\) deterministic finite shortest-path metrics and coefficient assignments, independently comparing with the local formula. Its recorded output is `DIRAC_MULTIPLIER_GLOBAL_LP_OK 720`. Both programs are supplementary checks. The proof above, not finite sampling or linear-programming solver success, establishes the statements for all finite and infinite metric spaces.

Two illustrations delimit the geometry. In a finite equilateral metric with at least three points the multiplier norm is \(\max\{\sup_x|\lambda_x|,\sup_{x\ne y}|\lambda_x-\lambda_y|\}\): suppression is \(1\) while sign unconditionality is \(2\). In a rooted-star metric (all non-root distances are sums of the two root distances), \(\mathcal N(\lambda)=\sup_x|\lambda_x|\), and both constants equal \(1\). On the ordinary interval with basepoint \(0\), a selector retaining an isolated single nonzero point is unbounded because other points approach it; this does not contradict the finite basis theorem.

## Relationship to prior work
Godard's tree-metric classification identifies rooted-tree free spaces with \(L^1\)-type spaces, consistent with the star specialization. Hájek and Pernecká construct Schauder bases for certain free spaces, and Novotný constructs retractional bases on grids with bounds controlled by their retractions; these are not exact norms for the canonical point-evaluation diagonals on all pointed metrics. Allen and collaborators study multiplication operators between tree-based Lipschitz-type function spaces with weighted function norms and norm estimates, rather than this universal free-space diagonal norm. The local six-vertex calculation, global diagonal boundedness criterion, and exact cut/sign constants are the present assertions; the underlying duality, extension theorem, and rooted-star \(\ell_1\) case are classical.

## Limitations
An equivalent norm formula might be present in older work on pointwise multipliers of Lipschitz algebras or Schauder multipliers without the vocabulary of Lipschitz-free spaces. The listed sources and targeted searches did not establish such coverage; this is a bibliographic risk, not proof of novelty. The result is real-scalar only and gives no criterion for arbitrary non-diagonal operators. Its exact expression can be infinite for infinite metric spaces, where canonical Dirac evaluations need not form a Schauder basis.

## References
- A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178v1 (first public posting 2009-04-21), Sections 1--5; primary MSC 46B04. https://arxiv.org/abs/0904.3178
- P. Hájek and E. Pernecká, *On Schauder bases in Lipschitz-free spaces*, J. Math. Anal. Appl. 416 (2014), 629--646, doi:10.1016/j.jmaa.2014.02.060. https://doi.org/10.1016/j.jmaa.2014.02.060
- R. F. Allen and collaborators, *Multiplication operators between Lipschitz-type spaces on a tree*, Int. J. Math. Math. Sci. (2011), doi:10.1155/2011/472495. https://doi.org/10.1155/2011/472495
- M. Novotný, *Schauder Basis on Free-Lipschitz Spaces of Grids*, POSTER 2016, Prague, May 24, 2016, proceedings pp. 1--5. https://poster.fel.cvut.cz/poster2016/proceedings/Section_NS/NS_066_Novotny.pdf
