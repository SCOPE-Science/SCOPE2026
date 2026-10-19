# Logarithmic-mean phase diagram and sharp condition-number gap for rank-one Bregman preconditioning

## Finding

Fix a real dimension \(n\ge3\) and an unpreconditioned spectral condition number \(K>1\). The positive-definite family
\[
S=S_{K,t}=\operatorname{diag}(t/K,\underbrace{1,\ldots,1}_{n-2},t),\qquad 1<t<K,
\]
models an approximate-factorization preconditioner with identity base and one positive and one negative relative spectral defect. Among **all** symmetric positive-definite rank-one updates \(P=I+W\succ0\) with \(\operatorname{rank}W\le1\), not just diagonal updates, the best achievable spectral condition number is
\[
\kappa_*(K,t)=\min\{t,K/t\}.
\]
Two candidate updates attain the two branches: \(P_- =\operatorname{diag}(t/K,1,\ldots,1)\) gives condition number \(t\), while \(P_+=\operatorname{diag}(1,\ldots,1,t)\) gives \(K/t\).

Define the log-determinant Bregman divergence on positive-definite matrices by
\[
D(X,Y)=\operatorname{tr}(XY^{-1})-\log\det(XY^{-1})-n.
\]
Let \(P_F\) minimize \(D(S,P)\) (forward direction) and \(P_R\) minimize \(D(P,S)\) (reverse direction) over the full admissible rank-one class. At non-tied parameters the minimizers are unique. Writing
\[
L_K=\frac{K-1}{\log K},\qquad T_F=\frac{K}{L_K},\qquad T_C=\sqrt K,\qquad T_R=L_K,
\]
we have the strict ordering
\[
1<T_F<T_C<T_R<K.
\]
The full selection and condition-number phase diagram, away from the three boundaries, is:

| Parameter range | Forward Bregman choice | Reverse Bregman choice | Best spectral choice |
| --- | --- | --- | --- |
| \(1<t<T_F\) | \(P_-\) | \(P_-\) | \(P_-\) |
| \(T_F<t<T_C\) | \(P_+\) | \(P_-\) | \(P_-\) |
| \(T_C<t<T_R\) | \(P_+\) | \(P_-\) | \(P_+\) |
| \(T_R<t<K\) | \(P_+\) | \(P_+\) | \(P_+\) |

Consequently **both orientations**, individually, have the same exact sharp worst-case ratio between their spectral condition number and the **globally optimal rank-one condition number**, when \(K\) is held fixed and \(t\) varies away from ties:
\[
\boxed{\sup_{t\in(1,K)\setminus\{T_F,T_R\}} \frac{\kappa(P_F^{-1/2}SP_F^{-1/2})}{\kappa_*(K,t)}
=\sup_{t\in(1,K)\setminus\{T_F,T_R\}} \frac{\kappa(P_R^{-1/2}SP_R^{-1/2})}{\kappa_*(K,t)}
=\frac{(K-1)^2}{K(\log K)^2}.}
\]
This is a supremum, approached as \(t\downarrow T_F\) for the forward objective and as \(t\uparrow T_R\) for the reverse objective. It grows as \(K/(\log K)^2\) for \(K\to\infty\). Thus optimizing either Bregman direction can be arbitrarily suboptimal for spectral conditioning, despite both optimizing their stated divergence exactly.

## Assumptions and scope

All matrices are real symmetric; \(n\ge3\), \(K>1\), \(1<t<K\), and the base approximate factorization is \(I\). The update \(W\) may be indefinite in the sense that either sign of its sole nonzero eigenvalue is allowed; \(P=I+W\) must be strictly positive definite. The two Bregman objectives are minimized globally over this set, including noncommuting rank-one updates. The condition number is the ratio of extreme eigenvalues of the symmetric preconditioned operator \(P^{-1/2}SP^{-1/2}\). Equal-score endpoints admit tied Bregman optimizers: \(P_F\) is nonunique at \(t=T_F\), and \(P_R\) at \(t=T_R\). At \(t=T_C\) the two candidate preconditioners have equal, globally minimal spectral condition number.

The dimension restriction matters: with two diagonal eigenvalues, a rank-one update can exactly match one of them and make the two remaining generalized eigenvalues equal by a scaling choice. The theorem does not assert any particular conjugate-gradient iteration count, finite-precision effect, or gain in wall-clock time.

## Proof

**Step 1: global Bregman minimizers.** Every nonzero symmetric rank-one update is \(W=\alpha uu^{\mathsf T}\), with \(\|u\|=1\) and \(\alpha>-1\). Sherman–Morrison gives
\[
P^{-1}=I-\frac{\alpha}{1+\alpha}uu^{\mathsf T},\qquad \log\det P=\log(1+\alpha).
\]
Thus, up to terms independent of \(\alpha,u\),
\[
D(S,P)= -\frac{\alpha}{1+\alpha}u^{\mathsf T}Su +\log(1+\alpha)+\text{constant},
\]
\[
D(P,S)=\alpha u^{\mathsf T}S^{-1}u-\log(1+\alpha)+\text{constant}.
\]
For \(\alpha>0\), the first expression is minimized at an eigenvector of the **largest** eigenvalue \(t\), as is the second, since that vector minimizes the inverse Rayleigh quotient. For \(-1<\alpha<0\), both are minimized at an eigenvector of the **smallest** eigenvalue \(\delta=t/K\). The extreme eigenvalues are simple. With a selected eigenvalue \(s\), putting \(q=1+\alpha>0\), the variable part is \(s/q+\log q\) in the forward case and \(q/s-\log q\) in the reverse case. Their derivatives vanish uniquely at \(q=s\); global optimality follows from the derivative sign on \(q>0\). Hence exactly \(P_+\) and \(P_-\) remain as Bregman candidates. The rank-zero update is strictly worse since both extreme eigenvalues differ from \(1\).

The scalar divergence costs of **leaving a mode \(s\) uncorrected** are
\[
A(s)=s-1-\log s,\qquad B(s)=s^{-1}-1+\log s.
\]
Correcting one mode leaves the cost of the other. Therefore \(P_F=P_+\) precisely when \(A(t)>A(\delta)\), equivalent to
\[
(1-K^{-1})t-\log K>0\quad\Longleftrightarrow\quad t>T_F.
\]
Likewise \(P_R=P_+\) precisely when \(B(t)>B(\delta)\), equivalent to
\[
\log K-(K-1)/t>0\quad\Longleftrightarrow\quad t>T_R.
\]
These equalities also give the tie conventions.

**Step 2: optimal spectral conditioning over arbitrary rank-one updates.** The spectrum of \(P^{-1/2}SP^{-1/2}\) equals that of
\[
H=S^{1/2}P^{-1}S^{1/2}=S-\frac{\alpha}{1+\alpha}(S^{1/2}u)(S^{1/2}u)^{\mathsf T}.
\]
If \(\alpha>0\), the perturbation of \(S\) is negative semidefinite of rank one. By one-rank interlacing, \(\lambda_{\max}(H)\ge\lambda_2(S)=1\); by Loewner monotonicity, \(\lambda_{\min}(H)\le\lambda_{\min}(S)=\delta\). Thus its condition number is at least \(1/\delta=K/t\). If \(-1<\alpha<0\), the perturbation is positive semidefinite of rank one: \(\lambda_{\max}(H)\ge t\) and interlacing gives \(\lambda_{\min}(H)\le\lambda_{n-1}(S)=1\). Therefore its condition number is at least \(t\). For \(\alpha=0\), the condition number is \(K\). The explicit candidates realize respectively \(K/t\) and \(t\), proving \(\kappa_*=\min(t,K/t)\) without any assumption that candidate updates commute with \(S\).

**Step 3: ordering and sharp gap.** Writing \(h=\tfrac12\log K>0\) gives \(L_K/\sqrt K=\sinh(h)/h>1\). Elementary inequalities \(\log K<K-1\) and \(\log K>1-K^{-1}\) yield \(1<T_F\) and \(T_R<K\). Thus \(1<T_F<\sqrt K<T_R<K\). Comparing \(t\) and \(K/t\) selects the globally best preconditioner at \(t=\sqrt K\), establishing the phase diagram.

Within the forward-only mismatch interval \(T_F<t<\sqrt K\), the exact ratio is \(K/t^2\), decreasing in \(t\); everywhere else it is one. Within the reverse-only mismatch interval \(\sqrt K<t<T_R\), the exact ratio is \(t^2/K\), increasing in \(t\); elsewhere it is one. Both sharp suprema are therefore
\[
\frac{K}{T_F^2}=\frac{T_R^2}{K}=\frac{(K-1)^2}{K(\log K)^2}
=\left(\frac{\sinh h}{h}\right)^2.
\]
The asymptotic \(K/(\log K)^2\) follows directly. All steps are exact in every specified dimension.

## Verification

The accompanying standalone \(\texttt{verify.py}\) numerically checks the threshold ordering and scalar scores, directly constructs the two diagonal preconditioned systems, and samples general noncommuting real rank-one updates of both signs. It runs 9,093 seeded checks, including comparisons against the global condition-number lower bound and global Bregman lower bounds. The exact sharp bound for all infinitely many admissible updates follows from interlacing and the scalar minimization arguments above, not these finite checks. Run with \(\texttt{python verify.py}\) and NumPy; the expected result is stored in \(\texttt{verification_output.txt}\).

## Relationship to prior work

Bock and Andersen's *A New Matrix Truncation Method for Improving Approximate Factorisation Preconditioners* (first public 2023-12-11, arXiv:2312.06417; published in 2025) supplies the forward and reverse Bregman low-rank objectives and their spectral mode selection. Those source formulas, the definitions of the divergences, and their principal-direction optimality are credited rather than claimed new. Their detailed discussion and numerical tables compare PCG iterations and condition numbers but do not give this fixed-\(K\) sharp rank-one competitive ratio, its logarithmic-mean threshold separation, or an all-rank-one spectral comparator for the indefinite-error case.

Bock and Andersen's earlier *Preconditioner Design via the Bregman Divergence* (arXiv:2304.12162) proves a condition-number optimality statement under **positive-semidefinite** relative error and a nontrivial kernel, excluding the mixed-sign spectrum treated here. Their later *Connecting Kaporin's condition number and the Bregman log determinant divergence* (arXiv:2503.22286) concerns Kaporin's determinant/trace-type condition measure, which is not the extreme-eigenvalue ratio proved here; only its abstract was available for this comparison. Search of related published mathematical records did not reveal a full-spectrum result implying the sharp fixed-\(K\) phase diagram. Lack of a matching search result is not itself a proof of originality.

## Limitations

The theorem holds for the indicated three-eigenvalue family (with repeated unit eigenvalues), one rank-one correction, and exact arithmetic. It is not a universal lower bound for arbitrary preconditioner classes or a statement about realized PCG iteration counts. At divergence ties the choice among global divergence minimizers affects the reported spectral condition number; the sharp competitive ratios explicitly use the unique-minimizer ranges. The geometric all-rank-one lower bound uses \(n\ge3\). Possible equivalent spectral formulations in earlier matrix-nearness or preconditioning literature remain a residual originality risk; the later Kaporin paper was available by abstract only.

## References

1. Andreas A. Bock and Martin S. Andersen, *A New Matrix Truncation Method for Improving Approximate Factorisation Preconditioners*, arXiv:2312.06417v1, 2023-12-11; *Numerical Linear Algebra with Applications*, 2025, DOI: 10.1002/nla.70012. https://arxiv.org/html/2312.06417v3 ; https://doi.org/10.1002/nla.70012
2. Andreas Bock and Martin S. Andersen, *Preconditioner Design via the Bregman Divergence*, arXiv:2304.12162, first submitted 2023-04-24. https://arxiv.org/html/2304.12162v7
3. Andreas A. Bock and Martin S. Andersen, *Connecting Kaporin's condition number and the Bregman log determinant divergence*, arXiv:2503.22286. https://arxiv.org/abs/2503.22286
