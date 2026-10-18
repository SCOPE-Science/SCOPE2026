# Sharp rational fastest-mixing regime for unbalanced double-star trees

## Finding

Let \(D_{p,q}\) be the tree obtained by connecting two adjacent hubs, the first with \(p\) pendant leaves and the second with \(q\) pendant leaves, where \(p>q\ge2\) are integers. Assign a symmetric nonnegative transition probability to every tree edge, allow a nonnegative holding probability at every vertex, and require all row sums to equal one. Minimize the second-largest eigenvalue modulus (SLEM) of the stochastic matrix over **all** such edge assignments, including unequal probabilities among leaves on the same side.

Put
\[
 K=p^2+p-q,\qquad
 a_*=\frac{p-q}{K},\quad
 c_*=\frac{p(p-q)}{qK},\quad
 b_*=\frac{p(q+1)-q}{K},
\]
\[
 N(p,q)=p^2(p-q)^2-[p(q+1)-q]^2-p^2q^2.
\]
The symmetric candidate places transition probabilities \(a_*\) on every left pendant edge, \(c_*\) on every right pendant edge and \(b_*\) on the central bridge; both hubs have zero holding probability. **This chain is globally fastest mixing if and only if \(N(p,q)\ge0\).** Whenever that criterion holds, the exact optimal SLEM is
\[
 \boxed{\mu_*(D_{p,q})=1-\frac{p-q}{p^2+p-q}.}
\]
When \(N(p,q)<0\), the displayed candidate is strictly suboptimal (the optimal SLEM in this complementary regime is not determined here).

For each fixed integer \(q\ge2\), the equation \(N(p,q)=0\), interpreted for real \(p>q\), has exactly one solution \(p_{\mathrm c}(q)>q\). Thus for integer \(p>q\) the displayed rational chain is optimal exactly for \(p\ge p_{\mathrm c}(q)\), and
\[
 \lim_{q\to\infty}\frac{p_{\mathrm c}(q)}q=1+\sqrt2.
\]
The first optimal integer \(p\) values for \(q=2,3,4\) are respectively \(6,8,11\).

## Assumptions and scope

All graphs are finite, simple, undirected and connected. Every edge transition weight may be zero, and holding probabilities make the transition matrix stochastic. The chain is symmetric and hence has uniform stationary distribution; no preset equal-leaf condition is imposed. Write \(P=I-L\) and let the eigenvalues of the positive semidefinite weighted Laplacian \(L\) be \(0=\lambda_1(L)\le\cdots\le\lambda_{p+q+2}(L)\). Then
\[
 \mu(P)=\max\{1-\lambda_2(L),\lambda_{p+q+2}(L)-1\}.
\]
The result classifies exactly when the explicit rational, hub-saturated candidate is globally optimal. It does not classify every optimizer or provide the numerical optimum when \(N(p,q)<0\).

## Proof

**1. Reduction to an upper bound on the spectral gap.** Averaging any feasible chain over permutations of the leaves within each side keeps feasibility, and concavity of the smallest positive Laplacian eigenvalue on the fixed orthogonal complement of the constants implies that this averaging cannot decrease \(\lambda_2(L)\). Thus an upper bound for the algebraic connectivity of all side-symmetric chains applies to all feasible chains. A side-symmetric chain has leaf-to-hub weights \(a,c\) and bridge weight \(b\), where \(pa+b\le1\) and \(qc+b\le1\). Increasing either spoke weight, with \(b\) fixed, to saturate the corresponding hub only adds a positive-semidefinite edge Laplacian. Hence it suffices for this upper bound to consider
\[
 0\le b\le1,\qquad a(b)=\frac{1-b}{p},\quad c(b)=\frac{1-b}{q}.
\]
The left leaf-difference eigenspace has eigenvalue \(a(b)\) with multiplicity \(p-1\), so
\[
 \lambda_2(L(b))\le a(b).
\]

**2. Exact candidate gap.** Elementary algebra gives \(pa_*+b_*=qc_*+b_*=1\), \(c_*>a_*>0\), and
\[
 (1-a_*)(c_*-a_*)=q c_*^2.
\]
In the orthonormal four-dimensional basis of the two normalized leaf sums and the two hub vectors, the remaining weighted Laplacian block is
\[
 M=\begin{pmatrix}
 a_*&-\sqrt p\,a_*&0&0\\
 -\sqrt p\,a_*&1&-b_*&0\\
 0&-b_*&1&-\sqrt q\,c_*\\
 0&0&-\sqrt q\,c_*&c_*
 \end{pmatrix}.
\]
Subtract \(a_*I\) and partition after the first two coordinates. The upper-left two-by-two block has determinant \(-pa_*^2<0\), hence one positive and one negative eigenvalue. Its inverse has bottom-right entry zero, so its Schur complement is exactly
\[
 \begin{pmatrix}1-a_*&-\sqrt q\,c_*\\-\sqrt q\,c_*&c_*-a_*\end{pmatrix},
\]
which is nonzero positive semidefinite of rank one. By congruence and Sylvester inertia, \(M-a_*I\) has exactly one negative, one zero, and two positive eigenvalues. Because the other leaf-difference eigenvalues are \(a_*\) and \(c_*>a_*\), the full Laplacian has
\[
 \lambda_2(L_*)=a_*.
\]
The eigenvalue \(a_*\) is represented in the quotient block by a nonconstant vector with left leaf value \(y=-b_*/(pa_*)\), left hub value \(0\), right hub value \(1\), and right leaf value \(w=c_*/(c_*-a_*)\), which is orthogonal to constants.

**3. Sharp global criterion.** Keep this fixed quotient eigenvector \(u\) while allowing \(b\) to vary in the saturated family. Its Rayleigh quotient is affine:
\[
 \frac{u^\mathsf{T}L(b)u}{\|u\|^2}
 =a_*+\frac{(b-b_*)[1-y^2-(1-w)^2]}{\|u\|^2}.
\]
Direct substitution yields
\[
 1-y^2-(1-w)^2
 =\frac{N(p,q)}{p^2(p-q)^2}.
\]
If \(N(p,q)\ge0\), for every \(b\le b_*\) this Rayleigh quotient is at most \(a_*\), hence \(\lambda_2(L(b))\le a_*\). For \(b\ge b_*\), the leaf-difference bound gives \(\lambda_2(L(b))\le a(b)\le a_*\). Together with step 1, no feasible chain has spectral gap exceeding \(a_*\). Consequently its SLEM cannot be smaller than \(1-a_*\).

Conversely suppose \(N(p,q)<0\). The eigenvalue \(a_*\) of the four-dimensional quotient block is simple, as the inertia calculation shows. Its analytic eigenvalue branch has derivative with the negative sign of \(N(p,q)\) under varying \(b\). For \(b<b_*\) sufficiently close to \(b_*\), this quotient eigenvalue is strictly larger than \(a_*\); so is the leaf-difference eigenvalue \(a(b)\), while the remaining nonzero eigenvalues have a strict positive gap above \(a_*\). It follows that \(\lambda_2(L(b))>a_*\) in this one-sided neighborhood.

**4. Control of negative transition eigenvalues.** For any saturated chain \(L(b)\), the tree is bipartite, so its weighted Laplacian and weighted signless Laplacian \(Q(b)\) are diagonally similar. Take the strictly positive vector \(v\) that equals \(1\) at each hub and \(1/2\) at every leaf. The coordinate ratios \((Q(b)v)_i/v_i\) equal \((3+b)/2\) at both hubs, and \(3a(b)\), \(3c(b)\) at their respective leaves. Since \(p\ge q\ge2\), these ratios are at most \((3+b)/2\). The Perron–Frobenius comparison gives
\[
 \lambda_{\max}(L(b))\le\frac{3+b}{2}\le2-a(b).
\]
Since \(\lambda_2(L(b))\le a(b)\), we conclude
\[
 \mu(I-L(b))=1-\lambda_2(L(b)).
\]
In particular the candidate has SLEM \(1-a_*\), establishing sufficiency in step 3. When \(N(p,q)<0\), the nearby \(b<b_*\) saturated chain from step 3 has strictly smaller SLEM, proving necessity.

**5. Threshold and asymptotics.** Put \(p=q+h\). Expansion gives
\[
 N(q+h,q)=h^4+2qh^3-(q^2+2q+1)h^2-(4q^3+2q^2)h-2q^4.
\]
For every \(q>0\) its nonzero coefficients have exactly one sign change, from positive to negative. Descartes' rule, the negative value at \(h=0\), and positive growth at infinity imply exactly one positive root. Finally, for \(t>1\),
\[
 \lim_{q\to\infty}\frac{N(tq,q)}{q^4}
 =t^2(t^2-2t-1).
\]
The unique positive root beyond \(t=1\) is \(1+\sqrt2\). Uniform convergence on compact neighborhoods and uniqueness of the positive root give the stated threshold ratio.

## Verification

The accompanying `verify.py` tests eight symbolic identities, including saturation, the quotient eigenvalue equality, the sign polynomial, its shifted expansion and the asymptotic leading coefficient. It independently builds all weighted Laplacian matrices for 231 integer pairs \(3\le p\le23\), \(2\le q<p\), checks the candidate spectral gap and the bound on the largest eigenvalue, and checks one-sided improvements and Rayleigh upper-bound comparisons where applicable. These are finite corroborations; steps 1–5 supply the all-integer proof.

Reproduce with Python 3, SymPy and NumPy:

```sh
python verify.py
```

## Relationship to prior work

Boyd, Diaconis and Xiao established the general convex/semidefinite formulation for minimizing SLEM on any fixed undirected graph; this general methodology is not claimed as new. Boyd, Diaconis, Parrilo and Xiao developed graph automorphism reduction and gave an exact symmetric clique-barbell example \(K_n\!\text{--}\!K_n\). That example allows positive internal clique transitions and has equal cluster sizes; its stated optimal weights and spectrum do not give the present unequal tree-edge probabilities, exact rational optimum, or the polynomial imbalance boundary by direct substitution. Symmetry reduction alone does not establish this threshold because it does not decide the competing leaf and quotient eigenmodes. The result is limited to unequal double-star trees \(p>q\ge2\) and the explicitly indicated high-imbalance regime.

## Limitations

This is an exact sufficient-and-necessary **optimality criterion for the displayed candidate**, not a classification of the optimizer for every unequal double-star. We do not claim uniqueness of the globally optimal stochastic matrix, or that previously known convexity/SDP methods are new. The graph family has no nonuniform stationary probabilities or directed transitions. A specialized prior treatment of unequal double-star FMMC may exist outside the inspected sources; no exhaustive novelty guarantee or independent review is asserted.

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689. DOI: 10.1137/S0036144503423264. Freely readable author manuscript: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization **20** (2009), 792–819. DOI: 10.1137/070689413. Preprint dated 2007-09-06: arXiv:0709.0955v1; full manuscript: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf .
