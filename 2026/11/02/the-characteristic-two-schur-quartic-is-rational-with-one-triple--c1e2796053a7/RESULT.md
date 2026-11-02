# The characteristic-two Schur quartic is rational with one triple singularity and a two-periodic zeta function

## Finding
The coefficientwise reduction of Schur's classical quartic
\[
S:\quad X_0^4+X_0X_1^3+X_2^4+X_2X_3^3=0\subset\mathbf P^3_{\mathbf F_2}
\]
is a geometrically integral, normal, rational quartic surface, with exactly one geometric singular point \(P=[1:0:1:0]\). Its local multiplicity is three, and its Jacobian/Tjurina scheme is supported at \(P\) with length \(16\). Exactly twelve geometric lines on \(S\) pass through \(P\); they are all defined over \(\mathbf F_4\), and two are defined over \(\mathbf F_2\). For every \(m\ge1\), putting \(q=2^m\) and \(r=\gcd(3,q-1)\),
\[
\#S(\mathbf F_q)=q^2+q+1+r^2q
=\begin{cases}q^2+2q+1 & m\text{ odd},\\q^2+10q+1 & m\text{ even}.\end{cases}
\]
The zeta function of **the singular surface itself** is
\[
Z(S/\mathbf F_2,T)=\frac{1}{(1-T)(1-4T)(1-2T)^6(1+2T)^4}.
\]

## Assumptions and scope
The field has characteristic two; geometric assertions are over its algebraic closure. The equation is the literal coefficientwise reduction of the displayed integral model, not a reduction of some projectively equivalent model using a change of coordinates with denominators divisible by two. The zeta function counts rational points of the singular projective surface, not those of a resolution.

## Proof
**1. A linear-in-one-coordinate model.** Put \(z=X_0\), \(t=X_0+X_2\), \(v=X_1\), and \(w=X_3\). The characteristic-two binomial identity yields
\[
F=z(v^3+w^3)+t(t^3+w^3).
\]
Write \(C=v^3+w^3\), \(N=t(t^3+w^3)\). Over an algebraic closure, the three linear factors of \(C\) have the form \(v-\zeta w\), for \(\zeta^3=1\); the four linear factors of \(N\) have the form \(t\) and \(t-\zeta w\). Because these factor sets are disjoint in \(k[t,v,w]\), \(\gcd(C,N)=1\). Thus \(zC+N\) is irreducible as a primitive polynomial of degree one in \(z\), proving geometric integrality.

**2. Singular locus and local structure.** The homogeneous partial derivatives in the \((z,t,v,w)\) coordinates are
\[
(F_z,F_t,F_v,F_w)=(v^3+w^3,\ w^3,\ zv^2,\ (z+t)w^2).
\]
At any projective singular point, \(w=v=0\), and the equation forces \(t^4=0\); hence \(t=0\) and \(z\ne0\), giving only \(P=[1:0:0:0]\) in the new coordinates. In the affine chart \(z=1\),
\[
f=t^4+v^3+(1+t)w^3.
\]
The lowest-degree term is \(v^3+w^3\), a product of three distinct linear forms over \(\mathbf F_4\), so the point has multiplicity three (and is not an ordinary double point). Since \(f_t=w^3\), \(f_v=v^2\), and \(f_w=(1+t)w^2\), the completed local Tjurina algebra is
\[
k[[t,v,w]]/(f,f_t,f_v,f_w)\cong k[[t,v,w]]/(t^4,v^2,w^2).
\]
The latter has basis \(t^iv^jw^h\) for \(0\le i<4\), \(0\le j,h<2\), of length \(16\). A hypersurface is Cohen–Macaulay; its singular locus here has codimension two in the surface, so Serre's \(R_1\) and \(S_2\) conditions prove normality.

**3. Rationality and lines through the singular point.** The projection from \(P\) to \(\mathbf P^2_{[t:v:w]}\) has inverse on the open locus \(C\ne0\) given by
\[
[t:v:w]\longmapsto[N:tC:vC:wC].
\]
Indeed \(F(N,tC,vC,wC)=0\) by homogeneity and characteristic two, and the projection returns \([t:v:w]\). Thus \(S\) is rational over \(\mathbf F_2\). A line through \(P\) with direction \([t:v:w]\) is contained in \(S\) exactly when \(C=N=0\). For nonzero \(w\), scale \(w=1\): \(v^3=1\) has three roots, while \(t(t^3+1)=0\) has four. If \(w=0\), the two equations force \(v=t=0\), which is not a projective direction. Thus precisely \(12\) geometric lines pass through \(P\), all defined over \(\mathbf F_4\); exactly \(1\cdot2=2\) are defined over \(\mathbf F_2\).

**4. All-extension point counts.** Let \(q=2^m\) and \(r=\gcd(3,q-1)\). The plane cubic \(C=0\) consists of \(r\) \(\mathbf F_q\)-lines through the point \([1:0:0]\), hence has \(1+rq\) rational points. The base-direction set \(B=V(C,N)\subset\mathbf P^2\) has \(r(r+1)\) rational points (\(r\) with \(t=0\) and \(r^2\) with \(t^3=w^3\)). For a direction with \(C\ne0\), exactly one point of \(S\setminus\{P\}\) projects to it. For a direction with \(C=0\) and \(N\ne0\), there are none. For each direction in \(B\), the entire line through \(P\) lies on \(S\), contributing \(q\) points apart from \(P\). Therefore
\[
\#S(\mathbf F_q)=1+\bigl((q^2+q+1)-(1+rq)\bigr)+q\,r(r+1)
=q^2+q+1+r^2q.
\]
For odd \(m\), \(r=1\), while for even \(m\), \(r=3\). Equivalently,
\[
\#S(\mathbf F_{2^m})=1+4^m+6\cdot2^m+4\cdot(-2)^m.
\]
By the definition of the Hasse–Weil zeta function as \(\exp(\sum_{m\ge1}\#S(\mathbf F_{2^m})T^m/m)\), this gives the stated factorization exactly.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 and no external packages. Exact finite-field enumeration in \(\mathbf F_2\), \(\mathbf F_4\), \(\mathbf F_8\), and \(\mathbf F_{16}\) gives respectively \(9,57,81,417\) points and \(2,12,2,12\) rational directions of lines through \(P\), agreeing with the formulas. The script also checks equality of the original and transformed equations on all enumerated projective points. These finite checks independently corroborate but do not replace the algebraic proofs of uniqueness, rationality, or formulas for all extensions.

## Relationship to prior work
Schur's classical quartic and its 64-line smooth geometry in characteristics other than two and three are documented by Rams–Schütt [1]. Rams–Schütt [2] explicitly note that the Schur quartic degenerates in characteristic two, but study upper bounds for **smooth** characteristic-two quartics, not the complete singular geometry of this particular coefficientwise reduction. Thus the bare observation of degeneration is established background. The present analysis concerns the precise normal rational special fiber: its lone non-Du Val triple point, Tjurina length, twelve concurrent lines, and complete point-count/zeta formulas.

## Limitations
This does not count all geometric lines on the surface, only those through the singular point. It does not determine a minimal resolution or its zeta function, nor the full analytic classification of the triple singularity. The literature comparison supports a provisional novelty assessment; no exhaustive historical priority guarantee or independent validation is asserted. The local Jacobian scheme length is a scheme-theoretic statement, distinct from the one-point reduced singular support.

## References
[1] S. Rams and M. Schütt, *64 lines on smooth quartic surfaces*, arXiv:1212.3511, first public version 2012-12-14, https://arxiv.org/abs/1212.3511.
[2] S. Rams and M. Schütt, *At most 64 lines on smooth quartic surfaces (characteristic 2)*, arXiv:1512.01358, first public version 2015-12-04, https://arxiv.org/abs/1512.01358; *Nagoya Mathematical Journal* 232 (2018), 76–95, doi:10.1017/nmj.2017.21.
