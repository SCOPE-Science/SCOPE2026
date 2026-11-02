# Exact fastest reversible mixing on Boolean cubes with one biased coordinate

## Finding

Let \(d\ge1\) be an integer and \(0<a\le1/2\); put \(b=1-a\). On the Boolean cube \(\{0,1\}^{d+1}\), prescribe the product stationary distribution
\[
\pi(0,\mathbf{x})=a/2^d,\qquad
\pi(1,\mathbf{x})=b/2^d\qquad (\mathbf{x}\in\{0,1\}^d).
\]
Among **all** reversible, entrywise-nonnegative, row-stochastic transition matrices whose off-diagonal support consists only of single-coordinate flips (self-loops allowed), the minimum second-largest eigenvalue modulus is
\[
\boxed{\mu_*(d,a)=\frac{d-1-4dab+\sqrt{(d-1)^2+16dab}}{2(d+1-2dab)}.}
\]
A globally optimal kernel has the following off-diagonal transition probabilities, independent of \(\mathbf{x}\):
\[
\begin{aligned}
P((0,\mathbf{x}),(1,\mathbf{x}))&=b(1-\mu_*),\\
P((1,\mathbf{x}),(0,\mathbf{x}))&=a(1-\mu_*),\\
P((0,\mathbf{x}),(0,\mathbf{x}\oplus\mathbf e_j))&=\frac{a+b\mu_*}{d+1},\\
P((1,\mathbf{x}),(1,\mathbf{x}\oplus\mathbf e_j))&=\frac{b+a\mu_*}{d+1},\qquad 1\le j\le d.
\end{aligned}
\]
Its holding probabilities are respectively \((a+b\mu_*)/(d+1)\) and \((b+a\mu_*)/(d+1)\). It is the **unique optimizer within the group-invariant class** described in the proof; no uniqueness is asserted among all asymmetric feasible kernels.

Write \(s=ab\). The sharp dependence on bias is
\[
\frac{d-1}{d+1}<\mu_*(d,a)\le\frac{d}{d+2},
\]
where the upper equality holds exactly at \(a=1/2\) and the lower bound is attained only as \(a\downarrow0\). The optimum increases strictly with \(s\). In particular, any genuine bias strictly improves the optimal spectral mixing rate relative to the uniform cube. At \(d=1\), the formula simplifies to \(\sqrt{ab}/(1+\sqrt{ab})\).

## Assumptions and scope

Reversibility means \(\pi_iP_{ij}=\pi_jP_{ji}\). The spectral objective is the operator norm of \(\operatorname{diag}(\pi)^{1/2}P\operatorname{diag}(\pi)^{-1/2}\) on the orthogonal complement of its stationary vector \(\sqrt\pi\); thus it is well-defined even for a reducible competitor. No laziness restriction is imposed, and both holding and all allowed directed transition probabilities may be optimized independently subject to reversibility. The state space has \(2^{d+1}\) vertices and the only allowed moves are holding or changing exactly one coordinate. The endpoint \(a=0\) is excluded because it assigns zero stationary mass to half the vertices; the stated lower endpoint is a limit.

## Proof

**Symmetry reduction.** Let \(G\) be the group of translations and coordinate permutations of the last \(d\) bits. Its actions preserve both the graph and \(\pi\). If \(P\) is feasible, each conjugate by \(G\) is feasible. The spectral objective is a convex operator norm, so averaging gives a \(G\)-invariant feasible kernel with objective no larger. Such a kernel has a common stationary flow \(c/2^d\) across every edge changing the first bit, and common probabilities \(p\) and \(q\) to flip any one of the last \(d\) bits in layers \(0\) and \(1\), respectively. Its vertical transition probabilities are \(c/a\) and \(c/b\), and its holding probabilities are \(1-c/a-dp\) and \(1-c/b-dq\). Here \(c,p,q\ge0\) and these holdings are nonnegative.

**Two-by-two Fourier blocks.** Apply Walsh characters to the last \(d\) bits. A character with Hamming weight \(k\) gives, after similarity by \(\operatorname{diag}(\sqrt\pi)\), the symmetric block
\[
H_k=\begin{pmatrix}
1-c/a-2kp&c/\sqrt{ab}\\
c/\sqrt{ab}&1-c/b-2kq
\end{pmatrix},\qquad k=0,\ldots,d.
\]
Set \(u=(\sqrt b,-\sqrt a)^\mathsf T\), \(v=(\sqrt a,\sqrt b)^\mathsf T\), \(z=c/(ab)\), and \(D=\operatorname{diag}(p,q)\). Then
\[
I-H_k=z uu^\mathsf T+2kD.
\]
For \(k=0\), the eigenvalues of \(H_0\) are \(1\) and \(1-z\). Because \(D\succeq0\), the blocks decrease in Loewner order as \(k\) increases. Therefore a proposed bound \(\mu\in[0,1)\) on all nonstationary eigenvalue moduli implies, and for a feasible group-invariant kernel is equivalent to,
\[
1-\mu\le z\le1+\mu,\qquad A_z\preceq D\preceq B_z,
\]
where
\[
A_z=\frac{(1-\mu)I-z uu^\mathsf T}{2},\qquad
B_z=\frac{(1+\mu)I-z uu^\mathsf T}{2d}.
\]
The first matrix inequality comes from \(H_1\preceq\mu I\); the second comes from \(H_d\succeq-\mu I\). All intermediate Fourier weights are then controlled.

**Sharp infeasibility below the claimed rate.** Put \(s=ab\) and \(K=(d+1)\mu-(d-1)\), and write \(U=(B_z-A_z)_{11}\), \(V=(B_z-A_z)_{22}\). Directly,
\[
2dU=K+(d-1)zb,\qquad2dV=K+(d-1)za.
\]
The off-diagonal entries of \(A_z\) and \(B_z\) are respectively \(z\sqrt{s}/2\) and \(z\sqrt{s}/(2d)\). Since \(D\) is diagonal and \(D-A_z\) and \(B_z-D\) are positive semidefinite, their determinant inequalities and Cauchy--Schwarz force
\[
\sqrt{UV}\ge \frac{z\sqrt{s}}{2}\left(1+\frac1d\right).
\]
Equivalently,
\[
F_\mu(z):=K^2+(d-1)Kz-4dsz^2\ge0.\tag{1}
\]
At the smallest allowed \(z=1-\mu\), direct expansion gives
\[
F_\mu(1-\mu)=2f(\mu),\qquad
f(\mu)=(d+1-2ds)\mu^2+(1-d+4ds)\mu-2ds.\tag{2}
\]
This upward-opening quadratic has one positive root \(\mu_*\in(0,1)\), equal to the displayed radical, because \(f(0)<0\) and \(f(1)=2>0\). Its discriminant is \((d-1)^2+16ds\). Thus \(f(\mu)<0\) for \(0\le\mu<\mu_*\).

It remains to exclude a larger \(z\) evading (2). Since \(f((d-1)/(d+1))<0\), the positive root satisfies \(\mu_*>(d-1)/(d+1)\), hence \(K_*=(d+1)\mu_*-(d-1)>0\). Write \(\eta_*=1-\mu_*\). The identity \(F_{\mu_*}(\eta_*)=0\) implies \(4ds\eta_*^2=K_*^2+(d-1)K_*\eta_*\), and therefore
\[
\left.\partial_zF_{\mu_*}(z)\right|_{z=\eta_*}
=-(d-1)K_*-\frac{2K_*^2}{\eta_*}<0.
\]
For \(\mu<\mu_*\), the derivative at \(z=1-\mu\) is still smaller, as it is increasing in \(\mu\). Since \(F_\mu\) is strictly concave in \(z\), it decreases throughout \(z\ge1-\mu\). Hence (1) would give \(0\le F_\mu(z)\le2f(\mu)<0\), a contradiction. This lower bound holds against every original (possibly asymmetric) feasible kernel by the symmetry reduction.

**Attainment and symmetric-class rigidity.** Set \(\mu=\mu_*\), \(\eta=1-\mu\), \(z=\eta\),
\[
c=ab\eta,\qquad p=\frac{a+b\mu}{d+1},\qquad q=\frac{b+a\mu}{d+1}.
\]
The two holding probabilities equal \(p,q\), so the constructed kernel is stochastic, positive on every allowed edge, and reversible. For \(z=\eta\), \(A_z=\eta vv^\mathsf T/2\) and \(B_z=[\mu uu^\mathsf T+(1+\mu)vv^\mathsf T/2]/d\). The displayed \(p,q\) satisfy
\[
p-(A_z)_{11}=\frac{d}{d+1}U,\quad (B_z)_{11}-p=\frac{U}{d+1},
\]
with analogous identities for \(q,V\). Both \(U,V\) are positive; indeed \(\mu_*\ge(d-1)/(d+1)\). The equation \(f(\mu_*)=0\) gives
\[
UV=\frac{(d+1)^2\eta^2ab}{4d^2}.
\]
Consequently both \(D-A_z\) and \(B_z-D\) are positive semidefinite with zero determinant, giving the desired upper spectral bound \(\mu_*\). The \(k=0\) contrast eigenvalue is exactly \(1-z=\mu_*\), so equality holds. At the optimum, \(F_{\mu_*}(z)\) decreases strictly for \(z\ge\eta\), forcing \(z=\eta\). Equality in the Cauchy--Schwarz and determinant steps then forces the unique diagonal splitting \((p,q)\) just displayed; thus the group-invariant optimizer is unique.

**Strict bias law.** In (2), \(\partial_s f=-2d(1-\mu)^2<0\), and \(\partial_\mu f>0\) at its positive root, so \(d\mu_*/ds>0\). As \(s\downarrow0\), the positive root approaches \((d-1)/(d+1)\); at \(s=1/4\), direct substitution gives \(d/(d+2)\). Because \(s\) increases strictly with \(a\) on \((0,1/2)\), all asserted strict inequalities follow. The case \(d=1\) follows by simplifying the same radical.

## Verification

The included standalone `verify.py` carries out exact symbolic checks of the feasibility quadratic, radical discriminant, holding identities, and determinant factorizations. It also constructs the full kernels for dimensions \(d=1,\ldots,5\) and five rational stationary biases, checks stochasticity, detailed balance, stationarity and exact predicted SLEM numerically, and compares with independently sampled asymmetric reversible kernels. Running it with the listed dependencies produced `ALL_CHECKS_PASSED 883`. The full-domain theorem is proved above; finite tests do not substitute for that proof.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) establish convex semidefinite optimization for general fastest-mixing reversible chains with arbitrary stationary distributions; their general framework is used here, not claimed as new. Boyd, Diaconis, Parrilo and Xiao (2009), Section 3.2.2, explicitly solve the **uniform-stationary hypercube**. That formula is exactly the \(a=1/2\) boundary of this result and is acknowledged as previously known. The additional result is the complete one-biased-coordinate, all-dimension formula, an optimizer whose fair-coordinate rates depend on the biased bit, and the sharp strict interpolation in the stationary bias. Fill and Kahn (2011) address a different order-based comparison and path-chain setting. Collevecchio and Griffiths (2020) examine product-iid Bernoulli cube walks, especially long-range update and finite-time cutoff phenomena, not this one-exceptional-coordinate unrestricted nearest-neighbor SLEM optimum. An equivalent result in further specialized literature is not ruled out by the searches described in the accompanying review.

## Limitations

No claim is made about unrestricted optimizer uniqueness, nonreversible kernels, multi-coordinate flips, multiple biased coordinates, arbitrary nonproduct target measures, or finite-time total-variation optimality. The limiting case \(a\downarrow0\) is not a full-support stationary distribution at the endpoint. Independent mathematical validation has not been performed.

## References

- S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667--689, https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf (electronic publication October 29, 2004).
- S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792--819, https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf (Section 3.2.2).
- J. A. Fill and J. Kahn, *Comparison inequalities and fastest-mixing Markov chains*, arXiv:1109.6075 (first submitted September 28, 2011), https://arxiv.org/abs/1109.6075.
- A. Collevecchio and R. C. Griffiths, *Three steps mixing for general random walks on the hypercube at criticality*, arXiv:2002.09059 (February 20, 2020), https://arxiv.org/abs/2002.09059.
