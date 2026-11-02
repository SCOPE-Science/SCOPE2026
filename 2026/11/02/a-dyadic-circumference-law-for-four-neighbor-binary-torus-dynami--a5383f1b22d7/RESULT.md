# A dyadic-circumference law for four-neighbor binary torus dynamics

## Finding
Consider the synchronous binary four-neighbor sum rule on a rectangular torus of dimensions \(m\times n\). If one circumference is a power of two, \(m=2^a\) with \(a\ge2\), write \(d=2^{\nu_2(n)}\), \(\ell=\max(m,d)/2\), and \(c=2\min(m,d)\). Its nilpotent primary component consists of **exactly \(c\) Jordan blocks, all of length \(\ell\)**, while the other component is invertible. Consequently, the fraction of initial configurations already periodic is \(2^{-md}\); the maximal first-periodic-entry time is exactly \(\ell\); and the number of labelled initial configurations with first-entry time \(t\) is

\[
\#\{x:T(x)=t\}=\begin{cases}
2^{m(n-d)},&t=0,\\
2^{m(n-d)+c(t-1)}(2^c-1),&1\le t\le\ell,\\
0,&t>\ell.
\end{cases}
\]

In particular, changing the **odd factor** of \(n\) leaves the normalized distribution of \(T\) unchanged. Under uniform initialization,
\[
\Pr(T\le t)=2^{-c(\ell-t)}\quad(0\le t\le\ell),\qquad
\mathbb E T=\ell-\frac{1-2^{-c\ell}}{2^c-1}.
\]

## Assumptions and scope
The vertex set is \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\), with integers \(m=2^a\ge4\) and \(n\ge3\). Each state \(x_{i,j}\in\mathbb F_2\). The update is simultaneous and has no self-term:
\[
(Fx)_{i,j}=x_{i-1,j}+x_{i+1,j}+x_{i,j-1}+x_{i,j+1}\pmod2.
\]
All four neighbor locations are distinct. A state is *periodic* if \(F^q x=x\) for some integer \(q\ge1\). Define \(T(x)=\min\{t\ge0:F^t x\text{ is periodic}\}\). Labelled states are counted separately, with no quotient by translations, reflections or global complementation. The positive integer \(d\) is the largest power of two dividing \(n\), including \(d=1\) for odd \(n\).

## Proof
Identify the configuration space with the binary group algebra
\[
R=\mathbb F_2[u,v]/(u^m-1,v^n-1),
\]
where \(u,v\) are invertible. The update is multiplication by \(f=u+u^{-1}+v+v^{-1}\). Because \(m\) is a power of two, \(u^m-1=(u+1)^m\). Put \(k=n/d\), an odd integer. In characteristic two,
\[
v^n-1=((v+1)h(v))^d,
\qquad h(v)=(v^k-1)/(v+1),\qquad h(1)=1.
\]
The Chinese remainder theorem splits the second variable's algebra into \(B_0=\mathbb F_2[v]/((v+1)^d)\) and \(B_*=\mathbb F_2[v]/(h(v)^d)\), with \(B_*\) absent if \(h=1\). Their dimensions are \(d\) and \(n-d\). On \(B_*\), multiplication by \(v+v^{-1}=(v+1)^2/v\) is invertible because \(v+1\) is a unit there. On the first-variable algebra, multiplication by \(u+u^{-1}=(u+1)^2/u\) is nilpotent, because \((u+1)^m=0\). Therefore \(f\) is invertible on \(\mathbb F_2[u]/((u+1)^m)\otimes B_*\): it is the sum of an invertible operator and a commuting nilpotent operator. This gives an invertible summand of dimension \(m(n-d)\).

On \(B_0\), multiplication by \(v+v^{-1}\) is nilpotent. For a truncated local ring \(\mathbb F_2[w]/(w^s)\), multiplication by \(w^2\) times a unit has power ranks \(\max(s-2t,0)\) and hence, for even \(s\), exactly two nilpotent Jordan blocks of length \(s/2\). Applied to the first variable, this yields two blocks of length \(m/2\). Applied to \(B_0\), it yields two blocks of length \(d/2\) when \(d\ge2\), or a single zero block of length one when \(d=1\).

It remains to establish the tensor-sum Jordan type without invoking a characteristic-zero tensor-product rule. Let \(A,B\) be powers of two, \(A\ge B\). Represent a pair of blocks \(J_A(0)\otimes I+I\otimes J_B(0)\) as multiplication by \(s+t\) on \(\mathbb F_2[s,t]/(s^A,t^B)\). Writing \(z=s+t\), the Frobenius identity \((z+t)^A=z^A+t^A\), together with \(t^B=0\), gives an algebra isomorphism
\[
\mathbb F_2[s,t]/(s^A,t^B)\cong\mathbb F_2[z,t]/(z^A,t^B).
\]
This is a free module of rank \(B\) over \(\mathbb F_2[z]/(z^A)\). Thus the tensor sum has exactly \(B\) Jordan blocks, each of length \(A\). By symmetry, the result holds without ordering the sizes.

For \(d\ge2\), there are four pairwise tensor sums, each yielding \(\min(m/2,d/2)\) blocks of size \(\max(m/2,d/2)\). Consequently the nilpotent part has exactly \(c=2\min(m,d)\) blocks of length \(\ell=\max(m,d)/2\), in total dimension \(c\ell=md\). When \(d=1\), the two horizontal blocks are unchanged, which again gives \(c=2\) and \(\ell=m/2\). In all cases
\[
\operatorname{rank}(F^t)=m(n-d)+c\max(\ell-t,0),\qquad t\ge0.
\]

A finite-dimensional linear map over a finite field has periodic states precisely on its invertible Fitting summand: the nilpotent summand has no periodic state except zero. Consequently, \(F^t x\) is periodic exactly when the initial nilpotent component belongs to \(\ker(F^t)\). The kernel of the \(c\) uniform nilpotent Jordan blocks has dimension \(c\min(t,\ell)\). Multiplying its cardinality by the \(2^{m(n-d)}\) freely chosen states in the invertible summand gives the stated cumulative counts. Differences give the exact shells. The block size proves sharpness of \(\ell\). The expectation follows by summing \(\Pr(T>t)\) over \(0\le t<\ell\).

## Verification
The standalone standard-library Python program `verify.py` forms the actual binary four-neighbor transition matrix, multiplies its powers and independently computes ranks by binary Gaussian elimination. It verified all predicted ranks at times through two steps beyond the terminal depth for 39 rectangular tori with \(m\in\{4,8,16\}\), \(3\le n\le24\), and at most 200 sites. It separately simulated and classified every one of the 69,632 labelled initial configurations for dimensions \((4,3)\) and \((4,4)\), then tested 2,500 additional concrete configurations. The actual program output is stored in `verify_output.txt`. Finite computation corroborates, but does not replace, the proof for arbitrary \(m,n\).

## Relationship to prior work
The two-dimensional binary linear-rule formalism and null-boundary matrix representation in Choudhury–Nayak–Sahoo–Rath (2008) motivate the finite two-dimensional setting. Siap–Akin–Uguz (2013) study a different, ternary-valued periodic-boundary local rule and obtain rank procedures; Acar–Uguz–Akin (2017) study binary periodic-boundary *hybrid* rules and their reversible matrices. These papers do not state the present binary uniform four-neighbor first-periodic-entry law, the dependence solely on \(\nu_2(n)\), or the equal-size nilpotent Jordan partition. The classical one-dimensional Rule 90 analysis of Thomas–Stevens–Lettieri (2006) supplies relevant one-dimensional context but does not by itself give this two-dimensional tensor-sum count. A potentially relevant older study of exceptional two-dimensional rules by Dihidar–Choudhury (2004) was identifiable by its abstract, but not inspectable in full; that limits the strength of the historical-originality conclusion.

## Limitations
The theorem requires one circumference to be a power of two and concerns the four-neighbor, no-self-term binary rule. It does not classify primitive periods on the invertible summand, or torus dimensions with neither circumference dyadic. No claim of independent auditing or historical exhaustiveness is made. The full historical content of Dihidar–Choudhury (2004) was not available for a decisive text-level comparison.

## References
1. P. P. Choudhury, B. K. Nayak, S. Sahoo and S. P. Rath, *Theory and Applications of Two-dimensional, Null-boundary, Nine-Neighborhood, Cellular Automata Linear rules* (arXiv:0804.2346, first submitted 2008-04-15). https://arxiv.org/abs/0804.2346
2. I. Siap, H. Akin and S. Uguz, *2-D Reversible Cellular Automata with Nearest and Prolonged Next Nearest Neighborhoods under Periodic Boundary*, European Journal of Pure and Applied Mathematics 6 (2013), 315–334. https://www.ejpam.com/index.php/ejpam/article/download/2011/305/0
3. E. Acar, S. Uguz and H. Akin, *Characterization of 2D Hybrid Cellular Automata with Periodic Boundary*, Acta Physica Polonica A 131 (2017), 432–436. https://doi.org/10.12693/APhysPolA.131.432
4. D. M. Thomas, J. G. Stevens and S. Lettieri, *Characteristic and Minimal Polynomials of Linear Cellular Automata*, Rocky Mountain Journal of Mathematics 36 (2006), 1077–1092. https://doi.org/10.1216/rmjm/1181069447
5. K. Dihidar and P. P. Choudhury, *Matrix algebraic formulae concerning some exceptional rules of two-dimensional cellular automata*, Information Sciences 165 (2004), 91–101. https://doi.org/10.1016/j.ins.2003.09.024
