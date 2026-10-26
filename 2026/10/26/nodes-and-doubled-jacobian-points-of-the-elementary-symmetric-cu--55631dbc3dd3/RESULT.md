# Nodes and doubled Jacobian points of the elementary symmetric cubic in characteristic two

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\). For every integer \(n\geq 3\) with \(n\not\equiv 2\pmod 4\), put
\[
 F_n=e_3(x_1,\ldots,x_n)=\sum_{1\leq i<j<\ell\leq n}x_ix_jx_\ell,
 \qquad X_n=V(F_n)\subset\mathbb P_k^{n-1}.
\]
Let \(J_n\subset\mathbb P_k^{n-1}\) be the projective Jacobian scheme defined by all \(n\) first partial derivatives of \(F_n\). By Euler's identity in characteristic \(2\), this is exactly the scheme-theoretic singular locus of \(X_n\).

For every nonempty subset \(S\subset\{1,\ldots,n\}\), write \(P_S=[\mathbf1_S]\), the projective point whose entries are \(1\) on \(S\) and \(0\) elsewhere. Then:

1. The geometric support of \(J_n\) is **exactly** \(\{P_S:|S|\equiv1\pmod4\}\). Each such point is an ordinary quadratic double point of \(X_n\): the projectivized quadratic tangent cone is smooth.
2. If \(n\) is odd, each local ring \(\mathcal O_{J_n,P_S}\) is \(k\). Thus \(J_n\) is reduced.
3. If \(n\equiv0\pmod4\), every \(\mathcal O_{J_n,P_S}\) is isomorphic to \(k[\epsilon]/(\epsilon^2)\). Thus the Jacobian scheme has uniform length-two infinitesimal structure at every node, although every quadratic tangent cone is smooth.

Consequently, with \(N_n=\sum_{j\equiv1\ (4)}\binom nj\) (the sum is over \(1\leq j\leq n\)),
\[
 \#\operatorname{Supp}(J_n)=N_n=2^{n-2}+\tfrac12\operatorname{Im}((1+i)^n),\qquad
 \operatorname{length}(J_n)=
 \begin{cases}N_n,&n\text{ odd},\\2^{n-1},&n\equiv0\pmod4.\end{cases}
\]
For odd \(n\geq3\), equivalently \(N_n=2^{n-2}+(-1)^{\lfloor(n-1)/4\rfloor}2^{(n-3)/2}\); for \(n\equiv0\pmod4\), \(N_n=2^{n-2}\). The first respective values are \(3,4,6,28,64,136,528,1024\) for \(n=3,4,5,7,8,9,11,12\).

## Assumptions and scope

The base field is algebraically closed of characteristic exactly \(2\); all schemes are over \(k\). The cubic is the degree-three *elementary symmetric* polynomial, not an arbitrary symmetric cubic. The result treats every \(n\geq3\) outside \(n\equiv2\pmod4\). In the excluded congruence class, the critical locus instead has dimension \(2\), by Xie's dimension theorem; the finite-length formula does not apply. The singular scheme is defined by the gradient ideal as a projective subscheme, so no claim is made about embedded structures at the vertex of its affine cone.

## Proof

**1. At most two coordinate values.** Write \(D_i=\partial F_n/\partial x_i=e_2(x_1,\ldots,\widehat{x_i},\ldots,x_n)\). In characteristic \(2\), deletion gives
\[
 D_i=e_2(x)+x_i e_1(x)+x_i^2.
\]
Therefore at any geometric common zero of the \(D_i\), all coordinate values are roots of the same monic polynomial \(T^2+e_1(x)T+e_2(x)\). There are at most two distinct values. For distinct indices, subtraction gives the *scheme-theoretic identity*
\[
 D_i+D_j=(x_i+x_j)\sum_{\ell\ne i,j}x_\ell.\tag{1}
\]

**2. Set-theoretic classification.** If the coordinates all have one nonzero value \(a\), then the common derivative is \(\binom{n-1}{2}a^2\), which is zero precisely for \(n\equiv1,2\pmod4\). In the present range this occurs only for \(n\equiv1\pmod4\), yielding \(P_{\{1,\ldots,n\}}\).

Otherwise split the coordinates into \(m\) copies of \(a\) and \(t=n-m\) copies of \(b\), with \(a\ne b\), \(m,t\geq1\). Equation (1) implies
\[
 (m-1)a+(t-1)b=0\quad\text{in }k.\tag{2}
\]
If \(n\) is odd, \(m,t\) have opposite parity; (2) forces the value in the even-sized group to be zero. Let \(u\) be the size of the nonzero group. Then \(u\) is odd and the derivative at a coordinate in that group equals \(\binom{u-1}{2}a^2\). Its vanishing is equivalent to \(u\equiv1\pmod4\). Conversely, if \(u\equiv1\pmod4\), the derivatives at coordinates outside that group equal \(\binom u2a^2=0\) and those inside also vanish.

If \(n\equiv0\pmod4\), the two groups have the same parity. Both even would make (2) read \(a+b=0\), a contradiction. Both are therefore odd. Since \(m+t\equiv0\pmod4\), their residues modulo \(4\) are \((1,3)\) or \((3,1)\). The derivative at an \(a\)-coordinate is
\[
 D_a=\binom{m-1}{2}a^2+(m-1)t\,ab+\binom t2 b^2.
\]
The middle coefficient vanishes in characteristic \(2\). If \((m,t)\equiv(1,3)\pmod4\), then \(D_a=b^2\), forcing \(b=0\); if \((m,t)\equiv(3,1)\), then \(D_a=a^2\), forcing \(a=0\). Again the nonzero support has cardinality \(1\) modulo \(4\), and a direct substitution verifies sufficiency. This proves the complete support description over the algebraic closure, not only over \(\mathbb F_2\).

**3. Local Jacobian algebras.** Fix a singular point \(P_S\) with \(m=|S|\equiv1\pmod4\), and put \(T=\{1,\ldots,n\}\setminus S\), \(t=|T|\). First suppose \(t>0\). In the local ring at \(P_S\), every \(x_i+x_j\) with \(i\in S\), \(j\in T\) is a unit. Equation (1), for all such pairs, gives \(\sum_{\ell\ne i,j}x_\ell=0\) modulo the gradient ideal. Comparing two such equations with the same \(j\) forces \(x_i=x_{i'}\) for \(i,i'\in S\); comparing with the same \(i\) forces \(x_j=x_{j'}\) for \(j,j'\in T\). These linear equalities hold *scheme-theoretically* after localization, not merely on points.

Thus one may set all \(S\)-coordinates equal to \(a\), all \(T\)-coordinates to \(b\), and work on the projective chart \(a=1\), where \(a+b\) remains a unit. If \(n\) is odd, then \(t\) is even, and (1) reduces to \((a+b)b=0\). Hence \(b=0\), and all remaining gradient equations vanish at \(b=0\); the local algebra is \(k\). If \(n\equiv0\pmod4\), then \(t\equiv3\pmod4\). Both types of derivatives on the two-block chart equal \(b^2\), so the local algebra is exactly \(k[b]_{(b)}/(b^2)\simeq k[\epsilon]/(\epsilon^2)\). If \(T=\varnothing\), then \(n=m\equiv1\pmod4\), and the Jacobian matrix computation below has full rank in projective coordinates, giving a reduced local point.

**4. Ordinary quadratic tangent cones.** At \(P_S\), the polar Hessian of the quadratic term of \(F_n\) has off-diagonal entry \(\sum_{\ell\ne i,j}(P_S)_\ell\). It is block diagonal with \(J_m+I_m\) on \(S\) and \(J_t+I_t\) on \(T\), where \(J\) denotes the all-ones matrix and \(I\) the identity (these expressions have zero diagonals in characteristic \(2\)). After choosing a projective chart by fixing one \(S\)-coordinate to \(1\), the first block has order \(m-1\), which is even, and is invertible. If \(n\) is odd, \(t\) is even and the second block is also invertible; the quadratic polar form is nonsingular, so the projectivized tangent quadric is smooth. If \(n\equiv0\pmod4\), then \(t\equiv3\pmod4\), and the polar form has a one-dimensional radical spanned by simultaneous first-order variation of the \(T\)-coordinates. The quadratic term evaluated on that radical is \(m\binom t2=1\in k\), as seen by setting \(S\)-coordinates to \(1\) and \(T\)-coordinates to \(z\) in \(F_n\). Thus the radical point does **not** lie on the tangent quadric; the latter is again smooth. Consequently all these points are ordinary quadratic double points in the tangent-cone sense, despite the length-two Jacobian scheme for \(n\equiv0\pmod4\).

**5. Counting.** Each eligible support \(S\) determines a distinct point. The roots-of-unity filter \(\frac14\sum_{r=0}^{3}i^{-r}(1+i^r)^n\) gives \(N_n=2^{n-2}+\tfrac12\operatorname{Im}((1+i)^n)\). For \(n\equiv0\pmod4\), the imaginary part vanishes and all \(N_n=2^{n-2}\) points have length \(2\). For odd \(n\), all points have length \(1\), giving the claimed degree formulas.

## Verification

The accompanying standalone `verify.py` exhaustively checks projective \(\mathbb F_2\)-points for \(3\leq n\leq12\), including the predicted Hessian ranks, and projective \(\mathbb F_4\)-points for \(n=3,4,5,7,8\). It also tests the characteristic-two parity identities underpinning the local doubling. It prints `VERIFY_OK`. These finite field checks are not used as a substitute for the proof over all algebraically closed characteristic-two fields or for all \(n\).

## Relationship to prior work

Ying Xie, arXiv:2610.00259v1 (first public version 2026-09-24), determines dimensions of derivative and multiplicity loci of elementary symmetric polynomials, classifies *maximal-dimensional* partition components, and calculates generic local multiplicity along coordinate subspaces. For \(d=3\) and \(p=2\), Xie's dimension result gives one-dimensional affine critical loci for \(n\not\equiv2\pmod4\), but the paper explicitly leaves a classification of lower-dimensional components and global reducedness open. Its coordinate-subspace local calculation accounts for the axis case; it does not identify all non-axis points \(P_S\), their complete node count, or their uniform projective Jacobian algebras.

Ian Orzel, arXiv:2509.05009v3, supplies broader order-two zero-locus dimension bounds motivated by complexity, rather than the exact projective cubic singular scheme. Cafure, Matera and Privitelli, arXiv:1109.2265v1, use partition-space constraints and dimension bounds for symmetric hypersurfaces, but not the scheme-theoretic classification for the elementary symmetric cubic in characteristic \(2\). The two-value bound in the proof is consistent with these earlier methods; the all-dimensional support, node and infinitesimal-length classification is the additional geometric assertion.

## Limitations

The theorem excludes \(n\equiv2\pmod4\), where the singular locus is positive-dimensional. It makes no assertion about other degrees, primes, characteristic-zero analogues or the affine vertex. The literature comparison is not a mathematical proof of worldwide novelty; a differently phrased tabulation of this symmetric cubic family could exist. In characteristic \(2\), ordinary quadratic tangent cones and nonreduced Jacobian schemes can coexist, as the theorem illustrates.

## References

1. Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (2026), https://arxiv.org/abs/2610.00259.
2. Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009v3 (2026 revision of a 2025 preprint), https://arxiv.org/abs/2509.05009.
3. Antonio Cafure, Guillermo Matera and Melina Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed-Solomon codes*, arXiv:1109.2265v1 (2011), https://arxiv.org/abs/1109.2265.
