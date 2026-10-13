# Optimal two-chord infinitesimal acceleration of cycle consensus

## Finding

**Theorem (all cycle sizes and all optimal chord placements).** Let \(n\ge4\), and let \(C_n\) be the undirected cycle with vertex set \(\mathbb Z/n\mathbb Z\), unit conductances on its original edges, and Laplacian \(L_n\). A *chord* is an unordered pair of nonadjacent, distinct vertices. For a chord \(e=\{i,j\}\), choose either orientation and write \(b_e=e_i-e_j\). Choose two **distinct** chords \(e,f\), nonnegative conductance fractions \(x,1-x\) with \(0\le x\le1\), and a total new conductance budget \(\varepsilon>0\). The augmented Laplacian is

\[
 L_n(\varepsilon;e,f,x)=L_n+\varepsilon\bigl(xb_eb_e^{\mathsf T}+(1-x)b_fb_f^{\mathsf T}\bigr).
\]

Put \(\mu_n=4\sin^2(\pi/n)\). Define the global first-order optimal gain

\[
 S_n=\max_{e\ne f\,\mathrm{chords}}\ \max_{0\le x\le1}
 \lim_{\varepsilon\downarrow0}
 \frac{\lambda_2(L_n(\varepsilon;e,f,x))-\mu_n}{\varepsilon},
\]

where \(\lambda_2\) denotes the second-smallest eigenvalue. Then the complete answer is

\[
\boxed{S_n=\begin{cases}
 \dfrac4n\cos^2\!\left(\dfrac{\pi}{2n}\right)
 \left(1-\sin\!\left(\dfrac{\pi}{2n}\right)\right),&n\text{ odd},\\[6pt]
 \dfrac4n,&n\equiv0\pmod4,\\[6pt]
 \dfrac8n\,\dfrac{\cos^2(\pi/n)}{1+\cos^2(\pi/n)},&n\equiv2\pmod4.
\end{cases}}
\]

All maximizers have the following structure (rotation, reflection, and reversal of chord endpoints leave the condition unchanged):

* For odd \(n\), **both** chords have maximal cyclic separation \(\lfloor n/2\rfloor\); their projected low-frequency directions make the closest available angle to a right angle, with absolute cosine \(\sin(\pi/(2n))\); and \(x=1/2\).
* For \(4\mid n\), **both** chords are diameters, their low-frequency projections are orthogonal, and \(x=1/2\).
* For \(n\equiv2\pmod4\), **exactly one chord is a diameter** of separation \(n/2\), the other has cyclic separation \(n/2-1\), and their low-frequency projections are orthogonal. The diameter receives conductance fraction \(x=\cos^2(\pi/n)/(1+\cos^2(\pi/n))\), and the shorter chord receives \(1-x=1/(1+\cos^2(\pi/n))\).

In particular, when \(n\equiv2\pmod4\), using two longest chords is **strictly suboptimal at first order**: the optimal design shortens one chord by one cycle edge and gives that shorter chord the larger conductance fraction. For instance \(S_6=4/7\); the best pair of two diameter chords gives only \(1/3\).

For every fixed \(n\), maximization of the **actual** spectral gap over all chord pairs and conductance allocations satisfies

\[
\max_{e\ne f,\,x\in[0,1]}\lambda_2(L_n(\varepsilon;e,f,x))
 =\mu_n+\varepsilon S_n+O_n(\varepsilon^2)
 \quad(\varepsilon\downarrow0).
\]

A single added chord, however strong, leaves \(\lambda_2\) exactly at \(\mu_n\); two chords are the minimum needed for positive improvement. This is a claim about the small-budget coefficient, **not** a claim that these same placements optimize every finite budget.

## Assumptions and scope

Every graph in the theorem is a finite, simple, undirected cycle \(C_n\), with \(n\ge4\) and fixed unit original cycle conductances. Added chords are nonedges of that original cycle, are distinct, and have nonnegative conductances summing exactly to \(\varepsilon\); chord crossings are allowed. The optimization searches **all** eligible pairs and **all** real conductance fractions in \([0,1]\). No stationarity distribution, noise model, or distance-based chord price is imposed. The output is the exact first derivative at zero budget and an asymptotic formula for the optimized spectral gap, with an error constant depending on \(n\).

The cyclic separation of \(\{i,j\}\) is \(d=\min\{|i-j|,n-|i-j|\}\). It satisfies \(2\le d\le\lfloor n/2\rfloor\) for a chord. An angle between projected vectors is understood modulo sign; only its absolute cosine matters.

## Proof

**1. The two-dimensional slow eigenspace.** The Fourier eigenvalues of the cycle are \(4\sin^2(\pi k/n)\). For \(n\ge4\), \(\mu_n\) has multiplicity exactly two, with orthonormal eigenvectors

\[
 u_j=\sqrt{\frac2n}\cos\frac{2\pi j}{n},\qquad
 v_j=\sqrt{\frac2n}\sin\frac{2\pi j}{n}.
\]

Let \(P\) project onto their span. For chord \(e=\{i,j\}\), the coordinate vector of \(Pb_e\) in this basis is \(p_e=(u_i-u_j,v_i-v_j)^{\mathsf T}\). Trigonometric subtraction gives

\[
 \|p_e\|^2=\frac8n\sin^2\frac{\pi(j-i)}n,
 \qquad
 \frac{|p_e^{\mathsf T}p_f|}{\|p_e\|\|p_f\|}
 =\left|\cos\frac{\pi(i+j-k-\ell)}n\right|,
\]

where \(f=\{k,\ell\}\). Thus the projected direction is specified, modulo sign, by the sum of the two chord endpoints. By standard symmetric perturbation theory for an isolated multiple eigenvalue, the one-sided first-order splitting of \(\mu_n\) is the spectrum of

\[
 H=xp_ep_e^{\mathsf T}+(1-x)p_fp_f^{\mathsf T}.
\]

The derivative of the **smaller** split eigenvalue is \(\lambda_{\min}(H)\). The eigenvalue \(0\) remains exactly zero, and the next eigenvalue above \(\mu_n\) stays separated for sufficiently small \(\varepsilon\). Hence the derivative in the finding is exactly \(\lambda_{\min}(H)\). All chord-update matrices have operator norm at most \(2\), and the nonzero spectral separation at fixed \(n\) is positive. The associated block Schur complement or analytic spectral projector provides a bound \(O_n(\varepsilon^2)\) uniform in both selected chords and \(x\in[0,1]\). This proves the optimized small-budget expansion once the projected maximum is known.

**2. Exact two-vector optimization.** For nonzero vectors \(p,q\in\mathbb R^2\), set \(a=\|p\|^2>0\), \(b=\|q\|^2>0\), and \(c=|p^{\mathsf T}q|/(\|p\|\|q\|)\in[0,1]\). The trace and determinant of \(xpp^{\mathsf T}+(1-x)qq^{\mathsf T}\) are

\[
 T=ax+b(1-x),\qquad D=abx(1-x)(1-c^2).
\]

Its smaller eigenvalue is \((T-\sqrt{T^2-4D})/2\). Direct optimization over \(0\le x\le1\) yields

\[
 \max_x\lambda_{\min}=\frac{ab(1-c^2)}{a+b+2\sqrt{ab}\,c},\qquad
 x_*=\frac{b+\sqrt{ab}\,c}{a+b+2\sqrt{ab}\,c}
\]

(for \(c=1\) the optimum is zero and all weights tie). For \(c<1\), this maximizer is unique: \(\lambda_{\min}\) is concave in \(x\), and the displayed choice is its unique interior stationary point when \(c>0\), or the unique crossing point of the two linear eigenvalues when \(c=0\). In particular, for orthogonal vectors the optimum is \(ab/(a+b)\), and for fixed angle the optimum is nondecreasing in each squared norm (by positive-semidefinite matrix ordering).

**3. Odd cycle sizes.** Every chord satisfies \(a\le A_n=(8/n)\cos^2(\pi/(2n))\). Because each angle is \(\pi m/n\) with integral \(m\), odd \(n\) forces \(c\ge\sin(\pi/(2n))\). Using step 2 and monotonicity in the norms, any pair has optimized derivative at most \(A_n(1-\sin(\pi/(2n)))/2\). Two chords both of maximal cyclic separation achieve equality: translate one such chord by an integer \(k\) with \(2k\equiv(n-1)/2\pmod n\), which is solvable since \(n\) is odd. Their projected angles have precisely the closest possible right-angle mismatch. Their squared norms coincide and \(x=1/2\) is optimal. The equality conditions in these strict bounds give the stated classification.

**4. Sizes divisible by four.** Every chord has squared projected norm at most \(8/n\). For any pair, \(\lambda_{\min}(H)\le\operatorname{tr}(H)/2\le4/n\), with equality only when both norms are maximal, \(x=1/2\), and \(H\) is scalar. The chords \(\{0,n/2\}\) and \(\{n/4,3n/4\}\) are orthogonal projected diameters, so equality is attained and the classification follows.

**5. Sizes congruent to two modulo four.** Write \(n=2m\), with odd \(m\ge3\). Maximal chord length \(m\) gives squared norm \(A=8/n\); the next-best cyclic length \(m-1\) gives \(B=(8/n)\cos^2(\pi/n)\). Two projected chords are orthogonal exactly when their endpoint sums differ by \(m\) modulo \(n\). Since \(i+j\equiv j-i\pmod2\), and \(m\) is odd, orthogonality requires opposite length parities; **two diameters can never be orthogonal**. Hence for orthogonal pairs at least one projected squared norm is at most \(B\), and step 2 bounds their optimum by \(AB/(A+B)\). This bound is attained by a diameter \(\{0,m\}\) and a length-\(m-1\) chord \(\{(m+1)/2,(3m-1)/2\}\), whose endpoint sums differ by \(m\). Their conductance fractions follow from step 2.

For **nonorthogonal** pairs, the available endpoint-sum angles imply \(c\ge\sin(\pi/n)\). Since both projected squared norms are at most \(A\), their optimum is at most \(A(1-\sin(\pi/n))/2\). Put \(s=\sin(\pi/n)\in(0,1)\). The orthogonal long–short optimum beats this bound strictly because

\[
 \frac{1-s^2}{2-s^2}-\frac{1-s}{2}
 =\frac{s(2-s-s^2)}{2(2-s^2)}>0.
\]

Thus every optimizer is an orthogonal long–short pair, proving the value and all equality conditions.

**6. One chord is insufficient.** A single edge update has rank one when restricted to the two-dimensional slow eigenspace. Choose a nonzero slow eigenvector orthogonal to that edge vector. It remains an eigenvector with eigenvalue \(\mu_n\) after any nonnegative update. Positive-semidefinite monotonicity prevents \(\lambda_2\) from decreasing, so \(\lambda_2\) stays exactly \(\mu_n\). By contrast every displayed two-chord optimizer has positive first-order gain. This completes the proof.

## Verification

Run `python3 verify.py` using Python 3 and NumPy. The executable enumerates all unordered pairs of eligible chords for \(4\le n\le32\), optimizes the projected two-dimensional eigenvalue over the continuous conductance split using the trace/determinant formula, and compares its maximum with the three-case theorem. It separately builds trigonometric Fourier projectors, diagonalizes actual full augmented graph Laplacians for selected sizes and small budgets, and checks the one-chord no-improvement assertion on those sizes.

Recorded run: `VERIFY_OK: exhaustive_pairs=707078 chord_edges=4930 full_laplacian_spectra=54 n=4..32 all_three_residue_cases`.

These finite numerical checks test the formulas and implementation. They are **not** the proof of the all-\(n\) assertions; those follow from steps 1–6. No floating-point tolerance is used as an infinity or impossibility certificate.

## Relationship to prior work

Ghosh and Boyd (2006), *Upper Bounds on Algebraic Connectivity via Convex Optimization*, establish a generic semidefinite approach and ring-structure bounds, but do not optimize a pair of added chords in a fixed cycle. Ghosh and Boyd (2006), *Growing Well-Connected Graphs*, study generic combinatorial edge addition and observe that a multiple Fiedler eigenvalue cannot rise after a single edge is added. Their heuristic and multiplicity observation motivate, but do not supply, the three congruence-class optimizer and optimal weight fractions here. Deng, Chang, and Yang (2026) analyze a **single** chord of a weighted cycle for algebraic connectivity and coherence and explicitly identify **multiple chords** as future work; their single-chord formulas do not imply the rank-two optimal-placement result. Related optimization of all distance-two edges or of network coherence uses different feasible sets or objectives. The claim is limited to the new precise two-chord first-order optimum, not general spectral perturbation, Fourier diagonalization, or the known one-chord obstruction.

## Limitations

The characterization is first-order in the **total added conductance** at zero budget. It does not assert that the same chords or conductance fractions remain optimal when the total added budget is finite and non-small. The theorem assumes uniform unit conductance on the original cycle and equal unit price for each unit of new conductance; it does not address edge-length-dependent communication prices, preweighted cycles, directed dynamics, or large-noise coherence. A published statement equivalent to the three-case closed form might exist in literature not retrieved by the described searches; originality has been assessed from the specifically compared material and is not independently certified.

## References

1. A. Ghosh and S. Boyd, *Upper bounds on algebraic connectivity via convex optimization*, Linear Algebra and its Applications **418** (2006), 693–707. DOI: 10.1016/j.laa.2006.03.006. Public full text: https://web.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf (available online 2006-05-05).
2. A. Ghosh and S. Boyd, *Growing Well-Connected Graphs*, Proceedings of the 45th IEEE Conference on Decision and Control (2006), 6605–6611. DOI: 10.1109/CDC.2006.377282. Full text: https://web.stanford.edu/~boyd/papers/pdf/growing_fast_graphs.pdf.
3. J. Deng, L. Chang, and Q. Yang, *Single-Chord Augmentation of Weighted Cycles for Algebraic Connectivity and Network Coherence*, arXiv:2605.24479v1 (2026-05-23), https://arxiv.org/pdf/2605.24479. Single-chord scope and multiple-chord future-work statement are in the introduction and conclusion.
