# A one-incidence toggle separates four-cycle and six-cycle dynamics in symmetric designs

## Finding

**Theorem.** Let \(\mathcal D\) be a nontrivial symmetric \(2\)-\((v,k,\lambda)\) design, with \(k\ge3\) odd and \(\lambda\) even. Let \(\mathbb F_q\) be any finite field of characteristic two. Form the bipartite point–block incidence graph on \(2v\) vertices. States in \(\mathbb F_q\) are updated synchronously by the sum of neighbor states, with no self-input. After changing exactly one point–block adjacency, write \(F\) for the new linear update map.

**Insertion of a missing incidence.** The map is invertible and satisfies \(F^6=I\). Its primitive periods are precisely \(1,2,3,6\), and the numbers of **periodic points of exact primitive period** are, respectively,
\[
 P_1=q^{v-2},\quad P_2=q^{2v-4}-q^{v-2},\quad
 P_3=q^v-q^{v-2},\quad
 P_6=q^{2v}-q^{2v-4}-q^v+q^{v-2}.
\]

**Deletion of an existing incidence.** The map satisfies \(F^5=F\) but \(F^3\ne F\), with rank \(2v-2\). Every configuration becomes periodic after at most one update, and this sharp bound is attained. Its exact primitive periods are \(1,2,4\), with periodic-point counts
\[
 P_1=q^{v-2},\quad P_2=q^{2v-4}-q^{v-2},\quad
 P_4=q^{2v-2}-q^{2v-4}.
\]
There are \(q^{2v-2}\) initially periodic configurations and \(q^{2v}-q^{2v-2}\) configurations of first-entry time one. Every periodic point has \(q^2\) one-step predecessors; a primitive \(d\)-cycle has attraction basin of size \(d q^2\). In both cases the number of primitive \(d\)-cycle **orbits** is \(P_d/d\).

Without the toggle, \(F^2=I\). Thus a single incidence change produces sharply different dynamics: deletion creates transient states and genuine four-cycles, whereas insertion preserves reversibility but creates genuine three- and six-cycles.

## Assumptions and scope

A symmetric \(2\)-\((v,k,\lambda)\) design has \(v\) points, \(v\) blocks of size \(k\), each point lying in \(k\) blocks, and every distinct pair of points lying together in exactly \(\lambda\) blocks. Nontriviality and \(k\ge3\) ensure the incidence columns contain at least three nonzero coordinates, so a basis coordinate and any column are linearly independent. There is no assumption that the design has an automorphism, cyclic representation, or a geometric embedding. All sums, ranks and powers are taken over \(\mathbb F_q\); the graph update is the same open-neighborhood, unweighted linear rule before and after toggling one incidence.

## Proof

Let \(B\in\mathbb F_q^{v\times v}\) be the incidence matrix. The design axioms give
\[
 BB^{\mathsf T}=(k-\lambda)I+\lambda J=I
\]
because the field has characteristic two, \(k\) is odd and \(\lambda\) is even. Thus \(B\) is invertible, \(B^{-1}=B^{\mathsf T}\), and also \(B^{\mathsf T}B=I\). The original bipartite adjacency update \(\begin{psmallmatrix}0&B\\B^{\mathsf T}&0\end{psmallmatrix}\) squares to the identity.

Fix the toggled point \(i\) and block \(j\), and let \(u=e_i\), \(a=Be_j\), and \(\sigma=u^{\mathsf T}a=B_{ij}\in\{0,1\}\). Changing one incidence replaces \(B\) by \(B+ue_j^{\mathsf T}\). Conjugate its adjacency map by the change of variables \((p,\ell)\mapsto(p,z)=(p,B\ell)\). Its matrix becomes
\[
 T=\begin{pmatrix}0&U\\V&0\end{pmatrix},\qquad
 U=I+ua^{\mathsf T},\quad V=I+au^{\mathsf T}.
\]
Here \(u^{\mathsf T}u=a^{\mathsf T}a=1\), and \(u,a\) are independent. The latter follows from \(k\ge3\), as \(a\) has exactly \(k\) nonzero coordinates whereas \(u\) has one.

**Case \(\sigma=0\) (insertion).** The orthogonal vectors \(u,a\), both of squared norm one, span a nondegenerate two-dimensional subspace \(H\). Thus \(\mathbb F_q^v=H\oplus H^\perp\). On \(H^\perp\), both \(U,V\) are the identity, hence \(T\) swaps the two copies of that subspace. On \(H\oplus H\), writing the coordinates in the order \((p_u,p_a,z_u,z_a)\), the update matrix is
\[
 T_H=\begin{pmatrix}
 0&0&1&1\\0&0&0&1\\1&0&0&0\\1&1&0&0
 \end{pmatrix}.
\]
The two diagonal blocks of \(T_H^2\) are \(\begin{psmallmatrix}0&1\\1&1\end{psmallmatrix}\) and \(\begin{psmallmatrix}1&1\\1&0\end{psmallmatrix}\), each of exact order three. In particular \(T_H^6=I\), and direct elimination gives
\[
 \dim\ker(T_H-I)=\dim\ker(T_H^2-I)=0,
 \qquad\dim\ker(T_H^3-I)=2.
\]
The complementary swap has fixed subspace of dimension \(v-2\) at odd powers and \(2(v-2)\) at even powers. Hence
\[
 \dim\ker(T-I)=v-2,\quad
 \dim\ker(T^2-I)=2v-4,\quad
 \dim\ker(T^3-I)=v,\quad
 \dim\ker(T^6-I)=2v.
\]
These dimensions imply the displayed exact-period counts by subtracting fixed-point populations of proper divisors. Their strict positivity for \(v\ge4\), \(q\ge2\) proves the listed periods all occur; order six is sharp.

**Case \(\sigma=1\) (deletion).** Now \(U^2=U\) and \(V^2=V\), both of rank \(v-1\). Set \(Q=UV=I+R\), where
\[
 R=ua^{\mathsf T}+au^{\mathsf T}+uu^{\mathsf T}.
\]
Direct multiplication using \(u^{\mathsf T}u=a^{\mathsf T}a=u^{\mathsf T}a=1\) yields \(R^2=aa^{\mathsf T}\), whence
\[
 Q^2=I+aa^{\mathsf T},\qquad Q^2U=U.
\]
Interchanging \(u\) and \(a\) gives the analogous \((VU)^2V=V\), so the off-diagonal block formula for \(T^5\) establishes \(T^5=T\). Furthermore, \(\ker U=\langle u\rangle\), \(\operatorname{im}V=\ker u^{\mathsf T}\), and \(u\notin\operatorname{im}V\), proving \(\operatorname{rank}(UV)=v-1\); similarly \(\operatorname{rank}(VU)=v-1\). Thus \(\operatorname{rank}T=\operatorname{rank}T^2=2v-2\).

Since \(R=u(a+u)^{\mathsf T}+a u^{\mathsf T}\) and the two vectors and two linear forms in this expression are each independent, \(\operatorname{rank}R=2\). Therefore \(\dim\ker(Q-I)=v-2\), and the same holds for \(VU-I\). The equations \(T(p,z)=(p,z)\) reduce to \(Qp=p\) and \(z=Vp\), proving \(\dim\ker(T-I)=v-2\); the two diagonal blocks of \(T^2\) give \(\dim\ker(T^2-I)=2v-4\). Finally, \(T^5=T\) says \(T^4\) is the identity on \(\operatorname{im}T\), which has dimension \(2v-2\). Thus exactly \(q^{2v-2}\) states are periodic, with fixed-point counts at periods one, two and four as displayed. Positivity of \(P_4\) proves \(T^3\ne T\). Equality of the ranks of \(T\) and \(T^2\) shows zero transient time on \(\operatorname{im}T\) and exactly one step for all other states. Every fiber of \(T\) has size \(q^{\dim\ker T}=q^2\). This completes the proof.

## Verification

The companion programs `check_matrix.py` and `check_independent.cpp` independently construct the symmetric \(2\)-\((4,3,2)\) design and the cyclic \(2\)-\((11,5,2)\) biplane using the difference set \(\{1,3,4,5,9\}\) modulo eleven. Both programs check every possible single incidence toggle (16 and 121 choices, respectively), the rank identities and fixed-subspace dimensions. They independently enumerate all 256 binary configurations on the four-point example for one insertion and one deletion, finding precisely the stated period counts and entrance times. The actual command outputs are in `verification_output.txt`. The algebraic argument, not the finite checks, proves the all-design and all-field statement.

Run `python3 check_matrix.py` and `g++ -O2 -std=c++17 -o check_independent check_independent.cpp && ./check_independent`. The C++ executable is generated locally and is not a required input artifact.

## Relationship to prior work

The odd-block/even-intersection condition places the incidence matrix among orthogonal matrices over characteristic two. Brown's exposition of the \(2\)-\((11,5,2)\) biplane supplies a concrete, independently checkable design example. Kaski and Östergård classify biplanes with a different block size; their accessible abstract addresses existence and classification rather than one-incidence XOR dynamics. Ogihara and Uchizawa analyze computational questions for general synchronous XOR networks, a broader methodological setting but not an explicit incidence-toggle orbit census. The stated contribution is the uniform algebraic dichotomy and its exact orbit and basin populations, not the design identities or general methods of linear finite dynamics.

## Limitations

The theorem assumes a symmetric design, odd \(k\), even \(\lambda\), characteristic two and a **single** toggled incidence. It does not assert the same cycle spectrum for odd-intersection designs, simultaneous multiple toggles, nonlinear rules, or positive characteristic other than two. Experimental checks are illustrative and do not establish the infinite-family theorem. An unlocated equivalent result in older design/code or Boolean-network literature remains possible; a relevant biplane-classification paper was accessible only through abstract/bibliography, not full text.

## References

1. E. Brown, “The Fabulous (11,5,2) Biplane,” *Mathematics Magazine* **77** (2004), 87–100. DOI: 10.1080/0025570X.2004.11953234. Full author-posted text: https://personal.math.vt.edu/brown/doc/1152.pdf.
2. P. Kaski and P. R. J. Östergård, “There are exactly five biplanes with k = 11,” *Journal of Combinatorial Designs* **16** (2008), 117–127; first published online February 22, 2007. DOI: 10.1002/jcd.20145.
3. M. Ogihara and K. Uchizawa, “Synchronous Boolean Finite Dynamical Systems on Directed Graphs over XOR Functions,” *Theory of Computing Systems* (2022). DOI: 10.1007/s00224-022-10111-x.
