# Sharp exponential correction to the regular-element density for two equal blocks

## Finding

Let \(T_m\) be the monoid of all total maps on a labeled union \(A\sqcup B\), \(|A|=|B|=m\ge1\), taking each block into a single block. A map \(f\) is regular when some \(g\in T_m\) satisfies \(fgf=f\). Let \(R_m\) be the proportion of regular maps. The claimed contribution is the sharp correction
\[
R_m=\frac12+C\rho^m(1+o(1))\qquad (m\to\infty),
\]
including its prefactor. Define \(x\in(0,1)\) as the unique solution to \(\exp[-x/(1-e^{-x})]=1+(x-1)e^x\), set \(y=x/(1-e^{-x})\), and write \(H(z,w)=1+(e^z-1)e^w\). Then
\[
\rho=\frac{H(x,y)}{e^2xy}=0.696742956572524\ldots,
\qquad C=\frac1{\sqrt{xy-(y-1)^2}}=1.210700991285293\ldots .
\]
The error is relative to the correction, not to \(R_m\). The exact Stirling count is included as a proof ingredient and is not claimed as an additional contribution: it is contained in the rank enumerator cited below. The assertion does not extend to unequal blocks or to an arbitrary number of blocks.

## Proof

### Counting reduction (background)

For each of four block characters there are \(m^{2m}\) maps. For either bijective character, choose one preimage within the corresponding source block for each image point to construct a partition-preserving inner inverse. For a constant character, let the two restriction images be \(U,V\) in the common target block. The inner inverse must take that block into one source block, so it can return points of \(U\cup V\) to preimages only if one of \(U,V\) contains the other. That condition suffices, by choosing preimages in the source block having the larger image and extending arbitrarily within the block constraints.

For independent uniform selfmaps \(F,G\) of an \(m\)-point set, let \(a_m=\Pr(\operatorname{im}G\subseteq\operatorname{im}F)\) and \(b_m=\Pr(\operatorname{im}G=\operatorname{im}F)\). Thus \(R_m=\tfrac12+a_m-\tfrac12 b_m\). With \(u_{m,s}=s!S(m,s)\), where \(S(m,s)\) is a Stirling number of the second kind,
\[
a_m=m^{-2m}\sum_s\binom ms u_{m,s}s^m,
\qquad b_m=m^{-2m}\sum_s\binom ms u_{m,s}^2.
\]
Indeed, choose the containing or common image, count the first map as a surjection to it, then count the second map as arbitrary into it or surjective onto it, respectively. In the cited rank-count record, the regular-map rank polynomial is \(2P_m(z)^2+C_m(z)\), with \(P_m(1)=m^m\) and \([z^s]C_m=4\binom ms u_{m,s}s^m-2\binom ms u_{m,s}^2\). Specializing to \(z=1\) and dividing by \(4m^{2m}\) gives exactly the above proportion for \(m\ge2\). The case \(m=1\) gives proportion one directly.

### Positive saddle and local limit

For a given target point, let \(u,v\) be its occupancies under \(F,G\). Containment allows \((0,0)\) or \(u\ge1,v\ge0\), with exponential generating function \(H(z,w)\). Allocation of both classes of labeled inputs gives
\[
a_m=\frac{(m!)^2}{m^{2m}}[z^mw^m]H(z,w)^m.
\]
The positive saddle solves \(xH_z/H=yH_w/H=1\) at \((x,y)\). Dividing the equations gives \(y=x/(1-e^{-x})\), and substituting in the first yields \(e^{-y}=1+(x-1)e^x\). On \((0,1)\) the left side decreases strictly as \(y\) increases, while the right side strictly increases from zero to one. The left side starts at \(e^{-1}\) and ends below one, so there is one solution there; for \(x\ge1\) the right side is at least one. The function \(\log H(e^u,e^v)-u-v\) is strictly convex: its Hessian is the covariance of the positively tilted occupancy vector and the admissible support is not collinear. Thus its critical point is its minimum. In particular, \(0<\rho\le H(1,1)/e^2=1-e^{-1}+e^{-2}<1\).

Give the admissible pair \((U,V)=(u,v)\) probability \(x^uy^v/(u!v!H(x,y))\). It has mean \((1,1)\), and its factorial second moments are \(\mathbb E[U(U-1)]=x\), \(\mathbb E[V(V-1)]=y\), \(\mathbb E[UV]=y\). Hence its covariance matrix is
\[
\Sigma=\begin{pmatrix}x&y-1\\y-1&y\end{pmatrix},\qquad D=\det\Sigma=xy-(y-1)^2>0.
\]
The positive masses at \((0,0),(1,0),(1,1)\) rule out any affine-line support or proper difference lattice. The tilted law has finite exponential moments. Let \(E_m\) be the event that the sum of \(m\) independent such pairs equals \((m,m)\). In the Fourier inversion integral on the two-torus, the modulus of the characteristic function is uniformly bounded by a constant strictly less than one outside a neighborhood of the origin, since modulus one would require identical phases at all three stated points. Near the origin the centered log characteristic function equals \(-\frac12t^{\mathsf T}\Sigma t+O(\|t\|^3)\), with real part bounded above by a negative constant times \(\|t\|^2\) there. Rescaling by \(m^{-1/2}\), Gaussian integration with this bound gives \(\Pr(E_m)=(1+o(1))/(2\pi m\sqrt D)\). No periodic multiplier occurs.

Coefficient extraction in the tilted law and Stirling's formula give
\[
a_m=\frac{(m!)^2}{m^{2m}}\left(\frac{H(x,y)}{xy}\right)^m\Pr(E_m)
\sim \frac1{\sqrt D}\left(\frac{H(x,y)}{e^2xy}\right)^m.
\]
Conditional on \(E_m\), occupancy weights are proportional to \(1/\prod u_i!v_i!\), exactly as for the two labeled maps conditioned on inclusion. Equal images cannot have a target point with \(U>0,V=0\). A tilted point has that type with probability \(p=(e^x-1)/H(x,y)>0\). Thus independence before conditioning yields \(b_m/a_m\le (1-p)^m/\Pr(E_m)=O(m(1-p)^m)=o(1)\). This establishes the claimed correction and prefactor.

## Verification and limitations

The attached finite Python check uses the exact identity \(f(g(y))=y\) for all \(y\) in the image of \(f\) to test regularity over every possible \(g\) when \(m\le3\). Counts are \(4/4,60/64,2400/2916\). A separate Stirling count and numerical saddle check reproduce the asymptotic ratios at \(m=40,80\); they do not prove the limit. The argument is for all regular elements, not the size of a specific regular subsemigroup or a count of idempotents. Priority in the broader occupancy literature is not certified.

## Compared sources

- [*Rank enumerators and exponential size asymmetry of the two maximal regular partition-preserving transformation semigroups*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-rank-enumerators-and-exponential-size-asymmetry-of-the-two-maxim--859bee082aaf), Finding. Its rank polynomial supplies the exact count; its exponential bound does not identify the asymptotic rate or prefactor of the excess regular fraction. The catalogue date is not a priority determination.
- M. Sarkar and S. N. Singh, [*Semigroups of transformations whose characters belong to a given semigroup*](https://arxiv.org/abs/2310.19414), Proposition 3.4. The image criterion is a specialization of their structural theorem.
- M. Sarkar and S. N. Singh, [*Regular, Unit-regular, and Idempotent elements of semigroups of transformations that preserve a partition*](https://arxiv.org/abs/2010.14033), §6. Their enumeration is for the onto-block subsemigroup, not the full monoid above.
- K. Sangkhanan, [*Maximal regular subsemigroups containing the group of units of transformation semigroups that preserve a uniform equivalence relation with two classes*](https://arxiv.org/abs/2610.38341v1), Theorem 3.15. This classifies two maximal regular subsemigroups containing the units, a different question from the sharp correction for all regular elements.
