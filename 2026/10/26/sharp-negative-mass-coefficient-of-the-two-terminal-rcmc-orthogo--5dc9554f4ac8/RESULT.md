# Sharp negative-mass coefficient of the two-terminal RCMC orthogonal projector

## Finding
Let a finite irreducible detailed-balance Markov generator have stationary distribution \(\pi>0\). Retain exactly two states \(a,b\), eliminate a nonempty set \(S\), and write \(\alpha=\pi_a\), \(\beta=\pi_b\), \(\mu=\sum_{s\in S}\pi_s=1-\alpha-\beta\). The uncorrected Type B rate-constant matrix contraction (RCMC) projector \(V_B\) has a negative cross-terminal entry unless each connected eliminated component touches at most one retained terminal. The following universal, **sharp**, fixed-stationary-mass bound holds over every connected reversible kinetic graph and all positive rates:

\[
\boxed{0\le -(V_B)_{ab}\le
\frac{\alpha\mu}{2\left[\alpha\beta+\sqrt{\alpha\beta(\alpha+\mu)(\beta+\mu)}\right]}.}
\]

The maximum is attained on a connected graph for every prescribed strictly positive stationary vector. In the uniform case on \(n\ge3\) states the maximum is exactly \((n-2)/(2n)\). With \(\alpha\in(0,1)\) fixed and \(\beta\downarrow0\), while \(\mu=1-\alpha-\beta\), the sharp bound is asymptotic to \(\tfrac12\sqrt{\alpha(1-\alpha)/\beta}\), and thus is unbounded even for three states. This is a *single matrix entry*, not an asserted bound on the total negative mass.

## Assumptions and scope
For \(n\ge3\), \(K\in\mathbb R^{n\times n}\) has off-diagonal entries \(K_{ij}\ge0\) and column sums zero. Its undirected support graph is connected. Assume \(\pi_i>0\), \(\sum_i\pi_i=1\), \(K\pi=0\), and detailed balance \(K_{ij}\pi_j=K_{ji}\pi_i\). Fix distinct terminals \(T=\{a,b\}\) and let \(S=\{1,\ldots,n\}\setminus T\ne\varnothing\). All rates on the chosen support edges are strictly positive. In the source's notation define \(C=-K_{SS}^{-1}K_{ST}\), the rectangular extension matrix \(\Omega\in\mathbb R^{n\times2}\) by \(\Omega_S=C\), \(\Omega_T=I_2\), its adjoint for \(\langle x,y\rangle_\pi=x^\top\operatorname{diag}(\pi)^{-1}y\) by \(\Omega^*=\operatorname{diag}(\pi_T)\Omega^\top\operatorname{diag}(\pi)^{-1}\), and
\[
V_B=\Omega(\Omega^*\Omega)^{-1}\Omega^*.
\]
The inverse exists by connectedness and positive definiteness of the relevant Dirichlet submatrix. The result concerns the *uncorrected* linear Type B projector; the source's subsequent nonlinear projection onto the probability simplex is not part of the claim.

## Proof
Write the symmetric edge conductances as \(w_{ij}=K_{ij}\pi_j=w_{ji}\). Let \(p_a=1\), \(p_b=0\), and let \(p_s\) solve \(\sum_jw_{sj}(p_s-p_j)=0\) for every \(s\in S\). The weighted graph maximum principle gives \(0\le p_s\le1\). Multiplying the Dirichlet equation by the reversible stationary masses gives the exact extension coefficients
\[
C_{sa}=\frac{\pi_s p_s}{\alpha},\qquad
C_{sb}=\frac{\pi_s(1-p_s)}{\beta}.
\]
Set \(z=\sum_{s\in S}\pi_s p_s\), \(q=\sum_{s\in S}\pi_s p_s^2\), \(A=q\), \(B=z-q\), and \(D=\mu-2z+q\). Thus \(B\ge0\), \(0\le z\le\mu\), and weighted Cauchy–Schwarz gives \(q\ge z^2/\mu\), with equality exactly when all \(p_s\) have one constant value. The weighted Gram matrix is
\[
M=\Omega^*\Omega=
\begin{pmatrix}1+A/\alpha&B/\beta\\B/\alpha&1+D/\beta\end{pmatrix}.
\]
Because the terminal rows of \(\Omega\) are coordinate rows, \((V_B)_{ab}=(M^{-1})_{ab}\). Direct inversion yields the **exact harmonic-moment identity**
\[
-(V_B)_{ab}
=\frac{\alpha B}{\alpha\beta+\beta A+\alpha D+AD-B^2}
=\frac{\alpha(z-q)}{\alpha(\beta+\mu)-2\alpha z+q-z^2},
\]
using \(AD-B^2=\mu q-z^2\). Both denominators are strictly positive since \(M\) is positive definite. For each fixed \(z\), increasing \(q\) decreases the numerator and increases the denominator; consequently the ratio is maximized at \(q=z^2/\mu\). Write \(z=\mu r\), \(0\le r\le1\); the resulting one-variable upper bound is
\[
 g(r)=\frac{\alpha\mu r(1-r)}{\alpha\beta+\beta\mu r^2+\alpha\mu(1-r)^2}.
\]
Put \(v=r/(1-r)\). For \(0<r<1\),
\[
 g=\frac{\alpha\mu v}{\alpha(\beta+\mu)+2\alpha\beta v+\beta(\alpha+\mu)v^2}.
\]
The derivative has the sign of \(\alpha(\beta+\mu)-\beta(\alpha+\mu)v^2\), so the *unique* maximizer is
\[
 v_*=\sqrt{\frac{\alpha(\beta+\mu)}{\beta(\alpha+\mu)}},\qquad
 r_*=\frac{\sqrt{\alpha(\beta+\mu)}}{\sqrt{\alpha(\beta+\mu)}+\sqrt{\beta(\alpha+\mu)}}.
\]
Substitution proves the sharp bound. To attain it for any prescribed \(\pi\), join each eliminated state \(s\) only to both terminals, with symmetric conductances \(w_{sa}=r_*\), \(w_{sb}=1-r_*\). The resulting connected reversible network satisfies \(p_s=r_*\) for every \(s\), hence equality in Cauchy–Schwarz and in the scalar optimization. Positive terminal-terminal conductance is optional.

Finally, \(B=\sum_{s\in S}\pi_s p_s(1-p_s)>0\) precisely when some eliminated connected component touches both terminals: if so, the strong graph maximum principle gives \(0<p_s<1\) throughout that component; otherwise each component has constant harmonic boundary data, and \(p_s\in\{0,1\}\). This proves the sign criterion. When \(B=0\) the Gram matrix is diagonal and Type A and B coincide; when \(B>0\), applying \(V_B\) to the terminal point mass \(e_b\) produces the negative \(a\)-coordinate \((V_B)_{ab}\). The uniform specialization and rare-terminal asymptotic follow by elementary substitution into the attained optimum.

## Verification
For three states \(a,s,b\) with uniform stationary distribution and equal edge conductances on the path \(a-s-b\), direct rational inversion gives
\[
V_B=\begin{pmatrix}5/6&1/3&-1/6\\1/3&1/3&1/3\\-1/6&1/3&5/6\end{pmatrix};
\]
thus the sharp bound equals \(1/6\). The self-contained \(\texttt{verify.py}\) uses only the Python standard library and exact fractions to reconstruct these matrices, assert weighted Gram identities, mass preservation, idempotence, the graph-sign condition, and the stated sharp inequality on a deterministic sample of weighted connected graphs. Execute \(\texttt{python3 verify.py}\) from the same extracted directory. Its finite checks do not establish universal graph assertions; the proof above does.

## Relationship to prior work
Iwata, Oki and Sakaue introduced the reformulated Type A and Type B RCMC matrices and proved Type B's weighted orthogonal-projection property. They explicitly noted that Type B can leave the probability simplex and proposed a subsequent simplex projection. Those known constructions and their qualitative failure of positivity are premises here, **not** new discoveries. The present result adds an exact cross-terminal formula and a sharp, attained bound depending only on the retained and eliminated stationary masses; it exposes an unbounded conditioning effect as a terminal becomes rare. Hemmi, Iwata and Oki analyze computational stabilization of RCMC (emphasizing Type A), not this sharp negative coefficient. Kron-reduction literature establishes related Dirichlet/harmonic extension mechanisms but does not in the inspected material give this RCMC Type B projector extremum. Publication priority remains subject to broader and independent review.

## Limitations
The sharp optimization requires *exactly two retained states*, a connected finite reversible chain, strictly positive stationary masses, and the uncorrected weighted Type B projection. The bound is for one ordered cross-terminal entry; it is neither a global norm bound nor an accuracy guarantee for the exponential semigroup. Equality permits arbitrary positive rates realizing the prescribed harmonic data, but fixed graph topologies or fixed rates may give smaller coefficients. The nonlinear simplex correction is not analyzed. The proof is analytic; finite verifier experiments neither exhaust all networks nor certify novelty. An equivalent result in specialized nonnegative-projection or harmonic-extension literature may have been missed.

## References
1. S. Iwata, T. Oki and S. Sakaue, *Rate Constant Matrix Contraction Method for Stiff Master Equations with Detailed Balance*, arXiv:2312.05470v1 (2023), https://arxiv.org/html/2312.05470v1.
2. R. Hemmi, S. Iwata and T. Oki, *Fast and Numerically Stable Implementation of Rate Constant Matrix Contraction Method*, arXiv:2409.13128v1 (2024), https://arxiv.org/html/2409.13128v1.
3. F. Dörfler and F. Bullo, *Kron Reduction of Graphs with Applications to Electrical Networks*, arXiv:1102.2950 (2011), https://arxiv.org/abs/1102.2950.
