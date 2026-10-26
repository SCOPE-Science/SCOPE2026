# Exact positivity horizon and peak amplification of biharmonic heat on rook graphs

## Finding
Let \(a,b\ge2\) be integers and let \(G=K_a\mathbin{\square}K_b\) be the unweighted rectangular rook graph. Its vertices are pairs \((i,j)\), adjacent when precisely one coordinate differs. Write \(L\) for the unnormalized combinatorial graph Laplacian and \(T(t)=\exp(-tL^2)\) for \(t\ge0\). Define
\[
F_{a,b}(t)=1-e^{-a^2t}-e^{-b^2t}+e^{-(a+b)^2t},\qquad M=(a-1)(b-1).
\]
For every \(t\ge0\), the sharp bounded-data amplification is exactly
\[
\boxed{\ \|T(t)\|_{\ell^\infty\to\ell^\infty}=1+\frac{2M}{ab}\,[-F_{a,b}(t)]_+,\quad [u]_+=\max\{u,0\}.\ }
\]
There is a **unique** positive \(\tau_{a,b}\) satisfying \(F_{a,b}(\tau_{a,b})=0\), and
\[
\boxed{\ T(t)\text{ is entrywise nonnegative }\Longleftrightarrow t=0\text{ or }t\ge\tau_{a,b}.\ }
\]
For \(0<t<\tau_{a,b}\), precisely the entries joining vertices that differ in **both** coordinates are negative; at \(t=\tau_{a,b}\) precisely those entries vanish and all others are positive. For larger positive times every entry is strictly positive. The norm is strictly greater than one exactly on \((0,\tau_{a,b})\).

The norm has a unique strict maximum at \(\theta_{a,b}\in(0,\tau_{a,b})\), the unique positive solution of
\[
a^2e^{-a^2\theta}+b^2e^{-b^2\theta}=(a+b)^2e^{-(a+b)^2\theta}.
\]
It increases strictly from one to this maximum, decreases strictly back to one at the cutoff, and stays one thereafter.

For the **square-board regime** \(a=b=m\ge2\), let \(z_*\in(0,1)\) denote the unique root of \(z^3+z^2+z-1=0\), and set \(u_*=-\log z_*\approx0.609377863436\). Then
\[
\boxed{\ \tau_{m,m}=\frac{u_*}{m^2},\quad
\theta_{m,m}=\frac{\log2}{3m^2},\quad
\max_{t\ge0}\|T(t)\|_{\infty\to\infty}
=1+2\left(1-\frac1m\right)^2\left(3\,2^{-4/3}-1\right).\ }
\]
In contrast, for each fixed integer \(a\ge2\), as \(b\to\infty\) through integers,
\[
\boxed{\ b^2\tau_{a,b}=\log(2b/a)+O_a(\log b/b),\qquad
b^2\theta_{a,b}=1+O_a(b^{-1}),\qquad
\max_{t\ge0}\|T(t)\|_{\infty\to\infty}
=1+\frac{4(a-1)}{eb}+O_a(b^{-2}).\ }
\]
Thus the thin-board regime has a **logarithmically delayed** positivity horizon in units of the inverse largest squared eigenvalue, even while the peak amplification decays to one.

## Assumptions and scope
All edges have conductance one, the Laplacian is \(L=D-A\) on \(\mathbb R^{ab}\) (or its complexification), and the norm is the usual maximum-coordinate operator norm. Time \(t\) is nonnegative. The result concerns the **squared-Laplacian heat operator**, not ordinary heat \(\exp(-tL)\), not a graph bi-Laplacian with alternative boundary conditions, and not graphs with arbitrary weights. The Cartesian product is symmetric in \(a,b\). Every asymptotic error \(O_a(\cdot)\) allows its constant to depend on the fixed \(a\) but not on \(b\).

## Proof
**1. Exact four-level functional calculus.** Write \(U_a=J_a/a\), \(V_a=I_a-U_a\), and similarly \(U_b,V_b\). Since the complete-graph Laplacian is \(aV_a\), the rook Laplacian is
\[
L=aV_a\otimes I_b+bI_a\otimes V_b.
\]
The four mutually orthogonal, sum-to-identity projections \(U_a\otimes U_b\), \(V_a\otimes U_b\), \(U_a\otimes V_b\), and \(V_a\otimes V_b\) have Laplacian eigenvalues \(0,a,b,a+b\). This remains valid when \(a=b\) (two levels then coincide). Consequently, with \(x=e^{-a^2t}\), \(y=e^{-b^2t}\), and \(z=e^{-(a+b)^2t}\),
\[
T(t)=U_a\otimes U_b+xV_a\otimes U_b+yU_a\otimes V_b+zV_a\otimes V_b.
\]
For an input and output vertex, the four possible equality patterns in the two coordinates yield these kernel entries, each with denominator \(ab\):
\[
\begin{array}{c|c}
\text{Both coordinates equal}&1+(a-1)x+(b-1)y+(a-1)(b-1)z\\
\text{First differs, second equal}&1-x+(b-1)(y-z)\\
\text{First equal, second differs}&1-y+(a-1)(x-z)\\
\text{Both differ}&1-x-y+z=F_{a,b}(t).
\end{array}
\]
For \(t>0\), \(0<z<x,y<1\), so the first three types are **strictly positive**. The fourth type is negative for sufficiently small positive time because \(F_{a,b}(0)=0\) and \(F'_{a,b}(0)=-2ab<0\). As \(t\to\infty\), \(F_{a,b}(t)\to1\).

**2. Exactly one positive crossing.** Rewrite
\[
F_{a,b}(t)=(1-e^{-a^2t})-e^{-b^2t}(1-e^{-(a^2+2ab)t}).
\]
For \(t>0\), its sign equals that of \(H(t)-1\), where
\[
H(t)=e^{b^2t}\frac{1-e^{-a^2t}}{1-e^{-(a^2+2ab)t}}.
\]
The function \(u\mapsto u/(e^{ut}-1)\) is strictly decreasing for fixed \(t>0\); differentiating gives numerator \(e^{ut}-1-ut e^{ut}<0\). Hence
\[
\frac{H'(t)}{H(t)}=b^2+\frac{a^2}{e^{a^2t}-1}
-\frac{a^2+2ab}{e^{(a^2+2ab)t}-1}>0.
\]
Moreover \(H(0+)=a/(a+2b)<1\), while \(H(t)\to\infty\). Therefore \(H=1\), equivalently \(F=0\), has exactly one positive solution; \(F\) is negative before and positive after. The four-entry table proves the entire positivity classification, including the equality case at the cutoff.

**3. Exact maximum norm and temporal peak.** Every row of \(T(t)\) sums to one because \(L\mathbf1=0\). Each row has exactly \(M=(a-1)(b-1)\) entries of the fourth type and no other potentially negative entries. For any real matrix whose rows sum to one, the absolute row sum is one plus twice the total negative mass in that row; the operator maximum norm is the maximum absolute row sum. The transitive graph makes all rows equivalent, giving the displayed sharp norm for all \(t\).

Differentiation gives
\[
F'_{a,b}(t)=a^2e^{-a^2t}+b^2e^{-b^2t}-(a+b)^2e^{-(a+b)^2t}.
\]
Multiplication by \(e^{(a+b)^2t}\) turns its sign into that of
\[
a^2e^{((a+b)^2-a^2)t}+b^2e^{((a+b)^2-b^2)t}-(a+b)^2,
\]
a strictly increasing function, initially \(-2ab\) and tending to infinity. Thus \(F\) has exactly one strict minimum at a positive time \(\theta_{a,b}\); because \(F(0)=0\), this minimum precedes the unique positive zero. The claimed norm monotonicity follows.

**4. Square-board constants.** If \(a=b=m\), set \(v=e^{-m^2t}\). The fourth kernel numerator is \(1-2v+v^4=(v-1)(v^3+v^2+v-1)\). The cubic is strictly increasing on \((0,1)\), with a unique zero \(z_*\), giving \(\tau_{m,m}=(-\log z_*)/m^2\). The peak equation becomes \(2e^{-m^2\theta}=4e^{-4m^2\theta}\), so \(m^2\theta=\log2/3\). At the peak, \(-F=3\,2^{-4/3}-1\); substitution into the norm formula completes the exact evaluation.

**5. Thin-board asymptotics.** Fix \(a\ge2\), let \(\delta=a/b\), and rescale \(y=b^2t\). The equation \(H(t)=1\) becomes
\[
1=e^y\frac{1-e^{-\delta^2y}}{1-e^{-(2\delta+\delta^2)y}}.
\]
At \(y=\log(2/\delta)+v\) with any fixed \(v\in\mathbb R\), the right side is \(e^v(1+O_a(\delta\log(1/\delta)))\). Monotonicity of \(H\) traps the unique solution in a fixed-width window around \(\log(2/\delta)\). Uniform expansion throughout that window yields
\[
1=e^y\frac{\delta}{2}\bigl(1+O_a(\delta\log(1/\delta))\bigr),
\]
and then \(y=\log(2/\delta)+O_a(\delta\log(1/\delta))\), proving the cutoff expansion.

The peak equation, divided by \(b^2\), is
\[
\delta^2e^{-\delta^2y}+e^{-y}-(1+\delta)^2e^{-(1+\delta)^2y}=0.
\]
Uniformly for \(y\) in a compact neighborhood of one, its left side is \(2\delta e^{-y}(y-1)+O_a(\delta^2)\). The already-proved unique peak and opposite signs at \(y=1\pm\varepsilon\) show \(y\to1\), and the same equation gives \(y=1+O_a(\delta)\). In this region
\[
-F_{a,b}(y/b^2)=\frac{2a}{b}\,ye^{-y}+O_a(b^{-2})
=\frac{2a}{eb}+O_a(b^{-2})
\]
at the peak. Multiplying by \(2(a-1)(b-1)/(ab)\) yields the claimed peak-norm expansion. No numerical extrapolation is used in these asymptotic arguments.

## Verification
The accompanying `verify_rook_biharmonic.py` reconstructs explicit Cartesian-product graph Laplacians and their matrix exponentials independently of the four-entry formula. It checks the four types of entries, constant row sums, exact norm formula, uniqueness sign regime at test points, square-board constants, and thin-board asymptotic consistency. Dependencies are Python with NumPy and SciPy; run `python verify_rook_biharmonic.py`. The script ran successfully with 6,465 assertions in the preparation of this note. The finite tests support the **analytical** proof; they do not establish the infinite-dimensional parameter ranges on their own.

## Relationship to prior work
Daners, Glück and Kennedy [1,2] establish the eventual-positivity and matrix-semigroup framework, including examples involving fourth-order operators; their inspected finite-dimensional theorems concern spectral characterizations, not the exact rectangular rook-graph kernel or its sharp times and maximum norms. The published three-spectral-value barrier [3] guarantees a final positivity ray for self-adjoint generators with up to three eigenvalues; when \(a\ne b\), the rook-graph generator here has **four** spectral levels, so [3] does not imply the no-gap conclusion. Even when \(a=b\), [3] does not provide the numerical cutoff, peak norm, or thin-board asymptotics. The rook-graph identity \(G=K_a\square K_b=L(K_{a,b})\) is standard [4].

Related exact squared-Laplacian heat calculations for complete multipartite graphs and for Boolean cubes cover different graph families, except for the common four-cycle \(K_2\square K_2\cong K_{2,2}\). The present theorem is not inferred from a similarity of graph names: it uses a distinct tensor-product eigenprojection decomposition and yields new formulas for all rectangular parameters. The proof claims originality of this **combined, exact family classification and asymptotics**, not of eventual positivity or spectral diagonalization generally.

## Limitations
No claim of a complete historical priority search or independent verification is made; equivalent formulas may occur under line graphs of complete bipartite graphs, Cartesian-product diffusion, or association schemes. The graph is finite, unweighted, undirected, and has exactly two complete-graph factors. Other operator functions and general products of three or more factors are outside scope. The norm measures coordinatewise bounded input error, not a Sobolev or Hilbert-space norm. The 6,465 checker assertions cover finite instances only. The result has had self-review; an independent audit has not been performed.

## References
[1] D. Daners, J. Glück, J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, first publicly posted 2015-11-17, arXiv:1511.05294, https://arxiv.org/abs/1511.05294 .

[2] D. Daners, J. Glück, J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, 2015, arXiv:1511.09020, https://arxiv.org/abs/1511.09020 .

[3] *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups*, published mathematical record, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-three-spectral-value-barrier-for-gaps-in-positivity-times-of-s--da21753d4271 .

[4] E. W. Weisstein, *Rook Graph*, MathWorld, https://mathworld.wolfram.com/RookGraph.html .
