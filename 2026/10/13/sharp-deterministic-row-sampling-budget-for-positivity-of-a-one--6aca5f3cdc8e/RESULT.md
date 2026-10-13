# Sharp deterministic row-sampling budget for positivity of a one-vector sketched Ritz value

## Finding

A row-subset sketch of a one-dimensional Rayleigh–Ritz problem can produce a negative approximate eigenvalue for a positive-definite matrix, even when the selected rows maximize the sampled norm of the trial vector. The exact worst-case interval, the optimal deterministic selection rule at every budget, and the sharp positivity threshold are as follows.

Fix integers \(n\ge 2\) and \(1\le s\le n\), and constants \(0<\mu<L\). For a unit vector \(v\in\mathbb R^n\), let \(J\subseteq\{1,\ldots,n\}\) contain \(s\) coordinates and let \(P_J\) denote the corresponding diagonal orthogonal projector. Assume \(a=\|P_Jv\|_2>0\). For \(\mu I\preceq A\preceq LI\), the one-vector sketched Ritz value is

\[
\widehat\lambda_J(A,v)=\frac{v^{\mathsf T}P_JAv}{v^{\mathsf T}P_Jv}.
\]

Writing \(c=(L+\mu)/2\) and \(\delta=(L-\mu)/2\), the **exact interval of attainable values over all such real symmetric matrices** is

\[
\boxed{\left[c-\frac{\delta}{a},\;c+\frac{\delta}{a}\right].}
\]

Both endpoints are attained by real positive-definite matrices with smallest eigenvalue \(\mu\) and largest eigenvalue \(L\).

Let \(J_{\rm top}(v)\) select the \(s\) coordinates of largest \(|v_i|\), breaking ties arbitrarily. Among all deterministic selection rules based only on \(v\) that always select \(s\) coordinates with nonzero sampled norm, this rule minimizes the worst possible deviation from the midpoint of the spectral interval, and the precise minimax value is

\[
\boxed{\inf_{J(\cdot)}\;\sup_{\|v\|_2=1}\;\sup_{\mu I\preceq A\preceq LI}
|\widehat\lambda_{J(v)}(A,v)-c|=\delta\sqrt{n/s}.}
\]

In particular, for every \(1\le s<n\), put \(q=\sqrt{n/s}\) and \(\kappa=L/\mu>1\). With top-\(s\) row sampling, **all** approximate eigenvalues are strictly positive for **all** admissible \(v,A\) if and only if

\[
\boxed{\kappa<\frac{q+1}{q-1};}
\]

at equality there are admissible matrices and trial vectors with sketched Ritz value zero, and above the threshold negative values occur. Equivalently, the sharp sufficient-and-necessary condition is

\[
\boxed{\frac{s}{n}>\left(\frac{\kappa-1}{\kappa+1}\right)^2.}
\]

For \(s=n\), ordinary one-vector Rayleigh–Ritz is recovered and its value always belongs to \([\mu,L]\). When \(s=1\), the top-coordinate rule is precisely the one-column DEIM/Q-DEIM coordinate choice; for \(s>1\), the theorem concerns **ideal** top-\(s\) sampling, not necessarily the output of a greedy oversampling heuristic.

## Assumptions and scope

All vectors, matrices, and sketches are real and arithmetic is exact. A sketch \(S\) consists of the rows of the identity matrix indexed by \(J\); any common nonzero scaling of these rows cancels in the quotient. The symmetric input \(A\) obeys the **spectral interval** \(\mu I\preceq A\preceq LI\). The selection rule can observe \(v\) but not \(A\). For each choice of \(v\), the adversarial admissible \(A\) may depend on the selected rows. We do not assume that \(v\) is an approximate eigenvector; indeed, any unit \(v\) spans a legitimate one-step Krylov trial space.

The statement classifies the only eigenvalue of the whitened one-column sketched Rayleigh–Ritz matrix, since \((Sv)^\dagger(SAv)=(Sv)^{\mathsf T}(SAv)/\|Sv\|_2^2\). It does not address larger trial spaces, residual-based acceptance, or floating-point calculations.

## Proof

**Step 1: the exact fixed-subset extremum.** Define \(u=P_Jv/a^2\), so \(u^{\mathsf T}v=1\), \(\|u\|_2=1/a\), and

\[
\widehat\lambda_J(A,v)=u^{\mathsf T}Av=\operatorname{tr}(AQ),\qquad
Q=\tfrac12(uv^{\mathsf T}+vu^{\mathsf T}).
\]

The symmetric operator \(Q\) acts on the plane spanned by \(u,v\) and has nonzero eigenvalues (counting a possible zero when \(a=1\))

\[
\theta_+=\tfrac12(1+a^{-1}),\qquad
\theta_-=\tfrac12(1-a^{-1}).
\]

This follows either by acting on the two normalized sum/difference directions, or from \(\operatorname{tr}Q=u^{\mathsf T}v=1\) and \(\operatorname{tr}(Q^2)=(1+a^{-2})/2\). In particular \(\theta_+\ge0\ge\theta_-\).

Every admissible matrix can be written \(A=\mu I+(L-\mu)B\) with \(B=B^{\mathsf T}\) and \(0\preceq B\preceq I\). Since the extrema of \(\operatorname{tr}(BQ)\) on this operator interval are the sums of the positive and the negative eigenvalues of \(Q\), respectively,

\[
\min_A\widehat\lambda_J(A,v)=\mu+(L-\mu)\theta_-
=c-\delta/a,\quad
\max_A\widehat\lambda_J(A,v)=\mu+(L-\mu)\theta_+
=c+\delta/a.
\]

For \(0<a<1\), the minimizing and maximizing \(B\) can be chosen as the rank-one orthogonal projectors onto the negative and positive eigenvectors of \(Q\). These choices give matrices with both endpoints \(\mu,L\) in their spectra. For \(a=1\), \(u=v\) and \(Q=vv^{\mathsf T}\); taking \(A\) with \(Av=\mu v\) or \(Av=Lv\), and the other eigenvalue equal to the opposite endpoint, gives the same endpoint formulas and both spectral endpoints because \(n\ge2\). The admissible-matrix set is convex and the quotient linear in \(A\), so every intermediate scalar value is also attained.

**Step 2: the minimax row budget.** For top-\(s\) selection, \(a^2\), the sum of the largest \(s\) numbers among \(v_1^2,\ldots,v_n^2\), is at least \(s/n\) because their total is one. Thus Step 1 gives deviation at most \(\delta\sqrt{n/s}\). Conversely take the flat unit vector \(v=(1,\ldots,1)^{\mathsf T}/\sqrt n\). Every \(s\)-coordinate subset then has \(a^2=s/n\). For any deterministic rule, the endpoint matrix constructed in Step 1 for its particular output \(J(v)\) achieves deviation \(\delta\sqrt{n/s}\). Therefore no basis-only row selector can improve the uniform minimax bound. Top-\(s\) is pointwise optimal because, for a fixed \(v\), the interval radius \(\delta/a\) is minimized precisely by maximizing sampled energy \(a^2\).

**Step 3: strict positivity and the boundary.** The worst possible sketched Ritz value under top-\(s\) selection is exactly \(c-\delta\sqrt{n/s}\). For \(s<n\), this is positive exactly when

\[
(\kappa+1)-(\kappa-1)\sqrt{n/s}>0,
\]

which rearranges to the stated condition. At equality, the flat-vector negative-projector witness of Step 1 gives zero; above equality it gives a negative value. For a strictly unique top-\(s\) index set above the threshold, perturb the flat vector by making the selected \(s\) coordinates slightly larger than the others and renormalize; continuity of \(a\) and of the endpoint formula keeps the value negative. If \(s=n\), then \(a=1\) identically and ordinary Rayleigh–Ritz positivity follows.

**Concrete exact witness.** Set \(n=4\), \(s=1\), \(\mu=1\), \(L=4\), \(v=(1,1,1,1)^{\mathsf T}/2\), and \(J=\{1\}\). Define \(z=(1,-1,-1,-1)^{\mathsf T}/2\) and \(A=I+3zz^{\mathsf T}\). Then \(\|z\|_2=1\), \(A\) has spectrum \(\{1,1,1,4\}\), and direct computation gives

\[
\widehat\lambda_J(A,v)=-\tfrac12,
\]

attaining the exact lower endpoint \(5/2-(3/2)\sqrt4=-1/2\).

## Verification

A reproducible standard-library script `verify.py` checks exact identities with rational arithmetic (including rank-one projectors and endpoint matrices), tests worst-case inequalities on explicit finite families, and evaluates matrix constructions and phase boundaries numerically. Run `python3 verify.py` from the directory containing this document and the script. The script prints `VERIFY_OK` only if its assertions succeed. These finite computations corroborate the algebraic formulas; they are neither an exhaustive search over all inputs nor a replacement for the proof above.

## Relationship to prior work

Bergermann, *Deterministic sketching for Krylov subspace methods* (arXiv:2604.07158v1, publicly submitted 8 April 2026), defines deterministic row-subset sketching and one-dimensional DEIM/Q-DEIM selection, introduces oversampling, and gives the deterministically sketched Rayleigh–Ritz method in Algorithm 6. Section 6.3 explicitly discusses spurious Ritz values outside the numerical range and the empirical benefit of adding rows. **Those phenomena and the construction of the sketched method are prior work.** The present result addresses the different, precise global rank-one question: the exact attainable interval under positive-definite spectral bounds, the minimax row-budget law, and the sharp condition-number threshold for preservation of positivity.

Nakatsukasa and Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems* (arXiv:2111.00113v2), analyze sketched Rayleigh–Ritz extraction and its failure to automatically respect self-adjoint structure. Drmač and Gugercin, *A New Selection Operator for the Discrete Empirical Interpolation Method—Improved A Priori Error Bound and Extensions* (arXiv:1505.00370v2), analyze deterministic basis-dependent index selection and conditioning. Their results provide relevant background, but the stated exact spectral-interval extremum, adversarial all-vector minimax rule, and positivity boundary are not supplied by the examined passages. Standard variational/eigenvalue trace inequalities are used as proof tools and are not claimed as new.

## Limitations

The theorem concerns **only one trial vector** and uniform unweighted row selection. It assumes the row selector is permitted to use the trial vector but not the matrix itself; a selector incorporating \(A\) or exploiting additional structure is outside the minimax model. For multiple Ritz vectors, the projected matrix can have additional nonsymmetric pathologies, so the one-dimensional result must not be extrapolated to a higher-dimensional algorithm. Ideal top-\(s\) selection is not synonymous with a particular sequential oversampling implementation. A positivity criterion does not imply small eigenvalue error or small eigenpair residual. All statements are in exact arithmetic, not floating point. The relationship to older results requires independent exhaustive literature validation.

## References

1. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1 (first submitted 8 April 2026), https://arxiv.org/html/2604.07158v1, esp. §§ 4–6 and Algorithm 6.
2. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113v2, https://arxiv.org/html/2111.00113v2, esp. sketched Rayleigh–Ritz discussion.
3. Z. Drmač and S. Gugercin, *A New Selection Operator for the Discrete Empirical Interpolation Method—Improved A Priori Error Bound and Extensions*, arXiv:1505.00370v2, https://arxiv.org/html/1505.00370v2.
