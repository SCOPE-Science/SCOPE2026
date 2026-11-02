# A unique sharp cooperation threshold for coexistence in a prey-refuge predator map

## Finding
For the Jang--Yousef discrete predator--prey map with a sufficiently large refuge and subcritical predator invasion, the *entire* set of strictly positive fixed points is governed by a unique, nondegenerate cooperation threshold. Below it there is no coexistence fixed point; at it there is one double fixed-point intersection; above it there are exactly two. The two predator-density branches are monotone in opposite directions. The threshold is given by the unique positive zero of an explicit strictly convex auxiliary function; it needs no numerical continuation or assumed branch completeness.

## Assumptions and scope
For every \(\lambda>1\), \(\beta>0\) and \(0<\gamma<1\), consider, for \(c\ge0\), the map
\[
X_{n+1}=\frac{\lambda X_n}{1+X_n}\left(1-\gamma+\gamma e^{-Y_n(1+cY_n)}\right),\qquad
Y_{n+1}=\beta\gamma X_n\left(1-e^{-Y_n(1+cY_n)}\right).
\]
A *positive fixed point* means both \(X>0\) and \(Y>0\), with no dynamical-stability assertion. Impose the further **nonempty parameter-regime assumptions**
\[
0<\gamma\le\frac{\lambda-1}{2\lambda},\qquad R:=\beta\gamma(\lambda-1)<1.
\]
Put \(A=\lambda(1-\gamma)-1\), \(B=\lambda\gamma\), \(k=\beta\gamma\), so \(A\ge B>0\), and define for every \(t>0\)
\[
F(t)=k(1-e^{-t})(A+Be^{-t}),\qquad
C(t)=\frac{t-F(t)}{F(t)^2},\qquad
K(t)=\frac{F(t)}{F'(t)}+F(t)-2t.
\]
Then there exists exactly one \(t_*>0\) with \(K(t_*)=0\). The number \(c_*:=C(t_*)>0\) has the following **sharp classification**, for all real \(c\ge0\):
\[
\begin{array}{c|c}
0\le c<c_* &0\text{ positive fixed points}\\
c=c_* &1\text{ (one nondegenerate double intersection)}\\
c>c_* &2\text{ distinct positive fixed points}.
\end{array}
\]
Each fixed point is uniquely reconstructed from a solution \(t>0\) to \(C(t)=c\) by
\[
Y=F(t),\qquad X=A+Be^{-t}.
\]
For \(c>c_*\), the low-\(Y\) branch strictly decreases and the high-\(Y\) branch strictly increases as \(c\) increases. At large cooperation,
\[
Y_{-}(c)\sim \frac{1-R}{Rc},\quad X_{-}(c)\to\lambda-1;
\qquad Y_{+}(c)\to kA,\quad X_{+}(c)\to A.
\]
For the parameters \((\lambda,\beta,\gamma)=(3,4,1/10)\), the threshold evaluates numerically to \(c_*\approx 2.31932345373819\), with fold coordinates \(X_*\approx 1.874900072882\), \(Y_*\approx 0.312733149962\).

## Proof
**Step 1 (complete equilibrium parameterization).** Set \(t=Y(1+cY)\) at any positive equilibrium. The prey equation divided by \(X>0\) yields \(X=A+Be^{-t}>0\). The predator equation then gives \(Y=k(A+Be^{-t})(1-e^{-t})=F(t)>0\). The identity \(t=Y+cY^2\) is equivalent to \(c=C(t)\). Conversely, if \(t>0\) and \(C(t)=c\ge0\), the displayed \(X,Y\) satisfy both map equations; no equilibria are omitted.

**Step 2 (strict positivity and endpoint limits).** Writing \(a=k(A-B)\ge0\), \(b=kB>0\),
\[
F(t)=a(1-e^{-t})+b(1-e^{-2t}),\qquad
f(t):=F'(t)=ae^{-t}+2be^{-2t}>0.
\]
Since \(f\) strictly decreases and \(f(0)=a+2b=R<1\), we have \(0<F(t)<Rt<t\). Therefore \(C(t)>0\) for every \(t>0\), and \(C(t)\to+\infty\) at both endpoints: as \(t\downarrow0\), \(F(t)=Rt+O(t^2)\) and \(C(t)\sim(1-R)/(R^2t)\); as \(t\to\infty\), \(F(t)\to a+b=kA>0\) and \(C(t)\sim t/(kA)^2\).

**Step 3 (strict convexity of the critical-point function).** Differentiate to obtain
\[
C'(t)=\frac{f(t)}{F(t)^2}K(t).
\]
Let \(p(t)=2be^{-2t}/f(t)\), so \(0<p(t)\le1\). Directly, \(-f'/f=1+p\) and \(f''/f=1+3p\). For \(Z=F/f\),
\[
Z'=1+(1+p)Z,\qquad
Z''=(1+p)+Z(1+p+2p^2).
\]
Thus the crucial *global convexity identity* is
\[
K''(t)=(1+p(t))(1-f(t))
+\frac{F(t)}{f(t)}(1+p(t)+2p(t)^2)>0,
\]
using \(f(t)\le R<1\). The continuous extension to \(t=0\) has \(K(0)=0\), \(K'(0)=R-1<0\). As \(t\to\infty\), \(F(t)/f(t)\to+\infty\) exponentially while \(2t-F(t)\) grows at most linearly, hence \(K(t)\to+\infty\). Strict convexity forces one and only one positive zero \(t_*\), at which \(K'(t_*)>0\). Therefore \(C\) decreases strictly until \(t_*\), increases strictly afterwards, and \(C''(t_*)=f(t_*)K'(t_*)/F(t_*)^2>0\). This is a *nondegenerate fold of the fixed-point equations*; no global dynamical stability is implied.

**Step 4 (count, monotonic branches and limits).** The endpoint divergence and unique strict minimum of \(C\) yield respectively zero, one, and two positive solutions of \(C(t)=c\) as stated. For the two branches \(t_-(c)<t_*<t_+(c)\), the inverse function theorem and the signs of \(C'\) give \(dt_-/dc<0<dt_+/dc\). As \(F'>0\), the same holds for predator densities. The prey densities move oppositely because \(A+Be^{-t}\) decreases with \(t\). The small-root expansion \(C(t)\sim(1-R)/(R^2t)\) gives \(t_-(c)\sim(1-R)/(R^2c)\), so \(Y_-(c)=F(t_- )\sim(1-R)/(Rc)\). The upper root must diverge since \(C\) is strictly increasing and unbounded there; hence its limits follow from \(F(t)\to kA\) and \(e^{-t}\to0\). This finishes the proof.

## Verification
The bundled standard-library program `verify_refuge_fold.py` computes the unique critical point by bracketing \(K\), checks the two reconstructed positive equilibria against **both original map equations** for several cooperation values and multiple admissible parameter triples, and checks numerical branch ordering. It reproduces the displayed threshold and fold state for \((3,4,1/10)\). Exact symbolic differentiation independently checks the displayed \(K''\) identity. These finite computations support the result; the preceding proof, not a grid search, establishes completeness for the entire stated parameter region.

## Relationship to prior work
Jang and Yousef (2023), Theorem 2.4, give a sufficient nonexistence condition and an upper bound of two coexistence equilibria in the subinvasion regime. Their Figure 3 reports a numerically estimated, expressly unproved switch for \((\lambda,\beta,\gamma)=(3,4,1/10)\). This finding proves *necessary and sufficient* existence inequalities and a unique fold **for every parameter triple in the specified strong-refuge region**, including strict branch monotonicity and large-cooperation limits. Chow, Jang and Wang (2018), Theorems 3.1--3.2, treat a *no-refuge* map and identify a fold as predator conversion varies, not the refuge-dependent cooperation threshold here. A no-refuge conclusion is not a stronger claim about all refuge values.

## Limitations
The theorem deliberately restricts the refuge fraction and assumes strictly subunit predator invasion \(R<1\); equality \(R=1\), larger accessible-prey fractions, and other response functions are not classified. It classifies *fixed points*, not survival from arbitrary starting states, basin sizes, attracting-periodic or chaotic dynamics, nor the stability of either positive branch. The numerical value of the threshold is approximate; the defining minimization and uniqueness are exact. Analogous formulas in related models may exist outside the inspected literature. Independent validation has not been conducted.

## References
1. S. R.-J. Jang and A. M. Yousef, *Effects of prey refuge and predator cooperation on a predator--prey system*, Journal of Biological Dynamics 17 (2023), article 2242372, DOI: 10.1080/17513758.2023.2242372; first published online 2023-08-03. Equation (2), Theorem 2.4 and Figure 3.
2. Y. Chow, S. R.-J. Jang and H.-M. Wang, *Cooperative hunting in a discrete predator-prey system*, arXiv:1808.00182 (2018), Theorems 3.1--3.2, no-refuge model.
