# Sharp harmonic projection constants on finite metric cycles

## Finding
Let \(n\ge3\) and let \(C_n=\mathbb Z_n\) carry the shortest-path metric with unit edge lengths. In the real Banach space \(X_n=\operatorname{Lip}_0(C_n)\), put
\[
E_{n,k}=\operatorname{span}_{\mathbb R}\left\{j\mapsto\cos\left(\frac{2\pi kj}{n}\right)-1,\quad j\mapsto\sin\left(\frac{2\pi kj}{n}\right)\right\},\qquad 1\le k\le\lfloor n/2\rfloor.
\]
Let \(\lambda(E_{n,k},X_n)\) be the infimum of the operator norms of all real linear projections from \(X_n\) onto \(E_{n,k}\), and write \(m=n/\gcd(n,k)\). The exact constant is
\[
\boxed{\lambda(E_{n,k},X_n)=\Lambda_m=\begin{cases}
1,&m=2,\\[2pt]
\dfrac2m\!\left(\csc\dfrac{\pi}{2m}-\sin\dfrac{\pi}{2m}\right),&m\ge3\ \text{odd},\\[5pt]
\dfrac4m\csc\dfrac\pi m,&m\equiv2\pmod4,\ m\ge6,\\[5pt]
\dfrac4m\cot\dfrac\pi m,&m\equiv0\pmod4.
\end{cases}}
\]
The usual real Fourier projection onto frequencies \(\pm k\) attains the infimum. In particular, \(E_{n,k}\) is contractively complemented precisely when \(m\in\{2,3,4\}\); for every larger order the optimal norm is strictly above one. As \(m\to\infty\) through integers, \(\Lambda_m\to4/\pi\). Thus the projection constant depends on the order of the character, not on the ambient cycle length separately.

## Assumptions and scope
The scalars and operators are real. For a function normalized by \(f(0)=0\), the Lipschitz norm is
\[
\|f\|_{\operatorname{Lip}}=\max_{j\in\mathbb Z_n}|f(j+1)-f(j)|.
\]
When \(n\) is even and \(k=n/2\), the sine generator is zero and \(E_{n,k}\) is one-dimensional (\(m=2\)). For all other allowed frequencies \(m\ge3\) and the subspace is two-dimensional. By "projection" we mean a bounded real linear idempotent with precisely the stated range; the infimum ranges over *all* such projections, not merely Fourier multipliers.

## Proof
**1. Exact derivative model.** Define the edge derivative by \((Df)_j=f(j+1)-f(j)\). The graph metric makes \(D\) a linear isometry from \(X_n\) onto
\[
H_n=\{g\in\mathbb R^n:\sum_{j=0}^{n-1}g_j=0\}\subset\ell_\infty^n.
\]
Every zero-sum edge array integrates to a periodic vertex function, uniquely after setting \(f(0)=0\). Rotations of the cycle act isometrically on \(X_n\) by \((R_h f)(j)=f(j+h)-f(h)\); under \(D\) they become cyclic shifts of \(H_n\).

**2. Why the Fourier projection is optimal among all projections.** For an arbitrary projection \(Q:X_n\to E_{n,k}\), average \(R_h^{-1} Q R_h\) over \(h\in\mathbb Z_n\). The average is again a projection onto \(E_{n,k}\), still fixes every element of that subspace, commutes with rotations, and has norm at most \(\|Q\|\). Complexifying the shift representation diagonalizes it into the distinct characters of \(\mathbb Z_n\). A rotation-commuting operator whose range is the real \(\pm k\) spectral subspace and which fixes that subspace has multiplier one at \(\pm k\) and zero at all other frequencies. It is therefore the unique real Fourier projection \(P_{n,k}\). Consequently \(\lambda(E_{n,k},X_n)=\|P_{n,k}\|\). For the one-dimensional alternating frequency, the Fourier projection is also a norm-one projection, directly by the median calculation below or by symmetry.

**3. Duality supplies the exact norm.** Suppose \(m\ge3\). The edge derivative of \(P_{n,k}\) is the real convolution operator on \(H_n\) with kernel
\[
K_{n,k}(r)=\frac2n\cos\left(\frac{2\pi kr}{n}\right).
\]
Since every output coordinate is a cyclic translate of the same functional,
\[
\|P_{n,k}\|=\frac2n\sup_{\substack{\|g\|_\infty\le1\\\sum_jg_j=0}}
\left|\sum_{j=0}^{n-1}\cos\left(\frac{2\pi kj}{n}\right)g_j\right|
=\frac2n\inf_{c\in\mathbb R}\sum_{j=0}^{n-1}\left|\cos\left(\frac{2\pi kj}{n}\right)-c\right|.
\]
The last equality is the finite-dimensional dual identity \(H_n^*\cong\ell_1^n/\operatorname{span}\{(1,\ldots,1)\}\); equivalently, it follows by strong linear-programming duality. A minimizing \(c\) is any median of the samples. The multiset of \(n\) cosine samples consists of \(d=\gcd(n,k)\) repetitions of the samples \(\cos(2\pi j/m)\), \(0\le j<m\). Hence
\[
\|P_{n,k}\|=\frac2m\min_{c\in\mathbb R}\sum_{j=0}^{m-1}\left|\cos\left(\frac{2\pi j}{m}\right)-c\right|.
\tag{1}
\]
For \(m=2\), the Fourier multiplier is the sign-alternating projection; its kernel on \(H_n\) has norm \(1\), as the analogous two-sample median calculation gives \(\frac12\min_c(|1-c|+|-1-c|)=1\).

**4. Evaluate the finite median sums.** When \(m\) is even, the cosine multiset is centrally symmetric and zero is a median. Elementary geometric-series identities give
\[
\sum_{j=0}^{m-1}\left|\cos\left(\frac{2\pi j}{m}\right)\right|
=\begin{cases}
2\csc(\pi/m),&m\equiv2\pmod4,\\
2\cot(\pi/m),&m\equiv0\pmod4.
\end{cases}
\]
For odd \(m\), put \(t=\lceil(m-1)/4\rceil\) and \(c=\cos(2\pi t/m)\). Exactly \(2t-1\) samples are larger than this median, two equal it, and the others are smaller. The sum of the larger samples is
\[
A=1+2\sum_{j=1}^{t-1}\cos\left(\frac{2\pi j}{m}\right)=\frac{\sin((2t-1)\pi/m)}{\sin(\pi/m)}.
\]
Because the total cosine sum vanishes, the absolute-deviation sum is \(2A+(m-4t+2)c\). Set \(u=\pi/(2m)\). If \(m=4s+1\), then \(t=s\), \(A=\cos(3u)/\sin(2u)\), and \(c=\sin u\); thus the deviation sum equals \(2\cos(3u)/\sin(2u)+3\sin u=\csc u-\sin u\). If \(m=4s+3\), then \(t=s+1\), \(A=\cos u/\sin(2u)\), and \(c=-\sin u\); it again equals \(2\cos u/\sin(2u)-\sin u=\csc u-\sin u\). Combining these identities with (1) gives the claimed closed forms.

**5. Contractivity and limiting behaviour.** For \(m=3,4\), the formulas give \(\Lambda_m=1\). For even \(m\equiv2\pmod4\) with \(m\ge6\), \(\sin(\pi/m)<\pi/m\) gives \(\Lambda_m>4/\pi>1\). For even \(m\equiv0\pmod4\) with \(m\ge8\), the function \(x\mapsto\tan x/x\) is increasing on \((0,\pi/8]\), so
\[
\tan(\pi/m)\le\frac8\pi(\sqrt2-1)\frac\pi m<\frac4m,
\]
which proves \(\Lambda_m>1\). For odd \(m\ge5\), writing \(u=\pi/(2m)\) gives \(\Lambda_m=2\cos^2u/(m\sin u)\). Here \(m\sin u<\pi/2\) while \(2\cos^2u\ge2\cos^2(\pi/10)>\pi/2\), so \(\Lambda_m>1\). Finally, \(\sin z\sim z\), \(\tan z\sim z\) yield \(\Lambda_m\to4/\pi\) in each residue class.

## Verification
The companion standalone program `verify_cycle_harmonics.py` computes the median deviation formula for every integer \(3\le m\le2000\) and independently solves the constrained linear program defining the operator norm for all \(3\le n\le64\) and \(1\le k\le\lfloor(n-1)/2\rfloor\). On the recorded execution it passed 1,998 sampled closed-form comparisons and 992 independent linear-programming instances. The program also checks the claimed contractivity boundary through order 2,000. These are corroborative numerical calculations; the all-dimensional theorem follows from the preceding proof.

## Relationship to prior work
M. Cúth and M. Doucha's *Projections in Lipschitz-free spaces induced by group actions* (arXiv:2104.11519v1) establishes complementary orbit-space and fixed-point constructions from group actions; its full text discusses invariant projections but does not determine the optimal norms of projections onto nontrivial harmonic eigenspaces. The published results *Numerical-index parity law for Lipschitz-free spaces over cycles* and *Exact three-frequency Fourier projection norm on every cyclic group* were compared in full. The first determines numerical indices of the dual Lipschitz-free spaces, which are different invariants; the second computes the endpoint convolution norm on the full \(\ell_\infty\) space for the \(\{-1,0,1\}\) spectrum, which is distinct from the zero-sum edge norm and the \(\{\pm k\}\) spectrum here. The published *Exact two-frequency \(L^1\) concentration on every cyclic group* computes a ratio for two complex-character sums, not the median-quotient real harmonic projection norm. These results motivate, but do not state or logically imply, the formula proved here.

## Limitations
All scalars are real, the metrics are unweighted unit-edge cycles, and the result concerns a single conjugate pair of Fourier frequencies (or the one-dimensional alternating frequency). No general result for multiple harmonic pairs or weighted cycles is asserted. The group-averaging principle is standard; the contribution assessed here is the sharp zero-sum Lipschitz norm, its uniform residue-class evaluation, and the exact complementability classification. Searches cannot exclude every equivalent formula in older unindexed approximation-theory literature, which is the remaining bibliographic risk. The numerical program does not certify the infinite family.

## References
1. M. Cúth and M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519v1 (first public 2021-04-23), subsequently *Mathematische Nachrichten* 296 (2023), 3301–3317, DOI 10.1002/mana.202100222.
2. *Numerical-index parity law for Lipschitz-free spaces over cycles*, publicly available research result (2026), full RESULT.md inspected.
3. *Exact three-frequency Fourier projection norm on every cyclic group*, publicly available research result (2026), full RESULT.md inspected.
4. *Exact two-frequency \(L^1\) concentration on every cyclic group*, publicly available research result (2026), full RESULT.md inspected.
