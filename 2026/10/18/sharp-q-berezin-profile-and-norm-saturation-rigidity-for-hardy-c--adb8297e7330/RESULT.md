# Sharp \(q\)-Berezin profile and norm-saturation rigidity for Hardy constant-symbol composition

## Finding
Let \(H^2(\mathbb D)\) be the Hardy Hilbert space, and let \(C_c f=f(c)\,\mathbf 1\) for an arbitrary \(c\in\mathbb D\). For \(0<q\le1\), write \(a=|c|\), \(b=\sqrt{1-a^2}\), and \(k=\sqrt{1-q^2}\). Then the sharp \(q\)-Berezin number is
\[
\boxed{\operatorname{ber}_q(C_c)=\frac{2q}{1-a k+q b}.}
\]
The supremum is always attained. If \(c\ne0\), the maximizing *ordered normalized-kernel pair* is unique and is described explicitly by
\[
 u_* =r_*\frac{c}{|c|},\qquad
 v_* =\frac{r_*-k}{1-kr_*}\frac{c}{|c|},\qquad
 r_* =\frac{a+k}{1+ak+qb}.
\]
For \(c=0\), the maximizing pairs are all simultaneous rotations of the real pair \(u_*=k/(1+q)\), \(v_*=-k/(1+q)\); for \(q=1\) this reduces to the unique pair \((0,0)\).

The operator norm is \(\|C_c\|=1/b\). Hence
\[
\operatorname{ber}_q(C_c)=\|C_c\|
\quad\Longleftrightarrow\quad q=\sqrt{1-|c|^2}.
\]
In fact its relative defect has the exact stability identity
\[
 1-\frac{\operatorname{ber}_q(C_c)}{\|C_c\|}
 =\frac{(a-k)^2+(b-q)^2}{2(1-ak+qb)}.
\]
For each fixed \(q\in(0,1]\), the complete range over constant symbols is
\[
 \bigl\{\operatorname{ber}_q(C_c):c\in\mathbb D\bigr\}
 =\left[\frac{2q}{1+q},\frac{2q}{1-\sqrt{1-q^2}}\right).
\]
The left endpoint occurs only at \(c=0\) and the right endpoint is a nonattained boundary limit. In particular, the \(q\)-Berezin numbers stay bounded at fixed \(q\), although \(\|C_c\|\to\infty\) as \(|c|\uparrow1\).

## Assumptions and scope
The kernel and inner product conventions are
\[
 k_u(z)=(1-\overline u z)^{-1},\qquad
 \widehat k_u=\sqrt{1-|u|^2}\,k_u,\qquad
 \langle f,g\rangle=\sum_{n\ge0}\widehat f(n)\overline{\widehat g(n)}.
\]
The positive-real overlap convention is essential:
\[
 \operatorname{ber}_q(T)
 =\sup\bigl\{|\langle T\widehat k_u,\widehat k_v\rangle|:
 u,v\in\mathbb D,\ \langle\widehat k_u,\widehat k_v\rangle=q\bigr\},
 \qquad 0<q\le1.
\]
The symbol \(c\) is a constant in the open disk, not a linear symbol \(z\mapsto\xi z\). The result concerns scalar-valued composition operators on ordinary \(H^2\), not all rank-one Hilbert-space operators or other reproducing-kernel geometries. The parameter \(q=0\) is excluded because two normalized Szegő kernels never have zero inner product.

## Proof
Put \(u=r e^{i\theta}\) with \(0\le r<1\). The normalized Szegő-kernel overlap is
\[
 \langle\widehat k_u,\widehat k_v\rangle
 =\frac{\sqrt{(1-|u|^2)(1-|v|^2)}}{1-\overline u v}.
\]
For it to equal the positive number \(q\), the quantity \(\overline u v\) must be real. If \(r>0\), this forces \(v=s e^{i\theta}\) for a real \(s\in(-1,1)\); solving the resulting scalar equation gives exactly
\[
 s_\pm(r)=\frac{r\pm k}{1\pm kr}.
\]
For \(u=0\), every \(v\) of modulus \(k\) is admissible. Both descriptions include \(q=1\), where the two scalar branches coincide. This kernel-pair parametrization is also established in [1, Theorem 2.2].

Since \(C_c\widehat k_u=\sqrt{1-r^2}(1-\overline u c)^{-1}\mathbf1\), the objective on a feasible pair equals
\[
 |\langle C_c\widehat k_u,\widehat k_v\rangle|
 =\frac{q(1-rs)}{|1-\overline u c|}.
\]
For any fixed positive \(r\), the minus branch gives the larger numerator, because \(s_-(r)\le s_+(r)\). Also \(|1-\overline u c|\ge1-ar\), with equality for \(u\) on the ray through \(c\) when \(c\ne0\). Therefore
\[
 \operatorname{ber}_q(C_c)
 =q\sup_{0\le r<1}
 \frac{1-rs_-(r)}{1-ar}
 =q\sup_{0\le r<1}
 \frac{1-r^2}{(1-kr)(1-ar)}.
\]
The same formula holds at \(r=0\), because there the phase of \(v\) does not affect the objective.

Set \(D=1-ak+qb\), \(L=1+ak+qb\), and \(t=a+k\). Both \(D\) and \(L\) are positive, and \(t^2=L(1+ak-qb)\) by \(a^2+b^2=k^2+q^2=1\). Direct expansion gives the globally exact nonnegative certificate
\[
 2(1-kr)(1-ar)-D(1-r^2)
 =\frac{(Lr-t)^2}{L}\ge0.
\]
Consequently the displayed supremum is at most \(2q/D\), and equality holds at the unique point \(r_*=t/L\). This point lies in \([0,1)\), since \(L-t=(1-a)(1-k)+qb>0\). The sign-branch comparison is strict when \(r>0\) and \(q<1\); in the remaining cases the branches coincide or the phase is irrelevant. This also proves the stated ordered-pair equality characterization.

The rank-one formula \(C_c f=\langle f,k_c\rangle\mathbf1\) yields \(\|C_c\|=\|k_c\|=1/b\). From the sharp profile,
\[
 \frac{\operatorname{ber}_q(C_c)}{\|C_c\|}
 =\frac{2bq}{1-ak+bq},
 \qquad
 1-\frac{\operatorname{ber}_q(C_c)}{\|C_c\|}
 =\frac{1-ak-bq}{1-ak+bq}.
\]
As \((a,b)\) and \((k,q)\) are unit vectors in the positive quadrant, Cauchy--Schwarz gives \(ak+bq\le1\) with equality precisely when \(a=k\) and \(b=q\). The two-squared-distance identity for their chord proves the stated exact relative defect and the unique saturation value of \(q\).

Finally, for fixed \(q\), the denominator \(1-ak+q\sqrt{1-a^2}\) is strictly decreasing on \([0,1)\), since its derivative is \(-k-qa/\sqrt{1-a^2}\), strictly negative for \(a>0\). Evaluating at \(a=0\) and letting \(a\uparrow1\) establishes the precise half-open range and the bounded-versus-unbounded contrast.

## Verification
A standard-library Python diagnostic, `check_q_berezin.py`, recomputes the two-parameter formula, all equality witnesses, the normalization constraint, the perfect-square certificate, boundary behavior, and the norm-saturation defect. It additionally performs finite Hardy-coefficient inner-product tests on representative constrained kernel pairs. A deterministic execution completed 41,440 finite diagnostic assertions. These checks detect arithmetic or normalization mistakes but do not replace the preceding all-parameter proof.

## Relationship to prior work
Bhattacharya and Patra [1] provide the exact geometry of kernel pairs with overlap \(q\) and investigate \(q\)-Berezin ranges for several operator classes. Their Section 3.4 treats \(\phi(z)=\xi z\); its \(\xi=0\) instance yields the already-known \(c=0\) endpoint \(2q/(1+q)\). The present assertion concerns all nonzero *constant* symbols and includes the sharp two-parameter numerical profile, full equality characterization, saturation locus, and boundary behavior. Thus the origin case and the kernel-pair parametrization are not asserted to be novel.

Stojiljković, Başaran, and Gürdal [2] introduce the \(q\)-Berezin invariant and general operator inequalities. The paper does not compute the constant-symbol Hardy composition profile. Augustine, Garayev, and Shankar [3] study the ordinary Berezin ranges of finite-rank Hardy and Bergman operators; their one-kernel invariant does not supply the two-kernel \(q\)-profile for \(q<1\). Their earlier composition-operator paper [4] addresses ordinary Berezin-range convexity of other symbol families. Generic rank-one \(q\)-numerical-radius bounds use arbitrary unit-vector pairs and do not determine the constrained normalized Szegő-kernel supremum here.

## Limitations
The sharp profile applies only to \(c\in\mathbb D\), \(0<q\le1\), and the unweighted scalar Hardy space. The boundary quantity at \(|c|=1\) is a limit, not a bounded composition operator in this family. The result does not classify every point in the full complex \(q\)-Berezin range, nor all nonlinear analytic composition symbols. Exhaustive publication-priority certification and independent mathematical validation have not been performed; older equivalent formulations remain possible.

## References
[1] D. Bhattacharya and A. Patra, “\(q\)-Berezin Range of Operators in Hardy Space,” arXiv:2601.02334 (initially public 2026-01-05), especially Theorem 2.2 and Section 3.4. https://arxiv.org/abs/2601.02334

[2] V. Stojiljković, H. Başaran, and M. Gürdal, “On \(q\)-Berezin number inequalities in reproducing kernel Hilbert space,” *Filomat* 39:28 (2025), 10129–10140, DOI:10.2298/FIL2528129S. https://www.pmf.ni.ac.rs/filomat-content/2025/39-28/39-28-20-28399.pdf

[3] A. Augustine, M. Garayev, and P. Shankar, “Convexity of the Berezin range of finite rank operators,” arXiv:2411.10771 (initially public 2024-11-16). https://arxiv.org/abs/2411.10771

[4] A. Augustine, M. Garayev, and P. Shankar, “Composition operators, convexity of their Berezin range and related questions,” *Complex Analysis and Operator Theory* 17 (2023), article 126; arXiv:2302.12547. https://arxiv.org/abs/2302.12547
