# Sharp projective symmetry jump in the extremal simultaneous-Galois quartic pairs

## Finding
For each \(a\in\{-1,i,-i\}\), let \(D_a\subset\mathbf P^2_{\mathbb C}\) be the reduced degree-eight union of the two smooth quartics
\[
C_1:\ XY^3+X^4+Z^4=0,\qquad
C_a:\ X((a-1)X+aY)^3+X^4+Z^4=0.
\]
These are the three canonical configurations of two smooth quartics with two simultaneous inner Galois points in Ikeda--Takahashi, Theorem 5.1. For every \(a\), the full singularity basket of \(D_a\) consists of exactly two \(A_7\) singularities and eight \(A_1\) nodes. Its full **embedded projective** stabilizer is
\[
\operatorname{Stab}_{\mathrm{PGL}_3(\mathbb C)}(D_a)\cong
\begin{cases}
C_8,&a=i\text{ or }a=-i,\\
G_{16},&a=-1,
\end{cases}
\]
where \(G_{16}\) is the nonabelian group of order \(16\) defined by
\[
G_{16}=\langle R,S,T\mid R^2=S^2=T^4=1,\ [R,T]=[S,T]=1,\ RS=T^2SR\rangle.
\]
The characteristic-zero assertion is about projective transformations of the **reducible plane embedding**; it makes no claim about automorphisms of its disconnected normalization. The stabilizer of the \(a=-1\) union is strictly larger than those of the other two canonical unions, despite identical local singularity types.

## Assumptions and scope
Work over \(\mathbb C\) in coordinates \([X:Y:Z]\). The parameter \(i\) denotes a fixed square root of \(-1\). In the binary coordinates \(u=X\), \(v=X+Y\), \(z=Z\), define
\[
g_b(u,v)=buv(b^2v^2-3buv+3u^2),\qquad F_b=g_b+z^4.
\]
Then \(C_b=V(F_b)\) for \(b=1,a\). Smoothness and non-equality of these quartics follow from the originating paper; the following explicit algebra also verifies that their intersection is reduced away from the two contact points.

## Proof
**1. The singularity basket.** The two smooth components meet where \(F_1=F_a=0\), equivalently where \(F_1=g_1-g_a=0\). The binary difference factors as
\[
g_1-g_a=uv\{(1-a^3)v^2-3(1-a^2)uv+3(1-a)u^2\}.
\]
The braces define two distinct lines through \([u:v]=[0:0]\), because their binary discriminant is \(-3(a-1)^4\ne0\). Neither coincides with \(u=0\) or \(v=0\) because \(a\ne1\), \(a^3\ne1\). The coordinate lines \(u=0\) and \(v=0\) meet \(z=0\) at \(P_0=[0:1:0]\) and \(P_1=[-1:1:0]\), respectively. On either special line the quartic equation reduces to \(z^4\), so each component meets that line with multiplicity four at the indicated smooth point. The binary difference vanishes to first order transversely to each line: its residual factor takes the values \(1-a^3\) at \(u=0\) and \(3(1-a)\) at \(v=0\). Consequently, the two components meet with intersection multiplicity exactly four at each \(P_0,P_1\), giving smooth two-branch tangencies analytically equivalent to \(A_7\).

On either of the other two lines, the scalar coefficient \(g_1(u,v)\) is nonzero. Indeed, the residual quadratic \(Q_a(t)=(1-a^3)t^2-3(1-a^2)t+3(1-a)\), in \(t=v/u\), has no common root with the non-axis factor \(t^2-3t+3\) of \(g_1(1,t)\), since
\[
\operatorname{Res}_t(Q_a(t),t^2-3t+3)=9a^2(a-1)^2(a^2-a+1)\ne0.
\]
Each residual line therefore meets \(F_1=0\) in four distinct points with \(z\ne0\); the two residual lines meet each other only at \([0:0:1]\), which is not on the quartics. These eight component-intersection points are transverse ordinary nodes. There are no further singularities because both components are smooth and all sixteen Bézout intersection multiplicities have been accounted for: \(4+4+8=16\). The arithmetic-genus check is \(p_a(D_a)=21=3+3+(4+4+8)-2+1\).

**2. Every projective symmetry fixes the contact line.** The only \(A_7\) points are \(P_0,P_1\), distinguished intrinsically from the eight nodes. A projective automorphism of \(D_a\) therefore permutes these two points and preserves their join \(z=0\). Consequently, in \((u,v,z)\) it has a representative
\[
(u,v,z)\longmapsto(A(u,v)+cz,\lambda z),\quad A\in\mathrm{GL}_2(\mathbb C),\ c\in\mathbb C^2,\ \lambda\ne0.
\]
The degree-eight equation is \(H=(g_1+z^4)(g_a+z^4)\), whose \(z\)-linear coefficient vanishes. For the transformed equation to be a nonzero multiple of \(H\), its coefficient of \(z\) must vanish; it is the directional derivative of \((g_1g_a)(A(u,v))\) in direction \(c\). Were this identically zero with \(c\ne0\), in characteristic zero the nonzero binary homogeneous octic \(g_1g_a\) would be a power of one linear form (after a change of variables). This contradicts its distinct roots \(u=0\) and \(v=0\). Thus \(c=0\).

Because the components are distinct irreducible quartics, their equations must be permuted with scalar multipliers. The coefficient of \(z^4\) in both equations is one, so these multipliers must both be \(\lambda^4\): for some permutation \(\sigma\) of \(\{1,a\}\),
\[
g_b(A(u,v))=\lambda^4g_{\sigma(b)}(u,v)\quad(b=1,a).
\]
The projective transformation also permutes \(P_0,P_1\), hence its binary matrix is diagonal or antidiagonal after a common rescaling. It remains to solve two elementary coefficient-comparison cases; we give all of the solutions, including their fourth-root lifts.

**3. Exhaustion of projective symmetries.** Up to a common scalar on \(u,v\), a diagonal binary map is \((u,v)\mapsto(cu,v)\). Comparing the three nonzero coefficients of \(g_b\) shows that \(g_b(cu,v)=m g_{b'}(u,v)\) holds exactly when \(c=b/b'\), with \(m=(b/b')^4\). Preserving both components gives only the identity; interchanging them additionally gives \(c=-1\) only when \(a=-1\). Each case has common multiplier one and therefore four possible values of \(\lambda\).

An antidiagonal binary map is \((u,v)\mapsto(cv,u)\). Matching coefficients now gives \(c=bb'/3\), \(m=b^4/9\). Since \(a^4=1\), all matched multipliers equal \(1/9\). Exchanging the two components is possible, and forces \(c=a/3\), for all three parameters. Preserving both is possible exactly when \(a=-1\), in which case \(c=1/3\). Every case again gives four possible \(\lambda\), now with \(\lambda^4=1/9\). There are therefore precisely \(8\) projective symmetries for \(a=\pm i\) and \(16\) for \(a=-1\); no matrices have been missed by the contact-point and coefficient-exhaustion argument.

For \(a=\pm i\), the representative
\[
U_a:(u,v,z)\mapsto\left(\frac a3v,u,\frac z{\sqrt3}\right)
\]
interchanges the components, has \(U_a^2\) equal projectively to \(z\mapsto a^{-1}z\), and hence has order eight (because \(a^{-1}\) has order four). It generates the full stabilizer.

For \(a=-1\), let
\[
R:(u,v,z)\mapsto(-u,v,z),\quad
S:(u,v,z)\mapsto\left(\frac v3,u,\frac z{\sqrt3}\right),\quad
T:(u,v,z)\mapsto(u,v,iz).
\]
These are projective transformations preserving the union, satisfy \(R^2=S^2=T^4=1\), centrality of \(T\), and \(RS=T^2SR\) in \(\mathrm{PGL}_3\). They generate four binary cases with four lifts each, hence the full order-sixteen stabilizer. As \(RS\ne SR\), the group is nonabelian. This proves the assertion.

## Verification
Run `python verify.py` using Python 3 and SymPy. The program checks the exact binary-form identities, the two resultants, component interchange/preservation, the fourth-root lifts and the displayed projective group relations for all three parameters. Exact symbolic identities provide reproducible cross-checks; the exhaustiveness is proved by the line preservation and coefficient comparison above, not by finite group enumeration.

## Relationship to prior work
Ikeda and Takahashi, Theorem 5.1 of arXiv:2305.05985v1, prove that their three explicit pairs exhaust the two-inner-simultaneous-Galois-point case and supply the smooth component equations; those are prior input. Their paper does not state the projective automorphism groups of the **unions** or the complete scheme-intersection singularity basket derived here. Fukasawa--Miura--Takahashi (arXiv:2211.16033) treat quasi-Galois points and automorphisms of irreducible smooth quartics; the full stabilizer of the reducible two-component union is a different object. The familiar genus and Bézout identities are classical tools rather than independent contributions.

## Limitations
The theorem is over \(\mathbb C\), for these three canonical **embedded** unions only. It does not classify abstract automorphisms of the components or their normalization; nor does it decide whether the two order-eight presentations are projectively equivalent. An independent mathematical audit has not been performed. Earlier unpublished or unindexed calculations could contain equivalent conclusions.

## References
- A. Ikeda and T. Takahashi, *Simultaneous Galois points for a reducible plane curve consisting of nonsingular components*, arXiv:2305.05985v1 (first public 2023-05-10), Theorem 5.1 and Section 5. https://arxiv.org/html/2305.05985v1
- S. Fukasawa, K. Miura and T. Takahashi, *Quasi-Galois points II: Arrangements*, arXiv:2211.16033v1 (2022). https://arxiv.org/abs/2211.16033
