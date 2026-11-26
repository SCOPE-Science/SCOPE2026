# Sharp finite-horizon quantile-Kaczmarz rates on equiangular planar tight frames

## Finding

For integers \(m\ge2\) and \(1\le r\le m\), take unit rows \(a_j=(\cos(j\pi/m),\sin(j\pi/m))\) for \(0\le j<m\) and consistent equations \(b_j=\langle a_j,x_\star\rangle\). The rank-\(r\), tie-inclusive quantile Kaczmarz step chooses uniformly among all rows whose absolute residual is at most the \(r\)-th smallest absolute residual, then projects orthogonally onto that equation.

Write
\[
Q_{m,r}=\frac12+\frac{\sin(\pi r/m)}{2r\sin(\pi/m)},\qquad
B_{m,r}=\begin{cases}Q_{m,r+1},&r<m\text{ and }r\text{ is even},\\ Q_{m,r},&r\text{ is odd or }r=m.\end{cases}
\]
For arbitrary deterministic \(x_0\), set \(e_k=x_k-x_\star\). For every integer \(k\ge1\),
\[
\mathbb E\|e_k\|_2^2=B_{m,r}^{k-1}\mathbb E\|e_1\|_2^2,\qquad
\sup_{e_0\ne0}\frac{\mathbb E\|e_k\|_2^2}{\|e_0\|_2^2}=Q_{m,r}B_{m,r}^{k-1}.
\]
The supremum is attained when the line perpendicular to \(e_0\) bisects a block of \(r\) consecutive frame lines, and for all initial directions if \(r=m\).

At a **nonzero** error after the first projection the retained set has \(r+1\) rows if \(r<m\) is even, and \(r\) otherwise. At zero error, **all \(m\) rows are admitted** and every update is zero. The conditional squared-error identity with factor \(B_{m,r}\) holds in both cases.

The frame is perfectly conditioned: \(A^{\mathsf T}A=(m/2)I_2\). For fixed rank \(r\ge2\), the one-step contraction gaps \(1-Q_{m,r}\) and \(1-B_{m,r}\) are of order \(m^{-2}\). At rank one a nonzero initial error stays nonzero and becomes stationary after at most one projection. At ranks \(r\ge2\) the iterates converge almost surely to the unique solution.

## Assumptions and scope

All objects are real; the state is two-dimensional, with the stated equispaced projective lines and exact consistency. The residual order statistic uses all rows at every step, with every cutoff tie included and a fresh uniform draw from that set. The implementation is one orthogonal projection \(x_{k+1}=x_k+(b_J-\langle a_J,x_k\rangle)a_J\), not an accept/reject proposal with idle iterations. Arithmetic and ties are exact, with no corruption, noise, subsampling, or overrelaxation. The rows span the plane, so the solution is unique.

## Proof

For nonzero error \(e\) let \(\phi\) be the angle modulo \(\pi\) of the line \(e^\perp\). The normalized squared residual at row \(j\) is \(\sin^2(\phi-j\pi/m)\); it is increasing in projective angular distance on \([0,\pi/2]\). A choice of the \(r\) nearest rows (with any cutoff tie resolved by extending at one end) is a consecutive circular block. The geometric series of doubled angles gives for any block starting at \(s\)
\[
\frac1r\sum_{\ell=0}^{r-1}\sin^2(\phi-(s+\ell)\pi/m)
=\frac12-\frac{\sin(\pi r/m)}{2r\sin(\pi/m)}
\cos(2\phi-(2s+r-1)\pi/m).
\]
The block average is at least \(1-Q_{m,r}\); adding further tied cutoff rows cannot decrease it. Pythagoras gives \(\|e-\langle a_J,e\rangle a_J\|^2=\|e\|^2-|\langle a_J,e\rangle|^2\), so the one-step conditional expected energy is at most \(Q_{m,r}\|e\|^2\). When \(r<m\), the block midpoint gives strictly smaller angular distance to all \(r\) block rows than to any outside the block and makes the cosine 1. For \(r=m\) the sine coefficient is zero and the average is independent of orientation. This proves the sharp first-step factor.

After a projection the error is perpendicular to the chosen row. If it is nonzero, its perpendicular line is therefore on the grid. The grid has one row at distance zero, pairs at successive positive distances, and, if \(m\) is even, a single row at distance \(\pi/2\) ranked last. Thus for \(r<m\) the tie-inclusive cutoff ends at size \(r\) for odd \(r\), and size \(r+1\) for even \(r\). The retained rows form a symmetric block, so the displayed average attains its centered-block value; for the full set the average is \(1/2\). At \(e=0\) the set instead has size \(m\) for every \(r\), and zero is absorbing. Consequently, for every \(k\ge1\),
\[
\mathbb E[\|e_{k+1}\|^2\mid e_k]=B_{m,r}\|e_k\|^2.
\]
Iteration and the already sharp first-step bound prove both horizon claims.

At rank one the chosen row cannot be parallel to a nonzero error, since any other row would have a strictly smaller residual. Thus the first projection does not annihilate the error, and thereafter precisely the just-enforced row has minimum residual zero. At rank \(r\ge2\) the conditional average removal at nonzero grid-aligned perpendicular error includes at least one strictly positive squared residual, so \(B_{m,r}<1\). The expected squared error tends to zero, and pathwise squared error is nonincreasing. Bounded convergence then gives zero limit almost surely.

For fixed \(r\ge2\), the sine Taylor expansion gives
\[
1-Q_{m,r}=\frac{\pi^2(r^2-1)}{12m^2}+O(m^{-4}).
\]
For fixed even \(r\), \(1-B_{m,r}=\pi^2r(r+2)/(12m^2)+O(m^{-4})\); for fixed odd \(r\) it equals \(1-Q_{m,r}\). If \(r/m\to q\in(0,1]\), both factors converge to \(\frac12+\sin(\pi q)/(2\pi q)\). Finally, summing the matrices \(a_ja_j^{\mathsf T}\) gives \((m/2)I_2\) by the vanishing sum of doubled-angle roots of unity. In particular full-rank selection \(r=m\) has squared-error contraction factor \(1/2\), unlike the slow fixed-rank quantile regime.

## Verification

The frozen companion `verify.py` uses the Python standard library to construct rows, apply projections with a numerical cutoff tolerance, enumerate transition energies through four updates, and check the first-step, post-step, horizon and scaling formulas. Its recorded output contains 39,420 checks. These are finite floating-point consistency tests, not a proof or a certificate of exact ties. The all-parameter proof is the one above; at zero error the retained count follows directly from the cutoff, not from numerical testing.

## Relationship to prior work

Steinerberger's formulation already selects uniformly from all rows at or below the empirical quantile. Lok–Rebrova and Coria–Haddock–Pacheco study related subspace or noisy formulations. Coria–Haddock–Pacheco distinguish implementations with rejected proposals from the conditional admitted-row sampling rule used here. For uniform fixed row sampling on this tight frame, the \(2^{-k}\) law is already a special case of exact planar randomized Kaczmarz analyses; it is not asserted as new. The specific contribution is the sharp finite-horizon law for adaptive \(r<m\), including the change of multiplier after the first projection and its even/odd cutoff dependence. General slowdown of small-residual selection, the planar trigonometric sum, and the projection identity are not claimed as new.

## Limitations

The result does not treat irregular frames, noisy or inconsistent measurements, corruption, arithmetic rounding, subsampled quantiles or different tie-breaking. The worst-initialization rate and parity are specific to the stated selection rule; this is not an algorithmic optimality claim. Older geometric projection results may offer alternative formulations or proofs.

## References

1. J. Lok and E. Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889.
2. S. Steinerberger, *Quantile-based Random Kaczmarz for corrupted linear systems of equations*, *Information and Inference*, doi:10.1093/imaiai/iaab029; arXiv:2107.05554.
3. N. Coria, J. Haddock and J. Pacheco, *On Quantile Randomized Kaczmarz for Linear Systems with Time-Varying Noise and Corruption*, arXiv:2403.19874.
4. *Planar coincidence theorem for optimal randomized Kaczmarz sampling*, published Resultary finding, 54597ea58934.
