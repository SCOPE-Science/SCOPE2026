# Exact rational bitangent counts for a tangent-filling plane curve

## Finding

Let \(q=p^r\), where \(p>3\) is prime and \(r\geq1\), and let \(C_q\) be the projective plane curve over \(\mathbb F_q\) defined by
\[
F_q(X,Y,Z)=X^{q-1}+Y^{q-1}+Z^{q-1}-3(X+Y+Z)^{q-1}=0.
\]
A rational tangent means a line tangent at a *smooth* \(\mathbb F_q\)-rational point. Let \(N_1(q)\) count distinct rational tangent lines with exactly one such contact point and \(N_2(q)\) those with exactly two. Every rational tangent has at most two distinct smooth rational contact points. The counts are
\[
(N_1(q),N_2(q))=
\begin{cases}
(7q-23,\ (q-5)^2/2),&q\equiv2\pmod3,\\
(9q-33,\ (q-5)(q-7)/2),&q\equiv1\pmod3.
\end{cases}
\]
In particular, the exact number \(T(q)\) of *distinct* rational tangent lines is
\[
\boxed{T(q)=
\begin{cases}
(q^2+4q-21)/2,&q\equiv2\pmod3,\\
(q^2+6q-31)/2,&q\equiv1\pmod3.
\end{cases}}
\]
The repeated-tangency count is for two distinct smooth \(\mathbb F_q\)-points, not merely for two geometric contacts whose points need not be rational. For example, \((N_1,N_2,T)=(54,18,72)\) over \(\mathbb F_{11}\), \((84,24,108)\) over \(\mathbb F_{13}\), and \((192,180,372)\) over \(\mathbb F_{25}\).

## Assumptions and scope

All assertions refer to the above explicitly marked plane model, not its projective-equivalence class or the complete rational locus of its dual. The source curve has the unique singular point \([1:1:1]\); that established fact is used only to specify which rational points admit tangent lines. Each smooth rational point has nonzero coordinates and nonzero coordinate sum. Scaling gives a unique representative \((x,y,z)\) with \(x+y+z=1\), \(xyz\ne0\), and \((x,y,z)\ne(1/3,1/3,1/3)\). Denote this set by \(\mathcal U_q\). Its cardinality is \((q-1)(q-2)\).

For \((x,y,z)\in\mathcal U_q\), put
\[
e_2=xy+yz+zx,\quad e_3=xyz,\quad
A=9e_2-27e_3-2,\quad B=27e_3-3e_2.
\]
Its tangent is represented in the dual plane by
\[
\Gamma(x,y,z)=[x^{-1}-3:y^{-1}-3:z^{-1}-3].
\]
The point lies on a **two-contact rational tangent** if and only if \(x,y,z\) are pairwise distinct and \(A B(A+B)\ne0\). When this holds, the unique other contact point has coordinates
\[
t=-B/A,\quad
(x',y',z')=\left(
\frac{x}{t+3(1-t)x},\frac{y}{t+3(1-t)y},\frac{z}{t+3(1-t)z}
\right).
\]
This formula defines an involution on the two-contact subset of \(\mathcal U_q\).

## Proof

**Rational source points.** For \(a\in\mathbb F_q^*\), \(a^{q-1}=1\). Therefore the rational points of \(C_q\) away from the established singular point are exactly \(\mathcal U_q\). The number of triples with \(x+y+z=1\) and \(xyz\ne0\) is \(q^2-3q+3\) by inclusion–exclusion; removing the center leaves \((q-1)(q-2)\). Differentiating the defining polynomial, using \(q-1=-1\) in the field, and normalizing the coordinate sum yields \(\Gamma\) as above. Since all three entries would vanish only at the deleted center, \(\Gamma\) is well-defined.

**All possible contacts.** Fix \(P=(x,y,z)\in\mathcal U_q\). If \(P'=(x',y',z')\in\mathcal U_q\) has the same projective tangent, there exists a nonzero \(t\in\mathbb F_q\) such that \(x'^{-1}-3=t(x^{-1}-3)\) and the analogous equations for \(y,z\). Thus, with \(d_v(t)=t+3(1-t)v\), necessarily
\[
(x',y',z')=\left(x/d_x(t),y/d_y(t),z/d_z(t)\right).
\]
Enforcing \(x'+y'+z'=1\), multiplying by \(d_xd_yd_z\), and expanding gives the exact identity
\[
\sum_{v\in\{x,y,z\}}v\!\prod_{w\ne v}d_w(t)-\prod_{v\in\{x,y,z\}}d_v(t)
=-t(t-1)(At+B).
\]
The original contact corresponds to \(t=1\). The root \(t=0\) would give the deleted singular point, whose tangent vector is zero. The remaining possibility is \(t=-B/A\). A distinct, finite, nonzero parameter different from one exists precisely when \(AB(A+B)\ne0\). If \(x,y,z\) are pairwise distinct, no denominator can vanish at this root: one vanishing denominator makes the displayed product identity nonzero, while two simultaneously vanishing denominators would force two coordinates equal. Thus there is a unique other smooth rational contact. Conversely, if two coordinates coincide, then the putative remaining root is exactly the common pole of their denominators. To see this, for \(x=y=a\), \(z=1-2a\), the residual root is \(3a/(3a-1)\) whenever it is defined, exactly where \(d_x=d_y=0\). When \(a=1/3\) this is the excluded center. Finally \(A=B=0\) forces \(e_2=1/3\), \(e_3=1/27\), so \(x,y,z\) are all \(1/3\) (their root polynomial is \((T-1/3)^3\)); this case is already excluded. Hence every fibre has size one or two and the stated criterion is exact. Interchanging the two contact points replaces \(t\) by \(1/t\), proving involutivity.

**Counting the singleton locus.** Put \(u=3x-1\), \(v=3y-1\), \(w=3z-1\). Then \(u+v+w=0\), \(u,v,w\ne-1\), and \((u,v,w)\ne(0,0,0)\). Write \(\sigma_2=uv+uw+vw\), \(\sigma_3=uvw\). A direct substitution gives
\[
A=-\sigma_3,\qquad B=\tfrac23\sigma_2+\sigma_3,\qquad A+B=\tfrac23\sigma_2.
\]
Thus singleton contacts are the union of: the three lines \(uvw=0\); the three diagonals where two of \(u,v,w\) coincide; the quadratic locus \(\sigma_2=0\); and the cubic locus \(2\sigma_2+3\sigma_3=0\). Their subsets in the permitted parameter domain are pairwise disjoint. Each of the first six lines contributes exactly \(q-3\) points after removing the origin and the forbidden coordinates \(-1\), yielding \(6(q-3)\).

Let \(e\in\{0,2\}\) be the number of roots of \(r^2+r+1\) in \(\mathbb F_q\); thus \(e=0\) if \(q\equiv2\pmod3\), and \(e=2\) if \(q\equiv1\pmod3\). Since \(w=-u-v\), the quadratic equation is \(u^2+uv+v^2=0\). When \(e=0\) it has only the removed origin. When \(e=2\), it is the union of two distinct rational lines, and each contributes \(q-4\) permitted points. Its contribution is therefore \(e(q-4)\).

For the cubic, any non-origin solution has \(u\ne0\), so put \(u=s\), \(v=rs\), \(w=-(1+r)s\). Its equation is
\[
-2(r^2+r+1)s^2-3r(r+1)s^3=0.
\]
After discarding \(s=0\), this gives the unique solution
\[
s=-\frac{2(r^2+r+1)}{3r(r+1)}.
\]
Here \(r\) excludes \(0,-1\) and the \(e\) roots of \(r^2+r+1\). The three further values \(r=1,-2,-1/2\) (distinct because \(p>3\)) are exactly those producing \(u=-1\), \(v=-1\), or \(w=-1\). They also account for the cubic's possible non-origin coincidences with a diagonal. The cubic therefore contributes \(q-5-e\) disjoint permitted points, and it does not meet the other exceptional loci in the permitted domain.

Adding the contributions gives the exact number of *singleton source points*:
\[
S(q)=6(q-3)+e(q-4)+(q-5-e)=7q-23+e(q-5).
\]
The complement consists of pairs exchanged by the contact involution. Accordingly
\[
N_1(q)=S(q),\qquad
N_2(q)=\frac{(q-1)(q-2)-S(q)}2,
\qquad T(q)=N_1(q)+N_2(q),
\]
which gives the displayed formulas. No finite-field extrapolation is used.

## Verification

Run \(\texttt{python3 verify_symbolic.py}\) to check the contact-fibre polynomial identity, the centered-coordinate substitutions and the cubic parametrization over \(\mathbb Q\). Run \(\texttt{python3 verify_fields.py}\) to independently enumerate smooth points, projectively normalized gradient lines, singleton/two-point fibres, and the stated formulas over the prime fields of sizes \(5,7,11,13,17,19,23,29,31,37,41\), and the quadratic fields of sizes \(25\) and \(49\). The latter program implements finite-field arithmetic without calling the symbolic program. These finite checks supplement, but do not replace, the unrestricted proof above.

## Relationship to prior work

Asgarli and Ghioca, *Tangent-filling plane curves over finite fields* (first public version 2023-02-26, arXiv:2302.13420), introduced the explicit curve, proved the underlying smooth-point criterion and geometric irreducibility, and showed that it is tangent-filling for \(q\ge11\) in characteristic \(>3\). Their Section 2.1 discusses general upper bounds for bitangents and Section 3.4 proves covering by rational tangents. Those results do not specify the number of distinct tangent lines, their rational-contact multiplicity spectrum, or the explicit pairing formula proved here. The earlier blocking-curve work of Asgarli, Ghioca and Yip (arXiv:2208.13299) concerns a different covering condition.

## Limitations

The formula counts distinct lines with one or two **smooth rational** contacts; it does not count all bitangents over the algebraic closure or all rational points of the geometric dual curve. It makes no claim that different contact points are ordinary tangencies rather than higher-order flex contacts. An earlier unindexed equivalent computation could exist; independent external review has not been performed.

## References

1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, first submitted 2023-02-26, https://arxiv.org/abs/2302.13420 .
2. S. Asgarli, D. Ghioca and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299, first submitted 2022-08-28, https://arxiv.org/abs/2208.13299 .
