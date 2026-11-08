# A characteristic-three Cremona jump for the chordal cubic

## Finding
Let \(k\) be an algebraically closed field with \(\operatorname{char}(k)=0\) or odd prime characteristic. Define the Hankel determinant
\[
F=\det\begin{pmatrix}x_0&x_1&x_2\\x_1&x_2&x_3\\x_2&x_3&x_4\end{pmatrix}
=x_0x_2x_4+2x_1x_2x_3-x_0x_3^2-x_1^2x_4-x_2^3.
\]
Its polar rational map \(\nabla F:\mathbb P^4\dashrightarrow\mathbb P^4\), defined by its five first partial derivatives, is dominant. The generic field degree is exactly
\[
[\,k(\mathbb P^4):\nabla F^*k(\mathbb P^4)\,]=
\begin{cases}1,&\operatorname{char}(k)=3,\\2,&\operatorname{char}(k)\neq3.\end{cases}
\]
Both maps are generically separable. In characteristic three, the polar map is a quadratic Cremona transformation. Its projective base scheme is the **disjoint reduced union** of the rational normal quartic
\[
C=\{[s^4:s^3t:s^2t^2:st^3:t^4]:[s:t]\in\mathbb P^1\}
\]
and the isolated reduced point \(P=[0:0:1:0:0]\). The point \(P\) does **not** lie on the cubic \(F=0\), so the base of its polar map is strictly larger than the singular locus of that cubic. For characteristic different from three and two, the set-theoretic base is precisely \(C\).

## Assumptions and scope
All degrees are geometric function-field degrees over an algebraically closed field of characteristic zero or odd positive characteristic; characteristic two is excluded. We work with the specified coordinates on projective four-space. The scheme assertion is the saturated projective base ideal, not the unsaturated homogeneous ideal. An assertion about reducedness outside characteristic three is not needed.

## Proof
**1. The catalecticant and the Klein quadric.** Form the \(2\times4\) Hankel matrix
\[
M=\begin{pmatrix}x_0&x_1&x_2&x_3\\x_1&x_2&x_3&x_4\end{pmatrix},
\]
with columns numbered \(0,1,2,3\). Denote its minors by \(p_{ij}\) for \(0\le i<j\le3\). Explicitly,
\[
\begin{aligned}
p_{01}&=x_0x_2-x_1^2,&p_{02}&=x_0x_3-x_1x_2,\\
p_{03}&=x_0x_4-x_1x_3,&p_{12}&=x_1x_3-x_2^2,\\
p_{13}&=x_1x_4-x_2x_3,&p_{23}&=x_2x_4-x_3^2.
\end{aligned}
\]
They satisfy the Pluecker equation
\[
p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0.
\]
The resulting rational map \(\Phi:\mathbb P^4\dashrightarrow Q\subset\mathbb P^5\) has target the smooth Klein quadric \(Q\simeq\operatorname{Gr}(2,4)\). Its base scheme set is the rank-one locus of \(M\), which is the rational normal quartic \(C\).

**2. The Pluecker map is birational.** A generic row two-plane \(W\subset k^4\) has a basis \(a,b\). For \(W\) to arise from a Hankel matrix, we must choose rows \(u=\alpha a+\beta b\), \(v=\gamma a+\delta b\) and impose the three overlap equations \(u_{j+1}=v_j\) for \(j=0,1,2\). These are three homogeneous linear equations in four unknown coefficients \(\alpha,\beta,\gamma,\delta\). They have generic rank three: at the Hankel point \([1:0:0:1:0]\), the rows are \(a=(1,0,0,1)\), \(b=(0,0,1,0)\), and the equations become \(\gamma=\beta=0\) and \(\alpha=\delta\). Thus an open subset of \(Q\) has a unique compatible rank-two Hankel matrix up to common scalar. This construction is rational in \(W\), so \(\Phi\) is birational onto \(Q\) in every characteristic.

**3. The gradient is a projection with a movable center.** Direct differentiation gives
\[
(\partial_0F,\partial_1F,\partial_2F,\partial_3F,\partial_4F)
=(p_{23},-2p_{13},p_{03}+3p_{12},-2p_{02},p_{01}).
\]
Because \(2\) is invertible, this is the composition of \(\Phi\) with projection of \(Q\) from the point
\[
c=[0:0:-3:1:0:0]
\]
in Pluecker coordinate order \([p_{01}:p_{02}:p_{03}:p_{12}:p_{13}:p_{23}]\). Substitution into the Klein equation gives \(q(c)=-3\). Hence \(c\in Q\) if and only if the characteristic equals three. If \(c\notin Q\), a general line through \(c\) meets \(Q\) at two distinct points: the finite map of generic degree two is separable in odd characteristic. If \(c\in Q\), a general line meets \(Q\) at \(c\) and precisely one other point, giving a birational projection. Composing with the birational map \(\Phi\) gives the asserted degree dichotomy and dominance.

**4. The characteristic-three base scheme.** In characteristic three the gradient ideal equals
\[
J=(p_{01},p_{02},p_{03},p_{13},p_{23})
\]
(up to invertible scalar factors). Its base lies wherever the minors map is undefined, or where their Pluecker point equals \(c\). The former is \(C\). For the latter, \(p_{01}=p_{02}=p_{03}=p_{13}=p_{23}=0\) forces exactly one additional projective point, \(P=[0:0:1:0:0]\).

For scheme-theoretic reducedness, on the chart \(x_0\ne0\), the equations \(p_{01}=p_{02}=p_{03}=0\) eliminate successively \(x_2,x_3,x_4\) as \(x_1^2/x_0,x_1^3/x_0^2,x_1^4/x_0^3\), and the other minors vanish automatically. This is a reduced chart of \(C\). The \(x_4\ne0\) chart is symmetric. On \(x_2=1\), the equations \(p_{01}=p_{23}=0\) eliminate \(x_0=x_1^2\) and \(x_4=x_3^2\); the remaining ideal is
\[
(x_1(x_1x_3-1),\;x_3(x_1x_3-1),\;x_1x_3(x_1x_3-1))
=(x_1,x_3)\cap(x_1x_3-1).
\]
The two factors are comaximal, respectively the reduced point \(P\) and the reduced affine chart of \(C\). No point of the base has \(x_0=x_2=x_4=0\), since the gradients there include \(-x_1^2\) and \(-x_3^2\). These charts therefore prove the global projective base scheme is reduced, with precisely the two disjoint components. Finally \(F(P)=-1\ne0\). For any odd characteristic other than three, the projection center lies outside \(Q\), hence the only base points are those of \(\Phi\), namely \(C\).

## Verification
The included Python program `verify_hankel_polar.py` performs exhaustive finite-field checks in characteristics three, five, and seven. For every projective point of \(\mathbb P^4(\mathbb F_p)\), it checks the six Pluecker minors, their quadratic relation, all five gradient identities, and the exact claimed base-point set. The total projective point counts are \(121,781,2801\), the corresponding base-point counts are \(5,6,8\), and the rational-normal-quartic counts are \(4,6,8\). This is a finite corroboration, not a proof over algebraically closed fields; the preceding arguments prove the infinite statement.

## Relationship to prior work
Mostafazadehfard and Simis, *Homaloidal determinants*, arXiv:1407.8089 (first submitted July 30, 2014), treat this precise \(3\times3\) Hankel determinant in Section 3.4.1, Proposition 3.20, establishing **nonhomaloidality in characteristic zero** and analyzing the gradient ideal. Their Introduction explicitly assumes characteristic zero, and the inspected passage does not state the characteristic-three birational jump or extra off-cubic base point. The present comparison identifies the precise missing characteristic and explains the degree change through a Pluecker projection whose center enters the Klein quadric. General facts about secant varieties, Grassmannians, and quadric projections are not claimed as new.

## Limitations
No statement is made in characteristic two. The inverse Cremona map and the full unsaturated graded primary decomposition in characteristic three are not determined here. Although relevant literature and indexed results were checked, specialized or later treatments might imply this characteristic-three result; historical priority is provisional.

## References
1. Maral Mostafazadehfard and Aron Simis, *Homaloidal determinants*, arXiv:1407.8089, first publicly submitted 2014-07-30; particularly Section 3.4.1, Proposition 3.20 and Introduction. https://arxiv.org/abs/1407.8089
2. Classical Pluecker description of \(\operatorname{Gr}(2,4)\) and the Klein quadric (standard linear-algebraic identity, proved explicitly above).
