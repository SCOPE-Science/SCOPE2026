# Quantitative rigidity of fastest-mixing walks on wheel graphs

## Finding

For each integer \(m\ge4\), let \(W_m=K_1\vee C_m\) have one hub \(0\) and rim vertices \(j\in\mathbb Z/m\mathbb Z\). Consider **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices \(P\) supported on the wheel edges and holding loops, without assuming any symmetry of their individual edge probabilities. Write \(\mu(P)=\|P-J\|_2\), where \(J\) is the uniform averaging matrix of order \(m+1\).

Set
\[
 u=2-2\cos(2\pi/m),\quad
 v=2-2\cos(2\pi\lfloor m/2\rfloor/m),\quad
 r=\frac{v-u}{v+u},\quad
 \mu_*=(1-1/m)r.
\]
The unique global optimizer \(P_*\) has every spoke transition probability equal to \(p_*=1/m\), every rim-edge probability equal to \(q_*=2(1-1/m)/(u+v)\), hub holding probability zero, and rim holding probability \((1-1/m)(1-4/(u+v))\). Its optimal SLEM is \(\mu_*\). **The value and symmetric optimal probabilities were previously determined by Boyd–Diaconis–Parrilo–Xiao; their recovery here is not an originality claim.**

There is also an explicit *global robustness estimate* for unrestricted, potentially inhomogeneous transitions. Given a feasible \(P\), let \(\varepsilon=\mu(P)-\mu_*\ge0\). Write \(p_j=P_{0j}\), \(q_j=P_{j,j+1}\), with indices modulo \(m\), and put
\[
 B(\varepsilon)=\varepsilon+\sqrt{2(\mu_*+\varepsilon)(1+u/v)\varepsilon},
 \qquad H(\varepsilon)=\frac{\varepsilon}{u}+\frac{2\varepsilon}{r(u+v)}.
\]
Then
\[
 \left(\frac1m\sum_j(q_j-q_*)^2\right)^{1/2}
 \le H(\varepsilon)+\frac{B(\varepsilon)}{2\sin(\pi/m)\sin(2\pi/m)}, \tag{1}
\]
and
\[
 \left(\frac1m\sum_j(p_j-p_*)^2\right)^{1/2}
 \le u\left[H(\varepsilon)+\frac{B(\varepsilon)}{2\sin(\pi/m)\sin(2\pi/m)}\right]+B(\varepsilon). \tag{2}
\]
For fixed \(m\), every edge probability of any nearly optimal chain is therefore within \(O_m(\sqrt\varepsilon)\) in root-mean-square of its prescribed optimal value; setting \(\varepsilon=0\) forces *every* spoke and rim weight, establishing uniqueness over the unrestricted feasible set. The constants in (1)–(2) are explicit but are not asserted to be sharp.

## Assumptions and scope

Edges not in the wheel have zero transition probability. Holding loops may have nonnegative weight. Symmetry of \(P\), not rotation invariance, is assumed; its stationary distribution is uniform. The problem minimizes second-largest eigenvalue modulus (spectral operator norm after subtracting uniform averaging), not total-variation mixing time, Kemeny's constant, or a nonreversible objective. The small complete-wheel case \(m=3\) is excluded because the Fourier-gap argument below uses a distinct first nonconstant rim mode.

The general parameterization is \(p_j,q_j\ge0\), \(\sum_j p_j\le1\), and \(p_j+q_{j-1}+q_j\le1\), with the holding probabilities determined by row sums. Let \(\bar p=m^{-1}\sum_jp_j\) and \(\bar q=m^{-1}\sum_jq_j\). The strict inequalities \(0<u<v\) and \(\sin(2\pi/m)>0\) hold for \(m\ge4\).

## Proof

**1. Two Fourier Rayleigh inequalities.** For each nonzero frequency \(k\), let \(f^{(k)}\) vanish at the hub and have rim components \(m^{-1/2}\exp(2\pi i k j/m)\). These unit vectors are orthogonal to constants. Since \(P\) is a weighted Laplacian subtraction from the identity,
\[
 \langle f^{(k)},P f^{(k)}\rangle
   =1-\bar p-[2-2\cos(2\pi k/m)]\bar q.
\]
At the first mode and the extreme rim mode, respectively, this gives
\[
 \mu(P)\ge\max\{1-\bar p-u\bar q,\;-(1-\bar p-v\bar q)\}.
\]
For a fixed \(\bar p\), the two affine expressions cross at \(q_0(\bar p)=2(1-\bar p)/(u+v)\), where their common value is \((1-\bar p)r\). Thus \(\mu(P)\ge(1-\bar p)r\ge(1-1/m)r=\mu_*\).

**2. Attainment and full spectral boundary.** The proposed invariant chain has \(p_*=1/m\) and \(q_*=q_0(p_*)\). Here \(u+v>4\): for even \(m\), \(v=4\) and \(u>0\); for odd \(m\ge5\), \(u+v=4+2[\cos(\pi/m)-\cos(2\pi/m)]>4\). Therefore its rim holding probability is nonnegative. Direct Fourier diagonalization gives eigenvalue \(1\) on constants, \(-1/m\) on the hub-versus-rim direction, and \(1-p_*-d_kq_*\) on nonconstant rim frequencies, where \(u\le d_k\le v\). The latter range is exactly \([-\mu_*,\mu_*]\). Also \(\mu_*\ge1/m\): when \(m\) is even, \(v=4\), \(u\le2\), so \(r\ge1/3\); when \(m\) is odd, monotonicity starting at \(m=5\) yields \(r\ge1/\sqrt5\). Hence \(\mu(P_*)=\mu_*\).

**3. Scalar stability of the averages.** Let \(\varepsilon=\mu(P)-\mu_*\). The preceding inequalities imply
\[
 0\le p_*-\bar p\le\varepsilon/r.
\]
The maximum of the two affine expressions exceeds its minimum \((1-\bar p)r\) by at least \(u|\bar q-q_0(\bar p)|\) (the other slope is \(v\ge u\)). Consequently
\[
 |\bar q-q_*|\le\varepsilon/u+2\varepsilon/[r(u+v)]=H(\varepsilon).
\]

**4. Near-null first-harmonic certificate.** Let \(f=f^{(1)}\), and \(g=f^{(\lfloor m/2\rfloor)}\). The exact identity
\[
 \langle f,Pf\rangle=(1-u/v)(1-\bar p)+(u/v)\langle g,Pg\rangle
\]
and the bounds \(\bar p\le1/m\), \(\langle g,Pg\rangle\ge-\mu(P)\) give
\[
 \langle f,Pf\rangle\ge\mu_*-(u/v)\varepsilon.
\]
Define \(M=(\mu_*+\varepsilon)I-(P-J)\). It is positive semidefinite with \(\|M\|_2\le2(\mu_*+\varepsilon)\). As \(Jf=0\),
\[
 0\le\langle f,Mf\rangle\le(1+u/v)\varepsilon,
 \qquad \|Mf\|_2^2\le\|M\|_2\langle f,Mf\rangle.
\]
Since \(P_*f=\mu_*f\), we obtain
\[
 \|(P-P_*)f\|_2
   =\|\varepsilon f-Mf\|_2\le B(\varepsilon). \tag{3}
\]
The positive-semidefinite inequality \(\|Mf\|_2^2\le\|M\|_2\langle f,Mf\rangle\) follows by diagonalizing \(M\) and bounding each squared eigenvalue by its largest eigenvalue times itself.

**5. Recovery of every individual edge.** Put \(\delta p_j=p_j-p_*\), \(\delta q_j=q_j-q_*\), and \(\theta=2\pi/m\). The rim coordinate of the residual in (3), divided by the nonzero coordinate \(f_j\), equals
\[
 (\cos\theta-1)(\delta q_{j-1}+\delta q_j)
 +i\sin\theta(\delta q_j-\delta q_{j-1})-\delta p_j.
\]
Its root-mean-square modulus is at most \(B(\varepsilon)\). Taking imaginary parts and applying the cycle Poincaré inequality
\[
 \frac1m\sum_j(z_j-\bar z)^2
 \le\frac1{4\sin^2(\pi/m)}\frac1m\sum_j(z_j-z_{j-1})^2
\]
gives
\[
 \left(\frac1m\sum_j(\delta q_j-\overline{\delta q})^2\right)^{1/2}
 \le \frac{B(\varepsilon)}{2\sin(\pi/m)\sin\theta}.
\]
Combining with \(|\overline{\delta q}|\le H(\varepsilon)\) proves (1). Taking the real parts and using \(2(1-\cos\theta)=u\), the triangle inequality and (3) gives (2). At \(\varepsilon=0\), both bounds vanish; the row sums then fix all holding probabilities, proving uniqueness.

## Verification

The companion standalone script `verify.py` reconstructs transition matrices from independent, nonidentical spoke/rim edge lists, diagonalizes each real symmetric matrix with a Jacobi rotation algorithm implemented using only the Python standard library, and checks the analytic minimum and both inequalities (1)–(2). It includes invariant optima and noninvariant perturbations close to and far from the optimum, on every rim size from 4 through 19. Running `python3 verify.py` yields `VERIFY_OK 22532 finite assertions; wheel m=4..19`. These are finite numerical corroborations with floating-point tolerances, **not** a proof for arbitrary size or infinite exact certification. All infinite-family statements above are proved analytically.

## Relationship to prior work

Boyd, Diaconis and Xiao formulated fastest mixing as a semidefinite program (2004). Boyd, Diaconis, Parrilo and Xiao derived the invariant wheel optimizer and exact SLEM in Section 5.3.3 of their 2007 preprint / 2009 journal article. Those formulas are cited as prior results. Their automorphism reduction guarantees the **existence** of a symmetric optimizer, not uniqueness among arbitrary edge assignments. The additional content here is an equality-case Fourier recovery theorem for all individual edges and an explicit global near-optimal-to-edge-distance estimate for arbitrary feasible weighted wheels.

The present conclusion concerns reversible symmetric stochastic matrices with uniform stationary distribution. A published study of spectral-gap optimization on cycles allowing inhomogeneity and nonreversibility addresses another family and a different set of assumptions; it does not yield this wheel-edge stability estimate. A public technical-report record for the main wheel source is dated May 2007 but does not specify a day. The dated arXiv v1 release of 6 September 2007 is the verified day-level source record used here.

## Limitations

The known optimum value and invariant optimal probabilities are **not** new. The explicit stability constants are not shown to be best possible, and the theorem does not cover nonreversible chains, arbitrary prescribed stationary laws, weighted wheel topology constraints, or total-variation-optimal mixing time. The check script uses floating-point finite tests. Equivalent quantitative rigidity statements could exist in specialized or incompletely indexed optimization literature.

## References

- S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264. Source: https://web.stanford.edu/~boyd/papers/fmmc.html .
- S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (6 September 2007), Section 5.3.3; SIAM Journal on Optimization 20 (2009), 792–819, DOI: 10.1137/070689413. Source: https://arxiv.org/html/0709.0955v1 .
- S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Symmetry Analysis of Reversible Markov Chains*, Internet Mathematics 2 (2005), 31–71, DOI: 10.1080/15427951.2005.10129100. Source: https://web.stanford.edu/~boyd/papers/symmetry.html .
- B. Gerencsér, J. M. Hendrickx, P. Van Dooren, *Spectral gap of Markov chains on a cycle*, European Control Conference (2015), 765–769, DOI: 10.1109/ECC.2015.7330635. Source: https://real.mtak.hu/173919/ .
