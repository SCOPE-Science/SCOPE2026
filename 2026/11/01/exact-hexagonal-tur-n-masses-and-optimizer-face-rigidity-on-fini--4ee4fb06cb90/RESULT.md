# Exact hexagonal Turán masses and optimizer-face rigidity on finite square tori

## Finding
For every integer \(N\ge5\), let \(G_N=(\mathbb Z/N\mathbb Z)^2\) and let
\[
\Omega=\{0,\pm e_1,\pm e_2,\pm(e_1-e_2)\}.
\]
Define the counting-measure Turán mass
\[
\mathcal T_N=\max\left\{\sum_{g\in G_N}f(g): f(0)=1,\ \operatorname{supp}f\subseteq\Omega,\ f\text{ positive definite on }G_N\right\}.
\]
Set \(q=\lfloor N/3\rfloor\) and
\[
\sigma_N=\begin{cases}
-3/2,&N=3q,\\
2\cos(2\pi q/N)+\cos(2\pi(q+1)/N),&N=3q+1,\\
\cos(2\pi q/N)+2\cos(2\pi(q+1)/N),&N=3q+2.
\end{cases}
\]
Then \(\sigma_N<0\) and the **exact sharp mass** is
\[
\boxed{\mathcal T_N=1-\frac3{\sigma_N}.}
\]
In particular, \(\mathcal T_N=3\) exactly when \(3\mid N\); otherwise \(\mathcal T_N>3\). The automorphism-invariant optimizer is
\[
f_*(0)=1,\qquad f_*(v)=-\frac{1}{2\sigma_N}\quad(v\in\Omega\setminus\{0\}),\qquad f_*(v)=0\quad(v\notin\Omega).
\]
**Optimizer-face rigidity.** When \(3\nmid N\), this is the **unique optimizer among all complex-valued admissible functions**, without assuming evenness or rotational symmetry. When \(3\mid N\), every optimizer is determined by three complex numbers \(f(e_j)=a_j+i b_j\), with \(e_3=e_1-e_2\), satisfying
\[
a_1+a_2+a_3=1,\qquad b_1-b_2-b_3=0,
\]
and all the remaining explicit Fourier nonnegativity inequalities. This complete optimizer face has relative affine dimension exactly four.

There is also a residue-sensitive asymptotic law along \(3\nmid N\):
\[
\boxed{\mathcal T_N=3+\frac{8\pi^2}{9N^2}+\varepsilon_N\frac{16\sqrt3\pi^3}{81N^3}+O(N^{-4}),}
\]
where \(\varepsilon_N=1\) when \(N\equiv1\pmod3\) and \(\varepsilon_N=-1\) when \(N\equiv2\pmod3\).

## Assumptions and scope
All assertions hold for **every integer \(N\ge5\)**, so the seven points of \(\Omega\) are distinct. Positive definiteness is the usual finite-abelian notion: for arbitrary \(g_1,\ldots,g_r\in G_N\) and \(z_1,\ldots,z_r\in\mathbb C\),
\[
\sum_{j,k=1}^{r}f(g_j-g_k)z_j\overline{z_k}\ge0.
\]
Equivalently, the Fourier transform \(\widehat f(u,v)=\sum_g f(g)\exp[-2\pi i(ug_1+vg_2)/N]\) is real and nonnegative at every \((u,v)\in G_N\). Positivity forces \(f(-g)=\overline{f(g)}\). The mass is \(\widehat f(0,0)\), **without** division by \(N^2\). Write \(e_3=e_1-e_2\), \(f(e_j)=a_j+i b_j\), \(\theta_j=2\pi j/N\); then precisely
\[
\widehat f(u,v)=1+2\left[a_1\cos\theta_u+a_2\cos\theta_v+a_3\cos\theta_{u-v}
+b_1\sin\theta_u+b_2\sin\theta_v+b_3\sin\theta_{u-v}\right].
\]
The optimizer face when \(3\mid N\) is thus described by the two displayed real equalities together with \(\widehat f(u,v)\ge0\) for all \((u,v)\in G_N\). There are no hidden positivity, regularity, or integrality assumptions. This is an exact finite-dimensional convex optimization theorem; no assertion is made for differently supported functions.

## Proof
**1. Rotation reduction and the Fourier minimum.** The lattice automorphism \(R(e_1)=e_2\), \(R(e_2)=e_2-e_1\) cyclically permutes the six nonzero support vectors. Averaging any feasible \(f\) over its six rotations preserves \(f(0)\), positive definiteness, support, and total mass. The averaged function takes a single **real** value \(a\) on all six vectors, and its Fourier transform equals
\[
P_a(u,v)=1+2a S_N(u,v),\qquad S_N(u,v)=\cos\theta_u+\cos\theta_v+\cos\theta_{u-v}.
\]
Because \(S_N(0,0)=3\), and because the minimum \(\sigma_N=\min_{u,v}S_N(u,v)\) is negative, feasibility implies \(a\le -1/(2\sigma_N)\). Taking equality gives nonnegative Fourier transform at every frequency: when \(S_N\le0\) this follows from its defining minimum; when \(S_N>0\) it is immediate because \(a>0\). The mass is \(1+6a\), hence \(\mathcal T_N=1-3/\sigma_N\). The symmetry average gives a matching upper bound for **all** functions, including complex ones.

**2. Exact discrete minimum and every contact.** Given \(u,v\), use symmetry of \(S_N\) to take \(0\le u\le v<N\). Its three arguments are the cyclic gaps \((u,v-u,N-v)\), so
\[
S_N(u,v)=\cos(2\pi g_1/N)+\cos(2\pi g_2/N)+\cos(2\pi g_3/N),\qquad g_1+g_2+g_3=N.
\]
Conversely every nonnegative integer gap triple with positive last gap arises; a triple with zero last gap can be cyclically rotated to one with positive last gap without changing the cosine sum. Sort the gaps as \(a\le b\le c\). If \(c-a\ge2\), shifting the extreme gaps inward gives the exact identity
\[
\begin{aligned}
&\cos\frac{2\pi(a+1)}N+\cos\frac{2\pi(c-1)}N-\cos\frac{2\pi a}N-\cos\frac{2\pi c}N\\
&\qquad=-4\sin\frac\pi N\,\cos\frac{\pi b}N\,\sin\frac{\pi(c-a-1)}N.
\end{aligned}
\]
If \(b<N/2\), this is **strictly negative**. As \(a+b+c=N\), the only case with \(b\ge N/2\) is \((a,b,c)=(0,N/2,N/2)\) at even order. Its first inward shift is neutral, but for \(N\ge6\) the resulting triple \((1,N/2-1,N/2)\) has a second strict inward shift, so the exceptional triple is not minimal. Consequently the only minima are gap triples whose entries differ by at most one. At orders \(N=3q\), \(3q+1\), and \(3q+2\) they have respectively multisets \((q,q,q)\), \((q,q,q+1)\), and \((q,q+1,q+1)\), yielding the stated formula for \(\sigma_N\). In frequency coordinates the complete minimizing sets are
\[
\begin{array}{ll}
N=3q:&\{(q,2q),(2q,q)\},\\
N=3q+1:& \pm\{(q,2q),(q,2q+1),(q+1,2q+1)\},\\
N=3q+2:& \pm\{(q,2q+1),(q+1,2q+1),(q+1,2q+2)\},
\end{array}
\]
with both signs interpreted componentwise modulo \(N\). The sets have exactly two or six distinct members. The exact identity
\[\left|1+e^{i\theta_u}+e^{i\theta_v}\right|^2=3+2S_N(u,v)\]
shows \(S_N\ge-3/2\), with equality only when the two nontrivial phases are the distinct primitive cube roots of unity. This occurs in the finite grid precisely when \(3\mid N\). Thus the equal-gap value is \(-3/2\), and all nonresonant values strictly exceed it. Finally the average of \(S_N\) over every frequency is zero, whereas \(S_N(0,0)=3\), so \(\sigma_N<0\). The mass claims follow.

**3. All optimal functions vanish at the minimum modes.** For any optimal function, its rotation average equals the constructed invariant optimizer, since the mass fixes its averaged coefficient. At any minimizing frequency \(\xi\), the averaged Fourier transform is zero. This average is a mean of nonnegative real Fourier values \(\widehat f(R^j\xi)\). Therefore every one of the minimum-mode Fourier values of the original optimizer vanishes. This also follows by averaging the Fourier inequalities over their orbit.

**4. Unique complex optimizer away from resonance.** Suppose \(N\not\equiv0\pmod3\). Choose the three positive modes from Step 2; vanishing at these and their negatives gives three equations for \((a_1,a_2,a_3)\) and independently three for \((b_1,b_2,b_3)\). Put \(A=\cos\theta_q\), \(B=\cos\theta_{q+1}\), \(s=\sin\theta_q\), \(t=\sin\theta_{q+1}\). When \(N=3q+1\), the cosine and sine coefficient matrices, respectively, are
\[
\begin{pmatrix}A&B&A\\A&A&B\\B&A&A\end{pmatrix},\qquad
\begin{pmatrix}s&-t&-s\\s&-s&-t\\t&-s&-s\end{pmatrix}.
\]
Their determinants equal \((A-B)^2(2A+B)\) and \((s-t)^2(2s+t)\). When \(N=3q+2\), the matrices are
\[
\begin{pmatrix}A&B&B\\B&B&A\\B&A&B\end{pmatrix},\qquad
\begin{pmatrix}s&-t&-t\\t&-t&-s\\t&-s&-t\end{pmatrix},
\]
with determinants \(-(A-B)^2(A+2B)\) and \(-(s-t)^2(s+2t)\). In all cases \(A\ne B\), \(s\ne t\), \(s,t>0\), and the relevant cosine linear factor is \(\sigma_N<0\), hence both matrices are invertible. The sine equations force all \(b_j=0\); the cosine equations force all \(a_j=-1/(2\sigma_N)\). Thus the optimizer is unique without imposing symmetry.

**5. Complete optimizer face at resonance.** If \(N=3q\), the only minimizing frequencies are \((q,2q)\) and its negative. Their two zero constraints are exactly
\[
a_1+a_2+a_3=1,\qquad b_1-b_2-b_3=0.
\]
Conversely any six-real-parameter supported function satisfying these equalities and every remaining Fourier positivity inequality has mass \(1+2\sum a_j=3\), so is optimal. The invariant optimum \(a_1=a_2=a_3=1/3\), \(b_1=b_2=b_3=0\) has **strictly** positive Fourier transform at every non-minimizing mode, by Step 2. A small four-dimensional Euclidean neighborhood within the two-constraint affine space is therefore feasible. Hence the full optimizer face has relative affine dimension four.

**6. Sharp residue correction.** For \(N\not\equiv0\pmod3\) set \(h=2\pi/(3N)\). Taylor expansion at \(2\pi/3\) gives
\[
\sigma_N=-\frac32+\frac32 h^2+\varepsilon_N\frac{\sqrt3}{2}h^3+O(h^4).
\]
Expanding \(1-3/\sigma_N\) yields the stated quadratic and signed cubic terms with a uniform \(O(N^{-4})\) remainder across the two residue classes. This finishes the proof.

## Verification
The standalone `checker.py` reconstructs all Fourier values directly from the six real coefficients and independently enumerates **every** pair \((u,v)\) for every integer \(5\le N\le90\). It checks all minimizing frequencies and their exact counts, the positivity and exact zeros of the predicted invariant optimizer, and the mass bound. This amounts to **247,035 Fourier inequalities**. When NumPy and SciPy are installed, it independently optimizes all six real Fourier coefficients by linear programming for each \(5\le N\le21\), checking both the exact optimum and uniqueness of the optimizer away from resonance; all 17 LP tests passed in the recorded run. It separately checks the signed cubic asymptotic formula at large orders. Run `python checker.py` from the directory containing this file; success prints `CHECK_PASS orders=5..90 grid_modes= 86 Fourier_inequalities= 247035 LP_instances= 17` with the optional dependencies installed. **Finite tests are corroboration only:** the exact all-order claims are proved by the balancing identity, the Fourier nonnegativity argument, the explicit determinant tests, and Taylor expansion above.

## Relationship to prior work
Kolountzakis and Révész (2003) formulate the general Turán extremal problem on finite abelian groups and give spectral/packing upper bounds (particularly their Theorems 2 and 4). Their general spectral construction explains the resonant three-point packing benchmark \(\mathcal T_N=3\) but does not identify the nonresonant masses, their uniquely complex extremal functions, or the face-dimension jump. Ivanov and Ivanov (2010) study periodic positive-definite Turán questions in one dimension, not this two-dimensional triangular support. The general Lovász theta/Hoffman eigenvalue formula for vertex- and edge-transitive graphs also explains why a least-adjacency-eigenvalue bound is exact for the invariant mass: that spectral optimization principle is **not claimed as new**. The explicit root-hexagon minimum and especially the full unrestricted-complex optimizer-face theorem constitute the specialization under study. John and Sachs (2009) study toroidal graph spectra, an important possible source for the discrete cosine minimum; the retrieved descriptions do not establish the present supported-positive-definite optimization or optimizer faces. Published results for a thirteen-point Lee ball on a square torus and for one-dimensional five-point supports involve distinct supports and Fourier constraints. The mass formula can be interpreted as an invariant Fourier/adjacency spectral-minimum optimization, but the assertion that **all** complex optimizers are unique off resonance and form an exact four-dimensional face at resonance requires the full Fourier-contact analysis in Steps 3–5.

## Limitations
The support must be exactly the seven-point root hexagon, and the two torus side lengths must agree. No result is claimed for triangular tori of unequal periods, larger hexagonal balls, or the complete adjacency spectrum. The asymptotic error term is asserted only along the nonzero residue classes; on multiples of three the mass equals three identically. The uniqueness statement concerns functions normalized by \(f(0)=1\), including complex-valued functions; a different normalization changes numeric values. Older finite-graph spectral computations or a multidimensional Turán calculation may contain an equivalent result: the accessible search and inspection cannot prove global novelty. In particular, the full text of the older *Spectra of toroidal graphs* preprint and of the continuous-hexagon Turán paper by Arestov and Berdysheva could not be examined; both remain named literature risks. The checker uses numerical tolerances and does not replace the analytic proof.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218v1, first public 2003-12-10, especially Theorems 2 and 4 and Section 4. https://arxiv.org/abs/math/0312218
2. V. I. Ivanov and A. V. Ivanov, *Turán problems for periodic positive definite functions*, 2010, full text https://ac.inf.elte.hu/Vol_033_2010/doi/219_33.pdf.
3. P. E. John and H. Sachs, *Spectra of toroidal graphs*, Discrete Mathematics 309 (2009), 2663–2681, DOI 10.1016/j.disc.2008.06.034.
4. I. S. Arestov and E. E. Berdysheva, *Turán's problem for positive definite functions with supports in a hexagon*, 2001; earlier continuous-domain hexagonal geometry, full text not verified.
5. I. Sason, *Observations on the Lovász \(\theta\)-Function, Graph Capacity, Eigenvalues, and Strong Products*, arXiv:2301.02820, 2023, graph eigenvalue bounds and their edge-transitive equality cases; relevant general spectral comparison.
6. S. Gy. Révész, *Turán's extremal problem on locally compact abelian groups*, arXiv:0904.1824v1, 2009; general survey.
