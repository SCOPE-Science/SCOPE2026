# The first integral-forcing Morse obstruction in a planar homogeneous cubic family

## Finding

The planar homogeneous cubic family
\[
 F_b(x,y)=\bigl(-r^2+b(x^2-y^2)\bigr)(x,y)+r^2(-y,x),\qquad r^2=x^2+y^2,
\]
has a structural transition between strict quadratic Lyapunov certificates and strict higher-degree polynomial certificates. Among nonnegative integer parameters, the least \(b\) for which no local \(C^2\) Morse Lyapunov function exists is \(b=2\). At this value the origin nevertheless has a strict coercive homogeneous quartic polynomial Lyapunov function.

Explicitly, for \(b=2\), put
\[
 V(x,y)=33x^4-150x^3y+326x^2y^2-318xy^3+125y^4.
\]
Then \(V(x,y)>0\) and \(\mathcal L_{F_2}V(x,y)<0\) for every \((x,y)\ne(0,0)\). However, there is no \(C^2\) function defined near the origin with a positive-definite Hessian there, a strict local minimum there, and nonpositive Lie derivative on a punctured neighborhood. This is a local obstruction, so in particular no global smooth Morse Lyapunov function exists.

## Assumptions and scope

All vector fields are autonomous polynomial maps on \(\mathbb R^2\); time is the original physical time. The integer parameter claim compares \(b=0\), \(b=1\), and \(b=2\) and makes no claim about a complete real-parameter transition. A Morse Lyapunov function is at least \(C^2\), attains a strict nondegenerate minimum at the equilibrium, and has a nonpositive directional derivative along the field in a neighborhood. A strict Lyapunov function has strictly negative derivative outside the equilibrium. The family and the general issue of non-Morse Lyapunov functions are established background; the claim is the exact certificate/obstruction combination at the indicated parameters.

## Proof

**The two smaller integer values.** At \(b=0\), \(Q_0=r^2\) has derivative \(\mathcal L_{F_0}Q_0=-2r^4\). At \(b=1\), use the positive-definite quadratic \(Q_1=r^2-xy\). In polar coordinates put \(C=\cos(2\theta)\) and \(S=\sin(2\theta)\). Since \(\dot r=r^3(-1+C)\) and \(\dot\theta=r^2\),
\[
 \frac{\mathcal L_{F_1}Q_1}{2r^4}
 =-1+\frac12(C+S-CS)
 \le-\frac12,
\]
because \((1-C)(1-S)\ge0\). Both quadratics have positive-definite Hessians and are coercive and strict.

**An exact strict quartic at the next integer.** For \(b=2\), the components of the field are
\[
 f_x=x^3-3xy^2-x^2y-y^3,\qquad
 f_y=x^3+x^2y+xy^2-3y^3.
\]
Differentiation gives
\[
 -\mathcal L_{F_2}V
 =18x^6+80x^5y-254x^4y^2-896x^3y^3
 +3598x^2y^4-3664xy^5+1182y^6.
\]
For the monomial columns \(u_2=(x^2,xy,y^2)^\top\) and \(u_3=(x^3,x^2y,xy^2,y^3)^\top\), the following are exact identities:
\[
 V=u_2^\top A u_2,\quad -\mathcal L_{F_2}V=u_3^\top B u_3,
\]
\[
 A=\begin{pmatrix}33&-75&50\\-75&226&-159\\50&-159&125\end{pmatrix},
 \qquad
 B=\begin{pmatrix}
18&40&-220&140\\
40&186&-588&330\\
-220&-588&2938&-1832\\
140&330&-1832&1182
\end{pmatrix}.
\]
Their respective leading principal minors are
\[
 (33,1833,22352)\quad\text{and}\quad
 (18,1748,258632,5083552).
\]
All are positive; Sylvester's criterion therefore makes both matrices positive definite. Since neither monomial column vanishes off the origin, both inequalities are strict. Positive definiteness, radial unboundedness and the strict derivative establish global asymptotic stability and global existence of forward trajectories.

**No \(C^2\) Morse Lyapunov function.** Suppose one exists near the origin. Its positive-definite quadratic Taylor term may, after multiplying by a positive scalar, be written
\[
 Q(x,y)=x^2+y^2+d(x^2-y^2)+2e xy.
\]
The field is homogeneous cubic. Because the putative Lyapunov function is \(C^2\), its gradient is \(\nabla Q+o(r)\), and division of the Lyapunov inequality along the ray \(r u\) by \(r^4\) proves the necessary global homogeneous inequality \(D:=\mathcal L_{F_2}Q\le0\) on the unit circle and hence on the plane. Exact substitution yields
\[
 D(1,0)=2(1+d+e),\qquad D(1,1)=-8(1+d+e).
\]
Thus \(d+e=-1\), and in particular \(D(1,0)=0\). As \(D\le0\) and \((1,0)\) is a direction on the circle, its tangential derivative there vanishes. Direct differentiation gives
\[
 \partial_yD(1,0)=4(e-d)=0,
\]
so \(d=e=-\tfrac12\). At that unique possible pair one instead has the exact identity
\[
 D(x,y)=8y^3(x-y),\qquad D(2,1)=8>0,
\]
a contradiction. The necessary inequality is impossible for every positive-definite Hessian (indeed for any normalized quadratic), proving the local claim.

## Verification

Run `python3 verification.py` with the Python standard library. The included program reconstructs the two vector-field components, the quartic, the sextic Lie derivative, both Gram expansions, their exact principal minors, and the directional Hessian contradiction using integer and rational arithmetic. Fourteen exact assertions passed. The Gram/principal-minor argument and the local Hessian argument, rather than any finite sampling, prove the statements for all real planar points and all \(C^2\) local candidates.

## Relationship to prior work

W. Jongeneel (arXiv:2610.05626, publicly submitted October 4, 2026) considers existence of Morse Lyapunov functions for globally stable vector fields and presents a non-Morse example. J. Liu and M. Fitzsimmons (arXiv:2607.16171) introduce a planar homogeneous cubic family, containing the displayed field, and prove nonexistence of any polynomial Lyapunov function in a different, more strongly forced parameter region. We do not claim the family, global stability mechanism, or the general non-Morse phenomenon as new. The present result isolates an explicit smallest integer forcing for *non-Morse behavior coexisting with a strict quartic polynomial Lyapunov function* and supplies both sides as exact rational certificates. The general sum-of-squares Lyapunov machinery of Ahmadi and El Khadir (arXiv:1803.01877) is established background.

## Limitations

The comparison is among nonnegative integral forcing parameters with unit damping and unit angular rotation; it does not classify all real parameter values, all homogeneous cubic fields, or existence of degenerate smooth Lyapunov functions. The obstruction is only to the nondegenerate minimum condition. Existence of a higher-degree polynomial Lyapunov function is not claimed to imply existence of a Morse one. Literature searches cannot exclude an unindexed equivalent example or a previously implicit specialization of a general result. This is a mathematical certificate with no independent audit yet.

## References

- W. Jongeneel, *On global Lyapunov functions being Morse*, arXiv:2610.05626 (initial public version October 4, 2026), https://arxiv.org/abs/2610.05626.
- J. Liu and M. Fitzsimmons, *A Globally Asymptotically Stable Planar Homogeneous Polynomial Vector Field With No Polynomial Lyapunov Function*, arXiv:2607.16171 (initial public version July 17, 2026), https://arxiv.org/abs/2607.16171.
- A. A. Ahmadi and B. El Khadir, *On Algebraic Proofs of Stability for Homogeneous Vector Fields*, arXiv:1803.01877 (2018), https://arxiv.org/abs/1803.01877.
