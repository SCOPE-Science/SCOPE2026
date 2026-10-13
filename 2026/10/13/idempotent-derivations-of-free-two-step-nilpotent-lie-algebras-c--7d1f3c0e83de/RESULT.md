# Idempotent derivations of free two-step nilpotent Lie algebras: conjugacy and exact rank spectra

## Finding
For every field \(K\) and integer \(n\ge3\), let \(V=K^n\) and let
\[
L_n(K)=V\oplus\bigwedge^2 V,\qquad [v+z,w+t]=v\wedge w.
\]
Here the second summand is central. A *composition-idempotent derivation* is a \(K\)-linear map \(D:L_n(K)\to L_n(K)\) satisfying the Leibniz identity for this Lie bracket and \(D^2=D\). It need not be a Lie-algebra endomorphism.

Every such derivation is conjugate under \(\operatorname{Aut}(L_n(K))\) to exactly one of the operators \(D_r\) induced by a rank-\(r\) projection \(P_r:V\to V\):
\[
D_r(v)=P_rv,\qquad
D_r(u\wedge v)=P_ru\wedge v+u\wedge P_rv.
\]
The permitted ranks and conjugacy-class counts are
\[
\begin{array}{c|c|c}
\operatorname{char}K & r & \#\operatorname{Aut}(L_n(K))\text{-orbits}\\ \hline
\ne2 & 0,1 & 2\\
2 & 0,1,\ldots,n & n+1.
\end{array}
\]
Different \(r\) always yield different classes, including when the full-operator ranks coincide.

Over any finite field \(\mathbb F_q\), let \(\mathcal R_{n,q}(T)=\sum_{D^2=D,\,D\in\operatorname{Der}(L_n(\mathbb F_q))}T^{\operatorname{rank}(D)}\), counting *labeled* derivations. If \(q\) is odd, then
\[
\boxed{\mathcal R_{n,q}(T)=1+{n\brack1}_q\,q^{(n-1)+\binom{n-1}{2}+(n-1)^2}T^n.}
\]
If \(q\) is even, then
\[
\boxed{\mathcal R_{n,q}(T)=
\sum_{r=0}^{n}{n\brack r}_q\,
q^{r(n-r)+r\left[\binom r2+\binom{n-r}{2}+(n-r)^2\right]}
T^{r(n-r+1)}.}
\]
The Gaussian coefficient \({n\brack r}_q\) counts the \(r\)-spaces of \(\mathbb F_q^n\). Terms with the same exponent of \(T\) are added. In particular,
\[
\mathcal R_{3,2}(T)=1+1408T^3+448T^4,
\qquad\mathcal R_{3,3}(T)=1+28431T^3.
\]
Thus the characteristic-two case has idempotent derivations of rank \(4\) on a six-dimensional free two-step Lie algebra, while in every odd characteristic the only possible ranks are \(0\) and \(n\).

## Assumptions and scope
The Lie algebra is the free nilpotent Lie algebra of class at most two on \(n\) generators (with alternating bracket also in characteristic \(2\)); its dimension is \(n+\binom n2\). The chosen presentation fixes a generator complement \(V\), which is useful for counting labeled operators; the conjugacy result is intrinsic. No algebraic-closedness or restriction on finite-field extension degree is assumed. Derivation is ordinary, not restricted, twisted, or super. The theorem concerns linear maps with \(D\circ D=D\), not elements \(x\) with \(\operatorname{ad}(x)^2=\operatorname{ad}(x)\) and not algebra retractions.

## Proof
**1. Exhaustive derivation parametrization.** Since \([L_n,L_n]=\bigwedge^2V\), every derivation preserves the second summand. Its restriction to generators has a unique expression
\[
D(v)=Av+f(v),\qquad
A\in\operatorname{End}_K(V),\quad
f\in\operatorname{Hom}_K(V,\bigwedge^2 V).
\]
The derivation identity on \([u,v]=u\wedge v\) forces
\[
D(u\wedge v)=L_A(u\wedge v),\qquad
L_A(u\wedge v)=Au\wedge v+u\wedge Av.
\]
Conversely any such pair \((A,f)\) defines a derivation: the required identity holds on generator pairs, and all brackets involving the central summand vanish. Uniqueness follows because generators and their brackets span the algebra. In block form relative to the fixed splitting,
\[
D_{A,f}=\begin{pmatrix}A&0\\ f&L_A\end{pmatrix}.
\]

**2. Idempotence and the characteristic boundary.** Squaring this block matrix shows that \(D_{A,f}^2=D_{A,f}\) is equivalent to
\[
A^2=A,\qquad L_A^2=L_A,\qquad fA+L_Af=f.
\]
Since \(A^2=A\), its image \(U\) and kernel \(W\) split \(V=U\oplus W\). Write \(r=\dim U\), \(s=\dim W=n-r\). There is a direct decomposition
\[
\bigwedge^2V=(\bigwedge^2U)\oplus(U\wedge W)\oplus(\bigwedge^2W),
\]
on which \(L_A\) acts by the respective scalars \(2,1,0\). Thus \(L_A^2=L_A\) holds precisely when \(2\cdot\bigwedge^2U=0\); equivalently, either \(\operatorname{char}K=2\) or \(r\le1\). This is the source of the characteristic jump.

The remaining equation is equivalent to the following *necessary and sufficient* restrictions:
\[
f(U)\subseteq\ker L_A,\qquad f(W)\subseteq U\wedge W.
\]
When the characteristic is different from \(2\), the permitted \(r\) are \(0,1\) and \(\ker L_A=\bigwedge^2W\). In characteristic \(2\), every \(r\) is permitted and \(\ker L_A=(\bigwedge^2U)\oplus(\bigwedge^2W)\). Conversely, every such \((A,f)\) obeys all three idempotence equations.

**3. All maps with a fixed generator projection are conjugate.** For \(h\in\operatorname{Hom}(V,\bigwedge^2V)\), the shear
\[
\Psi_h(v+z)=v+h(v)+z
\]
is a Lie-algebra automorphism with inverse \(\Psi_{-h}\): adding central terms does not change any bracket. Direct multiplication gives
\[
\Psi_hD_{A,0}\Psi_h^{-1}=D_{A,\,hA-L_Ah}.
\]
For every admissible \(f\), choose \(h(u)=f(u)\) for \(u\in U\) and \(h(w)=-f(w)\) for \(w\in W\). The restrictions from Step 2 then give \(hA-L_Ah=f\). Hence every idempotent derivation is shear-conjugate to \(D_{A,0}\). Every \(g\in\operatorname{GL}(V)\) extends to the Lie automorphism \(v+z\mapsto gv+(\bigwedge^2g)z\). All rank-\(r\) projections are \(\operatorname{GL}(V)\)-conjugate, proving the listed normal forms. An automorphism preserves the derived ideal, and thus the rank of the map induced by \(D\) on \(L_n/[L_n,L_n]\cong V\); this rank equals \(r\). Therefore distinct \(r\) are never conjugate.

**4. Full-operator ranks.** By the conjugacy in Step 3, \(\operatorname{rank}D=\operatorname{rank}A+\operatorname{rank}L_A\). For \(r\le1\) in characteristic different from \(2\), this is \(0\) when \(r=0\) and \(1+s=n\) when \(r=1\). In characteristic \(2\), \(L_A\) has eigenvalue \(1\) precisely on \(U\wedge W\), hence
\[
\operatorname{rank}D=r+rs=r(n-r+1).
\]
The rank need not distinguish conjugacy classes in characteristic \(2\).

**5. Labeled finite-field multiplicities.** The number of rank-\(r\) projections \(A\) on \(\mathbb F_q^n\) is \({n\brack r}_q q^{rs}\): choose the image \(U\), then choose one of the \(q^{rs}\) complementary kernels \(W\). For each such \(A\), the restrictions in Step 2 yield an affine-linear family of choices of \(f\). In odd characteristic, only \(r=1\) is nontrivial. The allowed maps have
\[
\dim\operatorname{Hom}(U,\bigwedge^2W)+
\dim\operatorname{Hom}(W,U\wedge W)
=\binom{s}{2}+s^2
\]
free coefficients. Multiplication by the projection count gives the odd formula, with the single zero derivation accounting for the constant term.

In characteristic \(2\), the respective free dimensions are
\[
\dim\operatorname{Hom}(U,(\bigwedge^2U)\oplus(\bigwedge^2W))
=r\left(\binom r2+\binom s2\right),\qquad
\dim\operatorname{Hom}(W,U\wedge W)=rs^2.
\]
Multiplying by \({n\brack r}_q q^{rs}\) and using Step 4 gives the even formula. Every admissible \((A,f)\) is counted exactly once by the unique generator-component map \(A\), so this is a complete count and not an isomorphism-class count.

## Verification
The self-contained `checker.py` uses no third-party dependencies. Run `python3 checker.py`. It enumerates every coefficient matrix \(A\) and every possible central generator image \(f\) for \(n=2,3\) over \(\mathbb F_2\), builds the full linear derivation matrices from their bracket identity, squares them directly, and computes their ranks by Gaussian elimination. It also enumerates the \(n=2\) cases over \(\mathbb F_3\) and \(\mathbb F_5\) by an independent prime-field matrix implementation. The observed rank-count dictionaries are
\[
\begin{aligned}
(n,q)=(2,2):&\quad\{0:1,2:16\};\\
(3,2):&\quad\{0:1,3:1408,4:448\};\\
(2,3):&\quad\{0:1,2:36\};\\
(2,5):&\quad\{0:1,2:150\}.
\end{aligned}
\]
All agree with the proved formulas, and the program prints `VERIFY_OK`. Additional integer formula checks cover \(3\le n\le5\) and \(q=2,4,8\). The exhaustive tests concern only these small finite fields; the arbitrary-field theorem follows from the preceding proof rather than extrapolation from computation.

## Relationship to prior work
Benito and Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients* (arXiv:1911.01897v2, §2, Proposition 1 and Corollary 1), establish the starting parametrization of all derivations and automorphisms. The present theorem imposes composition-idempotence and identifies the characteristic-sensitive conjugacy classes and full finite-field rank multiplicities; those conclusions are not among the inspected primary statements. La Rosa and Mancini, *Derivations of two-step nilpotent algebras* (arXiv:2301.11058v3, §§2–5), investigate derivation Lie algebras and almost-inner derivations, particularly for Heisenberg-type Leibniz algebras, rather than this finite-field composition-idempotent family.

Eick and Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields* (arXiv:2205.03155v2, §2.1 and §4.1), study characteristic-two gradings arising from idempotent **inner** derivations \(\operatorname{ad}(x)\) of simple Lie algebras. For any class-two nilpotent Lie algebra, \(\operatorname{ad}(x)^2=0\); hence their inner-idempotent condition yields only zero here and cannot account for the noninner operators counted in this finding. Hakavuori, Kivioja, Moisala, and Tripaldi, *Gradings for nilpotent Lie algebras* (arXiv:2011.06871v3, §§1–3), develop torsion-free grading methods in characteristic zero, without these characteristic-two and finite-field multiplicities.

## Limitations
The theorem classifies composition-idempotent *ordinary* derivations for the free class-two Lie algebra, not arbitrary class-two quotients, non-free brackets, restricted Lie operators, higher nilpotency classes, or algebra retractions. No claim is made that the rank enumerator determines isomorphism classes of arbitrary gradings. Its new content is the specific conjugacy/rank census; earlier general derivation and grading frameworks remain foundational. Bibliographic equivalence under different terminology cannot be ruled out by searches alone. The computational cases cannot independently certify the infinite family.

## References
1. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v2 (first public 2019-11-05), https://arxiv.org/html/1911.01897v2.
2. G. La Rosa and M. Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058v3 (first public 2023-01-26), https://arxiv.org/html/2301.11058v3.
3. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155v2 (first public 2022-05-06), https://arxiv.org/html/2205.03155v2.
4. E. Hakavuori, V. Kivioja, T. Moisala, and F. Tripaldi, *Gradings for nilpotent Lie algebras*, arXiv:2011.06871v3 (first public 2020-11-13), https://arxiv.org/html/2011.06871v3.
