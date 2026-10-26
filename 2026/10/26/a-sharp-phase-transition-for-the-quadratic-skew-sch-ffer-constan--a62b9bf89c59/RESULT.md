# A sharp phase transition for the quadratic skew Schäffer constant on the affine-regular hexagon

## Finding
Let \(H=(\mathbb R^2,N)\), where \(N(u,v)=\max\{|u|,|v|,|u-v|\}\). Let the quadratic skew Schäffer constant be
\[
\mathcal S_{H,2}(\tau)=\inf_{N(x)=N(y)=1}\left(\frac{N(x+\tau y)^2+N(\tau x-y)^2}{2}\right)^{1/2},\quad \tau\ge0.
\]
Let \(\rho\) be the unique root in \((0,1)\) of \(1-2\rho+\rho^2-\rho^3=0\), approximately \(0.569840290998053\). Then for \(0\le\tau\le1\),
\[
\boxed{\mathcal S_{H,2}(\tau)=
\begin{cases}
(1+\tau^2)\sqrt{1-\tau+\tau^2/2},&0\le\tau\le\rho,\\
\dfrac{(1+\tau^2)(1+\tau)}{\sqrt{2((1+\tau^2)^2+\tau^2)}},&\rho\le\tau\le1.
\end{cases}}
\]
For \(\tau>1\), the exact value is obtained by \(\mathcal S_{H,2}(\tau)=\tau\mathcal S_{H,2}(1/\tau)\). In particular \(\mathcal S_{H,2}(1)=4/\sqrt{10}\), and
\[
\mathcal S_{H,2}(\tau)=1-\frac{\tau}{2}+\frac{9\tau^2}{8}+O(\tau^3)\quad(\tau\downarrow0).
\]
At \(\rho\), the minimizer leaves the kink locus of the first transformed norm; a single defining facet becomes active for that norm.

## Assumptions and scope
The underlying normed space is real and two-dimensional; the unit ball has consecutive vertices \((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)\). The exponent of the *outer* power mean is exactly two. No identification with a Lebesgue or Hilbert space is assumed. All infima are attained by compactness. Put \(F_\tau(x,y)=[N(x+\tau y)^2+N(\tau x-y)^2]/2\), so that the theorem computes \(\min F_\tau\).

## Proof
**1. Reduction to two relative edge types.** The linear maps \(R(u,v)=(u-v,u)\) and \(Q(u,v)=(u,u-v)\) are isometries for \(N\). Rotation \(R\) cycles the six vertices and edges, while \(Q\) fixes the edge \(E_0\) between \((1,0)\) and \((1,1)\) and sends relative edge index \(j\) to \(-j\) modulo six. The transformation \((x,y)\mapsto(y,-x)\) interchanges the two norms in \(F_\tau\); followed by a rotation, it sends relative edge index \(j\) to \(3-j\) modulo six. Consequently, after rotating \(x\) onto \(E_0\), the six possible edges containing \(y\) fall into exactly two orbit types: \(j\in\{0,3\}\) and \(j\in\{1,2,4,5\}\). The first type has first coordinates \(x_1=1\), \(y_1=\pm1\), whence \(F_\tau(x,y)\ge[(1+\tau)^2+(1-\tau)^2]/2=1+\tau^2\).

**2. Exact reduction on the four-edge orbit.** It suffices to treat \(x=(1,a)\) on \(E_0\) and \(y=(-1+b,-1)\) on \(E_4\), with \(0\le a,b\le1\). For \(0\le\tau\le1\), direct inspection of the three defining linear facets of \(N\) gives
\[
N(x+\tau y)=1+\tau b-\min\{\tau,a\},\qquad
N(\tau x-y)=1+\max\{\tau-b,\tau a\}.
\]
Both expressions are nonnegative maxima of affine functions of \((a,b)\), hence
\[
f_\tau(a,b)=\frac12\left[(1+\tau b-\min\{\tau,a\})^2+(1+\max\{\tau-b,\tau a\})^2\right]
\]
is convex on the square \([0,1]^2\). Put \(A=1+\tau^2\). We give exact subgradient-zero certificates, which prove *global* minima rather than only stationary values.

**3. First branch.** For \(0<\tau\le\rho\), take \(a=\tau\), \(b=\tau(1-\tau)\). The two norm terms are \(U=A(1-\tau)\) and \(V=A\). At the two kinks \(a=\tau\) and \(\tau-b=\tau a\), choose a subgradient coefficient
\[
\kappa=\frac{\tau(1-\tau+\tau^2)}{1-\tau}\in[0,1]
\]
for the first norm's \(-\min\) contribution, and coefficient \(\theta=\tau(1-\tau)\in[0,1]\) for the \(\tau-b\) branch of the second norm. The full subgradient of \(f_\tau\) is
\[
(-\kappa U+(1-\theta)\tau V,\ \tau U-\theta V)=(0,0).
\]
The condition \(\kappa\le1\) is equivalent to \(1-2\tau+\tau^2-\tau^3\ge0\). This polynomial decreases strictly on \([0,1]\) and has the single root \(\rho\). The minimizing objective is therefore \(A^2(1-\tau+\tau^2/2)\). At \(\tau=0\), both input norms are one and the objective equals one for every unit pair.

**4. Second branch.** For \(\rho\le\tau\le1\), put \(D=A^2+\tau^2\) and choose
\[
a_*=(A^2-\tau)/D,\qquad b_*=\tau(1-a_*).
\]
One checks \(0<a_*\le\tau\) precisely because \(1-2\tau+\tau^2-\tau^3\le0\). The two norm terms now are \(U=A(1-a_*)\) and \(V=1+\tau a_*\), and they satisfy \(AU=\tau V\). At the ridge \(\tau-b_*=\tau a_*\), give the \(\tau-b\) branch weight \(\theta=\tau^2/A\) and its competitor weight \(1-\theta\). The subgradient becomes
\[
(-U+(1-\theta)\tau V,\ \tau U-\theta V)=(0,0).
\]
Convexity proves global optimality. Evaluating gives \(\min f_\tau=A^2(1+\tau)^2/(2D)\). At \(\tau=\rho\) the two formulas agree and the optimizers coincide.

**5. Comparison with the opposite edge type.** The first-branch *trial* pair is admissible for every \(0\le\tau\le1\), regardless of whether it is optimal there. Its objective obeys
\[
A^2(1-\tau+\tau^2/2)\le A,
\]
because \(1-A(1-\tau+\tau^2/2)=\tau(1-\tau)(\tau^2-\tau+2)/2\ge0\). Consequently the four-edge minimum is no larger than the \(E_0/E_3\) lower bound \(A\), proving that our two branches give the unrestricted infimum. Finally, swapping the roles of the unit vectors in the skew transform yields \(\mathcal S_{H,2}(\tau)=\tau\mathcal S_{H,2}(1/\tau)\) for \(\tau>0\). Expansion of the first branch at zero proves the stated series.

## Verification
The proof is analytic for every real \(\tau\ge0\). A self-contained standard-library script `verify.py` checks exact-rational candidate objectives, a finite grid over all thirty-six edge pairs at seven rational parameters, the algebraic branch crossing, and the numerical location of \(\rho\). It reports 30,492 sampled pairs in total. Sampling is corroboration only; the edge-orbit argument, convexity and subgradient certificates prove the universal inequalities.

## Relationship to prior work
Xu and Liu introduced the skew Schäffer invariant in arXiv:2610.03050v1, proved general bounds and reciprocal-parameter symmetry, and derived exact formulas for Hilbert and Lebesgue spaces. Their results do not evaluate this non-Hilbert hexagonal plane. The public finding *Exact skew Schäffer endpoint profile of the regular hexagonal Banach plane* computes precisely the *outer exponent \(\infty\)*, obtaining \(\mathcal S_{H,\infty}(\tau)=\tau+(1+\tau+\tau^2)^{-1}\); it explicitly leaves finite outer exponents untreated. That endpoint gives \(4/3\) at \(\tau=1\), whereas the distinct quadratic value is \(4/\sqrt{10}\), and its small-parameter behavior has no linear term. A skew James constant uses a supremum rather than this infimum and does not determine the theorem. Results on alternative planes or on Lebesgue \(L^4\) are not equivalent to the present two-dimensional polyhedral statement.

## Limitations
The result is restricted to the real affine-regular hexagonal plane and the outer quadratic mean. It asserts no complete profile for general Banach spaces, no new bound on the best universal constant, and no complex-space version. The sampled checks are not an infinite certificate. Literature searches and the inspected primary texts do not rule out an unindexed equivalent formulation; independent scientific validation has not been performed.

## References
1. Ying Xu and Qi Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, first public 2026-10-02, https://arxiv.org/html/2610.03050v1; definition (2), Proposition 2.1, Hilbert and Lebesgue examples, and sharp universal bounds.
2. *Exact skew Schäffer endpoint profile of the regular hexagonal Banach plane*, publicly indexed October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-skew-sch-ffer-endpoint-profile-of-the-regular-hexagonal-ba--ab622dc4661e; the completed outer-exponent-\(\infty\) case, not the finite quadratic mean.
