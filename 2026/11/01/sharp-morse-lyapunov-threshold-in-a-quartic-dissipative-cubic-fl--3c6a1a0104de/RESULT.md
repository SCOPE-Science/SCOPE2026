# Sharp Morse–Lyapunov threshold in a quartic-dissipative cubic flow

## Finding

A homogeneous converse criterion and its sharp concrete realization are established.

**Homogeneous Morse criterion.** Let \(f:\mathbb R^n\to\mathbb R^n\) be a smooth homogeneous vector field of degree \(d>1\) for which the origin is globally asymptotically stable (GAS). A smooth, positive, proper, strict Morse Lyapunov function exists if and only if there is a symmetric positive definite matrix \(H\) satisfying
\[
 z^{\mathsf T}Hf(z)\leq0\qquad\text{for every }z\in\mathbb R^n.
\]
Here 'Morse' means that the Hessian at the origin is positive definite; strictness makes the origin the only critical point.

**Sharp symmetric cubic family.** For each real \(\kappa\), consider
\[
 \dot x=-x^3+\kappa y^3,\qquad \dot y=-y^3-\kappa x^3.
\]
The origin is GAS for **every** \(\kappa\in\mathbb R\), and the quartic polynomial \(W(x,y)=(x^4+y^4)/4\) is a global strict Lyapunov function. Nonetheless the origin has a smooth strict Morse Lyapunov function **if and only if**
\[
 |\kappa|\leq2\sqrt2.
\]
For \(|\kappa|\leq2\sqrt2\), every \(\varepsilon>0\) gives an explicit polynomial Morse certificate
\[
 M_\varepsilon(x,y)=x^2+y^2+\varepsilon(x^4+y^4)/4.
\]
For \(|\kappa|>2\sqrt2\), no even **local** twice-continuously differentiable strict Lyapunov function can have a positive definite Hessian at the origin. Thus the threshold is one of **certificate existence**, not of dynamical stability.

## Assumptions and scope

Homogeneity is positive scalar homogeneity \(f(\lambda z)=\lambda^d f(z)\) for every \(\lambda>0\), with \(d>1\); the assumed flow is smooth and the origin GAS on all Euclidean space. A smooth strict proper Lyapunov function is a \(C^\infty\) function \(L\geq0\), vanishing only at zero, whose sublevel sets are compact and whose Lie derivative \(\nabla L(z)\cdot f(z)<0\) for all \(z\neq0\). A Morse Lyapunov function additionally has \(D^2L(0)\succ0\). In the negative local claim it is enough to assume \(C^2\), positive Hessian, and nonpositive Lie derivative near zero; it need not be strict or proper for the contradiction.

## Proof

### 1. Homogeneous necessity

Suppose \(L\) is \(C^2\) near zero with \(DL(0)=0\), \(D^2L(0)=H\succ0\), and \(\nabla L\cdot f\leq0\) near zero. For fixed \(z\), Taylor expansion and homogeneity give
\[
 \nabla L(\lambda z)\cdot f(\lambda z)
 =\lambda^{d+1}z^{\mathsf T}Hf(z)+o(\lambda^{d+1})
 \quad(\lambda\downarrow0).
\]
The coefficient cannot be positive. Thus \(z^{\mathsf T}Hf(z)\leq0\) for **all** \(z\), even though the Lyapunov inequality was only local.

### 2. Homogeneous sufficiency

Suppose \(H\succ0\) and \(z^{\mathsf T}Hf(z)\leq0\) everywhere. Set \(Q(z)=z^{\mathsf T}Hz/2\). Since the origin is GAS and the flow is smooth, the classical smooth converse Lyapunov theorem supplies a smooth, positive, proper function \(W_0\) whose Lie derivative is strictly negative away from zero (see Jongeneel [1], introduction and its cited converse theorem). Set \(L=Q+W_0\). Then \(L\) is positive and proper, with
\[
 \nabla L\cdot f=z^{\mathsf T}Hf+\nabla W_0\cdot f<0
 \quad(z\neq0).
\]
As \(W_0\) has a minimum at zero, \(D^2W_0(0)\succeq0\), and hence \(D^2L(0)=H+D^2W_0(0)\succ0\). There is no other critical point, since any nonzero critical point would have zero Lie derivative. This proves the criterion with all global qualifiers.

### 3. Global stability for the cubic family

For the displayed family, a direct computation gives
\[
 \nabla W\cdot f_\kappa
 =x^3(-x^3+\kappa y^3)+y^3(-y^3-\kappa x^3)
 =-x^6-y^6<0\quad((x,y)\neq0).
\]
The quartic \(W\) is positive definite and proper. Its forward sublevel sets are compact, ensuring forward completeness. Strict decrease and the standard compact-invariance argument give global attraction, while sublevel invariance gives Lyapunov stability. Thus zero is GAS for all real \(\kappa\), with no other equilibrium.

### 4. Symmetry forces the radial quadratic test

Let \(R(x,y)=(-y,x)\). The cubic field satisfies \(f_\kappa(Rz)=Rf_\kappa(z)\). If any matrix \(H\succ0\) satisfies \(z^{\mathsf T}Hf_\kappa(z)\leq0\), then the average of its four rotations also satisfies this inequality. But
\[
 \frac14\sum_{j=0}^3 (R^j)^{\mathsf T}H R^j=\frac{\operatorname{tr}H}{2}I_2.
\]
Therefore the quadratic test exists **exactly when** the radial expression \(z\cdot f_\kappa(z)\leq0\) everywhere: necessity is the averaged inequality (with a positive scalar), and sufficiency uses \(H=I_2\). Crucially, this is an obstruction to **every** Morse Hessian, not merely to a particular quadratic candidate.

The radial expression is
\[
 z\cdot f_\kappa(z)=-(x^4+y^4)+\kappa xy(y^2-x^2).
\]
The exact perfect-square factorization
\[
 (x^4+y^4)^2-8x^2y^2(y^2-x^2)^2
 =(x^4-4x^2y^2+y^4)^2
\]
shows
\[
 \sup_{(x,y)\neq0}
 \frac{|xy(y^2-x^2)|}{x^4+y^4}=\frac1{2\sqrt2}.
\]
Equality is achieved on the nonzero rays \(y^2/x^2=2\pm\sqrt3\), with the required sign obtained by choosing quadrants or swapping coordinates. Thus \(z\cdot f_\kappa(z)\leq0\) for all \(z\) exactly when \(|\kappa|\leq2\sqrt2\). When the inequality holds,
\[
 \nabla M_\varepsilon\cdot f_\kappa
 =2(z\cdot f_\kappa)-\varepsilon(x^6+y^6)<0
\]
away from zero, \(M_\varepsilon\) is proper and positive, and \(D^2M_\varepsilon(0)=2I_2\). If \(|\kappa|>2\sqrt2\), an extremizing direction has positive radial derivative, contradicting the averaged necessary condition and thereby excluding any local \(C^2\) Morse Lyapunov function. This includes the endpoints as **admissible**, since the quartic term makes the explicit certificate strictly decreasing even where the radial quadratic is only weakly decreasing.

## Verification

`CHECK.py` is a standalone SymPy checker. After `pip install -r requirements.txt`, running `python CHECK.py` verifies the cancellation in the quartic Lie derivative, the radial expression, the exact perfect-square identity, fourfold rotational equivariance, an explicit radial positivity witness at \(\kappa=3\), and the Hessian of the polynomial certificate. Each identity is exact. The sharp uniform quantifiers, the global stability conclusion, and the nonexistence of arbitrary local Morse certificates are proved analytically above; numerical tests alone would not suffice.

## Relationship to prior work

Jongeneel [1] studies smooth Morse Lyapunov existence, proves the hyperbolic positive case, constructs a non-Morse example with nilpotent linear part, and identifies semisimplicity of the linear center as **necessary** (Corollary 3.9). The present result gives an if-and-only-if test under homogeneous GAS assumptions, and an exact example with identically zero (thus semisimple) Jacobian where the Morse property switches but GAS does not. It does **not** assert that no-Morse GAS counterexamples are new in themselves.

Liu and Fitzsimmons [2] construct a different GAS homogeneous cubic with no polynomial Lyapunov function and a parameter family with that obstruction. Their vector fields and conclusion are different: the present cubic family always has a strict quartic polynomial Lyapunov function, while its **smooth Morse** status has an exact finite threshold. The already published observation that nonsmooth/nonpolynomial certificates may be necessary is not claimed as new. Published results on quadratic Lyapunov inequalities are also recognized as standard ingredients; the contribution here is the homogeneous equivalence and sharp explicit family, not the elementary averaging device in isolation.

## Limitations

No claim is made for nonhomogeneous flows without further leading-order analysis, for an arbitrary nonglobally-attracting homogeneous equilibrium, or for robustness of the Morse cutoff to general perturbations destroying quarter-turn symmetry. The cutoff concerns existence of a certificate and is **not** a bifurcation: dynamics remain globally attracting throughout. The converse Lyapunov theorem is used as a standard published external theorem. No independent mathematical audit or complete historical-priority certification has been performed. Broader symmetry-based Lyapunov literature might contain an equivalent criterion; published coverage was checked but exhaustive novelty is not asserted.

## References

[1] W. Jongeneel, *On global Lyapunov functions being Morse*, arXiv:2610.05626v1, first public October 4, 2026, especially Sections 1.1, 3, Proposition 3.5 and Corollary 3.9. https://arxiv.org/html/2610.05626v1

[2] J. Liu and M. Fitzsimmons, *A Globally Asymptotically Stable Planar Homogeneous Polynomial Vector Field With No Polynomial Lyapunov Function*, arXiv:2607.16171v1, first public July 17, 2026, especially Theorem II.2 and Section IV-D. https://arxiv.org/abs/2607.16171
