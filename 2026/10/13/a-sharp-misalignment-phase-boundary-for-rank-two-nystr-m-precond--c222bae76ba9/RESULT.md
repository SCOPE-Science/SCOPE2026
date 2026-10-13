# A sharp misalignment phase boundary for rank-two Nyström preconditioning

## Finding

Consider the exact rank-two Nyström preconditioner of Frangella, Tropp, and Udell for a regularized, positive-definite system. For every spectral contrast \(\kappa>1\) and every regularizer \(\eta>0\), there is a nonempty open set of rank-two sketches for a three-dimensional system that **strictly increases**, rather than decreases, the spectral condition number. Within an explicit one-parameter family, the transition between deterioration and improvement is sharp and unique.

Precisely, let \(A=\operatorname{diag}(\kappa,1,1)\), let \(T=A+\eta I_3\), and use the two-column test matrix
\[
\Omega=\begin{bmatrix}u&0\\v&0\\0&1\end{bmatrix},\qquad uv\ne0.
\]
Put
\[
t=\frac{\kappa^2u^2}{\kappa^2u^2+v^2}\in(0,1),\quad
\delta=\kappa-1,\quad a=\kappa+\eta,\quad b=1+\eta,\quad h=\kappa-\delta t,\quad H=a+b,
\]
and define the cubic polynomial
\[
G(t)=bhH(1-2t)+t(a-\delta t)^2.
\]
If \(P\) denotes the rank-two Nyström preconditioner defined below, then
\[
\boxed{\quad \operatorname{cond}_2(P^{-1/2}TP^{-1/2})>\operatorname{cond}_2(T)=\frac ab\quad\Longleftrightarrow\quad G(t)>0.\quad}
\]
For every \(\kappa>1\) and \(\eta>0\), there is exactly one \(t_*\in(0,1)\) with \(G(t_*)=0\). Consequently, every sketch with \(0<t<t_*\) strictly worsens the condition number, the value \(t=t_*\) preserves it, and every \(t_*<t<1\) strictly improves it. The endpoint \(t=0\) has \(P=I_3\) and equality, while \(t=1\) gives a perfectly conditioned system. Furthermore, a standard Gaussian \(3\)-by-\(2\) test matrix produces a strictly worse condition number with **positive probability**.

A rational example is
\[
A=\operatorname{diag}(5,3,3),\quad \eta=1,\quad
\Omega=\begin{bmatrix}1&0\\2&0\\0&1\end{bmatrix}.
\]
Here the original condition number is \(3/2\), whereas the exact preconditioned condition number equals
\[
\boxed{\quad\frac{3720+4\sqrt{42559}}{3720-4\sqrt{42559}}\;>\;\frac32,\quad}
\]
which is approximately \(1.570119803669\).

## Assumptions and scope

All matrices are real, and all formulas refer to exact arithmetic. The low-rank Nyström approximation of a positive-definite \(A\), for a full-column-rank test matrix \(\Omega\), is
\[
\widehat A=A\Omega(\Omega^\top A\Omega)^{-1}\Omega^\top A.
\]
Let \(\widehat A=U\widehat\Lambda U^\top\) be a thin eigendecomposition with \(\widehat\lambda_1\ge\widehat\lambda_2>0\). We use **the specified source preconditioner**, not the alternative \(\widehat A+\eta I\):
\[
P=\frac{1}{\widehat\lambda_2+\eta}U(\widehat\Lambda+\eta I_2)U^\top+(I_3-UU^\top).
\]
The condition number is the largest-to-smallest eigenvalue ratio of the SPD matrix \(P^{-1/2}TP^{-1/2}\). The deterministic phase law is for the displayed structured sketch and \(\kappa>1,\eta>0\). The Gaussian assertion concerns an absolutely continuous, full-support distribution on all \(3\)-by-\(2\) real test matrices; it is a positive-probability assertion, not an exact probability or expectation formula.

## Proof

**1. Exact Nyström eigendecomposition.** For the specified \(A\) and \(\Omega\), direct multiplication yields
\[
\widehat A=\frac{(\kappa u,v,0)^\top(\kappa u,v,0)}{\kappa u^2+v^2}+e_3e_3^\top
=\beta ww^\top+e_3e_3^\top,
\]
where
\[
\beta=\frac{\kappa^2u^2+v^2}{\kappa u^2+v^2}=\frac{\kappa}{h}>1,\qquad
w=\frac{(\kappa u,v,0)^\top}{\sqrt{\kappa^2u^2+v^2}}.
\]
The nonzero eigenvalues are \(\beta\) and \(1\), and \(w\perp e_3\). Thus \(\widehat\lambda_2=1\), the defining normalization is well-defined without eigenvalue ties, and
\[
P=I_3+sww^\top,\qquad s=\frac{\beta-1}{1+\eta}=\frac{\delta t}{bh}>0.
\]
On the first two coordinates, \(w\) has squared components \(t,1-t\); their relative sign has no effect on the ensuing eigenvalues.

**2. Eigenvalue location and trace-determinant reduction.** Let \(P_2\) be the upper-left \(2\)-by-\(2\) block of \(P\). Then
\[
\det P_2=1+s,\quad
\det\!\left(\begin{bmatrix}a&0\\0&b\end{bmatrix}-zP_2\right)
=ab-Sz+(1+s)z^2,
\]
where \(S=H+s(a-\delta t)\). Let the two positive generalized eigenvalues be \(\lambda_-<\lambda_+\). At \(z=b\), the displayed determinant is
\[
-b s\delta(1-t)<0,
\]
so \(\lambda_-<b<\lambda_+\). The third preconditioned eigenvalue is exactly \(b\), since \(P e_3=e_3\); the full condition number therefore equals \(r=\lambda_+/\lambda_-\). We have
\[
\lambda_++\lambda_-=\frac{S}{1+s},\quad
\lambda_+\lambda_-=\frac{ab}{1+s},\quad
r+2+r^{-1}=\frac{S^2}{ab(1+s)}.
\]
The function \(r\mapsto r+2+r^{-1}\) is strictly increasing for \(r>1\). Since \((a/b)+2+(b/a)=H^2/(ab)\), it follows that
\[
 r>\frac ab\quad\Longleftrightarrow\quad S^2>H^2(1+s).
\]
Expansion, **without dropping any positive factor**, gives the identity
\[
S^2-H^2(1+s)
=\frac{s\delta}{bh}\left[bhH(1-2t)+t(a-\delta t)^2\right]
=\frac{s\delta}{bh}G(t).
\]
Since \(s,\delta,b,h\) are positive in the interior, this proves the stated sharp sign test. The sign of the strict comparison is unchanged under simultaneous positive scaling of \(A\) and \(\eta\).

**3. A unique phase boundary.** Direct evaluation yields \(G(0)=b\kappa H>0\) and \(G(1)=-ab<0\). Its second derivative is
\[
G''(t)=4\delta(bH-a)+6\delta^2t>0\quad(0\le t\le1),
\]
because \(bH-a=1+\kappa\eta+2\eta+2\eta^2>0\). A strictly convex continuous function that starts positive and ends negative crosses zero exactly once in this interval: two interior crossings would require positive values after the second crossing, contradicting \(G(1)<0\). The endpoint \(t=0\) has \(s=0\), so the strict-sign equivalence there is not asserted; \(t=1\) gives \(P=\operatorname{diag}(a/b,1,1)\) and \(P^{-1/2}TP^{-1/2}=bI_3\).

**4. Exact rational witness.** For the displayed unnormalized witness, straightforward rational arithmetic gives
\[
\widehat A=
\begin{bmatrix}25/17&30/17&0\\30/17&36/17&0\\0&0&3\end{bmatrix},\qquad
P=\begin{bmatrix}
2199/2074&75/1037&0\\
75/1037&1127/1037&0\\
0&0&1
\end{bmatrix}.
\]
Its Nyström eigenvalues are \(61/17>3\), and
\[
\det\!\left(\operatorname{diag}(6,4,4)-zP\right)
=-\frac{3}{2074}(z-4)(793z^2-7440z+16592).
\]
The other two generalized eigenvalues are \((3720\pm4\sqrt{42559})/793\), strictly straddling \(4\). Their ratio exceeds \(3/2\): indeed, with \(S=11160/1037\) and \(\det P_2=39/34\),
\[
S^2-100\det P_2=\frac{1194450}{1075369}>0.
\]
By step 2 this rational positivity is equivalent to the strict condition-number comparison.

**5. Robustness and smallest dimension.** The determinant and ordered eigenvalues depend continuously on \(\Omega\) near the displayed full-column-rank witness, and the Nyström nonzero eigengap \(61/17-3\) is positive. Thus strict deterioration holds on an open neighborhood of that matrix. More generally, for each fixed \(\kappa>1\) and \(\eta>0\), choose \(t\in(0,t_*)\), set \(u=\sqrt t/\kappa\) and \(v=\sqrt{1-t}\), and use the corresponding full-rank structured sketch; its Nyström eigenvalues are distinct, and the same continuity argument supplies a nonempty open deterioration neighborhood. A standard Gaussian sketch has a strictly positive density everywhere, so each such event has positive probability. In dimensions at most two with a strictly positive-definite matrix and any admissible sketch rank, a rank-one Nyström approximation produces \(P=I\); a full-rank approximation reproduces \(A\), producing a scalar preconditioned system. Consequently, dimension three and sketch rank two are the smallest possible dimensions/rank permitting strict worsening with this preconditioner.

## Verification

The self-contained file `verify.py` uses only Python's standard library. Run `python verify.py` beside this document to reproduce the exact Nyström matrix, preconditioner, characteristic polynomial, and rational strict-inequality certificate; it also checks the decisive identity on 210 rational parameter triples. The general positivity, uniqueness, and Gaussian positive-probability statements follow from steps 1–5, **not** from finite numerical testing.

## Relationship to prior work

Frangella, Tropp, and Udell [1] define exactly this preconditioner (equations (1.2)–(1.3)), and Proposition 5.3 bounds its condition number deterministically in terms of the Nyström approximation error. Their Theorem 5.1 gives expected conditioning guarantees at a sufficiently large effective-dimension-based sketch rank. Neither of those estimates decides, for the explicit three-dimensional contrast family, whether an arbitrary rank-two sketch improves or deteriorates the *original* condition number. The theorem here is a sharp sign classification for that previously unaddressed comparison and does not contradict their sufficient guarantees.

Carson and Daužickaitė [2] extend Nyström preconditioner bounds to mixed precision, and their numerical study notes that conditioning improves with an appropriate sketch rank. That finite-precision and large-rank analysis does not determine this exact orientation transition in the original, exact-arithmetic preconditioner. Bock and Andersen [3] study Bregman-optimal low-rank preconditioners and Nyström approximations of their factors; the associated preconditioner is not the smallest-Nyström-eigenvalue-normalized operator analyzed here. No claim is made that general spectral deterioration from inaccurate eigenvectors is unknown; the new statement is the complete explicit threshold and minimal-dimension positive-probability obstruction for the specified algorithm.

## Limitations

The exact phase law covers a one-spike three-dimensional SPD matrix and the specified rank-two sketch subfamily, not all SPD matrices or sketches. The Gaussian conclusion establishes positive probability, not the probability's magnitude. This is an exact-arithmetic condition-number result, not a theorem about individual PCG iteration counts or finite-precision errors; a larger condition number need not imply slower convergence on every right-hand side. Published large-sketch and expectation guarantees remain applicable under their stated hypotheses. The literature comparison cannot exclude every unindexed specialized result.

## References

[1] Z. Frangella, J. A. Tropp, and M. Udell, *Randomized Nyström Preconditioning*, arXiv:2110.02820 (first publicly posted 2021-10-06), SIAM J. Matrix Anal. Appl. 44 (2023), 718–752, DOI: 10.1137/21M1466244. https://arxiv.org/pdf/2110.02820

[2] E. Carson and I. Daužickaitė, *Single-Pass Nyström Approximation in Mixed Precision*, SIAM J. Matrix Anal. Appl. 45 (2024), 1361–1391, DOI: 10.1137/22M154079X. https://epubs.siam.org/doi/full/10.1137/22M154079X

[3] A. Bock and M. S. Andersen, *Preconditioner Design via the Bregman Divergence*, arXiv:2304.12162 (2023). https://arxiv.org/pdf/2304.12162
