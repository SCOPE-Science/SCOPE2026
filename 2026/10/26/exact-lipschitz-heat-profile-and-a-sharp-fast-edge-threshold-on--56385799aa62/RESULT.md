# Exact Lipschitz heat profile and a sharp fast-edge threshold on the four-cycle

## Finding

Equip the four-cycle \(0-1-2-3-0\) with its **fixed unit-edge graph-distance metric**, independently of the jump conductances. Give the edge \(\{0,1\}\) conductance \(w>0\), and give the other three edges conductance \(1\). The continuous-time generator is the negative unnormalized weighted graph Laplacian \(-L_w\), and \(H_{w,t}=\exp(-tL_w)\).

Define
\[
\delta=\sqrt{(w-1)^2+1},\qquad \beta(t)=\frac{e^{-(w+2)t}\sinh(\delta t)}{\delta}.
\]
For every \(w>0\) and \(t\ge0\), the **exact** operator norm on the Lipschitz space modulo constants is
\[
\boxed{\|H_{w,t}\|_{\mathrm{Lip}\to\mathrm{Lip}}=
\begin{cases}
e^{-(w+2)t}\bigl(\cosh(\delta t)+(2-w)\sinh(\delta t)/\delta\bigr),&0<w\le1,\\
e^{-2t}+(w-1)\beta(t),&w\ge1.
\end{cases}}
\]
The two branches agree at \(w=1\), where the norm is \(e^{-2t}\).

Consequently, **all-time Lipschitz contractivity** holds exactly for \(0<w\le3\). The optimal exponent in an inequality \(\|H_{w,t}\|\le e^{-\kappa t}\) valid for every \(t\ge0\) is
\[
\boxed{\kappa(w)=\min\{2w,3-w\}.}
\]
The complete family obeys a **sharp nonattained envelope**
\[
\boxed{\sup_{w>0}\sup_{t\ge0}\|H_{w,t}\|_{\mathrm{Lip}\to\mathrm{Lip}}=\frac32.}
\]
At every fixed positive time,
\[
\lim_{w\to\infty}\|H_{w,t}\|=e^{-2t}+\frac12e^{-3t}.
\]
In particular, the limit of the norm as \(t\downarrow0\) equals \(1\) for each fixed \(w\), while sending \(w\to\infty\) first and then \(t\downarrow0\) gives \(3/2\).

## Assumptions and scope

The vertex set is \(\{0,1,2,3\}\), with undirected edges \(01,12,23,30\). Conductances are \(w,1,1,1\), respectively, and the graph metric assigns **unit length to every edge**, even the edge of conductance \(w\). Thus the distance metric is not a resistance metric and does not vary with \(w\). There are no vertex weights, killing terms, self-loops, other edges, or normalizations by weighted degree.

For real-valued functions define \(\|f\|_{\mathrm{Lip}}=\max_{ij\in E}|f(i)-f(j)|\); constants are factored out. The operator norm is taken on this real three-dimensional quotient, and the assertions quantify over all positive real \(w\) and all nonnegative real times \(t\). All matrix exponentials use the standard combinatorial Laplacian sign convention.

## Proof

**1. Exact block diagonalization.** Write every vertex function uniquely in coordinates \(p,q,x,y\) by
\[
f=(p+x,\ p-x,\ q+y,\ q-y),\qquad z=p-q.
\]
A direct substitution into \(\partial_t f=-L_wf\) gives
\[
\partial_t z=-2z,\qquad
\partial_t\begin{pmatrix}x\\y\end{pmatrix}
=-B_w\begin{pmatrix}x\\y\end{pmatrix},\qquad
B_w=\begin{pmatrix}2w+1&1\\1&3\end{pmatrix}.
\]
Writing \(u=e^{-2t}\), \(\alpha=e^{-(w+2)t}\cosh(\delta t)\), and \(\beta=e^{-(w+2)t}\sinh(\delta t)/\delta\), the odd-coordinate heat matrix is
\[
S_t=e^{-tB_w}=\begin{pmatrix}a&b\\b&c\end{pmatrix}
=\begin{pmatrix}\alpha-(w-1)\beta&-\beta\\-\beta&\alpha+(w-1)\beta\end{pmatrix}.
\]
Thus \(z'=uz\), \(x'=ax+by\), and \(y'=bx+cy\).

**2. The exact Lipschitz unit ball.** The four edge increments of \(f\), in the order \(01,12,23,30\), are
\[
2x,\quad z-x-y,\quad 2y,\quad-z-x-y.
\]
Consequently \(\|f\|_{\mathrm{Lip}}\le1\) is exactly
\[
|x|\le\frac12,\quad |y|\le\frac12,\quad |z|+|x+y|\le1.
\]
Set \(s=x+y\), \(r=x-y\). Then \(|s|+|r|\le1\); for the two edges next to the exceptional edge the heat-gradient maximum equals
\[
\max_{|s|+|r|\le1}\left[u(1-|s|)
+\left|\frac{a+2b+c}{2}s+\frac{a-c}{2}r\right|\right]
=\max\left\{\frac{|a+2b+c|}{2},\ u+\frac{|a-c|}{2}\right\}.
\]
The extrema occur at admissible boundary points \((s,r)=(\pm1,0)\) and \((0,\pm1)\) with an appropriate extremal \(z\); this calculation proves both inequalities. The first and opposite edges separately have exact amplifications \(a-b\) and \(c-b\): maximize \(2|ax+by|\) or \(2|bx+cy|\) at \((x,y)=(\pm1/2,\mp1/2)\), with \(z=0\).

Conjugating \(B_w\) by \(\operatorname{diag}(1,-1)\) gives a symmetric two-state *killed* Markov generator with off-diagonal rate \(1\) and killing rates \(2w\) and \(2\). Hence its exponential is nonnegative and substochastic. It follows that \(a,c\ge0\), \(b\le0\), and \(a-b,c-b\le1\). Positivity of \(S_t\) as a symmetric matrix also gives \(a+2b+c\ge0\), so
\[
\frac{|a+2b+c|}{2}\le\max\{a-b,c-b\}.
\]
The exact total norm is therefore
\[
\max\{\alpha+(2-w)\beta,\ \alpha+w\beta,\ u+|w-1|\beta\}
=\max\{\alpha+(1+|w-1|)\beta,\ u+|w-1|\beta\}.
\]

**3. The one-branch identity.** Put \(\lambda_\pm=w+2\pm\delta\). Then
\[
\alpha+\beta=\frac{1+1/\delta}{2}e^{-\lambda_-t}
+\frac{1-1/\delta}{2}e^{-\lambda_+t}.
\]
For \(w\ge1\), both rates satisfy \(\lambda_\pm\ge2\), proving \(\alpha+\beta\le u\). For \(0<w\le1\), differentiation of
\[
e^{2t}(\alpha+\beta)=e^{-wt}
\left(\cosh(\delta t)+\frac1\delta\sinh(\delta t)\right)
\]
yields the nonnegative quantity
\[
e^{-wt}\left((1-w)\cosh(\delta t)+\frac{(1-w)(2-w)}{\delta}\sinh(\delta t)\right).
\]
It starts at \(1\), so \(\alpha+\beta\ge u\) in this range. Comparing the two candidates in the preceding maximum gives precisely the stated piecewise formula.

**4. Contractivity and its sharp threshold.** If \(0<w\le1\), the norm equals the row sum \(a-b\le1\) of a killed Markov matrix. For \(w\ge1\), both eigenvalues \(\lambda_\pm\) are at least \(2\), so the convolution identity
\[
\beta(t)=\int_0^t e^{-\lambda_-(t-s)}e^{-\lambda_+s}\,ds
\le t e^{-2t}
\]
gives, whenever \(w\le3\),
\[
\|H_{w,t}\|=e^{-2t}+(w-1)\beta(t)
\le e^{-2t}(1+2t)\le1.
\]
If \(w>3\), the exact second branch has derivative \(w-3>0\) at \(t=0\); hence it exceeds \(1\) for all sufficiently small positive times. This proves the if-and-only-if threshold.

**5. Optimal exponential rate.** The right derivative at zero of the exact norm is \(-2w\) for \(0<w\le1\) and \(w-3\) for \(w\ge1\). Thus it equals \(-\kappa(w)\), where \(\kappa(w)=\min\{2w,3-w\}\). Submultiplicativity of induced norms and \(\|H_{w,t/n}\|=1-\kappa(w)t/n+O(n^{-2})\) show
\[
\|H_{w,t}\|\le\lim_{n\to\infty}\|H_{w,t/n}\|^n
=e^{-\kappa(w)t}.
\]
No larger exponent works because the derivative at \(0\) would contradict it.

**6. Sharp universal envelope and boundary layer.** In the second branch, \((w-1)\beta=|a-c|/2\); since \(0\le a,c\le1\), its value is at most \(1/2\). As the first branch is always at most \(1\), the norm never exceeds \(3/2\). For every fixed finite \(w\) and \(t>0\), \(u<1\) and the substochastic diagonal entries satisfy \(|a-c|<1\), so equality is impossible; at \(t=0\) the norm is \(1\).

For fixed \(t>0\), as \(w\to\infty\), the two rates satisfy \(\lambda_-\to3\), \(\lambda_+\to\infty\), and \((w-1)/\delta\to1\). The second branch therefore converges to \(e^{-2t}+e^{-3t}/2\). More strongly, take \(t=w^{-1/2}\). Then \(t\to0\), \(\lambda_+t\to\infty\), and \(\lambda_-t\to0\), so the exact norm converges to \(3/2\). This proves sharpness and nonattainment without extrapolating from finite computations.

## Verification

The accompanying `verify.py` checks the exact coordinate generator identities symbolically and independently evaluates the full four-by-four heat matrix using a matrix exponential. For 140 specified weight/time pairs it compares the formula against direct maximization over all integral graph-distance-Lipschitz potentials modulo constants; the polytope is integral because its constraints are signed vertex-edge incidences. The script is a finite diagnostic, not a replacement for the all-parameter proof above. It also checks representative threshold and fast-edge behavior. Its Python dependencies are `numpy`, `scipy`, and `sympy`.

## Relationship to prior work

Ollivier's transport-contraction formulation and Veysseire's continuous-time coarse-Ricci theorem explain why infinitesimal Wasserstein curvature controls an exponential Lipschitz bound. Lin–Lu–Yau compute normalized-walk curvature for an unweighted four-cycle; their normalization differs from the unnormalized one-edge-conductance generator studied here. Those statements do not give this parameter-dependent exact heat norm, a precise edge-rate \(3\) contractivity transition, or the singular sharp \(3/2\) transient envelope. A general diameter-based heat-amplification bound also does not determine the present two-branch exact profile. The result relies on direct spectral reduction and exact optimization of the Lipschitz unit ball, not on a claim that the general curvature framework is new.

## Limitations

All assertions concern a single exceptional **jump conductance** on a fixed unit-metric four-cycle. They do not cover varying edge **metric lengths**, degree-normalized generators, directed processes, more than one exceptional rate, or larger cycles. The sharp constant \(3/2\) is a supremum across conductances and times, not an attained norm at a fixed finite parameter. An equivalent exact formula in unindexed prior literature remains possible. Independent validation has not been performed.

## References

1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886, first submitted 2007-01-30, https://arxiv.org/abs/math/0701886.
2. Laurent Veysseire, *Coarse Ricci curvature for continuous-time Markov processes*, arXiv:1202.0420, first submitted 2012-02-02, https://arxiv.org/abs/1202.0420. See Definitions 3–6 and Theorem 9.
3. Yong Lin, Linyuan Lu, and Shing-Tung Yau, *Ricci curvature of graphs*, *Tohoku Mathematical Journal* **63** (2011), 605–627, https://doi.org/10.2748/tmj/1325886283; compare the normalized walk and Example 2.
