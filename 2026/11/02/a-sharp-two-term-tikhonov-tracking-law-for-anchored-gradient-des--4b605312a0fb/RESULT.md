# A sharp two-term Tikhonov tracking law for anchored gradient descent on invertible monotone linear problems

## Finding

For the fixed-anchor forward iteration below, its entire leading asymptotic residual is determined by the anchor, independently of the spectrum or nonnormality of the invertible monotone operator. More precisely, with \(s=k+\gamma\),

\[
u_k=\frac{\gamma L}{\sqrt{s}}M^{-1}b
-\frac{\gamma(\gamma-\tfrac12)L^2}{s}M^{-2}b
+\begin{cases}O(s^{-3/2}\log s),&\gamma=2,\\O(s^{-3/2}),&\gamma>2.\end{cases}
\]

In particular,

\[
\lim_{k\to\infty}\sqrt{k+\gamma}\,Mu_k=\gamma Lb,
\qquad
\lim_{k\to\infty}\sqrt{k+\gamma}\,\|Mu_k\|_2=\gamma L\|b\|_2.
\]

Define the instantaneous Tikhonov zero \(v_k\) by

\[
\bigl(M+\gamma Ls^{-1/2}I\bigr)v_k=\gamma Ls^{-1/2}b.
\]

Then the discrete trajectory has the universal **nonzero second-order tracking lag**

\[
\boxed{\lim_{k\to\infty}s(u_k-v_k)=\frac{\gamma L^2}{2}M^{-2}b.}
\]

The limit is nonzero for every nonzero anchor \(b\). The sharp residual holds in particular for symmetric positive-definite quadratics and for invertible skew-symmetric bilinear saddle operators; the assertion does not require strong monotonicity or a normal matrix.

## Assumptions and scope

Let \(d\ge1\) and \(M\in\mathbb R^{d\times d}\) be invertible and monotone in the Euclidean inner product:

\[\langle Mx,x\rangle\ge0\quad\text{for all }x\in\mathbb R^d.\]

Set \(L=\|M\|_2>0\), fix \(\gamma\ge2\) (real) and \(b\in\mathbb R^d\setminus\{0\}\), and initialize \(u_0=b\). For every integer \(k\ge0\) take exactly one forward step

\[
u_{k+1}=u_k-\frac{1}{L\sqrt{k+\gamma}}Mu_k+\frac{\gamma}{k+\gamma}(b-u_k).
\]

This is the unconstrained linear specialization of the anchored gradient-descent schedule studied in Cai--Zheng and Surina et al.; \(u_k\) is an exact-arithmetic iteration, not a continuous-time limit. All vector limits and big-O statements are in the Euclidean norm, with constants allowed to depend on the fixed \(M,L,\gamma,b\), never on \(k\). The unique zero of \(Mu=0\) is the origin.

## Proof

**1. Algebraic asymptotic coefficients.** Write \(s=k+\gamma\), \(B_s=(1-\gamma/s)I-s^{-1/2}M/L\). The iteration is \(u_{k+1}=B_su_k+\gamma b/s\). Define

\[
C=\gamma LM^{-1}b,\quad
D=-\gamma(\gamma-\tfrac12)L^2M^{-2}b,\quad
E=\gamma(\gamma-\tfrac12)(\gamma-1)L^3M^{-3}b.
\]

They obey the exact identities

\[
MC/L=\gamma b,\qquad MD/L=-(\gamma-\tfrac12)C,\qquad ME/L=(1-\gamma)D.
\]

Let \(w_k=Cs^{-1/2}+Ds^{-1}+Es^{-3/2}\). The ordinary binomial expansions, with remainders uniform for \(s\ge\gamma\ge2\), yield

\[
\begin{aligned}
w_{k+1}&=Cs^{-1/2}+Ds^{-1}+(E-\tfrac12C)s^{-3/2}-Ds^{-2}+O(s^{-5/2}),\\
B_sw_k+\gamma b/s
&=Cs^{-1/2}+Ds^{-1}
+(E-\gamma C-MD/L)s^{-3/2}
+(-\gamma D-ME/L)s^{-2}+O(s^{-5/2}).
\end{aligned}
\]

The three coefficient identities make the displayed coefficients identical, so the local defect satisfies

\[\|B_sw_k+\gamma b/s-w_{k+1}\|_2\le K s^{-5/2}\]

for a finite constant \(K\). In the scalar case and every finite dimension these identities are exact; no diagonalization or eigenvector conditioning estimate is used.

**2. Uniform transport bound for errors.** Let \(q_s=\sqrt{(1-\gamma/s)^2+1/s}\). Monotonicity of \(M\), \(1-\gamma/s\ge0\) and \(\|M\|_2=L\) imply for each \(x\)

\[
\|B_sx\|_2^2=(1-\gamma/s)^2\|x\|_2^2
-2(1-\gamma/s)\langle x,Mx\rangle/(L\sqrt s)
+\|Mx\|_2^2/(L^2s)
\le q_s^2\|x\|_2^2.
\]

For fixed \(\gamma\ge2\),

\[q_s=1-(\gamma-\tfrac12)/s+O(s^{-2}).\]

Summing logarithms gives a finite \(C_\gamma\) such that every pair of integers \(k>j\ge0\) satisfies

\[
\|B_{k+\gamma-1}\cdots B_{j+\gamma}\|_2\le
C_\gamma\left(\frac{j+\gamma}{k+\gamma}\right)^{\gamma-1/2}.
\]

To see that this bound also includes small \(s\), enlarge \(C_\gamma\) over finitely many initial factors; all \(q_s\) are positive because \(1/s>0\).

**3. Global asymptotic error.** Let \(e_k=u_k-w_k\). Iteration of the defect recursion and the preceding product estimate yield

\[
\|e_k\|_2\le C(k+\gamma)^{-(\gamma-1/2)}
\left(1+\sum_{j=0}^{k-1}(j+\gamma)^{\gamma-3}\right).
\]

For \(\gamma=2\), the sum is \(O(\log(k+\gamma))\); for \(\gamma>2\), it is \(O((k+\gamma)^{\gamma-2})\). Thus \(e_k=O(s^{-3/2}\log s)\) at \(\gamma=2\) and \(O(s^{-3/2})\) otherwise. Absorb \(Es^{-3/2}\) into the remainder to obtain the asserted two-term expansion. Multiplying by \(M\sqrt s\) and using \(MC=\gamma Lb\) proves the sharp residual vector limit; \(b\ne0\) makes its norm limit strictly positive.

**4. Moving equilibrium and the lag.** Because \(M\) is invertible and \(s\to\infty\), a Neumann expansion of the resolvent gives

\[
\begin{aligned}
v_k&=\frac{\gamma L}{\sqrt s}M^{-1}b
-\frac{\gamma^2 L^2}{s}M^{-2}b+O(s^{-3/2}),\\
u_k-v_k&=\frac{\gamma L^2}{2s}M^{-2}b+o(s^{-1}).
\end{aligned}
\]

Every inverse in this expansion exists for every positive \(s\), not merely asymptotically: monotonicity and invertibility imply that \(M+\lambda I\) has trivial kernel for all \(\lambda>0\). Since \(M^{-2}\) is invertible, the lag coefficient is nonzero when \(b\ne0\). This proves the theorem.

**5. Strongly convex witness.** For a symmetric positive-definite \(M\), let \(f(u)=\tfrac12u^\mathsf{T}Mu\). Direct substitution of the leading expansion gives

\[
\lim_{k\to\infty}(k+\gamma)(f(u_k)-f(0))=\frac{\gamma^2L^2}{2}b^\mathsf{T}M^{-1}b>0.
\]

Thus an exact \(\Theta(k^{-1/2})\) gradient-residual tail and \(\Theta(k^{-1})\) objective-error tail occur even on positive-definite quadratics for this *fixed anchored schedule*. This is not a limitation of unanchored gradient descent on that same quadratic.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It checks the three cancellation identities and the second-order lag coefficient exactly with rational arithmetic on identity, unequal-curvature diagonal, skew rotation and normal accretive matrices, for multiple anchors and \(\gamma\) values. It also executes long finite-step trajectories and checks the trend of residual and lag differences against their predicted limits. Run `python3 verify.py` after extraction. The analytical product and summation estimates above, rather than sampled trajectories, certify the infinite-time assertion.

## Relationship to prior work

Cai and Zheng [1] specify this anchored-step schedule and prove a general last-iterate \(O(k^{-1/2})\) tangent-residual upper bound for proximal monotone inclusions. Surina et al. [2] obtain the corresponding squared-gradient upper bound for the unconstrained saddle setting. Neither bound determines a nonzero leading vector, a second-order iterate coefficient or the offset from a moving Tikhonov zero. Chen [3, Section 4.2] explicitly explains anchored forward steps as operator-side Tikhonov regularization and provides a residual upper bound for the \(\gamma=4\) schedule; the regularized-target viewpoint is prior art, not claimed here. The present finite-dimensional linear theorem adds a two-term **discrete** expansion for all invertible monotone matrices, yielding a sharp residual and a signed nonvanishing tracking lag. The expansion is not implied by an upper norm rate or by the instantaneous resolvent identity alone.

## Limitations

This is an exact-arithmetic linear result with invertible \(M\) and a fixed nonzero anchor. It does not cover nonlinear monotone maps, singular maps with nonunique zeros, infinite-dimensional unbounded operators, stochastic or floating-point iterations, arbitrary step schedules or constrained proximal corrections. The asymptotic constants may deteriorate as \(M\) approaches singularity. No optimality assertion is made among other algorithms or schedules. Its historical novelty beyond the primary sources remains subject to further independent literature review; the mathematical theorem itself requires no numerical evidence.

## References

[1] Y. Cai and W. Zheng, *Last-Iterate Convergence of Anchored Gradient Descent*, arXiv:2604.12235v1, first posted 2026-04-14. https://arxiv.org/html/2604.12235v1

[2] A. Surina et al., *An Improved Last-Iterate Convergence Rate for Anchored Gradient Descent Ascent*, arXiv:2604.03782v1, first posted 2026-04-04. https://arxiv.org/html/2604.03782

[3] Z. Chen, *A Unifying View of Anchoring via Operator-Side Tikhonov Regularization*, arXiv:2605.30905v1, first posted 2026-05-29. https://arxiv.org/html/2605.30905v1
