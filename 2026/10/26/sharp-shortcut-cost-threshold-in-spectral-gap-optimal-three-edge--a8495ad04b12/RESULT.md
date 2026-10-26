# Sharp shortcut-cost threshold in spectral-gap-optimal three-edge parallel networks

## Finding
Let \(m\ge 2\) be an integer, \(B>0\), and \(\tau>0\). Construct a network with two terminals \(U,V\), one direct shortcut \(UV\), and \(m\) internally vertex-disjoint paths \(U-A_i-B_i-V\) of length three. Every edge has independently selectable nonnegative conductance. Each non-shortcut unit of conductance costs one unit, while each shortcut unit costs \(\tau\). The total cost is \(B\).

Put
\[
\tau_c(m)=\left(\frac{m}{m-1}\right)^2,
\qquad
D_m(\tau)=\begin{cases}
2m+m\sqrt{\tau}-\frac{m-1}{2}\tau,&0<\tau\le\tau_c(m),\\[2pt]
2m+\frac{m^2}{2(m-1)},&\tau\ge\tau_c(m).
\end{cases}
\]
The **exact globally maximal algebraic connectivity** (the second-smallest eigenvalue of the unnormalized weighted graph Laplacian) is
\[
\boxed{\Lambda_m(B,\tau)=\frac{B}{D_m(\tau)}.}
\]
One globally optimal allocation is symmetric, with every outer edge \(UA_i\) and \(B_iV\) receiving conductance \(x_*=\Lambda_m(B,\tau)\), every middle edge \(A_iB_i\) receiving
\[
y_*=\frac{\Lambda_m(B,\tau)}2\begin{cases}
\sqrt\tau,&\tau\le\tau_c(m),\\
\frac{m}{m-1},&\tau\ge\tau_c(m),
\end{cases}
\]
and the shortcut receiving
\[
z_*=\frac{\Lambda_m(B,\tau)}2\max\left\{0,1-m+\frac{m}{\sqrt\tau}\right\}.
\]
This is the unique allocation invariant under permutations of the paths and terminal reflection. **Every globally optimal allocation**, symmetric or not, assigns exactly \(z_*\) to the shortcut. In particular, every optimum deletes the shortcut precisely when \(\tau\ge\tau_c(m)\), even though adding conductance to an edge would increase connectivity if other weights were held fixed. Beyond the threshold the optimal value is independent of \(\tau\). The optimal eigenvalue has multiplicity exactly \(m\).

## Assumptions and scope
The weighted Laplacian is \(L=\sum_{\{u,v\}}w_{uv}(e_u-e_v)(e_u-e_v)^\mathsf{T}\), with \(w_{uv}\ge0\). The graph is simple, undirected, and has \(2m+2\) vertices. The cost is exactly
\[
\tau w_{UV}+\sum_{i=1}^{m}(w_{UA_i}+w_{A_iB_i}+w_{B_iV})=B.
\]
The theorem concerns **continuous-time** symmetric diffusion/consensus \(\dot p=-Lp\), not the second-largest eigenvalue modulus of a stochastic matrix. Every \(m\ge2\), \(B>0\), and \(\tau>0\) is included, with equality at the threshold included in the deletion regime. The edges on the paths all retain positive optimal conductance.

## Proof
**1. Symmetry reduction is globally valid.** For any weights, \(\lambda_2(L)=\min_{v\perp\mathbf1,\,\|v\|=1}v^{\mathsf T}Lv\) is concave in the weights. The graph automorphisms permute all \(m\) paths and interchange the terminals along with \(A_i\leftrightarrow B_i\). The costs are invariant under this group. Averaging any feasible allocation over the group cannot reduce \(\lambda_2\); hence a symmetric global maximizer exists. Denote by \(x\ge0\) its outer-edge conductance, by \(y\ge0\) its middle-edge conductance, and by \(z\ge0\) its shortcut conductance. Its cost is \(2mx+my+\tau z\).

**2. Exact spectrum.** Decompose the vertex space by terminal reflection and by fluctuations of the path indices. Direct substitution into the Laplacian gives the complete multiset of eigenvalues
\[
0,\quad (m+1)x,\quad
\underbrace{x,\ldots,x}_{m-1},\quad
\underbrace{x+2y,\ldots,x+2y}_{m-1},\quad
\operatorname{eig}(M),
\]
where the two remaining eigenvalues are those of
\[
M=\begin{pmatrix}mx+2z&-\sqrt m\,x\\-\sqrt m\,x&x+2y\end{pmatrix}.
\]
Since \(m\ge2\), the constraint \(\lambda_2(L)\ge1\) is equivalent to \(x\ge1\) and \(M\succeq I\). Indeed, the other listed nonzero eigenvalues then automatically exceed or equal one. The leading entry of \(M-I\) is \(mx+2z-1>0\); its Schur complement therefore gives precisely
\[
y\ge\frac12\left(\frac{mx^2}{mx+2z-1}-(x-1)\right).
\]

**3. Minimize cost at target spectral gap one.** Substitution yields the rigorous bound
\[
2mx+my+\tau z\ge F_\tau(x,z)
=\frac{3m}{2}x+\frac m2+\tau z+\frac{m^2x^2}{2(mx+2z-1)},
\qquad x\ge1,\ z\ge0.
\]
For fixed \(x\), the unconstrained minimizer in \(z\) is
\[
z_{\rm free}(x)=\frac{1+mx(\tau^{-1/2}-1)}2,
\]
and completing this one-variable minimization gives
\[
F_\tau(x,z)\ge \frac{m+\tau}{2}
+\frac{mx}{2}(3-\tau+2\sqrt\tau).
\]
When \(\tau\le\tau_c(m)\le4\), the coefficient \(3-\tau+2\sqrt\tau=4-(\sqrt\tau-1)^2\) is strictly positive. Thus the cost is bounded below by its expression at \(x=1\). The free minimizer there is nonnegative exactly when \(\tau\le\tau_c(m)\), so equality is attainable with
\[
x=1,\qquad y=\sqrt\tau/2,\qquad z=[1+m(\tau^{-1/2}-1)]/2.
\]
Its exact minimum cost is \(D_m(\tau)=2m+m\sqrt\tau-(m-1)\tau/2\).

When \(\tau>\tau_c(m)\), \(z_{\rm free}(x)<0\) for all \(x\ge1\). Consequently the minimum over \(z\ge0\) occurs at \(z=0\). The resulting lower bound
\[
F_\tau(x,0)=\frac{3m}{2}x+\frac m2+\frac{m^2x^2}{2(mx-1)}
\]
is strictly increasing for \(x\ge1\): its derivative equals
\[
\frac{3m}{2}+\frac{m^2}{2}\frac{x(mx-2)}{(mx-1)^2}>0
\]
because \(m\ge2\). Equality occurs uniquely at \(x=1\), \(z=0\), \(y=m/[2(m-1)]\), giving minimum cost \(D_m(\tau)=2m+m^2/[2(m-1)]\). At the boundary \(\tau=\tau_c(m)\), the two formulas agree and \(z=0\).

**4. Convert to any budget and recover unrestricted shortcut support.** Positive homogeneity of \(\lambda_2\) makes the best gap at budget \(B\) equal to \(B\) divided by the minimum cost for gap one. The equality conditions above uniquely determine the symmetric optimizer and are exactly the stated weights after scaling. Its antisymmetric matrix \(M\) has smaller eigenvalue \(x_*\), as seen from equality in the Schur complement, while the path-symmetric fluctuation eigenvalue \(x_*\) has multiplicity \(m-1\); all other nonzero eigenvalues are strictly larger. Thus the optimal gap has multiplicity \(m\).

Finally, average any unrestricted globally optimal allocation over the graph automorphism group. The averaged allocation is symmetric, feasible, and no worse by concavity; hence it equals the **unique** symmetric optimizer. The edge \(UV\) is fixed by every automorphism, so its weight is unchanged by averaging. Therefore **every unrestricted optimizer has shortcut conductance exactly \(z_*\)**. No unrestricted uniqueness of the other individual edge weights is asserted. \(\square\)

## Verification
The standalone `verify_numeric.py` constructs the exact graph Laplacian and independently evaluates the full spectrum on 90 parameter cases, including both sides of the threshold, the boundary, and large and small shortcut costs. It also checks 9,000 nonsymmetric randomly sampled feasible allocations and 12 independent constrained numerical optimizations. The maximum absolute discrepancy between the computed spectral gap and the closed form was approximately \(1.4\times10^{-16}\) in these cases; the maximum absolute cost discrepancy was approximately \(6.7\times10^{-16}\). The file `verify_exact.py` checks 30 rational-parameter characteristic-polynomial factorizations and budget identities in exact arithmetic. The recorded output is `verification_output.txt`. The universal statements rest on the preceding analytic argument, **not** on finite testing.

## Relationship to prior work
Sun, Boyd, Xiao, and Diaconis (2006) formulated cost-weighted fastest-mixing continuous-time graph design as a semidefinite program and connected it to maximum-variance unfolding. Their framework **contains this optimization problem**, but the inspected explicit examples concern a six-vertex triangle-with-tails graph, paths, and cycles, rather than the exact length-three parallel-path family and its shortcut-cost transition. In particular, a general semidefinite representation does not itself state the closed-form threshold or the all-optima shortcut deletion assertion. Boyd, Diaconis, Parrilo, and Xiao (2009) exploit graph automorphisms for the **discrete-time** fastest-mixing stochastic-matrix problem; their optimization objective and normalization differ. Shakeri and collaborators (2015) optimize interlayer link weights between fixed internal layers; the present problem optimizes all path weights and a redundant direct link jointly. These relationships motivate the reduction but do not imply the explicit classification.

## Limitations
No claim of uniqueness is made for the full **asymmetric** edge-weight vector, only for symmetric optimizers and for the shortcut weight across *all* optimizers. The result is restricted to exactly three-edge parallel paths with a single direct shortcut and the specified two-level cost structure. It does not imply analogous formulas for unequal path lengths, directed generators, discrete-time mixing, or additional constraints. The primary literature comparison is extensive but cannot exclude every obscure equivalent historical formulation; independent validation has not been performed.

## References
1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821, https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf. Public electronic publication confirmed on 2006-11-02.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819, arXiv:0709.0955, https://arxiv.org/abs/0709.0955.
3. H. Shakeri, N. Albin, F. D. Sahneh, P. Poggi-Corradini, and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785v1 (2015-10-22), https://arxiv.org/abs/1510.06785.
