# No real tangent-plane ramification in the five Appendix A.1 double-line spectrahedral witnesses
## Finding
Helsø--Ranestad give five explicit real symmetric \(4	imes4\) pencils in Appendix A.1, realizing the double-line spectrahedral node-count pairs \((a,b)=(6,4),(4,4),(4,2),(2,2),(2,0)\). For every one of these five pencils, the real rank-two double line has no real tangent-plane coalescence point.

More explicitly, take homogeneous coordinates \([z:w]\) on the double line and normal coordinates \((u,v)\) obtained from the two linear equations of that line. If the determinant is expanded in \((u,v)\), its degree-two normal part has discriminant, up to a positive scalar, equal in the five cases to
\[
egin{aligned}
(6,4):&\quad (w^2+2wz+2z^2)(2w^2+2wz+z^2),\
(4,4):&\quad (2w^2-2wz+z^2)(8w^2-4wz+z^2),\
(4,2):&\quad (w^2+2wz+2z^2)(w^2+4wz+5z^2),\
(2,2):&\quad (w^2+2wz+2z^2)(2w^2+2wz+z^2),\
(2,0):&\quad (4w^2+4wz+5z^2)(8w^2+4wz+z^2).
\end{aligned}
\]
Each binary quadratic factor is positive definite over \(\mathbb R\), and in every row the two factors are coprime. Therefore the transverse tangent cone is a pair of distinct real planes at every real point of the double line. Over \(\mathbb C\), the coalescence divisor has four simple points, all nonreal and hence arranged in two conjugate pairs.

## Assumptions and scope
The claim is about exactly the five matrices printed in Appendix A.1 of arXiv:1810.11235. It does not assert that every real quartic spectrahedral symmetroid with a rank-two double line has the same branch behavior. The matrices are taken over \(\mathbb R\), and the tangent-cone calculation is performed over \(\mathbb Q\) before interpreting the real roots.

## Proof
For a quartic determinant \(F=\det A\) singular doubly along a line \(L\), choose a parameter \([z:w]\) on \(L\) and two normal linear coordinates \((u,v)\). Write
\[
F=Q_2(u,v;z,w)+Q_3(u,v;z,w)+Q_4(u,v;z,w),
\]
where \(Q_i\) has total degree \(i\) in \((u,v)\). At a point of \(L\), the transverse tangent cone is \(Q_2=0\). Writing \(Q_2=A u^2+Buv+C v^2\), the two tangent planes coincide exactly when \(\Delta=B^2-4AC=0\).

For the five source matrices, use respectively \(u=x+w,x-w,x,x-2w,x+w\), and use \(v=y\); on \(L\) this leaves \([z:w]\). Exact determinant expansion gives the five factorizations in the Finding. Every factor has positive leading coefficient and negative binary discriminant. For example, \(w^2+2wz+2z^2\) has binary discriminant \(-4\), while \(2w^2+2wz+z^2\) has binary discriminant \(-4\). The same elementary check applies to every listed factor. Thus none vanishes on \(\mathbb RP^1\). The factors in each row are nonproportional, so they are coprime; each has two simple complex-conjugate roots. Hence the degree-four coalescence divisor consists of four distinct nonreal points.

## Verification
The accompanying `verify.py` reconstructs all five printed symmetric matrices, computes each determinant exactly, extracts the degree-two normal part, forms \(B^2-4AC\), and compares it with the displayed factorization. It then checks positive definiteness of every binary quadratic factor by its exact discriminant and verifies coprimality of the two factors. Running `python verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Helsø--Ranestad classify the possible real-node counts for a general rank-two double-line spectrahedral symmetroid and Appendix A.1 prints witnesses for every realized pair except \((0,0)\). Their discussion records the double line, the isolated-node counts, and the spectrahedral position, but it does not give the transverse tangent-cone discriminants of the five witnesses. Helsø's earlier classification of rational quartic symmetroids establishes the double-line family and its six additional rank-two points in the general complex case, but likewise does not determine this real coalescence divisor for the Appendix A.1 matrices. Classical double-line theory explains that the discriminant of the transverse quadratic tangent cone detects coalescing tangent planes; the contribution here is the exact complete real census for this five-matrix benchmark list.

## Limitations
This is a finite, source-specific classification. It neither settles the missing \((0,0)\) existence problem nor proves that real tangent-plane coalescence is impossible elsewhere in the double-line spectrahedral family. The result concerns the tangent-cone branch divisor; it makes no additional global claim about the normalization away from the double line.

## References
1. M. Helsø and K. Ranestad, *Rational Quartic Spectrahedra*, arXiv:1810.11235, especially Proposition 2.7, Remark 2.8, and Appendix A.1.
2. M. Helsø, *Rational Quartic Symmetroids*, arXiv:1708.04101; Advances in Geometry 20 (2020), 71--89.
