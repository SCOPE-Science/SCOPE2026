# Arithmetic resonance and finite termination of randomized reflection bundles

## Finding

For the two-row randomized \(r\)-sets Douglas–Rachford method of Han, Su and Xie, the probability-one **exact finite termination** property has a sharp arithmetic classification which depends on the parity of \(r\). The property is distinct from asymptotic or linear convergence.

Fix two distinct lines in \(\mathbb R^2\) through their common intersection, of acute angle \(0<\theta<\pi/2\). Give each defining row unit Euclidean norm. Let \(r\ge1\) be any integer and, independently at each macro-iteration, choose \(r\) rows with replacement, uniformly and independently, reflect successively across the corresponding lines, and average the result with the pre-iteration point using the exact relaxation \(\alpha=1/2\). This is Algorithm 1 of [1] with zero momentum. For every non-solution starting point, the algorithm reaches the intersection exactly in finitely many macro-iterations almost surely **if and only if**

\[
\begin{cases}
\exists d\in\{1,\ldots,r/2\}:\ \cos(d\theta)=0,&r\text{ even},\\
\exists d\in\{1,\ldots,r\}:\ \cos(d\theta)=0,&r\text{ odd}.
\end{cases}
\]

The condition means that \(\theta/\pi=a/b\), in reduced positive rational terms, has an **even** denominator \(b\); the sharp block-size thresholds are \(r\ge b\) for even \(r\), and \(r\ge b/2\) for odd \(r\). If the angle is irrational relative to \(\pi\), or has odd reduced denominator, no block size has probability-one exact finite termination. In the nonresonant case, a starting point outside finitely many explicitly described exceptional lines never reaches the solution in finite time. The smallest successful odd block size is the smallest odd integer at least \(b/2\), always strictly smaller than the smallest successful even block size \(b\).

For even \(r=2q\), the *exact* first-solution time is geometric with success probability
\[
\rho_{r,\theta}=2^{-r}\sum_{s=-q}^{q}\binom{r}{q+s}\mathbf1_{\{\cos(s\theta)=0\}}.
\]
For odd \(r=2q+1\), define \(\mathcal S=\{-q,-q+1,\ldots,q+1\}\), \(p_s=2^{-r}\binom r{q+s}\), and the substochastic matrix
\[
Q_{st}=p_t\mathbf1_{\{\cos((s-t)\theta)\ne0\}},\qquad s,t\in\mathcal S.
\]
At resonant angles, for every starting point not perpendicular to any line \(L_{s\theta}\) with \(s\in\mathcal S\), the first exact-solution index \(T\) has
\[
\Pr(T>k)=p^{\mathsf T}Q^{k-1}\mathbf1\quad(k\ge1),\qquad
\mathbb ET=1+p^{\mathsf T}(I-Q)^{-1}\mathbf1.
\]
For \(r=3\), the exact means are \(\mathbb ET=61/9\) when \(\theta=\pi/4\), and \(\mathbb ET=36\) when \(\theta=\pi/6\). At \(\theta=\pi/4\), the smallest successful even choice is \(r=4\), with mean \(8\) blocks; hence mean reflection counts are \(61/3\) for the odd three-reflection method and \(32\) for the even four-reflection method, respectively. These are exact-arithmetic counts, not finite-precision performance guarantees.

## Assumptions and scope

Let \(C_0,C_1\) be distinct affine lines in \(\mathbb R^2\) meeting at a unique point \(x^*\), whose acute line angle is \(\theta\in(0,\pi/2)\). Let their defining normals both have norm one, so the row-norm-proportional sampling in [1] chooses each with probability \(1/2\). Set \(R_i=2P_{C_i}-I\). The error after one macro-iteration of length \(r\) is
\[
e_{k+1}=\frac12\bigl(I+R_{j_r}\cdots R_{j_1}\bigr)e_k,
\]
where this displayed formula acts on translated errors \(e=x-x^*\), and every \(j_t\in\{0,1\}\) is sampled independently with probability \(1/2\), freshly at each macro-iteration. Equivalently take \(x^*=0\), \(C_0=L_0\) (the horizontal line), \(C_1=L_\theta\), where \(L_\phi=\{t(\cos\phi,\sin\phi):t\in\mathbb R\}\). Rotation/translation leaves both the algorithm and conclusions invariant. All equalities in this document concern exact real arithmetic.

Probability-one finite termination is meant **for each fixed nonzero initial error** (the random termination index need not admit a deterministic upper bound). The survival formulas for odd \(r\) assume a generic initial error outside the finite union \(\bigcup_{s\in\mathcal S}L_{s\theta}^\perp\). For an exceptional initial error, first-step annihilation may additionally occur, while the stated necessary-and-sufficient almost-sure criterion remains unchanged.

## Proof

**Reflection-product identity.** Identify the error plane with \(\mathbb C\). Reflection in \(L_{j\theta}\) is \(R_jz=e^{2ij\theta}\overline z\). For the ordered sample \((j_1,\ldots,j_r)\), write
\[
S=j_r-j_{r-1}+j_{r-2}-\cdots+(-1)^{r-1}j_1.
\]
Thus the product of \(r\) reflections maps \(z\) to \(e^{2iS\theta}z\) if \(r\) is even and \(e^{2iS\theta}\bar z\) if \(r\) is odd. Taking \(q=\lfloor r/2\rfloor\), the integer \(S\) is a difference of independent \(\operatorname{Bin}(r-q,1/2)\) and \(\operatorname{Bin}(q,1/2)\) variables. The probability-generating Laurent polynomial is
\[
\mathbb Ez^{S}=2^{-r}z^{-q}(1+z)^r,
\]
so \(\Pr(S=s)=2^{-r}\binom r{q+s}\) for each \(-q\le s\le r-q\), and every integer in that interval has positive probability.

**Even-length bundles.** If \(r=2q\), the averaged product acts as multiplication by
\[
\frac{1+e^{2iS\theta}}2=e^{iS\theta}\cos(S\theta).
\]
It is invertible on the real error plane unless \(\cos(S\theta)=0\), in which case it is identically zero. Since \(S\in\{-q,\ldots,q\}\) with positive masses, the probability of a zero update is exactly \(\rho_{r,\theta}\) in the Finding. Fresh sampling makes the first zero-update time geometric. If no support value kills, a product of invertible maps never kills any nonzero error.

**Odd-length bundles.** If \(r=2q+1\), the averaged product equals
\[
\frac12\bigl(I+R_{L_{S\theta}}\bigr)=P_{L_{S\theta}}.
\]
After the first nonzero projection, the error lies on the sampled line. The product of successive nonzero rank-one projections annihilates the error exactly when two consecutive sampled axes are perpendicular, equivalently when \(\cos((S_{k+1}-S_k)\theta)=0\). Differences between the smallest and largest available indices realize every integer in \(\{-r,\ldots,r\}\), so such a pair exists if and only if \(\cos(d\theta)=0\) for some \(1\le d\le r\). If so, choose any two such support values \(s,t\): disjoint successive pairs equal \((s,t)\) independently with probability \(p_sp_t>0\), proving almost-sure finite termination and an exponential tail. If not, every consecutive projection preserves a nonzero vector; a generic starting point also survives its first projection. For an exceptional nonzero starting point, the first step is nonzero with positive probability because \(L_0\) and \(L_\theta\) are distinct and both occur in the support. The almost-sure dichotomy follows for every nonzero start.

For the generic starting point the sampled-axis sequence is independent and identically distributed with law \(p\). Conditional on the current nonzero axis \(s\), a transition to \(t\) survives with probability \(p_t\) unless the pair is perpendicular. Consequently \(Q\) is the killed transition matrix. At resonance the survival probability in disjoint pairs decreases geometrically; hence \(\rho(Q)<1\), justifying the survival and inverse-matrix expectation formulas.

**Sharp arithmetic thresholds.** The equation \(\cos(d\theta)=0\) is equivalent to \(d\theta/\pi\in\mathbb Z+1/2\). It has an integer solution exactly when \(\theta/\pi=a/b\) in lowest terms with even \(b\) (and necessarily odd \(a\)); the least positive such \(d\) is \(b/2\). Substitution into the even and odd support conditions gives both sharp thresholds. For \(0<\theta<\pi/2\) one has \(b\ge4\), so the least successful odd length is strictly below \(b\).

**Concrete waiting times.** At \(r=3\), the sampled axes are \(s\in\{-1,0,1,2\}\) with \(p=(1,3,3,1)/8\). If \(\theta=\pi/4\), the forbidden transitions have index difference two. Solving \((I-Q)h=\mathbf1\) gives
\[
h=(40,56,56,40)/9,\qquad \mathbb ET=1+p^{\mathsf T}h=61/9.
\]
If \(\theta=\pi/6\), the forbidden transitions are only between \(-1\) and \(2\); the same exact computation gives \(h=(32,36,36,32)\) and \(\mathbb ET=36\). Finally, for \(r=4\), \(\theta=\pi/4\), only \(S=\pm2\) kills, each with binomial mass \(1/16\), yielding geometric success \(1/8\) and mean \(8\).

## Verification

Run `python -m pip install -r requirements.txt` followed by `python verify_reflection_resonance.py`. The checker independently enumerates all binary reflection words for each \(1\le r\le7\) at \(\theta=\pi/4\) and \(\theta=\pi/6\). It verifies the exact matrix composition identities and the binomial masses, using symbolic arithmetic including radicals, and computes the two rational hitting-time systems. All \(508\) word identities and the rational expectations pass. The checker does not certify the infinite or all-angle claims; those follow from the preceding algebraic and probabilistic proof.

## Relationship to prior work

Han, Su and Xie [1, Algorithm 1, Theorems 3.1 and 3.5] introduce precisely the sampled reflection bundle and prove expected-error decay and mean-iterate bounds. Their article does not state the all-length arithmetic finite-termination classification, killed-line Markov law, or the sharp parity threshold here. Its general convergence estimate does not distinguish a finite hitting time from asymptotic decay.

Bauschke and coauthors [2] determine the linear convergence rate for the fixed Douglas–Rachford operator on two subspaces and analyze the plane. Bauschke and Dao [3] obtain finite-convergence conditions for fixed two-set Douglas–Rachford problems. Dao and colleagues [4] characterize planar deterministic two-cone Douglas–Rachford finite convergence. The distinction is that [1] repeatedly draws **fresh reflection bundles** and, for odd bundle lengths, creates random *virtual axes* different from either original line; none of [2–4] yields the support arithmetic or its exact random hitting-time law. The elementary fact that orthogonal consecutive line projections annihilate a vector is an input rather than a claimed innovation.

## Limitations

The result is confined to **two** distinct consistent planar equations, independent row sampling with replacement, and the exact \(\alpha=1/2\) update without momentum. It does not assert corresponding finite termination for higher-dimensional problems, unequal relaxation, noisy equations, or finite-precision implementations. Finite termination is almost sure at resonant angles but has **unbounded random time**, not a fixed deterministic horizon. Small perturbations of an exactly resonant angle generally destroy exact termination; expected-error convergence may nonetheless persist. Bibliographic searches cannot eliminate all unindexed equivalent formulations, and independent scientific validation has not been performed.

## References

[1] D. Han, Y. Su, J. Xie, *Randomized Douglas–Rachford Methods for Linear Systems: Improved Accuracy and Efficiency*, arXiv:2207.04291 (first public submission 2022-07-09), especially Algorithm 1 and Section 3. https://arxiv.org/abs/2207.04291 ; https://arxiv.org/pdf/2207.04291 .

[2] H. H. Bauschke, J. Y. Bello Cruz, T. T. A. Nghia, H. M. Phan, X. Wang, *The rate of linear convergence of the Douglas–Rachford algorithm for subspaces is the cosine of the Friedrichs angle*, arXiv:1309.4709, Section 5. https://arxiv.org/pdf/1309.4709 .

[3] H. H. Bauschke, M. N. Dao, *On the finite convergence of the Douglas–Rachford algorithm for solving (not necessarily convex) feasibility problems in Euclidean spaces*, arXiv:1604.04657. https://arxiv.org/pdf/1604.04657 .

[4] M. N. Dao, M. Dressler, H. Liao, V. Roshchina, *Douglas–Rachford is the best projection method*, arXiv:2310.17077, Theorem 2.2. https://arxiv.org/pdf/2310.17077 .
